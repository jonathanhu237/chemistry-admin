## MODIFIED Requirements

### Requirement: RAG evidence refresh is asynchronous
The system SHALL refresh catalog-node evidence bindings through asynchronous jobs rather than blocking teacher saves.

#### Scenario: Point context changes
- **WHEN** point title, catalog path, normalized equations, phenomenon explanation, safety note, video readiness, or related point context changes
- **THEN** the system MUST mark catalog-node evidence as stale or enqueue a refresh according to configured trigger policy
- **AND** teacher save/publish actions MUST not wait for external textbook retrieval, external rerank, or evidence refresh completion
- **AND** evidence refresh queries MUST NOT use teacher-only video resource titles, media file names, or media asset metadata as point semantics.

#### Scenario: Evidence refresh runs
- **WHEN** a RAG evidence refresh job runs
- **THEN** it MUST generate retrieval queries from catalog node context
- **AND** it MUST use the external textbook RAG runtime to select candidate source chunks
- **AND** output bindings MUST target catalog node id or stable catalog seed key, not legacy `(experiment_id, point_key)`.

#### Scenario: External textbook RAG is unavailable
- **WHEN** Elasticsearch, embedding API, rerank API, index metadata, or evidence sufficiency is unavailable during evidence refresh
- **THEN** the job MUST fail or defer with a diagnostic reason
- **AND** the point MUST remain editable and dynamically RAG-consumable when external textbook RAG later becomes healthy.

### Requirement: RAG evidence freshness remains separate from ES sync
Catalog point evidence refresh SHALL remain independently observable and configurable even when ES sync is delayed or coalesced.

#### Scenario: Point context changes through autosave
- **WHEN** autosaved content or context changes affect RAG evidence inputs
- **THEN** the backend MUST mark evidence stale or schedule refresh according to the configured trigger policy
- **AND** the teacher save response MUST not wait for external textbook retrieval, external reranking, or evidence refresh completion.

#### Scenario: ES sync succeeds while evidence is stale
- **WHEN** a point's ES state becomes synced but RAG evidence remains stale, pending, failed, disabled, or unavailable
- **THEN** diagnostics MUST show those states independently
- **AND** the system MUST NOT imply that ES success guarantees RAG evidence freshness.

### Requirement: RAG evidence jobs remain separate but co-monitored
RAG evidence refresh and ES indexing SHALL remain separate job concerns while the monitoring surface presents their status together.

#### Scenario: ES is synced but RAG evidence is stale
- **WHEN** ES index state is synced and RAG evidence state is stale, failed, or unavailable
- **THEN** monitoring MUST show the two states separately
- **AND** it MUST NOT imply that successful ES indexing guarantees RAG evidence freshness.

#### Scenario: RAG refresh succeeds but ES sync fails
- **WHEN** RAG evidence refresh succeeds and ES sync fails for the same point placement
- **THEN** monitoring MUST show the successful RAG state and failed ES state independently
- **AND** retry actions MUST target the correct job type.

#### Scenario: Local BGE sidecar is absent
- **WHEN** RAG evidence jobs are configured after local sidecar retirement
- **THEN** job execution MUST NOT require local BGE model files, local BGE service URLs, or local BGE warmup state
- **AND** diagnostics MUST point to external textbook RAG configuration when remediation is needed.
