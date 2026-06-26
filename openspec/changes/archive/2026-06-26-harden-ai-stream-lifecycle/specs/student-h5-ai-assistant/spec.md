## ADDED Requirements

### Requirement: Student assistant cancels obsolete streams
The student H5 Atom assistant SHALL cancel any active assistant stream when that stream is no longer the active visible turn.

#### Scenario: Student leaves an active assistant route
- **WHEN** a student assistant stream is active
- **AND** the student leaves the route, the assistant component unmounts, or the teacher preview iframe destroys the student page
- **THEN** the frontend MUST abort the active stream request
- **AND** late events from that stream MUST NOT update React state after unmount.

#### Scenario: Student starts a new chat while streaming
- **WHEN** a student activates the Atom new-chat action while an answer is still streaming
- **THEN** the frontend MUST abort the active stream request
- **AND** the new empty chat state MUST NOT receive answer deltas, final metadata, or error events from the cancelled stream.

#### Scenario: Student resets or clears context while streaming
- **WHEN** a student resets the assistant context, clears the selected point, restores a different history entry, or otherwise replaces the active conversation while an answer is still streaming
- **THEN** the frontend MUST abort the obsolete stream
- **AND** the resulting active context and visible conversation MUST remain internally consistent.

#### Scenario: Student submits a replacement request
- **WHEN** the UI permits a new student assistant submission before the previous stream has completed
- **THEN** the previous request MUST be cancelled before the new stream becomes active
- **AND** only the newest active stream MUST be allowed to update the latest assistant turn.

### Requirement: Student cancellation is not shown as an assistant failure
The student H5 Atom assistant SHALL distinguish user-initiated cancellation from a real assistant error.

#### Scenario: Browser abort is caught
- **WHEN** the frontend catches an abort caused by its own `AbortController`
- **THEN** it MUST stop the loading state for the cancelled turn
- **AND** it MUST NOT show a student-facing error bubble, toast, or failed-answer copy solely because of the abort.

#### Scenario: Cancelled stream has no final event
- **WHEN** a cancelled stream ends before receiving a successful `final` event
- **THEN** the frontend MUST NOT persist that turn as a completed local history entry
- **AND** it MUST NOT attach stale `suggested_prompts`, stale `conversation_title`, or stale final metadata to the active chat.

#### Scenario: Real stream error occurs while connected
- **WHEN** a student assistant stream fails for a non-abort reason while the page is still active
- **THEN** the frontend MUST keep the existing student-safe error behavior
- **AND** the implementation MUST NOT hide real assistant failures as cancellation.

### Requirement: Student stream helper supports abort signals
The student H5 API stream helper SHALL accept an optional cancellation signal without breaking existing call sites.

#### Scenario: Signal is provided
- **WHEN** `streamStudentAssistantAsk` is called with an abort signal
- **THEN** the helper MUST pass that signal to `fetch`
- **AND** reader cleanup MUST stop reading the response body when the signal is aborted.

#### Scenario: Signal is omitted
- **WHEN** an existing caller uses `streamStudentAssistantAsk` without a signal
- **THEN** the helper MUST continue to stream successful SSE events with the existing callback contract.
