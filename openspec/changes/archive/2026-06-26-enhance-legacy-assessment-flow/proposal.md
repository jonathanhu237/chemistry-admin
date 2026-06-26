## Why

The old student product now has a convincing SYSU-red video library and chemistry learning drilldown, but its `评测` module is still a thin smart-assessment button and cannot demonstrate the BKT feedback loop end to end. The lower-level competition demo needs an old-style assessment home and exam-taking flow that merge smart weak-point testing with self-selected practice while preserving the legacy BKT narrative.

## What Changes

- Replace the old `评测` landing page with a traditional teaching-platform assessment setup page.
- Merge the current `智能组卷` and `自主测评` concepts into one old-style form surface with a single experiment multi-select list.
- Support four student-facing setup modes on the same page:
  - `智能薄弱项测试`: algorithm/BKT-driven weak-point composition.
  - `自选实验范围`: student manually selects experiment ranges from a multi-select list.
  - `随机练习`: the old frontend randomly selects eligible experiments from the available or filtered list, then starts a custom assessment.
  - `全部范围`: selects all eligible experiments and starts a custom assessment.
- Keep question-count selection on the setup page using the existing custom-assessment settings and options.
- Add an old-style exam-taking page that reuses current assessment session/question/submit APIs but renders as square, paper-like examination cards instead of the modern H5 assessment UI.
- Route generated smart/custom/point assessment sessions into the old exam-taking page and submit answers through the existing smart-assessment submit API.
- Preserve the old product boundary: no Atom, RAG, Agent, learning assistant, provider diagnostics, retrieval, chunk, embedding, modern green theme, or modern custom player language.
- Prefer existing current backend assessment APIs; add old-scoped backend adapters only if the old frontend cannot express the desired behavior with current student APIs.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `bkt-legacy-competition-profile`: Add the old student assessment setup and exam-taking requirements needed to demonstrate the BKT smart assessment feedback loop without exposing the current RAG/Agent product language.

## Impact

- Affected frontend code: `apps/web-student-old/src/LegacyStudentApp.tsx`, `apps/web-student-old/src/api.ts`, `apps/web-student-old/src/styles.css`, and old student tests.
- Referenced current frontend source for behavior migration: `apps/web-student/src/routes/assessment/AssessmentCustomPage.tsx`, `apps/web-student/src/routes/assessment/AssessmentSessionPage.tsx`, `apps/web-student/src/features/assessment/PosttestPanel.tsx`, and `apps/web-student/src/features/pretest/AssessmentPanel.tsx`.
- Reused backend APIs: `/api/student/custom-assessment/options`, `/api/student/custom-assessment/start`, `/api/student/smart-assessment/start`, `/api/student/point-assessment/start`, and `/api/student/smart-assessment/submit`.
- Possible old-scoped backend impact: only if random practice or old setup summaries require data that current student assessment APIs do not provide.
- No new chemistry seed data, old-only experiment/question ids, database fork, or current product behavior change is expected.
