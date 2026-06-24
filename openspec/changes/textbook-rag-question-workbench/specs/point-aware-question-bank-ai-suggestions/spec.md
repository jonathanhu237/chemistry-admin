## MODIFIED Requirements

### Requirement: RAG-grounded AI suggestions
AI question-bank suggestions SHALL be generated only from usable textbook RAG-grounded evidence for the selected experiment and point context.

#### Scenario: AI creates questions from selected points
- **WHEN** a teacher requests AI question creation for one or more selected video points
- **THEN** the suggestion request SHALL include the formal experiment id, selected point keys, point titles, folder paths, and three-part point descriptions
- **AND** generated drafts SHALL include source audit metadata derived from the sectioned textbook evidence package used for that request.

#### Scenario: AI repairs a bound question
- **WHEN** a teacher requests AI repair for an existing question with bound point metadata
- **THEN** the suggestion request SHALL include the original question id, formal experiment id, bound point keys, original answer shape, source audit, option diagnostics, and sectioned textbook evidence
- **AND** generated repair drafts SHALL record lineage to the original question and evidence package.

#### Scenario: No usable evidence is available
- **WHEN** the selected experiment and point context cannot produce usable textbook evidence under the healthy configured RAG route
- **THEN** the system SHALL refuse AI suggestion generation
- **AND** it SHALL NOT create local-template candidates that appear publishable.

## ADDED Requirements

### Requirement: Section-aware candidate coverage
AI suggestions SHALL only cover point sections that have usable textbook evidence.

#### Scenario: Only principle evidence is usable
- **WHEN** principle evidence is usable and phenomenon or safety evidence is missing
- **THEN** generated candidates SHALL avoid unsupported phenomenon or safety claims
- **AND** candidate metadata SHALL record the missing sections.

#### Scenario: Multiple section evidence is usable
- **WHEN** principle, phenomenon, and safety evidence are all usable
- **THEN** generated candidates MAY cover any of those sections according to teacher-selected question type and prompt intent
- **AND** each candidate SHALL cite the supporting section evidence in source audit metadata.

### Requirement: Textbook-grounded LLM output contract
AI suggestions SHALL preserve the existing objective JSON output contract while adding textbook evidence context.

#### Scenario: LLM returns structured candidates
- **WHEN** the configured final LLM returns generated candidates
- **THEN** each candidate SHALL include question type, stem, machine-gradable answer, explanation, primary point keys, source audit, and option diagnostic links where applicable
- **AND** candidate validation SHALL run before publication is allowed.

#### Scenario: LLM output is malformed or unsupported
- **WHEN** the configured final LLM returns malformed JSON, unsupported question types, unsupported answer shape, or missing source audit
- **THEN** the system SHALL mark generation as failed or candidates as invalid
- **AND** it SHALL NOT publish or auto-repair any question.
