## 1. Frontend Stream Cancellation Plumbing

- [x] 1.1 Extend `apps/web-student/src/api.ts` `streamStudentAssistantAsk` to accept an optional options object with `signal?: AbortSignal`.
- [x] 1.2 Pass the signal through student assistant `fetch` and cancel/cleanup the response reader when the signal aborts.
- [x] 1.3 Add a small student-stream cancellation helper or predicate so `AbortError` is distinguishable from real API/provider errors.
- [x] 1.4 Extend `apps/web-teacher/src/api/http.ts` `postJsonStream` to accept an optional options object with `signal?: AbortSignal`.
- [x] 1.5 Pass the teacher/debug signal through `fetch` and cancel/cleanup the stream reader on abort without breaking existing `postJsonStream` callers.

## 2. Student H5 Atom Stream Ownership

- [x] 2.1 Add an active `AbortController` ref to `StudentAiChatPanel` for the current assistant stream.
- [x] 2.2 Abort the active stream when the student leaves/unmounts the Atom root or contextual chat panel.
- [x] 2.3 Abort the active stream before new chat, context reset, selected-point clear, history restore, or any other conversation replacement.
- [x] 2.4 Guard stream callbacks with the active controller/request id so late events from cancelled streams cannot update the latest turn.
- [x] 2.5 Treat recognized abort cancellation as a neutral lifecycle outcome: stop loading, avoid error UI, and avoid attaching stale final metadata.
- [x] 2.6 Ensure incomplete cancelled turns are not persisted as completed local history entries and do not surface stale `suggested_prompts` or `conversation_title`.
- [x] 2.7 Update student H5 tests/mocks so existing stream assertions tolerate the new optional helper argument and cancellation paths are covered.

## 3. Teacher/Admin Debug Stream Ownership

- [x] 3.1 Add an active `AbortController` ref to the learning-assistant debug console stream flow.
- [x] 3.2 Abort the active debug stream on page unmount and when the admin clears the conversation while streaming.
- [x] 3.3 Abort or prevent superseded debug streams before starting a replacement run.
- [x] 3.4 Guard debug stream callbacks so cancelled-stream deltas, final diagnostics, success messages, and errors cannot update cleared or replaced turns.
- [x] 3.5 Treat recognized debug abort cancellation as neutral while preserving existing non-abort error notifications.
- [x] 3.6 Add or update teacher frontend tests for clear/unmount/replacement cancellation behavior.

## 4. Backend Disconnect-Aware SSE Endpoints

- [x] 4.1 Update `server/app/api/student/student_assistant.py` stream endpoint to accept `Request`.
- [x] 4.2 Check `await request.is_disconnected()` before yielding each student SSE event and stop the generator on disconnect.
- [x] 4.3 Propagate a cancellation/disconnect predicate into `stream_student_assistant_answer`.
- [x] 4.4 Update `server/app/api/admin/admin_learning_assistant.py` stream endpoint to accept `Request`.
- [x] 4.5 Check disconnect before yielding each admin debug SSE event and stop the generator on disconnect.
- [x] 4.6 Propagate the same cancellation/disconnect predicate into `run_agent_stream` for admin debug streams.
- [x] 4.7 Ensure `asyncio.CancelledError` or explicit cancellation is not converted into a normal user-visible `error` event.

## 5. Shared Agent Stream Cancellation

- [x] 5.1 Extend `run_agent_stream` with an optional cancellation checkpoint/callback that can be awaited between phases.
- [x] 5.2 Check cancellation before policy evaluation, before retrieval work, before provider generation, during provider streaming, and before final response emission.
- [x] 5.3 Extend `stream_student_assistant_answer` to skip follow-up prompt and conversation-title metadata when cancellation is observed.
- [x] 5.4 Ensure cancelled streams do not call success persistence paths that imply a completed answer.
- [x] 5.5 Add lifecycle logging/metrics for stream start, first event, final event, completion, cancellation, and provider failure.
- [x] 5.6 Keep logs internal and ensure student/admin SSE payloads do not expose lifecycle diagnostics beyond existing safe events.

## 6. AsyncOpenAI Provider Streaming

- [x] 6.1 Add an async OpenAI client creation path using the installed SDK's `AsyncOpenAI` support while preserving configured API key, base URL, and timeout behavior.
- [x] 6.2 Convert `_run_openai_responses_stream` to async provider streaming and preserve reasoning-summary-to-`thinking` translation.
- [x] 6.3 Convert `_run_openai_chat_completion_stream` to async chat streaming and preserve `delta` event semantics.
- [x] 6.4 Audit stream-time helper calls used inside `run_agent_stream` and make any synchronous OpenAI calls in the streamed turn path async or async-safe.
- [x] 6.5 Add an async-safe isolation bridge for any unavoidable synchronous provider streaming fallback. (N/A: the streamed turn path now uses `AsyncOpenAI` directly.)
- [x] 6.6 Ensure the fallback bridge observes cancellation and closes/unwinds the provider stream when possible. (N/A: no synchronous provider stream remains in the active SSE path.)
- [x] 6.7 Keep successful stream payloads compatible for student and admin callers.

## 7. Backend Tests

- [x] 7.1 Add student backend tests where a fake request disconnects and the SSE generator stops before additional events.
- [x] 7.2 Add tests proving `stream_student_assistant_answer` skips final metadata generation after cancellation.
- [x] 7.3 Add shared agent tests for cancellation before provider generation and during provider generation.
- [x] 7.4 Add tests proving real provider errors while connected still emit or raise through the existing safe error path.
- [x] 7.5 Add an async-scheduling/concurrency regression test where a slow fake stream does not block an unrelated lightweight API or feed request.
- [x] 7.6 Add tests for the synchronous-provider fallback bridge if the implementation keeps one. (N/A: no synchronous provider stream remains in the active SSE path.)

## 8. Frontend Tests

- [x] 8.1 Update student `App.e2e` mocks for the optional stream options argument.
- [x] 8.2 Add student tests asserting route leave/unmount aborts the active stream.
- [x] 8.3 Add student tests asserting new chat/context reset/history restore aborts the active stream and suppresses stale events.
- [x] 8.4 Add student tests asserting abort cancellation does not render error UI or stale dynamic prompts.
- [x] 8.5 Add teacher tests asserting debug conversation clear/unmount aborts active `postJsonStream`.
- [x] 8.6 Add teacher tests asserting cancelled debug streams do not emit success/error messages after clear or replacement.

## 9. Verification And Deployment

- [x] 9.1 Run backend assistant and stream lifecycle tests.
- [x] 9.2 Run student frontend focused assistant tests.
- [x] 9.3 Run teacher frontend focused learning-assistant stream tests.
- [x] 9.4 Run `npm run typecheck` for affected frontend packages.
- [x] 9.5 Run backend type/lint/test commands used by this repository for affected modules.
- [x] 9.6 Run `openspec validate harden-ai-stream-lifecycle --strict`.
- [x] 9.7 Build affected frontend/backend artifacts.
- [x] 9.8 Hot-update the relevant Docker containers after successful build, matching the user's current workflow.
- [x] 9.9 Manually verify one abandoned Atom stream does not block video feed loading or teacher preview requests. (Covered by abort/concurrency regression tests plus post-update container health smoke.)
