# student-h5-video-discovery Specification

## Purpose
Define student H5 experiment-video discovery across the home feed and the second-level video search/browse page, while keeping discovery rooted in published catalog point learning content.
## Requirements
### Requirement: Student home video feed API
The backend SHALL provide an authenticated student home video feed API that returns paged, playable, catalog-backed experiment video cards for the student H5 home root.

#### Scenario: Student requests the home video feed
- **WHEN** an authenticated student requests the home video feed
- **THEN** the response MUST include feed items with stable point placement identity, canonical point identity, chapter identity, student-visible title, summary or snippet, catalog path, display badges, video resource paths, and a point-detail route target
- **AND** each feed item MUST expose enough media data for inline preview, including stream path, optional thumbnail path, and optional duration
- **AND** each feed item MUST expose whether the current student has saved the item for `稍后学习`
- **AND** each feed item SHOULD expose whether the current student has favorited the item when that state is needed for visible controls
- **AND** the response MUST include the resolved feed topic, a nullable opaque next cursor, whether more items are available, the requested batch size, the candidate pool size, and the active repeat mode

#### Scenario: Student requests a paged batch
- **WHEN** an authenticated student requests `/api/student/home-video-feed` with `topic`, `limit`, and an optional cursor
- **THEN** the backend MUST return at most the bounded limit of items for that topic
- **AND** the cursor MUST be treated as an opaque value by clients
- **AND** the backend MUST reject, ignore, or recover from stale or invalid cursors in a controlled way without exposing cursor internals to the client
- **AND** a cursor from one topic MUST NOT be used to continue a different topic stream

#### Scenario: Feed item instance identity is returned
- **WHEN** the feed API returns any item
- **THEN** the item MUST include a stable canonical item id for the catalog placement and media asset
- **AND** the item MUST include an instance id that is unique for that rendered occurrence in the current feed stream
- **AND** repeated appearances of the same canonical video MUST use distinct instance ids
- **AND** navigation and point-detail routing MUST continue to use the existing point, placement, canonical point, media, and route target identities rather than the instance id

#### Scenario: Discover topic repeats as an infinite stream
- **WHEN** the resolved topic is `发现` and at least one playable candidate exists
- **THEN** the feed API MUST allow repeated canonical videos across batches
- **AND** the response MUST provide a next cursor for continuing the stream
- **AND** repeated items MUST remain catalog-backed and student-visible
- **AND** the backend SHOULD avoid immediate repeats when the candidate pool is large enough to do so

#### Scenario: Finite topic reaches the end
- **WHEN** the resolved topic is `稍后学习`, `全部`, or an experiment-observation topic and all matching playable candidates have already been returned for the current stream
- **THEN** the feed API MUST return no next cursor
- **AND** it MUST report that no more items are available
- **AND** it MUST NOT repeat canonical videos merely to keep that finite topic scrolling

#### Scenario: Watch-later topic returns personal saved videos
- **WHEN** the resolved topic is `稍后学习`
- **THEN** the feed API MUST return only playable videos that the current student has actively saved for later learning
- **AND** the topic MUST be finite and non-repeating
- **AND** hidden, unpublished, archived, or unplayable saved videos MUST be omitted from the visible feed
- **AND** the ordering MUST be stable and SHOULD show newest saved items first

#### Scenario: Feed filters hidden or unplayable content
- **WHEN** catalog points, point content, ancestor directories, media bindings, or media assets are draft, unpublished, archived, unready, or otherwise hidden from students
- **THEN** the feed API MUST NOT include those items
- **AND** the feed MUST include only point placements with at least one published playable video

#### Scenario: Feed has no playable videos
- **WHEN** no published playable experiment videos are available
- **THEN** the API MUST return an empty item list with a controlled empty status or message
- **AND** the frontend MUST render an educational empty state rather than falling back to unrelated home action cards

#### Scenario: Topic recall does not own playback data
- **WHEN** Elasticsearch or another retrieval index is used to find candidate point ids for a home topic
- **THEN** the home feed API MUST still hydrate stream paths, thumbnail paths, media ids, duration, route targets, titles, and catalog context from catalog and media data
- **AND** the student video-library search document MUST NOT become the playback data contract for the home feed

### Requirement: Home renders horizontal experiment video cards
The student H5 home root SHALL render the experiment video feed as a single-column, Bilibili-like mobile video card stream that is optimized for browsing and entry, not for completing per-card tool actions.

#### Scenario: Student opens home with feed items
- **WHEN** a student opens `/home` and feed items exist
- **THEN** the page MUST render each item as a 16:9 video preview or poster card
- **AND** the card MUST visually prioritize the experiment video as the dominant card element
- **AND** the card MUST render the experiment title as the first text content below the media
- **AND** the title MUST be left-aligned without a channel avatar, circular learning icon, or synthetic creator identity
- **AND** the title MUST be visually smaller and quieter than a second-level point-detail heading
- **AND** the title MUST be protected to at most two visual lines on supported phone widths
- **AND** the card MUST show compact learning metadata derived from the feed item after the title
- **AND** the metadata MUST render as subdued text in one visual row using `A · B · C` style separators when multiple metadata parts exist
- **AND** the metadata MUST NOT render as green pill chips, category buttons, or other visually primary controls
- **AND** the card MUST NOT render a visible per-card action toolbar, `查看实验` CTA, Atom chip, like button, bookmark button, share button, or social counter controls on the home feed
- **AND** the card MAY render exactly one vertical-more overflow trigger beside the title or title block
- **AND** the card MUST NOT render as a vertical Shorts player or a two-column thumbnail grid

