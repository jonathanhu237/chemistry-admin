# student-h5-assessment-flow Specification

## Purpose
Define student H5 pretest, posttest, explanation caching, mastery update, and recommendation safety behavior.
## Requirements
### Requirement: Student pretest session lifecycle
The system SHALL let students start, continue, and submit pretest sessions using server-side session records.

#### Scenario: Student starts a pretest
- **WHEN** an authenticated student starts a pretest
- **THEN** the backend SHALL create or return the current open pretest session
- **AND** it SHALL return questions without exposing hidden answer keys.

#### Scenario: Student submits a pretest
- **WHEN** a student submits answers for an open pretest session
- **THEN** the backend SHALL grade the answers
- **AND** it SHALL persist the completed session and item outcomes for later learning context.

### Requirement: Student posttest session lifecycle
The system SHALL let students start, continue, and submit posttest sessions after learning activity.

#### Scenario: Student starts a posttest
- **WHEN** an authenticated student starts a posttest for an available experiment context
- **THEN** the backend SHALL create or return an eligible posttest session
- **AND** it SHALL return questions without exposing hidden answer keys.

#### Scenario: Student submits a posttest
- **WHEN** a student submits answers for an open posttest session
- **THEN** the backend SHALL grade the answers
- **AND** it SHALL persist score, item outcomes, and mistake details for review.

### Requirement: Cached student assessment explanations
The system SHALL provide cached posttest summaries and wrong-answer explanations without requiring repeated AI generation for unchanged completed attempts.

#### Scenario: Student requests posttest summary
- **WHEN** a completed posttest has a cached AI summary
- **THEN** the backend SHALL return the cached summary
- **AND** it SHALL NOT regenerate it unless cache invalidation rules require regeneration.

#### Scenario: Student requests mistake explanation
- **WHEN** a completed posttest contains wrong answers eligible for review
- **THEN** the backend SHALL return generated or cached explanations only for the student's submitted mistakes
- **AND** it SHALL NOT reveal answers for unrelated unsubmitted assessment items.

### Requirement: Assessments update experiment mastery
Student H5 pretest and posttest submissions SHALL update experiment-level mastery evidence when submitted answers can be associated with formal experiments.

#### Scenario: Pretest submission records experiment mastery
- **WHEN** a student submits a completed pretest with graded question attempts linked to formal experiments
- **THEN** the backend MUST update experiment-level mastery state for those experiments
- **AND** it MUST preserve evidence kind and evidence identifier metadata for later analytics.

#### Scenario: Posttest submission records experiment mastery
- **WHEN** a student submits a completed posttest with graded question attempts linked to formal experiments
- **THEN** the backend MUST update experiment-level mastery state for those experiments
- **AND** the posttest report MUST be able to show experiment-level mastery changes where available.

#### Scenario: Experiment mastery table is unavailable before migration
- **WHEN** a local or test database lacks the experiment mastery table
- **THEN** student assessment submission MUST fail gracefully or skip optional mastery updates according to existing compatibility barriers
- **AND** core pretest/posttest completion MUST remain reliable.

### Requirement: Experiment mastery informs learning recommendation safely
The student H5 learning recommendation logic SHALL be allowed to use experiment mastery as an optional signal without replacing seed-backed current-chapter selection.

#### Scenario: Mastery data exists for candidate chapters
- **WHEN** experiment mastery data exists for a student's candidate chapter experiments
- **THEN** the recommendation logic MAY choose the weakest relevant current-family chapter profile
- **AND** the returned learning payload MUST still use the seed-backed profile, catalog chapter, and point grouping contract.

#### Scenario: Mastery data is missing
- **WHEN** no experiment mastery evidence exists or the mastery query is unavailable
- **THEN** the recommendation logic MUST fall back to existing seed, pretest-area, and default profile behavior.

### Requirement: Student point assessment session lifecycle
The student H5 SHALL let authenticated students start a point-scoped assessment from a catalog point detail page after learning that point.

