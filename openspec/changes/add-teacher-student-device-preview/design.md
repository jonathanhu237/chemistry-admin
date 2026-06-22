## Context

The repository already has three separate frontend products: `web-student` for the student H5 app, `web-teacher` for teacher workflows, and `web-admin` for platform operations. The student app owns mobile learning routes, shell context, auth token handling, app-config feature flags, assessment, assistant, feedback, catalog navigation, and styles. The teacher app already contains a point-level catalog preview window using `react-device-mockup` plus an iframe, and the backend already mints point-scoped preview tokens for draft point detail/media access.

The new requirement is broader: teachers need a page in the teacher console that behaves like a Chrome DevTools Device Mode subset for the full student app. The page is for visual review, interaction review, and guidance. Teachers do not need to select a real student identity, do not need to inspect preview writes in analytics, and do not need a browser debugger. Each teacher should get one default test student under a hidden preview class. Ordinary teacher class management must not show this hidden class; `web-admin` must be able to manage and audit it.

The key architectural constraint is that the teacher preview must not become a second student frontend. If student pages, styles, routes, or interaction logic change in `web-student`, the teacher preview must reflect those changes automatically. Any preview-only differences must be introduced through a small preview runtime layer, backend policy, route guards, and API write guards rather than component forks.

## Goals / Non-Goals

**Goals:**

- Provide a teacher-console full student H5 preview that uses the real `web-student` SPA inside a phone-sized iframe shell.
- Give every teacher one system-managed hidden preview class and one default test student account/session.
- Keep hidden preview classes invisible in ordinary teacher class/roster workflows while making them visible and manageable in `web-admin`.
- Support future preview-only differences, such as blocking feedback or synthetic-success write responses, without copying student pages or sprinkling page-local preview branches.
- Keep preview implementation route-owned and feature-local so teacher shell, student shell, backend routers, and web-admin remain maintainable.
- Preserve existing point-preview behavior where practical by extracting reusable device-shell primitives instead of duplicating device preset code.

**Non-Goals:**

- Do not embed Chrome DevTools or expose DOM/network/debugger tools inside the teacher console.
- Do not simulate full browser-level emulation such as real user-agent override, CPU throttling, network shaping, native virtual keyboard, or browser chrome.
- Do not import student business page components into `web-teacher` or recreate student UI markup in teacher modules.
- Do not allow teachers to choose arbitrary real student identities in this change.
- Do not require preview writes to appear in teacher analytics, student reports, or class learning dashboards.
- Do not redesign the student H5 visual system as part of this change.

## Decisions

### Decision 1: Use an iframe shell around the real student SPA

The teacher preview page will be a `web-teacher` feature module that owns only the device shell, toolbar, iframe lifecycle, preview-session request, and shell-level styles. The iframe `src` will point at a `web-student` preview bootstrap URL returned by the backend, for example `/preview/session?ticket=...`.

The device shell may reuse or extract logic from the existing catalog point preview window:

- curated iPhone/Android presets
- portrait/landscape dimensions
- zoom levels
- refresh-by-key iframe reload
- external-open command
- optional shell-level drag/zoom gestures

The iframe content remains the real student app. The teacher preview shell does not render student pages, does not import student route components, and does not own student feature state.

Alternatives considered:

- Embedding Chrome DevTools frontend: rejected because it is a debugger UI, not a teacher product surface, and most device emulation powers rely on browser internals/CDP rather than normal web app code.
- Rebuilding student pages inside `web-teacher`: rejected because it creates a permanent duplicate UI that will drift from student code and styles.
- Using module federation to mount student React components in teacher React: rejected for this phase because it would couple two app runtimes, routers, providers, package versions, and CSS cascades. An iframe keeps product boundaries cleaner and matches the existing preview direction.

### Decision 2: Bootstrap through a teacher-owned test student session

The teacher app requests a preview session from a teacher-console endpoint:

