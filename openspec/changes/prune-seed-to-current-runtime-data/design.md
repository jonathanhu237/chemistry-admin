## Context

The repository now has three generations of seed thinking in the same `data/seed` tree:

1. Current runtime data used by the application and restore flows: formal experiments, knowledge framework data, catalog tree/content seed, catalog-node textbook evidence seed, canonical textbook chunks, search dictionaries, ES/IK analyzer assets, student learning profiles, and the current published catalog-node question bank.
2. Retired local/BGE RAG data: BGE dense vectors, sparse sidecars, row maps, embedding manifests, embedding QA reports, and `chunk_embeddings` restore requirements that belonged to the old local BGE retrieval boundary.
3. Historical generation and migration artifacts: old video point inventory, old manual point evidence, old 2,310-question rebuilt bank, 30-example and normalized three-element audit drafts, import reports, validation reports, and retired workflow scripts that still default to old seed paths.

The product boundary has moved to catalog-node identities and external textbook RAG APIs. Canonical chunks remain current corpus data; BGE dense/sparse embeddings are no longer current data. The current question bank is not empty: the live baseline has 54 published generated banks and 1,965 published questions keyed by current experiment/catalog-node metadata. Seed import/reset and production validation need to reflect that reality.

## Goals / Non-Goals

**Goals:**

- Define `data/seed` as a strict current runtime/import/rebuild data boundary.
- Preserve canonical textbook chunk JSONL files as current corpus data.
- Remove BGE dense/sparse embedding files and `chunk_embeddings` counts from protected current seed/readiness requirements.
- Export and protect the current 54/1,965 catalog-node question-bank baseline as seed data.
- Delete retired old point inventory, old point evidence, old question-bank seed files, generated audit drafts, import reports, validation reports, and retired default-path scripts instead of moving them into docs.
- Make catalog seed import safe by default so it does not delete current question banks, questions, catalog-node evidence state/bindings, or current media bindings.
- Update validators, manifests, cleanup planning, and docs so they enforce the current whitelist and reject reintroduced retired seed artifacts.

**Non-Goals:**

- Do not remove canonical textbook chunks or `source_chunks`.
- Do not redesign external textbook RAG retrieval APIs or provider configuration.
- Do not introduce a new local embedding/rerank runtime to replace local BGE.
- Do not preserve historical generation/audit materials as operational docs.
- Do not regenerate the question bank content in this change; only export/import/validate the current accepted baseline.
- Do not require a database migration solely to drop the `chunk_embeddings` table; existing schema can remain while current restore/readiness stops requiring populated BGE embeddings.

## Decisions

### Use a seed whitelist instead of a cleanup blacklist

`data/seed` should be validated against a positive list of current resources. The allowed classes are:

- `formal_experiments.json`
- `knowledge_framework/*.json`
- `experiment_catalog/catalog_tree.json`
- `experiment_catalog/point_content_seed.json`
- `experiment_catalog/point_textbook_evidence_seed.json`
- a new current catalog-node question-bank seed artifact
- `canonical_rag/chunks/*.jsonl`
- `search/**`, including `chemistry_vocabulary.json`
- `student_learning/element_profiles.json`
- `manifests/core_resources.json` and any current manifest needed to validate the whitelist

Everything else under `data/seed` must justify itself as current runtime/import/rebuild data. Historical process files fail that test.

Alternative considered: keep a blacklist of known retired directories. Rejected because the repository has accumulated multiple rounds of one-off artifacts; a blacklist lets new audit/report files quietly become "seed".

### Delete non-runtime provenance instead of moving it to docs

Files such as `normalized_three_element_candidates.md`, `normalized_three_element_node_mapping.*`, `three_element_chemistry_review.md`, catalog import reports, and embedding QA reports are useful historical context only for the generation moment. They should not be moved to `docs` because docs are operational guidance for maintainers. Git history and archived OpenSpec changes are sufficient history.

Alternative considered: move audit drafts to `docs/archive`. Rejected because that keeps obsolete sources discoverable as if they were maintainable product documentation.

### Preserve canonical chunks but retire BGE embedding artifacts

Canonical chunks are current corpus data. They are the source imported into `source_chunks` and indexed into Elasticsearch/textbook RAG. BGE dense vectors, sparse vectors, row maps, embedding manifests, embedding QA reports, and `chunk_embeddings` counts are tied to the retired local BGE implementation and must not be required by current restore/readiness.

