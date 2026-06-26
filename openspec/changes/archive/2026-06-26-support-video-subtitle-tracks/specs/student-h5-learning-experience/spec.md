## ADDED Requirements

### Requirement: Student point video playback supports external subtitle tracks
Student full video playback SHALL render ready external subtitle tracks associated with the active media asset.

#### Scenario: Point video has ready subtitle tracks
- **WHEN** a student opens a point video whose media asset has ready subtitle tracks
- **THEN** the student video read model MUST include subtitle track metadata and stream paths
- **AND** the player MUST attach the ready tracks to the video playback element.

#### Scenario: Default subtitle exists
- **WHEN** the backend marks one ready subtitle track as default
- **THEN** the student player MUST mark that track as default for browser playback
- **AND** the track label and language MUST match the backend metadata.

#### Scenario: No subtitle tracks exist
- **WHEN** a point video has no ready subtitle tracks
- **THEN** the student player MUST behave like the current video player
- **AND** it MUST NOT show an error or empty subtitle control solely because no tracks exist.

#### Scenario: Subtitle stream fails
- **WHEN** a ready subtitle track stream fails to load in the browser
- **THEN** the video MUST continue playing if the video stream is available
- **AND** the UI MAY show a non-blocking subtitle warning rather than failing the whole video.

### Requirement: Student subtitle URLs respect media visibility
Student subtitle playback SHALL obey the same media visibility boundaries as student video playback.

#### Scenario: Student lacks access to media asset
- **WHEN** a student requests a subtitle stream for a media asset not visible in their learning context
- **THEN** the backend MUST reject the request
- **AND** the student frontend MUST not expose stale subtitle URLs for that media asset.

#### Scenario: Media asset is deleted or unavailable
- **WHEN** a media asset is deleted, tombstoned, archived, or not playback-ready
- **THEN** its subtitle tracks MUST NOT be returned as playable student tracks
- **AND** direct subtitle stream requests MUST be rejected.
