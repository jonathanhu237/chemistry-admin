# media-asset-lifecycle Specification

## Purpose
TBD - created by archiving change purify-video-resource-deletion-and-es-index. Update Purpose after archive.
## Requirements
### Requirement: Media assets have an explicit lifecycle
The system SHALL track media asset lifecycle separately from upload status, playback processing status, duplicate-detection status, and deletion cleanup.

#### Scenario: Existing media asset is read
- **WHEN** a media asset has no explicit lifecycle value after migration
- **THEN** the system MUST treat it as active
- **AND** its existing `upload_status` MUST continue to represent only upload or playback-processing state.

#### Scenario: Media asset is deleted
- **WHEN** an authorized teacher or operator deletes a media asset from the teacher video resource library
- **THEN** the system MUST make the asset unavailable to teacher preview, student playback, catalog selectors, duplicate candidate lists, and processing workers
- **AND** it MUST cancel queued or active processing jobs for the asset.

#### Scenario: Delete cleanup cannot fully complete
- **WHEN** destructive delete cannot remove every dependent row or local file artifact
- **THEN** the system MUST keep any remaining record unavailable to students and teachers
- **AND** it MUST expose diagnostics for maintenance cleanup without reactivating the media asset.

### Requirement: Destructive lifecycle rebuild is allowed
The system SHALL allow a controlled destructive database rebuild for media lifecycle structures when this change is applied.

#### Scenario: Fresh database is built
- **WHEN** migrations run on a fresh database
- **THEN** media asset lifecycle fields and lifecycle event storage MUST exist in the baseline schema
- **AND** existing upload, processing, rendition, fingerprint, and duplicate-candidate tables MUST remain consistent.

#### Scenario: Existing database is upgraded destructively
- **WHEN** operators choose the destructive rebuild path for this change
- **THEN** the migration or maintenance sequence MAY reset derived lifecycle/index state
- **AND** it MUST preserve or explicitly document the handling of `media_assets`, local media files, users, roles, and protected seed resources.

### Requirement: Media upload size policy is authoritative
The backend SHALL enforce the effective media upload size policy for every media upload path.

#### Scenario: Local deployment default is raised
- **WHEN** the local development or compose configuration is prepared for this change
- **THEN** the configured `MAX_MEDIA_UPLOAD_MB` default MUST be `8192`
- **AND** backend runtime policy responses MUST report that effective value unless operators override it.

#### Scenario: Direct upload exceeds media size policy
- **WHEN** a direct media upload request contains a file larger than `MAX_MEDIA_UPLOAD_MB`
- **THEN** the backend MUST reject the upload with a machine-readable `file_too_large` reason
- **AND** the response MUST include enough policy information for the client to explain the configured limit
- **AND** the backend MUST NOT enqueue a media processing job for that file.

#### Scenario: Resumable upload finalization exceeds media size policy
- **WHEN** a tus upload is finalized for a file larger than `MAX_MEDIA_UPLOAD_MB`
- **THEN** the backend MUST reject finalization with a machine-readable `file_too_large` reason
- **AND** the backend MUST NOT mark the media asset as pending, processing, ready, or reusable
- **AND** the backend MUST NOT enqueue a media processing job for that file.

#### Scenario: Client bypasses frontend precheck
- **WHEN** a client bypasses the teacher frontend and calls media upload APIs directly
- **THEN** the backend MUST apply the same effective size policy as the frontend policy endpoint
- **AND** it MUST reject oversized media consistently across direct upload and resumable upload finalization.

### Requirement: Oversized upload diagnostics are distinct from missing files
The media asset lifecycle SHALL distinguish size-policy failures from local media file availability failures.

#### Scenario: Oversized upload is rejected
- **WHEN** a media upload fails because the file exceeds `MAX_MEDIA_UPLOAD_MB`
- **THEN** teacher-facing diagnostics MUST describe the problem as an original video size-limit failure
- **AND** the system MUST NOT present the primary failure as `本地媒体文件缺失` or equivalent missing-file wording.

#### Scenario: Failed asset audit record is kept
- **WHEN** the system keeps an audit record for an oversized rejected upload
- **THEN** that record MUST preserve `error_reason=file_too_large`
- **AND** file-state summarization MUST prioritize the size-limit reason over placeholder path existence
- **AND** the record MUST NOT be actionable as a normal retry-processing item.

