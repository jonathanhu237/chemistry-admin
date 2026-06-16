## Context

The learning assistant is now used as a multi-turn chat simulation for the student learning page. Students are expected to arrive from a chapter page and often select a video-point prompt. Today that point context is mostly encoded in natural language, while the backend request only receives chapter/experiment fields and the optional RAG flag.

The current policy gate runs before answer generation and does not receive conversation history or a resolved follow-up question. It can therefore misclassify short follow-ups such as "why" and normal point explanation prompts as out-of-scope or resource availability requests.

The current platform-resource rail is intended to prevent fabricated claims about published videos or files. Its keyword boundary is too broad: ordinary point explanations that mention videos/materials can be routed to `published_resource_lookup`, producing "no published resources" instead of answering the learning question.

## Goals / Non-Goals

**Goals:**
- Treat chapter/experiment/video-point context as the base learning context, independent from optional RAG lookup.
- Add structured `point_key` support to learning assistant requests and debug prompt suggestions.
- Build a fixed point evidence package when point context is present.
- Make guardrail decisions context-aware by using recent conversation context or a resolved question before policy classification.
- Restrict platform resource availability handling to actual published-resource inventory questions.
- Keep RAG as supplemental recall/rerank for broader theory and figures.

**Non-Goals:**
- Do not require the model to understand video pixels or decode video content.
- Do not replace the hybrid BGE RAG service.
- Do not alter teacher-facing question-generation guardrails.
- Do not guarantee every point has perfect textbook evidence; missing evidence should be visible and handled gracefully.

## Decisions

### Temporary spike: generate video-point default evidence artifacts

Before relying on question-bank metadata as the point evidence source, run a temporary offline spike to generate default evidence chunks for all formal experiment video points. This is not a production feature in this change and does not modify the question bank.

The spike reads the existing Postgres data only:
- `formal_experiments.metadata.video_candidates` for the 300 video points and stable `point_key` reconstruction;
- `experiment_chapter_bindings` and `experiment_framework_formal_links` for experiment/chapter scope;
- `source_chunks` and `chunk_embeddings` for experiment and theory chunk recall;
- the existing BGE-M3 pgvector embeddings for vector recall.

It may start a temporary GPU BGE service on a separate port/profile using the existing local models, with rerank settings tuned for quality rather than online latency, for example `BGE_DEVICE=cuda`, `BGE_USE_FP16=true`, and `BGE_RERANK_MAX_LENGTH=1024`.

The output is an artifact, not a canonical database rewrite:
- raw candidates with vector scores, rerank scores, chunk metadata, and original chunk text;
- per-point default experiment chunk ids;
- per-point default theory chunk ids;
- a summary report for spot checks and threshold tuning.

If this artifact proves reliable, a later implementation can make the learning assistant prefer these default evidence chunks before falling back to question-bank metadata. That later read path should still be explicit and read-only.

### Structured point context is the stable contract

Learning assistant requests will accept an optional `point_key`. The frontend prompt card will send `chapter_id`, `experiment_id`, `point_key`, and the student-facing question. The text can stay natural, but backend behavior must not rely on parsing the point title from that text.

Alternative considered: keep embedding the point in the prompt only. This is fragile for guardrails, diagnostics, and fixed evidence assembly.

### Point evidence package precedes RAG

The agent will assemble a point evidence package before optional RAG lookup. Sources can include:
- selected chapter and experiment metadata;
- selected experiment video point metadata;
- question-bank records whose `metadata.primary_point_keys` include the selected point;
- `metadata.source_audit.canonical_chunk_ids` and `supporting_theory_chunk_ids` from those records;
- available source previews/assets for those chunk ids when the repository can resolve them.

This package is passed to the model regardless of `allow_rag_lookup`. Hybrid RAG may still add broader theory/figure evidence when enabled.

Alternative considered: put all point lookup through BGE. This makes point explanations fail when RAG is off or slow, and it ignores deterministic evidence already present in the question bank.

### Policy classification uses resolved context

Before model policy classification, the backend will create a lightweight resolved context:
- current raw question;
- short conversation history;
- previous in-scope topic if the current question is a short follow-up;
- structured chapter/experiment/point fields.

The policy gate will classify against the resolved question/context. Deterministic safety and assessment checks still win.

Alternative considered: only send full history to the final answer model. That is too late because policy gating can already short-circuit the request.

### Platform resource rail is inventory-only

The platform resource path applies only to availability/lookup questions such as "is there a published video", "where can I watch/download", or "has the teacher uploaded this material". It does not apply to "explain this video point", "use the material to explain", "what does this figure show", or follow-up conceptual questions.

If inventory lookup finds nothing, the assistant answers normally with "not published/found" rather than labeling the turn as a safety refusal.

## Risks / Trade-offs

- [Risk] Point evidence may be incomplete for some points -> Show diagnostics and let the model answer from chemistry knowledge without fabricating textbook provenance.
- [Risk] Querying question-bank metadata by point key can be slower if done naively -> Limit lookups to the selected experiment/chapter and cap evidence items.
- [Risk] Resolved follow-up may inherit the wrong prior topic -> Only inherit context for short/deictic follow-ups and preserve raw question in diagnostics.
- [Risk] Resource rail may become too narrow -> Keep explicit resource availability patterns and tests for published-resource lookup.

## Migration Plan

1. Add schema fields and frontend prompt metadata without removing existing natural-language prompt behavior.
2. Add point evidence package assembly and diagnostics.
3. Update policy-gate payload and deterministic classifier.
4. Update debug UI to show point context and route prompt cards with `point_key`.
5. Add tests covering RAG-disabled point explanation, resource lookup, and multi-turn follow-up.

Rollback is straightforward: ignore `point_key` in requests and retain current RAG behavior. Existing clients without `point_key` continue to work.
