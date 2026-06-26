# ai-stream-lifecycle Specification

## Purpose
TBD - created by archiving change harden-ai-stream-lifecycle. Update Purpose after archive.
## Requirements
### Requirement: Assistant streams are cancellable end to end
Every streamed assistant request SHALL have a cancellation path from the browser caller through the backend stream generator to the provider stream.

#### Scenario: Browser cancels an active assistant stream
- **WHEN** a browser assistant client aborts the request using the stream's `AbortSignal`
- **THEN** the network request MUST stop reading further SSE data
- **AND** the backend MUST stop generating additional assistant events for that request
- **AND** any active provider stream for that request MUST be closed or allowed to unwind without continuing answer generation.

#### Scenario: Stream is superseded by another stream
- **WHEN** the same UI surface starts a new assistant stream while an older stream is still active
- **THEN** the older stream MUST be cancelled before or during creation of the new stream
- **AND** late events from the older stream MUST NOT mutate the visible state of the newer turn.

#### Scenario: Cancellation is not a model failure
- **WHEN** a stream stops because the browser aborted or the client disconnected
- **THEN** the backend MUST treat it as a cancellation lifecycle outcome
- **AND** it MUST NOT emit a user-visible `error` event after disconnect
- **AND** it MUST NOT record the cancellation as a normal model failure.

### Requirement: Stream endpoints are disconnect-aware
Backend SSE endpoints SHALL detect client disconnects and stop streaming promptly.

#### Scenario: Client disconnects before the next SSE event
- **WHEN** an assistant SSE endpoint detects that the request is disconnected before yielding the next event
- **THEN** it MUST stop iterating the domain stream
- **AND** it MUST NOT yield additional SSE frames.

#### Scenario: Client disconnects during backend generation
- **WHEN** the client disconnects while policy, retrieval, provider generation, or metadata post-processing is in progress
- **THEN** the next cancellation checkpoint MUST stop the assistant turn
- **AND** final metadata generation MUST be skipped when the answer no longer has a connected client.

#### Scenario: Successful connected stream completes
- **WHEN** the client remains connected until the assistant answer completes
- **THEN** the endpoint MUST continue emitting the established successful stream events
- **AND** the final event contract MUST remain unchanged.

### Requirement: Provider streaming is async-safe
Assistant provider streaming SHALL NOT block the backend event loop while waiting for model tokens or provider stream events.

#### Scenario: Responses streaming is available
- **WHEN** the configured OpenAI-compatible runtime supports async Responses streaming
- **THEN** the assistant MUST use an async client path for Responses streaming
- **AND** reasoning-summary events MUST continue to be translated into student-safe `thinking` events when enabled.

#### Scenario: Chat completion streaming is available
- **WHEN** the assistant falls back to Chat Completions streaming
- **THEN** the assistant MUST use an async client path for chat streaming when the configured SDK/provider supports it
- **AND** answer deltas MUST continue to be emitted as existing `delta` events.

#### Scenario: Only synchronous provider streaming is available
- **WHEN** a configured provider path cannot stream through an async SDK interface
- **THEN** the synchronous provider stream MUST run outside the event loop in an async-safe isolation bridge
- **AND** the async generator MUST receive chunks without blocking unrelated FastAPI requests
- **AND** cancellation MUST be observable by the bridge.

### Requirement: Agent stream observes cancellation checkpoints
The shared assistant agent stream SHALL check for cancellation between expensive phases and before post-processing.

#### Scenario: Cancellation before policy evaluation completes
- **WHEN** a cancellation request is observed before policy evaluation finishes
- **THEN** the agent stream MUST stop without starting retrieval, provider generation, or final metadata generation.

#### Scenario: Cancellation before provider generation starts
- **WHEN** a cancellation request is observed after policy or retrieval decision but before provider generation
- **THEN** the agent stream MUST stop without opening a provider stream.

#### Scenario: Cancellation during provider generation
- **WHEN** a cancellation request is observed while provider generation is streaming
- **THEN** the agent stream MUST stop collecting answer deltas
- **AND** it MUST close or unwind the provider stream when possible
- **AND** it MUST NOT emit a successful `final` event for the cancelled turn.

#### Scenario: Cancellation before final metadata
- **WHEN** a cancellation request is observed after answer text exists but before final metadata generation completes
- **THEN** generated follow-up prompts, generated conversation title, and other final-only metadata MUST be skipped
- **AND** the cancelled turn MUST NOT be treated as a completed successful answer.

### Requirement: Successful stream contracts remain compatible
Lifecycle hardening SHALL preserve existing successful assistant stream event names and payload semantics.

#### Scenario: Successful student stream
- **WHEN** a student assistant stream completes without cancellation or provider failure
- **THEN** the stream MUST continue to support `status`, `thinking`, `delta`, `replace`, `final`, and `error` events according to existing student assistant specifications
- **AND** `suggested_prompts` and `conversation_title` MUST remain final metadata rather than answer text.

#### Scenario: Successful teacher debug stream
- **WHEN** a teacher/admin learning-assistant debug stream completes without cancellation or provider failure
- **THEN** the stream MUST continue to support the existing debug console status, delta, replacement, final response, and diagnostics behavior.

#### Scenario: Real provider failure while connected
- **WHEN** provider generation fails and the client is still connected
- **THEN** the backend MUST continue to surface the existing safe `error` behavior
- **AND** the implementation MUST NOT suppress real failures as cancellation.

### Requirement: Concurrent requests remain responsive during AI streaming
The backend SHALL continue serving unrelated student and teacher requests while an assistant stream is active, slow, or cancelled.

#### Scenario: Slow AI stream is active
- **WHEN** one assistant stream is waiting on a slow provider response
- **THEN** unrelated lightweight API requests MUST be scheduled without waiting for that provider stream to finish
- **AND** student video feed or teacher preview endpoints MUST remain able to return independently.

#### Scenario: Abandoned AI stream is cancelled
- **WHEN** an assistant stream is abandoned by navigation or disconnect
- **THEN** backend resources for that stream MUST be released promptly
- **AND** later student or teacher requests MUST NOT wait for the abandoned answer to finish.

#### Scenario: Multiple users stream concurrently
- **WHEN** multiple teachers and students start assistant streams at the same time
- **THEN** each stream MUST maintain isolated lifecycle state
- **AND** cancellation of one stream MUST NOT cancel or corrupt another user's stream.

### Requirement: Stream lifecycle is observable
Assistant streaming lifecycle events SHALL be diagnosable without exposing internals to students.

#### Scenario: Stream starts and completes
- **WHEN** an assistant stream starts and later completes successfully
- **THEN** backend logs or metrics MUST distinguish start, first event, final event, and completion timing
- **AND** student-facing payloads MUST NOT include internal timing diagnostics unless an existing student-safe contract allows them.

#### Scenario: Stream is cancelled
- **WHEN** an assistant stream is cancelled by browser abort or client disconnect
- **THEN** backend logs or metrics MUST record a cancellation lifecycle outcome
- **AND** logs MUST distinguish cancellation from provider error.
