## ADDED Requirements

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
