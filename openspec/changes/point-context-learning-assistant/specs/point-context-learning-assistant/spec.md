## ADDED Requirements

### Requirement: Structured point context request
The learning assistant SHALL accept optional structured video-point context in addition to the student question.

#### Scenario: Prompt suggestion sends point context
- **WHEN** a student or admin selects a video-point prompt suggestion
- **THEN** the request SHALL include the selected `chapter_id`, `experiment_id`, and `point_key`
- **AND** the backend SHALL preserve the original student-facing question text.

#### Scenario: Free-form question without point context
- **WHEN** a student sends a free-form question from a chapter page without selecting a point
- **THEN** the request SHALL still include the selected `chapter_id`
- **AND** the assistant SHALL continue to answer using chapter context and optional RAG behavior.

### Requirement: Fixed point evidence package
The learning assistant SHALL assemble a fixed point evidence package whenever structured point context is provided.

#### Scenario: Point context has matching evidence
- **WHEN** a request includes an `experiment_id` and `point_key`
- **THEN** the backend SHALL resolve the experiment point metadata
- **AND** it SHALL collect relevant point evidence from question-bank metadata, including matching `primary_point_keys`, `source_audit.canonical_chunk_ids`, and `source_audit.supporting_theory_chunk_ids` when available.

#### Scenario: RAG is disabled for a point request
- **WHEN** a point-context request is submitted with RAG lookup disabled
- **THEN** the assistant SHALL still receive the fixed point evidence package
- **AND** it SHALL answer from point evidence and reliable chemistry knowledge without claiming supplemental RAG evidence was used.

#### Scenario: RAG is enabled for a point request
- **WHEN** a point-context request is submitted with RAG lookup enabled
- **THEN** the fixed point evidence package SHALL be available before supplemental retrieval
- **AND** hybrid RAG SHALL only add broader supporting evidence rather than replacing the fixed point context.

#### Scenario: Point evidence is incomplete
- **WHEN** the backend cannot find matching source-audit chunks for the selected point
- **THEN** the assistant SHALL keep the structured point metadata in context
- **AND** it SHALL avoid claiming a specific textbook source that was not found.

### Requirement: Point context diagnostics
The learning assistant response SHALL expose point-context diagnostics for admin inspection.

#### Scenario: Admin inspects point-context turn
- **WHEN** an admin selects a turn that included `point_key`
- **THEN** diagnostics SHALL show the resolved chapter, experiment, point key, point title when available, and point evidence count
- **AND** diagnostics SHALL distinguish fixed point evidence from supplemental RAG evidence.
