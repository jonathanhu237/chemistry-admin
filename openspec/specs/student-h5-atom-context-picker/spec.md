# student-h5-atom-context-picker Specification

## Purpose
TBD - created by archiving change atom-context-point-picker. Update Purpose after archive.
## Requirements
### Requirement: Atom root plus opens learning-background picker
The student H5 Atom root assistant SHALL use the root composer `+` action to open an in-Atom learning-background picker without leaving the `/ai` route.

#### Scenario: Student opens picker from global Atom chat
- **WHEN** an authenticated student is on the `/ai` root assistant with the default global context
- **AND** the student activates the composer `+` action
- **THEN** the app MUST open a learning-background picker as a bottom sheet inside the Atom page
- **AND** the app MUST NOT navigate to `/search`, `/video-library`, `/ai/chat`, or any other route as part of opening the picker.

#### Scenario: Student dismisses picker without selecting
- **WHEN** the learning-background picker is open
- **AND** the student dismisses the sheet without choosing a point
- **THEN** the Atom root assistant MUST keep the existing active context unchanged
- **AND** the composer MUST remain usable for direct global free-form asking.

### Requirement: Picker sheet preserves Atom context and mobile geometry
The Atom learning-background picker SHALL render as a half-height bottom sheet that keeps the underlying Atom assistant identity visible and remains usable with the mobile keyboard.

#### Scenario: Picker opens without keyboard
- **WHEN** the picker is opened on a common mobile viewport
- **THEN** the sheet MUST use the Atom history-sheet height baseline of `min(72dvh, 640px)` or an equivalent bounded height
- **AND** the sheet MUST remain bottom-anchored
- **AND** the sheet MUST leave the Atom root title/header area readable above it.

#### Scenario: Picker search field receives focus
- **WHEN** the picker search field is focused and the soft keyboard changes the visual viewport
- **THEN** the picker MUST keep its search field visible above the keyboard
- **AND** the picker body MUST resize or scroll internally rather than covering the Atom title/header area.

#### Scenario: Picker renders on narrow phones
- **WHEN** the picker renders at 360px, 390px, or 430px CSS-pixel widths
- **THEN** the header, body rows, search footer, selected states, and close/dismiss affordance MUST avoid horizontal overflow and vertical overlap.

### Requirement: Empty query renders catalog selection
The Atom learning-background picker SHALL render a catalog selection component while the picker search query is empty.

#### Scenario: Picker opens with empty query
- **WHEN** the picker opens and the search query is empty or whitespace
- **THEN** the picker body MUST render catalog or chapter roots as the primary selection surface
- **AND** it MUST NOT render the compact point-search result list.

#### Scenario: Student opens a directory
- **WHEN** the student selects a directory row in empty-query mode
- **THEN** the picker MUST load and display that directory's child catalog entries within the same picker
- **AND** the app MUST NOT prefetch every descendant point in the full catalog tree.

#### Scenario: Student sees point rows in catalog mode
- **WHEN** a catalog layer contains point nodes
- **THEN** the picker MUST render those point nodes as selectable learning-background rows
- **AND** directory rows MUST remain navigational rather than bindable point contexts.

### Requirement: Non-empty query renders compact point search
The Atom learning-background picker SHALL render a compact bindable point-search list whenever the picker search query contains non-whitespace text.

#### Scenario: Student types in picker search
- **WHEN** the student enters a non-empty query in the picker search field
- **THEN** the picker body MUST switch from catalog selection to compact point-search results
- **AND** the picker MUST search student-visible experiment point learning content using the existing video-library search capability or an equivalent shared frontend helper.

#### Scenario: Search results render in picker
- **WHEN** point-search results are available
- **THEN** each bindable result row MUST show the point title, concise catalog path or direct parent context, and a short student-facing snippet or summary
- **AND** result rows MUST avoid thumbnails, autoplay previews, large cards, and full video-library page chrome.

#### Scenario: Search result is not bindable
- **WHEN** a search response item cannot be mapped to a concrete student-visible point placement
- **THEN** the picker MUST omit it from the bindable result list or render it as non-selectable context
- **AND** selecting it MUST NOT bind a directory-only or unsupported context as the chat point.

