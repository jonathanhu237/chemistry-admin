# Production Media Cleanup Plan

`data/media/` is local uploaded/transcoded video storage, not a protected production seed resource. It can be removed from a clean production baseline, but only together with database/UI consistency handling because `media_assets` rows can point to local files.

Current cleanup policy:

- Do not delete `data/media/` from the guarded legacy artifact cleanup script.
- Before deleting local media files, inspect `media_assets` and `media_bindings`.
- If media is no longer part of the current platform baseline, archive or delete the corresponding `media_assets` rows in the same maintenance step that removes files.
- If keeping media records for UI smoke tests, replace large local files with a tiny documented sample set and update records to point only to existing files.
- After any media cleanup, the admin UI must not list assets whose local files are missing.

Reference checks:

```sql
SELECT COUNT(*) FROM media_assets;
SELECT COUNT(*) FROM media_bindings;
SELECT id, file_name, storage_path, status FROM media_assets ORDER BY created_at DESC;
```

The production resource manifest intentionally excludes `data/media/`; videos are disposable unless a future spec promotes a small sample set to a protected seed resource.
