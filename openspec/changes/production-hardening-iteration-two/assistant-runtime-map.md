# Assistant Runtime Responsibility Map

`server/app/agent.py` remains the largest backend module. The second hardening pass treats it as working production code and splits only along stable, behavior-preserving boundaries.

## Current Public Surface

- `run_agent(...)`
- `run_agent_stream(...)`
- `agent_to_rag_request(...)`
- `rag_to_agent_request(...)`
- `_normalize_assistant_formula_output` re-exported for existing tests/imports

These imports must remain compatible while internals move.

## Responsibility Groups

### Runtime Orchestration

Current functions:

- `run_agent`
- `run_agent_stream`
- `_run_with_optional_sdk`
- `_preflight_response`
- `_chunk_stream_text`
- `_dump_agent_response`

Role: build `AgentRunContext`, apply point evidence, run policy, choose preflight/local/LLM path, normalize final output, persist logs, and emit stream events.

### Policy And Guardrails

Current functions/classes:

- `AgentPolicy`
- `StudentAIPolicyDecision`
- `load_agent_policy`
- `classify_agent_request`
- `_policy_gate_decision`
- `_run_openai_policy_gate`
- `_parse_policy_decision_payload`
- `_invalid_policy_decision`
- `_local_policy_decision_from_classification`
- `_apply_policy_decision_to_classification`
- `_is_rag_source_asset_request`
- `_is_platform_resource_request`
- `_intent_name`

Role: classify student turns, prevent platform-resource hallucination, keep source-figure requests on the learning evidence rail, and encode student AI policy.

### Point Evidence And Citation Shaping

Current functions:

- `_resolve_point_context`
- `_experiment_video_points`
- `_candidate_point_key`
- `_experiment_title`
- `_build_point_evidence_package`
- `_sources_for_chunk_ids`
- `_point_source_payloads`
- `_unique_texts`
- `_figure_evidence_items`
- `_source_asset_answer`
- `_merge_sources`
- `_rag_trace_payload`

Role: hydrate manual reviewed point evidence, merge canonical chunks into response sources, shape fixed evidence payloads, and expose image assets/citations.

### Retrieval And Tool Coordination

Current functions:

- `approved_tool_registry`
- `rag_search_tool`
- `curriculum_lookup_tool`
- `published_resource_lookup_tool`
- `own_student_progress_lookup_tool`
- `_retrieve_context`
- `_generate_retrieval_queries`
- `agent_to_rag_request`
- `rag_to_agent_request`

Role: bridge assistant requests to RAG/curriculum/media/progress repositories, record tool calls, generate retrieval queries, and maintain RAG trace semantics.

### LLM Adapters

Current functions:

- `_run_openai_agents_sdk`
- `_run_openai_chat_completion`
- `_run_openai_chat_completion_stream`
- `_sdk_enabled`
- `_agent_instructions`
- `_agent_user_input`
- `_conversation_history_payload`
- `_policy_conversation_payload`
- `_resolved_policy_question`

Role: translate the internal context into OpenAI Agents SDK or Chat Completions calls, including prompt construction and streaming deltas.

### Output Normalization And Persistence

Current functions:

- `_apply_output_guardrails`
- `_has_resource_tool_result`
- `_count_result`
- `_preview_result`
- `_persist_agent_log`
- `_persist_agent_error_log`

Role: enforce final evidence/resource/length/formula guardrails, summarize tool calls, and write success/error logs. Formula normalization already lives in `server/app/services/agent_output_normalization.py`.

## Characterization Tests Added

- `server/tests/test_assistant_runtime_characterization.py`
  - Fixed manual-reviewed point evidence remains preferred when supplemental RAG is disabled.
  - RAG disabled requests use curriculum context and record `rag_lookup_disabled` without calling `rag_search`.
- Existing tests retained:
  - `server/tests/test_student_chat_image_evidence.py`
  - `server/tests/test_assistant_chem_latex_normalization.py`

## Extraction Order

1. Move output guardrail helpers first; they are low-I/O and already partly backed by formula normalization tests.
2. Move point evidence and figure/citation shaping next; new characterization tests cover the manual evidence path.
3. Move retrieval/tool coordination after point evidence is stable.
4. Leave runtime orchestration as the last facade so public imports and endpoint behavior remain stable throughout.

Each extraction should keep compatibility imports in `server/app/agent.py` until callers/tests are intentionally updated.

## Extraction Completed

- Added `server/app/services/agent_evidence_shaping.py` for figure evidence item shaping, source merging, and RAG trace payload shaping.
- Added `server/app/services/agent_output_guardrails.py` for tool result summaries, resource-tool-result checks, and formula normalization wrapping.
- Added `server/app/services/agent_retrieval.py` for agent/RAG request conversion, legacy source-context retrieval, and retrieval query generation.
- Added `server/app/services/agent_runtime.py` for `AgentRunContext`, policy decision value object, response assembly, response dumping, and stream chunking.
- Kept compatibility aliases in `server/app/agent.py` for private helper imports used by existing tests.
- Reduced `server/app/agent.py` from 1562 lines to 1321 lines without changing public assistant entry points.
- Extended `server/tests/test_assistant_runtime_characterization.py` to cover retrieval helper round-tripping, disabled query-generation fallback, and source-context ranking.

## Verification

- `python -m pytest server\tests\test_assistant_runtime_characterization.py server\tests\test_student_chat_image_evidence.py server\tests\test_assistant_chem_latex_normalization.py -q`: 11 passed.
- `python -m pytest server\tests -q`: 50 passed.
- Backend container rebuilt with `docker compose --profile rag up -d --build backend`; `/health` returned `{"status":"ok"}`.
- Authenticated `POST /api/admin/learning-assistant/ask` returned a compatible assistant response with `rag_lookup_disabled` when `allow_rag_lookup=false`.
- Browser smoke on `http://localhost:5174/admin/learning-assistant`: workbench loaded, RAG runtime was visible, and representative experiment point prompts rendered.
