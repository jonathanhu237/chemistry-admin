## ADDED Requirements

### Requirement: Legacy teacher exposes learning scores and BKT mastery
The legacy teacher frontend SHALL expose teacher-readable class and student learning scores that close the BKT feedback loop.

#### Scenario: Legacy teacher reviews class learning scores
- **WHEN** a teacher opens legacy class analytics for a class with student assessment or mastery evidence
- **THEN** the old UI MUST show class-level learning score, experiment completion, assessment score, mastery or weak-point summaries where available
- **AND** it MUST connect those metrics to BKT mastery or experiment learning progress
- **AND** it MUST NOT require intelligent monitoring or RAG diagnostics to understand the class state

#### Scenario: Legacy teacher reviews an individual student
- **WHEN** a teacher opens a legacy student learning report
- **THEN** the old UI MUST show that student's assessment outcomes, mastery state, weak experiment points, recent learning activity, and recommended follow-up where available
- **AND** it MUST use teacher-facing learning-score language rather than Atom assistant, Agent, or retrieval-diagnostic language

### Requirement: Legacy analytics use shared assessment and mastery records
The legacy teacher frontend SHALL read analytics from the shared backend records used by current class analytics.

#### Scenario: Student completes assessment in old or current frontend
- **WHEN** a student completes an assessment in either current or old student frontend
- **THEN** the old teacher analytics view MUST be able to reflect the resulting shared score and mastery records when the teacher has access to that class
- **AND** the old teacher view MUST NOT depend on old-only analytics tables or duplicated student score imports
