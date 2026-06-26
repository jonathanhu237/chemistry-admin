## MODIFIED Requirements

### Requirement: Turn-level diagnostics inspector
The system SHALL expose guardrail, classification, retrieval-decision, tool-call, external RAG, source, and raw response diagnostics for each assistant turn.

#### Scenario: Admin selects a completed turn
- **WHEN** the admin selects a completed assistant turn
- **THEN** the inspector SHALL show the answer status, classification, retrieval decision, guardrail decisions, tool calls, selected sources, and raw structured response for that turn.

#### Scenario: Retrieval decision diagnostics are available
- **WHEN** a completed turn includes a retrieval decision
- **THEN** the inspector SHALL show the retrieval mode, decision source, strict-evidence state, confidence when available, decision reason, override state when applicable, and whether dynamic RAG or platform resource lookup executed
- **AND** it SHALL distinguish skipped dynamic RAG from RAG disabled, no usable match, fixed evidence only, and strict evidence failure.

#### Scenario: Retrieval diagnostics are available
- **WHEN** a turn uses RAG
- **THEN** the inspector SHALL show generated retrieval queries, recall sources, external rerank scores when available, final evidence selected for the answer, and the external textbook RAG stage that produced the evidence.

#### Scenario: Retrieval is skipped by decision
- **WHEN** a turn skips dynamic RAG because the retrieval decision selected ordinary model-knowledge answering or fixed evidence only
- **THEN** the inspector SHALL show the retrieval decision empty state for RAG diagnostics
- **AND** it SHALL NOT show stale retrieval diagnostics from a previous turn.

#### Scenario: Runtime performance is available
- **WHEN** external textbook RAG diagnostics are available
- **THEN** the debug console SHALL show Elasticsearch index readiness, embedding provider configured state, rerank provider configured state, request latency, model metadata, and recent check time when available
- **AND** it SHALL NOT show local BGE service URL, local model path, warmup state, sidecar memory, or sidecar uptime.

#### Scenario: External RAG is unavailable
- **WHEN** external textbook RAG is disabled, misconfigured, stale, or unreachable
- **THEN** the debug console SHALL show the unavailable stage and teacher-readable remediation context
- **AND** it SHALL not imply that starting a local BGE sidecar can fix the runtime.

#### Scenario: Retrieval diagnostics are unavailable
- **WHEN** a turn does not use RAG or diagnostics are not returned
- **THEN** the inspector SHALL show an explicit empty state rather than stale diagnostics from a previous turn.
