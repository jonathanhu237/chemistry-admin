# hybrid-bge-rag-retrieval Specification

## Purpose
TBD - created by archiving change upgrade-learning-assistant-debug-rag. Update Purpose after archive.
## Requirements
### Requirement: Hybrid retrieval preserves existing sources
The system SHALL preserve the current learning assistant source and keyword retrieval path while adding optional BGE-based recall and reranking.

#### Scenario: Hybrid RAG is enabled
- **WHEN** the learning assistant performs retrieval with hybrid RAG enabled
- **THEN** the candidate pool SHALL include candidates from the existing source/keyword recall path
- **AND** it SHALL merge those candidates with BGE vector recall candidates before final evidence selection.

#### Scenario: Hybrid RAG is disabled
- **WHEN** hybrid BGE RAG is disabled
- **THEN** the learning assistant SHALL continue using the existing retrieval behavior
- **AND** the optional BGE service SHALL NOT be required for the request to succeed.

### Requirement: AI-generated retrieval query
The system SHALL support generating retrieval queries for RAG separately from the final student-facing answer.

#### Scenario: Query generation succeeds
- **WHEN** the backend prepares a RAG lookup for a student/admin prompt
- **THEN** it SHALL generate one or more concise retrieval queries using the configured AI provider
- **AND** it SHALL use those queries for BGE/keyword recall while retaining the original question as a fallback query.

#### Scenario: Query generation fails
- **WHEN** the configured AI provider cannot generate retrieval queries
- **THEN** the retrieval path SHALL fall back to the original user question
- **AND** the diagnostic trace SHALL record the fallback reason.

### Requirement: BGE vector recall and reranking
The system SHALL use BGE-M3 query embeddings and BGE reranker scores when the optional BGE service is enabled and available.

#### Scenario: BGE service returns an embedding
- **WHEN** the backend receives a query embedding from the BGE service
- **THEN** it SHALL search existing `chunk_embeddings` with vector similarity
- **AND** it SHALL include the highest-scoring vector candidates in the merged candidate pool.

#### Scenario: BGE reranker returns scores
- **WHEN** the merged candidate pool is sent to the BGE reranker
- **THEN** the final evidence order SHALL prefer reranked candidates according to reranker scores while preserving source metadata.

#### Scenario: BGE service is unavailable
- **WHEN** the BGE service times out, returns an error, or is not configured
- **THEN** the backend SHALL fall back to the existing retrieval path
- **AND** it SHALL include a diagnostic indicating that BGE recall or rerank was skipped.

### Requirement: Optional CPU BGE service
The BGE embedding/reranking runtime SHALL be packaged as a separate optional Docker service.

#### Scenario: RAG is off in local Docker
- **WHEN** the application is started with RAG disabled
- **THEN** the main backend SHALL start and serve non-RAG/admin routes without starting the BGE service.

#### Scenario: Hybrid RAG is enabled in local Docker
- **WHEN** hybrid BGE RAG is enabled for local testing
- **THEN** operators SHALL be able to start the BGE service independently from the main backend
- **AND** the backend SHALL reach it through a configured service URL.

### Requirement: Retrieval diagnostics
The system SHALL return admin-facing retrieval diagnostics for hybrid RAG requests.

#### Scenario: Admin inspects a RAG turn
- **WHEN** an admin selects a turn that performed retrieval
- **THEN** the diagnostics SHALL include generated queries, fallback status, recall candidates, rerank scores when available, final evidence, and the retrieval mode used.

#### Scenario: Admin inspects reranked evidence
- **WHEN** hybrid BGE reranking succeeds for a RAG turn
- **THEN** the diagnostics SHALL mark the turn as reranked
- **AND** final evidence SHALL include rank, recall source, rerank score when available, and source metadata.

#### Scenario: Admin inspects retrieval timing
- **WHEN** a RAG turn completes
- **THEN** the diagnostics SHALL include stage timing for query generation, keyword recall, BGE embedding, vector recall, reranking, merging, and total retrieval time when those stages ran
- **AND** it SHALL include candidate counts for keyword candidates, vector candidates, merged candidates, rerank pool size, and final evidence count.

### Requirement: Teacher workbench retrieval contract
The system SHALL expose hybrid RAG health and retrieval diagnostics for teacher-side question-bank AI workbench requests.

#### Scenario: Workbench checks RAG runtime
- **WHEN** the question-bank page renders AI workbench actions
- **THEN** it SHALL use the same runtime health contract as the learning assistant to decide whether RAG-backed AI actions are available
- **AND** it SHALL distinguish RAG disabled, BGE unavailable, query generation disabled, and healthy hybrid rerank states.

#### Scenario: Workbench builds an evidence package
- **WHEN** a teacher starts or continues an AI workbench session under a healthy RAG runtime
- **THEN** the backend SHALL build an evidence package for the selected experiment, point context, original question when present, and teacher prompt
- **AND** the package SHALL include source references and retrieval diagnostics when available.

#### Scenario: Workbench records reranked evidence
- **WHEN** hybrid BGE reranking succeeds for a workbench request
- **THEN** the evidence package SHALL preserve final evidence order, chunk identifiers, source metadata, and rerank score where available
- **AND** the workbench SHALL show that the candidate was grounded in reranked RAG chunks.

#### Scenario: Workbench RAG fails closed
- **WHEN** hybrid RAG cannot provide healthy reranked evidence for a workbench request
- **THEN** the system SHALL block AI candidate generation rather than silently falling back to ungrounded local generation
- **AND** it SHALL return a diagnostic reason that the UI can display.