#### Scenario: Student starts point assessment
- **WHEN** an authenticated student starts point assessment for a valid catalog `point_node_id` and has no open assessment session
- **THEN** the backend MUST create an assessment session with `assessment_mode = "point"`
- **AND** it MUST compose questions only from published student-visible questions bound to that `point_node_id`
- **AND** it MUST return public questions without exposing hidden answer keys.

#### Scenario: Point assessment reuses open session
- **WHEN** a student starts point assessment while any assessment session is already in progress
- **THEN** the backend MUST return the existing open session rather than creating a point session
- **AND** the student H5 MUST tell the student that an unfinished assessment is being continued.

#### Scenario: Point assessment handles insufficient questions
- **WHEN** a point assessment is started for a point with one or more eligible questions but fewer than the target question count
- **THEN** the backend MUST create an underfilled point assessment
- **AND** the response composition metadata MUST indicate that the point question bank was underfilled.

#### Scenario: Point assessment rejects zero eligible questions
- **WHEN** a point assessment is started for a point with zero eligible published point-backed questions
- **THEN** the backend MUST reject the request
- **AND** it MUST NOT create a new assessment session.

### Requirement: Student assessment status and baseline prompt
The student H5 SHALL use server assessment status to guide students toward completing an initial smart assessment baseline and continuing unfinished assessments.

#### Scenario: Student assessment status is loaded
- **WHEN** an authenticated student enters the H5 shell
- **THEN** the frontend MUST request the student's assessment status
- **AND** the backend MUST report whether a completed `smart` assessment exists
- **AND** it MUST report any open assessment session id and mode
- **AND** it MUST report whether the smart-baseline prompt was permanently dismissed.

#### Scenario: Open assessment prompt has priority
- **WHEN** the assessment status reports an open assessment session
- **THEN** the student H5 MUST show a continuation prompt before any smart-baseline prompt
- **AND** continuing the prompt MUST navigate to the open assessment session.

#### Scenario: Smart baseline prompt is shown
- **WHEN** the assessment status reports no completed `smart` assessment, no open assessment, and no baseline prompt dismissal
- **THEN** the student H5 MUST show a dialog recommending a first smart assessment
- **AND** accepting the dialog MUST start or navigate to smart assessment.

#### Scenario: Smart baseline prompt is permanently dismissed
- **WHEN** the student chooses not to be reminded about the smart baseline prompt again
- **THEN** the frontend MUST call the dismissal endpoint
- **AND** future assessment status responses for that student MUST mark the prompt as dismissed.

#### Scenario: Point and custom assessments do not satisfy smart baseline
- **WHEN** a student has completed only `point` or `custom` assessments
- **THEN** the assessment status MUST still report that no completed smart baseline exists.

### Requirement: Student assessment submissions hand off to durable reports
Student H5 assessment submission flows SHALL create and hand off to durable report detail for pretest, custom assessment, smart assessment, and point assessment completions.

#### Scenario: Pretest submission completes
- **WHEN** a student submits the final pretest answers and grading succeeds
- **THEN** the backend SHALL create a durable `pretest` report snapshot
- **AND** the student app SHALL be able to navigate to that report without exposing pretest internal staging as report structure.

#### Scenario: Smart assessment submission completes
- **WHEN** a student submits a smart assessment and grading succeeds
- **THEN** the backend SHALL create a durable `smart` report snapshot
- **AND** the student app SHALL navigate to durable report detail rather than relying on browser session storage.

#### Scenario: Custom assessment submission completes
- **WHEN** a student submits a custom assessment and grading succeeds
- **THEN** the backend SHALL create a durable `custom` report snapshot
- **AND** the report SHALL preserve the selected experiment range and wrong-answer details.

#### Scenario: Point assessment submission completes
- **WHEN** a student submits a point assessment started after learning a point
- **THEN** the backend SHALL create a durable `point` report snapshot
- **AND** the report SHALL preserve the assessed point context.

