## MODIFIED Requirements

### Requirement: FastAPI Apps Use Lifespan Startup
The backend FastAPI applications SHALL use lifespan startup/shutdown hooks instead of deprecated `on_event` handlers while preserving existing startup behavior for supported runtime applications.

#### Scenario: Admin service startup behavior is preserved
- **WHEN** the admin service starts
- **THEN** it performs the configured database startup check, ensures the media root exists, registers the same routers/static admin routes, and returns the same `/health` response as before.

#### Scenario: Retired BGE app is absent
- **WHEN** backend FastAPI app modules are inspected after local sidecar retirement
- **THEN** no supported FastAPI app dedicated to local BGE embedding/rerank service MUST remain
- **AND** validation MUST NOT require preserving BGE warmup behavior.

#### Scenario: Deprecation warnings are removed
- **WHEN** backend tests or import smoke checks exercise the FastAPI app modules
- **THEN** FastAPI `on_event` deprecation warnings are not emitted by project startup code.