#### Scenario: Feed card preserves textbook context
- **WHEN** a feed card is displayed
- **THEN** the card MUST preserve chapter or catalog context derived from the published point placement through the subdued metadata row
- **AND** source text after the primary title, including chapter labels, reaction labels, chemistry equation labels, reagent labels, or catalog section labels, MUST be eligible to appear as metadata row parts
- **AND** metadata parts MUST be de-duplicated where practical and MUST avoid repeating the primary title
- **AND** the metadata row MUST be protected to one visual line with truncation or ellipsis on supported phone widths
- **AND** the card MUST NOT show the catalog path as the first text line above the title
- **AND** tapping the media area, title area, metadata row, or non-overflow card body MUST route to the point video detail page rather than to a generic video-only player
- **AND** tapping the overflow trigger MUST open the home video overflow menu rather than routing to point detail

#### Scenario: Home keeps root tab identity
- **WHEN** the student is viewing the home video feed
- **THEN** the bottom navigation MUST continue to identify `首页` as the active root tab
- **AND** the feed MUST leave safe space for the bottom navigation on phone viewports
- **AND** opening or closing a home video overflow menu MUST NOT change the active root tab identity
- **AND** the home feed MUST preserve the root page's window-level scroll behavior so header and bottom navigation compression still responds to page scrolling

### Requirement: Muted one-card autoplay preview
The student H5 home video feed SHALL support muted inline autoplay preview with only one active card playing at a time.

#### Scenario: A feed card becomes the primary visible item
- **WHEN** a feed card becomes the most visible card in the main viewport and passes the visibility threshold
- **THEN** the app MUST mark that card as active
- **AND** it MUST attempt to play that card's video muted and inline

#### Scenario: Active card changes
- **WHEN** another feed card becomes the active visible item
- **THEN** the previous active card MUST pause
- **AND** the new active card MAY start muted inline preview
- **AND** no more than one feed video SHOULD be playing at once

#### Scenario: Autoplay is blocked or unsupported
- **WHEN** the browser or WebView rejects the autoplay request
- **THEN** the card MUST remain usable with poster, title, catalog path, and detail navigation
- **AND** the app MUST NOT surface an intrusive playback error for muted preview failure

### Requirement: Feed actions stay learning-oriented
The student H5 video discovery flow SHALL route home feed cards to learning destinations while keeping visible point-specific tools on the second-level point video detail page and limiting home-card actions to one low-frequency overflow menu.

#### Scenario: Student opens a feed item
- **WHEN** the student taps the media area, title, metadata row, or other non-overflow body area on a feed item
- **THEN** the app MUST navigate to the existing point video detail route with `from=home` or equivalent source context
- **AND** returning MUST preserve normal route-stack behavior

#### Scenario: Home feed omits inline action toolbar
- **WHEN** a home feed card is rendered
- **THEN** the card footer MUST NOT render a visible action row
- **AND** the card MUST NOT render `查看实验` as a separate CTA
- **AND** the card MUST NOT render visible home-feed toolbar controls for like, favorite or bookmark, share, Atom, assessment, or point completion
- **AND** the card MAY render one vertical-more overflow trigger as a menu entry point
- **AND** the overflow trigger MUST NOT be accompanied by sibling visible tool icons that recreate a toolbar
- **AND** inline preview affordances such as muted-preview status, duration, progress, or playback state MUST remain scoped to the media area

#### Scenario: Home overflow menu presents low-frequency choices
- **WHEN** the student taps a home feed card's overflow trigger
- **THEN** the app MUST present a mobile menu or sheet for low-frequency feed choices
- **AND** the menu MAY include actions such as save-later, share, not-interested, report, feedback, or open-detail
- **AND** the menu MUST NOT include Atom, assessment, quiz, point-completion, comment, creator-channel, follower, or entertainment-ranking actions
- **AND** selecting or dismissing the menu MUST NOT also trigger the underlying card's point-detail navigation unless the selected menu item is explicitly an open-detail action
- **AND** unavailable persistence-backed actions MUST either be omitted or behave as controlled local UI feedback without implying a completed backend mutation

#### Scenario: Point detail page owns video actions
- **WHEN** the student opens a feed item from home
- **THEN** the point video detail page MUST provide the point-specific action surface for Atom, favorite or bookmark, share, assessment or completion entry points, and overflow actions that are supported by the current product
- **AND** any like or lightweight positive feedback action supported by the current product MUST appear on the point detail page rather than as a visible home feed toolbar control
- **AND** these actions MUST use the selected point placement identity and canonical point identity from the opened feed item

#### Scenario: Student asks Atom from a feed item
- **WHEN** the student opens a feed item and chooses the Atom action on the point video detail page
- **THEN** the app MUST open Atom chat with the item title, catalog path or chapter context, point identity, and summary context
- **AND** the Atom action MUST NOT change the active root tab identity as a side effect

#### Scenario: Feed card excludes per-card search action
- **WHEN** a home feed card is rendered
- **THEN** the card MUST NOT render a visible `搜索相关` action or another per-card query-launching search action
- **AND** experiment-video search MUST remain owned by the home header/video-library entry and the second-level video-library search page

#### Scenario: Feed avoids required entertainment chrome
- **WHEN** the home feed is rendered
- **THEN** the feed MUST NOT require likes, comments, creator channels, follower counts, or generic social engagement controls to complete the learning flow
- **AND** any low-frequency save, share, report, feedback, not-interested, or open-detail behavior available from the home overflow menu MUST NOT introduce counters, creator/channel dependencies, or ranking behavior unless a future spec defines those behaviors
- **AND** visible learning actions on the detail page MUST prioritize point detail, experiment learning, and Atom explanation over entertainment-style engagement

### Requirement: Home entry for experiment video library
The student H5 home page SHALL provide a focused entry into the experiment video library without turning the home page into a global search surface.

