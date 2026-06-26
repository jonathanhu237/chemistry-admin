## MODIFIED Requirements

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

## REMOVED Requirements

### Requirement: Media asset archive has an impact plan
**Reason**: Teacher video resources now use destructive delete semantics rather than archive-retention semantics.
**Migration**: Replace archive impact planning with delete impact planning.

### Requirement: Media asset archive emits lifecycle events
**Reason**: The teacher workflow no longer archives media assets for retention.
**Migration**: Emit delete lifecycle events or diagnostics for destructive delete operations instead.

### Requirement: Archived media is unavailable to student playback
**Reason**: Deleted media, not archived media, is the teacher-facing lifecycle outcome for this resource flow.
**Migration**: Enforce unavailable behavior for deleting, deleted, tombstoned, or cleanup-failed media.

### Requirement: Physical file deletion follows archive policy
**Reason**: Physical file deletion is now part of teacher media deletion rather than a separate post-archive maintenance policy.
**Migration**: Delete source, playback, thumbnail, rendition, fingerprint, and duplicate-analysis artifacts during or immediately after destructive delete.

## ADDED Requirements

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
