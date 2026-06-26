# teacher-video-resource-library Specification

## Purpose
TBD - created by archiving change purify-video-resource-deletion-and-es-index. Update Purpose after archive.
## Requirements
### Requirement: Upload policy is visible before teacher upload
The teacher video resource library SHALL display the effective original-video upload size policy before teachers start a video upload.

#### Scenario: Teacher opens video resource page
- **WHEN** the teacher video resource library loads
- **THEN** the frontend MUST request the effective media upload policy from the backend
- **AND** the metrics area MUST include a card titled `原始视频大小限制`
- **AND** the card value MUST reflect the backend runtime `MAX_MEDIA_UPLOAD_MB` policy rather than a hard-coded frontend constant.

#### Scenario: Upload policy is still loading
- **WHEN** the upload policy has not been loaded or has failed to load
- **THEN** the upload flow MUST NOT start hashing, duplicate precheck, tus upload, fallback upload, or finalization
- **AND** the UI MUST show a clear loading or error state instead of assuming there is no size limit.

#### Scenario: Upload policy changes after deployment
- **WHEN** operators change the backend upload limit and restart the backend
- **THEN** the teacher frontend MUST display and enforce the new effective limit from the policy endpoint without requiring a code change.

### Requirement: Oversized videos are rejected before upload work
The teacher video resource library SHALL reject local video files that exceed the effective upload policy before adding them to upload work.

#### Scenario: Teacher selects an oversized video
- **WHEN** a selected video file size is greater than `max_media_upload_bytes`
- **THEN** the file MUST be rejected before it enters the upload queue
- **AND** the frontend MUST NOT compute SHA-256, call duplicate precheck, start tus upload, start fallback upload, or call complete-upload for that file
- **AND** the teacher MUST see a message that includes the file size and the configured original-video size limit.

#### Scenario: Teacher selects mixed valid and oversized videos
- **WHEN** a file selection contains both videos within policy and videos above policy
- **THEN** only the within-policy videos MUST be added to the upload queue
- **AND** the oversized videos MUST be listed or summarized as rejected
- **AND** the accepted videos MUST preserve the existing serial upload behavior.

#### Scenario: Teacher retries after rejection
- **WHEN** a teacher removes or replaces an oversized file with a within-policy file
- **THEN** the upload queue MUST allow the new file to proceed through the existing duplicate precheck, resumable upload, and backend processing handoff.

### Requirement: Storage metrics distinguish playback savings from upload limit
The teacher video resource library SHALL present storage savings and upload limit as separate concepts in the metrics strip.

#### Scenario: Student playback sources exist
- **WHEN** the resource library has original source bytes and student playback-source rendition bytes
- **THEN** the `学生播放源空间` metric MUST show total student playback-source size
- **AND** it MUST also show the saved percentage derived from original bytes and rendition bytes.

#### Scenario: No student playback sources exist yet
- **WHEN** no student playback-source rendition bytes are available
- **THEN** the `学生播放源空间` metric MUST show an empty or pending value without inventing a savings percentage
- **AND** the upload limit metric MUST remain visible.

#### Scenario: Metrics strip renders final operational card
- **WHEN** the metrics strip renders the final storage-related card
- **THEN** that card MUST represent `原始视频大小限制`
- **AND** it MUST NOT continue to present the old standalone `已节省空间` metric as the final card.

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

### Requirement: Teacher can delete stored video resources
The teacher video resource library SHALL provide an explicit delete action for stored media assets and SHALL NOT present that action as archive.

#### Scenario: Teacher sees resource actions
- **WHEN** a teacher views an uploaded media asset in the video resource library
- **THEN** the asset actions MUST include preview when playable, retry when processing or duplicate detection failed, and delete when allowed
- **AND** the delete action MUST be visually distinct from removing a file from the pending upload queue
- **AND** the action text MUST use delete wording rather than archive wording.

#### Scenario: Asset is still processing
- **WHEN** a teacher attempts to delete a processing asset
- **THEN** the UI MUST either block the action with a clear reason or require confirmation that queued/running processing output will be abandoned
- **AND** the backend MUST keep media processing state consistent after deletion.

#### Scenario: Asset is deleted or being deleted
- **WHEN** a teacher opens a deleted, tombstoned, or deleting asset through any maintenance path
- **THEN** the UI MUST show it as unavailable
- **AND** it MUST NOT show the normal delete action as if the asset were active.

### Requirement: Delete confirmation explains binding, processing, and file impact
The teacher video resource library SHALL require impact-aware confirmation before destructively deleting a stored media asset.

#### Scenario: Asset is bound to points
- **WHEN** the delete impact plan reports active catalog point video bindings
- **THEN** the confirmation UI MUST show the affected binding count and representative point titles or catalog paths
- **AND** it MUST say those point video bindings will be removed while point content, questions, and publication state remain.

#### Scenario: Asset affects published student content
- **WHEN** at least one affected point is currently student-visible
- **THEN** the confirmation UI MUST warn that students will no longer play this video from those points
- **AND** it MUST avoid saying that the experiment point itself will be deleted.