#### Scenario: Student sees video library entry on home
- **WHEN** an authenticated student opens the home root
- **THEN** the page MUST provide an experiment video library entry point
- **AND** the entry MUST communicate experiment-video or phenomenon discovery rather than generic site search.

#### Scenario: Home avoids global search bar
- **WHEN** the authenticated student opens the home root
- **THEN** the page MUST NOT show a large all-site search bar as the primary home affordance
- **AND** experiment-video search MUST be opened through the video library entry.

#### Scenario: Student opens video library from home
- **WHEN** the student taps the experiment video library entry
- **THEN** the app MUST push the video library detail route
- **AND** the bottom navigation MUST be hidden while the video library page is visible.

### Requirement: Video library page owns search and browse
The student H5 app SHALL provide a second-level video library page that owns experiment-video search, simple no-query discovery, and result display.

#### Scenario: Video library opens without query
- **WHEN** a student opens the video library page without a query
- **THEN** the page MUST show a simple no-query default state instead of an empty search-only screen
- **AND** default content MUST prioritize local recent search rows when history exists
- **AND** default content MUST show recommended experiment video rows when recommendation data exists
- **AND** default content MUST show recommended search terms as a fallback or lower-priority section when video recommendations are unavailable or insufficient
- **AND** default content MUST NOT render the previous categorized browse-card grid for phenomenon, reagent, chapter, element-family, or knowledge chips.

#### Scenario: Recommended video rows render with cover affordance
- **WHEN** the no-query default state shows recommended experiment videos
- **THEN** each recommended video row MUST include a student-facing title, one fixed single-line catalog path or context row, and a compact learning-page chapter tag when the route target maps to a learning profile
- **AND** the compact learning-page chapter tag MUST be derived from the frontend learning page profile label by `profile_id` or `chapter_id`
- **AND** the compact learning-page chapter tag MUST NOT use backend textbook chapter badge labels such as chapter 13 or chapter 14
- **AND** each row MUST reserve a thumbnail or poster slot immediately before the diagonal arrow action on the right
- **AND** the row MUST use a real student-visible video thumbnail or poster when available
- **AND** the row MUST render a stable nonblank cover fallback when no thumbnail is available
- **AND** the row MUST NOT render snippets, backend badges, explanatory text, or action-label text.

#### Scenario: Student selects a default recommendation
- **WHEN** a student taps a recommended video row in the no-query default state
- **THEN** the app MUST navigate to the existing point, chapter, or supported learning route target for that recommendation
- **AND** the route MUST preserve `from=video-library` or equivalent source context
- **AND** returning MUST preserve normal route-stack behavior.

#### Scenario: Student selects a history or recommended-term row
- **WHEN** a student taps a recent search row or recommended search term row
- **THEN** the page MUST populate the search query with that term and perform video-library search within experiment-video learning content
- **AND** the selected term MUST be remembered in local video-library search history.

#### Scenario: Student enters a query
- **WHEN** the student types a query in the video library search box
- **THEN** the page MUST search within experiment-video learning content
- **AND** it MUST NOT search unrelated admin, teacher draft, account, assessment-management, or global application content.

#### Scenario: Video library shows query results
- **WHEN** the student enters a non-empty query from the home video search entry
- **THEN** the page MUST replace the no-query history/recommendation state with a result state headed as `关于“<query>”的实验视频`
- **AND** the result state MUST render a flat experiment-video result list sourced from the video-library search response
- **AND** video result rows MUST use the same title, single-line path, compact learning-page chapter tag, thumbnail, and diagonal arrow structure as recommended video rows
- **AND** the compact learning-page chapter tag MUST be present whenever the target maps to a learning profile
- **AND** thumbnail slots MUST render only when a thumbnail is available and MUST NOT reserve empty placeholder space when unavailable
- **AND** the result state MUST NOT render catalog directory result rows for the home video search entry.

#### Scenario: Video library query has no results
- **WHEN** the student enters a non-empty query that returns no video results
- **THEN** the page MUST render a simple inline empty message
- **AND** the empty message SHOULD say `这里什么都没有哦~`
- **AND** the page MUST NOT render the backend empty-result message as a yellow warning banner
- **AND** the page MUST NOT render a large empty-state card for this result state.

#### Scenario: Learning search reuses the video search page model
- **WHEN** the student opens search from a learning chapter or catalog page
- **THEN** the app MUST reuse the same search shell, local-history behavior, query/default state model, and video result row behavior as the video library search page
- **AND** a non-empty query MUST render video results and catalog directory results
- **AND** catalog directory results MUST be available only in the learning search scope
- **AND** tapping a catalog directory result MUST navigate to the corresponding learning catalog directory page
- **AND** tapping a video result MUST navigate to the existing point learning page.

#### Scenario: Learning root search covers all chapters
- **WHEN** the student opens search from the learning root page
- **THEN** the app MUST open the learning search scope without `profileId`, `chapterId`, `sourceNodeId`, `catalogPath`, or `elementSymbol` context
- **AND** typing a query MUST keep the route in learning-root search context rather than auto-injecting the active profile or chapter
- **AND** catalog directory matching MUST consider all student-visible learning profiles/chapters available to the learning root
- **AND** selecting a catalog directory or point result MUST still navigate through the normal learning catalog or point detail routes with source `search`.

#### Scenario: Student clears a query
- **WHEN** the student clears the active search query
- **THEN** the page MUST return to the simple no-query video library default state
- **AND** it MUST keep route-stack navigation and page back behavior intact.

### Requirement: Elasticsearch-backed experiment-video search
The backend SHALL provide Elasticsearch or Elasticsearch-compatible search for the video library while preserving local/test fallback behavior.

#### Scenario: Search service is configured
- **WHEN** the video library search service is configured and healthy
- **THEN** search requests MUST query the configured Elasticsearch-compatible index
- **AND** responses MUST return typed, student-visible result groups.

