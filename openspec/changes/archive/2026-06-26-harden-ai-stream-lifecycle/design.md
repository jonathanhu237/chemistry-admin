## Context

The Atom assistant now sits on two important streamed surfaces:

- Student H5 `/api/student/assistant/ask/stream`, called from the Atom root and contextual chat pages.
- Teacher/admin `/api/admin/learning-assistant/ask/stream`, used by the learning-assistant debug console and student preview workflows.

Both streams eventually use `run_agent_stream`. The current implementation has three lifecycle gaps:

1. The browser clients start `fetch` streams without passing an `AbortSignal`, so leaving a page, opening a new chat, or clearing a conversation does not intentionally close the active request.
2. The FastAPI streaming endpoints do not receive `Request` and do not check `request.is_disconnected()`, so the server can keep iterating after the browser is gone.
3. `run_agent_stream` is an async generator, but its OpenAI Responses and Chat Completions stream helpers use the synchronous `OpenAI` client and blocking `for event in stream` loops. In a single uvicorn worker this can delay scheduling unrelated requests such as student video feeds, teacher preview requests, or other AI turns.

The risk is not limited to one abandoned Atom page. It is a product-level concurrency problem: teachers and students must be able to view pages, load videos, and run independent AI requests at the same time without one stale stream monopolizing the backend event loop or provider connection.

Current simplified flow:

```text
Student/Teacher UI
  fetch(stream, no signal)
    -> FastAPI StreamingResponse
      -> stream_student_assistant_answer / run_agent_stream
        -> sync OpenAI stream loop inside async generator
```

Target flow:

```text
UI owns AbortController
  -> fetch(..., signal)
    -> endpoint checks request.is_disconnected()
      -> agent stream receives cancellation/disconnect predicate
        -> AsyncOpenAI async stream yields without blocking event loop
          -> cleanup stops final metadata and success persistence when cancelled
```

## Goals / Non-Goals

**Goals:**

- Make student and teacher assistant streams cancellable from the browser.
- Make backend stream generators stop promptly when the client disconnects.
- Replace synchronous OpenAI streaming inside async paths with `AsyncOpenAI` streaming where supported.
- Keep fallback providers async-safe by isolating unavoidable synchronous streaming away from the event loop.
- Preserve successful stream event contracts: `status`, `thinking`, `delta`, `replace`, `final`, `error`, `suggested_prompts`, and `conversation_title`.
- Ensure cancelled turns do not become user-visible errors or completed local history entries.
- Add concurrency regression tests proving a long or abandoned AI stream does not block unrelated API requests.

**Non-Goals:**

- Do not add backend chat-session persistence.
- Do not change Atom's one-chat-one-point binding policy.
- Do not redesign the Atom UI.
- Do not change RAG selection, guardrail policy, visible-thinking content rules, or final metadata generation semantics for successful turns.
- Do not rely on extra uvicorn workers as the primary correctness mechanism.

## Decisions

### Treat every stream as an owned lifecycle resource

Each UI stream caller should create one `AbortController` for one in-flight assistant request. The owner aborts it when:

- The component unmounts or route is left.
- The user starts a new chat, clears the current chat, or resets context.
- A new stream would replace the existing stream.

The low-level SSE client helpers should accept an optional `signal` and pass it to `fetch`. They should cancel the `ReadableStreamDefaultReader` in cleanup where possible, and they should surface browser aborts as a typed/recognizable cancellation outcome rather than a generic failure.

Alternative considered: only ignore late events in React state. Rejected because it hides stale UI updates but leaves the network request, backend generation, and provider stream running.

### Check disconnect at the FastAPI boundary and inside the generator

The stream endpoints should accept `Request` and provide a small disconnect predicate to the domain stream. The SSE wrapper should check before entering expensive iteration and before yielding each event. The domain stream should also check between agent phases and before final metadata post-processing.

Cancellation should stop the generator cleanly. It should not emit a student-facing `error` event after the client has gone away, and it should not run follow-up/title metadata generation for an answer that no longer has a client.

Alternative considered: rely on `StreamingResponse` automatically cancelling the generator. Rejected because the current code has blocking synchronous sections where cancellation cannot be observed promptly, and explicit checks make the lifecycle testable.

### Make the shared agent stream async-safe

The student and teacher streams share `run_agent_stream`, so async safety belongs in the shared agent helpers, not only in the student endpoint.

Preferred provider path:

