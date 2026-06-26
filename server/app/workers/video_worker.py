from __future__ import annotations

import json
import os
import queue
import re
import shlex
import shutil
import subprocess
import threading
import time
from pathlib import Path
from typing import Any

from sqlalchemy import text

from server.app.domains.media.processing_queue import (
    WorkerJob,
    claim_next_job,
    fail_job,
    finish_job,
    load_processing_asset,
    mark_asset_playback_ready,
    persist_duplicate_candidate,
    persist_learning_rendition,
    persist_thumbnail,
    persist_video_fingerprint,
    persist_video_probe,
    queue_legacy_backfill,
    relative_media_path,
    update_phase,
)
from server.app.infrastructure.settings import get_settings
from server.app.infrastructure.database import db_session
from server.app.domains.media.files import checksum_sha256_file


TRANSCODE_PROGRESS_START = 60
TRANSCODE_PROGRESS_END = 76
FFMPEG_IDLE_TIMEOUT_SECONDS = 120
_NVENC_PROBE_CACHE: tuple[bool, str | None] | None = None


def _media_path(relative_path: str) -> Path:
    root = get_settings().media_root.resolve()
    path = (root / relative_path).resolve()
    if root != path and root not in path.parents:
        raise RuntimeError("Media path escapes media root")
    return path


class JobCancelled(RuntimeError):
    pass


