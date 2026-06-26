## ADDED Requirements

### Requirement: Legacy teacher preserves AI question generation and review loop
The legacy teacher frontend SHALL keep AI-assisted objective question generation with teacher review before publication.

#### Scenario: Legacy teacher generates questions
- **WHEN** a teacher requests AI-generated objective questions from a selected experiment, point, or chapter context in `web-teacher-old`
- **THEN** the system MUST produce teacher-reviewable draft questions using the shared backend workflow
- **AND** the teacher MUST be able to accept, reject, or request revision before any draft becomes student-facing
- **AND** the old UI MUST present this as `AI出题` or equivalent teacher-facing wording

#### Scenario: Legacy teacher reviews generated question evidence
- **WHEN** a generated or repaired question includes source grounding metadata
- **THEN** the old UI MAY show teacher-readable `教材依据`, `实验资料依据`, `出题依据`, or source-reference wording
- **AND** it MUST NOT show visible labels such as `RAG evidence`, `chunk`, `embedding`, `rerank`, `Qwen`, `BGE`, provider metadata, raw prompt traces, or retrieval diagnostics

### Requirement: Legacy question bank remains objective and BKT-compatible
The legacy teacher frontend SHALL present the question bank as the assessment source for BKT mastery and smart assessment composition.

#### Scenario: Legacy teacher opens question bank
- **WHEN** a teacher opens the old question bank page
- **THEN** the page MUST organize questions by experiment, video point, chapter, or legacy teaching unit as appropriate for the shared data
- **AND** it MUST show objective question type, answer, explanation, status, point/experiment binding, and review state where available
- **AND** it MUST make clear that accepted questions feed student testing, mastery calculation, and smart assessment composition

#### Scenario: Legacy teacher publishes or rejects a draft
- **WHEN** a teacher publishes or rejects a draft AI-generated question
- **THEN** the action MUST update the shared question-bank workflow according to current backend rules
- **AND** the old UI MUST NOT create old-only question ids or old-only seed artifacts
