# ai-access-configuration Specification

## Purpose
TBD - created by archiving change upgrade-learning-assistant-debug-rag. Update Purpose after archive.
## Requirements
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

### Requirement: Backend setting updates follow local Docker rebuild discipline
The project SHALL document that backend source changes require rebuilding the backend Docker image in the local Compose environment.

#### Scenario: Backend AI or RAG code changes locally
- **WHEN** a developer changes backend AI, RAG, or admin API source code under the Docker Compose environment
- **THEN** they SHALL rebuild and recreate the backend service with `docker compose up -d --build backend`
- **AND** they SHALL verify the changed route or setting against the running backend instead of relying only on Vite or browser refresh.

### Requirement: H5 feature switch propagation
The system SHALL propagate admin-managed learning feature switches to the student H5 app through a pull-based configuration endpoint and enforce them again at protected action endpoints.

#### Scenario: Admin disables student AI entry
- **WHEN** an admin disables the AI learning assistant entry in system settings
- **THEN** subsequent student app-config responses MUST mark the H5 assistant entry as disabled
- **AND** the authenticated student app shell MUST hide or disable the `问答` bottom-nav entry and move any active assistant route back to a safe tab
- **AND** student assistant request endpoints MUST reject stale requests without invoking the agent.

#### Scenario: Admin disables feedback entry
- **WHEN** an admin disables the feedback entry in system settings
- **THEN** subsequent student app-config responses MUST mark the H5 feedback entry as disabled
- **AND** the `我的` tab MUST hide or disable the feedback section
- **AND** student feedback submission endpoints MUST reject stale requests.

#### Scenario: Admin disables student AI capability
- **WHEN** an admin disables student AI capability in AI feature controls
- **THEN** subsequent student app-config responses MUST mark student AI capability as disabled
- **AND** the H5 assistant tab MUST not be available even if the general learning assistant entry remains enabled.

### Requirement: Intelligent monitoring sections are independently available
The intelligent monitoring page SHALL render AI, RAG, ES, dictionary, and retrieval-diagnostic sections independently so one unavailable subsystem does not hide the others.

#### Scenario: ES is unavailable but AI provider is healthy
- **WHEN** the ES diagnostics API reports an unavailable cluster or backend
- **THEN** the page MUST still show AI provider and RAG status when those data are available
- **AND** the ES section MUST show effective backend, index name, local fallback state, and the teacher-readable failure reason.

#### Scenario: Dictionary assets are stale or missing
- **WHEN** dictionary diagnostics report missing files, changed hashes, stale analyzer assets, or a mismatch between application dictionaries and ES/IK assets
- **THEN** the page MUST show the affected dictionary category and asset state
- **AND** it MUST indicate whether the issue affects query normalization, IK tokenization, synonym expansion, formula recall, or feature recall.

#### Scenario: Retrieval diagnostic is run from monitoring
- **WHEN** an admin submits a diagnostic query from the monitoring page
- **THEN** the page MUST show normalized query terms, strict chemical synonym expansion, non-synonym feature terms, recall-route counts, and ranked point-placement results
- **AND** it MUST label the diagnostic output as teacher/operator-only data.

### Requirement: Report prompt settings live in controlled settings surfaces
The admin console SHALL expose assessment report prompt settings in settings-oriented surfaces rather than runtime monitoring.

#### Scenario: Admin edits global report prompts
- **WHEN** an administrator opens system settings
- **THEN** the console SHALL provide editable global defaults for report summary prompt and wrong-answer explanation prompt
- **AND** it SHALL provide a way to restore system-provided default prompt text.

#### Scenario: Teacher edits class report prompts
- **WHEN** a teacher with class edit access opens class settings
- **THEN** the console SHALL provide optional class-level overrides for report summary prompt and wrong-answer explanation prompt
- **AND** it SHALL indicate whether the class is inheriting global defaults or using class overrides.

