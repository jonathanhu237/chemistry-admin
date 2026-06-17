# Student H5 Mobile Baseline

Date: 2026-06-17
Branch: `codex/student-h5-real-learning-experience`
Change: `student-h5-mobile-design-system`

## Architecture Guardrail

- `apps/student-web` remains a React + Vite H5 app.
- Runtime dependencies before implementation: `react`, `react-dom`, `lucide-react`.
- Dev dependencies before implementation: Vite, TypeScript, React types, Vite React plugin.
- Repository scan found no `taro`, `uni-app`, `react-native`, `@taro`, native mini-program, or WeChat mini-program build chain under `apps/student-web`.
- This change must not add native mini-program output, Taro routing, uni-app pages, or React Native dependencies.

## Current Repeated Mobile Patterns

- Buttons: `.primary-action`, `.secondary-action`, `.sticky-action`, `.icon-action`, AI send/close buttons, feedback close/submit buttons, option buttons, profile/property/point card buttons.
- Inputs: login/password fields, password reset fields, assessment fill answers, AI chat input, feedback textarea.
- Status and empty states: `LoadingPanel`, `LearningState`, `.form-error`, `.form-hint`, `.empty-learning-card`, AI empty bubble, video placeholder, disabled practice strip.
- Floating overlays: AI chat and feedback are fixed bottom overlays with separate left/right positions and shared z-index.
- Safe-area handling: `env(safe-area-inset-*)` exists in the shell, learning panel bottom padding, AI/feedback fixed entries, and sticky assessment action.
- Domain-specific UI: element badges, family/property cards, experiment-point cards, video detail, source summaries, and posttest summary should stay custom.

## CSS Constants To Consolidate

- Colors: `#005826`, `#087246`, `#d9f0c7`, `#fffdf6`, `#183228`, `#64746c`, `#d29b2d`, `#b42318`, `#9aa9a1`, repeated rgba green/amber shadows and fills.
- Radius: `8px` is the dominant card/control radius; `999px` is used for pills; a few smaller code/chip values exist.
- Touch targets: common heights are 34px, 38px, 42px, 44px, 46px, 48px, 50px, 52px, and 54px.
- Viewport widths: auth and learning preview use phone-width caps around 430px; assessment uses 520px.
- Z-index: content uses 1, floating overlays use 20.
- Safe-area and bottom controls: shell padding, learning bottom padding, sticky action bottom, AI/feedback bottom positions repeat `env(safe-area-inset-*)`.

## Viewport Baseline

Existing manual/in-app checks from the previous student H5 work used:

- 360x780 CSS pixels
- 390x844 CSS pixels
- 430x932 CSS pixels

Observed target flows:

- Login and initial password screens render as centered phone H5 surfaces.
- Temporary pretest skip can fail open into learning for local feature testing.
- Learning home and point detail render as phone-width panels.
- AI chat and feedback overlays are mutually exclusive after the previous overlap fix.
- Bottom completion action can scroll clear of fixed AI/feedback entries.

This implementation adds a repeatable script so future checks are no longer only manual.
