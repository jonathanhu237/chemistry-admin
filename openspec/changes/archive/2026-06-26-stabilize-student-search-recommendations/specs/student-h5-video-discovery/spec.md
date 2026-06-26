## ADDED Requirements

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
