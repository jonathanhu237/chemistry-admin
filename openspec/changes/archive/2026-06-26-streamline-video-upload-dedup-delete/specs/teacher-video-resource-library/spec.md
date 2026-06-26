## REMOVED Requirements

### Requirement: Teacher can archive stored video resources
**Reason**: The teacher video resource library no longer treats this action as archive/retention. The expected product behavior is destructive deletion.
**Migration**: Replace teacher-facing archive actions with delete actions backed by delete-plan/delete APIs.

### Requirement: Archive confirmation explains binding impact
**Reason**: Confirmation remains required, but the operation is destructive delete rather than archive.
**Migration**: Use delete confirmation requirements that include binding impact, processing impact, and local artifact removal.

### Requirement: Video resource archive stays separate from upload
**Reason**: The separation remains important, but the stored-resource action is delete.
**Migration**: Keep pending upload queue removal separate from stored media delete APIs.

### Requirement: Archive result is auditable to teachers
**Reason**: The teacher workflow should not preserve deleted media as archived teacher-visible assets.
**Migration**: Show immediate delete results and affected binding counts; keep only minimal operator diagnostics outside normal teacher resource lists if needed.

## ADDED Requirements

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