#### Scenario: Temporary resumable file remains after rejection
- **WHEN** an oversized tus upload has already reached temporary storage before backend finalization rejects it
- **THEN** the system MUST either remove the temporary file during rejection or expose enough maintenance diagnostics to identify it for cleanup
- **AND** the temporary file MUST NOT be treated as an active student playback source or processing input.

### Requirement: Playback readiness is independent from analysis completion
Media asset lifecycle SHALL distinguish playable media readiness from later background analysis completion.

#### Scenario: Playback output exists while analysis is running
- **WHEN** a media asset has an available playback rendition and thumbnail but its latest processing job is still fingerprinting or comparing
- **THEN** the media asset MUST remain eligible for playback and preview
- **AND** the analysis job state MUST remain visible through diagnostics.

#### Scenario: Analysis fails after playback output exists
- **WHEN** similarity fingerprinting or duplicate comparison fails after playback output exists
- **THEN** the media asset MUST remain playback-ready
- **AND** the failure MUST be recorded as analysis diagnostics rather than a missing local media file or playback failure.

#### Scenario: Core playback processing fails
- **WHEN** validation, probing, thumbnail generation, or learning rendition generation fails before playback output exists
- **THEN** the media asset MAY remain failed according to existing processing failure semantics
- **AND** the failure MUST remain actionable through retry processing.

### Requirement: Media asset delete has an impact plan
The system SHALL provide a delete impact plan before a teacher can destructively delete a media asset from the video resource library.

#### Scenario: Asset has catalog point bindings
- **WHEN** the delete plan is requested for an asset with active catalog point video bindings
- **THEN** the response MUST include affected binding count, placement node ids, canonical point ids, point titles, catalog paths, and publication/readiness state
- **AND** it MUST state that point content remains but video bindings will be removed.

#### Scenario: Asset has no active bindings
- **WHEN** the delete plan is requested for an asset with no active point video bindings
- **THEN** the response MUST say the asset can be deleted without changing point video bindings
- **AND** it MUST still report processing jobs, renditions, thumbnails, fingerprints, duplicate candidates, and file-state summary.

#### Scenario: Legacy generic media bindings exist
- **WHEN** the delete plan sees generic `media_bindings` rows for the asset
- **THEN** the response MUST report them separately from catalog point video bindings
- **AND** generic binding counts MUST NOT be used as the only source of catalog point impact.

#### Scenario: Active processing exists
- **WHEN** the delete plan sees queued or running media processing jobs for the asset
- **THEN** the response MUST include active job count and phase details
- **AND** it MUST state that confirming delete will cancel those jobs.

### Requirement: Media asset delete removes resource records and local artifacts
The system SHALL destructively remove teacher-deleted media resources and their local media artifacts while preserving point content.

#### Scenario: Delete command succeeds
- **WHEN** a teacher confirms media asset deletion
- **THEN** the system MUST remove or tombstone the media asset so it is not returned by normal media asset list APIs
- **AND** it MUST remove active point video bindings that reference the asset while leaving point content, questions, and publication state intact.

#### Scenario: Local artifacts are deleted
- **WHEN** delete cleanup runs for a media asset
- **THEN** the system MUST delete source files, playback files, thumbnails, renditions, duplicate fingerprints, and duplicate-analysis artifacts that belong to the asset under `MEDIA_ROOT`
- **AND** it MUST verify each path stays inside `MEDIA_ROOT` before deleting.

#### Scenario: Duplicate references exist
- **WHEN** the asset appears as either side of duplicate candidate records
- **THEN** the system MUST remove or invalidate those duplicate candidate records
- **AND** remaining active assets MUST NOT show stale duplicate hints pointing to the deleted asset.

#### Scenario: Delete event is recorded
- **WHEN** a destructive delete command is accepted
- **THEN** the system MAY record a minimal delete event or diagnostic summary for operators
- **AND** any retained diagnostic MUST NOT preserve a servable local media path or make the deleted media selectable.

### Requirement: Duplicate detection only considers true full-video duplicates
The system SHALL use duplicate detection only to find full-video duplicates and SHALL NOT search for contained clips, partial overlaps, shared intros/outros, or generic visual similarity.

#### Scenario: Exact duplicate precheck matches
- **WHEN** an uploaded file has the same SHA-256 checksum and file size as an active existing asset
- **THEN** the system MUST treat it as an exact duplicate
- **AND** it MUST avoid re-uploading or reprocessing the same byte-identical video unless the teacher explicitly chooses a replacement workflow.

