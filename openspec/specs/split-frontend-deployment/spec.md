# split-frontend-deployment Specification

## Purpose
TBD - created by archiving change split-frontend-deployment-admin-shell. Update Purpose after archive.
## Requirements
### Requirement: Frontend applications are independently deployed services
The system SHALL deploy the student H5 frontend, teacher console, and platform operations console as independent frontend services rather than serving their SPA bundles from the backend service.

#### Scenario: Compose starts the full application
- **WHEN** the default production-like Compose application is started
- **THEN** `web-student` MUST be a running service with its own published port
- **AND** `web-teacher` MUST be a running service with its own published port
- **AND** `web-admin` MUST be a running service with its own published port
- **AND** `backend` MUST remain a separate service with its own published API port.

#### Scenario: Frontend service serves deep SPA routes
- **WHEN** a browser requests a deep student, teacher, or platform SPA route from the corresponding frontend service
- **THEN** that frontend service MUST return the correct SPA `index.html`
- **AND** the backend service MUST NOT be responsible for that SPA fallback.

### Requirement: Backend service is API-only
The backend runtime SHALL stop serving built frontend assets or frontend SPA fallback routes.

#### Scenario: Backend image is built
- **WHEN** the backend Docker image is built
- **THEN** it MUST NOT copy `apps/web-admin/dist`
- **AND** it MUST NOT copy `apps/web-teacher/dist`
- **AND** it MUST NOT copy `apps/web-student/dist`.

#### Scenario: Backend route table is inspected
- **WHEN** the canonical backend route inventory is validated
- **THEN** backend-hosted admin SPA routes MUST be absent
- **AND** backend-hosted student SPA fallback routes MUST be absent
- **AND** backend API and health routes MUST remain available.

### Requirement: Frontend services proxy API traffic to backend
Each frontend service SHALL make backend API calls available through the frontend origin.

#### Scenario: Student frontend calls API
- **WHEN** the student frontend issues a request to `/api/*`
- **THEN** the student frontend runtime MUST forward the request to the backend service
- **AND** the browser-facing API contract MUST remain `/api/*`.

#### Scenario: Teacher frontend calls API
- **WHEN** the teacher frontend issues a request to `/api/*`
- **THEN** the teacher frontend runtime MUST forward the request to the backend service
- **AND** the browser-facing API contract MUST remain `/api/*`.

#### Scenario: Platform operations frontend calls API
- **WHEN** the platform operations frontend issues a request to `/api/*`
- **THEN** the platform operations frontend runtime MUST forward the request to the backend service
- **AND** the browser-facing API contract MUST remain `/api/*`.

### Requirement: Compose validation includes frontend services
The Compose smoke validation SHALL treat the student, teacher, and platform frontend services as required application services.

#### Scenario: Compose smoke runs
- **WHEN** Compose smoke validation runs for the full application
- **THEN** it MUST verify `backend`, `web-student`, `web-teacher`, `web-admin`, `postgres`, `elasticsearch`, `tusd`, and `video-worker` are running
- **AND** it MUST verify backend health, frontend reachability, PostgreSQL readiness, Elasticsearch/IK readiness, migrations, and video-library search readiness.

### Requirement: Legacy frontend services are independently deployed
The deployment topology SHALL support optional old student and old teacher frontend services alongside the current student, teacher, and admin frontend services.

#### Scenario: Full legacy-enabled Compose topology starts
- **WHEN** the legacy-enabled production-like Compose application is started
- **THEN** `web-student-old` MUST be a running frontend service
- **AND** `web-teacher-old` MUST be a running frontend service
- **AND** `web-student-old` MUST publish browser port `15176` by default
- **AND** `web-teacher-old` MUST publish browser port `15177` by default
- **AND** both old frontend services MUST proxy browser-facing `/api/*` requests to the shared backend service
- **AND** `backend`, `postgres`, `elasticsearch`, `tusd`, and `video-worker` MUST remain shared services rather than old-specific duplicates

#### Scenario: Legacy frontend services serve deep routes
- **WHEN** a browser requests a deep old student or old teacher SPA route
- **THEN** the corresponding old frontend service MUST return its own old SPA `index.html`
- **AND** the backend service MUST NOT become responsible for old SPA fallback routing

#### Scenario: Current-only development topology starts
- **WHEN** a maintainer starts only the current frontend services
- **THEN** `web-student`, `web-teacher`, and `web-admin` MUST remain usable without requiring old frontend services to be running
- **AND** old frontend service definitions MUST NOT change current frontend ports or API proxy contracts

### Requirement: Legacy frontend service names and ports are stable
The system SHALL assign stable service names and browser ports to the old frontend products.

#### Scenario: Service topology is inspected
- **WHEN** the local or production-like service topology is inspected
- **THEN** the old student frontend service MUST be named `web-student-old`
- **AND** `web-student-old` MUST expose default browser port `15176`
- **AND** the old teacher frontend service MUST be named `web-teacher-old`
- **AND** `web-teacher-old` MUST expose default browser port `15177`
- **AND** the old service ports MUST not collide with `web-student`, `web-teacher`, or `web-admin`
