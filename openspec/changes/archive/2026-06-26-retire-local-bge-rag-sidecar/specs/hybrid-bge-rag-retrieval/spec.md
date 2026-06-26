## ADDED Requirements

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

## REMOVED Requirements

### Requirement: Hybrid retrieval preserves existing sources
**Reason**: The hybrid BGE path is no longer the supported RAG boundary.
**Migration**: Use `external-textbook-rag-runtime` for evidence-backed retrieval, or fixed reviewed evidence when dynamic RAG is not required.

### Requirement: AI-generated retrieval query
**Reason**: The old requirement binds generated queries to BGE/keyword recall.
**Migration**: Query generation, when retained, must feed the external textbook RAG runtime and must not imply local BGE recall.

### Requirement: BGE vector recall and reranking
**Reason**: BGE-M3 local vector recall and BGE reranker sidecar behavior is retired.
**Migration**: Use configured external embedding/rerank APIs and the textbook Elasticsearch index.

### Requirement: Optional CPU BGE service
**Reason**: The local CPU BGE Docker service is no longer a supported runtime.
**Migration**: Configure external embedding/rerank provider roles and do not start a local RAG profile.

### Requirement: Retrieval diagnostics
**Reason**: Diagnostics for BGE embedding, vector recall, sidecar rerank, and sidecar timings are obsolete.
**Migration**: Expose external textbook RAG diagnostics including ES index status, embedding API state, rerank API state, and evidence sufficiency.

### Requirement: Teacher workbench retrieval contract
**Reason**: The workbench now gates on external textbook RAG health rather than hybrid BGE health.
**Migration**: Use the modified `point-aware-ai-question-workbench` contract.

### Requirement: Catalog-node point evidence rebuild contract
**Reason**: The future GPU/BGE rerank job contract depends on a retired local model boundary.
**Migration**: Evidence generation must target catalog node identities through the external textbook RAG runtime.

### Requirement: Evidence-dependent AI generation fails closed during reset
**Reason**: The fail-closed behavior remains valid, but its BGE configuration scenario belongs to the external runtime contract.
**Migration**: Use the external textbook RAG unhealthy-state diagnostics and fail-closed workbench requirements.
