## 1. Data Contracts

- [x] 1.1 Add old student API types/functions for finite all-point home content using shared learning/catalog sources.
- [x] 1.2 Add old student API types/functions for query-based experiment video-library search, rendering only student-facing video/point results in old UI.
- [x] 1.3 Add old student API types/functions for learning page profiles, chapter catalog, catalog node children, and point detail.
- [x] 1.4 Confirm old student API wrappers reuse shared backend ids and do not introduce old-only seed, media, profile, or point identities.
- [x] 1.5 Specify that any necessary future old backend support must be isolated in old/legacy-scoped adapters or routes and must not change mainline student/teacher API semantics.
- [x] 1.6 Add an old-scoped lightweight point-library backend endpoint for legacy home default/search without changing the main video-library search endpoint.
- [x] 1.7 Add old-scoped teacher endpoints and storage for manually marking recommended learning points.

## 2. Navigation Shell

- [x] 2.1 Replace the old student three-item navigation with four first-level modules: `主页`, `学习`, `评测`, and `我的`.
- [x] 2.2 Keep old routing lightweight with `pushState` routes for home, learning root, learning chapter/profile, catalog directory, point detail, assessment, and profile/report surfaces.
- [x] 2.3 Preserve forbidden route redirects and forbidden visible term handling for Atom/RAG/Agent/monitoring/assistant/provider/retrieval wording.

## 3. Legacy Home Video Library

- [x] 3.1 Change old home no-query loading from personalized `discover` feed to finite catalog-backed point-library content.
- [x] 3.2 Update old home copy and empty/end states so the page presents itself as `实验视频库` or `全部视频`, not a personalized recommendation stream.
- [x] 3.3 Add a home-only search box that searches experiment-video content and renders one coherent result list without modern recommendation sections, category chips, or recommended search terms.
- [x] 3.4 Ensure old home does not repeat canonical point nodes as infinite-scroll filler; any additional loading remains finite point pagination.
- [x] 3.5 Keep home video card selection routed to old native/simple point detail using shared catalog identities.
- [x] 3.6 Switch old home default/search loading to the legacy point-library endpoint so it does not request modern browse/recommendation search payloads.
- [x] 3.7 Show `推荐学习` on recommended old student video-library cards and keep recommended point nodes ordered first.

## 4. Legacy Learning Drilldown

- [x] 4.1 Add old periodic-table data/helpers or old-scoped adapters based on the current student periodic-table semantics.
- [x] 4.2 Implement old `学习` root as periodic-table selection rather than a textbook chapter tree or searchable video page.
- [x] 4.3 Implement element-to-profile matching for exact element, family/group, and controlled unavailable states.
- [x] 4.4 Implement old family/chapter view with selected element context and catalog-backed property/category/directory/point entries.
- [x] 4.5 Implement directory-layer navigation that preserves profile/chapter context through nested catalog directories.
- [x] 4.6 Reuse old native/simple point detail for points opened from the learning drilldown and preserve a sensible back target.
- [x] 4.7 Ensure old learning surfaces do not expose global search, Atom model routes, AI assistant actions, RAG controls, or modern custom player chrome.
- [x] 4.8 Make periodic-table area chips selectable so `可学习章节` defaults to all profiles and filters dynamically by the selected element area.
- [x] 4.9 Render learning chapter cards using only the short family/chapter name inside parentheses, such as `卤素`, instead of the full `17族（卤素）` label.
- [x] 4.10 Simplify old chapter and directory drilldown pages so the top section only shows the element rail/current element card and the content section is a one-row-per-directory-or-point list.

## 5. Styling

- [x] 5.1 Style new old student navigation, home search/results, periodic table, chapter view, catalog rows, and empty states with SYSU-red/traditional square visual language.
- [x] 5.2 Keep old student styling independent from the modern green H5 theme and avoid importing modern shell/player/assistant CSS.
- [x] 5.3 Verify text fits on supported mobile and desktop widths without overlapping navigation, cards, or catalog rows.
- [x] 5.4 Keep the old student bottom navigation fully square with no rounded active tab treatment.
- [x] 5.5 Ensure the old periodic table shows the complete table, including separate lanthanide and actinide rows.

## 6. Tests and Validation

- [x] 6.1 Update old student tests for four-module navigation, default `主页`, and forbidden visible terms.
- [x] 6.2 Add old home tests proving no-query requests use finite catalog-backed all-point behavior, include no-video point nodes, and do not request `discover`.
- [x] 6.3 Add old home search tests proving search is home-owned and does not render modern recommendation/default browse sections.
- [x] 6.4 Add old learning tests for periodic-table selection, profile match, directory navigation, point detail opening, and unavailable element state.
- [x] 6.5 Run old student typecheck and tests.
- [x] 6.6 Run `openspec validate enhance-legacy-student-video-library-learning --strict`.
- [x] 6.7 Add old learning tests for area-chip filtering and short chapter-name rendering.
- [x] 6.8 Update old learning tests to assert chapter/directory pages omit extra headings, property grids, breadcrumbs, and other non-list content.

## 7. Legacy Runtime and Smoke Validation

- [x] 7.1 Add an old-only compose entrypoint for `backend-old`, `web-student-old`, and `web-teacher-old` without starting the full main stack.
- [x] 7.2 Document that old backend validation must rebuild/restart the old backend container before judging frontend failures.
- [x] 7.3 Document the real-database smoke-test pattern for old service queries so schema mismatches are caught outside fake-session unit tests.
- [x] 7.4 Document that old recommendation smoke tests must clean up temporary toggles and leave old-only association storage isolated.

## 8. Point Detail Correction

- [x] 8.1 Replace old point-detail `BKT 后续建议` copy with related experiment links.
- [x] 8.2 Add a full-width `进行学后测评` action that starts point-scoped post-learning assessment.
- [x] 8.3 Update old point-detail tests to assert related experiment links, no synthetic BKT suggestion block, and point-scoped assessment startup.

## 9. Home Video Library Ordering

- [x] 9.1 Sort old home default and search results by playable video availability first, then teacher recommendation within each video-availability group.
- [x] 9.2 Update old backend tests to prove recommended no-video points cannot outrank ordinary points that already have playable video.

## 10. Point Detail Back Routing

- [x] 10.1 Make old point-detail return behavior respect the opening source: home-opened points show `返回首页`, learning-opened points show `返回学习目录`.
- [x] 10.2 Make old learning-opened point detail resolve `返回学习目录` from the point breadcrumb/catalog path to the owning catalog directory.
- [x] 10.3 Add old student tests proving home-opened point detail returns to the home video library while learning-opened point detail keeps the learning-directory action.

## 11. Drilldown Breadcrumb

- [x] 11.1 Render an old-style `元素周期表 / 当前章节` breadcrumb in chapter and directory drilldown top bars.
- [x] 11.2 Add old student tests proving the breadcrumb returns to the periodic-table learning root.

## 12. Legacy Thumbnail Routes

- [x] 12.1 Return old home video-library thumbnails through student-accessible media thumbnail API routes instead of raw storage-relative paths.
- [x] 12.2 Add backend and frontend tests covering old thumbnail route output.
