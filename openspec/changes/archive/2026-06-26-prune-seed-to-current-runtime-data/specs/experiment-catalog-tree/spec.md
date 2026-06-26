## ADDED Requirements

### Requirement: Seeded current catalog point content
The system SHALL seed current catalog point content from the reviewed 76-record point-content seed.

#### Scenario: Current point content seed is validated
- **WHEN** the point-content seed is validated
- **THEN** every record MUST resolve to exactly one current catalog point node and one current canonical point id
- **AND** validation MUST confirm 76 records, 71 equation-mode records, 5 text-mode records, and 122 reaction equation rows.

#### Scenario: Current point content is imported
- **WHEN** current point content seed is imported
- **THEN** equation-mode records MUST populate structured reaction equations, phenomenon explanation, and safety note for the mapped point node
- **AND** text-mode records MUST populate text principle content, phenomenon explanation, and safety note for the mapped point node.

#### Scenario: Current point content drives student search
- **WHEN** current point content is imported in an indexable status
- **THEN** student search document builders MUST index the student-facing principle, phenomenon, safety, catalog title, and catalog path content
- **AND** indexing MUST NOT require old experiment video point evidence, old 30-example content, or local BGE embeddings.

## MODIFIED Requirements

### Requirement: Destructive legacy model replacement
The system SHALL retire legacy experiment-parent write paths and old seed-derived experiment data after replacing the catalog seed with the canonical outline-backed tree.

#### Scenario: Legacy admin point API is called
- **WHEN** a client calls the old experiment video-point write API after the catalog seed replacement
- **THEN** the system MUST not process the write as an authoritative path
- **AND** tests MUST verify application code uses catalog-node APIs.

#### Scenario: Catalog seed import runs
- **WHEN** the current catalog seed import runs against a database containing current catalog-node data
- **THEN** the seed/import process MUST validate and upsert current catalog tree and point-content seed rows by default
- **AND** it MUST NOT delete current question banks, questions, catalog-node evidence state, catalog-node evidence bindings, current catalog media bindings, users, roles, courses, source documents, source chunks, search dictionaries, or student learning seed data.

#### Scenario: Explicit destructive legacy cleanup runs
- **WHEN** a separately named destructive legacy cleanup operation runs
- **THEN** it MAY delete retired legacy experiment video points, legacy point content, old point evidence, old old-to-new audit maps, and retired seed-derived artifacts after protected current resources validate
- **AND** it MUST exclude current catalog-node question-bank data, current catalog-node evidence seed data, current media bindings, canonical chunks, and runtime search dictionaries from the default delete scope.

#### Scenario: Non-seed resources exist
- **WHEN** a destructive legacy cleanup runs
- **THEN** it MUST preserve canonical RAG chunks, analyzer dictionaries, users, roles, courses, current media assets, current question-bank seed data, and other current platform resources
- **AND** it MUST document which retired legacy tables or paths are intentionally reset.

### Requirement: Catalog seed replaces legacy experiment point seeds
The system SHALL use catalog node identities as the only authoritative point identity after seed replacement.

#### Scenario: Legacy point evidence is removed from seed baseline
- **WHEN** current seed cleanup runs
- **THEN** old point-to-chunk bindings keyed by legacy `(experiment_id, point_key)` MUST be deleted or left absent from current seed data
- **AND** canonical `source_chunks` MUST remain available as current corpus data.

#### Scenario: Legacy question bank is removed from seed baseline
- **WHEN** current seed cleanup runs
- **THEN** old question-bank seed data that depends on invalid legacy point identity MUST be deleted or left absent
- **AND** the system MUST treat the current default question bank as the catalog-node question-bank seed, not as empty.

#### Scenario: Validation checks legacy identity leakage
- **WHEN** production resource validation runs after the seed cleanup
- **THEN** it MUST fail if active point evidence or current question seed rows still depend only on legacy `(experiment_id, point_key)` identity
- **AND** it MUST accept references keyed by catalog node id, canonical point id, or stable catalog seed key.

## REMOVED Requirements

### Requirement: Sample point seed maps examples to catalog nodes
**Reason**: The 30-example source was an intermediate seed generation aid and is no longer current runtime seed data.

**Migration**: Use the reviewed 76-record `point_content_seed.json` as the current point-content seed. Delete the old sample mapping/audit artifacts rather than moving them into docs.

### Requirement: Seeded point content examples
**Reason**: The 30 text-mode examples have been replaced by the current 76-record seed with structured equation/text modes and current catalog-node targets.

**Migration**: Validate and import `experiment_catalog/point_content_seed.json`; remove validators and docs that expect 30 mapped examples.
