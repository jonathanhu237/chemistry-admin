## MODIFIED Requirements

### Requirement: First-screen health overview
The teacher intelligent monitoring console SHALL render a first-screen overview that summarizes AI, external textbook RAG, ES, dictionary, outbox, and guardrail health before detailed diagnostics.

#### Scenario: Teacher opens intelligent monitoring
- **WHEN** an authenticated teacher-console user opens the intelligent monitoring route
- **THEN** the page SHALL show a compact health overview for OpenAI, external textbook RAG, Elasticsearch, dictionary assets, outbox/index sync, and student AI guardrails without requiring vertical scrolling on a normal desktop viewport
- **AND** each health item SHALL expose a status label, status tone, and the most important supporting value such as model, backend, mapping version, synced count, or recent error count.

#### Scenario: A subsystem has a warning or error
- **WHEN** any monitored subsystem reports warning, error, stale, failed, unavailable, missing, or degraded state
- **THEN** the overview SHALL surface the condition in an attention area
- **AND** the attention item SHALL identify the affected subsystem and provide a direct path to the corresponding detail module.

#### Scenario: All subsystems are healthy
- **WHEN** all monitored subsystems report healthy or acceptable local-development states
- **THEN** the overview SHALL communicate that no immediate action is required
- **AND** it SHALL still show last refresh time and manual refresh affordance.

### Requirement: RAG runtime monitoring module
The RAG module SHALL monitor external textbook RAG runtime health separately from OpenAI provider health.

#### Scenario: RAG module opens
- **WHEN** the teacher opens the `RAG` module
- **THEN** the module SHALL show student RAG enabled state, textbook RAG enabled state, Elasticsearch URL/index readiness, embedding provider configured state, rerank provider configured state, model metadata, request latency, and recent check time
- **AND** it SHALL distinguish disabled, not configured, index missing, index stale, external provider failure, and healthy states.

#### Scenario: External RAG provider is unavailable
- **WHEN** Elasticsearch, embedding API, or rerank API checks return an error
- **THEN** the RAG module SHALL show the error locally inside the RAG module
- **AND** the overview SHALL show only the summarized attention item with a path back to the RAG module.

#### Scenario: Local BGE sidecar fields are absent
- **WHEN** the RAG module renders after local sidecar retirement
- **THEN** it MUST NOT show BGE service URL, BGE warmup state, BGE model load state, sidecar memory, sidecar uptime, or local BGE model paths.
