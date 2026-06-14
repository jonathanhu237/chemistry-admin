from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from sqlalchemy import text

from server.app.config import get_settings
from server.app.database import db_session
from server.app.media import checksum_sha256_file


PHASE_PROGRESS = {
    "starting": 1,
    "validating": 5,
    "probing": 15,
    "thumbnailing": 30,
    "transcoding": 60,
    "fingerprinting": 78,
    "comparing": 90,
    "ready": 100,
    "failed": 0,
}


@dataclass(frozen=True)
class WorkerJob:
    id: str
    media_asset_id: str
    attempts: int
    job_type: str = "process_uploaded_video"

    @property
    def preserves_ready_playback(self) -> bool:
        return self.job_type == "backfill_legacy_video"


def _json_param(value: Any) -> str:
    return json.dumps(value if value is not None else {}, ensure_ascii=False, default=str)


def _media_path(relative_path: str) -> Path:
    root = get_settings().media_root.resolve()
    path = (root / relative_path).resolve()
    if root != path and root not in path.parents:
        raise RuntimeError("Media path escapes media root")
    return path


def _relative(path: Path) -> str:
    root = get_settings().media_root.resolve()
    return path.resolve().relative_to(root).as_posix()


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


def claim_next_job(worker_id: str) -> WorkerJob | None:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    UPDATE media_processing_jobs
                    SET status = 'processing',
                        phase = 'starting',
                        progress = 1,
                        attempts = attempts + 1,
                        worker_id = :worker_id,
                        started_at = now(),
                        updated_at = now()
                    WHERE id = (
                      SELECT id
                      FROM media_processing_jobs
                      WHERE status = 'queued'
                        AND attempts < max_attempts
                      ORDER BY created_at
                      FOR UPDATE SKIP LOCKED
                      LIMIT 1
                    )
                    RETURNING id, media_asset_id, attempts, job_type
                    """
                ),
                {"worker_id": worker_id},
            )
            .mappings()
            .first()
        )
    if not row:
        return None
    return WorkerJob(
        id=str(row["id"]),
        media_asset_id=str(row["media_asset_id"]),
        attempts=int(row["attempts"]),
        job_type=str(row["job_type"] or "process_uploaded_video"),
    )


def update_phase(job: WorkerJob, phase: str, progress: int | None = None, metadata: dict[str, Any] | None = None) -> None:
    next_progress = PHASE_PROGRESS.get(phase, progress or 0) if progress is None else progress
    with db_session() as session:
        session.execute(
            text(
                """
                UPDATE media_processing_jobs
                SET phase = :phase,
                    progress = :progress,
                    metadata = metadata || CAST(:metadata AS jsonb),
                    updated_at = now()
                WHERE id = CAST(:job_id AS uuid)
                """
            ),
            {
                "job_id": job.id,
                "phase": phase,
                "progress": next_progress,
                "metadata": _json_param(metadata or {}),
            },
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = CASE
                      WHEN :preserve_ready_playback THEN upload_status
                      ELSE 'processing'
                    END,
                    processing_phase = :phase,
                    processing_progress = :progress,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                """
            ),
            {
                "asset_id": job.media_asset_id,
                "phase": phase,
                "progress": next_progress,
                "preserve_ready_playback": job.preserves_ready_playback,
            },
        )


def fail_job(job: WorkerJob, error: str) -> None:
    message = error[:1000]
    with db_session() as session:
        session.execute(
            text(
                """
                UPDATE media_processing_jobs
                SET status = 'failed',
                    phase = 'failed',
                    progress = 0,
                    error_reason = :error_reason,
                    finished_at = now(),
                    updated_at = now()
                WHERE id = CAST(:job_id AS uuid)
                """
            ),
            {"job_id": job.id, "error_reason": message},
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = CASE
                      WHEN :preserve_ready_playback THEN upload_status
                      ELSE 'failed'
                    END,
                    processing_phase = 'failed',
                    processing_progress = 0,
                    error_reason = :error_reason,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                """
            ),
            {
                "asset_id": job.media_asset_id,
                "error_reason": message,
                "preserve_ready_playback": job.preserves_ready_playback,
            },
        )


def finish_job(job: WorkerJob, outputs: dict[str, Any]) -> None:
    with db_session() as session:
        session.execute(
            text(
                """
                UPDATE media_processing_jobs
                SET status = 'ready',
                    phase = 'ready',
                    progress = 100,
                    outputs = CAST(:outputs AS jsonb),
                    finished_at = now(),
                    updated_at = now()
                WHERE id = CAST(:job_id AS uuid)
                """
            ),
            {"job_id": job.id, "outputs": _json_param(outputs)},
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = 'ready',
                    processing_phase = 'ready',
                    processing_progress = 100,
                    error_reason = NULL,
                    processed_at = now(),
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                """
            ),
            {"asset_id": job.media_asset_id},
        )