#### Scenario: Visual duplicate candidates are selected
- **WHEN** the worker is ready to run perceptual duplicate comparison for a media asset
- **THEN** it MUST only compare against active ready assets whose stored source-video durations are within the configured near-equal duration tolerance
- **AND** it MUST NOT compare against the full library when reliable duration metadata exists.

#### Scenario: Duration tolerance is calculated
- **WHEN** the system calculates near-equal duration tolerance for duplicate candidate selection
- **THEN** the default tolerance MUST be equivalent to `clamp(duration_seconds * 0.001, 0.5, 2.0)` seconds
- **AND** the final duplicate decision MUST still require high-confidence visual matching after the duration gate.

#### Scenario: Durations are materially different
- **WHEN** two videos differ in duration beyond the near-equal duration tolerance
- **THEN** the system MUST NOT create a suspected duplicate candidate between them
- **AND** it MUST NOT surface them as contained, overlapping, or generally similar videos.

#### Scenario: Duration metadata is unavailable
- **WHEN** a media asset lacks reliable video duration metadata
- **THEN** the system MUST avoid broad all-library perceptual comparison
- **AND** it MUST either skip visual duplicate detection with diagnostics or require a retry after probe metadata is repaired.

### Requirement: Perceptual duplicate signatures use duplicate-focused sampling
The system SHALL generate perceptual duplicate signatures using a sampling policy tuned for full-video duplicate detection rather than clip search.

#### Scenario: Long video signature is generated
- **WHEN** a video is longer than the short-video minimum sample window
- **THEN** the default signature interval SHOULD be 3 seconds per hash or an equivalent configurable duplicate-detection interval
- **AND** it MUST be documented as duplicate detection, not generic similarity analysis.

#### Scenario: Short video signature is generated
- **WHEN** a video is too short to produce enough samples at the default interval
- **THEN** the system MUST reduce the effective interval down to a configured minimum interval to preserve a minimum sample count
- **AND** it MUST NOT use this short-video behavior to enable partial-overlap matching.

#### Scenario: Signature metadata is stored
- **WHEN** a perceptual duplicate signature is persisted
- **THEN** metadata MUST include the source kind, effective sample interval or equivalent sampling settings, algorithm label, and duration used for duplicate gating
- **AND** diagnostics MUST be sufficient to explain why candidates were or were not compared.

### Requirement: Duplicate detection is asynchronous and non-blocking
The system SHALL keep playback readiness independent from duplicate-detection completion.

#### Scenario: Playback output is ready
- **WHEN** thumbnail and student playback output have been generated successfully
- **THEN** the media asset MUST become previewable/playable even if duplicate detection is queued, running, skipped, or failed
- **AND** upload/playback status MUST NOT be downgraded solely because duplicate detection is incomplete.

#### Scenario: Duplicate detection fails after playback readiness
- **WHEN** duplicate detection fails after playback output exists
- **THEN** the system MUST preserve playback readiness
- **AND** it MUST store duplicate-detection failure diagnostics for retry or maintenance.

#### Scenario: Duplicate detection is retried
- **WHEN** a teacher or operator retries a ready asset whose duplicate detection failed
- **THEN** the retry MUST run only the duplicate-detection portion when playback artifacts already exist
- **AND** it MUST NOT regenerate thumbnail or student playback output unless those artifacts are missing or invalid.

### Requirement: Duplicate comparison scales by candidate filtering
The system SHALL bound duplicate comparison work by pre-filtering candidates before invoking expensive perceptual comparison.

#### Scenario: Candidate list is built
- **WHEN** a new media asset has a ready duplicate signature
- **THEN** the worker MUST build the comparison candidate list using lifecycle, readiness, algorithm compatibility, and near-equal duration constraints
- **AND** it MUST exclude deleted, deleting, archived, failed, and materially different-duration assets.

#### Scenario: Candidate list is empty
- **WHEN** no duration-compatible active ready candidates exist
- **THEN** duplicate detection MUST complete without running perceptual compare commands
- **AND** it MUST record that no eligible candidates were available.

#### Scenario: Library grows
- **WHEN** the media library contains many ready assets
- **THEN** duplicate-detection runtime for a new upload SHOULD scale with the number of duration-compatible candidates rather than total ready assets
- **AND** the data access path SHOULD support range or bucket filtering on duration.

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