### Requirement: Assessment report text is generated at submission time
Covered student H5 assessment submissions SHALL generate report summary and wrong-answer explanation text during submission and persist the result for future views.

#### Scenario: Generated text is available immediately
- **WHEN** a covered assessment submission returns successfully
- **THEN** the returned or subsequently loaded report SHALL include persisted summary and wrong-answer explanation text
- **AND** future report views SHALL reuse persisted text instead of generating a new answer.

#### Scenario: No wrong answers exist
- **WHEN** a covered assessment has no wrong answers
- **THEN** the persisted wrong-answer explanation SHALL state that there are no wrong answers to review
- **AND** the report SHALL still be valid and visible in report history.

### Requirement: Student smart assessment session lifecycle
The student H5 SHALL let authenticated students start, continue, submit, and review smart assessment sessions directly from the assessment destination.

#### Scenario: Student starts smart assessment
- **WHEN** an authenticated student starts a smart assessment from the `测评` page
- **THEN** the backend MUST create or return that student's current open smart assessment session
- **AND** it MUST return public questions without exposing hidden answer keys
- **AND** it MUST include a concise composition summary suitable for student display.

#### Scenario: Student resumes open smart assessment
- **WHEN** a student with an in-progress smart assessment starts smart assessment again
- **THEN** the backend MUST return the same open session rather than composing a new paper
- **AND** the question list MUST remain stable.

#### Scenario: Student submits smart assessment
- **WHEN** a student submits answers for an open smart assessment session
- **THEN** the backend MUST validate that submitted question ids exactly match the session questions
- **AND** it MUST grade the answers
- **AND** it MUST persist item attempts with a smart-assessment evidence kind
- **AND** it MUST complete the session with a report.

### Requirement: Student custom assessment selection
The student H5 SHALL provide a separate custom assessment mode where students select experiments and question count before starting a paper.

#### Scenario: Student opens custom assessment options
- **WHEN** an authenticated student opens the custom assessment selection page
- **THEN** the backend MUST return the effective custom assessment settings
- **AND** it MUST return only selectable published root or first-level experiments that have at least one eligible published point-backed question under their descendants
- **AND** it MUST NOT return hidden answer keys or question bodies in the options payload.

#### Scenario: Student searches and selects experiments
- **WHEN** custom assessment options are displayed
- **THEN** the UI MUST let the student search experiments by visible experiment text
- **AND** the UI MUST let the student select one or more experiments
- **AND** it MUST NOT require the student to choose by knowledge point, wrong-answer set, weak threshold, or measured/untested status.

#### Scenario: Student chooses custom assessment question count
- **WHEN** the student configures a custom assessment
- **THEN** the UI MUST offer fixed question-count options from `5`, `10`, `15`, and `20`
- **AND** it MUST hide options greater than the effective maximum question count
- **AND** it MUST preselect the effective default question count.

#### Scenario: Student starts custom assessment
- **WHEN** a student starts custom assessment with selected experiments and a valid question count
- **THEN** the backend MUST create or return that student's current open assessment session
- **AND** if no open session exists, it MUST compose questions only from descendant point-backed questions under the selected experiments
- **AND** it MUST mark the session as custom assessment.

#### Scenario: Custom assessment rejects invalid selection
- **WHEN** a student starts custom assessment without selected experiments, with an unsupported question count, or with experiments outside the selectable options
- **THEN** the backend MUST reject the request
- **AND** it MUST NOT create a new assessment session.

#### Scenario: Existing open assessment is reused across modes
- **GIVEN** a student has any in-progress assessment session
- **WHEN** the student starts smart assessment or custom assessment
- **THEN** the backend MUST return the existing open session rather than creating a second session.

### Requirement: Smart assessment composes by point mastery
Smart assessment composition SHALL select point-backed questions from the full eligible question bank, using point mastery evidence and teacher-configured strategy.

