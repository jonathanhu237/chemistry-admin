# student-h5-ai-assistant Specification

## Purpose
Define the student H5 AI chat surfaces, including direct composer-first root chat, contextual detail chat, optional starter behavior, unsupported-control boundaries, and local conversation history.
## Requirements
### Requirement: Mobile assistant starter surface
The student H5 AI root SHALL prioritize a direct mobile chat composer before any structured starter surface; starter prompts, if present, SHALL be secondary and MUST NOT block free-form asking.

#### Scenario: Student opens global assistant with no prior messages
- **WHEN** an authenticated student opens the `/ai` root with the default `learning_home` context and no chat turns
- **THEN** the app MUST render a mobile chat shell with a visible free-form composer
- **AND** the page MUST NOT require the student to choose a starter prompt, point, or intent before asking.

#### Scenario: Optional starter appears without occupying the primary flow
- **WHEN** optional starter prompts or question directions are shown before the first turn
- **THEN** they MUST remain visually secondary to the free-form composer
- **AND** they MUST NOT reoccupy the entire chat area after the first sent question.

#### Scenario: Starter copy stays student-facing
- **WHEN** optional starter copy renders labels, descriptions, status, or preview text
- **THEN** the copy MUST use student-facing learning language
- **AND** it MUST NOT expose teacher/admin diagnostics, policy codes, raw retrieval traces, or implementation jargon.

### Requirement: Starter intent choices
When the student H5 assistant exposes compact learning-intent choices inspired by the teacher learning assistant, those choices SHALL remain optional secondary controls that preserve direct free-form asking.

#### Scenario: Optional structured starter intents are exposed
- **WHEN** the implementation exposes optional starter intents for `learning_profile`, `catalog_profile`, `catalog_point`, or `learning_point` contexts
- **THEN** the starter surface MUST offer student-readable choices such as observation, phenomenon explanation, principle explanation, or mistake review
- **AND** it MUST include experiment design or comparison intents only when the context contains experiment or point information.

#### Scenario: Intent choice is selected
- **WHEN** the student taps an optional starter intent
- **THEN** the app MUST mark that intent as selected
- **AND** it MUST make the text that will be sent unambiguous before submission.

#### Scenario: Student chooses custom asking
- **WHEN** the student selects a custom asking intent
- **THEN** the app MUST preserve the active assistant context
- **AND** it MUST guide the student to type their own question rather than sending an empty or generic prompt.

### Requirement: Starter question preview and launch
The student H5 assistant SHALL only show starter previews when an optional structured starter is active, and the preview MUST NOT replace the direct composer as the default first-screen action.

#### Scenario: Preview is available for selected optional intent
- **WHEN** the active context and selected optional intent can produce a starter question
- **THEN** the app MUST display a student-readable preview region
- **AND** the preview MUST include the relevant context title or point title when available.

#### Scenario: Student launches optional starter question
- **WHEN** the student activates the optional starter launch action
- **THEN** the app MUST submit the previewed question through the existing student assistant stream endpoint
- **AND** the request MUST include the active `AssistantContext` fields already used by the student assistant.

#### Scenario: Preview and composer both contain text
- **WHEN** a starter preview exists and the student has also typed free-form input
- **THEN** the app MUST make the sent text unambiguous
- **AND** it MUST either send the typed input with the active context or clearly label separate actions for sending the preview versus the typed input.

### Requirement: Active context header
The student H5 assistant SHALL make active contextual chat understandable and dismissible without duplicating separate "current content" cards on the first screen.

#### Scenario: Global context is active
- **WHEN** the assistant context is the default `learning_home`
- **THEN** the root chat shell MUST identify the assistant as a global course Q&A entry
- **AND** it MUST avoid implying that a chapter, experiment, or point is bound.

#### Scenario: Learning or catalog context is active
- **WHEN** the assistant context is provided by a chapter, catalog profile, catalog point, point handoff, video result, or assessment report
- **THEN** the contextual chat shell MUST show the context title and a concise context type cue
- **AND** the subsequent assistant request MUST include available `chapter_id`, `experiment_id`, `point_key`, and `context_summary` values.

#### Scenario: Student clears context
- **WHEN** the student activates the context clear action
- **THEN** the app MUST return to the default `learning_home` assistant context
- **AND** the UI MUST make clear whether existing chat turns were preserved or a new global chat state was started.

### Requirement: Optional experiment starter data
The student H5 assistant SHALL remain useful without loading optional experiment starter data in the global AI root.

#### Scenario: Experiment starter data is not loaded
- **WHEN** the global AI root opens before experiment starter data is available or if an experiment request fails
- **THEN** the direct chat composer MUST remain usable
- **AND** student asking MUST NOT be blocked on experiment data loading.

#### Scenario: Experiment module starter is exposed later
- **WHEN** a later implementation exposes an optional experiment-question path using student-visible modules
- **THEN** the starter MUST load those modules through existing student APIs
- **AND** it MUST NOT introduce a new backend starter-suggestion contract unless a later change explicitly adds one.

### Requirement: Grok-like root assistant visual target
The student H5 `AI` root SHALL learn the provided Grok-style mobile chat target's layout grammar and sizing rhythm while remaining a bright static chemistry-course interface.

#### Scenario: Root assistant fills available phone space
- **WHEN** the `AI` root renders at 360px to 430px CSS-pixel phone widths
- **THEN** the assistant surface MUST occupy the available route width and height without appearing as a floating card
- **AND** the `/ai` root MUST NOT render the normal fixed root-page `StudentAppHeader` above the assistant surface
- **AND** the route content and root assistant panel MUST begin at the top of the student page frame while still respecting safe-area and bottom-navigation constraints
- **AND** the chat composer MUST remain above the bottom navigation with visible separation.

#### Scenario: Root layout follows Grok vertical rhythm
- **WHEN** the root assistant first screen renders with no messages
- **THEN** the screen MUST use a light top bar, a large calm middle space, and bottom-weighted interaction area
- **AND** the empty first screen SHOULD show the Atom AI identity pictogram centered above the welcome line `从一个实验开始吧！`
- **AND** the welcome group MUST NOT include a card frame, subtitle, or explanatory copy
- **AND** the middle of the screen MUST remain mostly open rather than filled with cards, grids, explanations, or prompt stacks
- **AND** root chat shortcuts, if introduced later, MUST use compact low-position chips rather than large centered cards.

#### Scenario: Root assistant top identity is lightweight
- **WHEN** the root assistant first screen renders
- **THEN** the top identity area MUST render as a minimal chat-app title bar centered on `Atom 学习助手`
- **AND** the history and new-chat actions MUST appear as compact icon-only actions near the top-right of the chat surface and inline with the title row
- **AND** those actions MUST blend into the assistant background rather than appearing as framed cards
- **AND** the title row SHOULD stay close to a 52px to 56px visual height on common phone widths
- **AND** the root top identity MUST NOT show the previous `课程 AI` label, duplicated context title, global-course description, or explanatory summary block
- **AND** the identity area MUST NOT become a framed intro card.

#### Scenario: Static learning-page background is used
- **WHEN** the root assistant idle surface renders
- **THEN** it SHOULD use a near-white paper-like static background inspired by the student learning pages
- **AND** the background glow SHOULD reuse the student learning pages' warm paper, pale yellow-green, and light sage-green language rather than introducing a cold Tiffany or blue-mint wash
- **AND** the root assistant MUST NOT render animated star, particle, meteor, or canvas background effects
- **AND** the static background MUST sit behind all interactive content and not block scrolling, typing, sending, history, new-chat, or bottom navigation controls.

#### Scenario: Context description is not duplicated on root
- **WHEN** the root assistant first screen renders with no messages
- **THEN** the page MUST NOT show a separate fixed header or descriptive intro section above the empty chat surface
- **AND** the root assistant MAY show the Atom AI identity pictogram above the single centered welcome line `从一个实验开始吧！`
- **AND** the root assistant MUST NOT show a first-screen starter prompt card or explanatory copy block above the composer.

#### Scenario: Student starts a new root chat
- **WHEN** the student activates the root top-bar new-chat action
- **THEN** the root chat shell MUST clear the visible conversation turns and composer state
- **AND** it MUST return to the default global `learning_home` assistant context
- **AND** it MUST NOT delete existing local history entries.

#### Scenario: Unsupported controls are absent
- **WHEN** the root assistant composer renders
- **THEN** the composer MUST expose only supported text-entry and send controls
- **AND** it MUST NOT show upload, attachment, model picker, microphone, voice waveform, image generation, or external X/Grok controls.

#### Scenario: Root composer prompt matches experiment learning
- **WHEN** the root assistant composer renders before the student types
- **THEN** the placeholder SHOULD read `问实验现象、步骤或原理`
- **AND** the placeholder MUST NOT use generic open-chat phrasing such as `随便问点什么`
- **AND** contextual detail assistant routes SHOULD use a separate current-content placeholder rather than the root experiment-starting placeholder.

#### Scenario: Send action is embedded in composer
- **WHEN** the root assistant composer renders
- **THEN** the send action MUST sit visually inside the composer container rather than as a separate external button beside it
- **AND** the composer MUST read as a single rounded bottom chat capsule with a larger vertical presence than a standard form field
- **AND** the root composer SHOULD target approximately 82px minimum height and a large rounded radius near 24px on common phone widths
- **AND** the root composer SHOULD follow the reference page's spacing rhythm by using approximately 12px side margins from the phone surface and a compact 34px circular send action aligned to the bottom-right inside the capsule
- **AND** the composer MUST still expose a clear text input area and one supported send action.

