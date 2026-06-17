# Production Media Cleanup Plan

`data/media/` is local uploaded/transcoded video storage, not a protected production seed resource. It can be removed from a clean production baseline, but only together with database/UI consistency handling because `media_assets` rows can point to local files.

Current cleanup policy:

- Do not delete `data/media/` from the guarded legacy artifact cleanup script.
- Before deleting local media files, run `python scripts/media_lifecycle_cleanup.py --json` and inspect `media_assets`, `media_bindings`, `media_processing_jobs`, `media_renditions`, `media_video_fingerprints`, and `media_duplicate_candidates`.
- The cleanup script defaults to dry-run and reports `file_state`, dependency counts, candidate actions, referenced paths, orphan files, and byte impact.
- `--delete-asset-files` intentionally refuses DB-backed media files until the platform has an explicit archive/tombstone state for asset records.
- `--delete-orphans` may delete only files under `data/media/` that are not referenced by any `media_assets` or `media_renditions` path column.
- If media is no longer part of the current platform baseline, archive or delete the corresponding database rows in the same maintenance step that removes files.
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

Expected refusal for DB-backed asset file deletion:

```powershell
python scripts/media_lifecycle_cleanup.py --delete-asset-files
```

Reference checks:

```sql
SELECT COUNT(*) FROM media_assets;
SELECT COUNT(*) FROM media_bindings;
SELECT id, title, original_file_name, relative_path, source_relative_path, playback_relative_path,
       thumbnail_relative_path, upload_status
FROM media_assets
ORDER BY created_at DESC;

SELECT media_asset_id, status, COUNT(*)
FROM media_bindings
GROUP BY media_asset_id, status
ORDER BY media_asset_id, status;
```

The production resource manifest intentionally excludes `data/media/`; videos are disposable unless a future spec promotes a small sample set to a protected seed resource.
