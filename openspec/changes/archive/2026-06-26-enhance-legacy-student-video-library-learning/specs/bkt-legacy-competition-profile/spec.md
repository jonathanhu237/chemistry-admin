## ADDED Requirements

### Requirement: Legacy runtime validation uses an old-only compose boundary
The legacy product SHALL provide a compose entrypoint that validates the old student, old teacher, and old-scoped backend runtime without starting the unrelated mainline application stack.

#### Scenario: Maintainer starts the legacy runtime
- **WHEN** a maintainer needs to run or validate the old competition profile in containers
- **THEN** they MUST be able to use an old-specific compose file or profile that starts only the old frontend services and the backend surface needed by old
- **AND** the runtime MUST NOT start current `web-student`, `web-teacher`, `web-admin`, Elasticsearch, video worker, or other mainline-only services by default
- **AND** old student MUST default to port `15176`
- **AND** old teacher MUST default to port `15177`
- **AND** the old runtime MAY connect to the shared core database and media storage rather than creating a parallel old database

#### Scenario: Maintainer verifies old backend changes
- **WHEN** old-scoped backend routes, schemas, services, or association tables are changed
- **THEN** validation MUST rebuild or restart the old backend runtime so Python changes are present in the running container
- **AND** validation MUST check backend health and route registration/auth boundaries
- **AND** validation MUST execute the old service or endpoint path against the real database schema, not only mocked sessions
- **AND** validation MUST prove old-only storage such as recommended-learning association tables is isolated from main catalog/media/BKT identities
- **AND** any temporary recommendation toggles or smoke-test rows MUST be removed after validation
- **AND** a real-schema failure such as a missing SQL column MUST block acceptance until fixed

### Requirement: Legacy student navigation exposes four first-level modules
The legacy student product SHALL expose four first-level modules labeled `主页`, `学习`, `评测`, and `我的`.

#### Scenario: Legacy student opens the old product
- **WHEN** an authenticated student opens `web-student-old`
- **THEN** the first-level navigation MUST show exactly the student modules `主页`, `学习`, `评测`, and `我的`
- **AND** `主页` MUST be the default active module
- **AND** the bottom navigation active tab treatment MUST remain square with no rounded modern-pill styling
- **AND** the navigation MUST NOT show Atom, RAG, Agent, learning assistant, intelligent monitoring, provider, or retrieval-diagnostic entries

#### Scenario: Student switches modules
- **WHEN** the student selects a first-level module
- **THEN** the old app MUST route to that module without loading the modern student app shell
- **AND** current `web-student` routes and navigation MUST remain unchanged

### Requirement: Legacy student home is a finite all-point video library
The legacy student `主页` SHALL behave as an experiment video-point library that defaults to all student-visible experiment point nodes, not as a personalized discovery or infinite recommendation stream.

#### Scenario: Student opens legacy home without a query
- **WHEN** an authenticated student opens old `主页` without a search query
- **THEN** the page MUST render published experiment point nodes from the finite video-point library
- **AND** point nodes MUST be shown whether or not they currently have bound playable video media
- **AND** the data request MUST use shared student learning/catalog APIs or an equivalent finite all-point data source
- **AND** the page MUST NOT request or render the personalized `发现`/`discover` stream as the primary home content
- **AND** the page MUST NOT repeat canonical point nodes merely to keep the home scrolling

#### Scenario: Legacy home copy is inspected
- **WHEN** visible old `主页` copy is inspected
- **THEN** the page MUST present itself as `实验视频库`, `全部视频点位`, or equivalent all-point video-library wording
- **AND** it MUST NOT describe the primary home list as a personalized recommendation feed, discovery stream, or infinite recommendation flow
- **AND** BKT recommendation wording, if present elsewhere in old student, MUST NOT redefine old `主页` as personalized video recommendation

#### Scenario: Legacy home reaches the end of available point nodes
- **WHEN** all matching video-point library items have been loaded for the current old home view
- **THEN** the page MUST stop showing more items
- **AND** any additional loading control MUST preserve finite all-point pagination
- **AND** the page MUST render a controlled old-style empty or end state rather than cycling point nodes

