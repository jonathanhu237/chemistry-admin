from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from server.app.domains.media.processing_queue import WorkerJob
from server.app.workers import video_worker


def _settings(tmp_path, *, acceleration: str = "auto"):
    return SimpleNamespace(
        media_root=tmp_path,
        video_transcode_acceleration=acceleration,
        video_learning_max_width=1280,
        video_learning_crf=24,
        video_learning_max_fps=30,
        video_learning_transcode_threshold_mb=300,
        video_similarity_algorithm="test-vpdq",
        video_similarity_command='fake-vpdq "{input}" "{output}" "{seconds_per_hash}"',
        video_similarity_compare_command="",
        video_similarity_threshold=0.86,
        video_duplicate_detection_threshold=0.95,
        video_duplicate_detection_duration_tolerance_ratio=0.001,
        video_duplicate_detection_duration_tolerance_floor_seconds=0.5,
        video_duplicate_detection_duration_tolerance_ceiling_seconds=2.0,
        video_duplicate_detection_default_interval_seconds=3.0,
        video_duplicate_detection_min_samples=12,
        video_duplicate_detection_min_interval_seconds=0.5,
    )


def test_encoder_policy_auto_uses_successful_nvenc_probe(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path, acceleration="auto"))
    monkeypatch.setattr(video_worker, "_probe_nvenc", lambda: (True, None))

    policy = video_worker._select_encoder_policy()

    assert policy["encoder"] == "h264_nvenc"
    assert policy["hardware_acceleration"] == "nvenc"
    assert policy["nvenc_probe"] == {"attempted": True, "available": True}


def test_encoder_args_force_browser_playable_8_bit_h264(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path))

    cpu_args = video_worker._encoder_args("libx264")
    nvenc_args = video_worker._encoder_args("h264_nvenc")

    assert cpu_args[cpu_args.index("-pix_fmt") + 1] == "yuv420p"
    assert nvenc_args[nvenc_args.index("-pix_fmt") + 1] == "yuv420p"
    assert nvenc_args[nvenc_args.index("-profile:v") + 1] == "main"


def test_gpu_input_args_use_cuvid_resize_for_supported_nvenc_sources(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path))

    args, policy = video_worker._gpu_input_args(
        "h264_nvenc",
        {"video_codec": "hevc", "width": 3840, "height": 2160},
    )

    assert args == ["-c:v", "hevc_cuvid", "-resize", "1280x720"]
    assert policy["hardware_decoding"] == "nvdec"
    assert policy["hardware_scaling"] == "cuvid_resize"
    assert policy["target_width"] == 1280
    assert policy["target_height"] == 720

    args, policy = video_worker._gpu_input_args(
        "h264_nvenc",
        {"video_codec": "h264", "width": 1280, "height": 720},
    )
    assert args == ["-c:v", "h264_cuvid"]
    assert policy["hardware_decoding"] == "nvdec"
    assert policy["hardware_scaling"] == "none"


def test_encoder_policy_auto_falls_back_when_nvenc_probe_fails(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path, acceleration="auto"))
    monkeypatch.setattr(video_worker, "_probe_nvenc", lambda: (False, "missing video capability"))

    policy = video_worker._select_encoder_policy()

    assert policy["encoder"] == "libx264"
    assert policy["hardware_acceleration"] == "cpu"
    assert policy["fallback"] is True
    assert policy["fallback_stage"] == "probe"
    assert "missing video capability" in policy["fallback_reason"]


def test_ffmpeg_progress_value_maps_out_time_into_transcode_range():
    assert video_worker._ffmpeg_progress_value("out_time_ms=5000000", 10) == 68
    assert video_worker._ffmpeg_progress_value("out_time=00:00:10.000000", 10) == video_worker.TRANSCODE_PROGRESS_END
    assert video_worker._ffmpeg_progress_value("frame=12", 10) is None


