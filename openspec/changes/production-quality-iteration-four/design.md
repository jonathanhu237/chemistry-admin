## Context

The previous passes already moved the project away from the largest obvious risks:

- protected resources are manifest-validated and fixed under `data/seed`;
- GitHub production readiness no longer runs on ordinary pushes;
- representative admin pages have repeatable e2e smoke coverage;
- `App.tsx` has been reduced to the app shell, login page, protected shell, and lazy route boundaries;
- feature styles have been split into feature-owned CSS files;
- backend admin endpoint groups have largely moved from `experiment_admin.py` into routers/services.

Current frontend size hotspots are feature modules rather than the app shell:

| File | Current role | Risk |
| --- | --- | --- |
| `features/question-bank/QuestionBanksPage.tsx` | question bank list, drafts, AI workbench, point-aware controls | too many responsibilities in one page module |
| `features/media/VideoResourcesPage.tsx` | media list, upload queue, duplicate review, video preview | upload/runtime logic mixed with display logic |
| `features/learning-assistant/LearningAssistantPage.tsx` | assistant chat, debug diagnostics, evidence display, markdown rendering | chat state and diagnostics are hard to review together |
| `features/resources/LearningResourcesPage.tsx` | dashboard/resource overview/framework panels | medium-size page with extractable widgets |
| `src/api/index.ts` | API helpers and types | useful but growing shared contract surface |

## Goals / Non-Goals

**Goals:**

- Keep the fourth pass focused on maintainability, not new features.
- Reduce review risk by extracting stable UI/helpers from the largest feature files.
- Preserve page behavior, route paths, query keys, mutation behavior, and visible workflows.
- Keep route-level lazy loading and named vendor chunks intact.
- Maintain a clean, push-safe branch with validation recorded in OpenSpec notes.

**Non-Goals:**

- Do not change CI triggers. The production readiness workflow remains manual-only unless the owner explicitly asks otherwise.
- Do not redesign admin screens or rewrite feature workflows.
- Do not alter question bank content, knowledge framework data, experiment point inventory, canonical chunks/embeddings, or evidence bindings.
- Do not perform backend route refactors in this pass unless frontend validation reveals a small compatibility fix is required.
- Do not try to eliminate every Vite chunk warning by force; large Ant Design and chart vendor chunks may remain acceptable if named and documented.

## Decisions

1. Treat feature-file decomposition as the primary fourth-pass work.

   Rationale: `App.tsx` and `styles.css` have already improved. The next bottleneck is large page modules where unrelated concerns are hard to review.

2. Start with one low-risk feature slice rather than splitting every large page at once.

   Rationale: small behavior-preserving moves are easier to verify and review. A good first slice is display/helper code that has limited state coupling.

3. Keep CI unchanged during this pass.

   Rationale: remote workflow noise was a user concern, and the current manual `workflow_dispatch` posture is documented and working. CI/release automation can be revisited only when there is a real deployment target or branch protection policy.

4. Validate frontend behavior at the appropriate depth.

   Rationale: typecheck/test/build/build-report are mandatory for frontend moves. E2E smoke is valuable after route/load-boundary changes but remains opt-in because it requires a running backend/frontend stack.

## Candidate Extraction Order

1. Question bank pure display helpers and tags into a feature-local utility module.
2. Question bank workbench/draft display components into feature-local components.
3. Media upload state machine helpers into a feature-local module.
4. Learning assistant diagnostics/evidence panels into feature-local components.
5. Shared API type reorganization only after feature extractions stabilize.

## Risks / Trade-offs

- [Risk] Extracting helpers can accidentally change display labels or payload normalization. Mitigation: move code mechanically, preserve names where useful, and run typecheck/tests.
- [Risk] Large feature pages can have implicit coupling through local state. Mitigation: begin with pure helpers and presentational components before hooks/state machines.
- [Risk] Bundle size may not drop immediately because vendor chunks dominate. Mitigation: treat this pass as maintainability first; build reports should remain named and explainable.
- [Risk] E2E can be environment-sensitive. Mitigation: keep it opt-in and use it when route behavior changes.
