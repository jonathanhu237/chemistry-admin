## Context

The admin question-bank workbench already supports persistent create/repair sessions, objective question validation, draft candidates, and teacher-controlled publication. Its current RAG gate is tied to the legacy hybrid BGE route, while the new textbook assets are already available as curated chunks and separate Markdown point descriptions.

Two teacher-provided Markdown files define different parts of the data model. `实验目录_整理版.md` defines the hierarchy: chapter headings, experiment headings, folder path bullets, and leaf point bullets. `元素性质实验点位描述汇总.md` defines the three teacher-authored point description sections: experiment principle, phenomenon explanation, and safety note. The chunk JSONL files remain the evidence corpus for RAG; they are not imported as point content.

## Goals / Non-Goals

**Goals:**

- Import the textbook experiment hierarchy and point descriptions idempotently.
- Reuse existing formal experiment, experiment point, and point learning-content tables where possible.
- Create missing experiments or points when safe matching cannot find an existing record.
- Build a new Elasticsearch textbook chunk index using Qwen embeddings and Qwen rerank.
- Retrieve evidence separately for principle, phenomenon, and safety descriptions.
- Feed sectioned textbook evidence into the existing create/repair question workbench.
- Preserve current teacher controls, candidate storage, validation, review, and publish semantics.
- Store AI/RAG provider settings through backend configuration, not hardcoded constants.

**Non-Goals:**

- Do not publish generated questions automatically.
- Do not redesign the question-bank page or teacher workflow.
- Do not use BGE vectors as the authoritative path for this feature.
- Do not replace the existing student learning assistant RAG behavior unless a later change requires it.
- Do not treat the three-part Markdown descriptions as source evidence; they are retrieval hints and point content.
- Do not delete existing experiments, points, questions, or candidates during import.

## Decisions

### Use the directory Markdown as hierarchy authority

The import treats `#` as chapter, `##` as experiment, nested bullets as path folders, and leaf bullets as points. The leaf title has display-only markers such as `（点位）` removed before persistence. Folder path segments are stored in point metadata to disambiguate repeated leaf names and to preserve authoring context.

Alternative considered: infer experiments from the three-part point description Markdown alone. That file contains point content, but it is not as explicit about the tree semantics and would make duplicate point names harder to resolve.

### Import point descriptions into the existing learning-content model

The three description sections map to the existing point content fields: principle text, phenomenon explanation, and safety note. The import records source file, chapter, experiment title, folder path, original title, import timestamp, and content hash in metadata so re-imports can update safely.

Alternative considered: store descriptions only in a new RAG prompt table. That would bypass the teacher-facing point content model and create two sources of truth for the same three-part explanation.

### Match first, create only when needed

Experiments are matched by normalized chapter and experiment title. Points are matched within the resolved experiment by normalized leaf title plus full path metadata when available. If there is no safe match, the importer creates the missing experiment or point using server-controlled identifiers and deterministic point keys compatible with the existing `candidate-{n}-{hash}` shape.

Alternative considered: drop and re-import all points. That would risk breaking existing question bindings, source audits, media bindings, and student-facing analytics.

### Build a separate Qwen/ES textbook RAG route

The new route indexes canonical textbook chunks into an Elasticsearch index such as `canonical-rag-chunks-qwen-v1`. Each indexed document stores chunk id, text, metadata, source file, content hash, embedding model, embedding dimension, and indexed timestamp. Query embeddings must use the same configured Qwen embedding model as the index.

Alternative considered: reuse the old BGE/pgvector embeddings. The user explicitly accepted discarding BGE vectors for this path, and mixing embedding models would make similarity scores untrustworthy.

### Retrieve evidence separately for the three point sections

For a selected point, the backend builds three retrieval queries: principle, phenomenon, and safety. Each query includes the point title, experiment title, chapter, folder path, and that section's description. Elasticsearch lexical/vector recall uses soft boosts for same chapter/experiment/content type and chemical terms, but it does not hard-filter to one chapter because useful theory evidence can live in another chapter.

Alternative considered: concatenate all three descriptions into one query. That is simpler, but it loses which evidence supports principle versus phenomenon versus safety and makes insufficiency handling too coarse.

### Fail closed only when evidence cannot support generation

If some sections have usable evidence, the workbench may generate questions that only cover supported sections and records missing section diagnostics. If all selected sections lack usable evidence, generation fails with a teacher-readable reason and no candidate is created. Local template generation must not produce publishable candidates that appear RAG-grounded.

Alternative considered: always fall back to local templates. That keeps demos running but undermines the purpose of textbook-grounded question generation.

### Keep the current question-generation contract

The existing add/repair flow remains the product contract. Add mode uses the current selectable objective question types and count behavior. Repair mode remains anchored to the original question, original type, and lineage. The DeepSeek-compatible LLM receives a server-built prompt containing selected point context, sectioned evidence, teacher instructions, and the existing structured JSON output contract.

Alternative considered: add a new standalone "RAG generate" workflow. That would duplicate the workbench and create a separate review path for the same candidate data.

### Separate LLM, embedding, rerank, and ES configuration

Backend settings distinguish final chat generation from retrieval models. Admins can configure DeepSeek-compatible chat completion separately from Qwen embedding/rerank and Elasticsearch index parameters. Secrets are stored in configuration or environment-backed settings, returned only as configured/masked status, and never embedded in code or OpenSpec artifacts.

Alternative considered: reuse the single `agent_llm_*` configuration for all calls. That cannot represent separate provider roles, models, endpoints, and keys cleanly.

## Risks / Trade-offs

- [Risk] Markdown titles may not match existing experiments exactly. -> Mitigation: normalize punctuation/spacing, report low-confidence matches, and record created records in an import report.
- [Risk] Duplicate leaf point titles can be incorrectly merged. -> Mitigation: match on experiment plus full folder path and preserve source order in metadata.
- [Risk] Qwen embedding dimensions or model names may change. -> Mitigation: store model and dimension in index metadata and rebuild the index when the configured embedding model changes.
- [Risk] Sectioned retrieval can return evidence from adjacent experiments. -> Mitigation: use soft boosts, rerank, source diagnostics, and minimum evidence thresholds rather than hidden hard assumptions.
- [Risk] External APIs can fail or time out. -> Mitigation: fail candidate generation closed, preserve the teacher prompt/session, and show the failing stage.
- [Risk] Keys were shared in conversation during planning. -> Mitigation: implementation stores only configured secrets and should support rotation without code changes.

## Migration Plan

1. Add configuration models/endpoints for chat, embedding, rerank, and textbook RAG runtime status.
2. Add Markdown parsers and dry-run import reports for the directory and three-part point description files.
3. Import or update experiments, points, and point learning content idempotently in a controlled admin/backend operation.
4. Add Qwen embedding/rerank client code and the Elasticsearch textbook chunk indexer.
5. Build the sectioned evidence retriever and diagnostics payload.
6. Replace the question workbench RAG gate with the configured textbook RAG route while leaving legacy BGE code available for existing consumers.
7. Inject evidence packages into current create/repair generation and validation paths.
8. Verify import counts, index health, RAG retrieval, backend tests, and teacher-visible workbench behavior.

Rollback: disable the textbook RAG feature flag, keep imported point content as normal draft content, and revert the workbench gate to the previous route if needed. Existing questions and published bank records are not mutated by this change.

## Open Questions

- The exact Qwen embedding and rerank model identifiers should be set through admin configuration before production indexing.
- The import should produce a dry-run report first; final implementation can decide whether to expose that report only through CLI or also through the admin UI.
