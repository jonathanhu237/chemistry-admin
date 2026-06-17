## 1. Baseline And Guardrails

- [x] 1.1 Validate the OpenSpec change `student-h5-mobile-design-system` in strict mode before implementation starts.
- [x] 1.2 Confirm `apps/student-web` remains React + Vite H5 and does not introduce Taro, uni-app, React Native, or native mini-program build outputs.
- [x] 1.3 Audit current student-web screens for repeated mobile patterns: buttons, icon buttons, fields, cards, floating actions, overlays, empty states, and status messages.
- [x] 1.4 Record a mobile baseline for login, password change, temporary pretest skip, learning home, point detail, AI chat, feedback, and posttest/summary at 360x780, 390x844, and 430x932.
- [x] 1.5 Identify current duplicated CSS constants for color, spacing, radii, touch sizes, z-index, safe-area offsets, and bottom fixed-control spacing.

## 2. Mobile Tokens And Local Primitives

- [x] 2.1 Create a student mobile token layer for colors, typography, spacing, radii, shadows, touch target sizes, z-index layers, viewport widths, and safe-area offsets.
- [x] 2.2 Extract reusable mobile button primitives for primary, secondary, icon, full-width, disabled, and loading states.
- [x] 2.3 Extract reusable mobile field primitives for text/password input and textarea behavior while preserving existing auth/chat/feedback copy.
- [x] 2.4 Extract reusable status and empty-state primitives for loading, API error, missing video, no point data, and disabled practice states.
- [x] 2.5 Keep chemistry domain UI custom: element badges, family/property cards, experiment-point cards, point detail, and AI source summaries must preserve their product-specific structure.

## 3. Overlay, Safe Area, And Keyboard Behavior

- [x] 3.1 Introduce a shared floating overlay rule or component that coordinates AI chat, feedback, dialogs, sheets, and future bottom overlays.
- [x] 3.2 Ensure only one floating overlay family can be active at a time on student learning and point-detail screens.
- [x] 3.3 Normalize bottom safe-area spacing so fixed/floating controls do not block completion, submit, back, logout, chat, or feedback actions.
- [x] 3.4 Review chat and feedback input layouts for mobile keyboard behavior and adjust max-height/bottom spacing if needed.
- [x] 3.5 Verify all required controls are reachable without hover, precise mouse input, or desktop keyboard shortcuts.

## 4. Optional Mobile Library Spike

- [x] 4.1 Evaluate `antd-mobile` as the first candidate for generic primitives such as Toast, Dialog, Popup, ActionSheet, Tabs, form controls, and floating controls.
- [x] 4.2 Document bundle impact, CSS/theming fit, component coverage, and rollback path for any candidate library before adopting it.
- [x] 4.3 Decide whether to adopt no library, `antd-mobile`, or another small mobile primitive dependency for this iteration.
- [x] 4.4 If a library is adopted, wrap it behind project-local primitives instead of spreading library-specific usage across feature screens.

## 5. Mobile Viewport QA

- [x] 5.1 Add a repeatable local QA script or test that checks student-web at 360x780, 390x844, and 430x932.
- [x] 5.2 The QA check must detect page-level horizontal overflow on primary student flows.
- [x] 5.3 The QA check must detect overlapping fixed/floating controls where practical.
- [x] 5.4 The QA check must verify key flows are renderable: login, temporary pretest skip, learning home, point detail, AI panel, feedback panel, and bottom completion action.
- [x] 5.5 Add instructions for manual phone or WeChat WebView verification of keyboard and safe-area behavior.

## 6. Verification And Documentation

- [x] 6.1 Run `openspec validate student-h5-mobile-design-system --strict`.
- [x] 6.2 Run `npm run typecheck` in `apps/student-web`.
- [x] 6.3 Run `npm run build` in `apps/student-web` and record JS/CSS bundle sizes.
- [x] 6.4 Run the new mobile viewport QA script/test and record results.
- [x] 6.5 Update the final verification notes with viewport sizes, flows tested, library decision, residual risks, and whether manual phone/WebView testing remains.
- [x] 6.6 Keep all implementation local until the user explicitly asks to push.