Alternative considered: keep BGE embeddings as optional offline seed. Rejected because the system boundary is external textbook RAG APIs; keeping optional local embeddings makes validation and operational docs ambiguous.

### Seed the current question bank from live catalog-node data

The retired `rebuilt_question_bank_merged_v1.json` is not the current bank: it has old identity shape and 2,310 questions. The current accepted baseline is 54 published generated banks and 1,965 published questions with current experiment/question metadata, primary catalog-node ids, canonical point ids, and source references. This should be exported to a new seed artifact and imported by a current-only path.

Alternative considered: keep the current bank as database-only state. Rejected because restore/readiness would still be unable to rebuild the product baseline from declared seed resources.

### Make catalog seed import safe by default

The current catalog import reset helper was created for a destructive migration moment. Its default delete list now reaches into current data: question banks, questions, catalog-node evidence state/bindings, current media bindings, catalog jobs, and search state. The new default should validate and upsert current catalog seed data without deleting current runtime data. Any destructive legacy cleanup must be explicit, narrowly named, and guarded by validation.

Alternative considered: keep `--no-reset` as the safe mode. Rejected because the default command is what operators and validation will run under pressure; safe behavior must be the default.

### Retire legacy scripts completely when they only support old identities

Scripts that only know old `experiment_id + point_key` identities should be deleted or made unreachable as production tools. That includes old point-aware question-bank rebuild workflows and manual-reviewed point evidence importers. Current workflows should use catalog-node identities and current seed artifacts.

Alternative considered: keep retired scripts for historical recovery with explicit flags. Rejected by the product boundary: old data is not current and should not remain as a supported path in the product repository.

## Risks / Trade-offs

- [Risk] A hidden runtime path still reads a file that the whitelist removes.
  Mitigation: inventory runtime file reads before deletion, add protected entries for true runtime reads such as `chemistry_vocabulary.json`, and make validation fail on missing current runtime files.

- [Risk] The new question-bank seed export omits metadata that teacher browsing or AI repair depends on.
  Mitigation: validate a round-trip import against counts, point-node references, canonical point references, experiment refs, source refs, objective question payloads, and teacher detail/read-only browsing expectations.

- [Risk] Removing BGE embedding requirements breaks scripts that still import `chunk_embeddings` by default.
  Mitigation: update canonical evidence import/readiness scripts so embeddings are skipped or unsupported by default; scripts that remain must import chunks/source documents without requiring dense/sparse BGE files.

- [Risk] Safe catalog import leaves obsolete catalog rows that a destructive reset previously cleared.
  Mitigation: implement explicit current-scope pruning for seed-owned catalog rows only, and keep destructive legacy cleanup behind a separately named, guarded operation.

- [Risk] Documentation becomes too terse after removing historical notes.
  Mitigation: keep operational docs focused on current restore, validation, and "forbidden retired artifacts"; rely on Git/OpenSpec archives for archaeology.

## Migration Plan

1. Add a current seed whitelist and update `core_resources.json` generation/validation to remove BGE embeddings and include `chemistry_vocabulary.json` plus the current question-bank seed.
2. Add current question-bank export/import/validation using live catalog-node identities and source references.
3. Update catalog seed import/reset so default imports preserve current question banks, questions, catalog evidence, current media bindings, users/roles/courses, source documents/chunks, and search dictionaries.
4. Remove retired seed directories and files from `data/seed`, including old point inventory, old point evidence, old question bank, audit drafts, import reports, validation reports, and BGE embedding/report files.
5. Remove or retire old identity-only scripts and any default paths that point at deleted seed directories.
6. Update production readiness/resource validators and docs to enforce the whitelist and fail on forbidden retired seed paths or BGE embedding requirements.
7. Run strict OpenSpec validation, protected resource validation, catalog seed validation, current question-bank seed round-trip validation, backend architecture validation, and production-readiness validation.

Rollback: restore from version control. Do not reintroduce old local BGE or legacy point/question seed as supported current data. If the current question-bank seed export is found incomplete, block the change before deleting the live database source or publishing the new restore instructions.

## Open Questions

- What filename and schema version should the current question-bank seed use? Proposed default: `data/seed/question_banks/current_catalog_node_question_bank_seed_v1.json`.
- Should `chunk_embeddings` be left as an optional table populated only by explicit developer experiments, or should later migrations remove it once no code references remain?
