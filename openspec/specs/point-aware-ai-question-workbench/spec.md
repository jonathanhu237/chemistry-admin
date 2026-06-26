# point-aware-ai-question-workbench Specification

## Purpose
TBD - created by archiving change redesign-point-aware-ai-question-workbench. Update Purpose after archive.
## Requirements
### Requirement: AI question workbench sessions
The system SHALL represent AI-assisted question repair and creation as persistent workbench sessions.

#### Scenario: Teacher starts a repair session
- **WHEN** a teacher starts AI repair from an existing point-aware question
- **THEN** the system SHALL create or reopen a repair workbench session for that question
- **AND** the session SHALL reference the original question id, formal experiment id, selected point context when available, operator, creation time, and session status.

#### Scenario: Teacher starts a create session
- **WHEN** a teacher starts AI creation from a selected formal experiment or experiment point
- **THEN** the system SHALL create or reopen a create workbench session
- **AND** the session SHALL reference the formal experiment id, selected point key when available, operator, creation time, and session status.

#### Scenario: Session is reopened
- **WHEN** a teacher reopens an unfinished workbench session
- **THEN** the system SHALL restore prior chat turns, generated candidates, candidate statuses, selected context, and validation results.

### Requirement: Original-question context during repair
The repair workbench SHALL keep the original question and its point-aware metadata visible while the teacher prompts AI.

#### Scenario: Repair workbench opens
- **WHEN** the repair workbench is opened for an existing question
- **THEN** the workbench SHALL show the original stem, options when present, deterministic answer, explanation, status, linked experiment, primary point keys, point titles, source audit, source references, and review lineage
- **AND** the original context SHALL remain visible while the teacher reads chat history, writes prompts, reviews candidates, or publishes a candidate.

#### Scenario: Single-choice repair uses option diagnostics
- **WHEN** the original single-choice question has option-level diagnostic links
- **THEN** the workbench SHALL show each option's diagnostic role and linked point or note beside the original question context
- **AND** generated single-choice candidates SHALL expose comparable option diagnostics before publication.

#### Scenario: Fill-blank repair uses accepted answers
- **WHEN** the original fill-blank question has accepted answer aliases or matching rules
- **THEN** the workbench SHALL show the deterministic accepted-answer set
- **AND** generated fill-blank candidates SHALL show their deterministic accepted-answer set before publication.

### Requirement: Multi-turn AI repair conversation
The workbench SHALL support multi-turn teacher prompts within a single AI assistance session.

#### Scenario: Teacher sends a follow-up prompt
- **WHEN** a teacher sends a follow-up prompt in an existing workbench session
- **THEN** the system SHALL append the teacher message as a new chat turn
- **AND** the AI request SHALL include the server-built session context, relevant prior turns or session memory, and the teacher's latest instruction.

#### Scenario: AI returns a response
- **WHEN** the AI provider or local fallback returns a response
- **THEN** the system SHALL append an assistant turn to the session
- **AND** any generated question candidates SHALL be linked to that assistant turn.

#### Scenario: Generation fails
- **WHEN** an AI request fails
- **THEN** the workbench SHALL preserve the teacher prompt in the session
- **AND** it SHALL show an actionable failure state without discarding previous turns or candidates.

### Requirement: Candidate comparison and validation
The workbench SHALL present generated candidates as comparable, validation-gated versions.

#### Scenario: Candidate is generated for repair
- **WHEN** a repair candidate is generated
- **THEN** the workbench SHALL show the candidate next to or near the original question with changed stem, options, answer, explanation, point bindings, source audit, and option diagnostics highlighted in teacher-readable form.

#### Scenario: Candidate is generated for creation
- **WHEN** a create candidate is generated
- **THEN** the workbench SHALL show the candidate with formal experiment context, selected point context when available, source references, point bindings, answer, explanation, and validation readiness.

