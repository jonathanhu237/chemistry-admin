## 1. Backend Delete Semantics

- [x] 1.1 Add a media asset delete impact plan domain function that reports active catalog bindings, legacy bindings, active processing jobs, renditions, thumbnails, fingerprints, duplicate candidates, and safe local artifact paths.
- [x] 1.2 Add authenticated admin delete-plan and delete command routes for media assets, leaving existing archive routes unused by the teacher resource flow.
- [x] 1.3 Implement destructive delete orchestration: make the asset unavailable, cancel queued/running processing jobs, remove point video bindings, remove duplicate candidate references, and preserve point content/questions/publication state.
- [x] 1.4 Implement safe local artifact deletion for source, playback, thumbnail, rendition, fingerprint, and temp/analysis files with `MEDIA_ROOT` path containment checks.
- [x] 1.5 Add cleanup diagnostics for partial delete failures so remaining records are unavailable and repairable without reactivating the asset.
- [x] 1.6 Add backend tests for delete plan output, bound asset deletion, active processing cancellation, duplicate candidate cleanup, file path safety, and failed cleanup diagnostics.

## 2. Duplicate Detection Semantics

- [x] 2.1 Rename internal and API/read-model semantics from similarity analysis to duplicate detection where teacher-facing behavior depends on it.
- [x] 2.2 Add duplicate-detection settings for duration tolerance, default sample interval, minimum sample count, minimum sample interval, and high-confidence threshold.
- [x] 2.3 Implement near-equal duration candidate filtering with default tolerance equivalent to `clamp(duration_seconds * 0.001, 0.5, 2.0)` seconds.
- [x] 2.4 Add or adjust database access/indexing so duplicate candidates are filtered by active lifecycle, ready playback, algorithm compatibility, and duration range before perceptual compare commands run.
- [x] 2.5 Update the vPDQ helper or command environment so the effective seconds-per-hash can be computed from video duration using duplicate-focused sampling defaults.
- [x] 2.6 Update worker comparison to persist only suspected full-video duplicates and never emit contained clip, partial overlap, shared-intro, or generic similarity outcomes.
- [x] 2.7 Preserve playback readiness when duplicate detection is queued, running, skipped, failed, or retried.
- [x] 2.8 Add worker/domain tests for exact SHA duplicate reuse, duration-gated visual candidate selection, materially different duration exclusion, missing duration skip behavior, dynamic sample interval, empty candidate fast completion, and duplicate-only retry.

## 3. Teacher Resource UI

- [x] 3.1 Replace archive labels, confirmation copy, success messages, and action names with delete terminology in the video resource library.
- [x] 3.2 Wire stored resource delete actions to the new delete-plan/delete APIs and remove teacher flow usage of archive APIs.
- [x] 3.3 Show delete confirmation impact for point bindings, student-visible bindings, active processing jobs, and local media artifact removal.
- [x] 3.4 Update duplicate-detection badges, progress lines, retry buttons, and preview detail copy to use duplicate-only terminology instead of similarity/relationship wording.
- [x] 3.5 Ensure ready assets remain previewable/playable while duplicate detection is running or failed.
- [x] 3.6 Add/update teacher frontend contract tests for delete wording/API calls, upload queue removal separation, duplicate-detection labels, and preview availability during duplicate detection.

## 4. Upload Queue Manager

- [x] 4.1 Extract upload queue ownership from the upload modal into a modal-independent upload manager or provider that remains mounted while the teacher app is active.
- [x] 4.2 Change upload modal close behavior to hide/minimize the queue without destroying Uppy, aborting XHR, clearing selected items, or cancelling active work.
- [x] 4.3 Add explicit cancel-current-file and cancel-queue controls that are the only user actions that abort active upload work.
- [x] 4.4 Add a visible active upload indicator or reopen control outside the modal so teachers can monitor minimized uploads.
- [x] 4.5 Implement stage 0 validation for all selected files before hashing/uploading, including type and effective `MAX_MEDIA_UPLOAD_MB` rejection.
- [x] 4.6 Implement bounded checksum/precheck concurrency for multi-file queues.
- [x] 4.7 Implement bounded resumable upload concurrency and per-item finalization so completed uploads enqueue backend processing without waiting for the whole selection.
- [x] 4.8 Add per-item retry/cancel/progress states and queue-level progress that distinguishes browser upload/finalization from backend playback processing and duplicate detection.
- [x] 4.9 Add frontend tests or focused contract coverage for modal close persistence, explicit cancellation, serial-to-pipeline behavior, oversized rejection, and per-item finalization.

## 5. Documentation And Migration

- [x] 5.1 Update local video processing docs to describe duplicate detection, duration gating, duplicate-focused sampling, and the fact that partial overlaps are out of scope.
- [x] 5.2 Update deployment/config docs for new duplicate-detection settings and recommended defaults.
- [x] 5.3 Document teacher delete behavior, physical media artifact cleanup, and existing archived-media maintenance guidance.
- [x] 5.4 Document upload queue limitations: uploads continue while the teacher app remains mounted, but browser tab close requires later tus resume with access to the same file.
- [x] 5.5 Add migration or maintenance notes for existing archived assets and existing vPDQ fingerprints created with the old 1s similarity policy.

## 6. Verification

- [x] 6.1 Run targeted backend tests for media lifecycle, media assets, media processing queue, and video worker pipeline.
- [x] 6.2 Run targeted frontend tests for `web-teacher` media/resource contracts and any extracted upload manager tests.
- [x] 6.3 Run typecheck/lint/build for affected frontend and backend packages according to repository scripts.
- [x] 6.4 Run an end-to-end local smoke test with multiple video uploads: one exact duplicate, one re-encoded same-duration duplicate, one different-duration non-duplicate, and one deleted resource.
- [x] 6.5 Verify Docker compose services after changes, including backend, tusd, video-worker, and web-teacher rebuild/restart instructions.
