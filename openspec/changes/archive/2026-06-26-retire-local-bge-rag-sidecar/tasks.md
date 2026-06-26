## 1. Inventory And Baseline

- [x] 1.1 Search the repository for `bge-rag`, `BGE`, `RAG_HYBRID_BGE_ENABLED`, `RAG_BGE_SERVICE_URL`, `RAG_BGE_TIMEOUT_SECONDS`, `hybrid_rag`, `bge_service`, `requirements-bge`, `Dockerfile.bge-rag`, and `--profile rag`.
- [x] 1.2 Classify each hit as runtime code, Compose/deployment config, admin/teacher UI, test fixture, OpenSpec artifact, documentation, protected resource metadata, or historical archive.
- [x] 1.3 Identify every production runtime import of `server.app.hybrid_rag` and every API/UI payload that exposes local BGE sidecar fields.
- [x] 1.4 Capture current behavior for affected assistant, monitoring, question-workbench, and catalog evidence routes with focused tests or existing characterization tests before removal.
- [x] 1.5 Decide whether retired `RAG_*` environment variables should be ignored with warnings or rejected by validation, and record the decision in implementation notes.

## 2. Remove Local BGE Compose And Build Artifacts

- [x] 2.1 Remove the `bge-rag` service, `rag` profile, local BGE image tag, model volume mount, and BGE health check from `docker-compose.yml`.
- [x] 2.2 Remove `server/Dockerfile.bge-rag`.
- [x] 2.3 Remove `requirements-bge.txt`.
- [x] 2.4 Remove unused `bge_models` or equivalent named volumes if they only supported the retired sidecar.
- [x] 2.5 Update `scripts/deploy_compose_stack.py` to remove `--with-rag`, profile handling, and `bge-rag` service startup.
- [x] 2.6 Update `scripts/validate_compose_stack.py` and related smoke checks so required services exclude local RAG sidecar expectations.
- [x] 2.7 Run `docker compose config --quiet` and verify `docker compose config --services` lists only supported application services.

## 3. Remove Backend Local BGE Runtime

- [x] 3.1 Remove `server/app/bge_service.py` and all tests or references dedicated solely to its `/health`, `/metrics`, `/embed`, `/rerank`, or warmup behavior.
- [x] 3.2 Remove `server/app/hybrid_rag.py` after migrating every production caller.
- [x] 3.3 Remove local BGE settings from `server/app/infrastructure/settings.py`, including hybrid enablement, BGE service URL, BGE timeout, vector top-k, and sidecar-specific rerank settings.
- [x] 3.4 Remove local BGE fields from persisted/effective platform settings responses where they are no longer part of the supported admin contract.
- [x] 3.5 Replace runtime status helpers that report `bge_service_required`, sidecar URL, sidecar metrics, or warmup status with external textbook RAG status fields.
- [x] 3.6 Ensure retired local BGE settings are not read to select runtime behavior even if present in a developer `.env`.
- [x] 3.7 Update backend architecture validation to fail if retired sidecar modules or runtime imports are reintroduced.

## 4. Migrate RAG Consumers To External Textbook Runtime

- [x] 4.1 Update learning-assistant and point-context callers that previously used `retrieve_hybrid_context` to use fixed reviewed evidence, platform resource lookup, or the external textbook RAG runtime according to route policy.
- [x] 4.2 Preserve retrieval-decision diagnostics for assistant turns while removing local BGE trace modes and sidecar timing fields.
- [x] 4.3 Confirm question workbench create/repair gates use `_textbook_rag_runtime_status` or equivalent external runtime health only.
- [x] 4.4 Confirm workbench generation fails closed when Elasticsearch index, embedding API, rerank API, model metadata, or evidence sufficiency is unhealthy.
- [x] 4.5 Update catalog-node evidence refresh jobs to call only the external textbook RAG runtime or fail/defer with external-stage diagnostics.
- [x] 4.6 Remove any fallback that creates publishable candidates through local templates after external textbook RAG failure.
- [x] 4.7 Update duplicate-risk, cache, evidence-package, and retrieval helpers to keep using external provider-role configuration without referencing sidecar settings.

