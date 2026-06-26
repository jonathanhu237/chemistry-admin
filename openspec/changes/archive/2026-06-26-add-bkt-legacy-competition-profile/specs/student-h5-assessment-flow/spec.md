## ADDED Requirements

### Requirement: Legacy student assessments preserve BKT mastery loop
The legacy student frontend SHALL keep pretest, posttest, mastery update, learning recommendation, and smart assessment behavior as the core student learning loop.

#### Scenario: Legacy student completes assessment
- **WHEN** a student completes a pretest or posttest in `web-student-old`
- **THEN** the shared backend MUST grade the attempt and update available experiment or point mastery evidence
- **AND** the old frontend MUST present the result as BKT mastery, score, weak experiment point, or learning suggestion information
- **AND** the old frontend MUST NOT present the result as an Atom assistant or RAG-agent analysis

#### Scenario: Legacy student receives recommendations after assessment
- **WHEN** mastery evidence exists for the assessed experiment or point context
- **THEN** the old frontend MUST be able to show personalized experiment-video recommendations or next-test suggestions based on shared mastery data
- **AND** missing mastery evidence MUST fall back to controlled default recommendations without implying random recommendation

### Requirement: Legacy smart assessment copy is BKT-centered
The legacy student frontend SHALL describe smart assessment composition through mastery and BKT language.

#### Scenario: Legacy student starts a smart assessment
- **WHEN** a student starts an available smart assessment in the old product
- **THEN** visible copy MUST explain the assessment in terms of experiment learning, mastery, weak points, or BKT tracking
- **AND** it MUST NOT mention retrieval, chunks, model selection, Agent planning, or RAG evidence

#### Scenario: Legacy assessment report is rendered
- **WHEN** the old product renders a completed assessment report
- **THEN** it MUST show score, mastery change, wrong-answer review, weak experiment points, and recommended follow-up learning where available
- **AND** it MUST avoid assistant-branded report cards or current Atom visual treatment
