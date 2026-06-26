## ADDED Requirements

### Requirement: Debug console cancels obsolete streams
The teacher/admin learning-assistant debug console SHALL cancel active assistant streams that no longer belong to the current page session state.

#### Scenario: Admin leaves the debug console while streaming
- **WHEN** an admin or teacher leaves the learning-assistant debug console while an answer is still streaming
- **THEN** the frontend MUST abort the active debug stream request
- **AND** late stream events MUST NOT update the unmounted page.

#### Scenario: Admin clears the conversation while streaming
- **WHEN** an admin clears the debug console conversation while an answer is still streaming
- **THEN** the frontend MUST abort the active debug stream request
- **AND** the cleared conversation MUST NOT receive later answer deltas, final diagnostics, success messages, or error messages from the cancelled stream.

#### Scenario: Admin starts a replacement debug run
- **WHEN** the debug console permits a new assistant run before the previous stream completes
- **THEN** the previous stream MUST be aborted before the replacement run becomes active
- **AND** the replacement run MUST maintain independent turn and diagnostics state.

### Requirement: Debug stream helper supports abort signals
The teacher/admin SSE helper SHALL accept an optional cancellation signal without breaking existing debug-console streaming behavior.

#### Scenario: Debug signal is provided
- **WHEN** the debug console starts a stream with an abort signal
- **THEN** the shared teacher frontend SSE helper MUST pass that signal to `fetch`
- **AND** reader cleanup MUST stop consuming the response body after abort.

#### Scenario: Debug abort is caught
- **WHEN** a debug stream rejects because the console intentionally aborted it
- **THEN** the page MUST NOT show a success notification, provider failure notification, or stale diagnostics for that cancelled turn
- **AND** real non-abort stream failures MUST continue to use the existing admin-safe error behavior.
