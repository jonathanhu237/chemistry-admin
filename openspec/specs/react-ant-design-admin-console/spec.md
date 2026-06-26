# react-ant-design-admin-console Specification

## Purpose
Define the React + Ant Design teacher admin console shell, teacher workflow navigation, overview layout, visual conventions, integrated experiment workspace, and shared route states.
## Requirements
### Requirement: React Ant Design admin shell

The teacher console SHALL be implemented as a React + TypeScript + Ant Design desktop web application named `web-teacher`.

#### Scenario: Authenticated teacher-console user opens web-teacher

- **GIVEN** an active teacher-console user with `role='admin'` or compatible legacy `role='teacher'` is authenticated
- **WHEN** they open the teacher console
- **THEN** the system SHALL render a React application shell with Ant Design `Layout`, top account controls, route-based content, and a left navigation menu
- **AND** the shell SHALL load route data through typed API clients rather than direct DOM mutation.

#### Scenario: Unauthenticated user opens teacher console

- **GIVEN** a user is not authenticated or their session has expired
- **WHEN** they open a teacher-console route
- **THEN** the system SHALL redirect them to the teacher-console login screen
- **AND** successful login SHALL return them to the intended teacher-console route when possible.

#### Scenario: Non-teacher-console role opens teacher console

- **GIVEN** a student or platform-admin user is authenticated
- **WHEN** they open a teacher-console route
- **THEN** the system SHALL reject the session for the teacher console.

### Requirement: Teacher workflow navigation
The teacher console SHALL expose navigation organized around teacher operations for the experiment-centered product direction without feature-tier branching between teacher-console roles.

#### Scenario: Teacher views navigation
- **GIVEN** a teacher-console user is logged in
- **WHEN** the teacher menu is displayed
- **THEN** the menu SHALL include dashboards for overview, classes and students, experiment management, question bank management, learning analytics, learning assistant, intelligent monitoring, learning resources, feedback, and system settings
- **AND** the Classes and Students route SHALL use card-first class navigation rather than a table-first class list
- **AND** the Experiment Management route SHALL include video resource management inside experiment detail
- **AND** it SHALL NOT present course version management or video resources as primary teacher workflows.

#### Scenario: Teacher opens deprecated review workflow
- **GIVEN** a teacher previously used the generic question review workflow
- **WHEN** they look for question administration
- **THEN** the console SHALL route them to experiment question bank management
- **AND** it SHALL NOT expose generic "question review" as the main workflow.

#### Scenario: Legacy teacher views navigation
- **GIVEN** a legacy `role='teacher'` user is logged in
- **WHEN** the teacher menu is displayed
- **THEN** the navigation SHALL match the complete navigation available to `role='admin'`
- **AND** it SHALL NOT hide learning assistant, intelligent monitoring, or other teacher-console modules because of role.

### Requirement: Chapter-first overview aligned with the mini-program

The admin overview SHALL mirror the student H5/mini-program learning path of area selection followed by chapter selection.

#### Scenario: Teacher opens overview
- **GIVEN** the mini-program organizes learning as area -> chapter -> chapter detail
- **WHEN** a teacher opens the admin overview
- **THEN** the overview SHALL group theory chapters 13-22 by theory area and human-readable chapter title
- **AND** it SHALL show experiments, videos, and question resources as resources bound under each chapter rather than as the top-level overview table.

#### Scenario: Chapter has no bound experiments
- **GIVEN** a theory chapter has no bound experiment
- **WHEN** the teacher views the chapter overview
- **THEN** the system SHALL explicitly show the chapter row
- **AND** it SHALL display that no experiment is currently bound without using primary or partial coverage labels.

#### Scenario: Chapter has bound experiments
- **GIVEN** one or more experiments are bound to a theory chapter
- **WHEN** the teacher views the chapter overview
- **THEN** the chapter row SHALL show the bound experiments and resource counts
- **AND** it SHALL NOT label any bound experiment as primary, partial, or supporting.

