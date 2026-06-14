## ADDED Requirements

### Requirement: Enhanced diagnostic bank candidate import
The system SHALL treat a validated diagnostic enhanced bank as a candidate default-bank seed source that is separate from the reviewed old-bank artifact.

#### Scenario: Enhanced bank artifact is available
- **WHEN** a diagnostic enhanced bank artifact passes validation
- **THEN** it SHALL remain a candidate import source until an explicit promotion or import operation is requested
- **AND** it SHALL NOT automatically replace the current reviewed old-bank candidate or any published student-facing bank.

#### Scenario: Enhanced bank is imported later
- **WHEN** an administrator or deployment process imports a promoted enhanced bank in a later change
- **THEN** the import SHALL preserve experiment ids, primary point keys, secondary point keys, source audit metadata, option-level diagnostic links, and generation lineage.
