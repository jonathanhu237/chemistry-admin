# current-runtime-seed-boundary Specification

## Purpose
TBD - created by archiving change prune-seed-to-current-runtime-data. Update Purpose after archive.
## Requirements
### Requirement: Authoritative current seed whitelist
The repository SHALL treat `data/seed` as a strict whitelist of current runtime, import, rebuild, and validation data.

#### Scenario: Seed whitelist is validated
- **WHEN** production resource validation inspects `data/seed`
- **THEN** it MUST allow only current seed resources required to restore or validate the application baseline
- **AND** it MUST fail if unclassified historical reports, audit drafts, generated review artifacts, retired old point/evidence/question-bank artifacts, or local BGE embedding artifacts remain under `data/seed`.

#### Scenario: Current seed resources are listed
- **WHEN** the current seed manifest is generated or checked
- **THEN** it MUST include formal experiments, knowledge framework JSON, catalog tree seed, catalog point content seed, catalog point textbook evidence seed, the current catalog-node question-bank seed, canonical textbook chunks, search dictionaries, ES/IK analyzer assets, student learning profiles, and current manifests
- **AND** it MUST include `data/seed/search/chemistry_vocabulary.json` because runtime chemistry search reads it.

#### Scenario: Historical provenance is encountered
- **WHEN** files such as normalized three-element drafts, semantic mapping reports, chemistry review notes, import reports, validation reports, embedding QA reports, or old rebuilt-bank reports are encountered
- **THEN** validation MUST classify them as non-current seed
- **AND** cleanup MUST remove them rather than move them into operational docs.

### Requirement: Canonical corpus keeps chunks but not BGE embeddings
The current corpus seed SHALL preserve canonical textbook chunks while retiring local BGE embedding seed artifacts.

#### Scenario: Canonical chunks are validated
- **WHEN** production validation checks the canonical textbook corpus
- **THEN** it MUST validate the canonical chunk JSONL files and their expected chunk counts
- **AND** restore/import tooling MUST be able to recreate `source_documents` and `source_chunks` from those chunks.

#### Scenario: BGE embedding artifacts are encountered
- **WHEN** validation or cleanup encounters BGE dense vectors, sparse vector sidecars, row maps, embedding manifests, embedding reports, failed chunk reports, or input validation reports under seed paths
- **THEN** those files MUST NOT be protected as current seed
- **AND** they MUST be removed from current seed cleanup protection and production readiness requirements.

#### Scenario: Chunk embeddings table is checked
- **WHEN** production readiness validates the current baseline
- **THEN** it MUST NOT require `chunk_embeddings` to contain BGE vectors
- **AND** missing or empty `chunk_embeddings` MUST NOT fail current seed validation when canonical chunks and the external textbook RAG index path are valid.

### Requirement: Current catalog-node question bank seed
The current published question bank SHALL be exportable, importable, and validated as catalog-node seed data.

#### Scenario: Current question bank seed is exported
- **WHEN** the accepted current question-bank baseline is exported
- **THEN** the export MUST contain 54 published question banks and 1,965 published questions
- **AND** each question MUST preserve objective payload, experiment references, bank references, primary catalog point node ids, primary canonical point ids, source references, status, and generation/review lineage needed by teacher browsing and AI repair.

#### Scenario: Current question bank seed is imported
- **WHEN** a fresh database imports current seed resources
- **THEN** the import MUST recreate the current published catalog-node question-bank baseline
- **AND** it MUST reject seed rows that rely only on legacy `experiment_id + point_key` identity or the retired 2,310-question rebuilt-bank artifact.

#### Scenario: Current question bank seed is validated
- **WHEN** production readiness validates question-bank data
- **THEN** it MUST verify bank/question counts, valid experiment ids, valid bank ids, valid primary catalog node ids, valid canonical point ids, objective question payloads, and resolvable source references
- **AND** it MUST fail if the current question bank is silently treated as empty.

### Requirement: Safe seed import and reset defaults
Seed import tooling SHALL preserve current runtime data by default.

#### Scenario: Catalog seed import runs with defaults
- **WHEN** a maintainer runs the current catalog seed import command without a destructive flag
- **THEN** the command MUST validate and upsert current catalog seed rows
- **AND** it MUST NOT delete current experiment question banks, experiment questions, catalog-node evidence state, catalog-node evidence bindings, current catalog media bindings, users, roles, courses, source documents, source chunks, search dictionaries, or student learning seed data.

#### Scenario: Destructive legacy cleanup is requested
- **WHEN** a maintainer explicitly requests destructive cleanup of retired legacy seed data
- **THEN** the command MUST have a clearly named destructive option and validate protected current seed resources before deleting
- **AND** the delete scope MUST exclude current question-bank seed data, current catalog-node evidence seed data, current media bindings, canonical chunks, and runtime search dictionaries.

#### Scenario: Old reset targets are encountered
- **WHEN** reset or cleanup code still targets current runtime tables by default
- **THEN** architecture or production validation MUST fail
- **AND** the failure MUST identify the table or path that violates the current seed boundary.

### Requirement: Retired local and legacy seed chains are removed
Retired workflows that only support local BGE or legacy point identities SHALL NOT remain as supported repository paths.

#### Scenario: Legacy seed directories are encountered
- **WHEN** `data/seed/experiment_points`, `data/seed/point_evidence`, `data/seed/question_bank`, or equivalent retired seed directories exist after cleanup
- **THEN** production resource validation MUST fail
- **AND** cleanup MUST delete those directories once current protected resources validate.

#### Scenario: Legacy identity-only scripts are encountered
- **WHEN** scripts default to old point inventory, old manual point evidence, or old point-aware question-bank seed paths
- **THEN** those scripts MUST be deleted or removed from supported production workflows
- **AND** no default command MUST instruct maintainers to run them for current restore, validation, generation, or import.

#### Scenario: Operational docs are checked
- **WHEN** production or seed docs are validated
- **THEN** they MUST describe only the current seed whitelist, current restore/import order, current validation commands, and forbidden retired artifacts
- **AND** they MUST NOT preserve historical generation/audit details as current operational guidance.
