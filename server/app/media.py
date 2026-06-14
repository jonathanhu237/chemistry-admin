from __future__ import annotations

import hashlib
import json
import mimetypes
import secrets
import shutil
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from sqlalchemy import text

from server.app.config import get_settings
from server.app.database import db_session

ALLOWED_MEDIA_SUFFIXES = {".mp4", ".mov", ".m4v", ".webm", ".avi"}
ALLOWED_MEDIA_MIME_PREFIXES = ("video/",)
PROCESSING_JOB_TYPE = "process_uploaded_video"


@dataclass(frozen=True)
class MediaValidation:
    ok: bool
    mime_type: str
    file_size_bytes: int
    error: str | None = None


def validate_media_file(filename: str, content: bytes, content_type: str | None = None) -> MediaValidation:
    suffix = Path(filename).suffix.lower()
    guessed_type = content_type or mimetypes.guess_type(filename)[0] or ""
    if suffix not in ALLOWED_MEDIA_SUFFIXES:
        return MediaValidation(False, guessed_type, len(content), "unsupported_file_extension")
    if guessed_type and not guessed_type.startswith(ALLOWED_MEDIA_MIME_PREFIXES):
        return MediaValidation(False, guessed_type, len(content), "unsupported_mime_type")
    max_bytes = get_settings().max_media_upload_mb * 1024 * 1024
    if len(content) > max_bytes:
        return MediaValidation(False, guessed_type, len(content), "file_too_large")
    if not content:
        return MediaValidation(False, guessed_type, len(content), "empty_file")
    return MediaValidation(True, guessed_type or "application/octet-stream", len(content))


def checksum_sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def checksum_sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_student_visible_media(upload_status: str, binding_status: str) -> bool:
    return upload_status == "ready" and binding_status == "published"


def _json_param(value: Any) -> str:
    return json.dumps(value if value is not None else {}, ensure_ascii=False, default=str)


def _asset_id() -> str:
    return str(uuid.uuid4())


def _safe_media_path(filename: str) -> tuple[Path, str]:
    settings = get_settings()
    suffix = Path(filename).suffix.lower()
    relative_path = Path("uploads") / f"{secrets.token_hex(16)}{suffix}"
    absolute_path = settings.media_root / relative_path
    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    return absolute_path, relative_path.as_posix()


def _source_media_path(asset_id: str, filename: str) -> tuple[Path, str]:
    settings = get_settings()
    suffix = Path(filename).suffix.lower() or ".mp4"
    relative_path = Path("originals") / asset_id / f"source{suffix}"
    absolute_path = settings.media_root / relative_path
    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    return absolute_path, relative_path.as_posix()


def _resolve_media_relative(relative_path: str) -> Path:
    root = get_settings().media_root.resolve()
    path = (root / relative_path).resolve()
    if root != path and root not in path.parents:
        raise ValueError("Media path escapes media root")
    return path


def _row_dict(row: Any) -> dict[str, Any]:
    item = dict(row)
    for key in ("renditions", "duplicate_candidates", "processing_job"):
        if item.get(key) is None:
            item[key] = [] if key != "processing_job" else None
    return item


