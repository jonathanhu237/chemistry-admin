## Why

The first three productionization passes made the platform recoverable, validated, and quieter to operate. The admin frontend is no longer a single 8000-line `App.tsx`, and the backend admin routes have mostly moved behind focused routers and services.

The next maintainability risk is one layer deeper: several frontend feature pages have grown into 60 KB modules, and the remaining production build warnings are now mostly large named vendor chunks. This change captures the fourth pass so feature-level decomposition and bundle ownership can continue without depending on chat memory.

## What Changes

- Keep GitHub Actions production readiness manual-only; do not add push or pull-request triggers in this pass.
- Preserve all protected chemistry resources, route paths, API contracts, auth behavior, and current UI workflows.
- Establish a fourth-pass baseline for frontend feature module sizes, route chunk ownership, and remaining bundle warnings.
- Split one or more large frontend feature modules into behavior-preserving subcomponents, hooks, or local utilities.
- Prefer low-risk extractions from large pages such as question banks, videos/media, or learning assistant before touching cross-feature contracts.
- Keep page-level lazy loading and named vendor chunk ownership intact.
- Validate with OpenSpec strict checks, frontend typecheck/tests/build/build report, and broader readiness checks when the change surface warrants them.

## Capabilities

### New Capabilities

- `frontend-admin-maintainability`: Defines fourth-pass requirements for feature-level frontend decomposition, route chunk ownership, and manual-only CI posture.

### Modified Capabilities

None.

## Impact

- Frontend: `apps/admin-web/src/features/*`, shared components/hooks/utilities, and possibly route-level lazy imports.
- Build: Vite chunk output remains named and documented; this pass may reduce route chunk size or make ownership clearer, but does not require eliminating all vendor warnings.
- Validation: OpenSpec strict validation plus frontend typecheck/test/build/build report. E2E smoke remains opt-in when runtime behavior needs confirmation.
- Operations: CI / release flow remains unchanged; `Production Readiness` stays `workflow_dispatch` only.
- Compatibility: No intended changes to backend APIs, database migrations, protected seed resources, RAG evidence semantics, route paths, or admin workflows.
