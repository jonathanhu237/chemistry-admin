## Context

The media worker currently processes a video as one serial success path: validate, probe, thumbnail, transcode a learning rendition, generate a vPDQ fingerprint from the original source, compare fingerprints, then finally mark the media asset ready. This makes a teacher wait for every post-processing step before the asset can be previewed, even when the thumbnail and student playback rendition already exist.

Recent local investigation showed that the RTX GPU and FFmpeg NVENC path can work in temporary containers after Docker/WSL refresh, but the production `video-worker` service is not configured to request GPU devices and the worker command always uses CPU `libx264`. Investigation also showed that vPDQ fingerprinting is currently run against the original 4K MKV source and can remain at the fixed `fingerprinting` phase for many minutes.

## Goals / Non-Goals

**Goals:**

- Make thumbnail plus learning rendition completion sufficient for teacher preview and student playback eligibility.
- Keep vPDQ fingerprinting and duplicate comparison as background analysis that can continue after playback is available.
- Add transcode acceleration policy with `auto`, `cpu`, and `nvenc` modes.
- In `auto`, probe NVENC at runtime and fall back to CPU `libx264` when unavailable or when an NVENC transcode attempt fails.
- Report meaningful transcode progress from FFmpeg rather than a fixed phase percentage.
- Prefer the learning rendition as the similarity fingerprint source once it exists.
- Surface background analysis state and failures in the teacher video resource library without blocking preview.

**Non-Goals:**

- Do not change video aspect ratio policy, player layout, thumbnail ratio, or student feed card ratio.
- Do not replace vPDQ with a different similarity algorithm.
- Do not require GPU for correctness; CPU processing remains the safe fallback.
- Do not implement parallel workers or distributed processing in this change.

## Decisions

### Decision 1: Playback readiness becomes independent of analysis completion

After thumbnail and learning rendition persistence, the worker marks the media asset `upload_status='ready'` while the current processing job may still have `status='processing'` and phase `fingerprinting` or `comparing`.

Rationale: the user-facing value of upload processing is a playable student source. Similarity analysis is useful, but it should not make an otherwise playable video appear stuck.

Alternative considered: keep `upload_status='processing'` until all analysis finishes but allow preview if `playback_relative_path` exists. Rejected because downstream selectors and mental models already treat `ready` as the playable state; the asset should say what it can do.

### Decision 2: Similarity analysis failures do not fail playback-ready assets

If fingerprint generation or comparison fails after playback is ready, the worker records the processing job as failed and leaves the media asset ready. The asset processing phase becomes an analysis failure state or retains enough job diagnostics for the teacher UI to show that duplicate analysis failed.

Rationale: a duplicate-detection failure should not make students lose access to an already generated playback source.

Alternative considered: mark all worker failures as media asset failures. Rejected because it conflates core playback failure with optional analysis failure.

### Decision 3: Runtime encoder selection uses a probe and per-job fallback

Worker settings expose `VIDEO_TRANSCODE_ACCELERATION=auto|cpu|nvenc`. `cpu` always uses `libx264`; `nvenc` requests `h264_nvenc`; `auto` first runs a small NVENC probe and chooses GPU only when the probe succeeds. If a GPU transcode fails in `auto`, the worker removes the partial output and retries once with CPU.

Rationale: Docker GPU availability can drift after driver, WSL, or Docker restarts. A probe prevents known-bad GPU paths from turning every video into a failed media asset.

Alternative considered: configure NVENC only in Compose and assume it works. Rejected because a missing NVIDIA runtime, missing `video` driver capability, or unsupported frame dimensions can break the encode path.

### Decision 4: FFmpeg progress updates are phase-relative

The worker invokes FFmpeg with `-progress pipe:1` for learning rendition generation and maps `out_time_ms` against probed duration into a bounded progress range inside the existing processing progress field. This keeps the existing API shape but makes the `transcoding` phase visibly advance.

Rationale: the frontend already polls media assets and reads `processing_progress`. Reusing that contract avoids introducing a streaming progress channel.

Alternative considered: stream progress over WebSockets or Server-Sent Events. Rejected for this change because the existing polling model is enough and less invasive.

### Decision 5: Fingerprinting prefers playback output

The worker passes the learning rendition path to the configured similarity command when a rendition exists. If no rendition is available, the original source remains the fallback.

Rationale: vPDQ is perceptual and does not need the original 4K mezzanine source for normal duplicate detection. Hashing the playback rendition reduces decode cost and aligns with the student-visible representation.

Alternative considered: raise `VIDEO_VPDQ_SECONDS_PER_HASH` only. Rejected as the sole fix because it reduces accuracy without addressing the expensive original-source decode.

## Risks / Trade-offs

- [Risk] Ready assets can still have a failed processing job for similarity analysis. -> Mitigation: frontend labels must distinguish playable readiness from analysis state.
- [Risk] `gpus: all` can prevent `video-worker` from starting on CPU-only Docker hosts. -> Mitigation: keep CPU fallback in code and document that CPU-only deployments should remove or override GPU device requests or set a CPU compose override.
- [Risk] NVENC output quality/size differs from CRF `libx264`. -> Mitigation: use conservative constant-quality settings and record encoder metadata on the rendition.
- [Risk] Progress based on duration can be imperfect for odd media timestamps. -> Mitigation: clamp progress to the configured phase range and still finish based on command success.
- [Risk] Fingerprinting the rendition can miss differences only present in the original source. -> Mitigation: preserve original-source fallback and record fingerprint source metadata.

## Migration Plan

1. Add worker settings and local compose GPU/runtime environment.
2. Update learning rendition generation to select encoder, parse FFmpeg progress, and persist encoder policy metadata.
3. Mark assets ready after learning rendition persistence and keep analysis as background job work.
4. Prefer rendition path for similarity fingerprinting and make analysis failures non-blocking for ready assets.
5. Update teacher UI to allow preview when playback exists and to show background analysis states.
6. Add focused backend and frontend tests, then rebuild/restart `backend`, `web-teacher`, and `video-worker`.

Rollback: set `VIDEO_TRANSCODE_ACCELERATION=cpu` to force old CPU encoding behavior. If background analysis readiness causes trouble, revert the worker playback-ready split and return to marking ready only at `finish_job`.

## Open Questions

- Should local CPU-only developers use a separate `docker-compose.cpu.yml` override, or should GPU exposure remain documented as an optional manual edit?
- Should similarity analysis retries get a dedicated admin action separate from "retry processing" for full playback processing?
