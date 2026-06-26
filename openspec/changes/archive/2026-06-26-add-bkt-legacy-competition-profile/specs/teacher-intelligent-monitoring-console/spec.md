## ADDED Requirements

### Requirement: Legacy teacher profile excludes intelligent monitoring
The legacy teacher frontend SHALL not expose the intelligent monitoring console or AI/RAG/ES diagnostic modules.

#### Scenario: Legacy teacher navigation is rendered
- **WHEN** an authenticated teacher opens `web-teacher-old`
- **THEN** navigation MUST NOT include intelligent monitoring, learning assistant, AI/RAG/ES monitoring, OpenAI monitoring, RAG runtime monitoring, ES retrieval diagnostics, dictionary/outbox diagnostics, guardrail diagnostics, or trend diagnostics
- **AND** old teacher routes MUST NOT make those pages reachable through visible old navigation

#### Scenario: Legacy teacher manually enters monitoring URL
- **WHEN** a teacher manually enters an old-product URL that corresponds to intelligent monitoring or diagnostic modules
- **THEN** the old product MUST redirect to a safe old teacher route or show a controlled not-found state
- **AND** it MUST NOT mount the current diagnostic console inside `web-teacher-old`

### Requirement: Current monitoring remains available outside legacy profile
The legacy exclusion SHALL not remove the current intelligent monitoring console from the current teacher/admin products.

#### Scenario: Current teacher opens monitoring
- **WHEN** an authenticated teacher opens the current `web-teacher` product
- **THEN** the current intelligent monitoring behavior MUST remain available according to the existing capability
- **AND** legacy route hiding MUST be scoped to `web-teacher-old`
