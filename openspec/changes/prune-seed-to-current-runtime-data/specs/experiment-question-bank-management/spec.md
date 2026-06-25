## ADDED Requirements

### Requirement: Current catalog-node question bank seed baseline
The system SHALL treat the accepted published catalog-node question bank as current seed data.

#### Scenario: Current bank is exported as seed
- **WHEN** the default question-bank seed export runs
- **THEN** it MUST export 54 published generated banks and 1,965 published questions
- **AND** it MUST preserve current experiment references, current bank ids, primary catalog point node ids, primary canonical point ids, source references, objective payloads, publication status, and generation lineage.

#### Scenario: Current bank is restored
- **WHEN** a fresh environment imports current production seed data
- **THEN** it MUST restore the current catalog-node question-bank baseline
- **AND** teacher question-bank browsing MUST show the restored current questions rather than an empty bank.

#### Scenario: Retired bank artifact is encountered
- **WHEN** the retired `rebuilt_question_bank_merged_v1` bank or any seed row keyed only by old `experiment_id + point_key` identity is encountered
- **THEN** the system MUST reject it as current seed data
- **AND** it MUST NOT import it as published, draft, review, demo, or candidate question-bank content.

## MODIFIED Requirements

### Requirement: New question-bank generation depends on catalog-node evidence
The system SHALL require fresh catalog-node source evidence before creating or replacing catalog-node default question-bank content.

#### Scenario: Question generation is requested for the new catalog
- **WHEN** an administrator or teacher requests default question-bank generation for the new experiment catalog
- **THEN** the generation workflow MUST use catalog point node identities
- **AND** it MUST require fresh source evidence bound to those catalog point nodes.

#### Scenario: Evidence has not been regenerated
- **WHEN** a question-bank generation workflow has no fresh catalog-node evidence for the requested point scope
- **THEN** it MUST block or mark generation as unavailable
- **AND** it MUST NOT fall back to legacy point keys, legacy reviewed bank artifacts, old point evidence bindings, local BGE embeddings, or ungrounded generation.

#### Scenario: Current seed already exists
- **WHEN** the current catalog-node question-bank seed has been imported
- **THEN** new generation MUST be treated as an explicit replacement or additive workflow with validation
- **AND** it MUST NOT erase or supersede the current seed baseline merely because catalog seed import runs.

## REMOVED Requirements

### Requirement: Catalog reset leaves default experiment question bank empty
**Reason**: The current accepted baseline is no longer empty; the live system has 54 published generated banks and 1,965 published questions keyed by current catalog-node metadata.

**Migration**: Replace empty-bank reset behavior with the current catalog-node question-bank seed export/import/validation flow. Catalog seed import must preserve current question banks by default.
