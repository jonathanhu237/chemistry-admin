## MODIFIED Requirements

### Requirement: Dynamic RAG probe is supported
The workbench SHALL let teachers inspect dynamic external textbook RAG behavior for the selected point.

#### Scenario: Teacher runs RAG probe
- **WHEN** a teacher starts a dynamic RAG probe for a point
- **THEN** the backend MUST generate retrieval queries from the current catalog-node context
- **AND** the result MUST show generated queries, recall source, candidate count, final evidence, external rerank scores when available, and runtime health.

#### Scenario: RAG probe fails
- **WHEN** dynamic RAG cannot run because query generation, Elasticsearch recall, external embedding, external rerank, index metadata, or evidence sufficiency is unavailable
- **THEN** the workbench MUST show the failed stage and teacher-readable reason
- **AND** it MUST NOT present ungrounded model output as if evidence was found.

#### Scenario: Local BGE sidecar is absent
- **WHEN** a teacher inspects RAG probe diagnostics
- **THEN** the workbench MUST NOT show local BGE model paths, BGE warmup state, BGE service URL, or sidecar runtime metrics
- **AND** remediation MUST refer to external textbook RAG configuration and index readiness.
