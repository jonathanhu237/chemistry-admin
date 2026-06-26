## 1. Worker Configuration

- [x] 1.1 Add `VIDEO_TRANSCODE_ACCELERATION=auto|cpu|nvenc` to backend settings with a safe default.
- [x] 1.2 Add local compose GPU exposure and NVIDIA video driver capability for `video-worker`.
- [x] 1.3 Document CPU-only override and GPU runtime verification commands.

## 2. Worker Transcode Pipeline

- [x] 2.1 Add NVENC probe logic and encoder selection metadata.
- [x] 2.2 Update learning rendition command generation for CPU and NVENC encoder modes.
- [x] 2.3 Add per-job auto-mode fallback from failed NVENC transcode to CPU transcode.
- [x] 2.4 Parse FFmpeg progress output and update transcode progress during long jobs.
- [x] 2.5 Persist rendition metadata showing selected encoder, acceleration mode, fallback, and source dimensions.

## 3. Playback Readiness and Similarity Analysis

- [x] 3.1 Mark media assets playback-ready after thumbnail and learning rendition persistence.
- [x] 3.2 Preserve ready playback state while fingerprinting and comparing continue.
- [x] 3.3 Make fingerprinting and comparison failures non-blocking after playback readiness.
- [x] 3.4 Prefer the learning rendition path for vPDQ fingerprint input and record fingerprint source metadata.
- [x] 3.5 Ensure processing status APIs expose ready assets with active or failed background analysis jobs where needed.

## 4. Teacher Frontend

- [x] 4.1 Allow teacher preview when a video has a playback source even if background analysis is still running.
- [x] 4.2 Show playback-ready plus similarity-analysis-in-progress state distinctly on cards and tables.
- [x] 4.3 Show similarity-analysis failure without treating playback as failed.
- [x] 4.4 Keep transcode phase progress and labels visible during long worker processing.

## 5. Verification

- [x] 5.1 Add focused backend tests for encoder selection, progress parsing, playback readiness, and non-blocking analysis failure.
- [x] 5.2 Add focused teacher frontend contract tests for preview eligibility and background analysis labels.
- [x] 5.3 Run focused backend media/worker tests.
- [x] 5.4 Run focused teacher frontend tests and typecheck/build.
- [x] 5.5 Validate the OpenSpec change with `openspec validate --strict`.
- [x] 5.6 Rebuild/restart the relevant containers and verify GPU NVENC probe succeeds in a temporary container.