#### Scenario: Root composer text-entry state replaces the empty welcome
- **WHEN** the root assistant has no messages and the student has not entered text
- **THEN** the Atom welcome pictogram and welcome phrase MAY occupy the empty chat stream
- **WHEN** the student enters non-whitespace text into the root composer
- **THEN** the textarea placeholder MUST disappear through normal textarea behavior
- **AND** the Atom welcome group MUST disappear until the input is cleared or a new empty root chat is started.

#### Scenario: Root composer grows before becoming scrollable
- **WHEN** the student enters multi-line text in the root assistant composer
- **THEN** the input capsule SHOULD grow upward with the content while the textarea's natural content height is at or below approximately `61.8%` of the effective chat panel height
- **AND** the embedded send action MUST remain reachable inside the capsule
- **WHEN** the natural content height would exceed approximately `61.8%` of the effective chat panel height
- **THEN** the input capsule MUST stop growing
- **AND** the textarea content MUST scroll vertically inside the capsule instead of expanding the page or hiding behind the soft keyboard.

### Requirement: Root AI chat history entry
The student H5 AI root and focused Atom detail routes SHALL provide a history entry point for reviewing prior student AI conversations without requiring backend chat-session storage.

#### Scenario: Student opens history from AI root
- **WHEN** an authenticated student opens the `/ai` root route
- **THEN** the page MUST show a student-readable history action in the Atom chat top area
- **AND** activating the action MUST open a history list, panel, or sheet without leaving the AI root route.

#### Scenario: Student opens history from focused detail chat
- **WHEN** a student opens the contextual `/ai/chat` detail route
- **THEN** the page MUST show the same student-readable Atom history action
- **AND** activating the action MUST open the local Atom history list without promoting the route into the `/ai` root tab.

#### Scenario: Student restores history on either Atom route
- **WHEN** the student selects a local history entry from the Atom history list on `/ai` or `/ai/chat`
- **THEN** the current Atom surface MUST restore the saved conversation turns and saved active context
- **AND** follow-up questions MUST send recent restored turns as `conversation_history`.

### Requirement: First-round local conversation history
The student H5 AI chat SHALL persist first-round conversation history in client-side browser storage without requiring a backend chat-session migration.

#### Scenario: Root chat is saved
- **WHEN** a student sends a question from the `/ai` root chat shell
- **THEN** the app MUST create or update a local history entry for that conversation
- **AND** the entry MUST include enough information to restore visible user and assistant turns.

#### Scenario: Contextual detail chat is saved and restorable
- **WHEN** a student sends a question from `/ai/chat`
- **THEN** the app MUST create or update a local history entry in the same Atom history store
- **AND** the entry MUST include enough saved context to restore the context chip, visible turns, and follow-up request behavior.

#### Scenario: Student restores a local history entry
- **WHEN** a student selects a history entry from the Atom history list
- **THEN** the current Atom chat shell MUST restore the saved conversation turns
- **AND** follow-up questions MUST send recent restored turns as `conversation_history`.

#### Scenario: No local history exists
- **WHEN** the student opens the history panel and no local conversations are available
- **THEN** the app MUST show an empty state that explains there are no recent AI conversations
- **AND** the student MUST be able to return to the current Atom composer.

### Requirement: History rows identify context
The student H5 AI history SHALL identify whether a conversation was global or contextual without exposing teacher/admin diagnostics.

#### Scenario: History row comes from global root chat
- **WHEN** a history entry was created from the `/ai` root route
- **THEN** the row MUST label it as a global course assistant conversation or equivalent student-facing copy.

#### Scenario: History row comes from contextual chat
- **WHEN** a history entry was created from a point, chapter, video result, or assessment context
- **THEN** the row MUST show a concise context title or context type cue
- **AND** it MUST NOT expose raw RAG traces, policy codes, internal node diagnostics, or admin-only metadata.

### Requirement: Dynamic follow-up prompts
The student H5 Atom assistant SHALL display model-generated follow-up prompts only for the latest successful assistant turn.

#### Scenario: Successful answer returns follow-up prompts
- **WHEN** the student assistant stream emits a successful `final` event for a completed answer
- **THEN** the final response MAY include `suggested_prompts` as an array of student-facing follow-up questions
- **AND** the H5 app MUST store those suggestions on that assistant turn's metadata
- **AND** the H5 app MUST render the suggestions in the quick prompt row when at least one valid suggestion is present.

#### Scenario: Suggestions are absent
- **WHEN** a successful `final` event does not include valid `suggested_prompts`
- **THEN** the H5 app MUST NOT render static fallback prompt chips for that turn
- **AND** the chat composer MUST remain usable for free-form student input.

#### Scenario: Turn is still streaming
- **WHEN** a student sends a question and the assistant turn is loading or streaming
- **THEN** the H5 app MUST hide any previous quick prompt suggestions
- **AND** it MUST NOT show new suggestions until the current turn receives a successful `final` event.

#### Scenario: Assistant turn fails
- **WHEN** the student assistant stream emits an `error` event or the frontend catches a failed assistant request
- **THEN** the H5 app MUST show no follow-up prompt chips for that failed turn
- **AND** stale suggestions from previous successful turns MUST remain hidden.

#### Scenario: New successful turn replaces previous suggestions
- **WHEN** a later assistant turn completes successfully with valid `suggested_prompts`
- **THEN** the quick prompt row MUST show only that latest turn's suggestions
- **AND** suggestions from earlier turns MUST NOT be accumulated, merged, or reused.

#### Scenario: Restored history has suggestions
- **WHEN** the student restores a local chat history entry whose latest assistant turn includes valid `suggested_prompts`
- **THEN** the H5 app MAY render those latest-turn suggestions
- **AND** activating a suggestion MUST submit it using the restored active context and restored visible conversation history.

### Requirement: Follow-up prompt stream contract
The student H5 assistant stream SHALL return follow-up prompts as sanitized student-only final metadata without changing the existing answer streaming contract.

#### Scenario: Backend attaches suggestions to final metadata
- **WHEN** `/api/student/assistant/ask/stream` completes a student answer successfully
- **THEN** the backend SHOULD attempt to generate follow-up prompts from the current student question, completed answer, active assistant context, and recent conversation history
- **AND** the backend MUST attach valid suggestions as `response.suggested_prompts` on the `final` event rather than as answer text.

#### Scenario: Suggestion generation fails
- **WHEN** the answer succeeds but follow-up suggestion generation fails, times out, returns malformed output, or filters to zero valid suggestions
- **THEN** the backend MUST still send the successful answer final event
- **AND** the backend MUST omit `suggested_prompts` or send it as an empty array
- **AND** the frontend MUST render no quick prompt chips for that turn.

#### Scenario: Suggestion count is sanitized
- **WHEN** the model returns follow-up suggestions
- **THEN** the backend MUST keep at most five valid suggestions
- **AND** the backend MAY return fewer than three suggestions when only one or two valid suggestions remain after filtering
- **AND** the frontend MUST display any valid suggestions returned by the backend.

#### Scenario: Suggestion text is sanitized
- **WHEN** a model-generated follow-up suggestion is evaluated for display
- **THEN** the backend MUST trim whitespace, remove empty values, remove duplicates, and reject suggestions outside the 8-24 visible-character range
- **AND** the backend MUST reject values that are not plain student-facing question strings.

#### Scenario: Static context prompts no longer drive post-turn chips
- **WHEN** a chat turn has started or completed
- **THEN** the H5 app MUST NOT render post-turn quick prompt chips from frontend-authored `AssistantContext.prompts`
- **AND** any retained `AssistantContext.prompts` field MUST NOT override latest-turn model-generated suggestions.

#### Scenario: Student activates a generated suggestion
- **WHEN** the student taps a displayed follow-up suggestion
- **THEN** the H5 app MUST submit the suggestion text through the existing student assistant stream path
- **AND** the request MUST include the current active assistant context and recent conversation history exactly as a manually typed follow-up would.

### Requirement: Root composer has a fixed workbench zone
The student H5 Atom root composer SHALL separate text entry from a fixed composer workbench for supported chat actions.

#### Scenario: Compact composer renders before multi-line input
- **WHEN** the `/ai` root assistant renders with no composer text or with text that fits in one visual line
- **THEN** the composer MUST retain a compact race-track capsule appearance
- **AND** the composer MUST show a left-side background-knowledge `+` action and a right-side send action inside the same composer surface
- **AND** the text entry lane MUST remain usable between those actions
- **AND** placeholder or typed text MUST be vertically centered on the same visual row as those actions.

#### Scenario: Composer expands for multi-line input
- **WHEN** the student enters text that no longer fits in the compact one-line lane
- **THEN** the composer MUST transition to an expanded rounded-rectangle state
- **AND** the textarea MUST occupy an upper input zone
- **AND** the `+` action and send action MUST occupy a lower workbench zone inside the composer.

#### Scenario: Expansion threshold uses compact lane width
- **WHEN** the student enters boundary-length text that wraps in the compact race-track text lane
- **THEN** the composer MUST remain expanded even if the same text would fit on one line in the wider expanded textarea zone
- **AND** the composer MUST NOT oscillate between compact and expanded modes because the current rendered textarea width changed.

#### Scenario: Single-character input remains compact
- **WHEN** the student enters a single visible character into the root Atom composer
- **THEN** the composer MUST remain in the compact race-track state
- **AND** any hidden compact measurement textarea MUST mirror the visible compact textarea's one-row configuration rather than using the browser's multi-row default.

