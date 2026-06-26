## 1. Snapshot Model

- [x] 1.1 Identify the existing async sources used by `VideoLibraryPage` for no-query learning recommendations and document which are required for a stable snapshot.
- [x] 1.2 Add a route-context key for recommendation/result loads that includes scope, query, profile, chapter, source node, catalog path, and element context.
- [x] 1.3 Build a single recommendation snapshot from successful source results and commit it only when the load key still matches the current route context.
- [x] 1.4 Preserve the existing local history ordering while preventing `推荐内容` from rendering before the recommendation snapshot is ready.

## 2. Recommendation Content

- [x] 2.1 Ensure context-specific directory rows and video rows are prioritized when `/search` is opened from a selected profile, chapter, catalog node, or element context.
- [x] 2.2 Separate, label, or suppress unscoped/global video recommendations when they cannot be matched to the active learning context.
- [x] 2.3 Ensure recommended video rows render with stable cover geometry from first paint, using a nonblank fallback when a thumbnail is unavailable.
- [x] 2.4 Keep existing navigation behavior for history rows, recommended terms, catalog directory rows, and video point rows.

## 3. Loading And Failure States

- [x] 3.1 Show a compact controlled loading state while the no-query learning recommendation snapshot is being prepared.
- [x] 3.2 Use a controlled fallback snapshot when one auxiliary recommendation source fails but other sources succeed.
- [x] 3.3 Prevent late responses from old route/query contexts from changing the current recommendation or result view.

## 4. Verification

- [x] 4.1 Add or update student web tests proving `推荐内容` does not render partial rows before the no-query learning recommendation snapshot is committed.
- [x] 4.2 Add or update tests proving stale async responses from an old search context are ignored.
- [x] 4.3 Add or update tests for scoped learning search recommendations so selected chapter/profile context is preserved or global rows are clearly separated.
- [x] 4.4 Run the relevant student web test suite and `openspec validate stabilize-student-search-recommendations --strict`.