### Requirement: Visual consistency with mini-program brand

The admin console SHALL use Ant Design components while preserving the visual identity of the existing H5/mini-program frontend.

#### Scenario: Admin UI renders standard pages

- **GIVEN** the admin UI has loaded
- **WHEN** list, form, dashboard, drawer, modal, and upload pages are rendered
- **THEN** they SHALL use the project's existing green/teal visual language, restrained page background, compact card radius of 8px or less, and readable desktop table density
- **AND** they SHALL avoid a generic unrelated Ant Design theme.

### Requirement: Operational page states

Every admin route SHALL provide clear loading, empty, error, and permission-denied states.

#### Scenario: API request fails

- **GIVEN** an admin page requests data from the backend
- **WHEN** the request fails
- **THEN** the page SHALL display an Ant Design error state with retry support
- **AND** it SHALL avoid leaving partially rendered stale controls that can mutate unknown state.

#### Scenario: No records exist

- **GIVEN** a teacher opens a page with no matching records
- **WHEN** filters are applied or the dataset is empty
- **THEN** the page SHALL display an Ant Design empty state and the next available action when appropriate.

### Requirement: Integrated experiment resource workspace

The admin console SHALL manage experiment basic information, chapter bindings, and video resources inside a single experiment detail workspace.

#### Scenario: Teacher opens experiment management
- **GIVEN** a teacher is logged in
- **WHEN** they open the experiment management route
- **THEN** the page SHALL show experiments in a teacher-friendly list using sequence number, experiment name, bound chapters, resource status, publication status, and edit action
- **AND** it SHALL provide a clear action to create a new experiment.

#### Scenario: Teacher edits a selected experiment
- **GIVEN** a teacher selects an experiment
- **WHEN** the experiment detail workspace opens
- **THEN** the workspace SHALL include sections for basic information, bound theory chapters, video resources, and publication/archive status
- **AND** it SHALL keep database identifiers and coverage-strength fields hidden from the teacher.

#### Scenario: Teacher manages video inside experiment detail
- **GIVEN** a teacher is editing an experiment
- **WHEN** they upload, bind, publish, or review a video resource
- **THEN** the action SHALL happen inside the experiment detail workspace
- **AND** the teacher SHALL NOT need to use a separate primary video resources page.

### Requirement: Admin learning assistant test page
The teacher console SHALL provide a "learning assistant" page for all teacher-console accounts to test the student learning assistant guardrails.

#### Scenario: Teacher-console user opens learning assistant page
- **WHEN** an authenticated teacher-console user opens `/learning-assistant`
- **THEN** the page SHALL show a learning assistant test form with question input, optional student/chapter/experiment/knowledge-point context, RAG toggle, progress lookup toggle, and sample prompts
- **AND** it SHALL describe the test as a simulation of student learning-page chat.

#### Scenario: Legacy teacher operator views navigation
- **WHEN** an authenticated legacy teacher operator views the teacher-console navigation
- **THEN** the learning assistant test page SHALL be shown as a teacher workflow.

#### Scenario: Teacher-console user submits a test prompt
- **WHEN** a teacher-console user submits a learning assistant test prompt
- **THEN** the page SHALL call the admin learning assistant test API
- **AND** the API SHALL execute the request as student chat rather than as teacher AI.

#### Scenario: Guardrail result is returned
- **WHEN** the test API returns an assistant response
- **THEN** the page SHALL show the answer, mode, policy tag, guardrail decisions, source references, tool calls, and raw classification diagnostics.

#### Scenario: Student AI configuration is disabled
- **WHEN** the student AI assistant or student RAG feature switch affects the test request
- **THEN** the page SHALL show the current AI configuration status
- **AND** submission results SHALL reflect the same feature-switch behavior used by student chat.