#### Scenario: Text cannot occupy the workbench
- **WHEN** the composer is expanded or internally scrollable
- **THEN** typed text MUST NOT overlap, push, resize, or visually occupy the workbench zone
- **AND** the workbench zone MUST remain reserved for composer actions.

### Requirement: Composer workbench controls remain position-invariant
The student H5 Atom composer SHALL keep workbench actions visually anchored across composer states.

#### Scenario: Workbench action positions are stable
- **WHEN** the composer changes between compact, expanded, scrollable, keyboard-active, and loading states
- **THEN** the left-side `+` action MUST remain visually anchored to the left side of the workbench
- **AND** the send action MUST remain visually anchored to the right side of the workbench
- **AND** neither action MUST jump vertically because the textarea content grows.

#### Scenario: Loading preserves workbench geometry
- **WHEN** the student submits a question and the assistant turn is loading or streaming
- **THEN** the send action MAY show a loading or disabled state
- **AND** the workbench layout MUST NOT move, collapse, or change the `+` action position.

#### Scenario: Long text scrolls above the workbench
- **WHEN** the textarea's natural content height would make the outer composer exceed the configured root composer growth budget
- **THEN** the textarea MUST become internally scrollable in the upper input zone
- **AND** the lower workbench actions MUST remain visible and reachable without scrolling the composer actions away.

#### Scenario: Growth budget applies to the outer composer
- **WHEN** the root composer is expanded or scrollable
- **THEN** the combined outer composer height, including input zone, composer padding, and workbench row, MUST stay within the configured `61.8%` effective panel-height budget
- **AND** the textarea height MUST be calculated from the remaining budget after the fixed workbench row and composer padding are reserved.

### Requirement: Plus action injects background knowledge
The student H5 Atom composer SHALL treat the `+` action as a course-background knowledge affordance rather than an unsupported attachment affordance.

#### Scenario: Student activates plus with available context
- **WHEN** the student activates the composer `+` action and the current assistant context has available learning background such as video-point, catalog-point, experiment, assessment-report, or page context
- **THEN** the app MUST expose or apply that background knowledge as context for the next assistant turn
- **AND** the interaction MUST communicate that the action is about learning context or background knowledge.

#### Scenario: Plus does not imply uploads
- **WHEN** the root composer renders the `+` action
- **THEN** the app MUST NOT present the action as file upload, attachment selection, image selection, model selection, microphone input, or voice input
- **AND** the action MUST NOT introduce unsupported upload or attachment controls.

#### Scenario: No background context is available
- **WHEN** the student activates the `+` action and no usable background knowledge is available
- **THEN** the app MUST keep the composer usable for free-form text input
- **AND** the app MUST NOT block sending a manually typed question.

### Requirement: Composer workbench preserves existing Atom chat states
The student H5 Atom composer workbench SHALL preserve the existing root and contextual chat behavior while changing the composer internals.

#### Scenario: Empty welcome behavior remains
- **WHEN** the root assistant has no messages and no non-whitespace composer text
- **THEN** the Atom welcome group MAY remain visible according to the existing empty-state rules
- **AND** introducing the workbench MUST NOT force the welcome group to disappear before the student enters text.

#### Scenario: Typed text still clears root welcome
- **WHEN** the student enters non-whitespace text into the root composer
- **THEN** the root welcome group MUST disappear according to the existing text-entry rule
- **AND** the composer workbench MUST remain visible.

#### Scenario: Contextual chat remains distinct
- **WHEN** a student opens contextual `/ai/chat` from another page
- **THEN** the contextual route MUST preserve its detail-route navigation and context behavior
- **AND** root-only history or new-chat affordances MUST NOT appear because of the composer workbench change
- **AND** any reused workbench layout MUST NOT erase the distinction between root and contextual chat.

#### Scenario: Follow-up prompt chips remain outside composer workbench
- **WHEN** model-generated follow-up prompt chips are displayed after a successful assistant turn
- **THEN** those chips MUST remain post-turn prompt suggestions outside the pre-send composer workbench
- **AND** they MUST NOT move into, resize, or replace the `+` and send workbench actions.

### Requirement: Conversational body typography is consistent
The student H5 Atom chat SHALL use one shared body typography treatment for the primary reading and writing surfaces.

#### Scenario: Root text entry matches message body
- **WHEN** the root Atom composer renders placeholder text or typed student text
- **THEN** that root textarea body text MUST use the same font family, font size, line-height, font weight, and letter spacing as chat message body text.

#### Scenario: Markdown body matches message body
- **WHEN** assistant Markdown paragraphs or list items render inside a message bubble
- **THEN** those paragraph and list body lines MUST use the same font family, font size, line-height, font weight, and letter spacing as plain message body text.

#### Scenario: Supporting labels keep their hierarchy
- **WHEN** titles, status badges, metadata labels, quick prompt chips, history labels, or inline code render
- **THEN** they MAY use their existing specialized typography
- **AND** the body typography unification MUST NOT flatten those supporting hierarchy levels.

### Requirement: Root assistant header uses an integrated gradient veil
The student H5 Atom root assistant SHALL render its title row as a root-only translucent overlay whose own background veil fades from a more protective top edge to a transparent lower edge.

#### Scenario: Empty root assistant shows translucent title chrome
- **WHEN** an authenticated student opens the `/ai` root with no visible chat turns
- **THEN** the top title row MUST render `Atom 学习助手` as fully opaque foreground text
- **AND** the title row MUST use a transparent gradient veil as its background layer
- **AND** the veil MUST be part of the header itself rather than a separate extra region below the header
- **AND** the veil MUST fade to transparent at the lower edge so the root assistant canvas remains visually continuous.

#### Scenario: Content exists behind the root header
- **WHEN** root assistant messages, restored history, or the empty welcome group occupy the root chat stream
- **THEN** the stream content MUST be able to visually pass behind the root header overlay during scroll or layout
- **AND** the header veil MUST soften the underlying content near the title row instead of blocking it with a hard opaque header background
- **AND** the header title and root action controls MUST remain readable above that underlying content.

#### Scenario: Header veil does not duplicate the page background
- **WHEN** the root assistant header renders over the root assistant canvas
- **THEN** the header MUST NOT copy the root panel's radial-gradient glow background or any full page background stack into the header
- **AND** the root assistant's warm paper, pale yellow-green, and sage-green canvas background MUST continue to be painted by the root assistant canvas as the single source of background truth
- **AND** the header veil MUST be a simple semi-transparent tint or gradient layer that has no independent glow alignment requirement.

#### Scenario: Header foreground remains fully opaque
- **WHEN** the root assistant header renders its title and actions
- **THEN** the implementation MUST NOT use whole-header opacity that fades the title, icons, hit targets, or action capsule
- **AND** any veil, pseudo-element, mask, or similar background layer MUST be layered behind the title and actions.

#### Scenario: Header veil uses alpha gradient rather than blur
- **WHEN** the root assistant header overlays scrollable chat content
- **THEN** the veil MUST make underlying content progressively less visible toward the top through translucent gradient opacity stops
- **AND** the primary translucency effect MUST NOT rely on `backdrop-filter`, blur, or whole-header opacity
- **AND** the foreground title and action capsule MUST remain sharp and fully opaque.

### Requirement: Root assistant actions use one protected capsule
The student H5 Atom root assistant SHALL protect its root-only history and new-chat actions with one compact capsule while keeping the actions visually lightweight.

#### Scenario: Root actions render in one capsule
- **WHEN** the `/ai` root assistant header renders
- **THEN** the history action and new-chat action MUST sit inside a single rounded capsule with a real local background
- **AND** each action MUST occupy one half of the capsule's visual width
- **AND** the capsule MUST align with the title row rather than appearing as two separate cards.

#### Scenario: Action capsule preserves existing behavior
- **WHEN** the student activates the history half of the capsule
- **THEN** the app MUST open the existing root chat history UI without leaving the AI root route
- **WHEN** the student activates the new-chat half of the capsule
- **THEN** the app MUST preserve the existing new root chat behavior
- **AND** the visual capsule change MUST NOT alter local history storage, restored conversation turns, or assistant request payloads.

#### Scenario: Contextual chat does not inherit root capsule
- **WHEN** a student opens the contextual `/ai/chat` detail route from another page
- **THEN** the contextual chat page MUST NOT render the root history/new-chat capsule
- **AND** contextual detail header/navigation behavior MUST remain distinct from the root assistant overlay.

### Requirement: Root header veil preserves established Atom chat states
The student H5 Atom root header veil SHALL coexist with the established root welcome, composer, keyboard-aware layout, and conversation states without changing their state machines.

#### Scenario: Root welcome remains governed by input state
- **WHEN** the root assistant has no messages and no non-whitespace composer text
- **THEN** the Atom welcome group MUST remain governed by the existing empty-state rule
- **AND** adding the header veil MUST NOT force the welcome group to disappear
- **WHEN** the student enters non-whitespace composer text
- **THEN** the welcome group MUST still disappear according to the existing text-entry rule.

#### Scenario: Composer geometry is unchanged by header veil
- **WHEN** the root composer changes between compact, expanded, scrollable, loading, and keyboard-active states
- **THEN** the header veil change MUST NOT alter compact lane measurement, compact-to-expanded threshold, `61.8%` composer growth budgeting, workbench action placement, or internal textarea scrolling behavior.

#### Scenario: Keyboard-active layout remains stable
- **WHEN** the root composer is focused and the mobile keyboard is expected to be open
- **THEN** the bottom navigation hiding behavior, visual-viewport sizing, composer bottom breathing gap, and keyboard-active welcome positioning MUST continue to follow the existing keyboard-aware layout contract
- **AND** the header veil MUST NOT create a new top gap, bottom gap, or exposed raw page background band.

