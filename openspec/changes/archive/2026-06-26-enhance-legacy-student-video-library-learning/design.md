## Context

The old student frontend currently exists as a thin SYSU-red React app with a hand-rolled `pushState` router, a three-item navigation bar, a home video feed, smart assessment, reports, and native point-video playback. It shares the current backend and database, which is the correct data boundary for the legacy competition profile.

The current student frontend already has the richer learning mechanics needed for the demo: periodic-table metadata, profile matching, family/chapter catalog browsing, directory traversal, point detail loading, and video-library search. The implementation should selectively migrate those domain mechanics into the old student app while keeping the old product visually and narratively separate.

The most important product correction is home ownership: old `主页` is not a personalized `发现` feed and not an infinite recommendation stream. It is the old product's experiment video-point library, defaulting to all published point nodes, including points that do not yet have playable video media.

## Goals / Non-Goals

**Goals:**

- Make old student navigation four-part: `主页`, `学习`, `评测`, `我的`.
- Change old `主页` into a finite all-point experiment-video library with local search ownership.
- Add old `学习` as a periodic-table-driven catalog drilldown from element selection to point detail.
- Reuse current backend student APIs and published catalog/media data.
- Preserve SYSU-red, square, traditional teaching-platform styling.
- Preserve old forbidden-term and forbidden-route gates.
- Keep the change scoped to `web-student-old` unless a small shared typing or test adjustment is unavoidable.

**Non-Goals:**

- Do not change the modern `web-student` home, learning, Atom, search, or player behavior.
- Do not create a new backend endpoint for the first implementation.
- Do not create old-only seed data, old-only ids, or a parallel video catalog.
- Do not migrate the full TanStack Router app shell into old student.
- Do not add Atom/RAG/Agent, intelligent monitoring, learning assistant, provider diagnostics, or retrieval internals to old student.
- Do not redesign old `评测` and `我的` beyond route/nav alignment in this change.

## Decisions

### Decision: Treat old home as a finite point-node library

Old home should aggregate student-visible point nodes from the shared learning profile and catalog APIs. The no-query home should show all published experiment point nodes, including point nodes whose `published_media_count` is zero, not `topic=discover` or a playable-video-only feed.

Rationale: the lower-level competition story needs a straightforward experiment-video-point library. A personalized infinite stream implies the modern recommendation product, while a playable-video-only feed hides valid catalog point units that still belong in the old library.

Alternative considered: keep the current old home as `discover` or `home-video-feed?topic=all` and rename the copy. Rejected because `discover` is recommendation-first and playable-video feeds can omit no-video point units.

### Decision: Search belongs only to old home

Old home should expose a simple experiment-video search box. When a query is present, the UI should use an old-scoped lightweight point-library endpoint, render only student-facing video/point rows, and suppress modern no-query recommendations, recommended search terms, category chips, and learning-scope search sections.

Rationale: this matches the product model: `主页` is the video library and `学习` is the catalog locator. It also avoids the previously observed visual jump where recommendations appear in separate waves.

Alternative considered: reuse the modern `VideoLibraryPage` component. Rejected because it brings modern route assumptions, default recommendation sections, modern visual language, and optional learning-scoped search behavior.

Alternative considered: call the main `/api/student/video-library/search` endpoint from old home. Rejected for old home because that endpoint builds the full modern search payload, including browse/recommendation concepts that old intentionally hides and does not need.

### Decision: Keep old app routing lightweight

The old student app should continue using its current `pushState` router and add routes such as:

- `/` for video library home
- `/learn` for the periodic table learning root
- `/learn/chapter/:profileId` for family/chapter context
- `/learn/catalog/:nodeId` for catalog directory layers
- `/videos/:nodeId` for point detail
- `/assessment` and `/profile` or `/reports` for existing secondary surfaces

Rationale: importing the current router/app shell would blur old/new product boundaries and increase the chance of Atom/RAG leakage. The old app only needs a small route stack.

Alternative considered: add `@tanstack/react-router` to `web-student-old`. Rejected for this iteration because the old app does not need the full modern route system.

### Decision: Copy domain logic, restyle UI

The implementation may copy or adapt current student domain logic for:

- periodic element metadata and grid placement;
- element-to-learning-profile matching;
- learning page/profile API types;
- chapter catalog and catalog node API types;
- catalog node list behavior;
- point-detail API hydration.

It should not copy modern green styling, Atom controls, ArtPlayer/custom player chrome, assistant context builders, or modern mobile shell behavior.

Rationale: the chemistry navigation is useful product logic, while the modern visual and AI interaction layers are explicitly out of scope for old.

### Decision: Learning is a pure chemistry drilldown

Old `学习` should present this drilldown:

```
元素周期表
-> 元素/元素族对应章节
-> 性质分类或章节目录
-> 子目录
-> 点位详情
```

