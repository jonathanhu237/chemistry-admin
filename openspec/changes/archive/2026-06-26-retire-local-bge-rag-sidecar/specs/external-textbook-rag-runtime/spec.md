## ADDED Requirements

### Requirement: External textbook RAG is the only supported RAG runtime
The system SHALL treat backend-orchestrated textbook retrieval through Elasticsearch and configured external embedding/rerank APIs as the only supported RAG runtime.

#### Scenario: Runtime boundary is inspected
- **WHEN** developers inspect supported RAG runtime configuration
- **THEN** the supported boundary MUST consist of backend retrieval orchestration, the textbook Elasticsearch index, external embedding API configuration, and external rerank API configuration
- **AND** it MUST NOT require a local model-serving container, local BGE model mount, or local BGE HTTP sidecar.

#### Scenario: Local BGE settings are present
- **WHEN** deprecated local BGE variables such as `RAG_HYBRID_BGE_ENABLED` or `RAG_BGE_SERVICE_URL` are present in a local environment
- **THEN** supported RAG code MUST NOT use them to select a runtime
- **AND** validation MUST either ignore them with an explicit retirement warning or fail with a clear unsupported-setting diagnostic.

### Requirement: External textbook RAG configuration is explicit and role-separated
The system SHALL configure textbook RAG through explicit Elasticsearch, embedding, and rerank provider roles.

#### Scenario: External RAG is enabled
- **WHEN** textbook RAG is enabled
- **THEN** runtime validation MUST require an Elasticsearch URL and index name
- **AND** it MUST require embedding API base URL, API key, model, and expected dimension
- **AND** it MUST require rerank API base URL, API key, and model.

#### Scenario: Provider roles are displayed
- **WHEN** admin or teacher diagnostics show RAG runtime configuration
- **THEN** they MUST distinguish chat LLM, embedding provider, rerank provider, and Elasticsearch index configuration
- **AND** they MUST mask secrets while showing configured/missing state and model identifiers.

### Requirement: External textbook RAG health is stage-specific
The system SHALL report external textbook RAG health with stage-specific status instead of local sidecar status.

#### Scenario: Runtime health is checked
- **WHEN** a monitoring or gate endpoint checks textbook RAG
- **THEN** the response MUST distinguish disabled, Elasticsearch not configured, Elasticsearch unreachable, index missing, index stale, embedding not configured, rerank not configured, and healthy states
- **AND** the response MUST include teacher/operator-readable diagnostics for the failed stage.

#### Scenario: Index metadata mismatches provider configuration
- **WHEN** the textbook Elasticsearch index metadata does not match the configured embedding model or dimension
- **THEN** runtime status MUST be stale or unavailable for evidence-backed generation
- **AND** the diagnostic MUST identify the indexed model/dimension and configured model/dimension.

### Requirement: RAG consumers fail closed when external textbook RAG is unhealthy
The system SHALL prevent evidence-backed generation and evidence refresh from silently using obsolete local RAG behavior when external textbook RAG is unhealthy.

#### Scenario: Evidence-backed generation is requested while RAG is unhealthy
- **WHEN** a teacher or backend job requests evidence-backed generation and textbook RAG status is not healthy
- **THEN** the request MUST fail or defer with a diagnostic reason
- **AND** it MUST NOT invoke local BGE, local template generation, retired pgvector recall, or ungrounded fallback as if evidence was available.

#### Scenario: External API call fails
- **WHEN** the configured embedding or rerank API times out, returns invalid JSON, returns an invalid response shape, or rejects credentials
- **THEN** the runtime MUST report the failing provider role
- **AND** session state, previous candidates, and point content saves MUST remain preserved.

### Requirement: Local RAG sidecar artifacts are unsupported
The repository SHALL not include supported runtime artifacts for a local RAG sidecar.

#### Scenario: Docker Compose is inspected
- **WHEN** `docker-compose.yml` or Compose validation output is inspected
- **THEN** no `bge-rag` service, `rag` profile, local BGE image, local BGE model volume, or BGE health check MUST be part of the supported stack.

#### Scenario: Runtime code is inspected
- **WHEN** backend runtime code is searched for local BGE service entrypoints
- **THEN** modules dedicated to serving local embedding/rerank endpoints MUST be absent
- **AND** runtime code MUST not import a retired hybrid BGE retrieval helper.