#### Scenario: Root header layout states are explicit
- **WHEN** the `/ai` root assistant renders
- **THEN** the implementation MUST distinguish empty-welcome, no-message draft, and conversation/restored-message layout states with explicit classes, data attributes, or equivalently specific selectors
- **AND** the implementation MUST NOT use one shared root stream padding rule to represent all root states
- **AND** keyboard-active styling MAY add its own modifier, but it MUST preserve the empty/draft/conversation state distinction.

#### Scenario: Empty root welcome does not inherit message scroll spacing
- **WHEN** the root assistant has no messages and no non-whitespace composer text
- **THEN** the Atom welcome group MUST keep the established empty-state placement
- **AND** the root stream MUST NOT receive conversation-only header top padding or scroll-padding
- **AND** the header overlay MUST NOT create a scrollbar, bottom compression, or downward shift in the empty welcome state
- **AND** the composer and bottom navigation MUST keep their existing anchored positions.

#### Scenario: No-message draft state hides welcome without becoming conversation layout
- **WHEN** the root assistant has no messages
- **AND** the student enters non-whitespace composer text
- **THEN** the welcome group MUST disappear according to the existing input-state rule
- **AND** the root panel MUST still reserve or protect the title/header area without adding conversation-only message scroll padding
- **AND** the composer geometry MUST remain governed by the established compact, expanded, scrollable, and keyboard-active state machine.

#### Scenario: Conversation root applies header-safe scroll spacing only to messages
- **WHEN** root assistant messages, restored history, or a running assistant turn are present
- **THEN** the root stream MUST use the conversation layout that allows content to visually pass behind the header veil
- **AND** only this conversation/restored-message state MUST add header-safe top padding, scroll-padding, or equivalent first-content spacing
- **AND** quick prompts and the root composer MUST remain in their existing bottom rows without being pushed by empty-state header spacing.

#### Scenario: Conversation root scrolls without visible desktop scrollbar chrome
- **WHEN** root assistant conversation or restored-message content exceeds the visible stream height
- **THEN** the root chat stream MUST remain internally scrollable
- **AND** desktop, iframe, or teacher-preview environments MUST NOT render a persistent visible scrollbar over the phone canvas
- **AND** hiding scrollbar chrome MUST NOT disable touch, pointer, wheel, keyboard, or programmatic scrolling
- **AND** empty-welcome and no-message draft states MUST keep their established overflow behavior.

#### Scenario: Header overlay selector wins the CSS cascade
- **WHEN** root header overlay styles override generic root layering styles
- **THEN** the root header overlay selector MUST be at least as specific as any generic root header selector that sets `position`, `z-index`, or pointer interaction
- **AND** generic root foreground-layer rules MUST NOT accidentally force `.ai-chat-head.root` back to non-overlay positioning
- **AND** regression tests MUST verify the effective scoped selector/cascade contract, not only the presence of lower-specificity declarations.

#### Scenario: Mobile viewport QA covers the header veil
- **WHEN** root assistant visual QA runs for 360px, 390px, and 430px CSS-pixel-wide phone viewports
- **THEN** the QA MUST check the empty state, at least one message state, restored-history or scroll-near-top state, and keyboard-active focused state
- **AND** each checked state MUST avoid clipped title text, unreadable actions, horizontal overflow, and hard opaque header blocking.

### Requirement: Root assistant successful replies use a flat canvas turn
The student H5 Atom root assistant SHALL render successful assistant replies as flat text turns on the root chat canvas instead of white card-style bubbles.

#### Scenario: Successful root assistant reply is not a card
- **WHEN** an authenticated student asks a question on the `/ai` root route
- **AND** Atom completes a successful assistant response
- **THEN** the assistant reply MUST render as a full-width flat content turn on the root assistant canvas
- **AND** the successful assistant reply MUST NOT use the previous white card background, bordered card shell, or card-like shadow as its primary surface
- **AND** the root canvas background MUST remain visible around the reply text
- **AND** the reply text MUST keep the established Atom chat body font family, font size, line height, font weight, and zero letter spacing.

#### Scenario: User question remains a right-aligned bubble
- **WHEN** the root conversation contains both a user question and a successful Atom reply
- **THEN** the user question MUST remain visually distinct as a right-aligned green bubble
- **AND** removing the assistant reply card MUST NOT make user messages full-width
- **AND** long user messages MUST remain constrained enough to read as user-authored bubbles.

#### Scenario: Flat reply supports long educational Markdown
- **WHEN** a successful root assistant reply contains paragraphs, headings, lists, strong text, inline code, formulas, or markdown fallback text
- **THEN** the flat reply MUST preserve readable vertical rhythm and wrapping
- **AND** the content MUST avoid horizontal overflow on common phone widths
- **AND** the reply MUST use the available text width better than the previous card layout without colliding with the phone frame, composer, or header overlay.

### Requirement: Root assistant turn actions delimit successful replies
The student H5 Atom root assistant SHALL use a lightweight action row below each successful root assistant reply as the primary turn delimiter.

#### Scenario: Successful root assistant reply shows an action row
- **WHEN** a root assistant reply reaches a successful final state
- **THEN** the reply MUST show an action row below the answer body
- **AND** the action row MUST visually separate that assistant turn from following content without reintroducing a full card shell
- **AND** the action row MUST be lower contrast than the answer text.

#### Scenario: Action row exposes behavior-backed controls
- **WHEN** the successful root assistant action row renders
- **THEN** the left side SHOULD include icon controls for positive feedback, negative feedback, and copying the assistant answer text
- **AND** every visible action control MUST have an accessible name and a phone-appropriate hit target
- **AND** controls that do not yet have behavior SHOULD be hidden or placed behind a future menu rather than rendered as misleading inactive affordances.

#### Scenario: Feedback controls are local unless backend feedback is specified
- **WHEN** the student taps positive or negative feedback for a root assistant reply
- **THEN** the first implementation MAY store that selection as local UI state only
- **AND** selecting positive feedback MUST clear negative feedback for that turn
- **AND** selecting negative feedback MUST clear positive feedback for that turn
- **AND** the implementation MUST NOT require a new backend endpoint or durable feedback schema unless a later spec explicitly defines it.

#### Scenario: Copy action copies only assistant answer text
- **WHEN** the student activates the copy action for a successful root assistant reply
- **THEN** the app MUST attempt to copy the assistant answer content
- **AND** it MUST NOT include hidden metadata, raw sources, RAG traces, system prompts, guardrail decisions, or dynamic follow-up chip text in the copied answer
- **AND** the UI SHOULD provide lightweight confirmation that copying succeeded when practical.

### Requirement: Root assistant citations stay student-safe in the action row
The student H5 Atom root assistant SHALL move successful-reply citation disclosure to the action row while preserving student-safe source privacy.

#### Scenario: Citation count appears on the action row right side
- **WHEN** a successful root assistant reply has `source_count` greater than zero or sanitized `sources` metadata with at least one item
- **THEN** the action row MUST show a right-aligned citation affordance with the safe citation count
- **AND** the citation affordance MUST remain visually secondary to the answer body
- **AND** it MUST align with the action row rather than occupying a separate card section.

#### Scenario: Raw source fields are not exposed
- **WHEN** root assistant metadata includes `sources`, raw RAG traces, chunk identifiers, source titles, source sections, scores, tool calls, or guardrail details
- **THEN** the root reply action row MUST NOT expose raw source titles, sections, scores, chunk IDs, RAG trace details, tool-call internals, teacher-only metadata, or guardrail internals
- **AND** existing student role-boundary protections MUST continue to reject direct rendering of raw source fields in the student assistant panel.

#### Scenario: Citation affordance is hidden when no sources exist
- **WHEN** a successful root assistant reply has no positive safe citation count
- **THEN** the action row MUST omit the citation affordance
- **AND** omitting citations MUST NOT disturb the left-side action cluster alignment.

### Requirement: Root assistant dynamic chips remain latest-successful next-turn suggestions
The student H5 Atom root assistant SHALL preserve dynamic follow-up chip behavior while adapting their placement to the flat reply surface.

#### Scenario: Chips appear after the latest successful assistant turn
- **WHEN** the latest root assistant response completes successfully with sanitized `suggested_prompts`
- **THEN** the dynamic chips MUST render after that reply's action row and before the composer
- **AND** the chips MUST be visually understood as next-turn suggestions rather than metadata inside the answer body.

#### Scenario: Older suggestions are ignored
- **WHEN** the conversation contains multiple prior successful root assistant replies with suggested prompts
- **THEN** only the latest successful assistant reply's sanitized suggestions MUST be considered for visible chips
- **AND** older assistant suggestions MUST NOT remain visible once a newer successful assistant reply has completed.

#### Scenario: Chips remain hidden during loading and error states
- **WHEN** Atom is streaming a root assistant reply
- **THEN** dynamic chips MUST be hidden or disabled according to the established loading behavior
- **WHEN** the latest root assistant turn fails
- **THEN** dynamic chips MUST remain hidden
- **AND** a failed turn MUST NOT reuse the previous successful reply's suggestions.

### Requirement: Root flat replies preserve assistant state semantics
The student H5 Atom root assistant SHALL keep running and failed assistant states clear while successful replies use the flat turn model. Root running turns SHALL display the best available authentic visible thinking message from the stream: model reasoning summary first, real agent execution trace second, and legacy normalized status only as compatibility fallback.

