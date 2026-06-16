## ADDED Requirements

### Requirement: Point-aware diagnostic bank migration closure
The system SHALL treat the imported reviewed point-aware default bank as the current production migration target for experiment question-bank diagnostics.

#### Scenario: Production point-aware bank is used
- **WHEN** the teacher-facing question bank is opened after the reviewed bank import
- **THEN** the system SHALL use the imported default bank with formal experiment ids, primary point keys, source audit metadata, option links, and deterministic answer data
- **AND** it SHALL NOT require a separate fixed-mix enhanced-bank artifact for the current release.

#### Scenario: Objective question type mix is preserved
- **WHEN** imported point-aware questions are validated or displayed
- **THEN** the accepted student-facing types SHALL remain `single_choice`, `true_false`, and deterministic phone-friendly `fill_blank`
- **AND** the system SHALL NOT reject an otherwise valid imported fill-blank question merely because an older enhanced-bank plan excluded fill blanks.

#### Scenario: Fixed-mix diagnostic generation is reconsidered
- **WHEN** a future product requirement asks for exactly two single-choice and one true/false item per experiment video point
- **THEN** that requirement SHALL be proposed as a new explicit change
- **AND** it SHALL NOT silently override the current imported default bank.

### Requirement: Point-aware diagnostic release evidence
The system SHALL keep the release evidence for the imported point-aware default bank inspectable by administrators and teachers.

#### Scenario: Release bank is audited
- **WHEN** an administrator inspects the imported default bank
- **THEN** the system SHALL expose or preserve validation evidence showing question count, experiment coverage, point bindings, source refs, source audit status, option links, and deterministic answer shape.

#### Scenario: Teacher inspects a migrated question
- **WHEN** a teacher opens a migrated question detail
- **THEN** the console SHALL show the linked experiment, primary point titles, evidence status, source references, answer, explanation, and option-level diagnostic links where available.
