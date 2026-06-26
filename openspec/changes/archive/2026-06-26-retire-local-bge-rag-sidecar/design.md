## Context

The current repository carries two RAG generations at once. The older generation is `hybrid-bge-rag-retrieval`: a local CPU BGE sidecar (`bge-rag`) provides embedding and rerank HTTP endpoints, the backend calls it through `RAG_BGE_SERVICE_URL`, and monitoring pages expose BGE warmup, model load, memory, and sidecar reachability. The newer generation introduced by `textbook-rag-question-workbench` stores provider roles for chat, embedding, and rerank separately, indexes canonical textbook chunks into Elasticsearch, and calls configured Qwen/OpenAI-compatible embedding and rerank APIs through `server/app/domains/textbook_rag/clients.py`.

The product boundary has moved to external textbook RAG APIs. Keeping the local BGE service in Compose and specs creates operational ambiguity: developers can start a sidecar that is no longer the authoritative path, admins can see stale BGE health instead of the real external RAG gate, and validation/docs can ask operators to maintain model files under `E:/models/BAAI`.

## Goals / Non-Goals

**Goals:**

- Make the external textbook RAG runtime the only supported RAG boundary.
- Remove local BGE sidecar service definitions, images, Dockerfiles, requirements, model mounts, profile commands, runtime settings, probes, and documentation.
- Replace BGE sidecar status with external textbook RAG status everywhere operators or teachers inspect AI/RAG health.
- Preserve fail-closed question generation and evidence refresh gates when external textbook RAG is not healthy.
- Preserve current production resources: canonical chunks, canonical embeddings/index seed artifacts, Elasticsearch/IK analyzer assets, protected manifests, and current import/index validation reports.
- Keep the default Compose stack focused on application/data services: Postgres, Elasticsearch, backend, web frontends, tusd, and video-worker.

**Non-Goals:**

- Do not remove Elasticsearch or IK analyzer support.
- Do not remove the textbook RAG retrieval/indexing implementation that uses external embedding/rerank APIs.
- Do not redesign teacher question-bank workflows, student assistant UI, or provider credential management beyond removing BGE sidecar concepts.
- Do not introduce another local model-serving replacement for BGE.
- Do not delete protected canonical corpus resources merely because the old sidecar is removed.

## Decisions

### Remove local BGE rather than hiding it behind a disabled profile

The `bge-rag` Compose profile, `server/Dockerfile.bge-rag`, `requirements-bge.txt`, and `server/app/bge_service.py` should be removed. Keeping a disabled profile would preserve the confusing runtime option and leave future changes free to depend on it again.

Alternative considered: leave `bge-rag` as an unsupported dev-only profile. Rejected because the product boundary is no local RAG service; dev-only runtime options still influence docs, status pages, and future tests.

### Treat `hybrid_rag.py` as retired runtime code

`server/app/hybrid_rag.py` implements query generation, BGE vector recall through `chunk_embeddings`, BGE rerank, and fallback traces for the legacy assistant path. This code should be removed or replaced at call sites with the supported textbook RAG runtime, depending on the caller. Any remaining assistant or catalog-point call sites must either use fixed reviewed evidence, platform resource lookup, or the external textbook RAG path.

Alternative considered: keep the hybrid retrieval helper as a fallback. Rejected because fallback to the old BGE/pgvector corpus would make external textbook RAG health non-authoritative and could generate answers from a retired evidence path.

### Collapse BGE settings into textbook RAG settings

Environment and persisted settings must stop exposing `RAG_HYBRID_BGE_ENABLED`, `RAG_BGE_SERVICE_URL`, BGE timeout, vector top-k, and BGE warmup/metrics concepts as supported runtime configuration. Supported RAG settings are:

- textbook RAG enabled flag
- Elasticsearch URL/index/timeout
- embedding provider base URL, API key, model, dimension
- rerank provider base URL, API key, model
- rerank top-k and minimum score
- retrieval timeout and diagnostics

Query generation can remain a separate assistant behavior only if it does not imply BGE or local vector recall.

Alternative considered: keep old settings but mark deprecated. Rejected because Compose and `.env.example` currently make those variables look required, and settings deprecation would not remove operational ambiguity.

### Monitoring reports external RAG readiness, not sidecar internals

Admin and teacher monitoring surfaces should show whether external textbook RAG is disabled, misconfigured, missing its ES index, stale against model metadata, unreachable, or healthy. They should not show BGE model paths, warmup state, sidecar memory, sidecar process uptime, or `bge-rag` service URL.

