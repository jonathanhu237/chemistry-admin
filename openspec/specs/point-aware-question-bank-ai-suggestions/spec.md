# point-aware-question-bank-ai-suggestions Specification

## Purpose
TBD - created by archiving change add-point-aware-question-bank-ai-suggestions. Update Purpose after archive.
## Requirements
### Requirement: Point-aware suggestion context
The system SHALL build AI question-bank suggestions from the current formal experiment and point-aware question metadata.

#### Scenario: Teacher requests new questions for an experiment
- **WHEN** a teacher requests AI suggestions from the selected experiment question-bank page
- **THEN** the request SHALL include the formal experiment id
- **AND** it MAY include one selected experiment video point key
- **AND** generated suggestions SHALL preserve primary point keys, source audit metadata, option diagnostic links where applicable, and generation lineage.

#### Scenario: Teacher requests a repair for an existing question
- **WHEN** a teacher requests an AI repair suggestion from a question detail view
- **THEN** the request SHALL include the original question id
- **AND** the suggestion context SHALL include the original stem, answer, explanation, primary point keys, source audit, and option diagnostic links
- **AND** the returned draft SHALL record lineage back to the original question id.

### Requirement: Non-mutating suggestion drafts
AI suggestions SHALL be stored as teacher-reviewable drafts and SHALL NOT directly mutate the published default bank.

#### Scenario: Suggestion generation succeeds
- **WHEN** AI add or repair suggestions are generated
- **THEN** each suggestion SHALL be stored as an experiment question draft
- **AND** the published question bank SHALL remain unchanged until a teacher explicitly publishes a draft.

#### Scenario: Teacher rejects a suggestion
- **WHEN** a teacher rejects a generated suggestion draft
- **THEN** the draft SHALL be marked rejected
- **AND** no published question SHALL be changed.

### Requirement: Metadata-preserving publication
Publishing a generated suggestion SHALL preserve point-aware diagnostic metadata.

#### Scenario: Teacher publishes a generated suggestion
- **WHEN** a generated suggestion draft is published
- **THEN** the inserted generated question SHALL retain point-aware metadata including point keys, source audit, option links, coverage tags, quality flags, and review lineage
- **AND** the inserted question SHALL be stored outside the imported default bank unless an explicit promotion process later moves it.

### Requirement: Deterministic objective suggestion policy
AI suggestions SHALL remain objective and deterministic.

#### Scenario: Suggestion is validated
- **WHEN** a generated suggestion is validated
- **THEN** its type SHALL be `single_choice`, `true_false`, or `fill_blank`
- **AND** its answer SHALL be machine-gradable without AI semantic judging.

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

### Requirement: Prompt refinement preserves machine-valid question shape
Teacher prompts SHALL refine AI generation intent while the system preserves deterministic objective question structure.

#### Scenario: Prompt asks for direct manual structure changes
- **WHEN** a teacher prompt asks to directly overwrite answer JSON, point keys, or source audit fields
- **THEN** the system SHALL treat the prompt as an AI revision instruction
- **AND** the returned candidate SHALL still pass objective validation before publication is allowed.

#### Scenario: Prompt asks for unsupported subjective grading
- **WHEN** a teacher prompt asks for a subjective or AI-judged item type
- **THEN** the system SHALL keep suggestions limited to `single_choice`, `true_false`, or `fill_blank`
- **AND** it SHALL require machine-gradable answer metadata.

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
