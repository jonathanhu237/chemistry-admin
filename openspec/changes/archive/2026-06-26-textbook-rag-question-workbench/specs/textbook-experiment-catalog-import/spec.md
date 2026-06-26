## ADDED Requirements

### Requirement: Markdown experiment hierarchy import
The system SHALL import the textbook experiment catalog from Markdown using headings and leaf bullets as the authoritative hierarchy.

#### Scenario: Chapter and experiment headings are parsed
- **WHEN** the importer reads `实验目录_整理版.md`
- **THEN** level-one headings SHALL become chapter context
- **AND** level-two headings SHALL become experiments under the current chapter.

#### Scenario: Leaf bullets become points
- **WHEN** a bullet item has no nested child bullet
- **THEN** the importer SHALL treat it as an experiment point
- **AND** it SHALL remove display-only markers such as `（点位）` from the stored point title.

#### Scenario: Non-leaf bullets become path metadata
- **WHEN** a bullet item has one or more nested child bullets
- **THEN** the importer SHALL treat it as a folder path segment
- **AND** it SHALL store the full path on descendant point metadata rather than creating an experiment for that segment.

### Requirement: Idempotent experiment and point creation
The system SHALL match existing catalog records before creating missing experiments or points.

#### Scenario: Existing experiment matches the Markdown experiment
- **WHEN** an imported chapter and experiment title safely match an existing formal experiment
- **THEN** the importer SHALL reuse that formal experiment
- **AND** it SHALL NOT create a duplicate experiment record.

#### Scenario: Missing experiment is imported
- **WHEN** an imported experiment cannot be safely matched to an existing formal experiment
- **THEN** the importer SHALL create a new formal experiment with server-controlled identifiers
- **AND** it SHALL record the source chapter, source title, and import metadata.

#### Scenario: Existing point matches the Markdown leaf
- **WHEN** a Markdown leaf safely matches an existing point under the resolved experiment
- **THEN** the importer SHALL reuse that point key
- **AND** it SHALL update import metadata without changing existing question bindings.

#### Scenario: Missing point is imported
- **WHEN** a Markdown leaf cannot be safely matched under the resolved experiment
- **THEN** the importer SHALL create a new point using a deterministic key compatible with the existing candidate point-key shape
- **AND** it SHALL preserve the leaf title, full folder path, source order, and source chapter in metadata.

#### Scenario: Duplicate leaf titles exist
- **WHEN** two leaf points share the same normalized title under the same experiment
- **THEN** the importer SHALL use full folder path and source order to disambiguate them
- **AND** it SHALL NOT merge them solely by title.

### Requirement: Three-part point description import
The system SHALL import point descriptions into the existing point learning-content model.

#### Scenario: Description matches an imported point
- **WHEN** a point description block contains experiment principle, phenomenon explanation, and safety note sections
- **THEN** the importer SHALL store those sections as the point's principle text, phenomenon explanation, and safety note
- **AND** it SHALL keep the content in draft status unless an explicit publication step publishes it.

#### Scenario: Description point is missing from the catalog
- **WHEN** a three-part description references a point that does not exist after catalog import
- **THEN** the importer SHALL create the missing point under the resolved experiment when the experiment can be resolved
- **AND** it SHALL report unresolved descriptions when the experiment cannot be resolved safely.

#### Scenario: Descriptions are re-imported
- **WHEN** the same Markdown description is imported again
- **THEN** the importer SHALL update the existing point learning content idempotently
- **AND** it SHALL record content hash, source file, and import timestamp metadata.

### Requirement: Import report and auditability
The system SHALL produce an import report that makes catalog mutations auditable.

#### Scenario: Import dry run is requested
- **WHEN** an operator runs the import in dry-run mode
- **THEN** the system SHALL report matched experiments, created experiments, matched points, created points, updated descriptions, duplicates, and unresolved records
- **AND** it SHALL NOT mutate database state.

#### Scenario: Import is applied
- **WHEN** an operator applies the import
- **THEN** every created or updated experiment, point, or content row SHALL include import metadata
- **AND** the final report SHALL include counts that can be compared against the Markdown leaf-point count.
