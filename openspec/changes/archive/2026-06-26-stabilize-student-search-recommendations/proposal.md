## Why

The student H5 learning search default state currently feels unstable because recommendation rows are assembled from several asynchronous sources and can appear in visible batches. This makes the search page feel jumpy and can cause a student to tap content that shifts or changes while the page is still loading.

## What Changes

- Stabilize the no-query recommendation state for the learning search page so it is displayed from one coherent recommendation snapshot instead of partial source-by-source updates.
- Keep the existing search shell and route behavior, but add a clear loading boundary while the default recommendation snapshot is being prepared.
- Prevent stale or late async responses from replacing the current recommendation or result snapshot after the route/query context has changed.
- Clarify that learning-scoped search recommendations should preserve the active learning context where available, including chapter/profile context for directory rows and video rows.
- Add regression coverage that verifies the default recommendation section does not render partial batches before all required sources settle.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `student-h5-video-discovery`: Add stability and context requirements for the student H5 video/learning search default recommendation state.

## Impact

- Affects the student web search/video library page implementation in `apps/web-student/src/routes/video-library/VideoLibraryPage.tsx`.
- Affects student web tests around `/search` and `/video-library` default recommendation rendering.
- May affect frontend API usage by passing or preserving learning context for recommendation/search calls; no breaking backend API change is required by this proposal.
