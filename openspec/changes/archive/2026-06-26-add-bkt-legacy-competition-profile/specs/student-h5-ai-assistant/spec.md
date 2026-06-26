## ADDED Requirements

### Requirement: Legacy student profile excludes Atom assistant surfaces
The legacy student frontend SHALL not expose Atom or student AI assistant surfaces.

#### Scenario: Legacy student navigation is rendered
- **WHEN** an authenticated student opens `web-student-old`
- **THEN** root navigation MUST NOT include an Atom, AI, assistant, chat, or learning-assistant tab
- **AND** the old product MUST NOT provide visible routes equivalent to `/ai`, `/ai/chat`, or `/ai/artifact`

#### Scenario: Legacy student opens learning or video detail
- **WHEN** a student opens a legacy learning page, video feed item, point detail, search page, assessment page, or report page
- **THEN** the page MUST NOT show Atom ask buttons, contextual AI actions, AI prompt chips, assistant composer controls, or Atom model cards
- **AND** any current-product contextual assistant handoff MUST be omitted or replaced by BKT/learning-resource actions in the old product

#### Scenario: Stale old student URL targets an assistant route
- **WHEN** a student manually enters or follows a stale old-product URL for an assistant route
- **THEN** the old product MUST redirect to a safe old route or render a controlled not-found state
- **AND** it MUST NOT mount the current Atom assistant shell

### Requirement: Legacy student reports avoid assistant branding
The legacy student frontend SHALL present assessment explanations and learning suggestions without Atom or RAG branding.

#### Scenario: Legacy student views an assessment report
- **WHEN** a student opens a legacy assessment or posttest report
- **THEN** report copy MUST use BKT, mastery, mistake review, learning suggestion, or teacher-reviewed explanation wording
- **AND** it MUST NOT label summaries, suggestions, explanations, or source notes as Atom, RAG, Agent, or AI chat output
