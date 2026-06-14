## ADDED Requirements

### Requirement: Point-first enhanced diagnostic bank
The system SHALL support a diagnostic enhanced question-bank artifact authored from existing formal experiment video points rather than from old question-bank rows.

#### Scenario: Enhanced item is accepted
- **WHEN** an enhanced diagnostic question is accepted
- **THEN** it SHALL reference one primary existing experiment video point key
- **AND** it SHALL reference the formal experiment id and experiment code for that point
- **AND** it SHALL include source audit metadata with canonical experiment chunk ids, evidence sufficiency, and a reviewer note.

#### Scenario: Enhanced item spans multiple points
- **WHEN** a question requires evidence from more than one experiment video point
- **THEN** it SHALL keep one primary point key for coverage counting
- **AND** it SHALL store secondary point keys for the additional evidence targets.

### Requirement: Fixed diagnostic question mix
The enhanced bank SHALL target exactly `2` single-choice questions and `1` true/false question for each covered experiment video point.

#### Scenario: Demo artifact is validated
- **WHEN** the demo enhanced bank is validated
- **THEN** every covered point SHALL have exactly two `single_choice` questions
- **AND** every covered point SHALL have exactly one `true_false` question.

#### Scenario: Full artifact is planned
- **WHEN** the full enhanced bank is planned from the current formal experiment point inventory
- **THEN** the expected question count SHALL equal the current point count multiplied by three
- **AND** the plan SHALL report the expected single-choice and true/false counts before generation.

### Requirement: Mobile-safe objective answer policy
The enhanced bank SHALL use deterministic objective answers without fill-blank or AI-semantic grading.

#### Scenario: Enhanced question type is validated
- **WHEN** an enhanced diagnostic question is validated
- **THEN** its type SHALL be either `single_choice` or `true_false`
- **AND** it SHALL NOT require a free-text answer, equation entry, reagent-combination recall, or AI-based correctness judgment.

### Requirement: Option-level diagnostic links
Single-choice enhanced questions SHALL include option-level links that explain the diagnostic meaning of each answer option.

#### Scenario: Single-choice question is accepted
- **WHEN** an enhanced `single_choice` question is accepted
- **THEN** every option SHALL have an option link with the option label and diagnostic role
- **AND** the correct option SHALL be marked as `correct_evidence`
- **AND** incorrect options SHALL be marked as `misconception`, `adjacent_point`, `adjacent_experiment`, `weak_distractor`, or `unrelated_distractor`.

#### Scenario: Distractors are too weak
- **WHEN** a single-choice draft has distractors that do not reveal a plausible misconception or adjacent confusion
- **THEN** the draft SHALL be rewritten before it can be accepted.

### Requirement: Demo-first generation workflow
The enhanced bank SHALL be proven through a limited demo artifact before full 77-experiment generation.

#### Scenario: Demo is produced
- **WHEN** this change is implemented
- **THEN** it SHALL produce a demo enhanced-bank artifact for a small representative point set
- **AND** the demo report SHALL summarize covered experiments, covered points, question counts, source audit status, and reviewer quality notes.

#### Scenario: Demo is reviewed
- **WHEN** the demo has not been accepted by the product owner
- **THEN** the system SHALL NOT generate or promote the full enhanced default bank as a published student-facing bank.