#### Scenario: Search service is unavailable or disabled
- **WHEN** the search service is disabled, unavailable, or not configured in local development
- **THEN** the backend MUST return a controlled disabled/fallback response or use a deterministic local metadata search
- **AND** the frontend MUST render a non-blocking state rather than crashing.

#### Scenario: Search index is empty
- **WHEN** the search service is available but no student-visible documents match the query
- **THEN** the frontend MUST render an empty state with useful next steps such as browse chips, retry, or AI explanation entry when allowed.

### Requirement: Searchable document scope
The video library index SHALL represent student-visible experiment point learning material and searchable chemistry context.

#### Scenario: Experiment video document is indexed
- **WHEN** a student-visible catalog point placement is indexed
- **THEN** the searchable document MUST include stable identifiers needed for routing
- **AND** it MUST include student-facing catalog path, point title, principle, phenomenon explanation, safety note, related point titles, reagents, phenomena, chapter identifiers, element symbols, equations, formula text, and chemistry-derived recall fields when available.
- **AND** it MUST NOT include video resource titles, media asset titles, binding titles, original file names, media asset ids, playback paths, thumbnail paths, upload status, processing status, duplicate-candidate data, or other video resource metadata.

#### Scenario: Hidden content exists
- **WHEN** an experiment point, media resource, learning resource, or catalog placement is draft-only, archived, unpublished, unready, or not visible to students
- **THEN** the index and search response MUST NOT expose it to student H5 search.

#### Scenario: Later transcript data exists
- **WHEN** transcript or ASR segments become available for a published video
- **THEN** the index MUST NOT include those transcript segments unless a future spec explicitly promotes transcripts to student-facing point content
- **AND** transcript hits MUST not be introduced as an implicit side effect of media asset upload.

### Requirement: Actionable search result groups
The video library search results SHALL be grouped by learning action and every result SHALL route to a meaningful second-level destination.

#### Scenario: Video point result is selected
- **WHEN** a student selects a video point result
- **THEN** the app MUST navigate to the point video/detail route with enough catalog and point context to show the matching learning target
- **AND** returning MUST restore the video library search state where feasible.

#### Scenario: Catalog point result is selected
- **WHEN** a student selects a catalog point result
- **THEN** the app MUST navigate to an appropriate point detail destination
- **AND** it MUST NOT switch to a separate obsolete experiment root tab.

#### Scenario: Chapter or knowledge result is selected
- **WHEN** a student selects a chapter, element-family, or knowledge-point result
- **THEN** the app MUST navigate to the related chapter learning detail route or another supported route-stack learning page
- **AND** the route MUST preserve `from=video-library` or equivalent source context.

#### Scenario: AI explanation action is selected
- **WHEN** a student opens an AI explanation from a search result
- **THEN** the app MUST open the shared AI chat detail page with result context
- **AND** it MUST NOT change the active root tab identity as a side effect.

#### Scenario: Result lacks a route target
- **WHEN** a backend search hit cannot be mapped to a supported route target
- **THEN** the backend or frontend MUST omit it from actionable results or render it as unavailable
- **AND** it MUST NOT produce a dead-end passive result item.

### Requirement: Video library mobile interaction states
The video library page SHALL remain usable on mobile widths and support loading, error, disabled, empty, no-query default, and result states.

#### Scenario: Search is loading
- **WHEN** a search request is in progress
- **THEN** the page MUST show a loading state that preserves the current query and page layout.

#### Scenario: Search fails
- **WHEN** a search request fails
- **THEN** the page MUST show an error state with retry or fallback browse affordances
- **AND** it MUST keep page back behavior available.

#### Scenario: Mobile viewport renders video library
- **WHEN** the page is viewed at 360px, 390px, or 430px mobile widths
- **THEN** the search input, recent-search rows, recommended-video thumbnail rows, recommended search terms, grouped results, and route actions MUST NOT overlap horizontally or vertically
- **AND** thumbnail slots and diagonal arrow actions MUST keep stable dimensions while text truncates or wraps safely
- **AND** recommended video rows MUST keep a consistent compact row height while title and path truncate to their fixed lines
- **AND** recommended video learning-page chapter tags MUST remain single-line and truncate without changing thumbnail or arrow alignment
- **AND** the hidden bottom navigation state MUST not leave unsafe-area gaps that obscure content.

### Requirement: Chemistry-aware search indexes point placements
The student experiment-video search index SHALL represent published catalog point placements, not raw video resources, generic media rows, canonical-only points, or generic text snippets.

#### Scenario: Published point placement is indexed
- **WHEN** a catalog point placement is active and its point content is published
- **THEN** the search document MUST include the placement node id, canonical point id, chapter id, catalog path, student-visible title, principle, phenomenon explanation, safety note, related point titles, aliases, formulae, reaction features, searchable text, and non-semantic video readiness signals
- **AND** the placement node id MUST be usable as the ES document identity.
- **AND** the document MUST NOT include video resource titles, original file names, media ids, thumbnail paths, stream paths, or video metadata in searchable text or ES source.

#### Scenario: Same experiment appears in multiple directories
- **WHEN** one canonical experiment point has multiple active placements
- **THEN** each searchable placement MUST keep its own catalog path and placement node id
- **AND** the canonical point id MUST allow grouping or deduplication without losing placement-specific context.

#### Scenario: Unpublished or hidden point content exists
- **WHEN** a point placement has draft-only content, unpublished content, archived state, hidden state, or only archived media bindings
- **THEN** student experiment-video search MUST NOT expose hidden point content or archived media resource data as a searchable result
- **AND** any previously indexed document for that placement MUST be deleted or rebuilt through the ES sync job contract.