#### Scenario: Running root assistant turn uses authentic visible thinking when available
- **WHEN** Atom is generating a root assistant response on the `/ai` root route
- **AND** the student assistant stream emits a valid `thinking` event
- **THEN** the root running line MUST display the sanitized `thinking.message`
- **AND** it MUST prefer that message over locally preset labels such as `正在生成回答`
- **AND** it MUST NOT append the thinking message to the answer body
- **AND** streaming answer text MUST remain readable on the root canvas.

#### Scenario: Model reasoning summary drives the running line
- **WHEN** a `thinking` event arrives with `source` equal to `reasoning_summary`
- **THEN** the root running line MUST treat the event message as the current visible thinking text
- **AND** the UI MUST NOT relabel it as a generic phase while it remains the latest valid thinking message
- **AND** the UI MUST NOT show raw source labels, provider names, model names, or debugging metadata beside the student-facing text.

#### Scenario: Agent trace fallback remains honest
- **WHEN** a `thinking` event arrives with `source` equal to `agent_trace`
- **THEN** the root running line MUST display the sanitized trace message as truthful agent progress
- **AND** the UI MUST NOT present the trace fallback as model chain-of-thought
- **AND** the displayed message MUST remain student-facing rather than diagnostic.

#### Scenario: Legacy status remains fallback
- **WHEN** Atom is generating a root assistant response and no valid `thinking` event has arrived for the active turn
- **THEN** the root running line MUST continue to derive a concise student-facing fallback label from the existing stream `status` and answer presence
- **AND** the fallback MUST use existing normalized labels such as judging scope, retrieving course material, returning learning suggestions, or generating an answer
- **AND** the UI MUST NOT expose raw backend policy wording, RAG labels, provider connection details, exception text, or implementation-specific status strings as the normal running label.

#### Scenario: Answer text does not erase fresh reasoning summary
- **WHEN** the active assistant turn receives streamed answer text through `delta`, `replace`, or equivalent response state
- **AND** the latest valid visible thinking message came from `reasoning_summary`
- **THEN** the root running line SHOULD keep the reasoning-summary message until a newer valid thinking event, final completion, or error replaces it
- **AND** the UI MUST NOT automatically overwrite it with generic `正在生成回答` solely because answer text exists.

#### Scenario: Thinking text changes preserve fade-through behavior
- **WHEN** the displayed root thinking text changes from one valid visible thinking message to another while the assistant turn is still running
- **THEN** the text MUST continue to use the established fade-through transition where the previous message fades away before the next message becomes visually prominent
- **AND** the transition MUST be keyed to actual displayed-message changes rather than a continuous timer
- **AND** the root running turn MUST preserve stable line height and avoid vertical jumping during replacement.

#### Scenario: Root running turn remains flat
- **WHEN** Atom is generating a root assistant response on the `/ai` root route
- **THEN** the active assistant turn MUST render on the root canvas as a flat full-width turn
- **AND** the active assistant turn MUST NOT use a white assistant card background, bordered card shell, card-like shadow, rounded loading card, skeleton block, or filled progress pill as its primary surface
- **AND** the active assistant turn MUST NOT render the repeated assistant meta row containing `Atom 学习助手` and `生成中`
- **AND** the active assistant turn MUST NOT render the successful-reply action row while it is still running
- **AND** the root canvas background MUST remain visible around the running turn.

#### Scenario: Running line remains accessible
- **WHEN** the root running line displays a visible thinking message
- **THEN** assistive technology SHOULD receive a polite status update for the current displayed text
- **AND** decorative marks, dots, Lottie animation, and outgoing fade-through labels MUST NOT cause duplicate announcements
- **AND** reduced-motion preferences MUST preserve the current text while reducing or disabling movement.

#### Scenario: Successful completion removes thinking status
- **WHEN** the active root assistant turn receives a successful `final` event and is no longer loading
- **THEN** the thinking line MUST be removed from the completed assistant turn
- **AND** the completed assistant reply MUST render as the established flat markdown answer with its lightweight action row
- **AND** the completed assistant reply MUST NOT retain visible thinking text, fallback status text, `Atom 学习助手`, `生成中`, or any other running-only status header as persistent success chrome.

#### Scenario: Failed root assistant turn remains visibly bounded
- **WHEN** the latest root assistant turn fails
- **THEN** the error message MAY remain in a distinct error block or bounded error treatment
- **AND** the failed turn MUST not render the successful-reply action row
- **AND** the failed turn MUST not render dynamic follow-up chips
- **AND** the failed turn MUST not keep the running thinking line as if generation were still in progress.

#### Scenario: Quick prompt chips remain hidden during root thinking
- **WHEN** Atom is streaming a root assistant reply and the thinking line is visible
- **THEN** dynamic follow-up prompt chips MUST be hidden or disabled according to the established loading behavior
- **AND** stale suggestions from previous successful turns MUST NOT be visible beside or below the running thinking line.

#### Scenario: Contextual assistant route keeps its distinct surface
- **WHEN** a student opens the contextual `/ai/chat` detail route
- **THEN** the contextual chat page MUST NOT inherit the root-only flat successful reply styling or root-only flat thinking-line styling unless explicitly scoped by a later change
- **AND** contextual detail header, contextual reset behavior, detail-route message boundaries, and existing detail-route running state behavior MUST remain distinct from the root Atom assistant page.

### Requirement: Root assistant supports learning-background attachment action
The student H5 Atom root assistant SHALL treat the composer `+` as a supported learning-background action while preserving direct free-form asking.

#### Scenario: Root assistant composer renders plus action
- **WHEN** the `/ai` root assistant composer renders
- **THEN** the `+` action MUST be available only as a learning-background picker entry
- **AND** it MUST NOT imply generic file upload, image upload, model selection, microphone input, or unsupported external tools.

#### Scenario: Student asks globally
- **WHEN** the student submits text from the root assistant without selecting a point
- **THEN** the assistant request MUST use the existing active global or restored context
- **AND** the UI MUST NOT block submission with a required point-selection step.

#### Scenario: Student asks with selected point
- **WHEN** the student submits text from the root assistant after selecting a point background
- **THEN** the assistant request MUST use the selected point `AssistantContext`
- **AND** the user-authored question text MUST be preserved without adding visible picker text into the question field.

### Requirement: Root assistant preserves bound context across local history
The student H5 Atom root assistant SHALL preserve selected point context when saving and restoring local chat history.

#### Scenario: Bound point chat is saved
- **WHEN** a student sends the first question from a root chat with a selected point
- **THEN** the local history entry for that conversation MUST include enough context to restore the selected point title, context type, ids, summary, and catalog path
- **AND** restoring the entry MUST continue sending follow-up turns with that restored point context.

#### Scenario: Global chat is saved
- **WHEN** a student sends from the root chat without selecting a point
- **THEN** the local history entry MUST remain a global Atom conversation
- **AND** restoring the entry MUST NOT show a false selected-point chip.

#### Scenario: New root chat starts from restored bound chat
- **WHEN** a restored bound-point conversation is visible
- **AND** the student activates the new-chat action
- **THEN** the root assistant MUST clear the visible conversation and selected point binding
- **AND** the new chat MUST use the default global context.

### Requirement: Root assistant communicates one-point lock
The student H5 Atom root assistant SHALL make the selected point binding understandable before and after the first submitted message.

#### Scenario: Selected point is editable before sending
- **WHEN** the root chat has a selected point and no submitted user message
- **THEN** the selected-point chip MUST communicate that this learning background will be used for the next question
- **AND** the student MUST be able to remove or replace the selected point before submitting.

#### Scenario: Selected point is locked after sending
- **WHEN** the root chat has submitted at least one user message with a selected point context
- **THEN** the selected-point chip MUST communicate that the chat is bound to that point
- **AND** the app MUST require a new chat before binding a different point.

### Requirement: Atom history generated first-turn title
The student H5 Atom assistant SHALL support an optional sanitized `conversation_title` final metadata field for first-turn local history entries while preserving the existing local fallback title behavior.

#### Scenario: First turn saves generated title
- **WHEN** a student sends the first question in an Atom conversation and the final assistant metadata includes a valid `conversation_title`
- **THEN** the app MUST save that title on the same local history entry for the conversation
- **AND** the history row MUST display the generated title instead of the raw first-question truncation.

#### Scenario: Generated title is requested only for first turn
- **WHEN** the backend prepares final metadata for an assistant response whose request has empty `conversation_history`
- **THEN** the backend MUST attempt to include a concise student-readable `conversation_title` in the final metadata
- **AND** the title MUST be based on the latest student question, completed answer, active assistant context, and safe recent metadata inputs available to the existing final-metadata generation path.

#### Scenario: Follow-up turns do not rename history
- **WHEN** a student sends a follow-up question in a restored or ongoing Atom conversation
- **THEN** the backend MUST NOT require a new `conversation_title` for that turn
- **AND** the frontend MUST keep the existing local history title unless the conversation is still using the first-turn fallback and receives a valid first-turn title for the same history entry.

#### Scenario: Missing or invalid generated title falls back
- **WHEN** the final metadata omits `conversation_title`, metadata generation fails, or the returned title is invalid
- **THEN** the app MUST keep using the existing local fallback title derived from the conversation messages
- **AND** the chat answer, history persistence, and follow-up prompts MUST continue normally.

#### Scenario: Generated title stays out of answer and request history
- **WHEN** a generated `conversation_title` is accepted for a local history entry
- **THEN** the app MUST NOT append it to visible assistant answer text, copied answer text, visible thinking, source summaries, quick prompt chips, or backend `conversation_history`
- **AND** restoring the history entry MUST continue sending only recent `{ role, content }` turns as conversation history.

