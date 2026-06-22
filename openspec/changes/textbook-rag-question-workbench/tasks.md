## 1. Configuration and Runtime Status

- [x] 1.1 Add backend settings models for separate chat LLM, textbook embedding, textbook rerank, and Elasticsearch index configuration.
- [x] 1.2 Extend persisted platform AI configuration to retain existing keys when omitted and store per-role provider metadata.
- [x] 1.3 Expose admin-only full edit behavior and teacher-visible masked status for the new provider roles.
- [x] 1.4 Add a textbook RAG runtime status helper that checks feature enablement, Elasticsearch reachability, index metadata, embedding readiness, and rerank readiness.
- [x] 1.5 Update AI access/admin UI surfaces to display LLM and textbook RAG configuration/status separately from legacy BGE status.

## 2. Catalog and Point Content Import

- [x] 2.1 Implement a parser for `实验目录_整理版.md` that emits chapters, experiments, folder paths, leaf points, source order, and normalized titles.
- [x] 2.2 Implement a parser for `元素性质实验点位描述汇总.md` that emits point titles and the principle, phenomenon, and safety sections.
- [x] 2.3 Implement dry-run matching for experiments by normalized chapter and experiment title with low-confidence/unresolved reporting.
- [x] 2.4 Implement point matching by experiment, normalized leaf title, full folder path, and source order to avoid duplicate-title merges.
- [x] 2.5 Add idempotent creation for missing formal experiments and missing experiment points with import metadata.
- [x] 2.6 Upsert three-part point learning content into the existing point content table with source file, source path, content hash, and import timestamp metadata.
- [x] 2.7 Add import reports for dry-run and apply modes with matched/created/updated/unresolved counts.
- [x] 2.8 Add parser and import tests covering the 55 experiments, 393 leaf points, duplicate leaf titles, and re-import idempotency.

## 3. Textbook Chunk Indexing and Retrieval

- [x] 3.1 Add a Qwen-compatible embedding client with timeout, error, and response-shape validation.
- [x] 3.2 Add a Qwen-compatible rerank client with timeout, score normalization, and response-shape validation.
- [x] 3.3 Add an Elasticsearch canonical textbook chunk index mapping for text, metadata, keyword fields, vector field, model metadata, and content hashes.
- [x] 3.4 Implement a chunk indexer for the canonical JSONL files with batching, idempotent upserts, and index metadata validation.
- [x] 3.5 Implement sectioned retrieval for principle, phenomenon, and safety queries using point title, experiment title, chapter, folder path, and section description.
- [x] 3.6 Add soft boosts for chapter, experiment, content type, and chemical terms without hard-filtering cross-chapter theory evidence.
- [x] 3.7 Build an evidence package grouped by section with chunk ids, text excerpts, source metadata, recall scores, rerank scores, sufficiency, and diagnostics.
- [x] 3.8 Add mocked unit tests for embedding, rerank, ES search, stale-index detection, partial evidence, and all-evidence-missing failure.

## 4. Question Workbench Integration

- [x] 4.1 Replace the teacher question-workbench BGE gate with the configured textbook RAG runtime gate while keeping legacy BGE available for existing consumers.
- [x] 4.2 Load selected point descriptions and folder-path metadata into create-mode workbench context.
- [x] 4.3 Derive repair-mode target points from the original question and attach sectioned textbook evidence to the repair context.
- [x] 4.4 Update the prompt assembly for point-aware suggestions to include point descriptions as retrieval hints and textbook chunks as source evidence.
- [x] 4.5 Route final structured candidate generation through the configured DeepSeek-compatible chat LLM provider.
- [x] 4.6 Preserve existing add-mode type/count controls, repair-mode original type locking, candidate storage, validation, rejection, and teacher publication behavior.
- [x] 4.7 Prevent local-template or malformed LLM output from creating publishable candidates when textbook evidence is missing or invalid.
- [x] 4.8 Persist sectioned evidence diagnostics and missing-section metadata on workbench turns/candidates.
- [x] 4.9 Update the admin workbench UI to show textbook RAG gate status, sectioned evidence groups, missing evidence reasons, and model/index diagnostics.

## 5. Verification and Documentation

- [x] 5.1 Run the catalog import dry-run against the provided Markdown files and verify expected experiment and leaf-point counts.
- [x] 5.2 Run a controlled apply import in a development database and verify re-running it is idempotent.
- [x] 5.3 Index the provided canonical chunk JSONL files into the Qwen/ES index and verify index metadata matches configured model/dimension.
- [x] 5.4 Test sample point retrieval for halogen replacement, thiosulfate reactions, and concentrated sulfuric acid halide reactions with sectioned diagnostics.
- [x] 5.5 Add backend tests for configuration, import, retrieval, gate failure, generation success, partial evidence, and no-evidence refusal.
- [x] 5.6 Run frontend validation for AI access status and the question workbench evidence display.
- [x] 5.7 Run existing backend and admin-web test/build commands affected by the change.
- [x] 5.8 Run OpenSpec status/validation for `textbook-rag-question-workbench` before implementation is considered complete.
