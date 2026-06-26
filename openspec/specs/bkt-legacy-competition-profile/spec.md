# bkt-legacy-competition-profile Specification

## Purpose
TBD - created by archiving change add-bkt-legacy-competition-profile. Update Purpose after archive.
## Requirements
### Requirement: Legacy competition profile is a separate product profile
The system SHALL provide a legacy competition profile made of separate old student and old teacher frontend products that share the current backend and core data.

#### Scenario: Legacy profile is inspected
- **WHEN** a maintainer inspects the implemented legacy profile
- **THEN** it MUST expose a student product identified as `web-student-old`
- **AND** it MUST expose a teacher product identified as `web-teacher-old`
- **AND** both products MUST use the same backend API and database as the current products
- **AND** the profile MUST NOT require a separate legacy database, legacy seed corpus, or legacy backend fork

#### Scenario: Current products are inspected after legacy profile is added
- **WHEN** a maintainer opens the current `web-student` or `web-teacher` products
- **THEN** the current green Atom/RAG product behavior MUST remain available
- **AND** old-profile navigation, old SYSU-red theme, and old forbidden-term gating MUST NOT replace current product behavior

### Requirement: Legacy profile centers the BKT competition narrative
The legacy profile SHALL present BKT knowledge tracing as the core personalization mechanism for experiment-video learning and smart assessment composition.

#### Scenario: Legacy product narrative is shown
- **WHEN** a student, teacher, or competition reviewer views the legacy profile's primary pages
- **THEN** visible copy MUST frame the system around inorganic chemistry experiment learning, experiment knowledge units, BKT knowledge tracing, student mastery, personalized video recommendation, smart assessment composition, and teacher learning-score review
- **AND** visible copy MUST NOT frame the old product around RAG, Agent, Atom, retrieval diagnostics, provider monitoring, or generic chatbot capability

#### Scenario: Legacy feedback loop is demonstrated
- **WHEN** the legacy profile is used for a demo flow
- **THEN** the flow MUST be able to demonstrate `AI出题 -> 教师审核 -> 题库 -> 学生测评 -> BKT掌握度 -> 推荐视频/智能组卷 -> 教师查看学情分数`
- **AND** every visible step MUST have a legacy student or teacher surface that explains the step without exposing RAG/Agent internals

### Requirement: Legacy profile hides RAG Agent Atom implementation language
The legacy profile SHALL hide implementation terminology associated with the current RAG/Agent/Atom product line from all old visible user interfaces.

#### Scenario: Legacy visible UI is scanned
- **WHEN** rendered legacy student and teacher pages, navigation, modals, drawers, toasts, empty states, error states, table headers, and button labels are scanned
- **THEN** they MUST NOT contain visible terms such as `Atom`, `RAG`, `Agent`, `chunk`, `embedding`, `rerank`, `Qwen`, `BGE`, `OpenAI`, `ES诊断`, `智能监控`, or `学习助手`
- **AND** the scan MUST allow legacy-facing terms such as `AI出题`, `BKT`, `掌握度`, `个性化推荐`, `智能组卷`, `学情分数`, `教材依据`, and `出题依据`

#### Scenario: Backend returns diagnostic or provider wording to an old frontend
- **WHEN** a backend response or error contains raw diagnostic, retrieval, provider, model, or agent wording
- **THEN** the old frontend MUST render a controlled legacy-facing message
- **AND** it MUST NOT show the raw internal wording as normal visible UI

### Requirement: Legacy visual identity uses SYSU red branding
The legacy profile SHALL use official SYSU red branding and traditional teaching-platform visual language that is distinct from the current green modern product.

#### Scenario: Legacy brand tokens are inspected
- **WHEN** the legacy frontend theme is inspected
- **THEN** it MUST define SYSU red as the canonical primary brand color using the official SVG-derived red value approximately `#740003`
- **AND** the legacy theme MUST NOT depend on the current green Atom/RAG theme tokens for primary navigation, primary buttons, active states, or brand marks

#### Scenario: Legacy SYSU assets are used
- **WHEN** a legacy frontend is built
- **THEN** required SYSU logo assets MUST be loaded from repository-managed old-app assets
- **AND** those assets MUST originate from the official SYSU asset directory supplied during specification
- **AND** the build MUST NOT reference `E:\迅雷下载\sysu-logo-main` as a runtime or build-time path

#### Scenario: Reviewer compares old and current products
- **WHEN** a reviewer compares the old products with the current products
- **THEN** the old products MUST differ in primary color, school identity, navigation composition, page layout rhythm, player treatment, and AI/RAG copy exposure
- **AND** the difference MUST be more substantial than a color-token swap

### Requirement: Legacy profile preserves shared data self-consistency
The legacy profile SHALL reuse current runtime data without creating old-only seed mutations that can diverge from the current backend state.

#### Scenario: Legacy products read catalog and assessment data
- **WHEN** the old student or teacher frontend loads catalog, video, question bank, assessment, mastery, or analytics data
- **THEN** it MUST read from the same backend API and database records used by current products
- **AND** it MUST NOT transform seed identities into old-only ids that cannot be used by current backend services

#### Scenario: Legacy profile is deployed after seed validation
- **WHEN** production resource validation or seed validation is run
- **THEN** legacy frontend assets MUST NOT require changing chemistry dictionaries, question-bank seed records, student learning profiles, or media binding identities
- **AND** any legacy-specific sample or branding asset MUST be isolated from runtime chemistry seed data