`POST /api/admin/student-preview/session`

The backend verifies the teacher-console user, ensures a hidden preview class and test student exist for that teacher, mints a short-lived one-time ticket, and returns the student preview URL plus expiry metadata. The student app opens `/preview/session?ticket=...`, exchanges the ticket through a preview endpoint, stores the returned student preview token with the normal student auth mechanism or an explicit preview token slot, and redirects to `/home`.

The resulting request context is still a student role/session, but it carries preview claims such as:

- `preview: true`
- `preview_purpose: teacher_student_device_preview`
- `teacher_user_id`
- `preview_class_id`
- `preview_student_id`
- ticket/session expiry

This keeps the existing student API and router behavior usable while giving backend policy enough context to block, rewrite, or isolate unsupported preview actions.

Alternatives considered:

- Teacher token directly calls student APIs: rejected because existing student route contracts correctly reject teacher/admin roles and should not be weakened.
- Public unauthenticated preview API for every student endpoint: rejected because it would duplicate the student API surface and increase authorization risk.
- Requiring teachers to manually log into a test student: rejected because it defeats the goal of a one-click teacher workflow.

### Decision 3: Model hidden preview classes explicitly

Preview classes and preview students should be ordinary-enough records to reuse roster/student auth infrastructure, but they must be explicitly classified as system preview data. The exact schema can be chosen during implementation, but it must support:

- a class purpose/type such as `teacher_preview`
- owner teacher user id
- system-managed flag
- visibility or listing scope
- preview student account/roster classification
- stable one-to-one teacher to preview class/test student mapping
- timestamps and audit metadata

Ordinary teacher class list APIs must exclude preview classes by default. `web-admin` endpoints can list, inspect, reset, disable, or recreate preview classes/test students for operational support. These operations must be platform governance, not duplicated teacher class workflows.

Alternatives considered:

- Store test-student identity only in token claims without class/roster records: rejected because student APIs expect student/class context and web-admin needs auditability.
- Reuse a single global preview student for all teachers: rejected because it creates cross-teacher state collisions and makes operational audit/debug unclear.
- Show the preview class in the teacher class page with a hidden label: rejected because it pollutes normal class management and can confuse teachers.

### Decision 4: Preview differences are policy-driven, not page forks

The student app will get a thin preview runtime extension point. That layer may include:

- preview bootstrap route
- preview-aware app-config response
- `previewMode` and `previewPolicy` in student runtime context
- centralized route guard/visibility helpers
- centralized API behavior for preview media/auth and unsupported writes

Future differences must follow this priority order:

1. Backend preview policy or endpoint guard.
2. Student app-config feature flags and preview policy.
3. Central route guard or navigation visibility helper.
4. Shared shell/entry component behavior.
5. Page-local preview logic only when the difference cannot be expressed centrally, with explicit tests and review.

Examples:

- Feedback hidden in preview: `app-config` disables the entry; direct route is guarded; backend rejects or returns controlled synthetic behavior.
- Assessment allowed for interaction only: test-student session may create preview/test-owned state; the data is excluded from normal analytics.
- Password/profile account mutation blocked: backend rejects preview claims and the student route shows a controlled unavailable state.

This design accepts a small, intentional preview runtime hook in `web-student`. It rejects widespread page-local `if preview` checks and any teacher-side copy of student page UI.

### Decision 5: Web-admin governs preview infrastructure

`web-admin` expands to include platform operations for hidden preview classes/test students. It should not gain teacher learning workflows, catalog editors, question banks, analytics, or student app pages. Its preview management surface should be operational:

- list preview classes/test students
- inspect owner teacher and status
- reset or recreate a teacher's preview student
- disable or restore preview infrastructure
- view last session metadata and cleanup status where available

The backend owner must be `/api/web-admin/*` under platform token authorization. Teacher session creation remains `/api/admin/student-preview/*` under teacher-console authorization.

Alternatives considered:

