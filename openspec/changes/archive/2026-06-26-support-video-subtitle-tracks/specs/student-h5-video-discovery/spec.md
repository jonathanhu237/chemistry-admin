## ADDED Requirements

### Requirement: Student video discovery can carry subtitle metadata for full playback
Student video discovery surfaces SHALL make ready subtitle tracks available when a discovered video enters a full playback experience.

#### Scenario: Feed item opens full playback
- **WHEN** a student opens a video from home feed, video library, or catalog discovery into a full playback surface
- **THEN** the playback data MUST include ready subtitle track metadata and stream paths for the selected media asset
- **AND** the full player MUST render those tracks consistently with point video playback.

#### Scenario: Feed item is only a muted lightweight preview
- **WHEN** a feed card renders a muted autoplay preview or lightweight inline preview
- **THEN** it MAY omit loading subtitle track resources to preserve scroll and playback performance
- **AND** it MUST still provide subtitle tracks when the student opens a full playback surface.

#### Scenario: Discovery item has no ready subtitles
- **WHEN** a discovered video has no ready subtitle tracks
- **THEN** discovery and playback MUST continue without subtitle UI errors
- **AND** the absence of subtitles MUST NOT affect recommendation, search, or video availability.