- Use `AsyncOpenAI` for Responses streaming when reasoning summaries are enabled.
- Use `AsyncOpenAI` for Chat Completions streaming when the chat fallback path is used.
- Use `async with` / `async for` style APIs where the SDK exposes them.
- Keep the existing event translation and sanitizer behavior for `thinking`, answer deltas, replacements, and final responses.

Compatibility path:

- If a configured OpenAI-compatible provider or SDK shape cannot use async streaming, run the synchronous stream in an isolated worker thread and bridge chunks back to the async generator through an `asyncio.Queue`.
- The bridge must observe a cancellation flag and close the provider stream when possible.
- The event loop must never wait inside a synchronous provider `for chunk in stream` loop.

Alternative considered: convert only the student endpoint and leave `run_agent_stream` synchronous internally. Rejected because the teacher debug console uses the same agent stream, and synchronous provider waits can still block unrelated requests.

### Propagate cancellation through answer and metadata phases

`stream_student_assistant_answer` currently intercepts the successful `final` response to attach `suggested_prompts` and `conversation_title`. That remains correct for successful turns, but it must become cancellation-aware.

When cancellation/disconnect is detected:

- Stop iterating the agent stream.
- Skip final metadata generation.
- Do not persist a local frontend history entry as completed from a missing final event.
- Do not show a failure toast or error bubble for user-initiated cancellation.
- Backend may log an informational cancellation lifecycle event, but it must not record it as a model failure.

Alternative considered: let metadata generation finish after disconnect so history can still have titles/prompts. Rejected because there may be no UI to receive it and it keeps using model resources after the user has abandoned the turn.

### Preserve successful stream semantics exactly

This change should be invisible for normal successful turns except for better concurrency. Existing clients that receive a complete answer should continue to see the same event names and payload shapes.

In particular:

- Visible thinking is still separate from answer text.
- `final.response` remains the source for answer metadata, suggested prompts, and conversation title.
- Output guardrail `replace` events still replace answer content.
- Errors from real failed turns remain student-safe/admin-safe as already specified.

### Verify concurrency, not just cancellation flags

The implementation should include tests at three levels:

- Frontend tests that assert `AbortController.abort()` is called on route leave, new chat/reset, clear, and replacement scenarios.
- Backend generator tests that simulate disconnect and assert the stream stops before final metadata/persistence.
- Backend concurrency tests that run a slow fake AI stream while probing a lightweight endpoint or feed handler and assert the probe completes without waiting for the stream to finish.

Operational worker counts can still be tuned later, but tests should prove the single-process async path is not accidentally blocked by provider streaming.

## Risks / Trade-offs

- [Risk] Some OpenAI-compatible providers may not implement async streaming exactly like the official SDK. -> Mitigation: keep an async-safe thread bridge fallback and cover it with a fake sync provider test.
- [Risk] Cancellation could accidentally swallow real provider errors. -> Mitigation: distinguish client cancellation from provider exceptions and keep provider failures as normal `error` events while the client is connected.
- [Risk] Aborting after partial deltas may leave frontend state inconsistent. -> Mitigation: make cancelled turns a first-class UI state and remove or mark the in-flight draft according to the surface's behavior.
- [Risk] Final metadata generation may still use a synchronous OpenAI call. -> Mitigation: either convert title/prompt generation to async or run it in async-safe isolation; skip it entirely when cancellation has been requested.
- [Risk] Existing tests mock `streamStudentAssistantAsk` with the old two-argument signature. -> Mitigation: update mocks to accept an optional third options argument without changing existing payload assertions.
- [Risk] Hiding cancellation from students could hide real failures if overbroad. -> Mitigation: only suppress recognized abort/disconnect cancellation; all non-abort exceptions remain visible as existing safe error UI.

## Migration Plan

- Extend frontend stream helper signatures to accept optional `{ signal }` while keeping existing callers valid.
- Add cancellation ownership to student and teacher stream surfaces.
- Add backend request/disconnect plumbing without changing request payload schemas.
- Convert shared OpenAI streaming helpers to `AsyncOpenAI` or async-safe fallback.
- Add tests and run existing focused assistant suites.
- Deploy normally. Rollback is safe because payload and successful SSE contracts remain compatible; older clients simply will not send abort signals.

## Open Questions

- Whether cancelled turns should be removed from visible history or marked as cancelled when cancellation happens from an explicit user action while the page remains visible. The default implementation should remove in-flight drafts for new-chat/clear flows and avoid persisting incomplete turns as completed history.
- Whether to extend this lifecycle contract immediately to every non-streaming one-shot OpenAI call in the repository. This change should at minimum cover calls executed as part of streamed assistant turns; broader one-shot AI hardening can follow separately.