def _job_active(job: WorkerJob) -> bool:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    SELECT mpj.status AS job_status,
                           COALESCE(ma.lifecycle_status, 'active') AS lifecycle_status
                    FROM media_processing_jobs mpj
                    JOIN media_assets ma ON ma.id = mpj.media_asset_id
                    WHERE mpj.id = CAST(:job_id AS uuid)
                    """
                ),
                {"job_id": job.id},
            )
            .mappings()
            .first()
        )
    return bool(row and row["job_status"] == "processing" and row["lifecycle_status"] == "active")


def _ensure_job_active(job: WorkerJob) -> None:
    if not _job_active(job):
        raise JobCancelled("Media processing job was cancelled or asset was deleted")


def _duration_tolerance_seconds(duration_seconds: float | None) -> float | None:
    if duration_seconds is None or duration_seconds <= 0:
        return None
    settings = get_settings()
    return max(
        settings.video_duplicate_detection_duration_tolerance_floor_seconds,
        min(
            settings.video_duplicate_detection_duration_tolerance_ceiling_seconds,
            duration_seconds * settings.video_duplicate_detection_duration_tolerance_ratio,
        ),
    )


def _effective_duplicate_sample_interval(duration_seconds: float | None) -> float:
    settings = get_settings()
    default_interval = settings.video_duplicate_detection_default_interval_seconds
    if duration_seconds is None or duration_seconds <= 0:
        return default_interval
    min_samples = max(1, int(settings.video_duplicate_detection_min_samples))
    return min(
        default_interval,
        max(settings.video_duplicate_detection_min_interval_seconds, duration_seconds / min_samples),
    )



def _run(command: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    if result.returncode != 0:
        stderr = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(stderr[:1000] or f"Command failed: {' '.join(command)}")
    return result


def verify_required_tools() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe") if not shutil.which(name)]
    if missing:
        raise RuntimeError(f"Missing required video tool(s): {', '.join(missing)}")


def _transcode_acceleration_mode() -> str:
    mode = get_settings().video_transcode_acceleration.lower()
    if mode not in {"auto", "cpu", "nvenc"}:
        raise RuntimeError("VIDEO_TRANSCODE_ACCELERATION must be auto, cpu, or nvenc")
    return mode


def _probe_nvenc() -> tuple[bool, str | None]:
    global _NVENC_PROBE_CACHE
    if _NVENC_PROBE_CACHE is not None:
        return _NVENC_PROBE_CACHE
    command = [
        "ffmpeg",
        "-hide_banner",
        "-f",
        "lavfi",
        "-i",
        "testsrc2=size=640x360:rate=30",
        "-t",
        "0.5",
        "-c:v",
        "h264_nvenc",
        "-f",
        "null",
        "-",
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, check=False)
    except Exception as exc:
        _NVENC_PROBE_CACHE = (False, str(exc)[:500])
        return _NVENC_PROBE_CACHE
    if result.returncode == 0:
        _NVENC_PROBE_CACHE = (True, None)
    else:
        diagnostic = (result.stderr or result.stdout or "h264_nvenc probe failed").strip()
        _NVENC_PROBE_CACHE = (False, diagnostic[:500])
    return _NVENC_PROBE_CACHE


def _select_encoder_policy() -> dict[str, Any]:
    mode = _transcode_acceleration_mode()
    if mode == "cpu":
        return {
            "acceleration_mode": mode,
            "encoder": "libx264",
            "hardware_acceleration": "cpu",
            "fallback": False,
            "nvenc_probe": {"attempted": False},
        }
    if mode == "nvenc":
        return {
            "acceleration_mode": mode,
            "encoder": "h264_nvenc",
            "hardware_acceleration": "nvenc",
            "fallback": False,
            "nvenc_probe": {"attempted": False},
        }
    available, reason = _probe_nvenc()
    if available:
        return {
            "acceleration_mode": mode,
            "encoder": "h264_nvenc",
            "hardware_acceleration": "nvenc",
            "fallback": False,
            "nvenc_probe": {"attempted": True, "available": True},
        }
    return {
        "acceleration_mode": mode,
        "encoder": "libx264",
        "hardware_acceleration": "cpu",
        "fallback": True,
        "fallback_stage": "probe",
        "fallback_reason": reason or "h264_nvenc probe failed",
        "nvenc_probe": {"attempted": True, "available": False, "reason": reason},
    }


def _encoder_args(encoder: str) -> list[str]:
    settings = get_settings()
    if encoder == "h264_nvenc":
        return [
            "-c:v",
            "h264_nvenc",
            "-pix_fmt",
            "yuv420p",
            "-profile:v",
            "main",
            "-preset",
            "p4",
            "-cq",
            str(settings.video_learning_crf),
            "-b:v",
            "0",
        ]
    return [
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-preset",
        "medium",
        "-crf",
        str(settings.video_learning_crf),
    ]


def _even_dimension(value: float) -> int:
    rounded = max(2, round(value))
    return rounded if rounded % 2 == 0 else rounded + 1


def _target_dimensions(width: int, height: int) -> tuple[int, int] | None:
    settings = get_settings()
    if width <= 0 or height <= 0 or width <= settings.video_learning_max_width:
        return None
    target_width = settings.video_learning_max_width
    target_height = _even_dimension(target_width * height / width)
    return target_width, target_height


def _cuvid_decoder(codec: str | None) -> str | None:
    normalized = str(codec or "").lower()
    if normalized in {"hevc", "h265"}:
        return "hevc_cuvid"
    if normalized in {"h264", "avc1"}:
        return "h264_cuvid"
    return None


def _gpu_input_args(encoder: str, metadata: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if encoder != "h264_nvenc":
        return [], {"hardware_decoding": "cpu", "hardware_scaling": "cpu"}
    width = int(metadata.get("width") or 0)
    height = int(metadata.get("height") or 0)
    target = _target_dimensions(width, height)
    decoder = _cuvid_decoder(str(metadata.get("video_codec") or ""))
    if not decoder:
        return [], {"hardware_decoding": "cpu", "hardware_scaling": "cpu"}
    args = ["-c:v", decoder]
    policy: dict[str, Any] = {
        "hardware_decoding": "nvdec",
        "hardware_scaling": "none",
        "decoder": decoder,
    }
    if not target:
        return args, policy
    target_width, target_height = target
    args.extend(["-resize", f"{target_width}x{target_height}"])
    policy.update(
        {
            "hardware_scaling": "cuvid_resize",
            "target_width": target_width,
            "target_height": target_height,
        }
    )
    return (
        args,
        policy,
    )


def _parse_ffmpeg_timestamp(value: str) -> float | None:
    value = value.strip()
    if not value:
        return None
    if ":" not in value:
        try:
            return float(value)
        except ValueError:
            return None
    parts = value.split(":")
    if len(parts) != 3:
        return None
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
    except ValueError:
        return None
    return hours * 3600 + minutes * 60 + seconds


def _ffmpeg_progress_value(line: str, duration_seconds: float | None) -> int | None:
    if not duration_seconds or duration_seconds <= 0 or "=" not in line:
        return None
    key, value = line.strip().split("=", 1)
    elapsed_seconds: float | None = None
    if key in {"out_time_ms", "out_time_us"}:
        try:
            elapsed_seconds = float(value) / 1_000_000
        except ValueError:
            return None
    elif key == "out_time":
        elapsed_seconds = _parse_ffmpeg_timestamp(value)
    if elapsed_seconds is None:
        return None
    ratio = max(0.0, min(1.0, elapsed_seconds / duration_seconds))
    span = TRANSCODE_PROGRESS_END - TRANSCODE_PROGRESS_START
    return max(TRANSCODE_PROGRESS_START, min(TRANSCODE_PROGRESS_END, round(TRANSCODE_PROGRESS_START + span * ratio)))


def _run_ffmpeg_with_progress(command: list[str], job: WorkerJob, duration_seconds: float | None) -> None:
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )
    line_queue: queue.Queue[str | None] = queue.Queue()

    def read_output() -> None:
        assert process.stdout is not None
        try:
            for raw in process.stdout:
                line_queue.put(raw)
        finally:
            line_queue.put(None)

    reader = threading.Thread(target=read_output, daemon=True)
    reader.start()
    last_progress = TRANSCODE_PROGRESS_START
    last_update = time.monotonic()
    last_output = time.monotonic()
    output_tail: list[str] = []
    stdout_closed = False
    while True:
        if not _job_active(job):
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=10)
            raise JobCancelled("Media processing job was cancelled or asset was deleted")
        try:
            raw_line = line_queue.get(timeout=1)
        except queue.Empty:
            if process.poll() is not None and (stdout_closed or line_queue.empty()):
                break
            if time.monotonic() - last_output > FFMPEG_IDLE_TIMEOUT_SECONDS:
                process.kill()
                process.wait(timeout=10)
                raise RuntimeError(f"FFmpeg produced no progress output for {FFMPEG_IDLE_TIMEOUT_SECONDS} seconds")
            continue
        if raw_line is None:
            stdout_closed = True
            if process.poll() is not None:
                break
            continue
        last_output = time.monotonic()
        line = raw_line.strip()
        if line:
            output_tail.append(line)
            output_tail = output_tail[-60:]
        progress = _ffmpeg_progress_value(line, duration_seconds)
        if progress is None or progress <= last_progress:
            continue
        now = time.monotonic()
        if progress - last_progress >= 2 or now - last_update >= 1:
            update_phase(job, "transcoding", progress=progress)
            last_progress = progress
            last_update = now
        if process.poll() is not None and line_queue.empty():
            break
    return_code = process.wait()
    reader.join(timeout=2)
    if return_code != 0:
        diagnostic = "\n".join(output_tail).strip()
        raise RuntimeError(diagnostic[-1000:] or f"Command failed: {' '.join(command)}")
    if last_progress < TRANSCODE_PROGRESS_END:
        _ensure_job_active(job)
        update_phase(job, "transcoding", progress=TRANSCODE_PROGRESS_END)












def _probe(source: Path) -> dict[str, Any]:
    result = _run(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(source),
        ],
        timeout=120,
    )
    payload = json.loads(result.stdout or "{}")
    streams = payload.get("streams") or []
    video = next((stream for stream in streams if stream.get("codec_type") == "video"), {})
    audio = next((stream for stream in streams if stream.get("codec_type") == "audio"), {})
    subtitle_stream_count = sum(1 for stream in streams if stream.get("codec_type") == "subtitle")
    attachment_stream_count = sum(1 for stream in streams if stream.get("codec_type") == "attachment")
    data_stream_count = sum(1 for stream in streams if stream.get("codec_type") == "data")
    duration = video.get("duration") or (payload.get("format") or {}).get("duration")
    fps = _parse_rate(video.get("avg_frame_rate") or video.get("r_frame_rate"))
    return {
        "duration_seconds": float(duration) if duration else None,
        "width": int(video["width"]) if video.get("width") else None,
        "height": int(video["height"]) if video.get("height") else None,
        "fps": fps,
        "bitrate": int((payload.get("format") or {}).get("bit_rate")) if (payload.get("format") or {}).get("bit_rate") else None,
        "video_codec": video.get("codec_name"),
        "audio_codec": audio.get("codec_name"),
        "embedded_subtitle_stream_count": subtitle_stream_count,
        "attachment_stream_count": attachment_stream_count,
        "data_stream_count": data_stream_count,
        "rotation": _rotation(video),
    }


def _parse_rate(value: str | None) -> float | None:
    if not value or value == "0/0":
        return None
    if "/" in value:
        numerator, denominator = value.split("/", 1)
        try:
            return float(numerator) / float(denominator)
        except (ValueError, ZeroDivisionError):
            return None
    try:
        return float(value)
    except ValueError:
        return None


def _rotation(video_stream: dict[str, Any]) -> int | None:
    tags = video_stream.get("tags") or {}
    if tags.get("rotate"):
        try:
            return int(tags["rotate"])
        except ValueError:
            return None
    for item in video_stream.get("side_data_list") or []:
        if "rotation" in item:
            try:
                return int(item["rotation"])
            except (TypeError, ValueError):
                return None
    return None




def _thumbnail(job: WorkerJob, source: Path, tmp_dir: Path, duration: float | None) -> Path:
    thumb = tmp_dir / "poster.jpg"
    seek = "1"
    if duration and duration > 15:
        seek = str(min(max(duration * 0.1, 2), 10))
    _run(
        [
            "ffmpeg",
            "-y",
            "-ss",
            seek,
            "-i",
            str(source),
            "-vf",
            "thumbnail,scale=640:-2",
            "-frames:v",
            "1",
            str(thumb),
        ],
        timeout=180,
    )
    if not thumb.exists() or thumb.stat().st_size <= 0:
        raise RuntimeError("FFmpeg did not produce a thumbnail")
    final = get_settings().media_root / "thumbnails" / f"{job.media_asset_id}.jpg"
    final.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(thumb), final)
    return final


def _needs_transcode(source: Path, asset: dict[str, Any], metadata: dict[str, Any]) -> bool:
    settings = get_settings()
    threshold = settings.video_learning_transcode_threshold_mb * 1024 * 1024
    if int(asset.get("file_size_bytes") or 0) > threshold:
        return True
    if source.suffix.lower() != ".mp4":
        return True
    if str(metadata.get("video_codec") or "").lower() not in {"h264", "avc1"}:
        return True
    audio_codec = str(metadata.get("audio_codec") or "").lower()
    if audio_codec and audio_codec not in {"aac", "mp4a"}:
        return True
    width = metadata.get("width")
    return bool(width and int(width) > settings.video_learning_max_width)


def _learning_rendition(
    job: WorkerJob,
    source: Path,
    asset: dict[str, Any],
    metadata: dict[str, Any],
    tmp_dir: Path,
) -> tuple[Path, dict[str, Any]]:
    settings = get_settings()
    output = tmp_dir / "learning.mp4"
    width = int(metadata.get("width") or 0)
    height = int(metadata.get("height") or 0)
    duration_seconds = float(metadata.get("duration_seconds") or 0) or None
    should_transcode = _needs_transcode(source, asset, metadata)
    policy: dict[str, Any] = {
        "kind": "learning-720p" if should_transcode else "learning-remux",
        "transcoded": should_transcode,
        "source_width": width or None,
        "source_height": height or None,
        "source_duration_seconds": duration_seconds,
        "acceleration_mode": _transcode_acceleration_mode(),
        "fallback": False,
    }

    def build_command(encoder: str) -> list[str]:
        gpu_input_args, gpu_policy = _gpu_input_args(encoder, metadata)
        policy.update(gpu_policy)
        command = [
            "ffmpeg",
            "-y",
            "-progress",
            "pipe:1",
            "-nostats",
            *gpu_input_args,
            "-i",
            str(source),
            "-map",
            "0:v:0",
            "-map",
            "0:a:0?",
            "-sn",
            "-dn",
            "-map_chapters",
            "-1",
            "-map_metadata",
            "-1",
        ]
        if width and width > settings.video_learning_max_width and not gpu_input_args:
            command.extend(["-vf", f"scale={settings.video_learning_max_width}:-2"])
        command.extend(["-r", str(settings.video_learning_max_fps)])
        command.extend(_encoder_args(encoder))
        command.extend(["-c:a", "aac", "-ac", "2", "-b:a", "128k", "-movflags", "+faststart", str(output)])
        return command

    def build_remux_command() -> list[str]:
        return [
            "ffmpeg",
            "-y",
            "-progress",
            "pipe:1",
            "-nostats",
            "-i",
            str(source),
            "-map",
            "0:v:0",
            "-map",
            "0:a:0?",
            "-sn",
            "-dn",
            "-map_chapters",
            "-1",
            "-map_metadata",
            "-1",
            "-c",
            "copy",
            "-movflags",
            "+faststart",
            str(output),
        ]

    if should_transcode:
        encoder_policy = _select_encoder_policy()
        policy.update(encoder_policy)
        try:
            _run_ffmpeg_with_progress(build_command(str(encoder_policy["encoder"])), job, duration_seconds)
        except RuntimeError as exc:
            if encoder_policy.get("acceleration_mode") != "auto" or encoder_policy.get("encoder") != "h264_nvenc":
                raise
            output.unlink(missing_ok=True)
            fallback_reason = str(exc)[:500]
            policy.update(
                {
                    "encoder": "libx264",
                    "hardware_acceleration": "cpu",
                    "fallback": True,
                    "fallback_stage": "transcode",
                    "fallback_reason": fallback_reason,
                    "fallback_from_encoder": "h264_nvenc",
                }
            )
            _run_ffmpeg_with_progress(build_command("libx264"), job, duration_seconds)
    else:
        policy.update(
            {
                "encoder": "copy",
                "hardware_acceleration": "none",
                "nvenc_probe": {"attempted": False},
            }
        )
        _run_ffmpeg_with_progress(build_remux_command(), job, duration_seconds)
    if not output.exists() or output.stat().st_size <= 0:
        raise RuntimeError("FFmpeg did not produce a learning rendition")
    final = get_settings().media_root / "renditions" / str(asset["id"]) / "learning.mp4"
    final.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(output), final)
    return final, policy






def _generate_fingerprint(
    asset_id: str,
    source: Path,
    tmp_dir: Path,
    *,
    source_kind: str,
    duration_seconds: float | None,
) -> dict[str, Any]:
    settings = get_settings()
    algorithm = settings.video_similarity_algorithm
    effective_interval = _effective_duplicate_sample_interval(duration_seconds)
    fingerprint_metadata = {
        "source": source_kind,
        "source_relative_path": relative_media_path(source),
        "duration_seconds": duration_seconds,
        "seconds_per_hash": effective_interval,
        "duplicate_detection": {
            "default_interval_seconds": settings.video_duplicate_detection_default_interval_seconds,
            "min_samples": settings.video_duplicate_detection_min_samples,
            "min_interval_seconds": settings.video_duplicate_detection_min_interval_seconds,
        },
    }
    if duration_seconds is None or duration_seconds <= 0:
        persist_video_fingerprint(
            asset_id,
            algorithm=algorithm,
            status="skipped",
            relative_path=None,
            signature_hash=None,
            metadata={**fingerprint_metadata, "reason": "duration_unavailable"},
        )
        return {
            "status": "skipped",
            "algorithm": algorithm,
            "source": source_kind,
            "reason": "duration_unavailable",
            "seconds_per_hash": effective_interval,
        }
    if not settings.video_similarity_command:
        persist_video_fingerprint(
            asset_id,
            algorithm=algorithm,
            status="skipped",
            relative_path=None,
            signature_hash=None,
            metadata={**fingerprint_metadata, "reason": "duplicate detection command not configured"},
        )
        return {
            "status": "skipped",
            "algorithm": algorithm,
            "source": source_kind,
            "reason": "duplicate detection command not configured",
            "seconds_per_hash": effective_interval,
        }
    output = tmp_dir / "video-signature.bin"
    command_text = settings.video_similarity_command.format(
        input=str(source),
        output=str(output),
        seconds_per_hash=f"{effective_interval:.6f}",
    )
    _run(shlex.split(command_text), timeout=None)
    if not output.exists() or output.stat().st_size <= 0:
        raise RuntimeError("Configured video duplicate-detection command did not produce a signature")
    final = get_settings().media_root / "fingerprints" / asset_id / output.name
    final.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(output), final)
    signature_hash = checksum_sha256_file(final)
    persist_video_fingerprint(
        asset_id,
        algorithm=algorithm,
        status="ready",
        relative_path=relative_media_path(final),
        signature_hash=signature_hash,
        metadata={**fingerprint_metadata, "command": settings.video_similarity_command},
    )
    return {
        "status": "ready",
        "algorithm": algorithm,
        "relative_path": relative_media_path(final),
        "source": source_kind,
        "seconds_per_hash": effective_interval,
    }




def _compare_fingerprints(asset_id: str) -> list[dict[str, Any]]:
    settings = get_settings()
    if not settings.video_similarity_compare_command:
        return []
    with db_session() as session:
        current = (
            session.execute(
                text(
                    """
                    SELECT mvf.relative_path, mvf.algorithm, ma.duration_seconds
                    FROM media_video_fingerprints mvf
                    JOIN media_assets ma ON ma.id = mvf.media_asset_id
                    WHERE mvf.media_asset_id = CAST(:asset_id AS uuid)
                      AND mvf.status = 'ready'
                      AND ma.upload_status = 'ready'
                      AND COALESCE(ma.lifecycle_status, 'active') = 'active'
                      AND ma.duration_seconds IS NOT NULL
                    ORDER BY mvf.created_at DESC
                    LIMIT 1
                    """
                ),
                {"asset_id": asset_id},
            )
            .mappings()
            .first()
        )
        current_duration = float(current["duration_seconds"]) if current and current.get("duration_seconds") else None
        tolerance = _duration_tolerance_seconds(current_duration)
        if not current or current_duration is None or tolerance is None:
            return []
        candidates = session.execute(
            text(
                """
                SELECT mvf.media_asset_id, mvf.relative_path, mvf.algorithm, ma.duration_seconds
                FROM media_video_fingerprints mvf
                JOIN media_assets ma ON ma.id = mvf.media_asset_id
                WHERE mvf.media_asset_id <> CAST(:asset_id AS uuid)
                  AND mvf.status = 'ready'
                  AND mvf.algorithm = :algorithm
                  AND ma.upload_status = 'ready'
                  AND COALESCE(ma.lifecycle_status, 'active') = 'active'
                  AND ma.duration_seconds IS NOT NULL
                  AND ABS(ma.duration_seconds - CAST(:duration_seconds AS numeric)) <= CAST(:duration_tolerance AS numeric)
                ORDER BY mvf.created_at ASC
                """
            ),
            {
                "asset_id": asset_id,
                "algorithm": current["algorithm"],
                "duration_seconds": current_duration,
                "duration_tolerance": tolerance,
            },
        ).mappings().all()
    matches: list[dict[str, Any]] = []
    current_path = _media_path(current["relative_path"])
    for candidate in candidates:
        candidate_path = _media_path(candidate["relative_path"])
        command_text = settings.video_similarity_compare_command.format(
            current=str(current_path),
            candidate=str(candidate_path),
        )
        result = _run(shlex.split(command_text), timeout=None)
        score = _parse_score(result.stdout)
        if score is not None and score >= settings.video_duplicate_detection_threshold:
            candidate_duration = float(candidate["duration_seconds"]) if candidate.get("duration_seconds") else None
            match = {
                "candidate_asset_id": str(candidate["media_asset_id"]),
                "score": score,
                "algorithm": candidate["algorithm"],
                "metadata": {
                    "current_duration_seconds": current_duration,
                    "candidate_duration_seconds": candidate_duration,
                    "duration_tolerance_seconds": tolerance,
                    "threshold": settings.video_duplicate_detection_threshold,
                    "comparison_scope": "full_video_duration_gated_duplicate",
                },
            }
            persist_duplicate_candidate(asset_id, match)
            matches.append(match)
    return matches


def _parse_score(output: str) -> float | None:
    match = re.search(r"[-+]?\d*\.?\d+", output or "")
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def _run_duplicate_detection_steps(
    job: WorkerJob,
    fingerprint_source: Path,
    tmp_dir: Path,
    *,
    source_kind: str,
    duration_seconds: float | None,
) -> tuple[dict[str, Any], list[dict[str, Any]]] | None:
    try:
        _ensure_job_active(job)
        update_phase(job, "fingerprinting", metadata={"playback_ready": job.preserves_ready_playback})
        _ensure_job_active(job)
        fingerprint = _generate_fingerprint(
            job.media_asset_id,
            fingerprint_source,
            tmp_dir,
            source_kind=source_kind,
            duration_seconds=duration_seconds,
        )

        _ensure_job_active(job)
        update_phase(job, "comparing", metadata={"playback_ready": job.preserves_ready_playback})
        _ensure_job_active(job)
        matches = _compare_fingerprints(job.media_asset_id) if fingerprint.get("status") == "ready" else []
        return fingerprint, matches
    except JobCancelled:
        raise
    except Exception as exc:
        fail_job(job, f"Duplicate detection failed: {exc}", preserve_ready_playback=True)
        return None




def process_job(job: WorkerJob) -> None:
    tmp_dir = get_settings().media_root / "tmp" / job.id
    tmp_dir.mkdir(parents=True, exist_ok=True)
    try:
        update_phase(job, "validating")
        _ensure_job_active(job)
        asset = load_processing_asset(job.media_asset_id)
        if job.duplicate_detection_only:
            playback_relative_path = asset.get("playback_relative_path")
            if not playback_relative_path:
                raise RuntimeError("Playback media file is missing")
            rendition = _media_path(str(playback_relative_path))
            if not rendition.exists():
                raise RuntimeError("Playback media file is missing")
            _ensure_job_active(job)
            duplicate_detection = _run_duplicate_detection_steps(
                job,
                rendition,
                tmp_dir,
                source_kind="learning_rendition",
                duration_seconds=asset.get("duration_seconds"),
            )
            if duplicate_detection is None:
                return
            fingerprint, matches = duplicate_detection
            _ensure_job_active(job)
            finish_job(
                job,
                {
                    "retry_scope": "duplicate_detection",
                    "rendition": relative_media_path(rendition),
                    "fingerprint": fingerprint,
                    "duplicate_candidates": matches,
                },
            )
            return

        source = _media_path(asset.get("source_relative_path") or asset["relative_path"])
        if not source.exists():
            raise RuntimeError("Source media file is missing")
        digest = checksum_sha256_file(source)
        if asset.get("checksum_sha256") and str(asset["checksum_sha256"]).lower() != digest.lower():
            raise RuntimeError("Source media checksum does not match media asset record")

        update_phase(job, "probing")
        _ensure_job_active(job)
        probe = _probe(source)
        _ensure_job_active(job)
        persist_video_probe(job.media_asset_id, probe)

        update_phase(job, "thumbnailing")
        _ensure_job_active(job)
        thumb = _thumbnail(job, source, tmp_dir, probe.get("duration_seconds"))
        _ensure_job_active(job)
        persist_thumbnail(job.media_asset_id, thumb)

        update_phase(job, "transcoding")
        _ensure_job_active(job)
        rendition, policy = _learning_rendition(job, source, asset, probe, tmp_dir)
        _ensure_job_active(job)
        rendition_probe = _probe(rendition)
        _ensure_job_active(job)
        persist_learning_rendition(job.media_asset_id, rendition, rendition_probe, policy)

        _ensure_job_active(job)
        mark_asset_playback_ready(
            job,
            phase="fingerprinting",
            metadata={
                "playback_ready": True,
                "playback_ready_at_phase": "fingerprinting",
                "rendition": relative_media_path(rendition),
            },
        )
        fingerprint_source = rendition if rendition.exists() else source
        fingerprint_source_kind = "learning_rendition" if fingerprint_source == rendition else "original"
        duplicate_detection = _run_duplicate_detection_steps(
            job,
            fingerprint_source,
            tmp_dir,
            source_kind=fingerprint_source_kind,
            duration_seconds=probe.get("duration_seconds"),
        )
        if duplicate_detection is None:
            return
        fingerprint, matches = duplicate_detection

        _ensure_job_active(job)
        finish_job(
            job,
            {
                "probe": probe,
                "thumbnail": relative_media_path(thumb),
                "rendition": relative_media_path(rendition),
                "fingerprint": fingerprint,
                "duplicate_candidates": matches,
            },
        )
    except JobCancelled:
        return
    except Exception as exc:
        fail_job(job, str(exc))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def run_once(worker_id: str | None = None) -> bool:
    verify_required_tools()
    job = claim_next_job(worker_id or get_settings().video_worker_id)
    if not job:
        return False
    process_job(job)
    return True




def main() -> None:
    settings = get_settings()
    verify_required_tools()
    if os.getenv("VIDEO_WORKER_BACKFILL", "").lower() in {"1", "true", "yes"}:
        queued = queue_legacy_backfill(_int_env("VIDEO_WORKER_BACKFILL_LIMIT", 200))
        print(f"Queued {queued} legacy media backfill job(s)")
        return
    once = os.getenv("VIDEO_WORKER_ONCE", "").lower() in {"1", "true", "yes"}
    while True:
        processed = run_once(settings.video_worker_id)
        if once:
            return
        if not processed:
            time.sleep(max(settings.video_worker_poll_seconds, 1))


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name, "").strip()
    if not value:
        return default
    try:
        return int(value)
    except ValueError:
        return default


if __name__ == "__main__":
    main()
