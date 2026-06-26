## MODIFIED Requirements

### Requirement: RAG-gated workbench access
The system SHALL require a healthy external textbook RAG runtime before a teacher can start or continue AI-assisted question creation or repair in the point-aware question workbench.

#### Scenario: Teacher opens AI creation when RAG is healthy
- **WHEN** a teacher selects an experiment or experiment point and external textbook RAG is enabled, Elasticsearch index metadata is valid, embedding configuration is ready, and rerank configuration is ready
- **THEN** the workbench SHALL allow the teacher to start an AI create session
- **AND** it SHALL show that generated candidates will use textbook evidence from the configured external RAG runtime.

#### Scenario: Teacher opens AI repair when RAG is unhealthy
- **WHEN** a teacher selects AI repair for an existing question while textbook RAG is disabled, Elasticsearch is unavailable, the textbook index is missing or stale, embedding is not configured, or rerank is not configured
- **THEN** the workbench SHALL prevent starting the AI repair session
- **AND** it SHALL show the missing RAG condition in teacher-readable language.

#### Scenario: Teacher sends a prompt after RAG becomes unhealthy
- **WHEN** a teacher has an open workbench session and sends a follow-up prompt after the external textbook RAG runtime is no longer healthy
- **THEN** the backend SHALL reject candidate generation
- **AND** the UI SHALL preserve prior turns and candidates while showing the gate failure.

#### Scenario: Legacy local RAG is unavailable
- **WHEN** external textbook RAG is unhealthy
- **THEN** the workbench MUST NOT suggest starting `bge-rag`, enabling hybrid BGE, or using local model files as remediation
- **AND** it MUST NOT fall back to local-template generation that creates publishable candidates.