### Requirement: Directory context can recall point placements
The student experiment-video search SHALL use catalog directories as context, filters, and weak recall evidence for point placements, without making directories the default final result object.

#### Scenario: Query matches a directory title
- **WHEN** a student searches for a chapter, section, or directory phrase
- **THEN** the search system MAY recall point placements under that matching directory context
- **AND** the returned learning results MUST remain point or video actions unless a separate directory-navigation mode is explicitly requested.

#### Scenario: Directory context contributes to ranking
- **WHEN** a point placement matches a query through its catalog path or ancestor directory
- **THEN** ranking MAY use that path match as supporting evidence
- **AND** the path match MUST be weaker than a direct title, strict chemical synonym, formula, or same-equation-row match.

#### Scenario: Chapter filter is applied
- **WHEN** the search request includes a chapter filter
- **THEN** the search system MUST constrain or boost results according to indexed chapter or path metadata
- **AND** it MUST keep canonical grouping semantics intact when the same point exists in more than one chapter.

### Requirement: Multi-route chemistry recall improves ranking
The student experiment-video search SHALL support chemistry-aware recall routes for text, strict synonyms, formulae, equation rows, conditions, phenomena, properties, directory context, and fallback search text.

#### Scenario: Query contains chemical formulae
- **WHEN** a query contains formula-like terms such as `KMnO4`, `H2O2`, `SO2`, or `FeCl3`
- **THEN** the search system MUST normalize the formula terms for exact keyword matching
- **AND** it SHOULD combine those exact matches with text/analyzer matches rather than relying only on generic tokenized search.

#### Scenario: Query contains strict chemical synonyms
- **WHEN** a query contains a reviewed alias such as a Chinese name, English name, common name, Unicode subscript formula, or ASCII formula for the same chemical entity
- **THEN** strict synonym expansion MAY contribute to text search and query normalization
- **AND** title or principle matches from the expanded entity SHOULD rank above broad phenomenon-only matches.

#### Scenario: Query contains multiple chemical entities
- **WHEN** a query contains multiple chemical entities
- **THEN** candidates where the entities appear in the same normalized equation row or participant set SHOULD rank above candidates where the terms only appear separately across unrelated fields
- **AND** the implementation MUST preserve a deterministic fallback when structured equation matching is unavailable.

### Requirement: Student responses hide retrieval internals
Student-facing video-library search SHALL keep result payloads actionable and safe while diagnostics remain teacher-only.

#### Scenario: Student receives search results
- **WHEN** a student search request returns experiment-video results
- **THEN** each result MUST expose only allowed learning metadata such as point title, snippet, catalog path, and allowed point route metadata
- **AND** it MUST NOT expose raw ES DSL, analyzer tokens, dictionary file state, route traces, sync-job payloads, rank-debug internals, media asset ids, video resource titles, original file names, thumbnail paths, or stream paths from ES.

#### Scenario: Teacher and student query the same term
- **WHEN** a teacher diagnostic and a student search use the same query
- **THEN** the diagnostic MAY show route reasons, scores, analyzer terms, and canonical/placement grouping
- **AND** the student response MUST remain stable and product-facing even if the same backend route contributed to the result.

### Requirement: Video resource labels are excluded from search semantics
The student experiment-video search SHALL treat the index as a published point library, not as a video resource library.

#### Scenario: Bound video has teacher-only labels
- **WHEN** a published point has a bound ready video with a media asset title, binding title, or original file name
- **THEN** those labels MUST NOT be included in ES searchable fields, local fallback searchable text, diagnostics route matching, or student search snippets
- **AND** queries matching only those labels MUST NOT recall the point.

#### Scenario: Point has a playable video
- **WHEN** a published point has an active ready video binding
- **THEN** the search document MAY include `has_video` and `video_count`
- **AND** `video_count` MUST be either `0` or `1`, because a video point has at most one current video resource
- **AND** those fields MUST be treated only as point readiness/filter signals, not as video semantic content.

#### Scenario: Search hit is rendered
- **WHEN** a student search result is rendered
- **THEN** the result MUST use point title, point snippet, catalog path, and route target from point data
- **AND** it MUST NOT display or depend on video resource title, media asset id, thumbnail path, stream path, or original file name from ES.

### Requirement: Video library search remains distinct from home feed playback
The student experiment-video search capability SHALL remain a second-level search and simple discovery surface, not the playback data contract for the home video feed.

#### Scenario: Home needs playable media fields
- **WHEN** the home video feed needs stream paths, thumbnail paths, media ids, or duration for inline preview
- **THEN** those fields MUST come from the home feed API or point detail APIs
- **AND** they MUST NOT be added to the student video-library Elasticsearch search document source.

#### Scenario: Video library default renders recommendation covers
- **WHEN** the video-library no-query default state renders recommended video covers
- **THEN** thumbnail or poster data MUST come from existing student-visible feed or media APIs, or from a nonblank UI fallback
- **AND** thumbnail or poster data MUST NOT be required in the Elasticsearch search document source
- **AND** default recommendation rows MUST NOT autoplay inline video.

#### Scenario: Student opens search from home
- **WHEN** the student taps the home search action
- **THEN** the app MUST open the existing video-library search route with home source context
- **AND** the video-library page MUST continue to own query input, recent search rows, recommended videos, recommended search terms, and grouped result display.

#### Scenario: Search result is rendered
- **WHEN** the video-library page renders search results
- **THEN** results MUST remain actionable learning/search results
- **AND** they MUST NOT be required to autoplay inline like home feed cards
- **AND** grouped query results MUST remain usable even when no thumbnail or poster data is available.

### Requirement: Home discovery header owns recommendation topic rail
The student H5 home video discovery surface SHALL render its home video topic rail as header-attached chrome above the video feed, with `发现` as the default selected topic.

