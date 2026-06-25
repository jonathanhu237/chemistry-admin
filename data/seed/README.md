# Production Seed Resources

`data/seed` is a strict current-resource boundary. Files here must be required to restore, import, rebuild, or validate the current application baseline. Historical generation packets, audit drafts, local review reports, retired local BGE embeddings, and old `experiment_id + point_key` seed outputs do not belong here.

Protected current resources:

- `formal_experiments.json`: 77 current formal experiments.
- `knowledge_framework/`: 11 chapters, 133 knowledge units, 385 knowledge points, plus reviewed curriculum source.
- `experiment_catalog/catalog_tree.json`: current catalog tree seed with 569 nodes, 176 directories, 393 point placements, and 357 canonical experiment points.
- `experiment_catalog/point_content_seed.json`: 76 reviewed catalog point-content records, including 71 equation-mode records and 122 structured reaction-equation rows.
- `experiment_catalog/point_textbook_evidence_seed.json`: current catalog-node textbook evidence state and bindings, keyed by catalog node/canonical point identities.
- `question_banks/current_catalog_node_question_bank_seed_v1.json`: current published generated question-bank baseline with 54 banks and 1,965 questions.
- `canonical_rag/chunks/*.jsonl`: canonical textbook chunks used to recreate `source_documents` and `source_chunks`.
- `search/**`: runtime chemistry search dictionaries and ES/IK analyzer assets, including `chemistry_vocabulary.json`.
- `student_learning/element_profiles.json`: curated student-facing family and element learning profiles.
- `manifests/core_resources.json`: count, size, SHA256, and database expectation manifest for the current whitelist.

Forbidden retired seed artifacts:

- `experiment_points/`, `point_evidence/`, and old `question_bank/` directories.
- `canonical_rag/embeddings/**`, BGE dense/sparse vectors, row maps, embedding manifests, and embedding reports.
- `import_reports/`, cleanup plans, generated validation reports, review notes, and audit drafts under `data/seed`.
- Any question/evidence seed keyed only by legacy `experiment_id + point_key` identities.

Current restore order:

```bash
python scripts/apply_migrations.py
python scripts/publish_reviewed_curriculum.py
python scripts/seed_formal_experiments.py --skip-migrations
python scripts/import_canonical_evidence.py --skip-migrations
python scripts/import_experiment_knowledge_framework.py --skip-migrations
python scripts/generate_experiment_catalog_seed.py
python scripts/validate_experiment_catalog_seed.py --write-report
python scripts/import_experiment_catalog_seed.py --skip-migrations
python scripts/seed_catalog_point_evidence.py import
python scripts/seed_current_question_bank.py import --skip-migrations
python scripts/rebuild_video_library_index.py --recreate
```

Validation:

```bash
python scripts/validate_production_resources.py
python scripts/validate_experiment_catalog_seed.py --write-report
python scripts/seed_current_question_bank.py validate
python scripts/validate_experiment_points.py
```

Regenerate `manifests/core_resources.json` only after intentionally changing current seed resources:

```bash
python scripts/validate_production_resources.py --write-manifest
```
