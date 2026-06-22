## ADDED Requirements

### Requirement: Teacher can open a full student device preview
The teacher console SHALL provide a full student H5 preview page that displays the real student frontend inside a controlled phone-sized device shell.

#### Scenario: Teacher opens the student preview route
- **WHEN** an authenticated teacher opens the teacher-console student preview page
- **THEN** the page MUST request a teacher-authorized preview session from the backend
- **AND** it MUST render a phone-sized iframe using the returned student preview URL
- **AND** it MUST NOT ask the teacher to choose a student identity.

#### Scenario: Preview shell loads the real student SPA
- **WHEN** the preview iframe finishes bootstrap
- **THEN** the iframe MUST run the normal `web-student` SPA, router, shell, CSS, and feature modules
- **AND** changes made to the student frontend MUST be reflected in the teacher preview without duplicating student page code in `web-teacher`.

#### Scenario: Teacher uses preview controls
- **WHEN** the teacher changes device preset, orientation, zoom level, refresh, or open-in-window controls
- **THEN** the shell MUST update only the preview frame or iframe lifecycle
- **AND** it MUST NOT mutate student learning data, class data, catalog content, or teacher-authored data.

#### Scenario: Student preview cannot be created
- **WHEN** the backend cannot create or authorize the teacher preview session
- **THEN** the teacher page MUST show a controlled error and retry path
- **AND** it MUST NOT fall back to an unauthenticated public student URL.

### Requirement: Preview uses a teacher-owned hidden test student
The platform SHALL create or reuse one default hidden preview class and one default test student for each teacher preview owner.

#### Scenario: Teacher preview session is requested for the first time
- **WHEN** a teacher requests a student preview session and no preview class exists for that teacher
- **THEN** the backend MUST create a system-managed hidden preview class owned by that teacher
- **AND** it MUST create or link one default preview test student in that class
- **AND** the test student MUST be usable as a student session without requiring first-login password change.

#### Scenario: Teacher preview session is requested again
- **WHEN** a teacher who already has an active preview class and test student requests another preview session
- **THEN** the backend MUST reuse the existing preview class/test student unless a reset operation has explicitly invalidated them
- **AND** it MUST preserve the one active preview class/test student mapping for that teacher.

#### Scenario: Preview bootstrap ticket is exchanged
- **WHEN** the student frontend opens `/preview/session` with a valid teacher-preview ticket
- **THEN** the backend MUST exchange the ticket for a student-compatible preview session
- **AND** the session identity MUST include preview claims identifying the teacher owner, preview class, preview student, and preview purpose.

#### Scenario: Preview ticket is invalid or expired
- **WHEN** the student frontend attempts to exchange an invalid, reused, or expired preview ticket
- **THEN** the backend MUST reject the exchange
- **AND** the student app MUST render a controlled preview unavailable state rather than entering normal student routes.

### Requirement: Student frontend remains canonical with a thin preview runtime
The preview implementation SHALL reuse the existing student frontend and limit preview-specific student code to bootstrap, policy, route guard, and runtime extension points.

#### Scenario: Developer adds teacher preview functionality
- **WHEN** implementation adds the full teacher student preview
- **THEN** `web-teacher` MUST NOT import `web-student` route pages, student feature components, student CSS files, or student router internals
- **AND** teacher code MUST embed the student app through iframe or an equivalently isolated app boundary.

#### Scenario: Student app enters preview mode
- **WHEN** the student app receives a valid preview session
- **THEN** it MUST provide preview mode and preview policy through centralized app/runtime context
- **AND** student feature pages MUST continue to use the normal student router and shell.

#### Scenario: Preview-only route difference is needed
- **WHEN** a student route must be hidden, blocked, or redirected in preview mode
- **THEN** the behavior MUST be implemented through centralized route visibility, route guard, or app-config policy
- **AND** it MUST NOT require every individual page component to duplicate preview checks.

#### Scenario: Preview-only component difference is unavoidable
- **WHEN** a preview difference cannot be expressed through backend policy, app-config, route guard, or shared shell behavior
- **THEN** the page-local preview behavior MUST be narrowly scoped
- **AND** it MUST have focused test coverage proving normal student behavior is unchanged.

### Requirement: Preview policy governs unsupported or modified features
Preview-specific feature differences SHALL be expressed by backend policy and enforced consistently by student app-config, route guards, and backend endpoint guards.

