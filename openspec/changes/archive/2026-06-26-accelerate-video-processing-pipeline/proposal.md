## Why

Large teacher-uploaded videos currently become usable only after the entire video worker chain finishes. A successful learning rendition can be blocked behind slow CPU-only transcode progress, vPDQ fingerprint generation on the original 4K source, and duplicate comparison, leaving teachers with a long "processing" card even when a student playback source already exists.

This change makes playback availability the first-class outcome of media processing, improves worker acceleration and fallback behavior, and surfaces real processing progress so operators can tell whether the worker is active.

## What Changes

- Split playback readiness from asynchronous similarity analysis: thumbnail and learning rendition completion SHALL make a media asset previewable/playable while fingerprinting and duplicate comparison continue in the background.
- Add video worker transcode acceleration policy with `auto`, `cpu`, and `nvenc` modes. `auto` prefers NVIDIA NVENC when a runtime probe succeeds and falls back to CPU `libx264` when unavailable or failing.
- Add FFmpeg progress parsing during learning rendition generation so long transcodes report meaningful progress instead of staying fixed at the phase default.
- Change similarity fingerprint source selection so the worker can prefer the generated learning rendition for vPDQ signatures, avoiding repeated decoding of oversized original 4K sources when a playback source exists.
- Treat similarity-analysis failure as a non-blocking analysis failure when playback output is already available, while still surfacing diagnostics for retry or maintenance.
- Update teacher video resource UI semantics so assets with a playback source can be previewed during background analysis and display "similarity analysis in progress" separately from playback processing.

## Capabilities

### New Capabilities

- `video-worker-processing-pipeline`: Worker-side media processing policy, acceleration, progress reporting, playback readiness, and asynchronous similarity analysis.

### Modified Capabilities

- `media-asset-lifecycle`: Media assets shall distinguish playback readiness from later analysis completion and keep diagnostics for non-blocking analysis failures.
- `teacher-video-resource-library`: Teacher video resource cards shall allow preview once playback output exists and show processing/analysis state accurately.

## Impact

- Backend worker: `server/app/workers/video_worker.py`, media processing queue persistence, settings, and worker tests.
- Backend media APIs/read models: media asset status fields and processing diagnostics consumed by the teacher video library.
- Teacher frontend: video resource card progress, preview button eligibility, labels, and focused contract tests.
- Configuration and operations: `.env.example`, `docker-compose.yml`, and local Docker GPU runtime expectations for `video-worker`.
- Documentation: local video processing operations for GPU fallback, progress, and background similarity analysis.
