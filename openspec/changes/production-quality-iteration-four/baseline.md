# Fourth Quality Pass Baseline

Date: 2026-06-17
Branch: `codex/productionize-admin-platform`

## Repository And Workflow

- Branch is clean and aligned with `origin/codex/productionize-admin-platform` at the start of the pass.
- `.github/workflows/production-readiness.yml` remains manual-only with `workflow_dispatch`.
- No CI trigger or release automation changes are in scope for this pass.

## Frontend Source Hotspots

Current large-file baseline:

| File | Lines | Size |
| --- | ---: | ---: |
| `apps/admin-web/src/App.tsx` | 455 | 15.3 KB |
| `apps/admin-web/src/styles.css` | 1097 | 19.6 KB |
| `apps/admin-web/src/features/question-bank/QuestionBanksPage.tsx` | 1345 | 59.5 KB |
| `apps/admin-web/src/features/media/VideoResourcesPage.tsx` | 1176 | 59.4 KB |
| `apps/admin-web/src/features/learning-assistant/LearningAssistantPage.tsx` | 1331 | 59.4 KB |
| `apps/admin-web/src/features/experiments/ExperimentsPage.tsx` | 918 | 42.1 KB |
| `apps/admin-web/src/features/resources/LearningResourcesPage.tsx` | 976 | 38.4 KB |
| `apps/admin-web/src/api/index.ts` | 1179 | 31.1 KB |

Interpretation: the app shell has already been reduced. The next maintainability work should target feature modules rather than top-level routing.

## Build Chunk Baseline

`npm run build:report` reported:

- `charts-vendor-DhwdVBof.js`: 1449.2 KB, gzip 429.9 KB, owner `Charts/G2 vendor`
- `antd-vendor-J4TJASBj.js`: 937.8 KB, gzip 301.1 KB, owner `Ant Design vendor`
- `markdown-vendor-fcXWHA9Q.js`: 445.9 KB, gzip 131.2 KB, owner `Markdown/KaTeX vendor`
- `react-vendor-D0TUXMcu.js`: 267.9 KB, gzip 84.6 KB, owner `React/router/query vendor`
- `upload-vendor-BJaxDxyG.js`: 139.7 KB, gzip 44.4 KB, owner `Upload/tus/hash vendor`

Large chunks above 500 KB remain named and owned:

- Charts/G2 vendor
- Ant Design vendor

Representative lazy page chunks are already small compared with vendor chunks:

- `VideoResourcesPage`: 34.0 KB
- `LearningAssistantPage`: 31.5 KB
- `QuestionBanksPage`: 30.7 KB

Interpretation: this pass should prioritize source maintainability. Bundle improvements are still useful, but eliminating all vendor warnings is not required for the fourth-pass acceptance criteria.
