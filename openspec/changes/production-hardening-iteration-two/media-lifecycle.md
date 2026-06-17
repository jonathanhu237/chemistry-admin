# Media Lifecycle Hardening

## Implemented Scope

- Added per-asset filesystem summaries to the admin media listing without changing media upload, binding, or playback semantics.
- Added `file_state`, `primary_file_available`, file counts, and `media_files` entries so the UI can distinguish available, partial, missing, pending, and untracked local media.
- Added a guarded media cleanup dry-run CLI at `scripts/media_lifecycle_cleanup.py`.
- Kept destructive behavior intentionally narrow: DB-backed media asset file deletion refuses until an archive/tombstone state exists; orphan deletion only touches files under `media_root` that are not referenced by current media database rows.
- Updated the video resources UI to display missing/partial file states and disable previews when the primary local media file is unavailable.
- Updated production media cleanup documentation with current schema fields and the new dry-run/refusal workflow.

## Dependency Model

The dry-run reports each inspected asset with dependency counts from:

- `media_bindings`
- `media_processing_jobs`
- `media_renditions`
- `media_video_fingerprints`
- `media_duplicate_candidates`

The orphan scan uses all referenced paths from `media_assets` and `media_renditions`, independent of the inspected asset limit, so small dry-runs do not mark files from unlisted DB rows as orphaned.

## Deletion Policy

- Keep assets with active bindings.
- Keep ready assets without bindings unless a later archive flow explicitly retires them.
- Review missing-file records instead of deleting them automatically.
- Treat failed/replaced records as manual archive/delete candidates.
- Delete only unreferenced local orphan files when `--delete-orphans` is explicitly passed.

## Verification

Run:

```powershell
python -m pytest server\tests\test_media_lifecycle.py -q
python scripts/media_lifecycle_cleanup.py --json --limit 20 --orphan-limit 20
python scripts/media_lifecycle_cleanup.py --delete-asset-files --limit 5
npm run typecheck
```

The `--delete-asset-files` command must exit with code `2`.

Observed in this pass:

- `python -m pytest server\tests\test_media_lifecycle.py -q`: 3 passed.
- `python -m pytest server\tests -q`: 47 passed.
- `python scripts/media_lifecycle_cleanup.py --json --limit 20 --orphan-limit 20`: dry-run completed with 10 assets, 30 referenced paths, and 17 orphan local files reported.
- `python scripts/media_lifecycle_cleanup.py --delete-asset-files --limit 5`: refused DB-backed deletion with exit code `2`.
- Browser smoke on `http://localhost:5174/admin/videos`: 10 video cards and 10 preview buttons loaded after backend rebuild; all current assets were `available`, so no missing/partial file badge was shown.
