## ADDED Requirements

### Requirement: Frontend feature modules are decomposed incrementally
The admin frontend SHALL reduce large feature-page modules through behavior-preserving extraction of pure helpers, local components, or local hooks.

#### Scenario: A large feature slice is extracted
- **WHEN** a feature-page slice is moved into a new module
- **THEN** existing route paths, API calls, query keys, mutation behavior, and visible workflows MUST remain compatible

### Requirement: App shell avoids feature-heavy eager imports
The admin app shell SHALL keep feature-only dependencies behind lazy route boundaries.

#### Scenario: Heavy feature dependencies remain route-owned
- **WHEN** the production build is run
- **THEN** charts, markdown/math rendering, upload/tus utilities, and assistant/video/question-bank feature code MUST NOT be newly imported eagerly by the top-level app shell

### Requirement: Build warnings remain owned and actionable
Large production chunks SHALL be named, associated with an owner, and documented as intentional or targeted for later splitting.

#### Scenario: A vendor chunk exceeds the warning threshold
- **WHEN** Vite reports a chunk larger than the warning threshold
- **THEN** the build report MUST identify the chunk owner, and the pass MUST document whether it is accepted or a follow-up target

### Requirement: CI trigger posture remains unchanged
The production readiness workflow SHALL remain manually triggered during this pass.

#### Scenario: Fourth-pass changes are pushed
- **WHEN** commits are pushed to `codex/productionize-admin-platform`
- **THEN** no workflow change in this pass MUST cause production readiness to run solely because of that push
