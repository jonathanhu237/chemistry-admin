## Why

The repository now has two conflicting RAG boundaries: the newer textbook RAG path uses configured external embedding/rerank APIs, while older specs, Docker Compose, and monitoring surfaces still require or describe a local BGE/RAG sidecar. This change removes that obsolete local service boundary so operators, developers, and tests treat external textbook RAG APIs plus Elasticsearch as the only supported RAG runtime.

## What Changes

- **BREAKING** Remove the local `bge-rag` Docker Compose service, its Dockerfile, requirements file, local model mounts, profile startup docs, and validation expectations.
- **BREAKING** Remove backend runtime code and settings dedicated to the local BGE sidecar, including `RAG_HYBRID_BGE_ENABLED`, `RAG_BGE_SERVICE_URL`, BGE warmup/metrics probes, and hybrid BGE retrieval paths.
- Replace BGE sidecar diagnostics in admin/teacher monitoring with external textbook RAG runtime diagnostics: feature enabled state, Elasticsearch index readiness, embedding API configuration, rerank API configuration, model/index metadata, and request failure reasons.
- Keep Elasticsearch/IK, canonical textbook chunks, canonical embeddings/index data, and external embedding/rerank API configuration as current production resources.
- Preserve question workbench and catalog-node evidence gates as fail-closed when external textbook RAG is not healthy; they must not silently fall back to local templates or obsolete BGE sidecar behavior.
- Update Docker Compose validation, production-readiness validation, documentation, and `.env.example` so no supported command instructs operators to start or validate local RAG services.

## Capabilities

### New Capabilities
- `external-textbook-rag-runtime`: Defines the supported RAG runtime boundary: backend-owned retrieval orchestration, Elasticsearch textbook chunk index, and configured external embedding/rerank APIs.

### Modified Capabilities
- `hybrid-bge-rag-retrieval`: Retire the legacy hybrid BGE sidecar contract and remove local BGE vector/rerank requirements.
- `ai-access-configuration`: Change AI/RAG status wording and behavior from optional BGE service monitoring to external textbook RAG runtime status.
- `learning-assistant-debug-console`: Remove BGE warmup/sidecar metrics from turn/runtime diagnostics and show external RAG diagnostics instead.
- `teacher-intelligent-monitoring-console`: Replace RAG/BGE health cards with external textbook RAG health cards.
- `chemistry-point-retrieval-monitoring`: Replace RAG/BGE monitoring language with external textbook RAG monitoring language.
- `point-aware-ai-question-workbench`: Change RAG-gated workbench access from hybrid BGE health to external textbook RAG health.
- `catalog-point-index-evidence-jobs`: Change evidence refresh requirements from configured RAG/BGE pipelines to the external textbook RAG runtime.
- `catalog-point-ai-context-workbench`: Replace BGE rerank unavailability diagnostics with external textbook RAG stage diagnostics.
- `production-quality-hardening`: Remove BGE FastAPI warmup preservation as a required production-hardening behavior.
- `production-engineering-quality`: Add local BGE sidecar artifacts to retired runtime validation so they are not reintroduced.
- `production-readiness-governance`: Update protected resource and operations expectations to preserve current corpus/index resources while rejecting local RAG service deployment instructions.

## Impact

- Affected Compose and runtime files include `docker-compose.yml`, `.env.example`, `server/Dockerfile.bge-rag`, `requirements-bge.txt`, `server/app/bge_service.py`, `server/app/hybrid_rag.py`, backend settings, admin runtime APIs, validation scripts, and production operations docs.
- Affected product surfaces include AI access/settings, teacher intelligent monitoring, learning-assistant debug diagnostics, question workbench RAG gate status, and catalog point evidence job diagnostics.
- Existing local data services remain in scope: Postgres, Elasticsearch/IK, tusd, video-worker, backend, and the three frontend services.
- External service dependencies become explicit: embedding API base URL/key/model, rerank API base URL/key/model, and Elasticsearch textbook chunk index readiness.
