## ADDED Requirements

### Requirement: Local RAG sidecar is not a protected production resource
Production readiness governance SHALL preserve current corpus and index resources while excluding local BGE sidecar runtime artifacts from protected production resources.

#### Scenario: Protected resources are registered
- **WHEN** the production-readiness manifest is generated or checked
- **THEN** canonical chunks, canonical embedding/index artifacts, ES analyzer dictionaries, and current import/validation reports MUST remain protected current resources
- **AND** local BGE model directories, local BGE Dockerfiles, sidecar images, and local RAG profile commands MUST NOT be classified as required production resources.

#### Scenario: Cleanup classification runs
- **WHEN** cleanup classification encounters local BGE model caches or sidecar build artifacts outside protected seed/resource paths
- **THEN** they MUST NOT be treated as current protected application resources
- **AND** cleanup MUST still refuse to delete protected canonical corpus resources.

### Requirement: Production operations exclude local RAG sidecar deployment
Production operations documentation and validation SHALL direct operators to configure external textbook RAG APIs rather than deploy a local RAG service.

#### Scenario: Maintainer reads deployment instructions
- **WHEN** a maintainer reads Docker Compose or production operations documentation
- **THEN** the docs MUST describe external embedding/rerank provider configuration and textbook Elasticsearch index readiness
- **AND** they MUST NOT include supported commands to start `bge-rag`, use a `rag` Compose profile, or mount local BGE model paths.

#### Scenario: Compose smoke runs
- **WHEN** production-like Compose smoke validation runs
- **THEN** it MUST verify the remaining default application services
- **AND** it MUST NOT require a local RAG sidecar to be running before the stack is considered healthy.
