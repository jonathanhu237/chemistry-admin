## Context

`apps/student-web` is the student-facing React + Vite H5 app. It runs in mobile browsers and can run inside a WeChat WebView, but it is not currently a native WeChat mini-program package.

The previous `student-h5-real-learning-experience` change established that the student app is phone-first and verified the current learning screens at 360x780, 390x844, and 430x932 CSS pixel viewports. That work also exposed the pattern we need to preserve: the chemistry learning UI is product-specific, while generic mobile mechanics such as safe areas, overlays, dialogs, toasts, forms, floating actions, and viewport QA should be standardized.

Current student-web facts:
- dependencies are intentionally small: React, React DOM, Vite, TypeScript, and `lucide-react`;
- core UI is handcrafted in `App.tsx` and `styles.css`;
- the app already uses `env(safe-area-inset-*)`, 8px radii, 44px+ touch targets in many places, phone-width constraints, and fixed AI/feedback controls;
- the largest near-term risk is not missing features, but future contributors accidentally reintroducing desktop-admin density, hover-only behavior, horizontal overflow, or overlapping fixed controls.

Reference points from the exploration:
- Ant Design Mobile is a React mobile web component library and is suitable as an optional source for generic primitives.
- WeUI aligns with WeChat native visual language, but is more useful as a style reference than as the primary React implementation layer for this project.
- NutUI React is a mobile React component library with H5 / mini-program ecosystem relevance, but its JD-commerce visual assumptions are less aligned with this chemistry learning product.
- Taro supports H5 and WeChat mini-program targets, but using it would be a cross-platform rewrite and is explicitly out of scope here.
- CSS viewport and `env(safe-area-inset-*)` behavior must remain first-class because phone browsers and WebViews can have notches, curved edges, browser chrome, and dynamic keyboard effects.

## Goals / Non-Goals

**Goals:**
- Preserve `apps/student-web` as a phone-first mobile browser / WeChat WebView H5 app.
- Define a reusable mobile design-system layer for tokens, primitives, overlay rules, touch targets, and safe-area handling.
- Make mobile viewport QA repeatable and hard to skip.
- Keep the custom chemistry learning page visual direction: family facts, property cards, related experiment-points, video/point detail, chat, and feedback.
- Allow selective adoption of a mobile React component library for generic primitives only when it reduces risk and bundle cost is acceptable.
- Keep future student-web changes consistent even after context compaction or contributor handoff.

**Non-Goals:**
- No native WeChat mini-program package.
- No Taro or uni-app migration.
- No React Native target.
- No full visual redesign of the current chemistry learning experience.
- No replacement of custom domain cards with generic library cards.
- No backend API change unless a later implementation task discovers a specific need.
- No admin-web design-system migration.

## Decisions

### Decision: Keep React + Vite H5; do not introduce a mini-program build chain

Continue treating `apps/student-web` as a mobile web application rendered in a browser/WebView.

Rationale: the user only needs phone-browser behavior now. A Taro or native mini-program rewrite would change routing, component primitives, styling constraints, build/deploy flow, QA matrix, and merge risk without solving the immediate problem.

Alternative considered: migrate to Taro. Rejected for this change because it is useful only if the deliverable must become a true mini-program package.

### Decision: Build a project-local mobile design-system layer first

Create a small project-local layer, likely under `apps/student-web/src/mobile/`, before adopting a large UI library across the app:

- `tokens.css`: colors, typography scale, spacing, radii, z-index, safe-area sizing, touch target sizes, viewport constants.
- `primitives.tsx`: reusable mobile primitives such as `MobileButton`, `IconButton`, `Field`, `Sheet`, `Toast`, `Dialog`, `Tabs`, `Fab`, `FloatingOverlayRoot`.
- `viewport.ts`: helpers for visual viewport, keyboard-aware bottom offsets, and safe-area derived layout values if needed.
- `qa.ts` or a script: viewport checks for overflow, overlap, and touch-target sizes.

Rationale: the current UI is highly product-specific. A local layer lets the app standardize mobile behavior without losing the chemistry learning visual identity.

