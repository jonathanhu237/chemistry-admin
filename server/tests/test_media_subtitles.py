from __future__ import annotations

import json
import uuid
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from server.app.domains.media import subtitles


class _FakeResult:
    def __init__(self, *, row: dict[str, Any] | None = None, rows: list[dict[str, Any]] | None = None) -> None:
        self.row = row
        self.rows = rows if rows is not None else ([row] if row else [])

    def mappings(self) -> "_FakeResult":
        return self

    def first(self) -> dict[str, Any] | None:
        return self.row

    def one(self) -> dict[str, Any]:
        if self.row is None:
            raise AssertionError("Expected one fake row")
        return self.row

    def all(self) -> list[dict[str, Any]]:
        return self.rows


class _FakeSession:
    def __init__(self, *, select_row: dict[str, Any] | None = None) -> None:
        self.select_row = select_row
        self.calls: list[tuple[str, dict[str, Any]]] = []

    def execute(self, statement: object, params: dict[str, Any] | None = None) -> _FakeResult:
        sql = str(statement)
        values = dict(params or {})
        self.calls.append((sql, values))
        if "INSERT INTO media_subtitle_tracks" in sql:
            metadata = json.loads(values["metadata"]) if isinstance(values.get("metadata"), str) else values.get("metadata")
            return _FakeResult(
                row={
                    "id": values["id"],
                    "media_asset_id": values["asset_id"],
                    "language_code": values["language_code"],
                    "label": values["label"],
                    "kind": values["kind"],
                    "source_format": values["source_format"],
                    "source_relative_path": values["source_relative_path"],
                    "webvtt_relative_path": values["webvtt_relative_path"],
                    "file_size_bytes": values["file_size_bytes"],
                    "status": "ready",
                    "is_default": values["is_default"],
                    "uploaded_by": values.get("uploaded_by"),
                    "error_reason": None,
                    "metadata": metadata,
                    "created_at": None,
                    "updated_at": None,
                }
            )
        if "SELECT id, media_asset_id" in sql:
            return _FakeResult(row=self.select_row)
        return _FakeResult()


class _FakeSessionScope:
    def __init__(self, session: _FakeSession) -> None:
        self.session = session

    def __enter__(self) -> _FakeSession:
        return self.session

    def __exit__(self, *_args: object) -> None:
        return None


def _media_resolver(root: Path):
    def resolve(relative_path: str) -> Path:
        path = (root / relative_path).resolve()
        if root.resolve() != path and root.resolve() not in path.parents:
            raise ValueError("Media path escapes media root")
        return path

    return resolve


def test_vtt_upload_is_validated_and_normalized() -> None:
    source_format, mime_type, source_text, webvtt_text = subtitles.normalize_subtitle_content(
        "lesson.zh.vtt",
        b"\xef\xbb\xbfWEBVTT\n\n00:00:01.000 --> 00:00:02.000\nHello\n",
        "text/vtt",
    )

    assert source_format == "vtt"
    assert mime_type == "text/vtt"
    assert source_text.startswith("WEBVTT")
    assert webvtt_text.endswith("\n")


def test_srt_upload_converts_to_webvtt() -> None:
    _source_format, _mime_type, _source_text, webvtt_text = subtitles.normalize_subtitle_content(
        "lesson.zh.srt",
        "1\n00:00:01,5 --> 00:00:02,250\n你好\n".encode(),
        "application/x-subrip",
    )

    assert webvtt_text == "WEBVTT\n\n00:00:01.500 --> 00:00:02.250\n你好\n"


@pytest.mark.parametrize(
    ("filename", "content_type", "reason"),
    [
        ("lesson.ass", "text/plain", "styled_subtitle_not_supported"),
        ("lesson.mp4", "video/mp4", "unsupported_subtitle_extension"),
        ("lesson.vtt", "video/mp4", "unsupported_subtitle_mime_type"),
    ],
)
def test_invalid_subtitle_uploads_are_rejected(filename: str, content_type: str, reason: str) -> None:
    with pytest.raises(subtitles.SubtitleValidationError) as exc:
        subtitles.normalize_subtitle_content(filename, b"WEBVTT\n\n", content_type)

    assert exc.value.reason == reason


def test_subtitle_artifact_paths_are_scoped_under_media_root(monkeypatch, tmp_path) -> None:
    asset_id = str(uuid.uuid4())
    track_id = str(uuid.uuid4())
    monkeypatch.setattr(subtitles, "resolve_media_relative", _media_resolver(tmp_path))

    paths = subtitles.subtitle_artifact_paths(asset_id, track_id, "../unsafe.srt", "srt")

    assert paths.source_relative_path == f"subtitles/{asset_id}/{track_id}/source.srt"
    assert paths.webvtt_relative_path == f"subtitles/{asset_id}/{track_id}/track.vtt"
    assert tmp_path.resolve() in paths.source_path.resolve().parents

    with pytest.raises(subtitles.SubtitleValidationError) as exc:
        subtitles.subtitle_artifact_paths("../escape", track_id, "lesson.srt", "srt")
    assert exc.value.reason == "invalid_subtitle_path_scope"


