## 1. Architecture And State Model

- [ ] 1.1 Audit `StudentAiChatPanel`, `StudentAiChatTab`, `AiRootPage`, and `AiChatPage` for logic currently gated only by `variant === "root"`.
- [ ] 1.2 Split route role from Atom feature capability with explicit props or local state such as modern surface, full controls, route mode, and initial context policy.
- [ ] 1.3 Define a single context-binding lifecycle used by root and detail: seed, editable selected chip, submitted/locked context, restored history context, and new-chat reset.
- [ ] 1.4 Ensure restored history context wins over route seed until the student starts a new chat.

## 2. Context Chip And Picker

- [ ] 2.1 Generalize the composer `+` action so both `/ai` and `/ai/chat` can open the Atom context picker.
- [ ] 2.2 Treat `/ai/chat` `contextKey` as an initial editable context chip before the first user turn.
- [ ] 2.3 Keep context removal and replacement available before the first user turn on both root and detail surfaces.
- [ ] 2.4 Lock the context chip after the first submitted user message and require new chat before binding a different context.
- [ ] 2.5 When reopening the picker with an existing selected context, navigate/highlight the selected row where the catalog/search data can represent it.
- [ ] 2.6 Keep picker opening, dismissal, keyboard behavior, and selection inside the current route without navigating to search or video-library pages.

## 3. Detail Route Modernization

- [ ] 3.1 Update `/ai/chat` to use the modern Atom conversation surface while keeping it a second-level detail route.
- [ ] 3.2 Remove or hide the old detail "current context" card and legacy detail composer treatment.
- [ ] 3.3 Show Atom history and new-chat actions on the detail surface.
- [ ] 3.4 Keep bottom navigation hidden on `/ai/chat` in normal, focused, picker-open, and keyboard-active states.
- [ ] 3.5 Preserve source-aware back behavior from `/ai/chat` after history restore, new chat, and context replacement.

## 4. History Semantics

- [ ] 4.1 Allow the Atom history drawer to open from both `/ai` and `/ai/chat`.
- [ ] 4.2 Restore any local Atom history entry inside the current Atom surface, regardless of whether it originated from root or detail.
- [ ] 4.3 Save contextual detail conversations into the same local history store with enough context to restore the chip and future backend requests.
- [ ] 4.4 Keep generated history titles, context chip labels, picker state, and UI-only metadata out of copied answer text and backend `conversation_history`.
- [ ] 4.5 Keep the "clear all" and per-row delete behavior consistent across root and detail history drawers.

## 5. First-Turn Prompt Experience

- [ ] 5.1 Render context-start prompts only when a selected context exists and no user message has been submitted.
- [ ] 5.2 Use context-start prompt copy such as observation, phenomenon explanation, principle, design reason, comparison, and common mistakes.
- [ ] 5.3 Avoid horizontal scrollbar chrome for the first-turn prompt stack in mobile and teacher preview frames.
- [ ] 5.4 Keep post-answer `suggested_prompts` as a separate latest-successful-turn mechanism.

## 6. Tests And Validation

- [ ] 6.1 Update student-web tests that currently assert `/ai/chat` omits root actions.
- [ ] 6.2 Add tests proving `/ai/chat` exposes history, new chat, context chip, and picker while bottom navigation remains hidden.
- [ ] 6.3 Add tests for route-seeded context editability before first send and lock behavior after first send.
- [ ] 6.4 Add tests for history restore precedence over route seed and new-chat reseeding behavior.
- [ ] 6.5 Add tests proving backend `conversation_history` remains `{ role, content }` and excludes context chip/picker metadata.
- [ ] 6.6 Run focused student-web tests, typecheck, build, and a mobile/teacher-preview visual QA pass.