### Requirement: Operational monitoring route layout
The teacher console SHALL support dense operational pages that use Ant Design modules, tabs, tags, alerts, tables/lists, and responsive grids without becoming landing pages or monolithic card stacks.

#### Scenario: Intelligent monitoring route opens
- **WHEN** a teacher opens the `智能监控` route
- **THEN** the page SHALL render the operational content directly after the page title
- **AND** it SHALL use tabs or equivalent module navigation for detailed diagnostics rather than a single long card stack.

#### Scenario: Monitoring page contains many diagnostic panels
- **WHEN** the page needs to show OpenAI, RAG, ES, dictionary, outbox, guardrail, and trend diagnostics
- **THEN** related panels SHALL be grouped inside named modules
- **AND** the default view SHALL prioritize status and next action over exhaustive detail.

#### Scenario: Monitoring page is viewed on narrow laptop widths
- **WHEN** the left shell navigation and page content compete for horizontal space
- **THEN** the monitoring route SHALL stack or wrap module content without requiring horizontal page scrolling
- **AND** primary actions such as refresh, search diagnostics, and module navigation SHALL remain reachable.

### Requirement: Explainable smart assessment strategy controls
The admin console SHALL provide teacher-facing controls and visual previews for smart assessment composition strategy.

#### Scenario: Admin edits global smart assessment defaults
- **WHEN** an administrator opens system settings
- **THEN** the page MUST provide controls for smart assessment enabled state, total question count, untested point ratio, weak tendency percentage, and maximum questions per experiment
- **AND** the controls MUST use teacher-facing labels rather than internal algorithm names.

#### Scenario: Teacher sees mastery ticket curve
- **WHEN** a user edits or previews smart assessment strategy
- **THEN** the UI MUST show a chart mapping point mastery score to relative draw tickets for measured points
- **AND** it MUST label the chart as relative draw tickets or relative weight rather than final probability.

#### Scenario: Teacher changes weak tendency
- **WHEN** the weak tendency percentage changes
- **THEN** the strategy curve MUST update to show how lower mastery scores receive more tickets
- **AND** a zero weak tendency MUST render an approximately flat measured-point curve.

#### Scenario: Teacher changes untested ratio
- **WHEN** the untested point ratio changes
- **THEN** the UI MUST show untested quota separately from the measured-point mastery curve
- **AND** it MUST NOT display untested points as a fake mastery score on the curve.

#### Scenario: Teacher previews class distribution
- **WHEN** a class strategy preview is available
- **THEN** the UI SHOULD show estimated paper composition for the current class, including untested point quota, measured point distribution grouped by experiment, and any underfilled-pool warnings
- **AND** the preview MUST make clear that final papers depend on question availability and session sampling.

### Requirement: Custom assessment controls
The admin console SHALL provide simple teacher-facing controls for student custom assessment availability and question-count boundaries.

#### Scenario: Admin edits global custom assessment defaults
- **WHEN** an administrator opens system settings
- **THEN** the page MUST provide controls for custom assessment enabled state, default question count, maximum question count, and maximum questions per experiment
- **AND** default and maximum question count controls MUST use fixed values from `5`, `10`, `15`, and `20`.

#### Scenario: Admin configures custom assessment question boundaries
- **WHEN** an administrator saves custom assessment settings
- **THEN** the UI MUST prevent a default question count greater than the maximum question count
- **AND** the student H5 MUST only expose question-count options up to the effective maximum.

#### Scenario: Teacher edits class custom assessment settings
- **WHEN** an authorized teacher or admin opens class settings
- **THEN** the class settings UI MUST show whether custom assessment settings are inherited or overridden
- **AND** it MUST allow authorized users to save or clear class-level custom assessment settings.

#### Scenario: Custom assessment is disabled
- **WHEN** custom assessment is disabled by effective settings
- **THEN** the student H5 assessment center MUST keep smart assessment available if enabled
- **AND** it MUST show custom assessment as unavailable rather than opening the custom selection page.

