from __future__ import annotations

import hashlib
import mimetypes
import re
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from sqlalchemy import text

from server.app.domains.media.files import json_param, resolve_media_relative
from server.app.infrastructure.database import db_session
from server.app.infrastructure.settings import get_settings

ALLOWED_SUBTITLE_SUFFIXES = {".vtt", ".srt"}
REJECTED_STYLED_SUBTITLE_SUFFIXES = {".ass", ".ssa"}
ALLOWED_SUBTITLE_KINDS = {"subtitles", "captions"}
SUBTITLE_CONTENT_TYPE = "text/vtt; charset=utf-8"
DEFAULT_SUBTITLE_UPLOAD_MB = 10
_LANGUAGE_RE = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8}){0,2}$|^und$")
_SRT_TIMING_RE = re.compile(
    r"^(?P<start>\d{1,2}:\d{2}:\d{2},\d{1,3})\s*-->\s*(?P<end>\d{1,2}:\d{2}:\d{2},\d{1,3})(?P<settings>.*)$"
)


class SubtitleValidationError(ValueError):
    def __init__(self, reason: str, *, detail: dict[str, Any] | None = None) -> None:
        self.reason = reason
        self.detail = {"reason": reason, **(detail or {})}
        super().__init__(reason)


@dataclass(frozen=True)
class SubtitleArtifacts:
    track_id: str
    source_relative_path: str
    webvtt_relative_path: str
    source_path: Path
    webvtt_path: Path


def _max_subtitle_upload_bytes() -> int:
    settings = get_settings()
    max_mb = int(getattr(settings, "max_media_subtitle_upload_mb", DEFAULT_SUBTITLE_UPLOAD_MB) or DEFAULT_SUBTITLE_UPLOAD_MB)
    return max(1, max_mb) * 1024 * 1024


def _decode_text(content: bytes) -> str:
    try:
        return content.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise SubtitleValidationError("subtitle_not_utf8") from exc


def _normalize_language_code(language_code: str | None) -> str:
    value = (language_code or "und").strip() or "und"
    if len(value) > 35 or not _LANGUAGE_RE.match(value):
        raise SubtitleValidationError("invalid_language_code", detail={"language_code": value})
    return value


def _normalize_label(label: str | None, *, filename: str, language_code: str) -> str:
    value = (label or "").strip()
    if not value:
        value = Path(filename).stem.strip() or language_code
    if not value or len(value) > 80:
        raise SubtitleValidationError("invalid_subtitle_label", detail={"max_length": 80})
    return value


def _normalize_kind(kind: str | None) -> str:
    value = (kind or "subtitles").strip().lower() or "subtitles"
    if value not in ALLOWED_SUBTITLE_KINDS:
        raise SubtitleValidationError("unsupported_subtitle_kind", detail={"kind": value})
    return value


def _guess_subtitle_mime(filename: str, content_type: str | None) -> str:
    guessed = (content_type or mimetypes.guess_type(filename)[0] or "").split(";", 1)[0].strip().lower()
    return guessed or "text/plain"


def _validate_upload_file(filename: str, content: bytes, content_type: str | None) -> tuple[str, str]:
    suffix = Path(filename).suffix.lower()
    mime_type = _guess_subtitle_mime(filename, content_type)
    if suffix in REJECTED_STYLED_SUBTITLE_SUFFIXES:
        raise SubtitleValidationError(
            "styled_subtitle_not_supported",
            detail={"message": "ASS/SSA styling is not preserved by the fixed-video subtitle track pipeline."},
        )
    if suffix not in ALLOWED_SUBTITLE_SUFFIXES:
        raise SubtitleValidationError("unsupported_subtitle_extension", detail={"allowed_extensions": sorted(ALLOWED_SUBTITLE_SUFFIXES)})
    if mime_type.startswith("video/") or mime_type.startswith("audio/") or mime_type.startswith("image/"):
        raise SubtitleValidationError("unsupported_subtitle_mime_type", detail={"mime_type": mime_type})
    if not content:
        raise SubtitleValidationError("empty_subtitle_file")
    max_bytes = _max_subtitle_upload_bytes()
    if len(content) > max_bytes:
        raise SubtitleValidationError(
            "subtitle_file_too_large",
            detail={"file_size_bytes": len(content), "max_subtitle_upload_bytes": max_bytes},
        )
    return suffix.removeprefix("."), mime_type


def validate_webvtt_text(text_value: str) -> str:
    normalized = text_value.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    first = next((line.strip() for line in normalized.split("\n") if line.strip()), "")
    if not first.startswith("WEBVTT"):
        raise SubtitleValidationError("invalid_webvtt")
    return normalized if normalized.endswith("\n") else normalized + "\n"


