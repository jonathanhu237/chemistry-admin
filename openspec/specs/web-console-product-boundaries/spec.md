# web-console-product-boundaries Specification

## Purpose
TBD - created by archiving change split-web-admin-teacher-student-consoles. Update Purpose after archive.
## Requirements
### Requirement: Three web consoles have explicit product boundaries
The platform SHALL expose three independent web consoles named `web-admin`, `web-teacher`, and `web-student`.

#### Scenario: Services use canonical names and ports
- **WHEN** the default local or production-like service topology is inspected
- **THEN** the student frontend service MUST be named `web-student` and expose port `5173`
- **AND** the teacher frontend service MUST be named `web-teacher` and expose port `5174`
- **AND** the platform operations frontend service MUST be named `web-admin` and expose port `5175`.

#### Scenario: Product ownership is unambiguous
- **WHEN** a maintainer inspects frontend packages, Compose services, or documentation
- **THEN** `web-teacher` MUST identify the teacher console that owns experiment, question-bank, AI, settings, class, resource, analytics, feedback, learning-assistant, and student-preview shell workflows
- **AND** `web-admin` MUST identify the platform operations console for teacher-account management and teacher-preview infrastructure governance
- **AND** `web-student` MUST identify the student H5 frontend.

#### Scenario: Preview governance does not duplicate teacher workflows
- **WHEN** `web-admin` manages hidden preview classes or preview test students
- **THEN** it MUST expose only operational governance actions such as list, inspect, reset, disable, restore, or audit
- **AND** it MUST NOT duplicate teacher catalog, class instruction, question-bank, analytics, feedback, learning-assistant, or student learning workflows.

### Requirement: Console access boundaries are separated
The backend and frontend guards SHALL enforce access boundaries for the three web consoles.

#### Scenario: Configured token opens web-admin
- **WHEN** an operator opens `web-admin` with the configured access token
- **THEN** the console MUST allow access to the platform teacher-account workbench.

#### Scenario: Missing or invalid token opens web-admin
- **WHEN** an operator opens `web-admin` without the configured access token
- **THEN** the console MUST reject access
- **AND** protected `/api/web-admin/*` endpoints MUST return an authorization failure.

#### Scenario: Teacher-console user opens web-teacher
- **WHEN** an active authenticated user with `role='admin'` or legacy `role='teacher'` opens `web-teacher`
- **THEN** the console MUST allow access to all teacher-console workflows.

#### Scenario: Platform or student user opens web-teacher
- **WHEN** an authenticated user with `role='platform_admin'` or `role='student'` opens `web-teacher`
- **THEN** the teacher console MUST reject the session.

### Requirement: Teacher-console role compatibility does not affect feature visibility
The teacher console SHALL treat active `admin` and legacy `teacher` users as full teacher-console users.

#### Scenario: Legacy teacher opens teacher console
- **WHEN** an active legacy `role='teacher'` user is authenticated in `web-teacher`
- **THEN** learning assistant, AI access, settings, experiment catalog, question bank, classes, analytics, resources, media, and feedback navigation MUST be available according to the same route list as `role='admin'`.

#### Scenario: New teacher-console account is created
- **WHEN** a web-admin token request creates a teacher-console account
- **THEN** the backend MUST store it in `app_users` with `role='admin'`
- **AND** it MUST NOT create new `role='teacher'` rows.

### Requirement: Legacy products have explicit product boundaries
The platform SHALL treat `web-student-old` and `web-teacher-old` as separate competition products that share core services but do not replace the current student and teacher products.

#### Scenario: Product ownership is inspected
- **WHEN** a maintainer inspects frontend packages, Compose services, route documentation, or product docs
- **THEN** `web-student-old` MUST identify the legacy student experiment-learning frontend
- **AND** `web-teacher-old` MUST identify the legacy teacher BKT teaching-management frontend
- **AND** neither old product MUST be documented as the canonical replacement for `web-student` or `web-teacher`

#### Scenario: User opens current and old products
- **WHEN** the same backend account and data are used in current and old products
- **THEN** the current products MUST preserve current navigation and capabilities
- **AND** the old products MUST present their legacy navigation and capability subset
- **AND** route availability in one product MUST NOT imply the same route is visible in the other product

### Requirement: Legacy boundary hides platform and diagnostic ownership
The legacy teacher product SHALL avoid platform operations and diagnostic monitoring workflows that belong to current teacher/admin products.

#### Scenario: Legacy teacher navigation is rendered
- **WHEN** an authenticated teacher opens `web-teacher-old`
- **THEN** navigation MUST focus on experiment navigation, videos/resources, AI question generation, teacher review, question bank, assessments, classes, and learning scores
- **AND** navigation MUST NOT include platform-account governance, student-preview infrastructure governance, learning assistant, intelligent monitoring, AI/RAG/ES diagnostics, or provider credential management

