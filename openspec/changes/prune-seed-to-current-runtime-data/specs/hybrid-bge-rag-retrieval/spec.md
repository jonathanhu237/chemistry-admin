## MODIFIED Requirements

### Requirement: Catalog-node point evidence rebuild contract
The system SHALL treat old experiment video point evidence bindings as invalid after the catalog outline seed replacement and SHALL require catalog point evidence generation to target catalog point node identities through the supported external textbook RAG boundary.

#### Scenario: Catalog seed replacement retires evidence bindings
- **WHEN** current seed cleanup handles old experiment point data
- **THEN** it MUST remove or leave absent legacy point-to-chunk evidence bindings derived from old formal experiment and video point identities
- **AND** it MUST preserve canonical textbook chunks as reusable corpus data without requiring local BGE embeddings or populated `chunk_embeddings`.

#### Scenario: Future evidence generation selects points
- **WHEN** a future evidence generation job runs for the current catalog
- **THEN** it MUST load target points from leaf catalog nodes
- **AND** it MUST identify each target by catalog node id or deterministic catalog seed key rather than `experiment_id` and `point_key`.

#### Scenario: Future evidence generation builds queries
- **WHEN** a future evidence generation job prepares retrieval queries for a catalog point
- **THEN** it MUST include the point title and full catalog path context
- **AND** it MUST use the supported external textbook RAG retrieval boundary rather than retired local BGE vector recall or local BGE rerank.

#### Scenario: Future evidence output is imported
- **WHEN** freshly generated evidence is imported for catalog points
- **THEN** each evidence record MUST bind to a catalog point node identity
- **AND** validation MUST reject rows that only reference legacy experiment ids, old point keys, local BGE row ids, or retired embedding artifacts.

### Requirement: Evidence-dependent AI generation fails closed during reset
The system SHALL not generate new point-aware question-bank content from ungrounded, legacy, or retired local BGE evidence during the reset window.

#### Scenario: Teacher workbench requests evidence-backed generation
- **WHEN** a teacher or administrator starts evidence-backed question generation for a catalog point before fresh evidence exists
- **THEN** the backend MUST report insufficient catalog-node evidence
- **AND** it MUST NOT silently use old evidence bindings, local BGE embeddings, old rebuilt-bank artifacts, or ungrounded generation.

#### Scenario: External textbook RAG configuration is validated
- **WHEN** catalog-node evidence generation tooling is implemented or reused
- **THEN** it MUST validate the configured external textbook RAG runtime, including Elasticsearch/index readiness and external embedding/rerank provider configuration
- **AND** it MUST fail with a diagnostic if the supported external runtime is unavailable.

## REMOVED Requirements

### Requirement: BGE vector recall and reranking
**Reason**: Local BGE vector recall/rerank is retired and must not remain a current retrieval or seed requirement.

**Migration**: Use the supported external textbook RAG runtime and canonical chunk corpus. Remove `chunk_embeddings` vector recall, BGE dense/sparse seed artifacts, and local BGE rerank requirements from current validation.

### Requirement: Optional CPU BGE service
**Reason**: The product boundary no longer includes a local BGE Docker service, profile, model mount, service URL, or local CPU rerank runtime.

**Migration**: Remove local BGE Compose/profile/runtime/docs and validate external textbook RAG health instead.