#### Scenario: Candidate validation runs
- **WHEN** a candidate is stored or refreshed
- **THEN** the system SHALL validate objective type, deterministic answer shape, primary point keys, source audit, option diagnostic links where applicable, and generation lineage
- **AND** the workbench SHALL show whether the candidate is publishable, needs revision, or failed validation.

#### Scenario: Candidate is not publishable
- **WHEN** validation fails for a generated candidate
- **THEN** the workbench SHALL prevent publication of that candidate
- **AND** it SHALL show the validation errors so the teacher can prompt another revision.

### Requirement: Non-mutating candidate adoption
The workbench SHALL keep AI candidates non-student-facing until a teacher explicitly publishes a valid candidate.

#### Scenario: Teacher rejects a candidate
- **WHEN** a teacher rejects a generated candidate
- **THEN** the system SHALL mark the candidate rejected
- **AND** the live question bank SHALL remain unchanged.

#### Scenario: Teacher requests another revision
- **WHEN** a teacher asks for another revision after reviewing a candidate
- **THEN** the system SHALL keep the prior candidate and its status
- **AND** it SHALL add any newly generated candidate as a separate candidate version.

#### Scenario: Teacher publishes a candidate
- **WHEN** a teacher publishes a valid generated candidate
- **THEN** the system SHALL create or update the appropriate published question-bank record only after explicit confirmation
- **AND** it SHALL record session id, generating turn id, candidate id, original question id when repairing, operator, publish time, source audit, and validation result.

#### Scenario: Repair candidate is published
- **WHEN** a teacher publishes a repair candidate for an existing question
- **THEN** the system SHALL record lineage to the original question
- **AND** it SHALL follow an explicit replace, disable-original, or add-as-new policy rather than silently mutating the original question.

### Requirement: Workbench access and continuity
The workbench SHALL be reachable from normal question-bank browsing without hiding the teacher's current context.

#### Scenario: Teacher opens workbench from question detail
- **WHEN** a teacher chooses AI repair from a question detail surface
- **THEN** the system SHALL open the workbench with the selected question loaded as original context
- **AND** the teacher SHALL NOT have to close or mentally reconstruct the question detail to prompt AI.

#### Scenario: Teacher closes the workbench
- **WHEN** a teacher closes the workbench without publishing a candidate
- **THEN** the session SHALL remain available for later continuation unless the teacher explicitly discards it.

#### Scenario: Teacher returns to the question list
- **WHEN** a teacher exits the workbench
- **THEN** the question-bank page SHALL preserve the selected experiment, point filter, keyword filter, and list position when feasible.

### Requirement: Python Playwright Chrome takeover verification
The workbench SHALL be verified with Python Playwright against the teacher-visible Chrome page whenever a Chrome DevTools Protocol endpoint is available.

#### Scenario: Chrome exposes a DevTools endpoint
- **WHEN** Chrome is running with a reachable DevTools endpoint such as `http://127.0.0.1:9222`
- **THEN** the verification script SHALL connect with Python Playwright over CDP
- **AND** it SHALL reuse or open the `localhost` question-bank tab
- **AND** it SHALL verify that AI repair opens the workbench with original-question context, chat composer, and candidate area visible.

#### Scenario: Chrome does not expose a DevTools endpoint
- **WHEN** no reachable Chrome DevTools endpoint is available
- **THEN** verification SHALL report the missing endpoint as a browser-verification blocker
- **AND** it SHALL NOT claim that the teacher-visible Chrome page was inspected.

#### Scenario: Workbench screenshot is captured
- **WHEN** Python Playwright successfully attaches to Chrome and opens the workbench
- **THEN** it SHALL capture a screenshot artifact for desktop review
- **AND** it SHALL assert that original context, multi-turn chat, and candidate controls do not visibly collapse into a detached one-shot generation drawer.

### Requirement: RAG-gated workbench access
The system SHALL require a healthy external textbook RAG runtime before a teacher can start or continue AI-assisted question creation or repair in the point-aware question workbench.

