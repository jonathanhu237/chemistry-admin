## Why

The teacher video resource workflow currently mixes four different concerns: browser upload, backend playback processing, vPDQ similarity analysis, and asset archival. That makes large uploads feel like foreground tasks, makes background analysis look like unfinished processing, keeps "archived" media around when teachers expect deletion, and spends worker time on broad content relationship analysis that is not useful for this system.

This change narrows the product goal to true duplicate-video detection, makes deletion semantics explicit, and turns multi-file upload into a queue that can continue without forcing the teacher to babysit a modal.

## What Changes

- Replace broad "similarity analysis" semantics with "duplicate video detection" only.
- Restrict visual duplicate detection candidates to videos with nearly equal duration before running perceptual comparison.
- Treat SHA-256 byte identity as the authoritative exact duplicate path and visual matching as a secondary path for re-encoded copies of the same full video.
- Remove product support for detecting or surfacing partial overlaps, contained clips, shared intros/outros, or general content similarity.
- Change vPDQ sampling policy away from default 1 second per hash for long videos; use a simpler duplicate-focused sampling policy, such as 3 seconds per hash with a short-video minimum sample guard.
- Keep duplicate detection asynchronous and non-blocking once thumbnail and student playback output are ready.
- Replace teacher-facing "archive" behavior in the video resource library with true delete semantics: deleted media is no longer retained as a teacher-visible resource and local media artifacts are removed.
- Add impact-aware delete planning that explains affected point video bindings before destructive deletion.
- Decouple the upload queue from the upload modal so closing the modal minimizes/hides queue UI instead of cancelling browser upload state.
- Change multi-file upload from fully serial processing to a bounded pipeline: size validation first, checksum precheck with limited concurrency, resumable upload with bounded concurrency, and backend processing enqueue per completed file.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `teacher-video-resource-library`: replace archive wording/actions with delete semantics, clarify duplicate-detection UI, make the upload queue independent of the modal, and support bounded multi-file upload pipeline behavior.
- `media-asset-lifecycle`: replace archive-as-retention behavior for teacher video resources with destructive deletion, narrow vPDQ usage to duration-gated duplicate detection, and keep playback readiness independent from duplicate-detection completion.

## Impact

- Teacher frontend: `apps/web-teacher/src/features/media/VideoResourcesPage.tsx`, media helper labels/statuses, upload queue state ownership, preview/delete actions, focused contract tests, and any extracted upload manager components.
- Backend media API: admin media asset delete planning and delete command endpoints; existing archive endpoints may be retired, kept only for migration/audit, or removed from the teacher resource flow.
- Backend media domain: lifecycle cleanup, catalog point media binding removal, processing job cancellation, duplicate candidate persistence, and file artifact cleanup under `MEDIA_ROOT`.
- Video worker: duplicate detection candidate filtering, vPDQ command configuration, sampling policy, metadata naming, retry behavior, and progress/status reporting.
- Data model and migrations: possible lifecycle event additions for destructive delete, duplicate candidate metadata changes, duration bucketing/indexing, and cleanup of archived-resource assumptions.
- Operations and docs: local video processing docs, deployment notes for duplicate-detection sampling, and any maintenance guidance for existing archived media.
