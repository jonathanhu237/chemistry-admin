## MODIFIED Requirements

### Requirement: Protected Core Resource Manifest

The platform SHALL define a versioned manifest for every current core resource required to rebuild or validate the production baseline.

#### Scenario: Current resources are registered
- **GIVEN** the production-readiness manifest is generated or checked
- **WHEN** it lists protected core resources after the current seed boundary cleanup
- **THEN** it MUST include the structured experiment catalog seed, the 76-record point-content seed, the catalog point textbook evidence seed, the current catalog-node question-bank seed, the knowledge framework, canonical textbook chunk JSONL files, chemistry search dictionaries including `chemistry_vocabulary.json`, ES analyzer dictionaries, student learning profiles, and current manifests
- **AND** each entry MUST record semantic role, path or source location, required status, item count where applicable, byte size, and SHA256 where applicable.

#### Scenario: Retired resources are encountered
- **GIVEN** old point inventory files, old point-aware question-bank seed files, old manually reviewed point evidence files, old video-point evidence artifacts, local BGE embedding artifacts, generated import reports, generated validation reports, or audit drafts remain under historical paths
- **WHEN** cleanup classification or production validation runs
- **THEN** those retired resources MUST NOT be classified as protected current core data
- **AND** they MUST be removed from the current seed tree after the new protected resources validate.

#### Scenario: Canonical retrieval corpus is encountered
- **GIVEN** canonical textbook chunks remain under current production resource paths
- **WHEN** cleanup classification or production validation runs
- **THEN** those chunk resources MUST remain classified as protected current core data
- **AND** local BGE dense embeddings, sparse embeddings, embedding row maps, embedding manifests, and `chunk_embeddings` row counts MUST NOT be required as protected current core data.

### Requirement: Production Validation Chain

The repository SHALL provide a documented validation chain that proves the production baseline can be built, tested, and data-validated.

#### Scenario: Maintainer validates the baseline
- **GIVEN** a maintainer runs the production-readiness validation command or documented command set
- **WHEN** validation completes after the current seed boundary cleanup
- **THEN** it MUST check OpenSpec strict validation, protected current resource manifests, catalog seed counts, 76-record point-content seed mapping, current catalog-node question-bank seed counts and references, canonical chunk counts, runtime search dictionaries, backend tests, frontend typecheck, frontend tests, frontend build, and core data counts
- **AND** it MUST report failures with enough detail to identify the broken stage.

#### Scenario: Fresh rebuild is verified
- **GIVEN** an empty database and the declared current production resources are available
- **WHEN** the documented restore/import path is executed
- **THEN** the platform MUST recreate the current chapter-scoped experiment catalog tree from the structured seed
- **AND** it MUST recreate the 76 reviewed point-content seed records
- **AND** it MUST recreate canonical `source_documents` and `source_chunks` from canonical chunk JSONL files
- **AND** it MUST recreate the current 54-bank / 1,965-question catalog-node question-bank baseline
- **AND** it MUST leave retired old point inventory, old manual point evidence bindings, old rebuilt question-bank seed data, and local BGE embedding seed artifacts absent.

#### Scenario: Legacy protected counts are checked
- **GIVEN** validation code still contains old expected counts for 300 video points, 30 point-content examples, 77 old question banks, 2,310 old questions, 300 old point evidence bindings, 3,637 BGE `chunk_embeddings`, or BGE dense/sparse files
- **WHEN** the production-readiness validation command runs
- **THEN** validation MUST fail until those old protected counts are removed or replaced by current seed expectations
- **AND** the failure MUST identify the outdated baseline expectation.

### Requirement: Retired seed documentation
Production operations documentation SHALL explain the intentional retirement of legacy experiment seed resources without preserving historical generation artifacts as operational guidance.

#### Scenario: Maintainer reads production seed documentation
- **WHEN** a maintainer reads the seed or production operations documentation after this change
- **THEN** the documentation MUST state that old question-bank seeds, old video point inventory, old video references, old point evidence bindings, BGE embedding seed artifacts, and generated audit/report files are invalid for the current seed baseline
- **AND** it MUST state that canonical textbook chunks remain valid current corpus resources while local BGE embeddings and `chunk_embeddings` counts are not current restore requirements.

#### Scenario: Maintainer looks for question-bank regeneration instructions
- **WHEN** a maintainer searches the documentation for the current question-bank baseline
- **THEN** the documentation MUST state that the current baseline is the catalog-node question-bank seed exported from 54 published banks and 1,965 published questions
- **AND** it MUST NOT instruct maintainers to import the retired 2,310-question bank or treat the current bank as empty.