#### Scenario: Asset has generated artifacts
- **WHEN** the delete impact plan reports source, playback, thumbnail, rendition, fingerprint, or duplicate-candidate artifacts
- **THEN** the confirmation UI MUST state that local media artifacts for this resource will be removed
- **AND** it MUST NOT imply that the resource can be recovered from the teacher video library after deletion.

#### Scenario: Asset has active processing jobs
- **WHEN** the delete impact plan reports queued or running media processing jobs
- **THEN** the confirmation UI MUST warn that those jobs will be cancelled
- **AND** it MUST require explicit teacher confirmation before continuing.

### Requirement: Stored resource delete stays separate from upload queue removal
The teacher video resource library SHALL keep stored-resource deletion separate from upload selection, resumable upload, duplicate precheck, and pending upload queue controls.

#### Scenario: Teacher removes a pending upload item
- **WHEN** a teacher removes a file from the pending upload queue before it has been finalized as a media asset
- **THEN** the removal MUST affect only the pending upload queue
- **AND** it MUST NOT call stored media asset delete or archive endpoints.

#### Scenario: Teacher deletes a stored asset
- **WHEN** a teacher confirms delete for a stored media asset
- **THEN** the frontend MUST call the media asset delete API
- **AND** it MUST NOT call catalog point binding APIs directly.

#### Scenario: Delete succeeds
- **WHEN** the delete API returns success
- **THEN** the resource library MUST refresh asset lists, counts, duplicate hints, and processing states
- **AND** the deleted asset MUST disappear from normal teacher resource lists and selectors.

### Requirement: Duplicate detection UI uses duplicate-only semantics
The teacher video resource library SHALL present duplicate detection as an advisory full-video duplicate check and SHALL NOT present it as generic similarity or content relationship analysis.

#### Scenario: Duplicate detection is running
- **WHEN** a playable media asset is still running duplicate detection
- **THEN** the UI MUST keep preview/playback available
- **AND** it MUST show duplicate detection as a secondary state such as "重复检测中" rather than primary media processing.

#### Scenario: Suspected duplicate is found
- **WHEN** the backend reports a suspected full-video duplicate candidate
- **THEN** the UI MUST label it as "疑似重复"
- **AND** it MUST show enough candidate information for teacher review without automatically deleting, replacing, or skipping the uploaded asset.

#### Scenario: No full-video duplicate is found
- **WHEN** duplicate detection completes without a suspected full-video duplicate
- **THEN** the UI MUST avoid showing warnings for partial overlap, contained clips, shared intros/outros, or generic content similarity
- **AND** it MAY omit a success badge unless a detail view needs diagnostics.

#### Scenario: Duplicate detection fails
- **WHEN** duplicate detection fails after playback is ready
- **THEN** the UI MUST keep the asset previewable/playable
- **AND** it MUST offer retry as a duplicate-detection retry rather than implying the video itself cannot be played.

### Requirement: Upload queue survives modal close
The teacher video upload workflow SHALL keep active upload queue state outside the upload modal so closing the modal hides or minimizes the queue instead of cancelling it.

#### Scenario: Teacher closes upload modal during active upload
- **WHEN** a teacher closes the upload modal while checksum, resumable upload, or finalization is active
- **THEN** the upload manager MUST continue the active queue while the teacher app remains mounted
- **AND** the UI MUST provide a visible way to reopen or monitor the queue.

#### Scenario: Teacher explicitly cancels upload
- **WHEN** a teacher chooses an explicit cancel-current-file or cancel-queue action
- **THEN** the upload manager MUST abort the relevant browser upload work
- **AND** the queue item states MUST show cancellation distinctly from modal close.

#### Scenario: Browser tab is closed
- **WHEN** the teacher closes or reloads the browser tab during upload
- **THEN** the system MUST NOT claim upload will continue in the background
- **AND** the UI/documentation MUST rely on resumable upload behavior only after the teacher returns with access to the same local file.

### Requirement: Multi-file upload uses a bounded pipeline
The teacher video upload workflow SHALL process multiple selected files through bounded pipeline stages rather than one fully serial item loop.

#### Scenario: Files are selected
- **WHEN** a teacher selects one or more video files
- **THEN** the upload workflow MUST validate type and `MAX_MEDIA_UPLOAD_MB` policy for all files before hashing or upload starts
- **AND** oversized files MUST be rejected without entering active upload stages.

#### Scenario: Queue begins processing
- **WHEN** the teacher starts a multi-file queue
- **THEN** checksum and exact duplicate precheck MAY run with bounded concurrency
- **AND** resumable uploads MUST run with bounded concurrency appropriate for large local files.

#### Scenario: One item upload finalizes
- **WHEN** a queue item finishes upload and finalization
- **THEN** the backend processing job for that item MUST be enqueued without waiting for all other selected files to upload
- **AND** the next eligible pipeline work MUST continue according to concurrency limits.

#### Scenario: Queue progress is shown
- **WHEN** the teacher views the upload queue
- **THEN** each item MUST show its own state, progress, retry/cancel affordance, and backend handoff result
- **AND** queue-level progress MUST distinguish browser upload/finalization from later backend playback processing and duplicate detection.

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