#### Scenario: Monitoring page remains diagnostic
- **WHEN** a teacher opens the AI/RAG/ES monitoring page
- **THEN** the page SHALL remain focused on runtime status and diagnostics
- **AND** it SHALL not be the authoritative surface for editing report generation prompts.

### Requirement: Prompt editing exposes fixed variables
Report prompt editing SHALL expose fixed supported variables for assessment report generation.

#### Scenario: Teacher reviews available variables
- **WHEN** a teacher edits a report prompt
- **THEN** the UI SHALL show the supported variables for student, assessment, score, wrong answers, involved experiments or points, and mastery-change context
- **AND** the backend SHALL render prompts only from supported report context values.

#### Scenario: Unsupported variable is submitted
- **WHEN** a prompt includes an unsupported variable
- **THEN** the system SHALL reject the prompt with a teacher-readable validation error or ignore the unsupported variable safely
- **AND** it SHALL NOT allow arbitrary field lookup or teacher-only internal data access through prompt templates.

### Requirement: Prompt changes do not mutate historical reports
Changing report prompts SHALL affect only future report generation.

#### Scenario: Prompt changes after a report exists
- **WHEN** an administrator or teacher changes report prompts after a report has been generated
- **THEN** existing reports SHALL keep their persisted summary and wrong-answer explanation text
- **AND** opening those reports SHALL not regenerate text with the new prompt.

### Requirement: Role-based AI provider configuration
The system SHALL configure final LLM generation separately from textbook RAG embedding and rerank providers.

#### Scenario: Admin configures final question generation
- **WHEN** an admin configures the question-generation LLM
- **THEN** the system SHALL store provider role, base URL, model name, and API key for the final chat-completion provider
- **AND** this configuration SHALL be usable for DeepSeek-compatible structured question generation.

#### Scenario: Admin configures textbook embedding
- **WHEN** an admin configures the textbook RAG embedding model
- **THEN** the system SHALL store provider role, base URL, model name, API key, and expected vector dimension for the embedding provider
- **AND** the textbook chunk index SHALL report unhealthy when the active index metadata does not match this configuration.

#### Scenario: Admin configures textbook rerank
- **WHEN** an admin configures the textbook RAG rerank model
- **THEN** the system SHALL store provider role, base URL, model name, API key, and rerank thresholds for the rerank provider
- **AND** workbench retrieval SHALL use this configuration before candidate generation is allowed.

### Requirement: AI secret handling and visibility
The system SHALL store AI provider secrets as backend configuration secrets and expose only masked status outside admin edit flows.

#### Scenario: Teacher views AI-backed workbench readiness
- **WHEN** a teacher views the question workbench RAG or LLM status
- **THEN** the UI SHALL show availability, provider role, model name, and masked key fingerprint when available
- **AND** it SHALL NOT expose full API keys.

#### Scenario: Admin updates a provider without replacing its key
- **WHEN** an admin saves AI provider settings with the API key omitted
- **THEN** the system SHALL retain the previously stored key
- **AND** it SHALL update only the submitted non-secret fields.

#### Scenario: Configuration is loaded from environment
- **WHEN** environment-backed AI settings are present
- **THEN** the runtime SHALL use them as defaults or overrides according to backend configuration rules
- **AND** code SHALL NOT contain hardcoded provider API keys.

### Requirement: Textbook RAG runtime status
The system SHALL expose a runtime status for the configured textbook RAG route.

#### Scenario: Textbook RAG is healthy
- **WHEN** Elasticsearch is reachable, the active index matches the configured embedding model, and embedding and rerank checks succeed
- **THEN** the runtime status SHALL be healthy
- **AND** teacher question generation MAY proceed.

#### Scenario: Textbook RAG is unhealthy
- **WHEN** Elasticsearch, index metadata, embedding, or rerank checks fail
- **THEN** the runtime status SHALL identify the failed stage
- **AND** teacher question generation SHALL be disabled with a readable reason.