def _normalize_srt_timestamp(value: str) -> str:
    hours, minutes, second_part = value.split(":")
    seconds, millis = second_part.split(",", 1)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{millis[:3].ljust(3, '0')}"


def srt_to_webvtt(text_value: str) -> str:
    normalized = text_value.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff").strip()
    cues: list[str] = []
    for block in re.split(r"\n{2,}", normalized):
        lines = [line.rstrip() for line in block.split("\n") if line.strip()]
        if not lines:
            continue
        if lines[0].strip().isdigit():
            lines = lines[1:]
        if not lines:
            continue
        match = _SRT_TIMING_RE.match(lines[0].strip())
        if not match:
            raise SubtitleValidationError("invalid_srt_timing")
        start = _normalize_srt_timestamp(match.group("start"))
        end = _normalize_srt_timestamp(match.group("end"))
        settings = (match.group("settings") or "").strip()
        timing = f"{start} --> {end}" + (f" {settings}" if settings else "")
        text_lines = lines[1:]
        if not text_lines:
            raise SubtitleValidationError("invalid_srt_empty_cue")
        cues.append("\n".join([timing, *text_lines]))
    if not cues:
        raise SubtitleValidationError("invalid_srt")
    return "WEBVTT\n\n" + "\n\n".join(cues) + "\n"


def normalize_subtitle_content(filename: str, content: bytes, content_type: str | None) -> tuple[str, str, str, str]:
    source_format, mime_type = _validate_upload_file(filename, content, content_type)
    source_text = _decode_text(content)
    if source_format == "vtt":
        webvtt_text = validate_webvtt_text(source_text)
        return source_format, mime_type, source_text, webvtt_text
    if source_format == "srt":
        webvtt_text = srt_to_webvtt(source_text)
        return source_format, mime_type, source_text, webvtt_text
    raise SubtitleValidationError("unsupported_subtitle_extension")


def subtitle_artifact_paths(asset_id: str, track_id: str, filename: str, source_format: str) -> SubtitleArtifacts:
    try:
        safe_asset_id = str(uuid.UUID(str(asset_id)))
        safe_track_id = str(uuid.UUID(str(track_id)))
    except ValueError as exc:
        raise SubtitleValidationError("invalid_subtitle_path_scope") from exc
    suffix = "." + source_format.lower().lstrip(".")
    if suffix not in ALLOWED_SUBTITLE_SUFFIXES:
        suffix = Path(filename).suffix.lower()
    if suffix not in ALLOWED_SUBTITLE_SUFFIXES:
        raise SubtitleValidationError("unsupported_subtitle_extension")
    base = Path("subtitles") / safe_asset_id / safe_track_id
    source_relative = (base / f"source{suffix}").as_posix()
    webvtt_relative = (base / "track.vtt").as_posix()
    source_path = resolve_media_relative(source_relative)
    webvtt_path = resolve_media_relative(webvtt_relative)
    source_path.parent.mkdir(parents=True, exist_ok=True)
    return SubtitleArtifacts(
        track_id=safe_track_id,
        source_relative_path=source_relative,
        webvtt_relative_path=webvtt_relative,
        source_path=source_path,
        webvtt_path=webvtt_path,
    )


def _source_sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _asset_exists(session: Any, asset_id: str) -> bool:
    return bool(
        session.execute(
            text(
                """
                SELECT 1
                FROM media_assets
                WHERE id = CAST(:asset_id AS uuid)
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                  AND upload_status <> 'replaced'
                LIMIT 1
                """
            ),
            {"asset_id": asset_id},
        ).first()
    )


def _row_to_track(row: Any) -> dict[str, Any]:
    item = dict(row)
    if "id" in item:
        item["id"] = str(item["id"])
    if "media_asset_id" in item:
        item["media_asset_id"] = str(item["media_asset_id"])
    return item


def _track_select_sql(extra_where: str = "") -> str:
    return f"""
        SELECT id, media_asset_id, language_code, label, kind, source_format,
               source_relative_path, webvtt_relative_path, file_size_bytes,
               status, is_default, uploaded_by, error_reason, metadata,
               created_at, updated_at
        FROM media_subtitle_tracks
        WHERE 1 = 1
        {extra_where}
    """


def list_subtitle_tracks(asset_id: str) -> list[dict[str, Any]]:
    with db_session() as session:
        rows = session.execute(
            text(_track_select_sql("AND media_asset_id = CAST(:asset_id AS uuid) ORDER BY is_default DESC, label, created_at")),
            {"asset_id": asset_id},
        ).mappings().all()
    return [_row_to_track(row) for row in rows]