Alternative considered: show both legacy BGE and textbook RAG status. Rejected because the old status would be noise after sidecar removal and could be mistaken for a required health gate.

### Question generation fails closed on external RAG health

The point-aware question workbench already moved to a textbook RAG runtime gate. This gate should become the sole requirement for evidence-backed AI generation. If external embedding/rerank APIs, ES index metadata, or evidence sufficiency fail, candidate generation must be rejected while preserving session state and existing candidates.

Alternative considered: fall back to local templates or legacy keyword/BGE evidence when external RAG fails. Rejected because generated candidates would appear evidence-backed without authoritative textbook evidence.

### Evidence jobs use external RAG or remain unavailable

Catalog-node evidence refresh jobs should use external textbook RAG retrieval. When external RAG is disabled or unhealthy, jobs fail/defer with diagnostics and point content remains editable. They must not call local BGE, local model mounts, or retired `chunk_embeddings` vector recall.

Alternative considered: keep BGE only for offline evidence refresh jobs. Rejected because that would require preserving sidecar code, model files, and a second evidence scoring model.

### Validation prevents reintroduction

Architecture and production-readiness validation should reject local BGE sidecar artifacts as retired runtime surfaces. Compose smoke should not require a `rag` profile. Documentation checks should not tell operators to run `docker compose --profile rag up ... bge-rag`.

Alternative considered: rely on code review to prevent reintroduction. Rejected because old commands and files already exist and should be mechanically detectable.

## Risks / Trade-offs

- [Risk] Existing assistant paths still import `retrieve_hybrid_context`.
  Mitigation: implementation must inventory imports and either move those callers to external textbook RAG, fixed reviewed evidence, or explicit no-RAG behavior before deleting the helper.

- [Risk] Some monitoring UI tests assert BGE warmup or sidecar metrics.
  Mitigation: update tests to assert external textbook RAG status states and absence of BGE sidecar terms.

- [Risk] Operators may still have local scripts or habits that start `--profile rag`.
  Mitigation: update README and production operations docs with explicit retirement notes and replacement external API configuration steps.

- [Risk] Removing old settings may break environments that still set them.
  Mitigation: supported code should ignore retired variables or fail with a clear unsupported-setting diagnostic during validation, rather than silently using them.

- [Risk] Student learning assistant behavior may still depend on legacy hybrid retrieval.
  Mitigation: characterize assistant routes before deletion and document whether each route uses fixed reviewed evidence, platform resource lookup, or external textbook RAG after the change.

- [Risk] Protected resources may be over-deleted.
  Mitigation: keep canonical chunks, canonical embeddings/index artifacts, ES analyzer dictionaries, and manifest-listed resources protected; only remove local service/runtime artifacts.

## Migration Plan

1. Inventory every reference to `bge-rag`, `BGE`, `RAG_HYBRID_BGE_ENABLED`, `RAG_BGE_SERVICE_URL`, `hybrid_rag`, `bge_service`, `requirements-bge`, `Dockerfile.bge-rag`, and `--profile rag`.
2. Remove Compose service/profile and image build artifacts for local BGE.
3. Remove backend sidecar app and legacy hybrid retrieval code after call sites are migrated.
4. Remove retired BGE settings from `.env.example`, settings models, admin responses, runtime status payloads, and docs.
5. Update monitoring/debug/workbench surfaces to use external textbook RAG status payloads.
6. Update validation scripts so required Compose services exclude local RAG, OpenSpec validation reflects the new specs, and architecture checks reject retired sidecar artifacts.
7. Run targeted backend tests, frontend tests for affected monitoring/workbench UI, `docker compose config --quiet`, and Compose smoke for the remaining default services.
8. Run OpenSpec validation for this change.

Rollback: use git/deployment rollback. Do not restore `bge-rag` as a compatibility service. If external textbook RAG is unhealthy after rollout, disable the textbook RAG feature flag and keep evidence-backed generation unavailable until external configuration is fixed.

## Open Questions

- Should retired `RAG_*` environment variables be ignored with warnings or rejected by validation when present?
- Which student learning assistant routes should use external textbook RAG after legacy hybrid retrieval is removed, and which should rely only on reviewed point evidence or platform resource lookup?
- Should old local BGE model files under host paths such as `E:/models/BAAI` be documented as out-of-repo cleanup, or left entirely outside repository scope?
