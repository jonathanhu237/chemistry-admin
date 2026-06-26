## Why

The repository's seed boundary still mixes current runtime data with retired local BGE embedding artifacts, legacy `experiment_id + point_key` point evidence/question-bank files, generated review reports, and audit drafts. This makes validation and restore flows ambiguous after the system has moved to catalog-node identities, external textbook RAG APIs, and a current published question bank.

## What Changes

- **BREAKING** Redefine `data/seed` as current runtime/import/rebuild data only; generated audit drafts, historical reports, retired workflow outputs, and non-runtime provenance files must be deleted rather than moved into docs.
- **BREAKING** Remove all local BGE dense/sparse embedding seed protection and current-readiness expectations, including `data/seed/canonical_rag/embeddings/canonical_base_v1/**` and required `chunk_embeddings` counts.
- Preserve canonical textbook chunk JSONL files as current data because they are the canonical corpus imported into `source_chunks` and indexed/retrieved through the supported external textbook RAG boundary.
- Replace the retired old question-bank seed with a current catalog-node question-bank seed exported from the live 54 published banks / 1,965 published questions baseline.
- Remove old local point/evidence/question generation chains and their default paths, including retired point inventory, old manual point evidence, old point-aware question-bank files, and scripts that only operate on legacy point identities.
- Change catalog seed import/reset behavior so safe defaults never delete current question banks, questions, catalog-node evidence state/bindings, current media bindings, or other live catalog-node runtime data.
- Promote `data/seed/search/chemistry_vocabulary.json` into the protected current seed boundary because runtime search code reads it.
- Update validation, cleanup classification, manifests, and operational docs so they enforce the current seed whitelist and fail on reintroduced retired seed directories or BGE embedding requirements.

## Capabilities

### New Capabilities
- `current-runtime-seed-boundary`: Defines the authoritative current seed whitelist, forbidden retired artifact classes, safe import/reset behavior, and current seed restore expectations.

### Modified Capabilities
- `production-readiness-governance`: Replace protected-resource expectations so current seed validation preserves canonical chunks and current question-bank data, rejects BGE embedding seed protection, rejects non-runtime audit/report files in `data/seed`, and validates the new seed whitelist.
- `experiment-question-bank-management`: Change the default baseline from "empty after catalog reset" to the current catalog-node question-bank seed with 54 published banks and 1,965 published questions.
- `experiment-catalog-tree`: Change catalog seed reset semantics so default imports are safe upserts/prunes for catalog seed data and no longer delete current catalog-node question banks, evidence state/bindings, or media bindings.
- `hybrid-bge-rag-retrieval`: Remove remaining requirements that treat `chunk_embeddings`, BGE dense vectors, sparse vectors, row maps, local rerank outputs, or local BGE evidence generation as current production seed/corpus resources.

## Impact

- Affected seed data: `data/seed/**`, especially `canonical_rag`, `experiment_catalog`, `experiment_points`, `point_evidence`, `question_bank`, `import_reports`, `manifests`, `search`, and `student_learning`.
- Affected scripts: protected resource validation, production readiness validation, canonical evidence import, catalog seed import, catalog evidence seed import/export, cleanup planning, legacy question-bank/evidence scripts, and any seed README/docs generators.
- Affected database expectations: current `source_documents` / `source_chunks` remain protected; `chunk_embeddings` is no longer a required current data count; current `experiment_question_banks` / `experiment_questions` become protected seed/restorable data; catalog-node evidence tables and current media bindings are no longer default reset targets.
- Affected docs: production operations and seed docs must describe only the current seed boundary and must not preserve historical generation notes or retired local RAG/legacy point-evidence instructions as operational guidance.
