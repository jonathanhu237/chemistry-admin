## ADDED Requirements

### Requirement: Local BGE sidecar artifacts stay removed
The backend and Compose runtime SHALL keep retired local BGE sidecar artifacts out of supported production and local-production paths.

#### Scenario: Compose stack is inspected
- **WHEN** `docker-compose.yml` or Compose validation output is inspected
- **THEN** no `bge-rag` service or `rag` profile MUST be required or documented as part of the application stack
- **AND** validation MUST fail if the required default service list includes a local RAG sidecar.

#### Scenario: Backend runtime is inspected
- **WHEN** backend architecture validation searches runtime modules
- **THEN** `server/app/bge_service.py`, `server/app/hybrid_rag.py`, and sidecar-only settings MUST be absent or unreachable from production runtime
- **AND** validation MUST fail if those files are reintroduced as compatibility or local-demo modules.

#### Scenario: Environment example is inspected
- **WHEN** `.env.example` is inspected
- **THEN** it MUST document external textbook RAG provider settings
- **AND** it MUST NOT instruct maintainers to enable `RAG_HYBRID_BGE_ENABLED`, configure `RAG_BGE_SERVICE_URL`, mount local BGE models, or start `docker compose --profile rag`.
