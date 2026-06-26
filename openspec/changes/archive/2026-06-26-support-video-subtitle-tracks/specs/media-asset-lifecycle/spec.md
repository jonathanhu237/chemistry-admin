## ADDED Requirements

### Requirement: Media assets can have external subtitle tracks
The system SHALL model external subtitle tracks as independent artifacts attached to media assets.

#### Scenario: Subtitle track is created
- **WHEN** an authorized teacher creates a subtitle track for an active media asset
- **THEN** the system MUST persist subtitle metadata including media asset id, language code, label, kind, source format, status, and default flag
- **AND** it MUST store subtitle artifacts under managed media storage rather than inside the generated video file.

#### Scenario: Subtitle track becomes ready
- **WHEN** a subtitle track has a valid WebVTT artifact
- **THEN** the track status MUST become ready
- **AND** it MUST be eligible for teacher preview and student playback read models.

#### Scenario: Default subtitle changes
- **WHEN** a subtitle track is set as default for a media asset
- **THEN** the system MUST ensure no other ready subtitle track for that same asset remains default
- **AND** it MUST not change default tracks on other media assets.

### Requirement: Subtitle uploads normalize to WebVTT
The system SHALL normalize supported subtitle inputs to WebVTT for browser playback.

#### Scenario: WebVTT file is uploaded
- **WHEN** a `.vtt` subtitle file is uploaded
- **THEN** the system MUST validate that it is usable as WebVTT
- **AND** it MUST serve the ready track as `text/vtt; charset=utf-8`.

#### Scenario: SRT file is uploaded
- **WHEN** a `.srt` subtitle file is uploaded
- **THEN** the system MUST convert it to WebVTT
- **AND** it SHOULD preserve the source subtitle artifact for diagnostics or future reconversion.

#### Scenario: Unsupported subtitle file is uploaded
- **WHEN** a subtitle file cannot be validated or normalized
- **THEN** the system MUST reject or fail the subtitle track with a machine-readable subtitle error
- **AND** it MUST NOT mark the parent video asset as failed solely because subtitle normalization failed.

### Requirement: Generated student playback video remains subtitle-free
The media processing pipeline SHALL keep generated student playback video free of burned-in or muxed subtitle streams by default.

#### Scenario: Learning rendition is generated
- **WHEN** the video worker creates or remuxes the student playback source
- **THEN** it MUST include only the selected video stream and optional selected audio stream
- **AND** it MUST exclude subtitle and attachment/data streams from the generated playback file.

#### Scenario: Source contains embedded subtitles
- **WHEN** a source video contains embedded subtitle streams
- **THEN** the system MUST NOT automatically burn those subtitles into the student playback video
- **AND** it MUST NOT rely on those embedded streams as the student subtitle delivery mechanism in this change.

### Requirement: Subtitle stream endpoints are directly loadable by browser track elements
The system SHALL serve ready subtitle tracks through authenticated URLs compatible with native browser `<track>` loading.

#### Scenario: Teacher preview requests subtitle stream
- **WHEN** an authorized teacher preview video element loads a subtitle track URL
- **THEN** the backend MUST return the WebVTT artifact with a browser-compatible content type
- **AND** authorization MUST work without requiring custom request headers from the `<track>` element.

#### Scenario: Student requests subtitle stream
- **WHEN** an authenticated student loads a subtitle track for a student-visible video asset
- **THEN** the backend MUST allow the stream only if the media asset is active, ready, and published/visible in that student's learning context
- **AND** it MUST reject subtitle streams for unavailable, deleted, or unbound assets.

#### Scenario: Preview token requests subtitle stream
- **WHEN** teacher student-preview mode loads a subtitle track URL
- **THEN** the preview token scope MUST be validated consistently with video and thumbnail preview streams
- **AND** the subtitle URL MUST not grant broader media access than the corresponding preview video URL.

### Requirement: Media lifecycle cleanup includes subtitle artifacts
The system SHALL include subtitle track records and files in media lifecycle planning and cleanup.

#### Scenario: Media asset delete plan is requested
- **WHEN** a delete impact plan is requested for a media asset with subtitle tracks
- **THEN** the response MUST include subtitle track counts and subtitle artifact paths in the file cleanup summary
- **AND** it MUST state that deleting the video resource removes its attached subtitle tracks.

#### Scenario: Media asset is deleted
- **WHEN** a media asset delete command is confirmed
- **THEN** the system MUST make attached subtitle tracks unavailable
- **AND** it MUST delete safe subtitle source and WebVTT artifacts under `MEDIA_ROOT`.

#### Scenario: Subtitle track alone is deleted
- **WHEN** a teacher deletes only a subtitle track
- **THEN** the system MUST remove or tombstone that subtitle track and its subtitle artifacts
- **AND** it MUST leave the parent media asset, playback rendition, thumbnail, duplicate fingerprints, and point bindings unchanged.

### Requirement: Duplicate detection ignores subtitle tracks
The system SHALL keep video duplicate detection independent from subtitle track content.

#### Scenario: Video exact duplicate precheck runs
- **WHEN** an uploaded video has linked subtitles in the teacher upload queue
- **THEN** exact duplicate precheck MUST still compare only the video file checksum and file size
- **AND** linked subtitle files MUST NOT change whether the video is considered an exact duplicate.

#### Scenario: Perceptual duplicate detection runs
- **WHEN** the worker generates or compares video duplicate signatures
- **THEN** it MUST use video content only
- **AND** subtitle track files MUST NOT affect perceptual duplicate scores or candidate selection.