def _load_asset(asset_id: str) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    SELECT id, title, original_file_name, relative_path, source_relative_path,
                           checksum_sha256, mime_type, file_size_bytes
                    FROM media_assets
                    WHERE id = CAST(:asset_id AS uuid)
                    """
                ),
                {"asset_id": asset_id},
            )
            .mappings()
            .first()
        )
    if not row:
        raise RuntimeError("Media asset not found")
    return dict(row)


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


def _persist_probe(asset_id: str, metadata: dict[str, Any]) -> None:
    with db_session() as session:
        session.execute(
            text(
                """
                UPDATE media_assets
                SET duration_seconds = :duration_seconds,
                    width = :width,
                    height = :height,
                    fps = :fps,
                    bitrate = :bitrate,
                    video_codec = :video_codec,
                    audio_codec = :audio_codec,
                    metadata = metadata || CAST(:metadata AS jsonb),
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                """
            ),
            {
                "asset_id": asset_id,
                "duration_seconds": metadata.get("duration_seconds"),
                "width": metadata.get("width"),
                "height": metadata.get("height"),
                "fps": metadata.get("fps"),
                "bitrate": metadata.get("bitrate"),
                "video_codec": metadata.get("video_codec"),
                "audio_codec": metadata.get("audio_codec"),
                "metadata": _json_param({"video_probe": metadata}),
            },
        )


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


def _learning_rendition(source: Path, asset: dict[str, Any], metadata: dict[str, Any], tmp_dir: Path) -> tuple[Path, dict[str, Any]]:
    settings = get_settings()
    output = tmp_dir / "learning.mp4"
    width = int(metadata.get("width") or 0)
    should_transcode = _needs_transcode(source, asset, metadata)
    command = ["ffmpeg", "-y", "-i", str(source), "-map", "0:v:0", "-map", "0:a?"]
    if should_transcode:
        if width and width > settings.video_learning_max_width:
            command.extend(["-vf", f"scale={settings.video_learning_max_width}:-2"])
        command.extend(
            [
                "-r",
                str(settings.video_learning_max_fps),
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                str(settings.video_learning_crf),
                "-c:a",
                "aac",
                "-b:a",
                "128k",
            ]
        )
        kind = "learning-720p"
    else:
        command.extend(["-c", "copy"])
        kind = "learning-remux"
    command.extend(["-movflags", "+faststart", str(output)])
    _run(command, timeout=None)
    if not output.exists() or output.stat().st_size <= 0:
        raise RuntimeError("FFmpeg did not produce a learning rendition")
    final = get_settings().media_root / "renditions" / str(asset["id"]) / "learning.mp4"
    final.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(output), final)
    return final, {"kind": kind, "transcoded": should_transcode}


def _persist_rendition(asset_id: str, rendition: Path, metadata: dict[str, Any], policy: dict[str, Any]) -> None:
    relative_path = _relative(rendition)
    with db_session() as session:
        session.execute(
            text(
                """
                INSERT INTO media_renditions (
                  media_asset_id, kind, relative_path, mime_type, file_size_bytes,
                  duration_seconds, width, height, fps, bitrate, video_codec, audio_codec,
                  status, metadata
                )
                VALUES (
                  CAST(:asset_id AS uuid), 'learning', :relative_path, 'video/mp4',
                  :file_size_bytes, :duration_seconds, :width, :height, :fps,
                  :bitrate, :video_codec, :audio_codec, 'ready', CAST(:metadata AS jsonb)
                )
                ON CONFLICT (media_asset_id, kind) DO UPDATE SET
                  relative_path = EXCLUDED.relative_path,
                  mime_type = EXCLUDED.mime_type,
                  file_size_bytes = EXCLUDED.file_size_bytes,
                  duration_seconds = EXCLUDED.duration_seconds,
                  width = EXCLUDED.width,
                  height = EXCLUDED.height,
                  fps = EXCLUDED.fps,
                  bitrate = EXCLUDED.bitrate,
                  video_codec = EXCLUDED.video_codec,
                  audio_codec = EXCLUDED.audio_codec,
                  status = 'ready',
                  metadata = EXCLUDED.metadata,
                  updated_at = now()
                """
            ),
            {
                "asset_id": asset_id,
                "relative_path": relative_path,
                "file_size_bytes": rendition.stat().st_size,
                "duration_seconds": metadata.get("duration_seconds"),
                "width": metadata.get("width"),
                "height": metadata.get("height"),
                "fps": metadata.get("fps"),
                "bitrate": metadata.get("bitrate"),
                "video_codec": metadata.get("video_codec"),
                "audio_codec": metadata.get("audio_codec"),
                "metadata": _json_param(policy),
            },
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET playback_relative_path = :playback_relative_path,
                    playback_mime_type = 'video/mp4',
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                """
            ),
            {"asset_id": asset_id, "playback_relative_path": relative_path},
        )


