## MODIFIED Requirements

### Requirement: Intelligent monitoring page covers AI, RAG, ES, and chemistry retrieval
The teacher console SHALL provide a monitoring surface that summarizes AI provider health, external textbook RAG health, Elasticsearch search health, dictionary asset health, and chemistry retrieval readiness.

#### Scenario: Teacher opens global monitoring
- **WHEN** an authenticated teacher opens the intelligent monitoring page
- **THEN** the page MUST show separate status sections for AI provider connectivity, external textbook RAG runtime, ES index health, and chemistry dictionary assets
- **AND** it MUST show the effective backend configuration such as whether search is using Elasticsearch, local fallback, disabled mode, or an unavailable service.

#### Scenario: Monitoring data is partially unavailable
- **WHEN** one monitored subsystem cannot be reached
- **THEN** the page MUST show the failed subsystem and teacher-readable reason
- **AND** it MUST continue rendering the available AI, RAG, ES, and dictionary sections.

#### Scenario: Student accesses monitoring data
- **WHEN** a student calls student-facing APIs or opens student H5 pages
- **THEN** the system MUST NOT expose raw monitoring data, ES internals, dictionary file hashes, generated query diagnostics, job payloads, rerank traces, analyzer tokens, or external provider diagnostics.