#### Scenario: Legacy local history remains readable
- **WHEN** the app reads an existing local history entry that does not contain a generated title
- **THEN** the app MUST continue to render the entry with its stored title or the existing message-derived fallback
- **AND** no localStorage migration or backend chat-session record MUST be required.

### Requirement: Student assistant distinguishes streaming and completed answer rendering
The student H5 AI assistant SHALL route active and completed assistant answer content through the appropriate Markdown rendering mode while preserving the existing chat state model.

#### Scenario: Active answer turn is the only streaming Markdown turn
- **WHEN** the assistant is loading and the latest visible message is an assistant answer with non-empty content
- **THEN** only that latest assistant answer MUST use the streaming Markdown renderer
- **AND** earlier assistant answers MUST remain completed static Markdown turns
- **AND** user messages MUST remain plain user-authored chat bubbles.

#### Scenario: Final completion converts answer to stable turn
- **WHEN** the active assistant turn completes successfully
- **THEN** the visible assistant message MUST become a completed static Markdown turn
- **AND** successful root replies MUST continue using the established flat root assistant answer surface and action row
- **AND** contextual detail replies MUST continue using the established contextual assistant surface.

#### Scenario: Local history is renderer-agnostic
- **WHEN** a root or detail assistant conversation is saved to local history
- **THEN** the stored messages MUST include plain message content and supported metadata only
- **AND** stored messages MUST NOT include Streamdown component state, smooth-stream scheduler state, animation flags, Mermaid render output, or DOM-derived content.

#### Scenario: Follow-up prompt behavior is unchanged
- **WHEN** the latest assistant turn is still streaming
- **THEN** dynamic follow-up prompt chips MUST remain hidden or disabled according to existing loading behavior
- **WHEN** the turn completes successfully
- **THEN** dynamic follow-up prompt chips MUST still be derived only from the latest successful final metadata.

### Requirement: Root first-answer visual state survives modern streaming
The student H5 Atom root assistant SHALL preserve the approved first-answer background glow behavior while changing answer text rendering.

#### Scenario: First submitted root answer is waiting
- **WHEN** the `/ai` root has exactly the first user turn and an active first assistant turn waiting or streaming
- **THEN** the approved dynamic background glow MUST remain tied to the first-answer loading state
- **AND** switching the answer body to Streamdown MUST NOT prematurely remove or restart the glow.

#### Scenario: First answer completes
- **WHEN** the first root assistant answer finishes and the assistant turn becomes completed
- **THEN** the glow MUST still perform the established rapid disappearance behavior
- **AND** subsequent completed chat content MUST render on the theme background without recurring glow interference.

#### Scenario: Empty and draft root states remain static
- **WHEN** the root assistant is on the welcome screen or the student is editing the first message before submission
- **THEN** the background MUST remain in the established static state
- **AND** Streamdown or smooth-stream code MUST NOT introduce background animation before the first answer is actually waiting.

### Requirement: Assistant stream state handles smoothing without changing API semantics
The student H5 AI assistant SHALL integrate smooth answer display as frontend state only and SHALL NOT change request or response contracts.

#### Scenario: Request payload is unchanged
- **WHEN** the student submits a question after this change
- **THEN** the frontend MUST call the existing student assistant stream endpoint with the existing active `AssistantContext`, question, and `conversation_history` fields
- **AND** it MUST NOT require a new backend payload field for smoothing or renderer mode.

#### Scenario: Stream events keep existing meanings
- **WHEN** the frontend receives `status`, `thinking`, `delta`, `replace`, `final`, or `error` events
- **THEN** each event MUST keep its established semantic meaning
- **AND** smoothing MUST only affect how `delta` or replacement answer text is released to the visible answer body.

#### Scenario: User sends a follow-up after smoothed answer
- **WHEN** the student sends a follow-up after a smoothed rich Markdown answer completes
- **THEN** `conversation_history` MUST include the final plain answer text
- **AND** it MUST NOT include partially displayed text, omitted timer buffers, or rendered HTML.

#### Scenario: New chat clears active smoothing state
- **WHEN** the student activates the new-chat action or resets context
- **THEN** any active smoothing timer, raw answer buffer, display buffer, and streaming renderer state for the previous turn MUST be cleared
- **AND** the new chat MUST begin from the established empty or contextual state.

### Requirement: Student assistant rich Markdown remains mobile layout-safe
The student H5 AI assistant SHALL contain rich Markdown inside the assistant route without breaking mobile chat ergonomics.

#### Scenario: Rich answer appears on root flat canvas
- **WHEN** a root assistant answer contains tables, formulas, task lists, or Mermaid diagrams
- **THEN** the content MUST remain visually part of the flat answer turn
- **AND** it MUST not reintroduce a white card shell around the entire completed root assistant answer.

#### Scenario: Rich answer appears on contextual route
- **WHEN** a contextual assistant answer contains tables, formulas, task lists, or Mermaid diagrams
- **THEN** the content MUST remain within the contextual assistant message boundary
- **AND** it MUST not inherit root-only flat reply spacing unless explicitly scoped.

#### Scenario: Rich content reaches the bottom area
- **WHEN** a long rich Markdown answer scrolls near the composer and bottom navigation
- **THEN** tables, formula scroll containers, Mermaid containers, and plugin controls MUST not overlap the composer or bottom navigation
- **AND** the student MUST be able to continue scrolling, reading, and typing.

#### Scenario: Keyboard-active chat remains usable
- **WHEN** the soft keyboard is active while rich Markdown content exists in the conversation
- **THEN** the composer MUST remain reachable according to the existing keyboard-aware layout
- **AND** rich Markdown overflow containers MUST not steal layout height in a way that hides the input field.

### Requirement: AI table detail uses a mobile table reader
The student H5 Atom assistant SHALL render completed AI-generated Markdown table artifacts in a dedicated mobile table reader instead of a bare desktop-style grid.

#### Scenario: Student opens a completed table artifact
- **WHEN** a student opens a table artifact from a completed assistant answer
- **THEN** the app MUST show the table in the existing route-backed artifact detail flow
- **AND** the detail view MUST provide a polished mobile table reader surface with table canvas and row reading affordances.

#### Scenario: Other rich artifacts remain unchanged
- **WHEN** a student opens a Mermaid artifact from a completed assistant answer
- **THEN** the app MUST continue to use the existing Mermaid detail viewer behavior
- **AND** the table reader changes MUST NOT alter Mermaid rendering, Mermaid pan/zoom controls, or Mermaid fallback behavior.

#### Scenario: Table artifact cannot be resolved
- **WHEN** the table artifact id no longer maps to a table in the local assistant message history
- **THEN** the app MUST show the existing student-safe unavailable state
- **AND** it MUST NOT expose route internals, parser diagnostics, stack traces, or hidden artifact metadata.

### Requirement: AI table canvas supports touch exploration
The student H5 Atom assistant SHALL provide a touch-friendly canvas mode for wide AI-generated tables so students can inspect table structure on mobile screens.

#### Scenario: Student explores a wide table
- **WHEN** the table detail view contains more columns or cell width than the mobile viewport can comfortably display
- **THEN** the viewer MUST allow the student to drag or scroll within the table area to inspect offscreen cells
- **AND** the page itself MUST NOT gain horizontal document overflow.

#### Scenario: Student zooms the table canvas
- **WHEN** the student pinches the table canvas or uses explicit zoom controls
- **THEN** the viewer MUST scale the table content within the detail surface
- **AND** it MUST provide explicit controls for zoom in, zoom out, fit, and reset.

#### Scenario: Student needs table context while exploring
- **WHEN** the student pans or zooms a table in canvas mode
- **THEN** the viewer MUST preserve enough header or first-column context for the student to understand which row and column they are inspecting
- **AND** it MUST provide row reading mode as a non-transformed fallback for exact text reading.

#### Scenario: Reduced motion is enabled
- **WHEN** the device or browser indicates reduced motion preferences
- **THEN** table canvas transitions MUST avoid nonessential animation
- **AND** zoom/reset state changes MUST remain functional.

### Requirement: AI table row reading preserves chemistry Markdown
The student H5 Atom assistant SHALL let students focus a single AI table row as labeled fields while preserving the existing chemistry Markdown rendering stack.

#### Scenario: Student opens a row reader
- **WHEN** the student taps or activates a row in the table detail view
- **THEN** the viewer MUST open a focused row reading surface
- **AND** the first column value MUST be presented as the row title when available
- **AND** each remaining cell MUST be presented with its column header as the field label.

#### Scenario: Row cells contain chemistry content
- **WHEN** a row cell contains Markdown, GFM emphasis, inline math, block math, or mhchem syntax
- **THEN** the row reader MUST render that cell through the existing static AI Markdown rendering path
- **AND** formulas such as `\\ce{Cl2 + 2Br- -> 2Cl- + Br2}` MUST be readable without leaking raw renderer implementation details.

#### Scenario: Student closes the row reader
- **WHEN** the student closes the focused row reading surface
- **THEN** the viewer MUST return to the same table detail artifact
- **AND** the selected row state MUST remain local UI state only.

### Requirement: AI table detail preserves assistant answer boundaries
The student H5 Atom assistant SHALL keep enhanced table viewer state separate from assistant messages, copying, and backend conversation history.

