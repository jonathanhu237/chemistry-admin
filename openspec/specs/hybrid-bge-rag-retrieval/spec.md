# hybrid-bge-rag-retrieval Specification

## Purpose
TBD - created by archiving change upgrade-learning-assistant-debug-rag. Update Purpose after archive.
## Requirements
### Requirement: Legacy hybrid BGE retrieval remains retired
The system SHALL keep the legacy hybrid BGE retrieval path retired after local RAG sidecar removal.

#### Scenario: Legacy retrieval modules are inspected
- **WHEN** repository architecture validation searches runtime code
- **THEN** local BGE retrieval helpers, local BGE service clients, and sidecar-specific trace modes MUST be absent from production runtime paths
- **AND** no new caller MUST depend on `hybrid_bge_rerank`, `hybrid_bge_vector`, or local BGE service diagnostics.

#### Scenario: A developer needs RAG behavior
- **WHEN** a new feature needs evidence-backed retrieval
- **THEN** it MUST use the external textbook RAG runtime or another explicitly specified external provider boundary
- **AND** it MUST NOT revive the legacy local BGE sidecar.

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

