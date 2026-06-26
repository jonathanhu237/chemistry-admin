# assistant-chem-latex-rendering Specification

## Purpose
TBD - created by archiving change assistant-chem-latex-rendering. Update Purpose after archive.
## Requirements
### Requirement: Model chemistry math output contract
The learning assistant SHALL instruct answer-generation models to emit chemistry and math notation in renderer-supported formats.

#### Scenario: Model formats chemistry reactions
- **WHEN** the assistant asks a model to answer a chemistry learning question
- **THEN** the prompt SHALL require inline formulas to use `$...$`
- **AND** block formulas to use `$$...$$`
- **AND** chemistry formulas or reactions to use `\ce{...}` when appropriate
- **AND** whole reaction equations to be emitted as one `\ce{...}` expression using mhchem arrows such as `->`, not split into multiple `\ce` fragments
- **AND** loose mhchem forms such as `\ceKMnO4`, `\ceCl2`, `\ceMn^{2+}`, and reaction arrows such as `-->`, `-- >`, or `\rightarrow` SHALL be explicitly forbidden
- **AND** raw LaTeX commands such as `\mathrm`, `\ce`, `\ch`, or `\rightarrow` SHALL NOT be emitted outside math delimiters.

### Requirement: Backend normalizes assistant formula output
The learning assistant backend SHALL normalize final assistant answers before returning them to clients.

#### Scenario: Bare chemistry command is produced
- **WHEN** a final answer contains bare formula commands such as `\ce{...}`, `\ch{...}`, or `\mathrm{...}` outside math delimiters
- **THEN** the backend SHALL repair the text by wrapping safe formula segments in math delimiters
- **AND** the final response SHALL avoid exposing the raw command as ordinary prose.

#### Scenario: Alternate math delimiters are produced
- **WHEN** a final answer contains `\(...\)` or `\[...\]`
- **THEN** the backend SHALL normalize those delimiters to renderer-supported inline or block math syntax.

#### Scenario: Loose mhchem reaction is produced
- **WHEN** a final answer contains malformed reaction notation such as `\ceCl2 + 2Br^- --> 2Cl^- + Br2`
- **THEN** the backend SHALL repair it to a renderer-supported whole-reaction expression such as `$\\ce{Cl2 + 2Br^- -> 2Cl^- + Br2}$`
- **AND** the final response SHALL NOT expose loose `\ce...` commands or non-mhchem reaction arrows as ordinary prose.

#### Scenario: Answer text contains code blocks
- **WHEN** a final answer contains fenced code blocks
- **THEN** backend formula normalization SHALL NOT rewrite content inside code blocks.

### Requirement: Frontend renders chemistry math robustly
The learning assistant frontend SHALL render Markdown with chemistry/math support instead of exposing raw LaTeX commands.

#### Scenario: Completed answer includes chemistry formulas
- **WHEN** a completed assistant answer contains `$\\ce{Cl2 + 2Br- -> 2Cl- + Br2}$`, `$\\mathrm{Cl_2}$`, or `$0.1\\,\\mathrm{mol\\cdot L^{-1}}$`
- **THEN** the frontend SHALL render the notation as math/chemistry content
- **AND** the student-visible answer SHALL NOT contain raw `\ce`, `\mathrm`, `\rightarrow`, or `\cdot` text.

#### Scenario: Evidence preview includes source LaTeX
- **WHEN** a fixed point source or RAG source preview contains chemistry/math LaTeX
- **THEN** the frontend SHALL render it through the same math-capable renderer
- **AND** authenticated RAG image rendering SHALL continue to work.

#### Scenario: Math rendering fails
- **WHEN** a formula segment cannot be parsed by the math renderer
- **THEN** the frontend SHALL fall back to readable sanitized text
- **AND** it SHALL NOT display common raw LaTeX command words to students.

### Requirement: Formula rendering regressions are tested
The project SHALL include regression tests that prevent common chemistry LaTeX leaks.

#### Scenario: Backend normalization test
- **WHEN** backend tests run against representative malformed assistant outputs
- **THEN** they SHALL verify final normalized text wraps or repairs common chemistry/math commands.

#### Scenario: Frontend no-leak test
- **WHEN** frontend rendering tests run against representative chemistry answers
- **THEN** they SHALL fail if student-visible rendered output contains raw `\ce`, `\ch`, `\mathrm`, `\rightarrow`, or `\cdot`
- **AND** they SHALL fail if KaTeX renders a chemistry formula as `.katex-error`.

### Requirement: Student report AI text renders chemistry Markdown
Student-facing AI or fallback text in posttest reports SHALL use the math-capable Markdown rendering path when displayed in the H5 app.

#### Scenario: Posttest summary contains chemistry notation
- **WHEN** a student views a posttest summary containing Markdown, math, or chemistry notation
- **THEN** the H5 app MUST render the content through the chemistry/math-capable Markdown renderer
- **AND** the visible report MUST avoid exposing raw supported LaTeX commands as ordinary text.

