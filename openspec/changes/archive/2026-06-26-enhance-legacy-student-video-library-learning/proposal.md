## Why

The current old student frontend is intentionally separate and SYSU-red, but it is still too thin for the lower-level competition demo: its home is a personalized recommendation feed and it has no dedicated chemistry learning navigation. For this profile, the old student product must feel like a traditional inorganic chemistry experiment learning platform where the home is a finite "all experiment video points" library and the learning module is a pure element-to-experiment catalog.

## What Changes

- Replace the old student home meaning from `BKT personalized recommendation stream` to a finite experiment video-point library that defaults to all published point nodes, including point nodes with no playable video yet.
- Add a four-module old student navigation: `主页`, `学习`, `评测`, `我的`.
- Keep `主页` focused on the video library and make it the only old student surface with experiment-video search.
- Serve old `主页` default list and search through a legacy-scoped lightweight point-library endpoint when the modern video-library search payload is unnecessarily broad.
- Add a `学习` module that uses a periodic-table entry and drills through element family/chapter, catalog directories, and experiment point detail.
- Preserve the old product boundary: no Atom, RAG, Agent, learning assistant, intelligent monitoring, provider, retrieval, chunk, embedding, or custom-player exposure.
- Reuse the current backend, catalog, media, BKT, assessment, and learning-profile data without adding old-only seed data or old-only ids.
- If old-specific backend behavior becomes necessary, add it as isolated legacy/old backend adapters or routes instead of changing mainline student or teacher API semantics.
- Leave old `评测` and `我的` mostly as existing/placeholder surfaces for this change, except for navigation label alignment.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `bkt-legacy-competition-profile`: Specify the old student home video-point library behavior, four-module navigation, periodic-table learning drilldown, search ownership, and continued data-sharing boundaries.

## Impact

- Affected frontend code: `apps/web-student-old/src/LegacyStudentApp.tsx`, `apps/web-student-old/src/api.ts`, `apps/web-student-old/src/styles.css`, and old student tests.
- Referenced frontend source for migration: current student periodic-table, learning entry, family catalog, catalog node, video-library search, and point-detail data contracts.
- Affected backend APIs: reuse existing student APIs such as `/api/student/learning-page`, `/api/student/chapters/{chapter_id}/catalog`, `/api/student/catalog/nodes/{node_id}`, and `/api/student/catalog/points/{node_id}`, plus an old-scoped `/api/student/legacy/video-points` adapter for the old home point library.
- Affected deployment code: add an old-only compose entrypoint (`docker-compose.old.yml`) for legacy backend/student/teacher validation without starting the full main application stack.
- Future backend impact constraint: any backend code introduced solely for the old profile must be old-scoped and must not alter current `web-student`, `web-teacher`, or shared API behavior.
- No database migration, seed split, new backend service, or old-only chemistry data mutation is expected.
