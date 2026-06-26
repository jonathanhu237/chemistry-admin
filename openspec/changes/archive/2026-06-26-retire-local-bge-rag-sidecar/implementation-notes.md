# Implementation Notes

## Inventory classification

- Runtime code: `server/app/bge_service.py`, `server/app/hybrid_rag.py`, `server/app/infrastructure/settings.py`, `server/app/domains/platform/settings.py`, `server/app/api/admin/admin_learning_assistant.py`, `server/app/domains/assistant/agent.py`, `server/app/domains/catalog_tree/ai_context.py`, `server/app/domains/questions/workbench.py`, and catalog evidence job tests referenced local BGE sidecar state or `retrieve_hybrid_context`.
- Compose/deployment config: `docker-compose.yml`, `server/Dockerfile.bge-rag`, `requirements-bge.txt`, `scripts/deploy_compose_stack.py`, and operational docs described the optional `bge-rag` profile, local model mounts, and sidecar health checks.
- Admin/teacher UI: teacher AI monitoring, learning-assistant debug, question-bank runtime display, and catalog AI context labels exposed `BGE`, sidecar status, sidecar metrics, or `hybrid_bge_rag`.
- Test fixtures: backend and frontend fixtures asserted `bge_service_required`, `bge_status`, `bge_metrics`, sidecar URLs, and hybrid BGE labels.
- Documentation/current specs: README, production operations docs, and active specs still mentioned the old local BGE profile and should be updated or superseded by this change.
- Protected resource metadata: canonical chunk/index artifacts and seed manifests that describe historical BGE embedding rows are preserved as corpus metadata, not as a local runtime dependency.
- Historical archive/OpenSpec records: archived changes and old OpenSpec history may continue to mention BGE as historical context.

## Production import and payload boundary

- Production imports of `server.app.hybrid_rag` were found in `server/app/domains/assistant/agent.py` and `server/app/domains/catalog_tree/ai_context.py`.
- API/UI payloads exposing local sidecar fields were found in the admin learning-assistant runtime endpoint, AI platform runtime status, question workbench RAG gate payloads, teacher monitoring mappers, learning-assistant debug UI, and question-bank display types.
- The catalog evidence refresh job already calls the external textbook RAG evidence path (`retrieve_point_textbook_evidence`) and should keep failing/defering through external runtime diagnostics only.

## Characterization baseline

- Existing characterization coverage exists in backend tests for catalog point jobs, catalog point AI context, question workbench RAG gates, and frontend tests for monitoring mappers and learning-assistant streaming fixtures.
- The current behavior before removal is that local BGE sidecar settings can still be read from developer env, Compose can start `bge-rag` through the `rag` profile, and UI payloads can surface sidecar status/metrics.

## Retired environment variable decision

Retired local BGE environment variables (`RAG_HYBRID_BGE_ENABLED`, `RAG_BGE_SERVICE_URL`, `RAG_BGE_TIMEOUT_SECONDS`, and sidecar-only top-k tuning) are no longer read to select runtime behavior. Deployment examples and validation should reject reintroducing supported local sidecar configuration, while an already-present developer `.env` does not resurrect the sidecar because the application settings model ignores those variables.

Rollback is deployment/git rollback plus disabling external textbook RAG feature flags. Rollback must not restore the local `bge-rag` sidecar as a supported service.

## Verification log

- `openspec validate retire-local-bge-rag-sidecar --strict`: passed.
- `docker compose config --quiet`: passed.
- `docker compose config --services`: passed with `elasticsearch`, `postgres`, `backend`, `web-admin`, `web-student`, `web-teacher`, `tusd`, and `video-worker`.
- `python scripts/validate_compose_stack.py --skip-up --skip-index-rebuild`: passed against the running default stack.
- `python -m pytest server/tests/test_textbook_rag_runtime_status.py server/tests/test_question_workbench_rag_gate.py server/tests/test_catalog_point_ai_context.py server/tests/test_catalog_point_jobs.py -q`: passed, 29 tests.
- `npm run typecheck` in `apps/web-teacher`: passed.
- `npm test -- monitoringMappers.test.ts LearningAssistantPage.stream.test.tsx` in `apps/web-teacher`: passed, 2 files / 7 tests.
- `python scripts/validate_backend_architecture.py`: blocked by pre-existing route inventory drift in `server/tests/contracts/backend_route_inventory.json`; no retired local RAG artifact/import violation was reported before the route inventory failure list.
- `python scripts/validate_production_readiness.py --run-compose-smoke --skip-frontend --skip-backend-tests`: Compose smoke, catalog outline seed validation, protected resource manifest, and video-library ES/IK readiness passed; final catalog point identity validation failed on existing data state (`example content` counts and retired question bank/question rows), not on local RAG sidecar checks.
- Final retired-term search: remaining live-code hits are explicit retirement/validation entries; remaining non-code hits are OpenSpec records, archived history, the explicit production-operations retirement note, or protected canonical BGE resource metadata.