def list_ready_subtitle_tracks_for_assets(
    asset_ids: list[str],
    *,
    stream_path_builder: Callable[[str, str], str],
) -> dict[str, list[dict[str, Any]]]:
    clean_ids = [str(value) for value in asset_ids if str(value or "").strip()]
    if not clean_ids:
        return {}
    with db_session() as session:
        rows = session.execute(
            text(
                _track_select_sql(
                    """
                    AND media_asset_id IN (SELECT CAST(value AS uuid) FROM jsonb_array_elements_text(CAST(:asset_ids AS jsonb)) AS value)
                    AND status = 'ready'
                    AND webvtt_relative_path IS NOT NULL
                    ORDER BY media_asset_id, is_default DESC, label, created_at
                    """
                )
            ),
            {"asset_ids": json_param(clean_ids)},
        ).mappings().all()
    grouped: dict[str, list[dict[str, Any]]] = {asset_id: [] for asset_id in clean_ids}
    for row in rows:
        track = _row_to_track(row)
        asset_id = str(track["media_asset_id"])
        track["stream_path"] = stream_path_builder(asset_id, str(track["id"]))
        grouped.setdefault(asset_id, []).append(track)
    return grouped


def student_ready_subtitle_tracks(asset_id: str) -> list[dict[str, Any]]:
    return list_ready_subtitle_tracks_for_assets(
        [asset_id],
        stream_path_builder=lambda media_id, track_id: f"/api/student/media/assets/{media_id}/subtitle-tracks/{track_id}/stream",
    ).get(str(asset_id), [])


def preview_ready_subtitle_tracks(asset_id: str, *, preview_token: str) -> list[dict[str, Any]]:
    return list_ready_subtitle_tracks_for_assets(
        [asset_id],
        stream_path_builder=lambda media_id, track_id: f"/api/preview/media/assets/{media_id}/subtitle-tracks/{track_id}/stream?preview_token={preview_token}",
    ).get(str(asset_id), [])


def _find_existing_ready_track(session: Any, *, asset_id: str, source_hash: str, language_code: str, label: str) -> dict[str, Any] | None:
    row = session.execute(
        text(
            _track_select_sql(
                """
                AND media_asset_id = CAST(:asset_id AS uuid)
                AND status = 'ready'
                AND language_code = :language_code
                AND label = :label
                AND metadata->>'source_sha256' = :source_hash
                ORDER BY created_at ASC
                LIMIT 1
                """
            )
        ),
        {
            "asset_id": asset_id,
            "source_hash": source_hash,
            "language_code": language_code,
            "label": label,
        },
    ).mappings().first()
    return _row_to_track(row) if row else None


