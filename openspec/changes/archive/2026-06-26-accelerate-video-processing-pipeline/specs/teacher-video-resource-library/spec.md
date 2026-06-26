## ADDED Requirements

### Requirement: Teacher can preview playback-ready assets during background analysis
The teacher video resource library SHALL allow preview once a media asset has a usable playback source, even if similarity analysis is still running.

#### Scenario: Asset is playback-ready but analysis is running
- **WHEN** a media asset has `playback_relative_path` and its latest processing job is fingerprinting or comparing
- **THEN** the preview action MUST be enabled
- **AND** the asset card MUST indicate that similarity analysis is still in progress.

#### Scenario: Asset is ready and analysis failed
- **WHEN** a media asset has playback output but the latest similarity analysis job failed
- **THEN** the preview action MUST remain enabled
- **AND** the asset card MUST show analysis failure wording without labeling the video playback as failed.

### Requirement: Teacher sees meaningful processing progress
The teacher video resource library SHALL display processing progress in a way that reflects worker activity.

#### Scenario: Learning rendition is transcoding
- **WHEN** the worker reports transcode progress from FFmpeg
- **THEN** the teacher UI MUST show the current progress value
- **AND** it MUST keep the phase label visible so teachers can distinguish transcoding from fingerprinting.

#### Scenario: Similarity analysis is running
- **WHEN** playback output exists and the worker is fingerprinting or comparing
- **THEN** the teacher UI MUST show background analysis state separately from playback availability
- **AND** it MUST NOT imply that the video cannot be previewed solely because analysis is still running.
