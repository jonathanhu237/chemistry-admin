## Context

The current video resource flow grew from a broader media lifecycle model:

- The browser upload queue lives inside `VideoResourcesPage` modal state. Closing the modal resets the queue, destroys the Uppy client, and aborts in-flight upload work.
- Backend media processing produces thumbnail and learning rendition, then marks playback ready before vPDQ work, but the teacher UI still presents duplicate/similarity work as a processing tail.
- vPDQ currently runs with `VIDEO_VPDQ_SECONDS_PER_HASH=1` and compares each new ready fingerprint against every existing ready fingerprint for the same algorithm. That creates full-library linear comparison and uses vPDQ's clip/subsequence strengths even though this product only needs duplicate-video detection.
- Teacher-facing "archive" hides a media asset and retains files/metadata for audit. The user expectation for this page is destructive delete: remove the resource and its local media artifacts.

The product goal for this change is intentionally narrower than generic near-duplicate video retrieval. We only need to identify videos that are truly the same full video after re-encoding or compression. We do not need to detect contained clips, partial overlaps, common intros/outros, or content that merely looks related.

## Goals / Non-Goals

**Goals:**

- Replace "similarity analysis" terminology and behavior with duplicate-focused detection.
- Gate perceptual duplicate comparisons by near-equal duration so the worker does not compare against unrelated videos.
- Preserve fast exact duplicate behavior through SHA-256 and file-size checks.
- Make generated student playback output sufficient for preview/playback even if duplicate detection is still queued, running, skipped, or failed.
- Replace teacher resource "archive" actions with destructive delete actions and impact-aware delete confirmation.
- Ensure deleted teacher video resources are not retained as selectable, previewable, or teacher-visible library assets.
- Decouple upload queue execution from the upload modal and allow the teacher to close/minimize the modal without cancelling active browser upload work.
- Convert multi-file upload into a bounded pipeline with independent item progress and explicit cancel/retry controls.

**Non-Goals:**

- Detecting clips, sub-sequences, partial overlaps, shared openings/endings, or "looks similar" content.
- Building a forensic duplicate-detection system with zero false negatives across arbitrary edits.
- Uploading files after the browser tab or app process has been closed. Browser uploads can continue while the teacher app remains mounted; after tab close, resumable upload can only resume when the user returns and reselects or restores the file.
- Changing student-side video aspect ratio, thumbnail aspect ratio, or learning rendition dimensions.
- Replacing vPDQ/TMK wholesale in this change. The change narrows when and how perceptual comparison is used.

## Decisions

### 1. Rename the product concept to duplicate detection

Teacher-facing UI and backend metadata will stop presenting "similarity analysis" as a first-class task. The teacher video library should display statuses such as "重复检测中", "疑似重复", "未发现重复", and "重复检测失败".

Partial-overlap concepts will not be persisted or surfaced as product outcomes. Existing vPDQ output may still contain directional match percentages internally, but the product decision is binary/advisory: suspected full duplicate or no duplicate signal.

Alternatives considered:

- Keep "similarity analysis" and add labels for contained clips. Rejected because it solves a problem this product does not need and keeps the slowest part of vPDQ in the primary workflow.
- Disable vPDQ entirely. Rejected because re-encoded full duplicates would no longer be detected after SHA-256 misses.

### 2. Use duration as a hard candidate gate, with tolerance

Perceptual duplicate comparison will only run against candidate videos whose source-video durations are nearly equal.

The default tolerance should be:

```text
duration_tolerance_seconds = clamp(duration_seconds * 0.001, 0.5, 2.0)
```

This means:

- 40s and 60s videos are not candidates.
- Short clips get at least 0.5s tolerance to absorb timebase/container noise.
- Long videos allow roughly 0.1% drift but no more than 2s.

Rationale:

- True full-video duplicates, including recompressed files, should preserve the actual viewing duration.
- Exact equality is too strict because ffprobe stream duration, format duration, timebase rounding, audio padding, and encoder/container metadata can differ by fractions of a second.
- Our observed local data already shows same-content source/rendition duration differences around 0.27s for 24-minute videos, while the intended product boundary excludes materially different lengths.

