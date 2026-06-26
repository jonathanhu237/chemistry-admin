## Why

Student and teacher AI usage is moving from a single Atom page experiment into a shared product capability. The current student assistant stream can continue generating after the user leaves the page, and the backend uses synchronous OpenAI streaming inside an async request path, which can waste model work and can delay unrelated student or teacher requests under concurrent use.

This change hardens the full AI streaming lifecycle so an abandoned Atom request is cancelled promptly, the backend notices client disconnects, and OpenAI streaming no longer blocks the event loop that also serves video feeds, teacher previews, and other student pages.

## What Changes

- Add a platform-level lifecycle contract for AI streaming requests: every streamed assistant response must be cancellable, disconnect-aware, and non-blocking.
- Convert the student assistant OpenAI streaming path to use `AsyncOpenAI` or an equivalent async-safe isolation path for providers that cannot stream asynchronously.
- Add frontend `AbortController` ownership for student AI stream requests so route leave, unmount, new chat, reset, or replacement submission cancels the active stream.
- Add the same cancellation ownership to the teacher/admin learning-assistant debug stream client so teacher preview/debug work does not leave abandoned streams running.
- Add backend `Request` disconnect checks for `/api/student/assistant/ask/stream` and propagate cancellation through the assistant domain stream.
- Treat client-initiated cancellation as a normal lifecycle outcome, not as a student-visible error, backend answer failure, or history entry to persist as complete.
- Preserve existing answer, `thinking`, `final`, `error`, `suggested_prompts`, and `conversation_title` event contracts for successful turns.
- Add regression coverage proving one long or abandoned AI stream does not block unrelated student/teacher API work.
- Do not introduce backend chat-session persistence or change the one-point Atom context-binding model.

## Capabilities

### New Capabilities
- `ai-stream-lifecycle`: Defines platform requirements for cancellable, disconnect-aware, async-safe AI streaming across assistant endpoints.

### Modified Capabilities
- `student-h5-ai-assistant`: Clarifies student H5 behavior when a stream is cancelled by navigation, new chat, reset, or component unmount.
- `learning-assistant-debug-console`: Clarifies teacher/admin debug-console behavior when an active stream is cancelled by navigation, clearing, or replacement submission.

## Impact

- Frontend:
  - `apps/web-student/src/api.ts`
  - `apps/web-student/src/features/assistant/StudentAiChatPanel.tsx`
  - related student H5 route and assistant tests
- Teacher/admin frontend:
  - `apps/web-teacher/src/api/http.ts`
  - `apps/web-teacher/src/features/learning-assistant/LearningAssistantPage.tsx`
  - related teacher learning-assistant stream tests
- Backend:
  - `server/app/api/student/student_assistant.py`
  - `server/app/domains/assistant/student_assistant.py`
  - `server/app/domains/assistant/agent.py`
  - backend tests for disconnect, cancellation, and concurrent request scheduling
- Runtime/dependencies:
  - Uses the already-installed OpenAI Python SDK async client support.
  - May add request timing/cancellation logs.
  - Multiple uvicorn workers may be considered as operational mitigation, but they are not the primary fix.