- Put preview class management in `web-teacher`: rejected because ordinary teachers should not manage hidden system classes.
- Hide preview records from all UI and rely on database access: rejected because support/audit would become opaque and risky.

### Decision 6: Verification must prove reuse and boundaries

The change should include tests and checks that fail if implementation drifts into duplicated frontend code or mixed product ownership:

- teacher preview shell tests assert iframe URL/session loading and device controls
- student tests assert preview bootstrap redirects to normal student routes and uses normal student shell
- route guard tests assert disabled preview features are blocked centrally
- backend tests assert hidden preview classes are excluded from teacher class list APIs
- web-admin tests assert preview classes can be listed/managed only via platform endpoints
- import-boundary or source checks assert `web-teacher` does not import `web-student` route/page modules
- typecheck/build for `web-teacher`, `web-student`, and `web-admin`
- targeted browser/screenshot QA for the preview shell at common device presets

This explicit verification is important because the easiest implementation shortcut is to copy student UI into the teacher console. The tests should make that shortcut expensive.

## Risks / Trade-offs

- [Risk] Preview sessions accidentally pollute normal analytics or teacher dashboards. -> Mitigation: classify preview classes/students and preview token claims; exclude them from normal class/analytics queries; add backend tests for exclusions.
- [Risk] Future feature blocking becomes scattered across student pages. -> Mitigation: require preview policy, app-config, route guard, and backend guard first; only allow page-local exceptions with tests.
- [Risk] Iframe origin/CSP settings block local or deployed preview. -> Mitigation: define explicit environment variables for student app base URL and allowed frame origins; test local ports and production-like origins.
- [Risk] Student app auth storage conflicts with a teacher's real student login in the same browser. -> Mitigation: use a preview-specific token key or clearly scoped bootstrap/session handling if normal localStorage would overwrite real student sessions.
- [Risk] Hidden preview class lifecycle creates orphan records. -> Mitigation: make ensure/reset idempotent, store owner metadata, expose web-admin cleanup/reset actions, and add unique constraints for one active preview class/test student per teacher.
- [Risk] Device shell is mistaken for complete mobile emulation. -> Mitigation: product copy and requirements restrict it to viewport/device-shell simulation, not Chrome DevTools or real device emulation.
- [Risk] Existing point preview and new full preview duplicate device code. -> Mitigation: extract reusable device-shell primitives or share a feature-local module during implementation.

## Migration Plan

1. Add data classification fields and migration for preview classes/test students, including indexes/constraints for teacher ownership and listing filters.
2. Add backend service functions to ensure/reset teacher preview class and test student records idempotently.
3. Add teacher-console preview session endpoint returning a short-lived student bootstrap URL.
4. Add student preview ticket exchange and preview-aware auth/session claims.
5. Add student preview bootstrap route and runtime policy plumbing.
6. Add teacher preview page using a feature-local device shell and iframe.
7. Add web-admin preview infrastructure page and platform endpoints for listing/resetting hidden preview records.
8. Add backend exclusions so preview classes/students do not appear in ordinary teacher class workflows or normal analytics.
9. Add tests and browser QA for device shell, session bootstrap, policy/guard behavior, web-admin governance, and product/import boundaries.
10. Optionally refactor existing catalog point preview to use the shared device-shell primitives once the full preview shell is stable.

Rollback is safe if feature-gated: disable the teacher preview route and session endpoint while leaving hidden preview records inert. The student app should continue to run normal student sessions when no preview ticket is present.

## Open Questions

- Exact schema names for class/account classification can be chosen during implementation, but they must be explicit and queryable rather than hidden in opaque JSON only.
- Whether preview auth should reuse the normal student localStorage token key or use a preview-specific token key depends on how often teachers may also open `web-student` directly in the same browser.
- The first implementation can block or disable feedback/real account mutation broadly; later changes can refine individual preview policies once product needs are clearer.
