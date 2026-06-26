## ADDED Requirements

### Requirement: Teacher can manage external subtitle tracks for video resources
The teacher video resource library SHALL let teachers manage external subtitle tracks as media-asset attachments without modifying the generated student playback video.

#### Scenario: Teacher opens a playable video resource
- **WHEN** a teacher opens a stored video resource detail or preview
- **THEN** the UI MUST show a subtitle track section for that media asset
- **AND** it MUST allow ready tracks to be previewed with the video when track stream URLs are available.

#### Scenario: Teacher adds a subtitle after upload
- **WHEN** a teacher uploads a supported subtitle file for an existing media asset
- **THEN** the UI MUST collect or infer language code, label, and default-track choice
- **AND** the backend MUST create a subtitle track attached to that media asset rather than changing the video file.

#### Scenario: Subtitle processing fails
- **WHEN** a subtitle upload or normalization fails
- **THEN** the UI MUST show the subtitle track failure separately from the video playback status
- **AND** the video MUST remain previewable/playable if its playback output is ready.

#### Scenario: Teacher deletes a subtitle track
- **WHEN** a teacher deletes a subtitle track from a video resource
- **THEN** the UI MUST make clear that only that subtitle track is removed
- **AND** it MUST NOT call media asset delete APIs or remove the video from points.

### Requirement: Teacher can link a subtitle while selecting a video upload
The teacher video upload workflow SHALL support selecting an external subtitle file linked to a pending video queue item before the video asset exists.

#### Scenario: Teacher attaches subtitle to queued video
- **WHEN** a teacher selects a video file in the upload modal or queue
- **THEN** the teacher MAY attach one or more supported subtitle files to that specific video queue item
- **AND** the UI MUST show a link indicator that the subtitle will be bound to that video's resulting media asset.

#### Scenario: Queue item has no backend asset id yet
- **WHEN** the linked subtitle is selected before video finalization
- **THEN** the frontend MUST maintain the association using a stable local link identifier
- **AND** it MUST NOT require a persisted media asset id until the video upload finalizes.

#### Scenario: Video finalization succeeds
- **WHEN** the video queue item finalizes and returns a media asset id
- **THEN** the upload manager MUST create subtitle tracks for linked subtitle files on that media asset
- **AND** subtitle upload/normalization status MUST be shown independently for each linked subtitle.

#### Scenario: Exact duplicate video is reused
- **WHEN** duplicate precheck finds an existing exact video asset and the queue item has linked subtitles
- **THEN** the UI MUST require explicit teacher choice before adding those subtitle tracks to the existing asset
- **AND** it MUST offer a reuse-without-subtitle option that leaves the existing asset unchanged.

### Requirement: Teacher upload guidance explains subtitle policy
The teacher video resource library SHALL explain that generated student playback does not burn or carry embedded subtitles and that external subtitles are managed as separate tracks.

#### Scenario: Teacher selects a video with embedded subtitles
- **WHEN** the system can detect that the source video contains embedded subtitle streams
- **THEN** the UI SHOULD tell the teacher that embedded subtitles are not automatically included in the student playback source
- **AND** it SHOULD guide the teacher to upload an external subtitle track if subtitles are needed.

#### Scenario: Teacher sees upload guidance
- **WHEN** the upload modal or video detail displays supported media behavior
- **THEN** it MUST avoid implying that MKV/MP4 embedded subtitles will appear in student playback
- **AND** it MUST avoid offering burn-in as the default subtitle path.

### Requirement: Teacher preview renders ready subtitle tracks
The teacher video preview SHALL render ready external subtitle tracks using the same student playback contract.

#### Scenario: Ready default subtitle exists
- **WHEN** a video has a ready default subtitle track
- **THEN** teacher preview MUST include a native subtitle track for it
- **AND** the track label and language MUST match the subtitle metadata.

#### Scenario: Multiple ready tracks exist
- **WHEN** a video has multiple ready subtitle tracks
- **THEN** teacher preview MUST expose each ready track to the video element/player
- **AND** exactly one track SHOULD be marked default when the backend reports a default track.
