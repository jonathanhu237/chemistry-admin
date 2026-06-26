## Why

The current question-generation workflow can already create and repair point-aware draft questions, but its grounding is tied to legacy/static evidence and the BGE RAG gate rather than the textbook chunks and point descriptions teachers now use to author element-property experiments.

This change imports the experiment/point structure from the curated Markdown catalog, stores the three-part point descriptions, and uses configurable Qwen embedding/rerank plus Elasticsearch textbook evidence to improve the existing teacher question workbench without changing the teacher's authoring flow.

## What Changes

- Import `实验目录_整理版.md` as the authoritative experiment/point hierarchy:
  - `#` headings are chapters.
  - `##` headings are experiments under the chapter.
  - Nested bullet items are folder path segments.
  - Leaf bullet items are experiment points.
- Import `元素性质实验点位描述汇总.md` as point learning content with the existing three sections: experiment principle, phenomenon explanation, and safety note.
- Match existing formal experiments and points where possible; create missing experiments or points only when no safe match exists.
- Index the canonical textbook chunk JSONL files into Elasticsearch with Qwen embeddings and retrievable chunk metadata.
- Use Qwen rerank at query time and separate point evidence retrieval by `principle`, `phenomenon`, and `safety` query sections.
- Preserve the current teacher question-generation interaction:
  - add mode defaults to the current question type/count behavior;
  - repair mode remains anchored to the original question type and lineage;
  - generated questions remain drafts/candidates until teacher publication.
- Add admin-managed configuration for separate LLM, embedding, rerank, and Elasticsearch settings; API keys are stored as configuration secrets and are never hardcoded.
- Use DeepSeek-compatible chat completion for final candidate generation, with textbook evidence and point descriptions supplied as context.
- Treat legacy BGE vectors and pgvector retrieval as non-authoritative for this new teacher question-generation path.

## Capabilities

### New Capabilities

- `textbook-experiment-catalog-import`: Imports the textbook experiment catalog hierarchy and three-part point descriptions into formal experiments, experiment points, and point learning content.
- `qwen-es-textbook-rag-retrieval`: Indexes textbook chunks into Elasticsearch with Qwen embeddings and retrieves per-section evidence using Qwen embedding plus rerank.

### Modified Capabilities

- `ai-access-configuration`: Separates LLM provider configuration from embedding/rerank/RAG configuration, including admin-only secret handling and masked teacher-facing status.
- `point-aware-ai-question-workbench`: Uses the configured textbook RAG health/evidence contract instead of requiring legacy BGE health for teacher question creation and repair.
- `point-aware-question-bank-ai-suggestions`: Generates drafts from per-section textbook evidence while preserving existing objective question validation, draft review, and publication behavior.
- `hybrid-bge-rag-retrieval`: Clarifies that BGE remains a legacy/optional retrieval route and is not the required teacher question-workbench gate after the Qwen/ES textbook RAG route is available.

## Impact

- Backend:
  - import/parsing jobs for the experiment catalog and point description Markdown files;
  - formal experiment and point creation/matching logic;
  - point learning-content upsert behavior;
  - Elasticsearch canonical chunk indexing;
  - Qwen embedding/rerank client and DeepSeek-compatible generation client configuration;
  - question workbench RAG gate and evidence-package construction.
- Admin web:
  - AI access/configuration screens show separate LLM and RAG model status;
  - teacher question workbench shows textbook RAG readiness and per-section evidence diagnostics while keeping existing add/repair controls.
- Data/deployment:
  - new Elasticsearch chunk index for Qwen embeddings;
  - imported experiments/points/content are idempotent and auditable;
  - existing published questions and generated candidates are not republished or deleted by the import.
