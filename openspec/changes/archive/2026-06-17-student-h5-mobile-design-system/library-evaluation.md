# Mobile Library Evaluation

Date: 2026-06-17
Candidate: `antd-mobile`

## Candidate Fit

`antd-mobile` is a reasonable React mobile-web candidate for generic mechanics:

- Toast
- Dialog
- Popup
- ActionSheet
- Tabs
- Form/Input controls
- floating controls

It is not a good replacement for the product-specific chemistry learning surface:

- element and family badges
- property cards
- related experiment-point cards
- video/point detail
- AI source summaries
- chemistry empty states

## Bundle And Styling Impact

The current student H5 dependency set is intentionally small. Adding a mobile UI kit would increase dependency surface and CSS/theming work before we have enough repeated generic primitives to justify it.

The current implementation can standardize behavior with a local layer first:

- CSS tokens for colors, spacing, radius, touch sizes, z-index, safe area, and viewport dimensions.
- React primitives for button, icon button, field, textarea, status, empty state, and floating overlay governance.
- Mobile viewport QA to catch the layout failures that a library would otherwise help prevent.

## Decision

Do not adopt `antd-mobile` in this iteration.

Instead, keep a project-local `apps/student-web/src/mobile/` layer and make it the only place future library adoption should enter. If a later change adopts `antd-mobile`, wrap it behind these local primitives instead of importing it directly into feature screens.

## Rollback Path

Because no third-party mobile library is adopted in this iteration, rollback is limited to removing the local mobile primitives and returning the JSX/CSS to direct controls.
