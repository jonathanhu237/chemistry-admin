## Why

The student frontend is now a real phone-facing H5 surface, but its mobile behavior is still protected mostly by page-level CSS and manual checks. To keep future development from drifting back toward desktop-admin patterns, the project needs a durable student H5 mobile design-system contract and verification path.

This change explicitly keeps `apps/student-web` as a mobile browser / WeChat WebView H5 app. It does not create a native mini-program package, Taro app, or uni-app migration.

## What Changes

- Define a project-level mobile design-system layer for `apps/student-web`, covering tokens, primitives, overlays, safe areas, touch targets, and viewport QA.
- Standardize the student H5 surface as phone-first for common mobile browser and WeChat WebView dimensions.
- Add a library adoption stance: keep the custom chemistry learning UI, optionally use a mobile React library only for generic primitives such as Toast, Dialog, Popup, ActionSheet, Tabs, FloatingBubble, and form controls.
- Require automated or repeatable visual/layout checks for 360x780, 390x844, and 430x932 CSS pixel viewports.
- Preserve the current React + Vite H5 architecture; no native mini-program packaging or cross-platform rewrite in this change.
- Keep desktop browser behavior as a constrained preview of the phone layout, not a separate desktop student product.

## Capabilities

### New Capabilities

- `student-h5-mobile-design-system`: Mobile-browser design-system rules, implementation boundaries, reusable primitives, optional library usage, and phone viewport verification for `apps/student-web`.

### Modified Capabilities

- None. Existing student login and learning requirements remain functionally unchanged; this change adds a cross-cutting mobile H5 engineering contract.

## Impact

- Affected app: `apps/student-web`.
- Expected future code areas: `apps/student-web/src/styles.css`, `apps/student-web/src/App.tsx`, and possible new files under `apps/student-web/src/mobile/`.
- Possible optional dependency: `antd-mobile` for generic mobile primitives, evaluated before adoption.
- Verification impact: student-web typecheck/build plus phone viewport layout checks become part of the student H5 completion definition.
- No backend API changes are required by this proposal.
- No Taro, uni-app, React Native, or native WeChat mini-program build output is introduced.