## 5. Update Monitoring, Debug, And Teacher UI Contracts

- [x] 5.1 Update admin learning-assistant runtime endpoint payloads to remove BGE sidecar status, metrics, warmup, local model paths, sidecar memory, and sidecar uptime.
- [x] 5.2 Add or expose external textbook RAG status fields for disabled, missing provider config, Elasticsearch unavailable, index missing, index stale, embedding unavailable, rerank unavailable, and healthy states.
- [x] 5.3 Update teacher intelligent monitoring RAG module to render external textbook RAG health and remove local BGE-specific labels.
- [x] 5.4 Update AI access/settings monitoring surfaces to separate chat LLM, embedding provider, rerank provider, and Elasticsearch status.
- [x] 5.5 Update learning-assistant debug console diagnostics to show external RAG stages and remove BGE warmup/sidecar runtime sections.
- [x] 5.6 Update catalog point AI context workbench probes to report external textbook RAG stage failures instead of BGE vector/rerank failures.
- [x] 5.7 Update frontend tests, mappers, fixtures, and snapshots that mention `BGE`, `bge-rag`, sidecar metrics, or warmup state.

## 6. Update Environment, Documentation, And Operations

- [x] 6.1 Update `.env.example` to remove local BGE variables and document external textbook RAG provider variables.
- [x] 6.2 Align current `.env` guidance and docs so supported Compose ports and service lists do not mention `bge-rag` or `--profile rag`.
- [x] 6.3 Update README deployment instructions to remove local RAG profile startup and describe external textbook RAG setup.
- [x] 6.4 Update `docs/production-operations.md` to remove local BGE model mount instructions, BGE archive/profile commands, and sidecar health expectations.
- [x] 6.5 Update any local development docs that previously described `E:/models/BAAI`, BGE warmup, or local RAG sidecar remediation.
- [x] 6.6 Preserve documentation that canonical chunks, canonical embeddings/index artifacts, and ES analyzer dictionaries remain protected current resources.

## 7. Update Validation And Tests

- [x] 7.1 Update backend tests that assert hybrid BGE settings, sidecar runtime status, BGE metrics, or BGE warmup behavior.
- [x] 7.2 Add backend tests for external textbook RAG status states: disabled, missing ES URL, missing embedding config, missing rerank config, index missing, index stale, and healthy.
- [x] 7.3 Add tests proving question workbench generation fails closed when external textbook RAG is unhealthy.
- [x] 7.4 Add tests proving catalog evidence jobs fail/defer with external-stage diagnostics when external textbook RAG is unhealthy.
- [x] 7.5 Add validation coverage that retired sidecar artifacts are absent from Compose, runtime imports, and environment examples.
- [x] 7.6 Update production-readiness validation so Compose smoke verifies only the supported default services and external RAG readiness checks do not require a local sidecar.
- [x] 7.7 Run relevant backend test subsets for settings, textbook RAG clients/retrieval, question workbench, catalog evidence jobs, assistant diagnostics, and architecture validation.
- [x] 7.8 Run relevant frontend checks for teacher monitoring, AI access/settings, learning-assistant debug, and workbench RAG gate displays.

## 8. Final Verification

- [x] 8.1 Run `openspec validate retire-local-bge-rag-sidecar --strict`.
- [x] 8.2 Run `docker compose config --quiet`.
- [x] 8.3 Run `python scripts/validate_compose_stack.py --skip-up --skip-index-rebuild` against an already-running supported stack, or record why Compose runtime validation is unavailable.
- [x] 8.4 Run `python scripts/validate_production_readiness.py --run-compose-smoke --skip-frontend --skip-backend-tests` when the supported Compose stack and external RAG configuration are available, or record blockers.
- [x] 8.5 Search the repository again for retired local RAG terms and verify remaining hits are only historical archives, OpenSpec records, or explicit retirement notes.
- [x] 8.6 Document rollback as git/deployment rollback and disabling textbook RAG feature flags, not restoring `bge-rag`.
