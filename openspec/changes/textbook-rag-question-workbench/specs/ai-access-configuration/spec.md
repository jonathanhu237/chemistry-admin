## ADDED Requirements

### Requirement: Role-based AI provider configuration
The system SHALL configure final LLM generation separately from textbook RAG embedding and rerank providers.

#### Scenario: Admin configures final question generation
- **WHEN** an admin configures the question-generation LLM
- **THEN** the system SHALL store provider role, base URL, model name, and API key for the final chat-completion provider
- **AND** this configuration SHALL be usable for DeepSeek-compatible structured question generation.

#### Scenario: Admin configures textbook embedding
- **WHEN** an admin configures the textbook RAG embedding model
- **THEN** the system SHALL store provider role, base URL, model name, API key, and expected vector dimension for the embedding provider
- **AND** the textbook chunk index SHALL report unhealthy when the active index metadata does not match this configuration.

#### Scenario: Admin configures textbook rerank
- **WHEN** an admin configures the textbook RAG rerank model
- **THEN** the system SHALL store provider role, base URL, model name, API key, and rerank thresholds for the rerank provider
- **AND** workbench retrieval SHALL use this configuration before candidate generation is allowed.

### Requirement: AI secret handling and visibility
The system SHALL store AI provider secrets as backend configuration secrets and expose only masked status outside admin edit flows.

#### Scenario: Teacher views AI-backed workbench readiness
- **WHEN** a teacher views the question workbench RAG or LLM status
- **THEN** the UI SHALL show availability, provider role, model name, and masked key fingerprint when available
- **AND** it SHALL NOT expose full API keys.

#### Scenario: Admin updates a provider without replacing its key
- **WHEN** an admin saves AI provider settings with the API key omitted
- **THEN** the system SHALL retain the previously stored key
- **AND** it SHALL update only the submitted non-secret fields.

#### Scenario: Configuration is loaded from environment
- **WHEN** environment-backed AI settings are present
- **THEN** the runtime SHALL use them as defaults or overrides according to backend configuration rules
- **AND** code SHALL NOT contain hardcoded provider API keys.

### Requirement: Textbook RAG runtime status
The system SHALL expose a runtime status for the configured textbook RAG route.

#### Scenario: Textbook RAG is healthy
- **WHEN** Elasticsearch is reachable, the active index matches the configured embedding model, and embedding and rerank checks succeed
- **THEN** the runtime status SHALL be healthy
- **AND** teacher question generation MAY proceed.

#### Scenario: Textbook RAG is unhealthy
- **WHEN** Elasticsearch, index metadata, embedding, or rerank checks fail
- **THEN** the runtime status SHALL identify the failed stage
- **AND** teacher question generation SHALL be disabled with a readable reason.