Implementation notes:

- Prefer source video duration stored on `media_assets` for duplicate gating. If absent, use the best available primary video stream duration from probe metadata.
- Add a duration-range query or duration bucket/index so candidate lookup is bounded by duration, lifecycle, readiness, and algorithm instead of scanning all fingerprints.
- The gate is a candidate filter, not the final duplicate decision. A duration match alone never creates a duplicate warning.

Alternatives considered:

- Require exact duration equality. Rejected because media metadata precision varies.
- Use a broad percentage such as 5%. Rejected because it admits many non-duplicates and reintroduces partial-overlap confusion.
- Compare every existing fingerprint. Rejected for performance and product semantics.

### 3. Use a duplicate-focused sampling policy

The vPDQ signature interval should move away from a fixed 1s default for all videos.

Recommended default policy:

```text
default_interval_seconds = 3.0
minimum_hash_samples = 12
minimum_interval_seconds = 0.5
effective_interval = min(default_interval_seconds, max(minimum_interval_seconds, duration_seconds / minimum_hash_samples))
```

This keeps long videos much cheaper while avoiding very short videos producing too few samples. For example:

- 24-minute video: about 484 samples at 3s, instead of about 1452 samples at 1s.
- 40-second video: about 14 samples at 3s.
- 6-second video: about 12 samples at 0.5s.

The exact settings should be configurable, but the defaults should reflect duplicate detection, not clip search.

Alternatives considered:

- Keep 1s everywhere. Rejected because it is expensive and over-targeted for full-video duplicate detection.
- Use one fixed 10s interval. Rejected because short videos would have too few samples.

### 4. Require high-confidence full-duplicate confirmation

After duration gating, perceptual comparison should require high bidirectional coverage before creating a suspected duplicate.

The current helper uses the lower of query-match and compared-match percentages as a conservative score. That remains aligned with full-video duplicate detection: a contained 40s clip inside a 60s video will not pass because only one direction is high.

Recommended defaults:

- Use a high threshold such as 0.95 for suspected duplicate warnings.
- Persist only `duplicate_type = suspected` for full-video duplicate candidates.
- Store diagnostic metadata for score, candidate duration, current duration, tolerance, sample interval, and algorithm version.

### 5. Split playback readiness from duplicate-detection state

Thumbnail and learning rendition completion should make the asset ready for teacher preview and student playback. Duplicate detection should be a background advisory signal.

The read model should avoid showing ready assets as "processing" solely because duplicate detection is queued or running. If duplicate detection needs a visible state, it should be presented as a secondary badge or detail line, not as the primary upload/processing status.

Implementation options:

- Add explicit duplicate-detection status fields or metadata on media assets/read models.
- Or keep processing jobs but have the teacher API expose `playback_ready` and `duplicate_detection_status` separately.

The implementation should choose the smallest data model change that keeps UI semantics clear.

### 6. Replace archive with destructive delete in teacher video resources

The teacher video library delete action should:

- Request a delete impact plan before confirmation.
- Explain active point video bindings, student-visible impact, active processing jobs, duplicate candidates, renditions, fingerprints, thumbnails, source files, and playback artifacts.
- On confirmation, make the asset immediately unavailable to teacher preview, student playback, catalog selectors, duplicate candidate lists, and processing workers.
- Cancel queued/active jobs for the asset.
- Remove or archive point video bindings so points no longer reference the deleted asset while point text/content remains.
- Delete local media artifacts under `MEDIA_ROOT` using path-safety checks.

Deletion should not retain a usable media asset record. A minimal deletion event may remain for diagnostics/audit, but it must not contain enough retained paths to serve or reconstruct the deleted media.

To avoid half-deleted states, use a two-phase pattern:

1. Transactionally mark the asset unavailable/deleting, cancel jobs, collect safe relative paths, and remove active bindings/references.
2. Delete local files after the asset is no longer servable/selectable.
3. Finalize by deleting dependent DB rows or leaving only a tombstone/error diagnostic if physical cleanup fails.

Existing archive endpoints may remain for legacy/audit maintenance, but the teacher video resource flow must call delete-plan/delete endpoints and use delete wording.

