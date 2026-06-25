## 1. Current Seed Inventory And Whitelist

- [x] 1.1 Inventory all runtime reads and import reads under `data/seed`, including backend code, scripts, tests, validators, Docker/Compose mounts, and docs references.
- [x] 1.2 Define the allowed current seed whitelist for formal experiments, knowledge framework, catalog tree/content/evidence seed, current question-bank seed, canonical chunks, search dictionaries, ES/IK assets, student learning profiles, and current manifests.
- [x] 1.3 Define forbidden seed classes for retired point inventory, retired manual point evidence, retired question-bank artifacts, non-runtime audit drafts, generated import/validation reports, and local BGE embedding/report artifacts.
- [x] 1.4 Add validation that fails when forbidden directories or files remain under `data/seed` after cleanup.

## 2. Current Question-Bank Seed

- [x] 2.1 Design the current catalog-node question-bank seed schema and versioned path.
- [x] 2.2 Implement export of the live current baseline with 54 published generated banks and 1,965 published questions.
- [x] 2.3 Preserve objective payloads, experiment refs, bank refs, primary catalog node ids, primary canonical point ids, source refs, status, and generation/review lineage in the export.
- [x] 2.4 Implement import/upsert for the current catalog-node question-bank seed.
- [x] 2.5 Add validation for bank/question counts, objective payloads, valid experiments, valid banks, valid primary catalog nodes, valid canonical point ids, and resolvable source refs.
- [x] 2.6 Add a round-trip smoke path that proves a fresh database can restore the current question-bank baseline from seed.

## 3. Canonical Corpus And BGE Artifact Retirement

- [x] 3.1 Keep canonical chunk JSONL files protected and ensure chunk import can recreate `source_documents` and `source_chunks`.
- [x] 3.2 Remove BGE dense/sparse embedding files, row maps, embedding manifests, embedding reports, failed chunk reports, and input validation reports from current protected seed resources.
- [x] 3.3 Remove `chunk_embeddings` required counts from production resource manifests and production-readiness validation.
- [x] 3.4 Update canonical evidence import tooling so current/default restore does not require BGE embedding files or populated `chunk_embeddings`.
- [x] 3.5 Remove or update docs and validator messages that state canonical embeddings or `chunk_embeddings` are current protected resources.

## 4. Retired Legacy Seed And Script Removal

- [x] 4.1 Delete retired seed directories `data/seed/experiment_points`, `data/seed/point_evidence`, and `data/seed/question_bank`.
- [x] 4.2 Delete or remove from supported workflows scripts that only operate on legacy `experiment_id + point_key` seed data.
- [x] 4.3 Remove retired question-bank import/validation reports and old point/evidence reports from `data/seed/import_reports`.
- [x] 4.4 Delete non-runtime catalog provenance files such as normalized three-element drafts, node mapping reports, chemistry review notes, and canonical grouping audit artifacts from `data/seed`.
- [x] 4.5 Update cleanup planning so it validates current protected resources and then removes forbidden seed artifacts instead of preserving or archiving them.

## 5. Safe Catalog Seed Import And Reset

- [x] 5.1 Refactor catalog seed import so the default command validates and upserts current catalog seed rows without destructive reset.
- [x] 5.2 Remove current question banks, questions, catalog-node evidence state/bindings, current media bindings, users, roles, courses, source documents, source chunks, search dictionaries, and student learning data from default reset targets.
- [x] 5.3 Add an explicit destructive legacy cleanup mode with clear naming, protected-resource validation, and a delete scope limited to retired legacy data.
- [x] 5.4 Add tests or validation checks proving default catalog import preserves current question-bank counts, catalog-node evidence counts, and current media bindings.
- [x] 5.5 Update import reports so generated reports are written outside `data/seed` unless they are explicitly current manifest data.

## 6. Manifest, Validators, And Docs

- [x] 6.1 Regenerate or update `data/seed/manifests/core_resources.json` to include the current whitelist, `chemistry_vocabulary.json`, canonical chunks, and current question-bank seed while excluding BGE embeddings.
- [x] 6.2 Update `scripts/validate_production_resources.py`, `scripts/validate_production_readiness.py`, `scripts/validate_experiment_points.py`, and `scripts/verify_canonical_evidence.py` to match the current seed boundary.
- [x] 6.3 Update architecture/readiness validation to fail if default import/reset code deletes current runtime data or if retired BGE/local legacy seed paths are reintroduced.
- [x] 6.4 Rewrite seed and production operations docs so they describe only the current seed whitelist, restore order, validation commands, and forbidden retired artifacts.
- [x] 6.5 Remove historical generation/audit process notes from operational docs rather than moving deleted seed artifacts into docs.

## 7. Verification

- [x] 7.1 Run `openspec validate prune-seed-to-current-runtime-data --strict`.
- [x] 7.2 Run protected resource validation and confirm the whitelist passes with forbidden artifacts absent.
- [x] 7.3 Run catalog seed validation and current question-bank seed validation.
- [x] 7.4 Run backend architecture validation.
- [x] 7.5 Run production-readiness validation with Compose smoke and without BGE embedding requirements.
- [x] 7.6 Summarize removed artifacts, preserved current seed resources, and any residual optional `chunk_embeddings` table/code references.