### Requirement: Legacy student search is owned by the home video library
The legacy student product SHALL provide experiment-video search only from `主页`.

#### Scenario: Student searches from legacy home
- **WHEN** the student enters a query on old `主页`
- **THEN** the app MUST search within student-visible experiment video and point content
- **AND** the results MUST replace or filter the home video-library list in one coherent result view
- **AND** the results MUST route video or point selections to old point detail using shared catalog identities
- **AND** the search MAY use an old-scoped lightweight backend endpoint when the main video-library search endpoint is too broad or slow for the legacy surface
- **AND** the page MUST NOT render modern no-query recommendation sections, recommended search terms, category chips, or learning-scope search panels

#### Scenario: Student opens legacy learning
- **WHEN** the student opens old `学习`
- **THEN** the page MUST NOT show the old home video-library search box
- **AND** it MUST NOT provide a global search entry for videos, directories, Atom, RAG, or all-site content
- **AND** any future element locator in the periodic table MUST only select or highlight elements and MUST NOT call video-library search

### Requirement: Legacy student learning uses periodic-table catalog drilldown
The legacy student `学习` module SHALL provide a chemistry-logic navigation path from periodic table selection to catalog directories and point detail.

#### Scenario: Student opens legacy learning root
- **WHEN** an authenticated student opens old `学习`
- **THEN** the page MUST show a periodic-table entry surface rather than a textbook chapter tree as the first learning surface
- **AND** the page MUST load available learning profiles from the shared student learning API
- **AND** the periodic table MUST render a complete table including separate lanthanide and actinide rows
- **AND** the page MUST use old SYSU-red/traditional styling rather than the current green modern H5 shell

#### Scenario: Student filters learning chapters by periodic-table area
- **WHEN** the student opens old `学习`
- **THEN** `可学习章节` MUST default to all loaded learning profiles
- **WHEN** the student selects an element-area chip such as `p区元素` or `s区元素`
- **THEN** `可学习章节` MUST update to only profiles whose element symbols belong to the selected area
- **AND** selecting the same area again MAY clear the area filter and restore all profiles
- **AND** learning chapter cards MUST show only the short family or chapter name inside parentheses, such as `卤素`, not the full `17族（卤素）` label

#### Scenario: Student selects an element with a matching learning profile
- **WHEN** the student selects an element on the old periodic table and a matching family or chapter profile exists
- **THEN** the app MUST open the matching family or chapter learning view
- **AND** the view MUST preserve selected element context where available
- **AND** the app MUST NOT open an Atom model, AI assistant, or modern element-detail route as the primary action

#### Scenario: Student browses family or chapter content
- **WHEN** the student is on a family or chapter learning view
- **THEN** the page MUST show catalog-backed learning entries such as property categories, directories, subdirectories, and point entries for the selected profile
- **AND** selecting a directory MUST move to that directory layer while preserving profile/chapter context
- **AND** selecting a point MUST open old point detail for that point
- **AND** unavailable, draft, archived, or unplayable student-hidden content MUST NOT be rendered as normal learning entries

#### Scenario: Student views old chapter or directory drilldown
- **WHEN** the student is on an old family/chapter view or a nested directory view
- **THEN** the upper section MUST show only the same-family element cards and the current selected element card
- **AND** the drilldown top bar MUST show an old-style breadcrumb entry for `元素周期表` plus the current chapter label, where `元素周期表` returns to the periodic-table root
- **AND** the content section MUST render each directory or video point as one full-width row entry
- **AND** the view MUST NOT render extra chapter hero copy, property-card grids, breadcrumb strips, or directory-positioning description blocks