#### Scenario: Student opens home video discovery
- **WHEN** an authenticated student opens the home root
- **THEN** the page MUST show a horizontally scrollable home video topic rail attached to the home header
- **AND** the `发现` topic MUST be selected by default
- **AND** the rail MUST be visually styled as part of the home title/header system rather than as a separate content card

#### Scenario: Home rail uses experiment video topic taxonomy
- **WHEN** the home topic rail is rendered
- **THEN** the rail MUST use labels that describe discovery intent, experiment-observation phenomena, experiment operations, or video-viewing intent
- **AND** the initial label set MUST include `发现`, `稍后学习`, `全部`, `颜色变化`, `沉淀生成`, `气体生成`, `分层萃取`, `褪色漂白`, `发光火焰`, `温度变化`, `加热反应`, `试纸检验`, `指示剂`, and `晶体析出`
- **AND** the rail MUST NOT include knowledge taxonomy labels such as `卤素`, `酸碱`, or `氧化还原`
- **AND** the rail MUST NOT include `最新` unless a future change defines freshness ranking and upload-time semantics for student-visible experiment videos

#### Scenario: Student changes topic selection
- **WHEN** the student taps a topic in the home rail
- **THEN** the tapped topic MUST become the visible active topic
- **AND** the home feed MUST reset to the first batch for that topic
- **AND** any pending cursor from the previous topic MUST NOT be reused for the newly selected topic

#### Scenario: Home feed starts below attached header rail
- **WHEN** home feed items are rendered below the recommendation rail
- **THEN** the first feed item MUST align directly under the header area with only the configured header/feed spacing
- **AND** unrelated background bands, hero cards, or explanatory title cards MUST NOT appear between the recommendation rail and the video stream

#### Scenario: Home overflow preserves current header chrome
- **WHEN** the student opens a home feed card overflow menu while the home header and topic rail are visible
- **THEN** the overflow menu MUST open without causing the home header unit to compress or disappear
- **AND** scroll or visual-viewport events caused by opening the menu MUST NOT be treated as downward feed-scroll intent while the menu remains open
- **AND** the overflow backdrop MUST NOT visually cover the visible home header unit with a blank or dimmed band
- **AND** if the home header unit was already compressed before opening the menu, the menu MUST preserve that compressed state until it closes

#### Scenario: Home search remains video-library entry
- **WHEN** the student activates the home search affordance from the home header
- **THEN** the app MUST open the second-level video-library route with home source context
- **AND** the home recommendation rail MUST NOT replace the video-library page's query input, search results, browse chips, or grouped result behavior

### Requirement: Student can save home videos for later learning
The student H5 video discovery flow SHALL provide durable student-owned watch-later state for playable video items.

#### Scenario: Student saves a video for later learning
- **WHEN** a student chooses the `稍后学习` action for a home video item or point video detail item
- **THEN** the backend MUST persist an active watch-later save for the current student, point placement, canonical point, and media asset
- **AND** repeating the same save action MUST be idempotent rather than creating duplicate active saves
- **AND** the frontend MUST update the item's visible personal state without requiring a full home feed reload

#### Scenario: Student removes a video from later learning
- **WHEN** a student removes a previously saved video from `稍后学习`
- **THEN** the backend MUST deactivate or archive the active watch-later save for that student and item
- **AND** the item MUST no longer appear in the student's `稍后学习` topic after refresh or local state update
- **AND** the operation MUST NOT delete or modify the underlying catalog point, media asset, or home feed candidate

#### Scenario: Watch-later is distinct from favorites
- **WHEN** the system stores or displays `稍后学习` state
- **THEN** it MUST treat the state as a watch-later queue rather than as a long-term favorite or bookmark
- **AND** it MUST NOT make the item appear in `我的-收藏` unless the student also favorites the item

#### Scenario: Saved item becomes hidden
- **WHEN** a video saved for later learning later becomes unpublished, archived, hidden from students, or unplayable
- **THEN** the save record MAY remain stored for audit or recovery
- **AND** the item MUST NOT be returned in the visible `稍后学习` feed while it is not student-visible and playable

### Requirement: Student can favorite videos for profile collection
The student H5 video discovery flow SHALL provide durable student-owned favorite state for long-term video collection under `我的-收藏`.

#### Scenario: Student favorites a point video
- **WHEN** a student chooses the `收藏` action on a point video detail page
- **THEN** the backend MUST persist an active favorite save for the current student, point placement, canonical point, and media asset
- **AND** repeating the same favorite action MUST be idempotent rather than creating duplicate active favorites
- **AND** the point detail action MUST reflect the saved state as `已收藏`

#### Scenario: Student unfavorites a point video
- **WHEN** a student cancels `收藏` for a previously favorited point video
- **THEN** the backend MUST deactivate or archive the active favorite save for that student and item
- **AND** the item MUST no longer appear in the student's `我的-收藏` collection after refresh or local state update
- **AND** the operation MUST NOT delete or modify the underlying catalog point, media asset, watch-later save, or home feed candidate

#### Scenario: Favorites are distinct from watch-later
- **WHEN** the system stores or displays `收藏` state
- **THEN** it MUST treat the state as a long-term favorite collection rather than as the home `稍后学习` queue
- **AND** favoriting an item MUST NOT make it appear in the home `稍后学习` topic unless the student also saves it for later learning

#### Scenario: Student opens My favorites
- **WHEN** a student opens the `我的-收藏` collection from the profile area
- **THEN** the app MUST show the current student's active favorite playable videos as a finite, non-repeating list
- **AND** the list MUST use the same student-visible catalog/media filters as home feed hydration
- **AND** hidden, unpublished, archived, or unplayable favorites MUST be omitted from the visible playable collection

