## MODIFIED Requirements

### Requirement: AI access page naming and scope
The admin console SHALL present the former AI access entry as an intelligent monitoring concern for AI, external textbook RAG, Elasticsearch, and chemistry retrieval, while keeping provider credentials and feature switches separated according to their existing ownership boundaries.

#### Scenario: Admin views navigation
- **WHEN** an authenticated admin views the left navigation
- **THEN** the AI/RAG/ES monitoring entry SHALL be labeled with Chinese product wording such as `AI/RAG/ES monitoring`
- **AND** it SHALL avoid implying that provider credentials, RAG feature switches, ES dictionary assets, and catalog authoring behavior are all edited on the same page.

#### Scenario: Admin opens monitoring page
- **WHEN** an admin opens the intelligent monitoring route
- **THEN** the page SHALL prioritize runtime status, health checks, dictionary asset state, index state, and retrieval diagnostics for the OpenAI-compatible provider, external textbook RAG, Elasticsearch, and chemistry search
- **AND** provider, model name, base URL, API key, connection testing, and save behavior SHALL remain visually separated as credential or settings concerns when they are reachable from this page.

#### Scenario: Admin adjusts runtime behavior
- **WHEN** an admin needs to change AI feature switches, external textbook RAG settings, ES analyzer assets, or chemistry dictionaries
- **THEN** the monitoring page SHALL either deep-link to the authoritative settings/import workflow or present a role-appropriate controlled action
- **AND** it SHALL NOT silently mutate feature behavior through diagnostic probes.

### Requirement: AI feature controls are separated from provider credentials
The system SHALL visually separate feature switches, provider credentials, and runtime monitoring.

#### Scenario: Admin reviews feature switches
- **WHEN** an admin reviews student assistant, RAG, analytics, or question-bank AI switches
- **THEN** those controls SHALL live in the system settings surface rather than the monitoring page
- **AND** they SHALL be grouped under feature/range wording distinct from provider credential forms and read-only monitoring modules.

#### Scenario: Admin reviews RAG runtime state
- **WHEN** the monitoring page shows RAG settings or service status
- **THEN** the UI SHALL present the section as read-only external textbook RAG runtime status
- **AND** it SHALL make clear whether textbook RAG is disabled, missing provider configuration, missing or stale Elasticsearch index metadata, degraded by external API failure, or healthy.
