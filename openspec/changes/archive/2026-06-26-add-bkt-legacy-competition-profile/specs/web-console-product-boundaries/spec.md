## ADDED Requirements

### Requirement: Legacy products have explicit product boundaries
The platform SHALL treat `web-student-old` and `web-teacher-old` as separate competition products that share core services but do not replace the current student and teacher products.

#### Scenario: Product ownership is inspected
- **WHEN** a maintainer inspects frontend packages, Compose services, route documentation, or product docs
- **THEN** `web-student-old` MUST identify the legacy student experiment-learning frontend
- **AND** `web-teacher-old` MUST identify the legacy teacher BKT teaching-management frontend
- **AND** neither old product MUST be documented as the canonical replacement for `web-student` or `web-teacher`

#### Scenario: User opens current and old products
- **WHEN** the same backend account and data are used in current and old products
- **THEN** the current products MUST preserve current navigation and capabilities
- **AND** the old products MUST present their legacy navigation and capability subset
- **AND** route availability in one product MUST NOT imply the same route is visible in the other product

### Requirement: Legacy boundary hides platform and diagnostic ownership
The legacy teacher product SHALL avoid platform operations and diagnostic monitoring workflows that belong to current teacher/admin products.

#### Scenario: Legacy teacher navigation is rendered
- **WHEN** an authenticated teacher opens `web-teacher-old`
- **THEN** navigation MUST focus on experiment navigation, videos/resources, AI question generation, teacher review, question bank, assessments, classes, and learning scores
- **AND** navigation MUST NOT include platform-account governance, student-preview infrastructure governance, learning assistant, intelligent monitoring, AI/RAG/ES diagnostics, or provider credential management