#### Scenario: Teacher opens AI creation when RAG is healthy
- **WHEN** a teacher selects an experiment or experiment point and external textbook RAG is enabled, Elasticsearch index metadata is valid, embedding configuration is ready, and rerank configuration is ready
- **THEN** the workbench SHALL allow the teacher to start an AI create session
- **AND** it SHALL show that generated candidates will use textbook evidence from the configured external RAG runtime.

#### Scenario: Teacher opens AI repair when RAG is unhealthy
- **WHEN** a teacher selects AI repair for an existing question while textbook RAG is disabled, Elasticsearch is unavailable, the textbook index is missing or stale, embedding is not configured, or rerank is not configured
- **THEN** the workbench SHALL prevent starting the AI repair session
- **AND** it SHALL show the missing RAG condition in teacher-readable language.

#### Scenario: Teacher sends a prompt after RAG becomes unhealthy
- **WHEN** a teacher has an open workbench session and sends a follow-up prompt after the external textbook RAG runtime is no longer healthy
- **THEN** the backend SHALL reject candidate generation
- **AND** the UI SHALL preserve prior turns and candidates while showing the gate failure.

#### Scenario: Legacy local RAG is unavailable
- **WHEN** external textbook RAG is unhealthy
- **THEN** the workbench MUST NOT suggest starting `bge-rag`, enabling hybrid BGE, or using local model files as remediation
- **AND** it MUST NOT fall back to local-template generation that creates publishable candidates.

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

### Requirement: Teacher prompt controls intent, not structure mutation
The workbench SHALL treat teacher text as refinement instructions for AI-generated candidates rather than direct mutation of published question structure.

#### Scenario: Teacher requests a revision
- **WHEN** a teacher asks the AI to change wording, diagnostic options, difficulty, or explanation
- **THEN** the system SHALL generate a new candidate version
- **AND** it SHALL keep the previous candidate and the published question unchanged until explicit validated publication.

#### Scenario: Candidate fails structural validation
- **WHEN** an AI candidate lacks deterministic answer shape, point bindings, source audit, lineage, or required option diagnostics
- **THEN** the workbench SHALL prevent publication
- **AND** it SHALL guide the teacher to request another AI revision.

### Requirement: Duplicate-aware candidate generation
The point-aware AI question workbench SHALL annotate generated candidates with same-point duplicate-risk metadata.

#### Scenario: Candidate is generated
- **WHEN** the workbench stores a generated candidate and its backing draft
- **THEN** the backend SHALL evaluate duplicate risk against published questions, active drafts, and earlier candidates in the same generation batch for the same point
- **AND** it SHALL store the duplicate-risk result in the draft payload metadata.

#### Scenario: Teacher edits a draft candidate
- **WHEN** a teacher saves edits to a workbench draft candidate
- **THEN** the backend SHALL recompute duplicate risk for the edited payload
- **AND** the updated draft SHALL retain the latest duplicate-risk result.

#### Scenario: Candidate is published
- **WHEN** a teacher publishes a workbench candidate or its backing draft
- **THEN** the backend SHALL refresh duplicate-risk metadata before publication
- **AND** it SHALL allow publication even when duplicate risk is present.

### Requirement: Generation uses precomputed evidence only
The workbench SHALL use precomputed selected evidence bindings as the only textbook evidence source for AI candidate generation.

#### Scenario: Selected evidence exists
- **WHEN** selected point evidence bindings are fresh or partial
- **THEN** the backend SHALL build the workbench evidence package from those bindings
- **AND** it SHALL call the final chat-generation model with that evidence.

#### Scenario: Selected evidence is unavailable
- **WHEN** selected point evidence bindings are missing, stale, failed, disabled, or unavailable
- **THEN** the backend SHALL block generation
- **AND** it SHALL NOT fall back to live Qwen embedding, Elasticsearch recall, or Qwen rerank.

#### Scenario: Candidate diagnostics exist
- **WHEN** candidate evidence diagnostics exist for the selected point
- **THEN** the backend MAY expose those diagnostics in admin inspection payloads
- **AND** it SHALL NOT send candidate-only chunks to the final chat-generation model.

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
