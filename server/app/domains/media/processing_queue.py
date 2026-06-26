from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from sqlalchemy import text

from server.app.domains.media.files import PROCESSING_JOB_TYPE, json_param
from server.app.infrastructure.database import db_session
from server.app.infrastructure.settings import get_settings


PHASE_PROGRESS = {
    "starting": 1,
    "validating": 5,
    "probing": 15,
    "thumbnailing": 30,
    "transcoding": 60,
    "fingerprinting": 78,
    "comparing": 90,
    "analysis_failed": 100,
    "duplicate_detection_failed": 100,
    "ready": 100,
    "failed": 0,
}


@dataclass(frozen=True)
class WorkerJob:
    id: str
    media_asset_id: str
    attempts: int
    job_type: str = PROCESSING_JOB_TYPE
    metadata: dict[str, Any] | None = None

    @property
    def preserves_ready_playback(self) -> bool:
        return self.job_type == "backfill_legacy_video" or self.retry_scope in {"duplicate_detection", "similarity"}

    @property
    def retry_scope(self) -> str | None:
        return str((self.metadata or {}).get("retry_scope") or "") or None

    @property
    def duplicate_detection_only(self) -> bool:
        return self.retry_scope in {"duplicate_detection", "similarity"}

    @property
    def similarity_only(self) -> bool:
        return self.duplicate_detection_only


def relative_media_path(path: Path) -> str:
    root = get_settings().media_root.resolve()
    return path.resolve().relative_to(root).as_posix()


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
                      SELECT mpj.id
                      FROM media_processing_jobs mpj
                      JOIN media_assets ma ON ma.id = mpj.media_asset_id
                      WHERE mpj.status = 'queued'
                        AND mpj.attempts < mpj.max_attempts
                        AND COALESCE(ma.lifecycle_status, 'active') = 'active'
                      ORDER BY mpj.created_at
                      FOR UPDATE SKIP LOCKED
                      LIMIT 1
                    )
                    RETURNING id, media_asset_id, attempts, job_type, metadata
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
        job_type=str(row["job_type"] or PROCESSING_JOB_TYPE),
        metadata=dict(row["metadata"] or {}),
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
                "metadata": json_param(metadata or {}),
            },
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = CASE
                      WHEN :preserve_ready_playback OR upload_status = 'ready' THEN upload_status
                      ELSE 'processing'
                    END,
                    processing_phase = :phase,
                    processing_progress = :progress,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                """
            ),
            {
                "asset_id": job.media_asset_id,
                "phase": phase,
                "progress": next_progress,
                "preserve_ready_playback": job.preserves_ready_playback,
            },
        )


def mark_asset_playback_ready(
    job: WorkerJob,
    *,
    phase: str = "fingerprinting",
    progress: int | None = None,
    metadata: dict[str, Any] | None = None,
) -> None:
    next_progress = PHASE_PROGRESS.get(phase, progress or 100) if progress is None else progress
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
                "metadata": json_param(metadata or {}),
            },
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = 'ready',
                    processing_phase = :phase,
                    processing_progress = :progress,
                    error_reason = NULL,
                    processed_at = COALESCE(processed_at, now()),
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                """
            ),
            {
                "asset_id": job.media_asset_id,
                "phase": phase,
                "progress": next_progress,
            },
        )


def fail_job(job: WorkerJob, error: str, *, preserve_ready_playback: bool | None = None) -> None:
    message = error[:1000]
    preserve_playback = job.preserves_ready_playback if preserve_ready_playback is None else preserve_ready_playback
    asset_phase = "duplicate_detection_failed" if preserve_playback else "failed"
    asset_progress = PHASE_PROGRESS[asset_phase]
    asset_error_reason = None if preserve_playback else message
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
                      WHEN :preserve_ready_playback THEN 'ready'
                      ELSE 'failed'
                    END,
                    processing_phase = :asset_phase,
                    processing_progress = :asset_progress,
                    error_reason = :error_reason,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                """
            ),
            {
                "asset_id": job.media_asset_id,
                "asset_phase": asset_phase,
                "asset_progress": asset_progress,
                "error_reason": asset_error_reason,
                "preserve_ready_playback": preserve_playback,
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
            {"job_id": job.id, "outputs": json_param(outputs)},
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
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                """
            ),
            {"asset_id": job.media_asset_id},
        )


