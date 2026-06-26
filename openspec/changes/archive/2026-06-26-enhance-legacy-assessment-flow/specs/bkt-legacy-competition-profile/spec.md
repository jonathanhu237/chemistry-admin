## ADDED Requirements

### Requirement: Legacy student assessment uses a unified setup page
The old student `评测` module SHALL present smart weak-point testing and self-selected experiment practice as one traditional assessment setup page rather than separate modern entry cards.

#### Scenario: Student opens legacy assessment root
- **WHEN** a logged-in old student opens `评测`
- **THEN** the page MUST render a SYSU-red old-style assessment setup form
- **AND** it MUST show the BKT assessment narrative in legacy-facing terms such as `掌握度`, `薄弱项`, `智能组卷`, `实验范围`, and `题数`
- **AND** it MUST NOT render the previous one-button-only smart assessment page as the primary experience
- **AND** it MUST NOT expose Atom, RAG, Agent, learning assistant, retrieval, provider, model, chunk, embedding, rerank, or monitoring wording

#### Scenario: Student sees one combined assessment control surface
- **WHEN** the assessment setup page loads successfully
- **THEN** it MUST show mode controls, experiment-range controls, question-count controls, and one primary start action on the same page
- **AND** it MUST NOT require the student to choose between separate `智能组卷` and `自主测评` launcher cards before seeing the experiment list
- **AND** the page MUST keep a square, old teaching-platform layout using form rows, checkbox rows, or table-like list rows rather than modern rounded mobile cards

#### Scenario: Assessment options are loaded
- **WHEN** the old assessment setup page needs experiment-range data
- **THEN** it MUST load available experiment options from the current student custom-assessment options API or an old-scoped adapter with equivalent shared identities
- **AND** each selectable row MUST show the experiment title and available question count
- **AND** rows with no available questions MUST be disabled or visibly unavailable rather than selectable as normal rows
- **AND** the option identities MUST remain current backend experiment ids, not old-only ids

#### Scenario: Assessment options fail to load
- **WHEN** experiment-range options cannot be loaded
- **THEN** the old frontend MUST render a controlled old-style unavailable or retry state
- **AND** it MUST still allow `智能薄弱项测试` to be started if the smart-assessment start API is available independently
- **AND** it MUST NOT show raw backend diagnostics, provider names, SQL, retrieval, or model wording

### Requirement: Legacy assessment setup supports smart selected random and all-range modes
The old student assessment setup SHALL support `智能薄弱项测试`, `自选实验范围`, `随机练习`, and `全部范围` modes with clear request semantics.

#### Scenario: Student starts smart weak-point testing
- **WHEN** the student selects `智能薄弱项测试` and clicks the primary start action
- **THEN** the old frontend MUST call the current smart assessment start API
- **AND** the request MUST let the backend/BKT algorithm choose weak, unmeasured, or otherwise prioritized assessment coverage
- **AND** manual experiment checkbox selection MUST NOT be required for this mode
- **AND** the resulting session MUST open in the old exam-taking page

#### Scenario: Student starts selected-range practice
- **WHEN** the student selects `自选实验范围`, selects one or more experiments, chooses a question count, and clicks the primary start action
- **THEN** the old frontend MUST call the current custom assessment start API with the selected experiment ids and question count
- **AND** the resulting session MUST open in the old exam-taking page
- **AND** if no experiment is selected, the page MUST show a legacy-facing validation message instead of starting a request

#### Scenario: Student starts random practice
- **WHEN** the student selects `随机练习` and clicks the primary start action
- **THEN** the old frontend MUST choose eligible experiment ids from the currently available option set or current filtered option set
- **AND** it MUST call the custom assessment start API with the generated random experiment id set and selected question count
- **AND** it MUST show enough selected/random context before or after start for the student to understand that this was range-randomized practice
- **AND** it MUST NOT describe random practice as the BKT weak-point algorithm

#### Scenario: Student starts all-range practice
- **WHEN** the student selects `全部范围` and clicks the primary start action
- **THEN** the old frontend MUST select all eligible experiments with available questions
- **AND** it MUST call the custom assessment start API with those experiment ids and selected question count
- **AND** it MUST not include disabled or zero-question rows in the request

#### Scenario: Student changes search filter and batch selection
- **WHEN** the student types in the assessment search field
- **THEN** the visible experiment list MUST filter by experiment title, parent title, chapter/category text, or code when available
- **AND** batch actions such as `全选当前列表`, `清空`, `随机选择`, or `仅显示有题实验` MUST operate predictably on the current eligible option set
- **AND** the selected count and target question count MUST update without navigating away from the setup page

#### Scenario: Student chooses question count
- **WHEN** custom assessment option settings provide question-count choices
- **THEN** the old setup page MUST render those choices as square old-style buttons or segmented controls
- **AND** the selected question count MUST be used for `自选实验范围`, `随机练习`, and `全部范围`
- **AND** the page MUST fall back to safe choices such as `5`, `10`, `15`, and `20` only when the API returns no configured choices

### Requirement: Legacy generated assessments open in an old exam-taking page
The old student frontend SHALL route smart, custom, random, all-range, and point-scoped generated assessment sessions into an old-style exam-taking page.