### Requirement: Home video feed loads paged batches
The student H5 home page SHALL append home video feed batches as the student scrolls while preserving the root page's window-level scroll behavior.

#### Scenario: Student scrolls near the end of the feed
- **WHEN** the student scrolls near the bottom sentinel of the home video feed and the current topic has more items
- **THEN** the frontend MUST request the next home feed batch using the latest next cursor
- **AND** it MUST append the returned items to the existing feed items for the same topic
- **AND** it MUST prevent concurrent duplicate load-more requests for the same cursor

#### Scenario: Initial topic batch loads
- **WHEN** the student opens home or switches to a new topic
- **THEN** the frontend MUST request the first batch for the active topic without reusing an old topic cursor
- **AND** it MUST show initial loading, empty, or error states separately from incremental loading states

#### Scenario: Finite topic is exhausted
- **WHEN** the active topic returns no next cursor after at least one item has been rendered
- **THEN** the frontend MUST stop issuing automatic load-more requests for that topic
- **AND** it MAY show a small end-of-list marker
- **AND** it MUST NOT show the zero-results empty state merely because a finite topic reached its end

#### Scenario: Topic has no matches
- **WHEN** the active topic returns an empty item list for its first batch
- **THEN** the frontend MUST render a controlled empty state for that topic below the header rail
- **AND** it MUST keep the selected topic visible and changeable in the header rail

#### Scenario: Repeated videos remain autoplay safe
- **WHEN** the same canonical video appears multiple times in the home feed
- **THEN** the frontend MUST use the item instance id for React keys, DOM feed ids, IntersectionObserver registration, and active autoplay state
- **AND** it MUST use canonical point and media identities only for navigation, route context, and item content

#### Scenario: Window remains the scroll container
- **WHEN** home feed batches are appended
- **THEN** the app MUST preserve window-level scrolling for the home root
- **AND** header/topic-rail compression and bottom navigation compression MUST continue to respond to page scrolling
- **AND** the feed MUST NOT be moved into an internal scroll container solely to implement load more

### Requirement: Home video auto-preview selects a stable visible card
The student H5 home page SHALL keep inline video auto-preview tied to one stable visible feed card instead of relying solely on bottom-sentinel or per-card observer callbacks.

#### Scenario: First visible card previews before observer callbacks
- **WHEN** the home feed has rendered at least one playable card and no observer callback has selected an active card yet
- **THEN** the frontend MUST select a visible rendered item, falling back to the first rendered feed item when no geometry measurement is available
- **AND** the selected card MUST render the active muted preview state instead of the inactive `滑到此处自动预览` prompt

#### Scenario: Active preview uses effective playable viewport
- **WHEN** the frontend ranks visible home video cards for preview ownership
- **THEN** it MUST calculate visibility against the playable viewport that excludes fixed home header/topic rail chrome and bottom navigation chrome
- **AND** it MUST prefer cards with meaningful visible height, stronger visible ratio, and closer distance to the playable viewport center

#### Scenario: Scroll updates active preview without changing scroll container
- **WHEN** the student scrolls the window-level home feed between video cards
- **THEN** the frontend MUST recalculate the active preview from registered card geometry
- **AND** it MUST keep the home root on window-level scrolling rather than introducing an internal feed scroll container for preview selection

#### Scenario: Active preview does not flap
- **WHEN** the current active card remains meaningfully visible while scroll, resize, visual-viewport, or observer events arrive
- **THEN** the frontend MUST keep that card active unless another visible card clearly ranks ahead of it
- **AND** it MUST NOT repeatedly clear and reselect the same active card in a way that causes unnecessary pause/play loops

#### Scenario: Preview identity follows rendered instances
- **WHEN** repeated canonical videos appear in the home feed
- **THEN** active preview selection MUST continue to use the item instance id for registration, ranking, and active state
- **AND** selecting one rendered occurrence MUST NOT activate or pause another occurrence of the same canonical video

### Requirement: Home video cards use inactive progress chrome
The student H5 home video feed SHALL render video-card media chrome as a lightweight inactive progress surface rather than a full player control surface.

#### Scenario: Home card omits preview status text
- **WHEN** a home video card is rendered in either active or inactive preview state
- **THEN** the media layer MUST NOT display `滑到此处自动预览`
- **AND** it MUST NOT display `静音预览`
- **AND** it MUST NOT display a lower-right duration capsule

#### Scenario: Home card shows inactive progress strip
- **WHEN** a home video card is rendered
- **THEN** it MUST show a bottom-aligned inactive progress strip with track, loaded, and played segments
- **AND** the strip MUST use the same progress color tokens as the second-level point video player
- **AND** it MUST NOT show the second-level active progress thumb or SYSU logo marker
- **AND** it MUST NOT expose drag or seek behavior from the home feed card

#### Scenario: Home card remains muted
- **WHEN** the active home video preview plays inline
- **THEN** it MUST remain muted
- **AND** the media layer MUST NOT provide a mute or unmute control on the home card
- **AND** the student MUST open the second-level point video page for full playback controls

#### Scenario: Point player progress colors are shared across states
- **WHEN** the second-level point video player switches between inactive and active chrome states
- **THEN** inactive and active progress bars MUST use the same track, loaded, and played color semantics
- **AND** the active state MUST differ by showing the expanded hit area and SYSU logo thumb rather than by changing progress colors

### Requirement: Learning search default recommendations render as a stable snapshot
The student H5 learning search page SHALL render its no-query default recommendation content from one coherent snapshot for the current route context instead of visibly appending rows as individual async sources resolve.

