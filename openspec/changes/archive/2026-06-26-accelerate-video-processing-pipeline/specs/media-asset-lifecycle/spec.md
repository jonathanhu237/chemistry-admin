## ADDED Requirements

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