def test_probe_reports_embedded_subtitle_stream_diagnostics(monkeypatch, tmp_path):
    payload = {
        "format": {"duration": "40.0", "bit_rate": "1200000"},
        "streams": [
            {"codec_type": "video", "codec_name": "hevc", "width": 1920, "height": 1080, "avg_frame_rate": "30000/1001"},
            {"codec_type": "audio", "codec_name": "flac"},
            {"codec_type": "subtitle", "codec_name": "ass"},
            {"codec_type": "attachment", "codec_name": "ttf"},
            {"codec_type": "data", "codec_name": "bin_data"},
        ],
    }
    monkeypatch.setattr(video_worker, "_run", lambda *_args, **_kwargs: SimpleNamespace(stdout=json.dumps(payload)))

    metadata = video_worker._probe(tmp_path / "source.mkv")

    assert metadata["embedded_subtitle_stream_count"] == 1
    assert metadata["attachment_stream_count"] == 1
    assert metadata["data_stream_count"] == 1
    assert metadata["video_codec"] == "hevc"
    assert metadata["audio_codec"] == "flac"


def test_duplicate_duration_tolerance_and_sampling_defaults(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path))

    assert video_worker._duration_tolerance_seconds(40) == 0.5
    assert video_worker._duration_tolerance_seconds(24 * 60) == pytest.approx(1.44)
    assert video_worker._duration_tolerance_seconds(3 * 60 * 60) == 2.0
    assert video_worker._effective_duplicate_sample_interval(24 * 60) == 3.0
    assert video_worker._effective_duplicate_sample_interval(6) == 0.5
    assert video_worker._effective_duplicate_sample_interval(24) == 2.0


def test_generate_fingerprint_passes_dynamic_sample_interval(monkeypatch, tmp_path):
    settings = _settings(tmp_path)
    monkeypatch.setattr(video_worker, "get_settings", lambda: settings)
    monkeypatch.setattr(video_worker, "relative_media_path", lambda path: path.relative_to(tmp_path).as_posix())
    source = tmp_path / "renditions" / "asset-1" / "learning.mp4"
    source.parent.mkdir(parents=True)
    source.write_bytes(b"rendition")
    tmp_dir = tmp_path / "tmp" / "job-1"
    tmp_dir.mkdir(parents=True)
    commands: list[list[str]] = []
    persisted: list[dict[str, object]] = []

    def fake_run(command, **_kwargs):
        commands.append(command)
        (tmp_dir / "video-signature.bin").write_text("signature", encoding="utf-8")
        return SimpleNamespace(stdout="", stderr="", returncode=0)

    monkeypatch.setattr(video_worker, "_run", fake_run)
    monkeypatch.setattr(video_worker, "persist_video_fingerprint", lambda *args, **kwargs: persisted.append({"args": args, "kwargs": kwargs}))
    monkeypatch.setattr(video_worker, "checksum_sha256_file", lambda _path: "signature-digest")

    result = video_worker._generate_fingerprint(
        "asset-1",
        source,
        tmp_dir,
        source_kind="learning_rendition",
        duration_seconds=24,
    )

    assert commands[0][-1] == "2.000000"
    assert result["seconds_per_hash"] == 2.0
    assert persisted[0]["kwargs"]["metadata"]["seconds_per_hash"] == 2.0


