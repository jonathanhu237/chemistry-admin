## MODIFIED Requirements

### Requirement: RAG-gated workbench access
The system SHALL require a healthy configured textbook RAG runtime before a teacher can start or continue AI-assisted question creation or repair in the point-aware question workbench.

#### Scenario: Teacher opens AI creation when textbook RAG is healthy
- **WHEN** a teacher selects an experiment or experiment point and textbook RAG is enabled, Elasticsearch is healthy, the active chunk index matches the configured Qwen embedding model, and Qwen rerank is healthy
- **THEN** the workbench SHALL allow the teacher to start an AI create session
- **AND** it SHALL show that generated candidates will use reranked textbook evidence.

#### Scenario: Teacher opens AI repair when textbook RAG is unhealthy
- **WHEN** a teacher selects AI repair for an existing question while textbook RAG is disabled, Elasticsearch is unreachable, the chunk index is stale, embedding is unavailable, or rerank is unavailable
- **THEN** the workbench SHALL prevent starting the AI repair session
- **AND** it SHALL show the missing RAG condition in teacher-readable language.

#### Scenario: Teacher sends a prompt after textbook RAG becomes unhealthy
- **WHEN** a teacher has an open workbench session and sends a follow-up prompt after the configured textbook RAG runtime is no longer healthy
- **THEN** the backend SHALL reject candidate generation
- **AND** the UI SHALL preserve prior turns and candidates while showing the gate failure.

### Requirement: Evidence-first workbench context
The workbench SHALL show the selected experiment, target point context, source evidence package, and RAG health before or alongside teacher prompts.

#### Scenario: Create workbench targets multiple points
- **WHEN** a teacher starts AI creation for multiple points under one experiment
- **THEN** the workbench SHALL record all selected point keys in the session context
- **AND** the context panel SHALL show those target points before generation.

#### Scenario: Repair workbench uses bound points
- **WHEN** a teacher starts AI repair from an existing point-aware question
- **THEN** the workbench SHALL derive target points from the question's bound primary point metadata
- **AND** the teacher prompt SHALL refine intent without directly editing the original question structure.

#### Scenario: Workbench shows sectioned evidence diagnostics
- **WHEN** a workbench session has textbook RAG source references or retrieval diagnostics
- **THEN** the workbench SHALL show the evidence package grouped by principle, phenomenon, and safety section
- **AND** it SHALL show source count, missing sections, retrieval mode, and whether the evidence came from Qwen-reranked textbook chunks.

## ADDED Requirements

### Requirement: Current authoring controls are preserved
The workbench SHALL keep the current teacher-facing add and repair controls while changing the evidence source behind generation.

#### Scenario: Teacher starts add-mode generation
- **WHEN** a teacher starts add-mode AI generation from the current question-bank workflow
- **THEN** the workbench SHALL preserve the existing selectable objective question types and count behavior
- **AND** it SHALL send selected type and count intent along with textbook evidence to the LLM.

#### Scenario: Teacher starts repair-mode generation
- **WHEN** a teacher starts repair-mode AI generation from an existing question
- **THEN** the workbench SHALL remain anchored to the original question, original question type, point bindings, source audit, and repair lineage
- **AND** it SHALL generate repair candidates rather than mutating the published question directly.