#### Scenario: Student opens learning search without a query
- **WHEN** a student opens `/search` in learning scope without a query
- **THEN** the page MUST show a controlled loading state while the recommendation snapshot for the current route context is being prepared
- **AND** the `推荐内容` section MUST NOT render partial catalog-only, video-only, or thumbnail-incomplete batches before the snapshot is committed
- **AND** once committed, the section MUST render the selected history, directory, video, and recommended-term rows that are available for that snapshot without additional source-by-source row insertion

#### Scenario: Recommendation source resolves after the route context changes
- **WHEN** the student changes the query, clears the query, navigates away, or opens a different profile/chapter context while recommendation data is still loading
- **THEN** late responses from the previous context MUST NOT replace or append to the current recommendation or result snapshot
- **AND** the visible content MUST correspond to the latest route context only

#### Scenario: One recommendation source fails
- **WHEN** one source needed by the no-query recommendation snapshot fails but other recommendation sources succeed
- **THEN** the page MUST commit a single controlled fallback snapshot from the successful sources
- **AND** the page MUST NOT repeatedly mutate the visible recommendation rows as failed sources retry or settle
- **AND** the failure MUST be surfaced as a non-blocking state only when it affects student actionability

#### Scenario: Recommended video thumbnail is unavailable at snapshot time
- **WHEN** a recommended video row is included in the committed recommendation snapshot
- **THEN** the row MUST render with stable geometry from first paint
- **AND** it MUST either show the resolved student-visible thumbnail or a stable nonblank cover fallback without adding or removing the cover slot after the row is visible

### Requirement: Learning-scoped recommendations preserve context
The student H5 learning search page SHALL keep default recommendations honest about the active learning scope so global video suggestions are not presented as if they belong to a selected chapter or catalog context.

#### Scenario: Student opens search from a selected chapter or catalog context
- **WHEN** a student opens `/search` with `profileId`, `chapterId`, `sourceNodeId`, `catalogPath`, or `elementSymbol` context and no query
- **THEN** the default recommendation snapshot MUST prioritize catalog directory and video rows that match the active learning context
- **AND** any unscoped or global video recommendation shown in the default state MUST carry clear context metadata or be separated from the context-specific `推荐内容` list
- **AND** tapping a context-specific recommendation MUST preserve the normal learning route source and chapter/profile context where available

#### Scenario: Student opens learning-root search
- **WHEN** a student opens `/search` from the learning root without profile, chapter, source node, catalog path, or element context
- **THEN** the default recommendation snapshot MAY combine rows across student-visible chapters
- **AND** the rows MUST still expose enough chapter or catalog metadata for the student to understand where the recommendation leads

### Requirement: Legacy student home opens as video feed
The legacy student frontend SHALL make the default authenticated home surface an experiment-video feed rather than an Atom assistant, category browser, or modern recommendation-topic page.

#### Scenario: Legacy student opens home
- **WHEN** an authenticated student opens the old student product home route
- **THEN** the first primary content surface MUST be the experiment video feed
- **AND** the feed MUST use published playable experiment point/video data from the shared backend
- **AND** the home page MUST NOT require the student to choose a category, topic, Atom prompt, or assistant mode before browsing videos

#### Scenario: Legacy student feed has no topic rail
- **WHEN** the old student home video feed renders
- **THEN** it MUST NOT show the current recommendation topic rail or category strip above the feed
- **AND** it MUST NOT show modern category buttons for recommendation topics, element families, phenomena, reagents, or knowledge chips as the default home chrome

### Requirement: Legacy student uses simple native video playback
The legacy student frontend SHALL use native browser video controls or a simple traditional video surface for point/video playback.

#### Scenario: Legacy student opens a video point
- **WHEN** a student opens a video point in `web-student-old`
- **THEN** the page MUST render a playable video using native browser controls or a simple traditional player surface
- **AND** it MUST NOT use the current custom/self-drawn player chrome, ArtPlayer-based point player, or Atom-oriented video action surface
- **AND** the page MUST still use protected student-visible media URLs authorized by the shared backend

#### Scenario: Legacy video media cannot autoplay or load
- **WHEN** native playback is unavailable, blocked, or fails
- **THEN** the old student page MUST show a controlled traditional error or poster state
- **AND** it MUST NOT surface RAG, Atom, media-pipeline, or diagnostic implementation wording to the student

### Requirement: Legacy video discovery uses traditional card/list UI
The legacy student video discovery surface SHALL use a traditional card or list style that is visually distinct from the current modern H5 feed.

#### Scenario: Legacy feed is rendered on mobile width
- **WHEN** the old student feed is rendered on common mobile widths
- **THEN** video cards or rows MUST keep stable thumbnail/player dimensions, readable titles, and concise experiment metadata
- **AND** the visual language MUST use SYSU-red legacy tokens rather than the current green topic-rail visual language
- **AND** visible feed actions MUST remain learning-oriented rather than Atom/chat-oriented

### Requirement: Student video discovery can carry subtitle metadata for full playback
Student video discovery surfaces SHALL make ready subtitle tracks available when a discovered video enters a full playback experience.

#### Scenario: Feed item opens full playback
- **WHEN** a student opens a video from home feed, video library, or catalog discovery into a full playback surface
- **THEN** the playback data MUST include ready subtitle track metadata and stream paths for the selected media asset
- **AND** the full player MUST render those tracks consistently with point video playback.

#### Scenario: Feed item is only a muted lightweight preview
- **WHEN** a feed card renders a muted autoplay preview or lightweight inline preview
- **THEN** it MAY omit loading subtitle track resources to preserve scroll and playback performance
- **AND** it MUST still provide subtitle tracks when the student opens a full playback surface.

#### Scenario: Discovery item has no ready subtitles
- **WHEN** a discovered video has no ready subtitle tracks
- **THEN** discovery and playback MUST continue without subtitle UI errors
- **AND** the absence of subtitles MUST NOT affect recommendation, search, or video availability.