def _find_exact_asset(checksum: str, file_size_bytes: int) -> dict[str, Any] | None:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    SELECT id, title, original_file_name, relative_path, source_relative_path,
                           thumbnail_relative_path, playback_relative_path, playback_mime_type,
                           checksum_sha256, mime_type, file_size_bytes, duration_seconds,
                           upload_status, processing_phase, processing_progress,
                           error_reason, created_at, updated_at
                    FROM media_assets
                    WHERE checksum_sha256 = :checksum
                      AND file_size_bytes = :file_size_bytes
                      AND upload_status <> 'failed'
                      AND upload_status <> 'replaced'
                    ORDER BY created_at ASC
                    LIMIT 1
                    """
                ),
                {"checksum": checksum, "file_size_bytes": file_size_bytes},
            )
            .mappings()
            .first()
        )
    return dict(row) if row else None


def precheck_exact_duplicate(*, checksum_sha256_value: str, file_size_bytes: int) -> dict[str, Any]:
    existing = _find_exact_asset(checksum_sha256_value.lower(), file_size_bytes)
    return {"exists": bool(existing), "asset": existing}


def _enqueue_processing_job(asset_id: str, *, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    INSERT INTO media_processing_jobs (
                      media_asset_id, job_type, status, phase, progress, metadata
                    )
                    VALUES (
                      CAST(:asset_id AS uuid), :job_type, 'queued', 'queued', 0,
                      CAST(:metadata AS jsonb)
                    )
                    RETURNING id, media_asset_id, job_type, status, phase, progress,
                              attempts, error_reason, created_at, updated_at
                    """
                ),
                {
                    "asset_id": asset_id,
                    "job_type": PROCESSING_JOB_TYPE,
                    "metadata": _json_param(metadata or {}),
                },
            )
            .mappings()
            .one()
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = 'processing',
                    processing_phase = 'queued',
                    processing_progress = 0,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                """
            ),
            {"asset_id": asset_id},
        )
    return dict(row)


def enqueue_processing_job(asset_id: str, *, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return _enqueue_processing_job(asset_id, metadata=metadata)


def _insert_failed_asset(
    *,
    title: str,
    filename: str,
    relative_path: str,
    mime_type: str,
    file_size_bytes: int,
    error_reason: str | None,
    uploaded_by: str | None,
) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    INSERT INTO media_assets (
                      title, original_file_name, relative_path, source_relative_path,
                      mime_type, file_size_bytes, upload_status, processing_phase,
                      processing_progress, error_reason, uploaded_by, metadata
                    )
                    VALUES (
                      :title, :original_file_name, :relative_path, :relative_path,
                      :mime_type, :file_size_bytes, 'failed', 'failed', 0,
                      :error_reason, CAST(:uploaded_by AS uuid), '{}'::jsonb
                    )
                    RETURNING id, title, original_file_name, relative_path, source_relative_path,
                              mime_type, file_size_bytes, upload_status, processing_phase,
                              processing_progress, error_reason, created_at, updated_at
                    """
                ),
                {
                    "title": title,
                    "original_file_name": filename,
                    "relative_path": relative_path,
                    "mime_type": mime_type,
                    "file_size_bytes": file_size_bytes,
                    "error_reason": error_reason,
                    "uploaded_by": uploaded_by,
                },
            )
            .mappings()
            .one()
        )
    return dict(row)