### Requirement: Picker binds one point to current chat
The Atom learning-background picker SHALL bind at most one concrete point placement to the current Atom chat, whether the chat is on `/ai` or `/ai/chat`.

#### Scenario: Student selects a point
- **WHEN** the student selects a point from catalog mode or search mode
- **THEN** the picker MUST close
- **AND** the current Atom chat MUST receive an `AssistantContext` for that selected point
- **AND** the context MUST include the best available point title, summary, chapter identity, point placement identity, source node identity, experiment or canonical point identity, and catalog path.

#### Scenario: Student replaces selection before first send
- **WHEN** a point is selected but the current Atom chat has no submitted user message
- **AND** the student selects a different point through the picker
- **THEN** the current Atom chat MUST replace the previous selected point context with the new selected point context.

#### Scenario: Student attempts replacement after first send
- **WHEN** the current Atom chat has submitted at least one user message with a selected point context
- **THEN** the picker MUST NOT silently replace the bound point inside the same chat
- **AND** the UI MUST require starting a new chat before binding a different point.

#### Scenario: Student sends without selecting
- **WHEN** the student submits a question without selecting a point
- **THEN** the assistant request MUST continue to use the current global or restored active context
- **AND** the app MUST NOT require point selection before asking.

### Requirement: Bound point displays as learning-background chip
The Atom assistant SHALL display the selected point as an attachment-like learning-background chip near the composer across full-control Atom routes.

#### Scenario: Point selected before first send
- **WHEN** the current Atom chat has a selected point and no submitted user message
- **THEN** the composer area MUST show a visible selected-point chip
- **AND** the chip MUST include the selected point title and concise path or context cue when space allows
- **AND** the chip MUST expose remove or replace affordance.

#### Scenario: Bound chat has messages
- **WHEN** the current Atom chat has at least one submitted user message with a selected point context
- **THEN** the selected-point chip MUST remain visible as the chat's bound learning background
- **AND** the chip MUST no longer allow silently changing or removing the bound point inside the same chat.

#### Scenario: Student starts a new Atom chat
- **WHEN** the student activates the new-chat action from a full-control Atom route
- **THEN** the visible conversation, composer draft, active local history id, and selected-point binding MUST reset according to that route's initial context policy
- **AND** existing local history entries MUST remain available.

### Requirement: Atom detail plus opens learning-background picker
The student H5 Atom assistant SHALL allow the focused `/ai/chat` composer to open the same learning-background picker used by the Atom root composer.

#### Scenario: Student opens picker from focused detail chat
- **WHEN** an authenticated student is on `/ai/chat`
- **AND** the current chat has no submitted user message or otherwise allows context replacement
- **AND** the student activates the composer context action
- **THEN** the app MUST open the learning-background picker as a bottom sheet inside the focused Atom page
- **AND** the app MUST NOT navigate to `/search`, `/video-library`, `/ai`, or any other route as part of opening the picker.

#### Scenario: Detail picker dismisses without selecting
- **WHEN** the learning-background picker is open on `/ai/chat`
- **AND** the student dismisses the sheet without choosing a point
- **THEN** the current Atom chat MUST keep the existing active context unchanged
- **AND** the composer MUST remain usable for free-form asking.

#### Scenario: Detail picker respects route chrome
- **WHEN** the learning-background picker opens on `/ai/chat`
- **THEN** the detail route MUST continue hiding the bottom navigation
- **AND** the picker MUST remain keyboard-safe and internally scrollable without covering the route's required back affordance or Atom identity area.

### Requirement: Picker initializes from current Atom context
The Atom learning-background picker SHALL make the current selected context visible when the picker is opened for replacement or review.

#### Scenario: Picker opens with selected point context
- **WHEN** the picker opens and the current Atom chat has a selected point context that can be represented in catalog or search data
- **THEN** the picker SHOULD navigate to or highlight the matching row
- **AND** the selected row SHOULD use a subtle Atom-green treatment that distinguishes it from ordinary rows.

#### Scenario: Current context is not present in loaded picker data
- **WHEN** the picker opens and the current selected context cannot be represented in the currently loaded catalog/search data
- **THEN** the picker MUST still render normally
- **AND** absence of a highlighted row MUST NOT clear or replace the current chat context.

