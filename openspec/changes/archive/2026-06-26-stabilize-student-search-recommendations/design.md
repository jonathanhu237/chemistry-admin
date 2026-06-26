## Context

`/search` reuses `VideoLibraryPage` with `scope="learning"`. In the no-query state the page builds "推荐内容" from multiple independently loaded sources: the video library search payload, the home video feed, the learning page profile list, and a client-built catalog search index. Because each source commits state as soon as it resolves, the visible recommendation list can render in batches: catalog directory rows first, video rows later, and thumbnails or chapter tags after a related source catches up.

The desired behavior is a stable first paint for the recommendation section: students should see a loading boundary while recommendations are being assembled, then one coherent list for the current route/query context.

## Goals / Non-Goals

**Goals:**

- Render the no-query learning search recommendation section from one committed snapshot per route/query context.
- Prevent late responses for an old context from changing the current recommendation or search result UI.
- Preserve existing route behavior, local search history behavior, and point/catalog navigation targets.
- Make the snapshot tolerant of partial source failure while still avoiding visible source-by-source batching.
- Add regression tests for the initial recommendation load and stale-response behavior.

**Non-Goals:**

- Replace the video-library search backend or introduce a new recommendation ranking service.
- Change seed data, catalog authoring data, or media binding semantics.
- Redesign the full search UI or home feed.
- Require a backend migration.

## Decisions

1. Use an explicit recommendation snapshot keyed by the current route context.

   The frontend should derive a stable key from `scope`, `query`, `profileId`, `chapterId`, `sourceNodeId`, `catalogPath`, and `elementSymbol`. A load for that key collects the sources needed by the default recommendation state and commits a single snapshot only if the key is still current.

   Alternative considered: keep independent `useEffect` state but hide sections with extra boolean flags. That reduces some flicker but still leaves stale responses and hidden coupling between partial states.

2. Treat the no-query default recommendation state differently from typed search results.

   For no-query browsing, the page should wait for required recommendation sources to settle before rendering "推荐内容". For typed search, the existing result loading boundary can remain, but search results should also ignore stale async responses.

   Alternative considered: progressively reveal rows as each source resolves. This was rejected because the reported problem is the progressive reveal itself.

3. Use `Promise.allSettled`-style source collection with a controlled fallback.

   The page should not fail the entire default recommendation state because one auxiliary source fails. Instead, it should build one final snapshot from successful sources, record a controlled non-blocking error if needed, and avoid additional visible row insertion after the snapshot has committed.

   Alternative considered: `Promise.all` with all-or-nothing failure. That would be simpler but would make the search page unnecessarily fragile when, for example, thumbnail/feed data is unavailable.

4. Keep unscoped and scoped recommendations visually honest.

   When learning search is opened from a specific profile/chapter/catalog context, directory rows are context-specific. Video rows should either be matched to that context, clearly carry their own context label, or be separated/suppressed so a global recommendation does not appear to belong to the current chapter by accident.

   Alternative considered: continue mixing catalog rows and global video rows in one "推荐内容" list. That preserves implementation simplicity but creates confusing recommendations.

5. Stabilize row geometry before commit.

   Video rows included in the snapshot should already know whether they have a real thumbnail, or they should render a stable fallback slot. The row should not gain a new cover slot after first paint.

   Alternative considered: let thumbnails appear later as images load. That can still be acceptable inside a reserved slot, but not if it changes row layout.

## Risks / Trade-offs

- Waiting for multiple sources can delay the first recommendation section by a short amount -> show a compact loading state or skeleton instead of a blank page.
- `buildCatalogSearchIndexes` can be expensive for all-chapter learning-root search -> keep the existing chapter scoping rules and consider caching catalog indexes by chapter ID.
- Suppressing unscoped video rows in a scoped learning search may reduce visible recommendations -> use clear fallback search terms or a separate global video section if scoped videos are unavailable.
- Snapshot logic can grow complex if kept inside one large component -> extract small helpers for building snapshot inputs and rows so the behavior is testable.