def _persist_thumbnail(asset_id: str, thumbnail: Path) -> None:
    with db_session() as session:
        session.execute(
            text(
                """
                UPDATE media_assets
                SET thumbnail_relative_path = :thumbnail_relative_path,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                """
            ),
            {"asset_id": asset_id, "thumbnail_relative_path": _relative(thumbnail)},
        )


def _generate_fingerprint(asset_id: str, source: Path, tmp_dir: Path) -> dict[str, Any]:
    settings = get_settings()
    algorithm = settings.video_similarity_algorithm
    if not settings.video_similarity_command:
        _persist_fingerprint(
            asset_id,
            algorithm=algorithm,
            status="skipped",
            relative_path=None,
            signature_hash=None,
            metadata={"reason": "VIDEO_SIMILARITY_COMMAND not configured"},
        )
        return {"status": "skipped", "algorithm": algorithm}
    output = tmp_dir / "video-signature.bin"
    command_text = settings.video_similarity_command.format(input=str(source), output=str(output))
    _run(shlex.split(command_text), timeout=None)
    if not output.exists() or output.stat().st_size <= 0:
        raise RuntimeError("Configured video similarity command did not produce a signature")
    final = get_settings().media_root / "fingerprints" / asset_id / output.name
    final.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(output), final)
    signature_hash = checksum_sha256_file(final)
    _persist_fingerprint(
        asset_id,
        algorithm=algorithm,
        status="ready",
        relative_path=_relative(final),
        signature_hash=signature_hash,
        metadata={"command": settings.video_similarity_command},
    )
    return {"status": "ready", "algorithm": algorithm, "relative_path": _relative(final)}


def _persist_fingerprint(
    asset_id: str,
    *,
    algorithm: str,
    status: str,
    relative_path: str | None,
    signature_hash: str | None,
    metadata: dict[str, Any],
) -> None:
    with db_session() as session:
        session.execute(
            text(
                """
                INSERT INTO media_video_fingerprints (
                  media_asset_id, algorithm, algorithm_version, relative_path,
                  status, signature_hash, metadata
                )
                VALUES (
                  CAST(:asset_id AS uuid), :algorithm, :algorithm_version,
                  :relative_path, :status, :signature_hash, CAST(:metadata AS jsonb)
                )
                ON CONFLICT (media_asset_id, algorithm) DO UPDATE SET
                  algorithm_version = EXCLUDED.algorithm_version,
                  relative_path = EXCLUDED.relative_path,
                  status = EXCLUDED.status,
                  signature_hash = EXCLUDED.signature_hash,
                  metadata = EXCLUDED.metadata,
                  updated_at = now()
                """
            ),
            {
                "asset_id": asset_id,
                "algorithm": algorithm,
                "algorithm_version": "external",
                "relative_path": relative_path,
                "status": status,
                "signature_hash": signature_hash,
                "metadata": _json_param(metadata),
            },
        )


def _compare_fingerprints(asset_id: str) -> list[dict[str, Any]]:
    settings = get_settings()
    if not settings.video_similarity_compare_command:
        return []
    with db_session() as session:
        current = (
            session.execute(
                text(
                    """
                    SELECT relative_path, algorithm
                    FROM media_video_fingerprints
                    WHERE media_asset_id = CAST(:asset_id AS uuid)
                      AND status = 'ready'
                    ORDER BY created_at DESC
                    LIMIT 1
                    """
                ),
                {"asset_id": asset_id},
            )
            .mappings()
            .first()
        )
        candidates = session.execute(
            text(
                """
                SELECT media_asset_id, relative_path, algorithm
                FROM media_video_fingerprints
                WHERE media_asset_id <> CAST(:asset_id AS uuid)
                  AND status = 'ready'
                  AND algorithm = :algorithm
                """
            ),
            {"asset_id": asset_id, "algorithm": current["algorithm"] if current else ""},
        ).mappings().all()
    if not current:
        return []
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
        if score is not None and score >= settings.video_similarity_threshold:
            match = {
                "candidate_asset_id": str(candidate["media_asset_id"]),
                "score": score,
                "algorithm": candidate["algorithm"],
            }
            _persist_duplicate_candidate(asset_id, match)
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