def test_generate_fingerprint_skips_when_duration_is_missing(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path))
    source = tmp_path / "renditions" / "asset-1" / "learning.mp4"
    source.parent.mkdir(parents=True)
    source.write_bytes(b"rendition")
    persisted: list[dict[str, object]] = []

    monkeypatch.setattr(video_worker, "_run", lambda *_args, **_kwargs: pytest.fail("missing duration must skip vPDQ command"))
    monkeypatch.setattr(video_worker, "relative_media_path", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(video_worker, "persist_video_fingerprint", lambda *args, **kwargs: persisted.append({"args": args, "kwargs": kwargs}))

    result = video_worker._generate_fingerprint(
        "asset-1",
        source,
        tmp_path / "tmp",
        source_kind="learning_rendition",
        duration_seconds=None,
    )

    assert result["status"] == "skipped"
    assert result["reason"] == "duration_unavailable"
    assert persisted[0]["kwargs"]["status"] == "skipped"
    assert persisted[0]["kwargs"]["metadata"]["reason"] == "duration_unavailable"


def test_duplicate_compare_query_is_duration_gated_and_active_only() -> None:
    source = Path("server/app/workers/video_worker.py").read_text(encoding="utf-8")

    assert "COALESCE(ma.lifecycle_status, 'active') = 'active'" in source
    assert "ma.upload_status = 'ready'" in source
    assert "ma.duration_seconds IS NOT NULL" in source
    assert "ABS(ma.duration_seconds - CAST(:duration_seconds AS numeric)) <= CAST(:duration_tolerance AS numeric)" in source
    assert "video_duplicate_detection_threshold" in source
    assert "media_subtitle_tracks" not in source


def test_learning_rendition_auto_retries_cpu_after_nvenc_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(video_worker, "get_settings", lambda: _settings(tmp_path, acceleration="auto"))
    monkeypatch.setattr(video_worker, "_probe_nvenc", lambda: (True, None))
    job = WorkerJob(id="job-1", media_asset_id="asset-1", attempts=1)
    source = tmp_path / "originals" / "asset-1" / "source.mkv"
    source.parent.mkdir(parents=True)
    source.write_bytes(b"source")
    tmp_dir = tmp_path / "tmp" / "job-1"
    tmp_dir.mkdir(parents=True)
    encoders: list[str] = []
    commands: list[list[str]] = []

    def fake_run(command, _job, _duration_seconds):
        commands.append(command)
        encoder = command[command.index("-c:v") + 1]
        encoders.append(encoder)
        if encoder == "h264_nvenc":
            (tmp_dir / "learning.mp4").write_bytes(b"partial")
            raise RuntimeError("nvenc failed")
        (tmp_dir / "learning.mp4").write_bytes(b"rendition")

    monkeypatch.setattr(video_worker, "_run_ffmpeg_with_progress", fake_run)

    rendition, policy = video_worker._learning_rendition(
        job,
        source,
        {"id": "asset-1", "file_size_bytes": 1024},
        {"width": 3840, "height": 2160, "duration_seconds": 120},
        tmp_dir,
    )

    assert encoders == ["h264_nvenc", "libx264"]
    assert commands[-1][commands[-1].index("-map") + 1] == "0:v:0"
    assert "0:a:0?" in commands[-1]
    assert "-sn" in commands[-1]
    assert "-dn" in commands[-1]
    assert commands[-1][commands[-1].index("-map_chapters") + 1] == "-1"
    assert commands[-1][commands[-1].index("-map_metadata") + 1] == "-1"
    assert rendition == tmp_path / "renditions" / "asset-1" / "learning.mp4"
    assert rendition.read_bytes() == b"rendition"
    assert policy["encoder"] == "libx264"
    assert policy["fallback"] is True
    assert policy["fallback_stage"] == "transcode"
    assert policy["fallback_from_encoder"] == "h264_nvenc"
    assert policy["source_width"] == 3840
    assert policy["source_height"] == 2160


def test_process_job_keeps_playback_ready_when_duplicate_detection_fails(monkeypatch, tmp_path):
    settings = _settings(tmp_path, acceleration="cpu")
    monkeypatch.setattr(video_worker, "get_settings", lambda: settings)
    monkeypatch.setattr(video_worker, "relative_media_path", lambda path: path.relative_to(tmp_path).as_posix())
    job = WorkerJob(id="job-1", media_asset_id="asset-1", attempts=1)
    source = tmp_path / "originals" / "asset-1" / "source.mp4"
    source.parent.mkdir(parents=True)
    source.write_bytes(b"source")
    thumb = tmp_path / "thumbnails" / "asset-1.jpg"
    thumb.parent.mkdir(parents=True)
    thumb.write_bytes(b"thumb")
    rendition = tmp_path / "renditions" / "asset-1" / "learning.mp4"
    rendition.parent.mkdir(parents=True)
    rendition.write_bytes(b"rendition")
    events: list[tuple[str, object]] = []

    monkeypatch.setattr(video_worker, "_ensure_job_active", lambda _job: None)
    monkeypatch.setattr(video_worker, "update_phase", lambda _job, phase, **_kwargs: events.append(("phase", phase)))
    monkeypatch.setattr(
        video_worker,
        "load_processing_asset",
        lambda _asset_id: {
            "id": "asset-1",
            "relative_path": "originals/asset-1/source.mp4",
            "source_relative_path": "originals/asset-1/source.mp4",
            "checksum_sha256": None,
            "file_size_bytes": 1024,
            "duration_seconds": 10,
        },
    )
    monkeypatch.setattr(video_worker, "checksum_sha256_file", lambda _path: "digest")
    monkeypatch.setattr(
        video_worker,
        "_probe",
        lambda _path: {"width": 1280, "height": 720, "duration_seconds": 10, "video_codec": "h264", "audio_codec": "aac"},
    )
    monkeypatch.setattr(video_worker, "persist_video_probe", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(video_worker, "_thumbnail", lambda *_args, **_kwargs: thumb)
    monkeypatch.setattr(video_worker, "persist_thumbnail", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(video_worker, "_learning_rendition", lambda *_args, **_kwargs: (rendition, {"transcoded": False}))
    monkeypatch.setattr(video_worker, "persist_learning_rendition", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(video_worker, "mark_asset_playback_ready", lambda *_args, **_kwargs: events.append(("ready", True)))
    monkeypatch.setattr(
        video_worker,
        "_generate_fingerprint",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("vpdq failed")),
    )
    monkeypatch.setattr(video_worker, "finish_job", lambda *_args, **_kwargs: pytest.fail("analysis failure must not finish the job"))

    def fake_fail(_job, error, *, preserve_ready_playback=None):
        events.append(("fail", (error, preserve_ready_playback)))

    monkeypatch.setattr(video_worker, "fail_job", fake_fail)

    video_worker.process_job(job)

    assert ("ready", True) in events
    assert events[-1][0] == "fail"
    error, preserve_ready = events[-1][1]
    assert preserve_ready is True
    assert "Duplicate detection failed" in error


def test_process_job_duplicate_detection_retry_skips_rendition_regeneration(monkeypatch, tmp_path):
    settings = _settings(tmp_path, acceleration="cpu")
    monkeypatch.setattr(video_worker, "get_settings", lambda: settings)
    monkeypatch.setattr(video_worker, "relative_media_path", lambda path: path.relative_to(tmp_path).as_posix())
    job = WorkerJob(id="job-1", media_asset_id="asset-1", attempts=1, metadata={"retry_scope": "duplicate_detection"})
    rendition = tmp_path / "renditions" / "asset-1" / "learning.mp4"
    rendition.parent.mkdir(parents=True)
    rendition.write_bytes(b"rendition")
    events: list[tuple[str, object]] = []

    monkeypatch.setattr(video_worker, "_ensure_job_active", lambda _job: None)
    monkeypatch.setattr(video_worker, "update_phase", lambda _job, phase, **_kwargs: events.append(("phase", phase)))
    monkeypatch.setattr(
        video_worker,
        "load_processing_asset",
        lambda _asset_id: {
            "id": "asset-1",
            "relative_path": "originals/asset-1/source.mp4",
            "source_relative_path": "originals/asset-1/source.mp4",
            "playback_relative_path": "renditions/asset-1/learning.mp4",
            "checksum_sha256": None,
            "file_size_bytes": 1024,
            "duration_seconds": 24,
        },
    )
    monkeypatch.setattr(video_worker, "_probe", lambda *_args, **_kwargs: pytest.fail("duplicate retry must not probe source"))
    monkeypatch.setattr(video_worker, "_thumbnail", lambda *_args, **_kwargs: pytest.fail("duplicate retry must not regenerate thumbnail"))
    monkeypatch.setattr(video_worker, "_learning_rendition", lambda *_args, **_kwargs: pytest.fail("duplicate retry must not transcode"))
    monkeypatch.setattr(
        video_worker,
        "_generate_fingerprint",
        lambda _asset_id, source, _tmp_dir, *, source_kind, **_kwargs: {
            "status": "ready",
            "source": source_kind,
            "relative_path": source.relative_to(tmp_path).as_posix(),
        },
    )
    monkeypatch.setattr(video_worker, "_compare_fingerprints", lambda _asset_id: [])
    monkeypatch.setattr(video_worker, "fail_job", lambda *_args, **_kwargs: pytest.fail("duplicate retry should not fail"))
    monkeypatch.setattr(video_worker, "finish_job", lambda _job, outputs: events.append(("finish", outputs)))

    video_worker.process_job(job)

    assert ("phase", "fingerprinting") in events
    assert ("phase", "comparing") in events
    finish = [payload for event, payload in events if event == "finish"][0]
    assert finish["retry_scope"] == "duplicate_detection"
    assert finish["fingerprint"]["source"] == "learning_rendition"
