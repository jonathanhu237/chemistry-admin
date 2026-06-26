## 1. Assessment Contracts

- [x] 1.1 Expand old student assessment API types for custom assessment options, smart/custom/point session responses, questions, answers, submit responses, and report summaries.
- [x] 1.2 Add old student API functions for `/api/student/custom-assessment/options`, `/api/student/custom-assessment/start`, and `/api/student/smart-assessment/submit`.
- [x] 1.3 Add old-scoped session/report storage helpers for generated assessment sessions and completed assessment reports.
- [x] 1.4 Confirm old assessment API wrappers reuse current backend ids and do not introduce old-only experiment, question, session, or mastery identities.

## 2. Legacy Assessment Setup Page

- [x] 2.1 Replace the old one-button assessment root with a unified old-style assessment setup page.
- [x] 2.2 Load custom assessment options and render eligible experiments as square checkbox/list rows with available question counts.
- [x] 2.3 Add setup modes for `智能薄弱项测试`, `自选实验范围`, `随机练习`, and `全部范围`.
- [x] 2.4 Implement search/filtering for experiment title, parent title, chapter/category text, and code when available.
- [x] 2.5 Implement batch actions such as select all current eligible rows, clear selection, random selection, and hiding or disabling zero-question rows.
- [x] 2.6 Render configured question-count choices with old square styling and safe fallback values.
- [x] 2.7 Add old-style validation and loading/error states for missing selections, disabled options, failed option loading, and unavailable custom assessment settings.

## 3. Assessment Start Routing

- [x] 3.1 Start `智能薄弱项测试` through the current smart-assessment start API.
- [x] 3.2 Start `自选实验范围` through the current custom-assessment start API with selected experiment ids and question count.
- [x] 3.3 Start `随机练习` by choosing eligible experiments in the old frontend and starting a custom assessment.
- [x] 3.4 Start `全部范围` by selecting all eligible experiments and starting a custom assessment.
- [x] 3.5 Store generated sessions and navigate all start modes to an old assessment session route such as `/assessment/session/:sessionId`.
- [x] 3.6 Keep the old bottom navigation on `评测` for assessment setup and session routes.

## 4. Legacy Exam-Taking Page

- [x] 4.1 Add an old assessment session route and controlled missing-session state.
- [x] 4.2 Render a paper-like old exam heading with mode, experiment/point coverage, question count, and composition warnings.
- [x] 4.3 Render single-choice questions with square selectable option rows.
- [x] 4.4 Render true/false questions with backend-compatible `正确`/`错误` answer choices.
- [x] 4.5 Render fill-blank questions with old square text inputs.
- [x] 4.6 Track local answers and prevent incomplete submissions with a legacy-facing validation state.
- [x] 4.7 Submit completed answers through the current smart-assessment submit API and store or route to an old-compatible result/report state.
- [x] 4.8 Render underfilled assessment warnings when generated question count is below the requested target.

## 5. Point Post-Learning Assessment Integration

- [x] 5.1 Update old point-detail `进行学后测评` to store the returned point-scoped assessment session.
- [x] 5.2 Navigate point-scoped assessment sessions to the same old exam-taking route.
- [x] 5.3 Label point-scoped sessions with old-facing post-learning assessment copy.

## 6. Styling and Product Boundary

- [x] 6.1 Style old assessment setup, experiment rows, mode controls, question-count controls, exam cards, option rows, and submit actions with SYSU-red square visual language.
- [x] 6.2 Avoid importing modern `web-student` green H5 CSS, modern mobile primitives, TanStack router shell, Atom/RAG controls, or assistant context surfaces into old assessment.
- [x] 6.3 Ensure old assessment text fits supported mobile and desktop widths without overlapping the fixed bottom navigation.
- [x] 6.4 Preserve forbidden visible-term gating across setup, exam, loading, empty, validation, error, and result/report states.

## 7. Tests and Validation

- [x] 7.1 Add old student tests for the unified assessment setup page and absence of the previous one-button-only primary experience.
- [x] 7.2 Add old student tests for custom assessment option loading, experiment search/filtering, selection, question-count choice, and validation.
- [x] 7.3 Add old student tests for smart, selected, random, and all-range start requests and session route navigation.
- [x] 7.4 Add old student tests for old exam rendering of single-choice, true/false, and fill-blank questions.
- [x] 7.5 Add old student tests for incomplete-submit prevention and successful submit payload shape.
- [x] 7.6 Add old student tests proving point post-learning assessment opens the old exam page.
- [x] 7.7 Run old student typecheck, tests, and production build.
- [x] 7.8 Run relevant backend assessment route tests if backend adapters are added.
- [x] 7.9 Run `openspec validate enhance-legacy-assessment-flow --strict`.
