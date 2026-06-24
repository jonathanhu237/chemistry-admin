## MODIFIED Requirements

### Requirement: Teacher workbench retrieval contract
The system SHALL expose retrieval health and diagnostics for teacher-side question-bank AI workbench requests without treating legacy BGE as the only acceptable runtime once the configured Qwen/Elasticsearch textbook RAG route is available.

#### Scenario: Workbench checks RAG runtime
- **WHEN** the question-bank page renders AI workbench actions
- **THEN** it SHALL use the configured teacher question-workbench RAG runtime to decide whether RAG-backed AI actions are available
- **AND** it SHALL distinguish RAG disabled, Elasticsearch unavailable, active index stale, embedding unavailable, rerank unavailable, and healthy rerank states.

#### Scenario: Workbench builds an evidence package
- **WHEN** a teacher starts or continues an AI workbench session under a healthy configured teacher RAG runtime
- **THEN** the backend SHALL build an evidence package for the selected experiment, point context, original question when present, and teacher prompt
- **AND** the package SHALL include source references and retrieval diagnostics when available.

#### Scenario: Workbench records reranked evidence
- **WHEN** configured reranking succeeds for a workbench request
- **THEN** the evidence package SHALL preserve final evidence order, chunk identifiers, source metadata, and rerank score where available
- **AND** the workbench SHALL show that the candidate was grounded in reranked RAG chunks.

#### Scenario: Workbench RAG fails closed
- **WHEN** the configured teacher RAG runtime cannot provide healthy reranked evidence for a workbench request
- **THEN** the system SHALL block AI candidate generation rather than silently falling back to ungrounded local generation
- **AND** it SHALL return a diagnostic reason that the UI can display.

#### Scenario: Legacy BGE route remains available elsewhere
- **WHEN** another feature still uses the hybrid BGE retrieval route
- **THEN** the BGE route MAY continue to expose BGE health and diagnostics for that feature
- **AND** it SHALL NOT be required for teacher question-workbench generation when the Qwen/Elasticsearch textbook RAG route is selected.