#### Scenario: Student copies an assistant answer with a table
- **WHEN** the student copies a completed assistant answer that contains a table artifact
- **THEN** the copied content MUST be the original plain assistant Markdown answer
- **AND** it MUST NOT include table reader labels, row reader labels, route ids, row ids, zoom state, rendered HTML, or control text.

#### Scenario: Student asks a follow-up after using table detail
- **WHEN** the student opens table detail, pans or zooms the table, opens a row reader, and then asks a follow-up
- **THEN** the backend request MUST continue to send `conversation_history` as plain `{ role, content }` turns only
- **AND** it MUST NOT include table viewer state, rendered table HTML, pan/zoom transforms, or artifact metadata.

#### Scenario: Table rendering fails
- **WHEN** the enhanced table reader cannot render a parsed table
- **THEN** the app MUST show a student-safe fallback that preserves access to the original table content when possible
- **AND** it MUST NOT present development diagnostics as normal answer text.

### Requirement: AI artifact details use one canvas detail page
The student H5 Atom assistant SHALL render completed AI-generated table and Mermaid artifacts through one route-backed second-level canvas detail page model.

#### Scenario: Student opens a completed rich artifact
- **WHEN** a student opens a completed assistant answer's table or Mermaid artifact detail
- **THEN** the app MUST use the existing route-backed artifact detail flow
- **AND** the detail page MUST use the shared AI artifact canvas shell for both table and Mermaid artifact kinds
- **AND** the page title or accessible heading MUST identify whether the student is viewing a table detail or flowchart detail.

#### Scenario: Artifact detail remains a second-level destination
- **WHEN** a student is viewing an AI artifact detail page
- **THEN** the page MUST behave as a second-level/detail route
- **AND** the bottom navigation MUST remain hidden according to the existing route-stack rules
- **AND** the back action MUST return to the assistant route or history context that opened the artifact when that context is still available.

#### Scenario: Inline previews remain normal answer content
- **WHEN** a completed assistant answer contains a table or Mermaid artifact
- **THEN** the inline chat answer MUST remain readable without requiring navigation
- **AND** the inline artifact affordance MUST open the shared canvas detail page
- **AND** inline chat preview styles MUST NOT inherit the full-page canvas grid or floating detail controls.

### Requirement: AI Mermaid detail renders as a canvas object
The student H5 Atom assistant SHALL render completed Mermaid flowchart artifacts directly on the artifact canvas workspace instead of inside an inner card or framed panel.

#### Scenario: Student opens a Mermaid flowchart detail
- **WHEN** a student opens a Mermaid artifact detail from a completed assistant answer
- **THEN** the flowchart MUST render as a transparent canvas object on the detail workspace grid
- **AND** the detail view MUST NOT wrap the flowchart in an inner rounded card, bordered panel, framed preview box, or duplicated page background surface.

#### Scenario: Student explores a Mermaid flowchart
- **WHEN** the Mermaid flowchart is larger than the visible phone viewport
- **THEN** the viewer MUST allow the student to pan the canvas and zoom the flowchart with touch gestures
- **AND** the viewer MUST provide explicit controls for zoom in, zoom out, fit-to-view, and reset
- **AND** those controls MUST remain outside the transformed Mermaid SVG layer.

#### Scenario: Mermaid detail cannot render
- **WHEN** the Mermaid artifact cannot be rendered from the completed assistant Markdown
- **THEN** the detail page MUST show a student-safe fallback
- **AND** it MUST NOT expose raw exceptions, parser internals, route internals, RAG traces, guardrail details, or backend diagnostics as normal student-facing text.

### Requirement: AI table detail adapts to the canvas page
The student H5 Atom assistant SHALL render completed Markdown table artifacts inside the same AI artifact canvas detail page while preserving table readability and row reading mode.

#### Scenario: Student opens a table artifact detail
- **WHEN** a student opens a completed assistant answer's table artifact detail
- **THEN** the table MUST render inside the shared AI artifact canvas shell
- **AND** the table content MUST be placed as an artifact object on the workspace rather than inside a stretched blank card or page-filling framed panel
- **AND** the table object MUST size to useful table content instead of creating large empty table-detail space.

#### Scenario: Table content remains readable on the canvas
- **WHEN** a table contains dense Chinese text, Markdown emphasis, GFM content, KaTeX math, or mhchem chemistry syntax
- **THEN** the table detail MUST preserve readable cells, table header context, and row/column relationships
- **AND** table cell rendering MUST continue to use the existing static AI Markdown rendering path where rich chemistry content is rendered.

#### Scenario: Student reads one table row
- **WHEN** the student activates a row in the table detail page
- **THEN** the viewer MUST provide the existing focused row reading mode
- **AND** the row reader MUST remain an exact-reading surface that is not distorted by the current canvas zoom transform
- **AND** closing the row reader MUST return to the same table artifact detail page.

### Requirement: AI artifact canvas preserves assistant boundaries
The student H5 Atom assistant SHALL keep canvas detail state separate from assistant messages, copied answer text, local history content, and backend conversation history.

#### Scenario: Student copies an answer after opening artifact detail
- **WHEN** the student opens table or Mermaid detail, pans or zooms the artifact, and then copies the assistant answer
- **THEN** the copied content MUST be the original plain assistant Markdown answer
- **AND** it MUST NOT include artifact route ids, canvas labels, zoom values, pan transforms, row-reader state, rendered SVG, rendered HTML, or detail control text.

#### Scenario: Student asks a follow-up after using artifact detail
- **WHEN** the student opens artifact detail, changes zoom or pan state, returns to chat, and asks a follow-up question
- **THEN** the backend request MUST continue to send `conversation_history` as plain `{ role, content }` turns only
- **AND** it MUST NOT include artifact metadata, rendered table DOM, rendered Mermaid SVG, canvas state, route state, row ids, or control labels.

#### Scenario: Local history restores a previous answer
- **WHEN** a student restores a local assistant history entry containing completed table or Mermaid artifacts
- **THEN** the inline completed answer MUST still be able to open the shared artifact canvas detail page
- **AND** any initial canvas transform or row-reader state MUST be recomputed locally rather than restored from assistant message content.

### Requirement: Atom detail route supports full conversation controls
The student H5 Atom assistant SHALL expose the same core Atom conversation controls on the focused `/ai/chat` detail route that it exposes on the `/ai` root route, while preserving detail-route navigation semantics.

#### Scenario: Student opens focused Atom detail chat
- **WHEN** a student opens `/ai/chat` from a point, video, chapter, assessment, history handoff, or future supported learning scene
- **THEN** the page MUST render a modern Atom conversation surface rather than the legacy contextual assistant card layout
- **AND** the page MUST expose supported Atom controls for local history, new chat, free-form asking, send, and context selection.

#### Scenario: Detail chat keeps route role
- **WHEN** `/ai/chat` renders with full Atom controls
- **THEN** the route MUST remain a second-level detail route
- **AND** the bottom navigation MUST remain hidden
- **AND** source-aware back behavior MUST continue to return to the opening source.

#### Scenario: Detail chat does not duplicate old context cards
- **WHEN** `/ai/chat` has an active or seeded context
- **THEN** the context MUST be represented through the Atom composer context chip or equivalent modern Atom binding affordance
- **AND** the page MUST NOT also render the old standalone "current context" card as a parallel context surface.

### Requirement: Atom route seed becomes editable context binding
The student H5 Atom assistant SHALL treat a contextual route seed as an editable initial context before the first submitted user turn.

#### Scenario: Detail route opens with contextKey
- **WHEN** `/ai/chat` opens with a valid `contextKey`
- **THEN** the resolved `AssistantContext` MUST seed the current Atom chat's context chip
- **AND** the student MUST be able to ask immediately using that seeded context.

#### Scenario: Seeded context is editable before first send
- **WHEN** a seeded context is visible and the chat has no submitted user message
- **THEN** the student MUST be able to remove or replace the seeded context
- **AND** replacing the context MUST update the context used for the first submitted question.

#### Scenario: Restored history overrides route seed
- **WHEN** the student restores a local Atom history entry while on `/ai/chat`
- **THEN** the restored history entry's saved context MUST become the active chat context
- **AND** the original route seed MUST NOT overwrite the restored context until the student starts a new chat.

#### Scenario: New chat reseeds from current route when available
- **WHEN** the student activates new chat from `/ai/chat`
- **THEN** visible turns, draft text, loading state, generated suggestions, and active local history id MUST be cleared
- **AND** if the route still has a valid opening context seed, the fresh chat SHOULD show that seed as an editable context chip
- **AND** if no valid route seed exists, the fresh chat MUST use the default global Atom context.

### Requirement: Atom context binding locks after first user turn
The student H5 Atom assistant SHALL enforce one bound context per chat after the first submitted user message across root and focused detail entry points.

#### Scenario: Selected context before first send
- **WHEN** the current Atom chat has a selected context and no submitted user message
- **THEN** the context chip MUST communicate the selected learning background
- **AND** the chip MUST allow removal or replacement before submission.

#### Scenario: Selected context after first send
- **WHEN** the current Atom chat has submitted at least one user message with a selected context
- **THEN** the context chip MUST communicate that the chat is bound to that context
- **AND** the app MUST NOT silently replace or remove that bound context inside the same chat
- **AND** the student MUST start a new chat before binding a different context.

#### Scenario: Global chat remains valid
- **WHEN** the student submits from an Atom chat without selecting a context
- **THEN** the assistant request MUST use the current global or restored context
- **AND** the UI MUST NOT require context selection before asking.

### Requirement: Atom first-turn context prompts are separate from follow-up prompts
The student H5 Atom assistant SHALL use context-start prompts for selected-context empty chats and keep them distinct from model-generated post-answer follow-up prompts.