def _persist_duplicate_candidate(asset_id: str, match: dict[str, Any]) -> None:
    with db_session() as session:
        session.execute(
            text(
                """
                INSERT INTO media_duplicate_candidates (
                  media_asset_id, candidate_asset_id, duplicate_type, score,
                  algorithm, status, metadata
                )
                VALUES (
                  CAST(:asset_id AS uuid), CAST(:candidate_asset_id AS uuid),
                  'suspected', :score, :algorithm, 'pending', CAST(:metadata AS jsonb)
                )
                ON CONFLICT (media_asset_id, candidate_asset_id, duplicate_type, algorithm)
                DO UPDATE SET
                  score = EXCLUDED.score,
                  status = 'pending',
                  metadata = EXCLUDED.metadata,
                  updated_at = now()
                """
            ),
            {
                "asset_id": asset_id,
                "candidate_asset_id": match["candidate_asset_id"],
                "score": match["score"],
                "algorithm": match["algorithm"],
                "metadata": _json_param({"source": "video_worker"}),
            },
        )


def process_job(job: WorkerJob) -> None:
    tmp_dir = get_settings().media_root / "tmp" / job.id
    tmp_dir.mkdir(parents=True, exist_ok=True)
    try:
        update_phase(job, "validating")
        asset = _load_asset(job.media_asset_id)
        source = _media_path(asset.get("source_relative_path") or asset["relative_path"])
        if not source.exists():
            raise RuntimeError("Source media file is missing")
        digest = checksum_sha256_file(source)
        if asset.get("checksum_sha256") and str(asset["checksum_sha256"]).lower() != digest.lower():
            raise RuntimeError("Source media checksum does not match media asset record")

        update_phase(job, "probing")
        probe = _probe(source)
        _persist_probe(job.media_asset_id, probe)

        update_phase(job, "thumbnailing")
        thumb = _thumbnail(job, source, tmp_dir, probe.get("duration_seconds"))
        _persist_thumbnail(job.media_asset_id, thumb)

        update_phase(job, "transcoding")
        rendition, policy = _learning_rendition(source, asset, probe, tmp_dir)
        rendition_probe = _probe(rendition)
        _persist_rendition(job.media_asset_id, rendition, rendition_probe, policy)

        update_phase(job, "fingerprinting")
        fingerprint = _generate_fingerprint(job.media_asset_id, source, tmp_dir)

        update_phase(job, "comparing")
        matches = _compare_fingerprints(job.media_asset_id) if fingerprint.get("status") == "ready" else []

        finish_job(
            job,
            {
                "probe": probe,
                "thumbnail": _relative(thumb),
                "rendition": _relative(rendition),
                "fingerprint": fingerprint,
                "duplicate_candidates": matches,
            },
        )
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


def queue_legacy_backfill(limit: int = 200) -> int:
    settings = get_settings()
    with db_session() as session:
        rows = (
            session.execute(
                text(
                    """
                    WITH candidates AS (
                      SELECT ma.id
                      FROM media_assets ma
                      WHERE ma.upload_status = 'ready'
                        AND (
                          ma.thumbnail_relative_path IS NULL
                          OR ma.playback_relative_path IS NULL
                          OR NOT EXISTS (
                            SELECT 1 FROM media_video_fingerprints mf
                            WHERE mf.media_asset_id = ma.id
                              AND mf.algorithm = :algorithm
                              AND mf.status IN ('ready', 'skipped')
                          )
                        )
                        AND NOT EXISTS (
                          SELECT 1
                          FROM media_processing_jobs existing
                          WHERE existing.media_asset_id = ma.id
                            AND existing.job_type = 'backfill_legacy_video'
                            AND existing.status IN ('queued', 'processing')
                        )
                      ORDER BY ma.updated_at DESC
                      LIMIT :limit
                    )
                    INSERT INTO media_processing_jobs (
                      media_asset_id, job_type, status, phase, progress, metadata
                    )
                    SELECT id, 'backfill_legacy_video', 'queued', 'queued', 0,
                           '{"source":"legacy_backfill"}'::jsonb
                    FROM candidates
                    RETURNING id
                    """
                ),
                {"limit": limit, "algorithm": settings.video_similarity_algorithm},
            )
            .mappings()
            .all()
        )
    return len(rows)


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