def test_create_subtitle_track_writes_artifacts_and_clears_previous_default(monkeypatch, tmp_path) -> None:
    asset_id = str(uuid.uuid4())
    session = _FakeSession()
    monkeypatch.setattr(subtitles, "db_session", lambda: _FakeSessionScope(session))
    monkeypatch.setattr(subtitles, "_asset_exists", lambda _session, _asset_id: True)
    monkeypatch.setattr(subtitles, "_find_existing_ready_track", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(subtitles, "resolve_media_relative", _media_resolver(tmp_path))

    track = subtitles.create_subtitle_track(
        asset_id=asset_id,
        filename="lesson.zh.srt",
        content="1\n00:00:01,000 --> 00:00:02,000\n你好\n".encode(),
        content_type="text/plain",
        language_code="zh-CN",
        label="中文字幕",
        is_default=True,
        metadata={"client_link_id": "local-1"},
    )

    assert track["status"] == "ready"
    assert track["language_code"] == "zh-CN"
    assert track["label"] == "中文字幕"
    assert track["is_default"] is True
    assert track["metadata"]["client_link_id"] == "local-1"
    assert Path(tmp_path, track["source_relative_path"]).read_text(encoding="utf-8").startswith("1\n")
    assert Path(tmp_path, track["webvtt_relative_path"]).read_text(encoding="utf-8").startswith("WEBVTT\n")
    assert any("SET is_default = false" in sql for sql, _params in session.calls)


def test_create_subtitle_track_reuses_existing_ready_track_for_same_content_language_and_label(monkeypatch, tmp_path) -> None:
    asset_id = str(uuid.uuid4())
    track_id = str(uuid.uuid4())
    session = _FakeSession()
    existing = {
        "id": track_id,
        "media_asset_id": asset_id,
        "language_code": "zh-CN",
        "label": "Chinese",
        "kind": "subtitles",
        "source_format": "vtt",
        "source_relative_path": f"subtitles/{asset_id}/{track_id}/source.vtt",
        "webvtt_relative_path": f"subtitles/{asset_id}/{track_id}/track.vtt",
        "file_size_bytes": 9,
        "status": "ready",
        "is_default": False,
        "uploaded_by": None,
        "error_reason": None,
        "metadata": {"source_sha256": "same"},
        "created_at": None,
        "updated_at": None,
    }
    monkeypatch.setattr(subtitles, "db_session", lambda: _FakeSessionScope(session))
    monkeypatch.setattr(subtitles, "_asset_exists", lambda _session, _asset_id: True)
    monkeypatch.setattr(subtitles, "_find_existing_ready_track", lambda *_args, **_kwargs: dict(existing))
    monkeypatch.setattr(subtitles, "resolve_media_relative", _media_resolver(tmp_path))

    track = subtitles.create_subtitle_track(
        asset_id=asset_id,
        filename="lesson.zh.vtt",
        content=b"WEBVTT\n\n00:00:01.000 --> 00:00:02.000\nHello\n",
        content_type="text/vtt",
        language_code="zh-CN",
        label="Chinese",
        metadata={"client_link_id": "local-duplicate"},
    )

    assert track["id"] == track_id
    assert track["reused_existing"] is True
    assert not any("INSERT INTO media_subtitle_tracks" in sql for sql, _params in session.calls)
    assert not list(tmp_path.rglob("track.vtt"))


def test_subtitle_track_delete_removes_only_subtitle_artifacts(monkeypatch, tmp_path) -> None:
    asset_id = str(uuid.uuid4())
    track_id = str(uuid.uuid4())
    video = tmp_path / "renditions" / asset_id / "learning.mp4"
    source = tmp_path / "subtitles" / asset_id / track_id / "source.vtt"
    webvtt = tmp_path / "subtitles" / asset_id / track_id / "track.vtt"
    video.parent.mkdir(parents=True)
    source.parent.mkdir(parents=True)
    video.write_bytes(b"video")
    source.write_text("WEBVTT\n\n", encoding="utf-8")
    webvtt.write_text("WEBVTT\n\n", encoding="utf-8")
    session = _FakeSession(
        select_row={
            "id": track_id,
            "media_asset_id": asset_id,
            "language_code": "zh-CN",
            "label": "Chinese",
            "kind": "subtitles",
            "source_format": "vtt",
            "source_relative_path": f"subtitles/{asset_id}/{track_id}/source.vtt",
            "webvtt_relative_path": f"subtitles/{asset_id}/{track_id}/track.vtt",
            "file_size_bytes": 9,
            "status": "ready",
            "is_default": True,
            "uploaded_by": None,
            "error_reason": None,
            "metadata": {},
            "created_at": None,
            "updated_at": None,
        }
    )
    monkeypatch.setattr(subtitles, "db_session", lambda: _FakeSessionScope(session))
    monkeypatch.setattr(subtitles, "resolve_media_relative", _media_resolver(tmp_path))

    result = subtitles.delete_subtitle_track(asset_id=asset_id, track_id=track_id)

    assert result["deleted"] is True
    assert source.exists() is False
    assert webvtt.exists() is False
    assert video.exists() is True
