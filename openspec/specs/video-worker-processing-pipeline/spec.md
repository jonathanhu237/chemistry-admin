# video-worker-processing-pipeline Specification

## Purpose
TBD - created by archiving change accelerate-video-processing-pipeline. Update Purpose after archive.
## Requirements
### Requirement: Worker selects a safe transcode encoder
The video worker SHALL select the learning-rendition encoder from runtime policy while preserving CPU fallback correctness.

#### Scenario: Auto mode uses a successful NVENC probe
- **WHEN** `VIDEO_TRANSCODE_ACCELERATION` is `auto` and the worker can successfully encode a small probe with `h264_nvenc`
- **THEN** learning rendition transcodes MUST use the NVENC encoder
- **AND** the persisted rendition metadata MUST identify the selected encoder.

#### Scenario: Auto mode falls back when NVENC is unavailable
- **WHEN** `VIDEO_TRANSCODE_ACCELERATION` is `auto` and the NVENC probe fails
- **THEN** learning rendition transcodes MUST use CPU `libx264`
- **AND** the worker MUST keep enough diagnostic metadata to explain the fallback reason.

#### Scenario: GPU transcode fails during auto mode
- **WHEN** an auto-selected NVENC transcode fails during a media job
- **THEN** the worker MUST remove any partial learning rendition output
- **AND** it MUST retry the learning rendition once with CPU `libx264` before failing the job.

### Requirement: Worker reports learning-rendition progress
The video worker SHALL update media processing progress during long FFmpeg learning-rendition generation.

#### Scenario: FFmpeg emits progress
- **WHEN** FFmpeg emits `out_time_ms` or equivalent progress while generating a learning rendition
- **THEN** the worker MUST map that progress into the transcode phase progress range
- **AND** teacher-visible processing progress MUST advance before the command finishes.

#### Scenario: FFmpeg progress is unavailable
- **WHEN** FFmpeg does not emit usable progress for a media source
- **THEN** the worker MUST retain the existing phase progress behavior
- **AND** it MUST still complete or fail the job based on command success.

### Requirement: Playback readiness precedes similarity analysis
The video worker SHALL make media playback available after thumbnail and learning rendition outputs are persisted, before similarity analysis has to finish.

#### Scenario: Rendition persistence succeeds
- **WHEN** the worker has persisted a thumbnail and learning rendition for an active media asset
- **THEN** the media asset MUST become ready for playback and preview
- **AND** the current processing job MAY continue with fingerprinting and duplicate comparison.

#### Scenario: Similarity analysis continues after playback readiness
- **WHEN** a media asset is playback-ready and the worker enters fingerprinting or comparing
- **THEN** the media asset MUST remain playback-ready
- **AND** the job phase MUST continue to expose background analysis progress.

### Requirement: Similarity analysis is non-blocking after playback readiness
The video worker SHALL treat fingerprinting and duplicate comparison as non-blocking analysis once playback output exists.

#### Scenario: Fingerprint generation fails after playback readiness
- **WHEN** fingerprint generation fails after a learning rendition has been persisted
- **THEN** the media asset MUST remain ready and previewable
- **AND** the processing job MUST retain failure diagnostics for the analysis failure.

#### Scenario: Duplicate comparison fails after playback readiness
- **WHEN** duplicate comparison fails after a learning rendition has been persisted
- **THEN** the media asset MUST remain ready and previewable
- **AND** the processing job MUST retain failure diagnostics for the analysis failure.

### Requirement: Similarity fingerprinting uses the playback source when available
The video worker SHALL prefer the generated learning rendition as the vPDQ fingerprint input when playback output exists.

#### Scenario: Learning rendition exists
- **WHEN** the worker starts similarity fingerprinting after generating a learning rendition
- **THEN** the fingerprint command MUST receive the learning rendition path as input
- **AND** fingerprint metadata MUST record that the playback source was used.

#### Scenario: Learning rendition does not exist
- **WHEN** a worker job needs fingerprinting and no learning rendition is available
- **THEN** the worker MUST fall back to the original source path
- **AND** fingerprint metadata MUST record that the original source was used.