The learning module should not expose global search. If an element locator is ever added, it must only select/highlight periodic-table elements and must not call video-library/global search.

Rationale: the demo image and product story emphasize a clean subject-logic navigation path rather than a mixed search/recommendation product.

### Decision: Reuse native point detail treatment

Old point detail should continue using native browser video controls and traditional text sections. When opened from learning, it can reuse the same point detail component as home video entries, with the back target determined by source route.

Rationale: native playback is one of the visible old/new differentiators already required by the legacy profile.

### Decision: Keep any future old backend isolated

If the legacy competition profile needs backend behavior that existing shared student APIs cannot provide, the implementation should add old-scoped backend adapters, routes, schemas, or services instead of changing mainline student/teacher API behavior. Those routes should be visibly namespaced for the old product, for example with an `old` or `legacy` module/prefix, and should read shared published content identities rather than forking seed data.

Rationale: the old product is a competition/demo profile with intentionally different presentation and constraints. Its backend affordances must not create regressions in the current student H5, teacher admin, shared catalog, BKT, media, search, or seed validation flows.

Alternative considered: extend existing shared endpoints with old-specific flags. Rejected as the default approach because flags can make the main product carry legacy-only behavior and increase the risk that future mainline changes accidentally break the old profile or vice versa.

### Decision: Verify legacy backend changes with an old-only compose runtime

Legacy backend changes should be verified in a containerized runtime, but the runtime should be the old product slice, not the full application stack. The old compose target should start only the old backend-facing service and `web-student-old` / `web-teacher-old`, connect to the shared core database/media storage, and avoid starting current `web-student`, `web-teacher`, `web-admin`, Elasticsearch, video worker, or other mainline services unless a later old requirement explicitly needs them.

The smoke test pattern for old backend changes should include:

- build/restart the old backend service from source so Python route/schema changes are present in the running image;
- check `/health` and unauthenticated route boundaries, where applicable;
- execute the old service/query path against the real database schema, not only fake unit-test sessions, so missing-column or table-shape mismatches are caught;
- verify old-only association tables or adapters are created/used in isolation and clean up any recommendation toggles or test records after the check;
- confirm old frontend ports continue to serve the old UI.

Rationale: the `pc.id`/`pc.node_id` mismatch showed that fake-session unit tests can miss real schema errors. Container smoke tests are useful, but running the full compose stack is too heavy and can disturb unrelated current services. The old profile needs a narrow, repeatable validation path.

## Risks / Trade-offs

- [Risk] Copying current learning code can accidentally bring Atom/RAG strings or modern green styles. -> Mitigation: keep old components separate, scan old rendered UI and source for forbidden terms, and avoid importing assistant/player modules.
- [Risk] The all-point library may be large. -> Mitigation: keep the list finite and catalog-backed, with optional explicit "加载更多" only if it preserves finite point pagination and never repeats canonical point nodes as an infinite stream.
- [Risk] Search API default browse payload includes recommendations not wanted by old. -> Mitigation: old UI must ignore no-query browse sections and only render query result rows when a query is submitted.
- [Risk] Learning profile coverage can be incomplete for some elements. -> Mitigation: use the current profile matching fallback and show a controlled old-style empty state for elements without published learning profiles.
- [Risk] Old and current student learning behavior can drift. -> Mitigation: old should reuse current backend APIs and add old-specific tests around route flow, not fork backend data or seed identities.
- [Risk] Old-only backend needs can leak into mainline API behavior. -> Mitigation: use explicitly namespaced old backend modules/routes when backend work is unavoidable, and treat shared endpoint semantic changes as out of scope unless separately specified.
- [Risk] Container validation can accidentally restart unrelated mainline services. -> Mitigation: use the old-only compose runtime for old backend/frontend checks and reserve the full compose stack for whole-product validation.

## Migration Plan

1. Add old API types and functions for the legacy point-library endpoint, learning page, chapter catalog, catalog node, and point detail as needed.
2. Update old student navigation and route selection to support `主页`, `学习`, `评测`, and `我的`.
3. Convert old home from `discover` recommendation feed to finite catalog-backed point library and add home-only search behavior.
4. Add old periodic-table learning components and catalog drilldown components using SYSU-red/traditional styling.
5. Reuse old native point detail for both home and learning entry paths.
6. Add tests for forbidden terms, catalog-backed all-point home behavior, home search ownership, four-module navigation, periodic-table drilldown, and no old seed/backend fork.
7. Add an old-only compose runtime for legacy backend/student/teacher checks.
8. Run old student typecheck/tests, old backend route/service smoke tests against the real database schema, and OpenSpec validation.

Rollback is a normal frontend revert. No data migration is expected.

## Open Questions

- Whether `我的` should be a renamed report page (`/profile` or `/reports`) in the first implementation or a minimal profile shell with report links. The first implementation can keep it intentionally light because the user scoped this round to `主页` and `学习`.