Alternative considered: immediately install a mobile UI kit and rewrite screens. Rejected because it risks churn, bundle growth, and generic-looking learning cards.

### Decision: Use mobile component libraries only as generic primitive suppliers

If a library is adopted, prefer `antd-mobile` as the first candidate for generic components: Toast, Dialog, Popup, ActionSheet, Tabs, Form/Input, FloatingBubble-like controls, PullToRefresh or InfiniteScroll if needed later.

Keep product-specific pieces custom:
- element/family hero;
- property cards;
- related experiment-point cards;
- video/point detail layout;
- student AI source rendering;
- chemistry-specific empty states.

Rationale: generic interaction mechanics are easy to get wrong on mobile. Domain learning surfaces are where the product needs its own taste.

Alternative considered: WeUI as the primary implementation. Rejected as primary because this app is React/Vite and already has a custom brand/learning surface; WeUI remains a good WeChat visual reference.

Alternative considered: NutUI React. Keep as a fallback if `antd-mobile` is unsuitable, especially if future requirements lean toward a stronger mobile app component set.

### Decision: Make overlays mutually exclusive and safe-area aware

Only one bottom/floating overlay family may be active at a time. AI chat, feedback, dialogs, sheets, and sticky actions must share z-index and bottom safe-area rules.

Rationale: phone viewports are small, and WebViews make bottom UI unpredictable. The recent mobile check already found and fixed overlap between AI and feedback controls; this rule prevents regressions.

### Decision: Verification is part of the design system

Student-web completion requires repeatable checks at these viewport sizes:

- 360x780
- 390x844
- 430x932

Checks should include:
- no page-level horizontal overflow;
- touch targets at or above the minimum size where applicable;
- fixed/floating overlays do not overlap each other or block primary actions;
- important flows are usable without hover or desktop keyboard shortcuts;
- desktop preview remains a centered/constrained phone layout.

Rationale: mobile correctness is observable. It should not depend on memory or taste.

## Risks / Trade-offs

- [Risk] Adding a component library increases bundle size and visual inconsistency. -> Mitigate by evaluating bundle impact first and adopting only generic primitives.
- [Risk] A local design-system layer becomes another abstraction without enough reuse. -> Mitigate by extracting only repeated controls and mobile mechanics already present in the app.
- [Risk] Browser automation cannot perfectly represent WeChat WebView behavior. -> Mitigate with automated viewport checks plus at least one manual phone/WeChat WebView check before major release.
- [Risk] Keyboard behavior differs across iOS Safari, Android Chrome, and WeChat WebView. -> Mitigate by keeping input overlays keyboard-aware and testing chat/feedback compose flows on device.
- [Risk] Future contributors bypass primitives and create raw fixed controls. -> Mitigate with OpenSpec requirements, task checklist, and a mobile QA script that catches overlap and overflow.

## Migration Plan

1. Capture the contract in OpenSpec and keep this change as the durable context.
2. Extract CSS tokens and repeated mobile constants from `styles.css` without changing UI behavior.
3. Extract only proven primitives from current code, starting with buttons, icon buttons, feedback/chat overlay shell, fields, and status/empty states.
4. Add a viewport QA script or test that can be run locally against the Vite dev server.
5. Evaluate `antd-mobile` on a small branch for generic primitives only; adopt only if bundle and styling are acceptable.
6. Apply primitives incrementally to login/password/pretest, learning home, point detail, chat, feedback, and posttest surfaces.
7. Document final verification results in the change before implementation completion.

Rollback is straightforward if the work is incremental: primitives can be inlined back into current JSX/CSS, and optional library adoption can be skipped.

## Open Questions

- Should `antd-mobile` be adopted at all, or should the first implementation stay purely project-local?
- Should viewport QA be Playwright-based, in-app-browser based, or a repo script that runs against a local Vite server?
- Do we need an explicit WeChat WebView manual test checklist for keyboard and safe-area behavior, or is phone browser QA sufficient for the next iteration?