def create_subtitle_track(
    *,
    asset_id: str,
    filename: str,
    content: bytes,
    content_type: str | None = None,
    language_code: str | None = None,
    label: str | None = None,
    kind: str | None = None,
    is_default: bool = False,
    uploaded_by: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    normalized_language = _normalize_language_code(language_code)
    normalized_label = _normalize_label(label, filename=filename, language_code=normalized_language)
    normalized_kind = _normalize_kind(kind)
    source_format, mime_type, source_text, webvtt_text = normalize_subtitle_content(filename, content, content_type)
    source_hash = _source_sha256(content)
    with db_session() as session:
        if not _asset_exists(session, asset_id):
            raise SubtitleValidationError("media_asset_not_found")
        existing = _find_existing_ready_track(
            session,
            asset_id=asset_id,
            source_hash=source_hash,
            language_code=normalized_language,
            label=normalized_label,
        )
        if existing:
            if is_default and not existing.get("is_default"):
                session.execute(
                    text(
                        """
                        UPDATE media_subtitle_tracks
                        SET is_default = false, updated_at = now()
                        WHERE media_asset_id = CAST(:asset_id AS uuid)
                          AND id <> CAST(:track_id AS uuid)
                        """
                    ),
                    {"asset_id": asset_id, "track_id": existing["id"]},
                )
                row = session.execute(
                    text(_track_select_sql("AND id = CAST(:track_id AS uuid)")),
                    {"track_id": existing["id"]},
                ).mappings().one()
                existing = _row_to_track(row)
                session.execute(
                    text("UPDATE media_subtitle_tracks SET is_default = true, updated_at = now() WHERE id = CAST(:track_id AS uuid)"),
                    {"track_id": existing["id"]},
                )
                existing["is_default"] = True
            existing["reused_existing"] = True
            return existing
        track_id = str(uuid.uuid4())
        paths = subtitle_artifact_paths(asset_id, track_id, filename, source_format)
        paths.source_path.write_text(source_text, encoding="utf-8")
        paths.webvtt_path.write_text(webvtt_text, encoding="utf-8")
        if is_default:
            session.execute(
                text(
                    """
                    UPDATE media_subtitle_tracks
                    SET is_default = false, updated_at = now()
                    WHERE media_asset_id = CAST(:asset_id AS uuid)
                    """
                ),
                {"asset_id": asset_id},
            )
        track_metadata = {
            **(metadata or {}),
            "source_sha256": source_hash,
            "source_mime_type": mime_type,
            "source_file_name": filename,
        }
        row = session.execute(
            text(
                """
                INSERT INTO media_subtitle_tracks (
                  id, media_asset_id, language_code, label, kind, source_format,
                  source_relative_path, webvtt_relative_path, file_size_bytes,
                  status, is_default, uploaded_by, error_reason, metadata
                )
                VALUES (
                  CAST(:id AS uuid), CAST(:asset_id AS uuid), :language_code, :label, :kind, :source_format,
                  :source_relative_path, :webvtt_relative_path, :file_size_bytes,
                  'ready', :is_default, CAST(:uploaded_by AS uuid), NULL, CAST(:metadata AS jsonb)
                )
                RETURNING id, media_asset_id, language_code, label, kind, source_format,
                          source_relative_path, webvtt_relative_path, file_size_bytes,
                          status, is_default, uploaded_by, error_reason, metadata,
                          created_at, updated_at
                """
            ),
            {
                "id": track_id,
                "asset_id": asset_id,
                "language_code": normalized_language,
                "label": normalized_label,
                "kind": normalized_kind,
                "source_format": source_format,
                "source_relative_path": paths.source_relative_path,
                "webvtt_relative_path": paths.webvtt_relative_path,
                "file_size_bytes": len(content),
                "is_default": bool(is_default),
                "uploaded_by": uploaded_by,
                "metadata": json_param(track_metadata),
            },
        ).mappings().one()
    return _row_to_track(row)


def update_subtitle_track(
    *,
    asset_id: str,
    track_id: str,
    language_code: str | None = None,
    label: str | None = None,
    kind: str | None = None,
    is_default: bool | None = None,
) -> dict[str, Any]:
    updates: dict[str, Any] = {"asset_id": asset_id, "track_id": track_id}
    set_parts: list[str] = []
    if language_code is not None:
        updates["language_code"] = _normalize_language_code(language_code)
        set_parts.append("language_code = :language_code")
    if label is not None:
        value = label.strip()
        if not value or len(value) > 80:
            raise SubtitleValidationError("invalid_subtitle_label", detail={"max_length": 80})
        updates["label"] = value
        set_parts.append("label = :label")
    if kind is not None:
        updates["kind"] = _normalize_kind(kind)
        set_parts.append("kind = :kind")
    if is_default is not None:
        updates["is_default"] = bool(is_default)
        set_parts.append("is_default = :is_default")
    if not set_parts:
        tracks = list_subtitle_tracks(asset_id)
        for track in tracks:
            if str(track["id"]) == str(track_id):
                return track
        raise SubtitleValidationError("subtitle_track_not_found")
    with db_session() as session:
        if is_default is True:
            session.execute(
                text(
                    """
                    UPDATE media_subtitle_tracks
                    SET is_default = false, updated_at = now()
                    WHERE media_asset_id = CAST(:asset_id AS uuid)
                      AND id <> CAST(:track_id AS uuid)
                    """
                ),
                updates,
            )
        row = session.execute(
            text(
                f"""
                UPDATE media_subtitle_tracks
                SET {", ".join(set_parts)}, updated_at = now()
                WHERE id = CAST(:track_id AS uuid)
                  AND media_asset_id = CAST(:asset_id AS uuid)
                RETURNING id, media_asset_id, language_code, label, kind, source_format,
                          source_relative_path, webvtt_relative_path, file_size_bytes,
                          status, is_default, uploaded_by, error_reason, metadata,
                          created_at, updated_at
                """
            ),
            updates,
        ).mappings().first()
    if not row:
        raise SubtitleValidationError("subtitle_track_not_found")
    return _row_to_track(row)


def subtitle_track_file(asset_id: str, track_id: str) -> tuple[Path, str, str]:
    with db_session() as session:
        row = session.execute(
            text(
                """
                SELECT st.id, st.webvtt_relative_path, st.label, st.language_code, ma.upload_status,
                       COALESCE(ma.lifecycle_status, 'active') AS lifecycle_status
                FROM media_subtitle_tracks st
                JOIN media_assets ma ON ma.id = st.media_asset_id
                WHERE st.id = CAST(:track_id AS uuid)
                  AND st.media_asset_id = CAST(:asset_id AS uuid)
                  AND st.status = 'ready'
                  AND st.webvtt_relative_path IS NOT NULL
                """
            ),
            {"asset_id": asset_id, "track_id": track_id},
        ).mappings().first()
    if not row or row.get("upload_status") != "ready" or row.get("lifecycle_status") != "active":
        raise SubtitleValidationError("subtitle_track_not_found")
    path = resolve_media_relative(str(row["webvtt_relative_path"]))
    if not path.is_file():
        raise SubtitleValidationError("subtitle_file_not_found")
    filename = f"{asset_id}-{row.get('language_code') or 'und'}.vtt"
    return path, SUBTITLE_CONTENT_TYPE, filename


def delete_subtitle_track(*, asset_id: str, track_id: str) -> dict[str, Any]:
    with db_session() as session:
        row = session.execute(
            text(_track_select_sql("AND id = CAST(:track_id AS uuid) AND media_asset_id = CAST(:asset_id AS uuid)")),
            {"asset_id": asset_id, "track_id": track_id},
        ).mappings().first()
        if not row:
            raise SubtitleValidationError("subtitle_track_not_found")
        track = _row_to_track(row)
        session.execute(
            text("DELETE FROM media_subtitle_tracks WHERE id = CAST(:track_id AS uuid) AND media_asset_id = CAST(:asset_id AS uuid)"),
            {"asset_id": asset_id, "track_id": track_id},
        )
    deleted_files: list[dict[str, Any]] = []
    for key in ("source_relative_path", "webvtt_relative_path"):
        relative_path = str(track.get(key) or "").strip()
        if not relative_path:
            continue
        result = {"relative_path": relative_path, "kind": key, "deleted": False, "error": None}
        try:
            path = resolve_media_relative(relative_path)
            if path.exists() and path.is_file():
                path.unlink()
                result["deleted"] = True
        except OSError as exc:
            result["error"] = f"{exc.__class__.__name__}: {str(exc)[:300]}"
        except ValueError as exc:
            result["error"] = str(exc)
        deleted_files.append(result)
    return {"deleted": True, "asset_id": asset_id, "track_id": track_id, "deleted_files": deleted_files}


def retry_subtitle_track_normalization(*, asset_id: str, track_id: str) -> dict[str, Any]:
    with db_session() as session:
        row = session.execute(
            text(_track_select_sql("AND id = CAST(:track_id AS uuid) AND media_asset_id = CAST(:asset_id AS uuid)")),
            {"asset_id": asset_id, "track_id": track_id},
        ).mappings().first()
    if not row:
        raise SubtitleValidationError("subtitle_track_not_found")
    track = _row_to_track(row)
    if track.get("status") == "ready" and track.get("webvtt_relative_path"):
        return track
    source_relative = str(track.get("source_relative_path") or "").strip()
    if not source_relative:
        raise SubtitleValidationError("subtitle_source_missing")
    source_path = resolve_media_relative(source_relative)
    if not source_path.is_file():
        raise SubtitleValidationError("subtitle_source_missing")
    content = source_path.read_bytes()
    source_format, _mime_type, _source_text, webvtt_text = normalize_subtitle_content(source_path.name, content, None)
    artifacts = subtitle_artifact_paths(asset_id, track_id, source_path.name, source_format)
    artifacts.webvtt_path.write_text(webvtt_text, encoding="utf-8")
    with db_session() as session:
        row = session.execute(
            text(
                """
                UPDATE media_subtitle_tracks
                SET source_format = :source_format,
                    webvtt_relative_path = :webvtt_relative_path,
                    file_size_bytes = :file_size_bytes,
                    status = 'ready',
                    error_reason = NULL,
                    updated_at = now()
                WHERE id = CAST(:track_id AS uuid)
                  AND media_asset_id = CAST(:asset_id AS uuid)
                RETURNING id, media_asset_id, language_code, label, kind, source_format,
                          source_relative_path, webvtt_relative_path, file_size_bytes,
                          status, is_default, uploaded_by, error_reason, metadata,
                          created_at, updated_at
                """
            ),
            {
                "asset_id": asset_id,
                "track_id": track_id,
                "source_format": source_format,
                "webvtt_relative_path": artifacts.webvtt_relative_path,
                "file_size_bytes": len(content),
            },
        ).mappings().one()
    return _row_to_track(row)