#### Scenario: Mistake explanation contains chemistry notation
- **WHEN** a student views an AI-generated or fallback mistake explanation containing chemistry notation
- **THEN** the H5 app MUST render the content through the same renderer used for assistant chemistry answers
- **AND** rendering failures MUST fall back to readable sanitized text rather than breaking the report.

### Requirement: Chemistry math rendering works in streaming and completed paths
The learning assistant frontend SHALL preserve chemistry and math rendering behavior across both Streamdown active-answer rendering and static completed-answer rendering.

#### Scenario: Active streamed answer contains supported chemistry notation
- **WHEN** the active assistant answer contains supported chemistry notation such as `$\\ce{Cl2 + 2Br^- -> 2Cl^- + Br2}$`
- **THEN** the streaming renderer MUST attempt to render the notation using KaTeX with mhchem support
- **AND** the active answer MUST remain readable while the stream is still incomplete.

#### Scenario: Completed answer contains supported chemistry notation
- **WHEN** the same answer reaches final completion
- **THEN** the static renderer MUST render the completed notation through the chemistry/math-capable static Markdown path
- **AND** the visible completed answer MUST NOT expose supported raw `\\ce`, `\\ch`, `\\mathrm`, `\\rightarrow`, or `\\cdot` commands as ordinary prose.

#### Scenario: Streaming and static renderers differ internally
- **WHEN** Streamdown and `react-markdown` use different plugin chains internally
- **THEN** both renderers MUST still accept the established assistant output contract of `$...$`, `$$...$$`, and `\\ce{...}` inside math delimiters
- **AND** both renderers MUST share normalization rules for `\\(...\\)` and `\\[...\\]` delimiters where practical.

#### Scenario: Chemistry notation is split across stream events
- **WHEN** stream chunks divide a chemistry expression across multiple `delta` events
- **THEN** the active renderer MUST avoid crashing or permanently exposing partial parser errors
- **AND** the completed renderer MUST render the valid final formula when all chunks have arrived.

### Requirement: Formula normalization remains fenced-block aware
The learning assistant frontend SHALL keep formula normalization from corrupting fenced code blocks, Mermaid diagrams, or other preformatted Markdown blocks.

#### Scenario: Formula-like text appears inside Mermaid
- **WHEN** a Mermaid code fence contains chemistry labels, arrows, or formula-like text
- **THEN** frontend formula normalization MUST NOT rewrite Mermaid source in a way that breaks diagram parsing
- **AND** the Mermaid renderer or fallback block MUST receive the intended diagram source.

#### Scenario: Formula-like text appears inside fenced code fallback
- **WHEN** an answer contains a non-Mermaid fenced block with formula-like text
- **THEN** frontend formula normalization MUST NOT rewrite the fenced block content
- **AND** the block MUST render as safe preformatted fallback content.

#### Scenario: Formula-like text appears in ordinary prose
- **WHEN** ordinary answer prose contains supported alternate math delimiters such as `\\(...\\)` or `\\[...\\]`
- **THEN** frontend normalization SHOULD convert them to the renderer-supported inline or block math delimiters
- **AND** conversion MUST preserve the visible formula semantics.

### Requirement: Chemistry formula failures are student-readable
The learning assistant frontend SHALL handle math or chemistry render failures without breaking the answer turn.

#### Scenario: Streaming math plugin rejects a formula
- **WHEN** the Streamdown math plugin rejects or cannot yet parse a formula during active streaming
- **THEN** the active answer MUST remain visible
- **AND** the failure MUST NOT crash the assistant panel or block later chunks from rendering.

#### Scenario: Static renderer rejects a formula
- **WHEN** the static renderer cannot parse a completed formula
- **THEN** the answer MUST fall back to readable sanitized text or inline code treatment for that formula
- **AND** the rest of the Markdown answer MUST continue rendering.

#### Scenario: KaTeX error markup would be visible
- **WHEN** a formula failure would create `.katex-error` or equivalent error markup
- **THEN** student-facing tests MUST detect the leak
- **AND** the implementation MUST prefer readable fallback text over exposed renderer error chrome.

### Requirement: Chemistry Markdown examples cover teaching patterns
The learning assistant frontend SHALL validate chemistry-rich Markdown using examples that match the application's teaching context.

#### Scenario: Acid-base answer is rendered
- **WHEN** a representative answer explains pH or acid-base equilibrium using `$pH=-\\log[H^+]$` and `$$K_a=\\frac{[H^+][A^-]}{[HA]}$$`
- **THEN** the formulas MUST render in both active and completed answer states where supported
- **AND** the completed state MUST be regression tested.

#### Scenario: Reaction equation answer is rendered
- **WHEN** a representative answer contains a whole reaction equation such as `$\\ce{2H2 + O2 -> 2H2O}$`
- **THEN** the chemistry equation MUST render through mhchem
- **AND** the visible answer MUST avoid raw command leakage.

#### Scenario: Observation table answer is rendered
- **WHEN** a representative answer uses a GFM table to compare `CO2`, `NH3`, `Cl2`, and `O2` test methods
- **THEN** the table MUST render as a table
- **AND** formulas inside table cells MUST remain readable and overflow-safe.