#### Scenario: Empty selected-context chat shows start prompts
- **WHEN** an Atom chat has a selected experiment or point context
- **AND** no user message has been submitted
- **THEN** the app SHOULD show compact first-turn prompt options tied to that context
- **AND** those prompts SHOULD include student-facing directions such as observation, phenomenon explanation, principle, design reason, comparison, or common mistakes.

#### Scenario: Start prompt is selected
- **WHEN** the student activates a first-turn context prompt
- **THEN** the app MUST submit a concrete question using the currently selected context
- **AND** the selected context MUST become locked for that chat after submission.

#### Scenario: Post-answer suggestions remain latest-turn metadata
- **WHEN** a successful assistant turn returns sanitized `suggested_prompts`
- **THEN** those prompts MUST remain post-answer next-turn suggestions
- **AND** they MUST NOT be confused with the empty-chat context-start prompt stack.

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

### Requirement: Completed AI answers expose rich-content detail viewing
The student H5 Atom assistant SHALL let students open completed AI-generated table and Mermaid artifacts into a mobile detail viewer while preserving inline chat readability.

#### Scenario: Completed answer contains a GFM table
- **WHEN** a completed assistant answer contains a rendered GFM table
- **THEN** the inline chat answer MUST continue to render the table preview in place
- **AND** the table preview MUST expose a touch-friendly detail affordance
- **AND** activating the affordance MUST open a student AI rich-content detail view for that table.

#### Scenario: Completed answer contains a Mermaid diagram
- **WHEN** a completed assistant answer contains a rendered Mermaid flowchart or graph
- **THEN** the inline chat answer MUST continue to render the diagram preview in place
- **AND** the Mermaid preview MUST expose a touch-friendly detail affordance
- **AND** activating the affordance MUST open a student AI rich-content detail view for that diagram.

#### Scenario: Answer is still streaming
- **WHEN** the latest assistant answer is still streaming or has incomplete Markdown
- **THEN** the custom route-backed rich-content detail affordance SHOULD remain hidden or disabled
- **AND** partial tables or partial Mermaid blocks MUST NOT be opened as final rich-content artifacts
- **AND** any Streamdown-native active-turn controls MUST NOT corrupt the final completed-answer viewer state.

#### Scenario: Inline preview remains usable
- **WHEN** the student does not open the detail view
- **THEN** inline tables and Mermaid previews MUST remain readable and scrollable within the chat surface
- **AND** the detail affordance MUST NOT obscure table cells, diagram labels, formulas, the assistant action row, follow-up chips, or the composer.

### Requirement: AI rich-content artifacts are identified from local Markdown history
The student H5 Atom assistant SHALL identify table and Mermaid detail artifacts from plain Markdown chat history rather than persisted rendered HTML or SVG.

#### Scenario: New assistant messages are created
- **WHEN** the frontend creates user and assistant messages for a student AI conversation
- **THEN** it MAY attach local-only message identifiers for UI routing
- **AND** those identifiers MUST NOT be sent to the backend as part of `conversation_history`.

#### Scenario: Rich artifact route opens
- **WHEN** a rich-content detail route is opened with a history id, message id, and artifact id
- **THEN** the app MUST read the local AI history entry
- **AND** it MUST locate the assistant message by message id or a documented legacy fallback
- **AND** it MUST derive the target table or Mermaid artifact from the message's plain Markdown content.

#### Scenario: Legacy history lacks message identifiers
- **WHEN** a restored local AI history entry was created before message ids existed
- **THEN** the app MUST continue to render the conversation
- **AND** it SHOULD derive stable local fallback ids from the history entry and message position
- **AND** opening rich content SHOULD work when the target message and artifact can be unambiguously resolved.

#### Scenario: Artifact cannot be resolved
- **WHEN** the requested history entry, assistant message, or artifact cannot be found
- **THEN** the rich-content detail view MUST show a student-safe fallback state
- **AND** the student MUST have a clear back action
- **AND** the UI MUST NOT expose parser internals, local-storage keys, stack traces, raw route params, or implementation diagnostics.

### Requirement: Table detail viewer supports mobile reading
The student H5 Atom assistant SHALL render AI-generated table details as a read-only mobile table reader optimized for comparison and inspection.

#### Scenario: Student opens a table detail
- **WHEN** a student opens a table artifact detail view
- **THEN** the view MUST render the table content as a read-only learning artifact
- **AND** it MUST preserve semantic table structure where practical
- **AND** it MUST provide enough spacing and contrast for chemistry-learning prose, formulas, and observations.

#### Scenario: Table is wider than the phone viewport
- **WHEN** the table width exceeds the available detail-view width
- **THEN** horizontal scrolling MUST remain available
- **AND** persistent desktop scrollbar chrome SHOULD be hidden in phone preview contexts
- **AND** hiding scrollbar chrome MUST NOT disable touch, pointer, wheel, keyboard, or programmatic scrolling.

#### Scenario: Table has many rows
- **WHEN** the table extends vertically beyond the visible detail area
- **THEN** vertical scrolling MUST remain available
- **AND** table header cells SHOULD remain visible through sticky header behavior where it improves reading
- **AND** the detail header and controls MUST NOT cover table content.

#### Scenario: First column provides row labels
- **WHEN** the first column contains row labels, steps, reagents, or comparison categories
- **THEN** the table detail viewer MAY keep the first column sticky
- **AND** sticky first-column behavior MUST NOT overlap formulas, hide adjacent content, or create unreadable stacked cells.

### Requirement: Mermaid detail viewer supports pan and zoom
The student H5 Atom assistant SHALL render AI-generated Mermaid diagrams in a detail viewer that supports mobile pan, zoom, fit, and reset interactions.

#### Scenario: Student opens a Mermaid detail
- **WHEN** a student opens a Mermaid artifact detail view
- **THEN** the app MUST render the diagram as SVG using the Atom assistant Mermaid theme
- **AND** the diagram MUST remain sharp when zoomed
- **AND** the view MUST provide drag or pan inspection for diagrams larger than the visible area.

#### Scenario: Student uses touch gestures
- **WHEN** the student's browser supports touch gestures
- **THEN** the Mermaid detail viewer SHOULD support pinch-to-zoom and drag-to-pan inside the diagram area
- **AND** the gesture handling MUST remain scoped to the viewer area
- **AND** normal page back/navigation behavior MUST remain available.

#### Scenario: Student uses explicit controls
- **WHEN** the Mermaid detail viewer renders
- **THEN** it MUST provide explicit controls for zooming in, zooming out, and fitting or resetting the diagram
- **AND** each control MUST have a phone-appropriate hit target and accessible name
- **AND** the controls MUST remain readable over the light Atom viewer surface.

#### Scenario: Reduced motion is requested
- **WHEN** the device or browser requests reduced motion
- **THEN** pan/zoom functionality MUST remain available
- **AND** animated transform transitions SHOULD be reduced or disabled.

#### Scenario: Mermaid rendering fails
- **WHEN** the Mermaid source cannot be rendered
- **THEN** the detail viewer MUST show a student-safe fallback for the diagram
- **AND** it MUST NOT expose raw stack traces, Mermaid parser internals, or development diagnostics as ordinary student content.

### Requirement: Rich-content viewer preserves assistant privacy and copy boundaries
The student H5 Atom assistant SHALL keep rich-content viewer controls separate from answer content, backend history, copied text, and student-safe role boundaries.

#### Scenario: Student copies an assistant answer
- **WHEN** the student activates the answer copy action on a message that contains rich-content controls
- **THEN** the copied text MUST contain the original assistant answer Markdown
- **AND** it MUST NOT include rendered table controls, Mermaid viewer controls, hidden route ids, HTML, SVG, pan/zoom state, parser diagnostics, or detail-view labels.

#### Scenario: Conversation history is sent to backend
- **WHEN** a follow-up assistant request sends recent conversation history
- **THEN** each history item MUST include only the expected role and content fields
- **AND** it MUST NOT include local message ids, artifact ids, route params, rendered HTML, rendered SVG, zoom state, or detail-view UI state.

#### Scenario: Role-boundary metadata is present
- **WHEN** assistant metadata includes sources, retrieval details, guardrail decisions, tool traces, or other internal fields
- **THEN** the rich-content viewer MUST NOT expose those fields as visible student content
- **AND** it MUST NOT make those fields available through table, Mermaid, copy, route, or fallback UI.

### Requirement: Rich-content detail navigation preserves chat context
The student H5 Atom assistant SHALL open rich-content detail views without losing the student's chat context, root/detail route semantics, or local history.

#### Scenario: Rich content opens from the root AI route
- **WHEN** the student opens a rich artifact from `/ai`
- **THEN** the app MUST navigate to a student detail route or equivalent route-backed second-level view
- **AND** the route MUST hide the root bottom navigation according to detail-route rules
- **AND** the back action MUST return the student to the root AI conversation.

#### Scenario: Rich content opens from contextual AI chat
- **WHEN** the student opens a rich artifact from contextual `/ai/chat`
- **THEN** the app MUST preserve enough source context to return the student to the contextual chat flow
- **AND** the detail viewer MUST NOT introduce the root history action or root-only empty-state chrome.

#### Scenario: New chat is started after returning
- **WHEN** the student returns from a rich-content detail view and starts a new chat
- **THEN** the existing new-chat behavior MUST continue to clear visible turns and context binding according to the established root/detail rules
- **AND** the rich-content route state MUST NOT keep stale artifact content alive in the new chat.