#### Scenario: Preview policy disables a feature entry
- **WHEN** the preview policy disables a feature such as feedback, real account mutation, or another unsupported student action
- **THEN** the student app-config or runtime policy MUST hide or disable normal navigation entries for that feature
- **AND** direct route access MUST be blocked or redirected by a centralized guard.

#### Scenario: Preview request calls a blocked write endpoint
- **WHEN** a preview session calls a student write endpoint that is not allowed in preview mode
- **THEN** the backend MUST reject the request or return a controlled preview-only response according to policy
- **AND** it MUST NOT create normal student feedback, normal learning analytics, normal assessment records, or normal account mutation side effects.

#### Scenario: Preview request calls an allowed interaction endpoint
- **WHEN** a preview session uses an allowed interaction endpoint for visual or interaction review
- **THEN** the backend MUST scope resulting state to the preview test student or a preview-only storage path
- **AND** ordinary teacher analytics and normal class reports MUST exclude that preview state by default.

#### Scenario: Policy changes after the iframe is open
- **WHEN** preview policy changes while the teacher preview remains open
- **THEN** the student app MUST refresh policy through the normal app-config refresh path or a controlled reload
- **AND** stale policy MUST NOT grant access to blocked write behavior after backend policy denies it.

### Requirement: Device preview is a DevTools-like subset, not an embedded debugger
The teacher preview shell SHALL provide a focused device-preview subset without exposing browser debugging or unsafe emulation controls.

#### Scenario: Teacher uses the device selector
- **WHEN** the teacher selects a phone preset
- **THEN** the preview shell MUST apply curated CSS-pixel viewport dimensions for common iPhone and Android sizes
- **AND** it MUST keep the student app constrained within the selected phone screen.

#### Scenario: Teacher rotates the device
- **WHEN** the teacher switches between portrait and landscape
- **THEN** the preview shell MUST update the iframe viewport dimensions
- **AND** the student app MUST respond through its normal responsive layout behavior.

#### Scenario: Teacher expects debugger tools
- **WHEN** the teacher opens the preview shell
- **THEN** the shell MUST NOT expose DOM inspection, network panels, JavaScript source debugging, arbitrary user-agent editing, CPU throttling, or network throttling controls
- **AND** the shell MUST present itself as a student preview tool rather than a browser DevTools replacement.

### Requirement: Preview framing and origins are controlled
The platform SHALL allow the teacher app to frame only the expected student preview origin while preventing broad clickjacking exposure.

#### Scenario: Teacher and student apps use different local ports
- **WHEN** the teacher preview page runs on the teacher frontend origin and frames the student frontend origin
- **THEN** configuration MUST allow the expected local and deployed student preview origins
- **AND** it MUST NOT allow arbitrary external origins to be framed.

#### Scenario: Iframe tries to load an unexpected URL
- **WHEN** the teacher preview shell receives or computes a preview URL outside the allowed student origin list
- **THEN** it MUST reject the URL and show a controlled error
- **AND** it MUST NOT render the unexpected origin inside the teacher console.

#### Scenario: Student app is opened without preview bootstrap
- **WHEN** a user opens the normal student frontend without a valid student session or valid preview ticket
- **THEN** normal student authentication rules MUST still apply
- **AND** teacher credentials MUST NOT be treated as student credentials.

### Requirement: Preview implementation is verified across products
The change SHALL include focused verification that proves reuse of the student app, correct hidden-class behavior, and product-boundary safety.

#### Scenario: Frontend boundary checks run
- **WHEN** implementation is complete
- **THEN** tests or import-boundary checks MUST verify that `web-teacher` preview modules do not import student route/page modules
- **AND** `web-student` remains the owner of student learning, assessment, assistant, feedback, auth, and catalog behavior.

#### Scenario: Product builds and typechecks run
- **WHEN** implementation is complete
- **THEN** `web-teacher`, `web-student`, and `web-admin` typecheck/build validation MUST pass or any unavailable command MUST be documented with a concrete blocker.

#### Scenario: Browser preview QA runs
- **WHEN** browser or screenshot QA validates the teacher preview page
- **THEN** it MUST cover at least one iPhone-sized viewport, one Android-sized viewport, orientation switching, iframe refresh, and normal student route navigation inside the frame.

#### Scenario: Backend preview exclusions are tested
- **WHEN** backend tests cover teacher preview sessions
- **THEN** they MUST verify hidden preview classes are excluded from ordinary teacher class APIs
- **AND** preview/test-student state is excluded from normal analytics by default.
