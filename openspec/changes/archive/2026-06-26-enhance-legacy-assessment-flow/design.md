## Context

The old student app already exists as a SYSU-red, square, hand-routed React product in `apps/web-student-old`. It currently has `主页`, `学习`, `评测`, and `我的`, but `评测` only starts smart assessment and shows a composition summary. That is not enough for the BKT competition story because students cannot choose a practice range, cannot visibly start weak-point testing from the same old page, and cannot take the generated exam inside an old-style interface.

The current student app already has the assessment mechanics:

- `AssessmentRootPage` separates `智能组卷` and `自主测评`.
- `AssessmentCustomPage` loads `/api/student/custom-assessment/options`, lets students select experiments, chooses a question count, and starts `/api/student/custom-assessment/start`.
- `AssessmentSessionPage`, `PosttestPanel`, and `AssessmentPanel` render and submit smart/custom/point sessions through `/api/student/smart-assessment/submit`.

The old assessment change should reuse those backend contracts and domain semantics while replacing the modern mobile experience with a traditional teaching-platform layout. The implementation must continue the established old-profile rules: shared backend/database identities, no old seed split, no Atom/RAG/Agent wording, and old-scoped backend adapters only when the shared API surface is insufficient.

## Goals / Non-Goals

**Goals:**

- Turn old `评测` into a complete setup page for BKT-driven weak-point testing and experiment-range practice.
- Merge the visible smart/custom entry choices into one old-style form instead of two modern cards.
- Provide mode choices for `智能薄弱项测试`, `自选实验范围`, `随机练习`, and `全部范围`.
- Reuse current assessment option/start/submit APIs and session identities.
- Add an old-style exam-taking page for generated smart/custom/point sessions.
- Preserve old visual language: SYSU red, square controls, form/table-like rows, old examination paper rhythm.
- Keep all assessment copy aligned with the BKT story: mastery, weak points, question coverage, post-learning assessment, and learning-score feedback.

**Non-Goals:**

- Do not redesign the modern `web-student` assessment flow.
- Do not add Atom, RAG, Agent, assistant, provider, retrieval, or model diagnostics to old assessment.
- Do not build a new question engine or duplicate BKT calculation logic.
- Do not create old-only question ids, experiment ids, session ids, or seed records.
- Do not require an old backend endpoint for the first implementation unless current APIs cannot express a required behavior.
- Do not implement teacher-side assessment configuration in this change.

## Decisions

### Decision: Use one old setup form instead of two entry cards

Old `评测` should not copy the modern root page that splits `智能组卷` and `自主测评` into two large cards. It should show one form-like page with mode controls, experiment multi-select rows, search, batch actions, question count, and one primary `开始测评` action.

Rationale: the old product is closer to a traditional educational management site than a modern app launcher. A single form makes the distinction between "algorithm chooses questions" and "student chooses range" visible without fragmenting the flow.

Alternative considered: keep a smart card and a custom card, then restyle both. Rejected because it preserves the modern product mental model and does not satisfy the requested "合二为一" page.

### Decision: Model smart/custom/random/all as modes over the same setup state

The page should maintain a local setup state:

```
mode: smart | selected | random | all
query: string
selectedExperimentIds: Set<string>
questionCount: number
```

Mode behavior:

- `smart`: calls `/api/student/smart-assessment/start`; selection controls may remain visible as context but do not drive the request.
- `selected`: requires at least one selected experiment and calls `/api/student/custom-assessment/start`.
- `random`: randomly selects eligible experiments from the current filtered or full option pool, then calls `/api/student/custom-assessment/start`.
- `all`: selects all eligible experiments, then calls `/api/student/custom-assessment/start`.

Rationale: current backend custom assessment already composes from selected experiments and question count. Random practice can be implemented safely as an old frontend selection convenience without introducing a new backend algorithm.

Alternative considered: add a backend random endpoint. Deferred because there is no current requirement for server-side seeded randomness, weighted randomization, or auditability.

### Decision: Reuse current assessment APIs and session storage semantics

Old frontend API types should be expanded to match `StudentCustomAssessmentOptionsResponse`, `StudentSmartAssessmentResponse`, `PublicSmartAssessmentQuestion`, and submit/report response shapes. Generated sessions should be stored in old sessionStorage under an old key prefix and routed to an old `/assessment/session/:sessionId` page.

Rationale: the backend already owns assessment composition, BKT update, and report creation. The old frontend only needs old visual presentation and routing.

Alternative considered: keep old `评测` as a summary-only page after starting an assessment. Rejected because it does not let the student complete the measurement loop.

### Decision: Build an old exam page by copying behavior, not modern styling

The old exam page may adapt the logic of `PosttestPanel` and `AssessmentPanel`:

- display session mode and composition;
- render question list;
- support single choice, true/false, and fill blank;
- keep local answer state;
- disable submit until all questions are answered;
- submit through `/api/student/smart-assessment/submit`.

It must not import modern `MobileButton`, `MobileField`, `DetailPageFrame`, modern green assessment CSS, or TanStack router dependencies. The page should render as old examination paper cards, with square options and a full-width submit button.

Rationale: behavior is mature in the current app, but presentation and routing would leak the modern product if imported wholesale.

Alternative considered: directly reuse `PosttestPanel` and `AssessmentPanel`. Rejected because their surrounding layout, class names, and mobile primitives are modern H5-specific.

### Decision: Point post-learning assessment should enter the same old exam page

The existing old point detail `进行学后测评` action should store the returned point-scoped assessment session and navigate to the old exam page rather than only displaying a summary on `/assessment`.

Rationale: point assessment is part of the same BKT feedback loop and should feel like a real test, not just a generated composition report.

Alternative considered: leave point assessment summary-only until later. Rejected because it creates inconsistent behavior: home `评测` can lead to an exam while point `进行学后测评` cannot.

### Decision: Preserve old-only backend isolation if backend support is later needed

If future implementation discovers that current APIs cannot supply enough old setup metadata, any backend addition must live under a legacy/old namespace or adapter and must not alter mainline student API semantics.

Rationale: this keeps the old product from changing the current green Atom/RAG product and follows the established old profile boundary.

Alternative considered: modify `/api/student/custom-assessment/options` to add old-only fields. Rejected unless the added fields are genuinely product-neutral and current frontend-compatible.

## Risks / Trade-offs

- [Risk] Large all-experiment selection may produce too many selected ids for custom assessment → Mitigation: use the existing backend max question count and display underfilled/warning messages from the response.
- [Risk] Frontend random selection is not auditable or repeatable → Mitigation: present it only as `随机练习`, not as a formal algorithmic recommendation; keep BKT smart mode separate.
- [Risk] Copying modern assessment logic can accidentally import modern green style or assistant wording → Mitigation: copy only type/answer handling logic into old files and add forbidden visible-term tests.
- [Risk] Existing old tests only cover summary generation → Mitigation: add tests for setup modes, start endpoints, session page rendering, answer submission, and point assessment routing.
- [Risk] Session refresh cannot reload a generated assessment from the backend by session id → Mitigation: store generated session payload in old sessionStorage; if missing, render a controlled old-style "请重新开始测评" state.