def load_processing_asset(asset_id: str) -> dict[str, Any]:
    with db_session() as session:
        row = (
            session.execute(
                text(
                    """
                    SELECT id, title, original_file_name, relative_path, source_relative_path,
                           playback_relative_path,
                           checksum_sha256, mime_type, file_size_bytes, duration_seconds
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


def persist_video_probe(asset_id: str, metadata: dict[str, Any]) -> None:
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
                  AND COALESCE(lifecycle_status, 'active') = 'active'
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
                "metadata": json_param({"video_probe": metadata}),
            },
        )


def persist_learning_rendition(asset_id: str, rendition: Path, metadata: dict[str, Any], policy: dict[str, Any]) -> None:
    relative_path = relative_media_path(rendition)
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
                "metadata": json_param(policy),
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
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                """
            ),
            {"asset_id": asset_id, "playback_relative_path": relative_path},
        )


def persist_thumbnail(asset_id: str, thumbnail: Path) -> None:
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
            {"asset_id": asset_id, "thumbnail_relative_path": relative_media_path(thumbnail)},
        )


def persist_video_fingerprint(
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
                "metadata": json_param(metadata),
            },
        )


def persist_duplicate_candidate(asset_id: str, match: dict[str, Any]) -> None:
    metadata = {"source": "video_worker", **dict(match.get("metadata") or {})}
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
                "metadata": json_param(metadata),
            },
        )


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
                        AND COALESCE(ma.lifecycle_status, 'active') = 'active'
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


def enqueue_processing_job(
    asset_id: str,
    *,
    metadata: dict[str, Any] | None = None,
    preserve_ready_playback: bool = False,
) -> dict[str, Any]:
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
                    "metadata": json_param(metadata or {}),
                },
            )
            .mappings()
            .one()
        )
        session.execute(
            text(
                """
                UPDATE media_assets
                SET upload_status = CASE
                      WHEN :preserve_ready_playback AND upload_status = 'ready' THEN 'ready'
                      ELSE 'processing'
                    END,
                    processing_phase = 'queued',
                    processing_progress = 0,
                    updated_at = now()
                WHERE id = CAST(:asset_id AS uuid)
                  AND upload_status <> 'replaced'
                  AND COALESCE(lifecycle_status, 'active') = 'active'
                """
            ),
            {"asset_id": asset_id, "preserve_ready_playback": preserve_ready_playback},
        )
    return dict(row)


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
                    WHERE COALESCE(ma.lifecycle_status, 'active') = 'active'
                      AND (
                        ma.upload_status IN ('pending', 'processing', 'failed')
                        OR (
                          ma.upload_status = 'ready'
                          AND (
                            mpj.status IN ('queued', 'processing')
                            OR ma.processing_phase IN ('analysis_failed', 'duplicate_detection_failed')
                          )
                        )
                      )
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
                text(
                    """
                    SELECT id, upload_status, processing_phase, playback_relative_path
                    FROM media_assets
                    WHERE id = CAST(:asset_id AS uuid)
                      AND COALESCE(lifecycle_status, 'active') = 'active'
                    """
                ),
                {"asset_id": asset_id},
            )
            .mappings()
            .first()
        )
    if not asset:
        raise ValueError("Media asset not found")
    duplicate_detection_only = (
        asset.get("upload_status") == "ready"
        and asset.get("processing_phase") in {"analysis_failed", "duplicate_detection_failed"}
        and bool(asset.get("playback_relative_path"))
    )
    metadata = {"source": "admin_retry"}
    if duplicate_detection_only:
        metadata["retry_scope"] = "duplicate_detection"
    return enqueue_processing_job(asset_id, metadata=metadata, preserve_ready_playback=duplicate_detection_only)
