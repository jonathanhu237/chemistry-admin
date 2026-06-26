# Production Media Cleanup Plan

`data/media/` is local uploaded/transcoded video storage, not a protected production seed resource. It can be removed from a clean production baseline, but only together with database/UI consistency handling because `media_assets` rows can point to local files.

Current cleanup policy:

- Do not delete `data/media/` from the guarded legacy artifact cleanup script.
- Before deleting local media files, run `python scripts/media_lifecycle_cleanup.py --json` and inspect `media_assets`, catalog point media bindings, legacy `media_bindings`, `media_processing_jobs`, `media_renditions`, `media_subtitle_tracks`, `media_video_fingerprints`, and `media_duplicate_candidates`.
- The cleanup script defaults to dry-run and reports `file_state`, dependency counts, candidate actions, referenced paths, orphan files, and byte impact.
- Teacher delete in `/videos` tombstones the `media_assets` row, cancels queued/running media processing jobs, removes point video bindings while preserving point content and publication state, removes subtitle track records/artifacts, removes duplicate-candidate references, and deletes local source/playback/thumbnail/rendition/subtitle/fingerprint/temp artifacts under `MEDIA_ROOT`.
- Subtitle track deletion is narrower than video resource deletion: deleting a subtitle removes only that track's source/WebVTT artifacts and leaves the parent video, playback rendition, thumbnail, point bindings, and duplicate fingerprints intact.
- Existing archived assets from the old retention flow remain hidden legacy records until an operator deliberately tombstones or cleans them; do not silently delete old archived media during deployment.
- `--delete-asset-files` is a maintenance fallback for DB-backed media files on archived or tombstoned asset records. Active assets are refused even when unbound.
- `--delete-orphans` may delete only files under `data/media/` that are not referenced by any `media_assets` or `media_renditions` path column.
- If media is no longer part of the current platform baseline, delete it through the teacher video resource flow when possible; for old archived records, confirm catalog point bindings no longer reference the asset before running maintenance cleanup.
- If keeping media records for UI smoke tests, replace large local files with a tiny documented sample set and update records to point only to existing files.
- After any media cleanup, the admin UI must represent missing local files intentionally: unavailable previews stay disabled and missing files show as media lifecycle state, rather than broken playback links.

Dry-run:

```powershell
python scripts/media_lifecycle_cleanup.py --json --limit 500 --orphan-limit 200
```

Delete only unreferenced local files:

```powershell
python scripts/media_lifecycle_cleanup.py --delete-orphans --limit 500 --orphan-limit 200
```

Delete DB-backed files only for archived or tombstoned assets:

```powershell
python scripts/media_lifecycle_cleanup.py --delete-asset-files
```

The command reports `refused_active_asset_file_asset_ids` when active asset rows still reference files.

Reference checks:

```sql
SELECT COUNT(*) FROM media_assets;
SELECT COUNT(*) FROM media_bindings;
SELECT id, title, original_file_name, relative_path, source_relative_path, playback_relative_path,
       thumbnail_relative_path, upload_status, lifecycle_status, archived_at, archive_reason
FROM media_assets
ORDER BY created_at DESC;

SELECT media_asset_id, status, COUNT(*)
FROM media_bindings
GROUP BY media_asset_id, status
ORDER BY media_asset_id, status;

SELECT media_asset_id, binding_status, COUNT(*)
FROM experiment_catalog_point_media_bindings
GROUP BY media_asset_id, binding_status
ORDER BY media_asset_id, binding_status;

SELECT media_asset_id, event_type, handler_status, handler_error, created_at, handled_at
FROM media_asset_lifecycle_events
ORDER BY created_at DESC
LIMIT 50;

SELECT media_asset_id, status, language_code, label, is_default, source_relative_path, webvtt_relative_path
FROM media_subtitle_tracks
ORDER BY created_at DESC;
```

The production resource manifest intentionally excludes `data/media/`; videos are disposable unless a future spec promotes a small sample set to a protected seed resource.