#### Scenario: Composition separates untested points
- **WHEN** the system composes a smart assessment
- **THEN** points with no mastery row or zero evidence count MUST be treated as untested
- **AND** untested points MUST NOT be assigned a fake mastery score for the mastery curve.

#### Scenario: Untested ratio reserves question quota
- **WHEN** the effective strategy has a non-zero untested point ratio
- **THEN** the composer MUST reserve the configured proportion of question slots for untested points where eligible untested questions exist
- **AND** if untested questions are insufficient, it MUST backfill from eligible measured points and record a warning.

#### Scenario: Measured points use mastery tickets
- **WHEN** the system selects from measured points
- **THEN** lower mastery scores MUST produce higher relative draw tickets according to the effective weak-tendency strategy
- **AND** high mastery points MUST retain non-zero draw opportunity unless no eligible questions exist.

#### Scenario: Only point-backed questions are eligible
- **WHEN** the backend builds smart assessment candidates
- **THEN** it MUST include only published questions bound to at least one valid point node
- **AND** questions without valid point binding MUST NOT be selected for smart assessment.

#### Scenario: Experiment question cap is enforced
- **WHEN** questions are selected for a smart assessment
- **THEN** the system MUST respect the effective maximum questions per root or first-level experiment where enough candidate points and questions exist
- **AND** it SHOULD select at most one question per point before using any point-level backfill
- **AND** if a selected experiment lacks enough point-backed questions, the composer MUST backfill from remaining eligible points before returning an underfilled paper.

### Requirement: Smart assessment updates point mastery
Smart assessment submissions SHALL update point-level mastery using BKT updates and derive experiment summaries from affected points.

#### Scenario: Completed smart assessment records mastery changes
- **WHEN** a student submits a smart assessment with graded attempts linked to point nodes
- **THEN** the backend MUST update `student_point_mastery` for those points using the configured BKT update model
- **AND** if a question is linked to multiple valid point nodes, every linked point MUST receive evidence from the graded result
- **AND** the report MUST include point mastery before/after changes grouped under affected experiments where available.

#### Scenario: Smart assessment report explains composition
- **WHEN** a completed smart assessment report is returned
- **THEN** it MUST include score, correct rate, experiment summary cards, point mastery changes, composition summary, and wrong-answer details where available
- **AND** experiment mastery shown in the report MUST be derived from descendant point mastery rather than stored as an independent fact
- **AND** it MUST explain untested and low-mastery point coverage in student-facing language without requiring the student to understand the internal ticket formula.

### Requirement: Custom assessment composes balanced papers from selected experiments
Custom assessment composition SHALL sample questions only from student-selected experiments and SHOULD cover selected experiments and their descendant points as evenly as question availability allows.

#### Scenario: Custom assessment samples selected experiments evenly
- **WHEN** the backend composes a custom assessment from multiple selected experiments
- **THEN** it MUST allocate requested question slots approximately evenly across selected experiments
- **AND** it MUST expand selected experiments to descendant point nodes
- **AND** it MUST prefer at most one question per point before selecting additional questions from an already covered point
- **AND** it MUST stable-shuffle eligible questions within each point or experiment bucket until the requested question count is reached or eligible questions are exhausted.

#### Scenario: Custom assessment handles insufficient questions
- **WHEN** selected experiments cannot fill the requested question count
- **THEN** the backend MUST return the underfilled assessment if at least one question was selected
- **AND** it MUST include warning metadata with requested and actual question counts
- **AND** the UI MUST tell the student that the selected experiment question bank was insufficient.

#### Scenario: Custom assessment has zero eligible questions
- **WHEN** selected experiments produce zero eligible questions
- **THEN** the backend MUST reject the start request
- **AND** it MUST explain that no eligible questions are available.

#### Scenario: Custom assessment report is simple
- **WHEN** a custom assessment is completed
- **THEN** the report MUST include at least correct rate, selected experiment summaries, and wrong-answer details where available
- **AND** it MUST NOT require a finalized custom report design beyond the shared assessment report shell.

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