#### Scenario: Smart assessment session is generated
- **WHEN** the old setup page receives a smart assessment session response
- **THEN** it MUST store the session payload in old frontend session storage or equivalent old-scoped transient storage
- **AND** it MUST navigate to an old route such as `/assessment/session/:sessionId`
- **AND** the old bottom navigation MUST keep `评测` active while the session page is open

#### Scenario: Custom assessment session is generated
- **WHEN** the old setup page receives a custom assessment session response from selected, random, or all-range mode
- **THEN** it MUST store the session payload in old frontend session storage or equivalent old-scoped transient storage
- **AND** it MUST navigate to the same old exam-taking route used by smart sessions
- **AND** the page copy MUST distinguish custom/self-selected practice from BKT smart weak-point testing

#### Scenario: Point post-learning assessment is generated
- **WHEN** the student clicks `进行学后测评` on an old point detail page and the backend returns a point-scoped assessment session
- **THEN** the old frontend MUST navigate to the old exam-taking page rather than only rendering a composition summary
- **AND** the exam page MUST label the session as point-scoped or post-learning assessment using old-facing copy
- **AND** the route MUST preserve the old product boundary and bottom navigation behavior

#### Scenario: Session route is opened without stored payload
- **WHEN** a student opens an old assessment session route and the generated session payload is unavailable
- **THEN** the old frontend MUST render a controlled old-style state telling the student to return and start a new assessment
- **AND** it MUST NOT attempt to recreate an arbitrary session with unrelated questions
- **AND** it MUST NOT show raw storage, JSON parsing, or backend diagnostic errors

### Requirement: Legacy exam page renders a square paper-like answering experience
The old student exam-taking page SHALL render current assessment questions in a traditional square examination layout while preserving current answer semantics.

#### Scenario: Student opens an old exam session
- **WHEN** a stored smart, custom, or point assessment session is opened
- **THEN** the page MUST show an old-style exam heading with session mode, covered experiments or points, total question count, and composition hints when available
- **AND** it MUST render question cards with square borders and old teaching-platform spacing
- **AND** it MUST NOT import or visually expose the modern green H5 assessment panel style

#### Scenario: Single choice question is rendered
- **WHEN** a question has `question_type` equal to `single_choice`
- **THEN** the page MUST render each option as a selectable square row
- **AND** selecting one option MUST store that option as the answer for the question
- **AND** the selected state MUST be visible without relying only on color

#### Scenario: True false question is rendered
- **WHEN** a question has `question_type` equal to `true_false`
- **THEN** the page MUST render exactly two answer choices for `正确` and `错误`
- **AND** selecting one choice MUST store a backend-compatible true/false answer value

#### Scenario: Fill blank question is rendered
- **WHEN** a question has `question_type` equal to `fill_blank`
- **THEN** the page MUST render a square old-style text input
- **AND** the typed value MUST be stored as the answer for that question

#### Scenario: Student submits before all questions are answered
- **WHEN** at least one rendered question has no answer
- **THEN** the submit action MUST be disabled or MUST show a clear old-style validation message
- **AND** the frontend MUST NOT submit a partial answer payload as if it were complete

#### Scenario: Student submits completed answers
- **WHEN** every question has an answer and the student submits
- **THEN** the old frontend MUST call the current smart-assessment submit API with the session id and answer list
- **AND** the backend MUST remain responsible for scoring, BKT mastery updates, report creation, and next recommendations
- **AND** the old frontend MUST render or navigate to an old-compatible result/report state after successful submission

#### Scenario: Backend returns an underfilled assessment
- **WHEN** a generated assessment contains fewer questions than requested because the available question bank is insufficient
- **THEN** the old exam page or setup transition MUST show a controlled old-style notice with the actual and requested question counts
- **AND** it MUST still allow the student to answer the generated questions

### Requirement: Legacy assessment implementation preserves current product and data boundaries
The old assessment implementation SHALL reuse current assessment APIs and data identities unless old-scoped adapters are explicitly necessary.

#### Scenario: Maintainer inspects old assessment API usage
- **WHEN** the implementation is inspected
- **THEN** old assessment setup, session, point post-learning assessment, and submission flows MUST use current student assessment endpoints when possible
- **AND** any backend code introduced solely for old assessment MUST be clearly old-scoped or legacy-scoped
- **AND** the implementation MUST NOT change current `web-student` assessment routes, modern assessment UI, or mainline API semantics merely to support old styling

#### Scenario: Assessment data is inspected after implementation
- **WHEN** generated assessment sessions, submitted answers, mastery updates, reports, or experiment/question ids are inspected
- **THEN** they MUST use current backend identities and current BKT/reporting mechanisms
- **AND** they MUST NOT require old-only question records, old-only experiment records, old-only mastery rows, or a separate legacy database

#### Scenario: Legacy assessment UI is scanned
- **WHEN** old assessment setup, exam, loading, empty, validation, and error states are scanned
- **THEN** they MUST preserve the legacy forbidden-term gate for Atom, RAG, Agent, chunk, embedding, rerank, Qwen, BGE, OpenAI, learning assistant, intelligent monitoring, provider, and retrieval diagnostics
- **AND** they MAY show legacy-facing AI/BKT terms such as `AI出题`, `BKT`, `掌握度`, `智能组卷`, `薄弱项`, `题库`, and `学情`