def _create_media_asset_record_from_file(
    *,
    title: str,
    filename: str,
    source_path: Path,
    content_type: str | None,
    uploaded_by: str | None,
    replace_asset_id: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    file_size = source_path.stat().st_size if source_path.exists() else 0
    validation = validate_media_file(filename, b"x" * min(file_size, 1), content_type)
    if not validation.ok and validation.error != "file_too_large":
        return _insert_failed_asset(
            title=title,
            filename=filename,
            relative_path=f"failed/{secrets.token_hex(16)}{Path(filename).suffix.lower()}",
            mime_type=validation.mime_type,
            file_size_bytes=file_size,
            error_reason=validation.error,
            uploaded_by=uploaded_by,
        )
    max_bytes = get_settings().max_media_upload_mb * 1024 * 1024
    if file_size > max_bytes:
        return _insert_failed_asset(
            title=title,
            filename=filename,
            relative_path=f"failed/{secrets.token_hex(16)}{Path(filename).suffix.lower()}",
            mime_type=validation.mime_type,
            file_size_bytes=file_size,
            error_reason="file_too_large",
            uploaded_by=uploaded_by,
        )
    if file_size <= 0:
        return _insert_failed_asset(
            title=title,
            filename=filename,
            relative_path=f"failed/{secrets.token_hex(16)}{Path(filename).suffix.lower()}",
            mime_type=validation.mime_type,
            file_size_bytes=file_size,
            error_reason="empty_file",
            uploaded_by=uploaded_by,
        )

    digest = checksum_sha256_file(source_path)
    existing = _find_exact_asset(digest, file_size)
    if existing and not replace_asset_id:
        try:
            source_path.unlink(missing_ok=True)
        except OSError:
            pass
        existing["reused_existing"] = True
        existing["duplicate_type"] = "exact"
        return existing

    asset_id = _asset_id()
    destination, relative_path = _source_media_path(asset_id, filename)
    if source_path.resolve() != destination.resolve():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source_path), destination)
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    INSERT INTO media_assets (
                      id, title, original_file_name, relative_path, source_relative_path,
                      checksum_sha256, mime_type, file_size_bytes, upload_status,
                      processing_phase, processing_progress, uploaded_by, replaced_by, metadata
                    )
                    VALUES (
                      CAST(:id AS uuid), :title, :original_file_name, :relative_path, :source_relative_path,
                      :checksum_sha256, :mime_type, :file_size_bytes, 'processing',
                      'queued', 0, CAST(:uploaded_by AS uuid), CAST(:replaced_by AS uuid),
                      CAST(:metadata AS jsonb)
                    )
                    RETURNING id, title, original_file_name, relative_path, source_relative_path,
                              checksum_sha256, mime_type, file_size_bytes, upload_status,
                              processing_phase, processing_progress, error_reason,
                              created_at, updated_at
                    """
                ),
                {
                    "id": asset_id,
                    "title": title,
                    "original_file_name": filename,
                    "relative_path": relative_path,
                    "source_relative_path": relative_path,
                    "checksum_sha256": digest,
                    "mime_type": validation.mime_type,
                    "file_size_bytes": file_size,
                    "uploaded_by": uploaded_by,
                    "replaced_by": replace_asset_id,
                    "metadata": _json_param(metadata or {}),
                },
            )
            .mappings()
            .one()
        )
        if replace_asset_id:
            session.execute(
                text(
                    """
                    UPDATE media_assets
                    SET upload_status = 'replaced',
                        replaced_by = CAST(:new_asset_id AS uuid),
                        updated_at = now()
                    WHERE id = CAST(:old_asset_id AS uuid)
                    """
                ),
                {"new_asset_id": row["id"], "old_asset_id": replace_asset_id},
            )
    _enqueue_processing_job(str(row["id"]), metadata={"source": "upload"})
    return dict(row)


def create_media_asset(
    *,
    title: str,
    filename: str,
    content: bytes,
    content_type: str | None,
    uploaded_by: str | None,
    replace_asset_id: str | None = None,
) -> dict[str, Any]:
    validation = validate_media_file(filename, content, content_type)
    if not validation.ok:
        return _insert_failed_asset(
            title=title,
            filename=filename,
            relative_path=f"failed/{secrets.token_hex(16)}{Path(filename).suffix.lower()}",
            mime_type=validation.mime_type,
            file_size_bytes=validation.file_size_bytes,
            error_reason=validation.error,
            uploaded_by=uploaded_by,
        )

    absolute_path, relative_path = _safe_media_path(filename)
    absolute_path.write_bytes(content)
    return _create_media_asset_record_from_file(
        title=title,
        filename=filename,
        source_path=absolute_path,
        content_type=content_type,
        uploaded_by=uploaded_by,
        replace_asset_id=replace_asset_id,
        metadata={"legacy_upload_path": relative_path},
    )


def complete_resumable_upload(
    *,
    title: str,
    upload_id: str,
    filename: str,
    content_type: str | None,
    uploaded_by: str | None,
    checksum_sha256_value: str | None = None,
) -> dict[str, Any]:
    if not upload_id or "/" in upload_id or "\\" in upload_id or upload_id in {".", ".."}:
        raise ValueError("Invalid upload id")
    settings = get_settings()
    upload_path = _resolve_media_relative((Path(settings.tus_upload_dir) / upload_id).as_posix())
    if not upload_path.exists():
        raise FileNotFoundError("Uploaded file not found")
    if checksum_sha256_value:
        actual = checksum_sha256_file(upload_path)
        if actual.lower() != checksum_sha256_value.lower():
            raise ValueError("Uploaded file checksum does not match")
    return _create_media_asset_record_from_file(
        title=title,
        filename=filename,
        source_path=upload_path,
        content_type=content_type,
        uploaded_by=uploaded_by,
        metadata={"resumable_upload_id": upload_id},
    )


def list_media_assets(upload_status: str | None = None, limit: int = 200) -> dict[str, Any]:
    filters = []
    params: dict[str, Any] = {"limit": limit}
    if upload_status:
        filters.append("upload_status = :upload_status")
        params["upload_status"] = upload_status
    where_clause = "WHERE " + " AND ".join(filters) if filters else ""
    with db_session() as session:
        rows = [
            dict(row)
            for row in session.execute(
                text(
                    f"""
                    SELECT id, title, original_file_name, relative_path, checksum_sha256,
                           source_relative_path, thumbnail_relative_path, playback_relative_path,
                           playback_mime_type, mime_type, file_size_bytes, duration_seconds,
                           width, height, fps, bitrate, video_codec, audio_codec,
                           upload_status, processing_phase, processing_progress,
                           error_reason, created_at, updated_at,
                           (
                             SELECT COUNT(*)
                             FROM media_bindings mb
                             WHERE mb.media_asset_id = media_assets.id
                               AND mb.status <> 'archived'
                           ) AS association_count
                           ,
                           (
                             SELECT jsonb_build_object(
                               'id', mpj.id,
                               'status', mpj.status,
                               'phase', mpj.phase,
                               'progress', mpj.progress,
                               'attempts', mpj.attempts,
                               'error_reason', mpj.error_reason,
                               'updated_at', mpj.updated_at
                             )
                             FROM media_processing_jobs mpj
                             WHERE mpj.media_asset_id = media_assets.id
                             ORDER BY mpj.created_at DESC
                             LIMIT 1
                           ) AS processing_job,
                           COALESCE((
                             SELECT jsonb_agg(jsonb_build_object(
                               'id', mr.id,
                               'kind', mr.kind,
                               'relative_path', mr.relative_path,
                               'mime_type', mr.mime_type,
                               'file_size_bytes', mr.file_size_bytes,
                               'duration_seconds', mr.duration_seconds,
                               'width', mr.width,
                               'height', mr.height,
                               'status', mr.status,
                               'video_codec', mr.video_codec,
                               'audio_codec', mr.audio_codec
                             ) ORDER BY mr.kind)
                             FROM media_renditions mr
                             WHERE mr.media_asset_id = media_assets.id
                           ), '[]'::jsonb) AS renditions,
                           COALESCE((
                             SELECT jsonb_agg(jsonb_build_object(
                               'id', mdc.id,
                               'duplicate_type', mdc.duplicate_type,
                               'score', mdc.score,
                               'algorithm', mdc.algorithm,
                               'status', mdc.status,
                               'candidate_asset_id', mdc.candidate_asset_id,
                               'candidate_title', candidate.title,
                               'candidate_thumbnail_relative_path', candidate.thumbnail_relative_path
                             ) ORDER BY mdc.created_at DESC)
                             FROM media_duplicate_candidates mdc
                             LEFT JOIN media_assets candidate ON candidate.id = mdc.candidate_asset_id
                             WHERE mdc.media_asset_id = media_assets.id
                           ), '[]'::jsonb) AS duplicate_candidates
                    FROM media_assets
                    {where_clause}
                    ORDER BY created_at DESC
                    LIMIT :limit
                    """
                ),
                params,
            )
            .mappings()
            .all()
        ]
    return {"items": [_row_dict(row) for row in rows], "total": len(rows)}


def active_media_processing_status(limit: int = 200) -> dict[str, Any]:
    with db_session() as session:
        rows = [
            dict(row)
            for row in session.execute(
                text(
                    """
                    SELECT ma.id, ma.upload_status, ma.processing_phase, ma.processing_progress,
                           ma.error_reason, ma.thumbnail_relative_path, ma.playback_relative_path,
                           mpj.id AS job_id, mpj.status AS job_status, mpj.phase AS job_phase,
                           mpj.progress AS job_progress, mpj.error_reason AS job_error_reason,
                           mpj.updated_at AS job_updated_at
                    FROM media_assets ma
                    LEFT JOIN LATERAL (
                      SELECT id, status, phase, progress, error_reason, updated_at
                      FROM media_processing_jobs
                      WHERE media_asset_id = ma.id
                      ORDER BY created_at DESC
                      LIMIT 1
                    ) mpj ON true
                    WHERE ma.upload_status IN ('pending', 'processing', 'failed')
                    ORDER BY ma.updated_at DESC
                    LIMIT :limit
                    """
                ),
                {"limit": limit},
            )
            .mappings()
            .all()
        ]
    return {"items": rows, "total": len(rows)}


def retry_media_processing(asset_id: str) -> dict[str, Any]:
    with db_session() as session:
        asset = (
            session.execute(
                text("SELECT id FROM media_assets WHERE id = CAST(:asset_id AS uuid)"),
                {"asset_id": asset_id},
            )
            .mappings()
            .first()
        )
    if not asset:
        raise ValueError("Media asset not found")
    return _enqueue_processing_job(asset_id, metadata={"source": "admin_retry"})


def decide_duplicate_candidate(candidate_id: str, *, decision: str, actor_user_id: str | None) -> dict[str, Any]:
    if decision not in {"kept", "reused", "ignored"}:
        raise ValueError("Invalid duplicate candidate decision")
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    UPDATE media_duplicate_candidates
                    SET status = :decision,
                        decided_by = CAST(:actor_user_id AS uuid),
                        decided_at = now(),
                        updated_at = now()
                    WHERE id = CAST(:candidate_id AS uuid)
                    RETURNING id, media_asset_id, candidate_asset_id, duplicate_type,
                              score, algorithm, status, decided_at, updated_at
                    """
                ),
                {
                    "candidate_id": candidate_id,
                    "decision": decision,
                    "actor_user_id": actor_user_id,
                },
            )
            .mappings()
            .first()
        )
    if not row:
        raise ValueError("Duplicate candidate not found")
    return dict(row)