#### Scenario: Student opens point detail from legacy learning
- **WHEN** the student opens a point from the old learning drilldown
- **THEN** point detail MUST use the old native/simple video treatment
- **AND** point detail MUST show traditional experiment content sections such as phenomenon, principle, safety, or learning notes when available
- **AND** point detail MUST show related experiment links when the shared point-detail payload provides related points
- **AND** related experiment links MUST open the old native/simple point detail using shared catalog node identities
- **AND** point detail opened from old `主页` MUST show `返回首页` and navigate back to the old home video library
- **AND** point detail opened from old `学习` MUST show `返回学习目录` and navigate to the owning catalog directory for the current experiment point
- **AND** point detail MUST provide a full-width `进行学后测评` action after the learning content and related experiment links
- **AND** the `进行学后测评` action MUST start a point-scoped post-learning assessment for the current point
- **AND** point detail MUST NOT render the modern custom player chrome, Atom action surface, RAG explanation controls, or assistant context tools
- **AND** point detail MUST NOT render a synthetic `BKT 后续建议` content block in place of related experiment links or the assessment action

#### Scenario: Selected element has no published profile
- **WHEN** the student selects an element that cannot be mapped to a published learning profile
- **THEN** the app MUST render a controlled old-style unavailable state
- **AND** it MUST NOT expose raw backend errors, seed identifiers, retrieval internals, or provider/model wording

### Requirement: Legacy student enhancement preserves shared data boundaries
The legacy student video library and learning drilldown SHALL reuse current backend data and MUST NOT create a parallel old content corpus.

#### Scenario: Legacy student loads video and learning content
- **WHEN** old `主页` or `学习` loads videos, learning profiles, directories, or point details
- **THEN** it MUST call shared backend APIs and use shared catalog, media, learning-profile, assessment, and mastery identities
- **AND** it MUST NOT require old-only seed records, old-only media bindings, old-only point ids, or a separate old database

#### Scenario: Legacy student implementation is inspected
- **WHEN** maintainers inspect the old student implementation
- **THEN** any copied or adapted periodic-table and catalog logic MUST remain scoped to the old frontend or shared frontend-safe utilities
- **AND** it MUST NOT modify chemistry seed data, production resource manifests, BKT model state, or current student app behavior merely to support the old UI

#### Scenario: Legacy backend support becomes necessary
- **WHEN** the old competition profile requires backend support that cannot be satisfied by existing shared student APIs
- **THEN** the implementation MUST add old-scoped backend adapters, routes, schemas, or services rather than changing existing mainline student or teacher API semantics
- **AND** any old-scoped backend route MUST be clearly namespaced for the legacy product, such as an `old`/`legacy` module or route prefix
- **AND** the old-scoped backend MAY read shared database tables and shared published content identities
- **BUT** it MUST NOT require old-only seed records, mutate shared seed/resource manifests, fork catalog/media/BKT identities, or change the behavior of current `web-student`, `web-teacher`, or shared API clients

#### Scenario: Legacy home uses an old-scoped point library endpoint
- **WHEN** old `主页` loads its default point list or query results
- **THEN** it MAY call a legacy namespaced endpoint that returns only old-home point-library fields
- **AND** that endpoint MUST include published point nodes without playable video media
- **AND** point nodes with playable published video media MUST be returned before point nodes without playable video media
- **AND** point thumbnails returned by the endpoint MUST use student-accessible media thumbnail API routes rather than raw media storage-relative file paths
- **AND** teacher-selected recommended learning points MUST be returned before ordinary point nodes only within the same video-availability group
- **AND** it MUST NOT return modern browse recommendations, AI prompt targets, diagnostic metadata, provider names, retrieval fields, or category-chip payloads
- **AND** current mainline video-library search and home-feed endpoints MUST keep their existing response shapes and semantics

#### Scenario: Teacher sets legacy recommended learning points
- **WHEN** a teacher or admin opens the legacy teacher backend
- **THEN** they MUST be able to mark or unmark published experiment point nodes as `推荐学习`
- **AND** the setting MAY be stored in an old-scoped association table separate from the main catalog identity tables
- **AND** marked points MUST show a `推荐学习` label in the old student video library
- **AND** marked points MUST be ordered before ordinary points within the same video-availability group in the old student video library