### 7. Make upload queue modal-independent

Upload queue ownership should move out of the modal component into an upload manager that remains mounted while the teacher app is active.

The modal becomes a view/controller:

- Closing the modal hides or minimizes the queue.
- Explicit cancel controls cancel current item or entire queue.
- The page/header can show an active upload indicator with resume/open controls.
- A route change inside the teacher SPA should not destroy active upload state if the provider remains mounted.

Browser limitation:

- Upload cannot continue after the browser tab/process closes.
- With tus fingerprints enabled, a later session can resume only when the file is available again to browser code.

### 8. Pipeline multi-file upload with bounded concurrency

The upload manager should process files through explicit stages:

```text
select files
  -> stage 0: validate extension and MAX_MEDIA_UPLOAD_MB for all files
  -> stage 1: checksum + exact duplicate precheck, limited concurrency
  -> stage 2: resumable upload, bounded concurrency
  -> stage 3: complete-upload/finalize per file
  -> backend queue: thumbnail/rendition then duplicate detection
```

Recommended defaults:

- Hash/precheck concurrency: 2.
- Upload concurrency: 1 by default for large local videos; configurable up to 2.
- Backend video transcode concurrency remains controlled by worker instances/GPU capacity.
- Duplicate detection runs lower priority than playback generation.

Each item should have independent status, progress, retry, and cancellation. Queue-level progress should not imply that backend processing is complete; it should distinguish uploaded/enqueued from playable/duplicate-checked.

## Risks / Trade-offs

- **Risk: Duration metadata can be wrong on damaged containers.** -> Use video stream duration first, fall back to format duration, and treat missing/untrusted duration as "skip visual duplicate detection" or "manual retry" rather than comparing against the whole library.
- **Risk: Strict duration gating may miss a true duplicate if a tool trims leading/trailing frames.** -> This is acceptable for this product boundary; such edits are no longer "true full-video duplicate" in the teacher resource workflow. The tolerance absorbs normal metadata drift but not meaningful edits.
- **Risk: 3s sampling can miss rare one-frame differences or very short videos.** -> The goal is duplicate warnings, not forensic proof. A minimum sample guard protects short videos.
- **Risk: Physical file deletion can fail after DB state changes.** -> Make the asset unavailable first, use path-safety checks, record cleanup diagnostics, and expose maintenance cleanup for failed deletions.
- **Risk: Upload manager state can be lost on full page reload/tab close.** -> Document the browser boundary and rely on tus resumability after the user returns with access to the same local file.
- **Risk: Upload concurrency can saturate disk/network and hurt UI responsiveness.** -> Keep conservative defaults and make concurrency bounded/configurable.

## Migration Plan

1. Add new delete-plan/delete API and frontend wiring while keeping existing archive endpoints untouched for compatibility.
2. Update teacher UI wording from archive/similarity to delete/duplicate detection.
3. Introduce duration-gated candidate lookup and duplicate-detection settings without deleting existing fingerprints.
4. Change worker duplicate detection to use the new candidate gate and sampling policy.
5. Split read-model/UI states so playback readiness is primary and duplicate detection is secondary.
6. Move upload queue state into a modal-independent upload manager and then enable bounded pipeline behavior.
7. Update documentation for duplicate-detection semantics, delete behavior, upload limitations, and worker settings.
8. Existing archived assets should remain hidden until a deliberate cleanup/delete maintenance action is run; do not silently delete prior archived media during deployment.

Rollback:

- If duplicate detection misbehaves, disable or skip the duplicate-detection command while preserving playback processing.
- If delete rollout finds cleanup issues, keep assets unavailable/tombstoned and disable the frontend delete button while maintenance cleanup is repaired.
- If upload manager issues occur, fall back to serial upload in the manager without returning queue ownership to modal teardown.

## Open Questions

- Should delete leave a minimal `media_asset_deleted` event row with title/file size/checksum for operator audit, or should it only emit application logs?
- Should upload concurrency default to exactly 1 for all files, or allow 2 when files are below a size threshold?
- Should existing archived assets get a one-time admin-only "delete archived media" cleanup command as part of this change or a follow-up?