def create_media_binding(
    *,
    media_asset_id: str,
    target_type: str,
    target_id: str,
    title: str | None,
    status: str = "draft",
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metadata_json = json.dumps(metadata or {}, ensure_ascii=False)
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    INSERT INTO media_bindings (
                      media_asset_id, target_type, target_id, title, status, metadata
                    )
                    VALUES (
                      CAST(:media_asset_id AS uuid), :target_type, :target_id, :title, :status,
                      CAST(:metadata AS jsonb)
                    )
                    ON CONFLICT (media_asset_id, target_type, target_id) DO UPDATE SET
                      title = EXCLUDED.title,
                      status = EXCLUDED.status,
                      metadata = media_bindings.metadata || EXCLUDED.metadata,
                      updated_at = now()
                    RETURNING id, media_asset_id, target_type, target_id, title, status,
                              metadata, created_at, updated_at
                    """
                ),
                {
                    "media_asset_id": media_asset_id,
                    "target_type": target_type,
                    "target_id": target_id,
                    "title": title,
                    "status": status,
                    "metadata": metadata_json,
                },
            )
            .mappings()
            .one()
        )
    return dict(row)


def publish_media_binding(binding_id: str, actor_user_id: str | None) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    UPDATE media_bindings
                    SET status = 'published',
                        published_by = CAST(:actor AS uuid),
                        published_at = now(),
                        updated_at = now()
                    WHERE id = CAST(:binding_id AS uuid)
                    RETURNING id, media_asset_id, target_type, target_id, title, status,
                              published_at, updated_at
                    """
                ),
                {"binding_id": binding_id, "actor": actor_user_id},
            )
            .mappings()
            .first()
        )
    if not row:
        raise ValueError("Media binding not found")
    return dict(row)


def unpublish_media_binding(binding_id: str) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    UPDATE media_bindings
                    SET status = 'draft',
                        published_by = NULL,
                        published_at = NULL,
                        updated_at = now()
                    WHERE id = CAST(:binding_id AS uuid)
                      AND status <> 'archived'
                    RETURNING id, media_asset_id, target_type, target_id, title, status,
                              published_at, updated_at
                    """
                ),
                {"binding_id": binding_id},
            )
            .mappings()
            .first()
        )
    if not row:
        raise ValueError("Media binding not found")
    return dict(row)


def delete_media_binding(binding_id: str) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    DELETE FROM media_bindings
                    WHERE id = CAST(:binding_id AS uuid)
                    RETURNING id, media_asset_id, target_type, target_id, title, status,
                              published_at, updated_at
                    """
                ),
                {"binding_id": binding_id},
            )
            .mappings()
            .first()
        )
    if not row:
        raise ValueError("Media binding not found")
    return dict(row)
