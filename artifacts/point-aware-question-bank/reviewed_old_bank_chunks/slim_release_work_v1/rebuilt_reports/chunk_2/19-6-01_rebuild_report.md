# 19-6-01 Rebuild Report

## Packet Scope

- Packet id: 19-6-01
- Chunk: chunk_2
- Experiment: 金属钠燃烧及产物性质
- Input packet: `semantic_work_packets/chunk_2/19-6-01.json`
- Rebuilt JSON output: `rebuilt_packages/chunk_2/19-6-01_rebuilt_v1.json`
- Report output: `rebuilt_reports/chunk_2/19-6-01_rebuild_report.md`
- Direct release JSON modification: not performed.

## Manual Reconstruction Statement

I manually read the source packet and the cited RAG chunks, then manually read and semantically reconstructed question by question. This report documents manual per-question reconstruction, not batch generation.

## Semantic Points Covered

- `candidate-1-137976d3`: 金属钠加热燃烧。
- `candidate-2-43d12c37`: 燃烧产物加水溶解。
- `candidate-3-42b0372b`: 检验溶液 pH。
- `candidate-4-4e7f7f6c`: 酸化后加入 KMnO₄，检验过氧化物 / 过氧化氢相关性质。

## Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite ID List

- REBUILT_CH2_19_6_01_Q001
- REBUILT_CH2_19_6_01_Q002
- REBUILT_CH2_19_6_01_Q003
- REBUILT_CH2_19_6_01_Q004
- REBUILT_CH2_19_6_01_Q005
- REBUILT_CH2_19_6_01_Q006
- REBUILT_CH2_19_6_01_Q007
- REBUILT_CH2_19_6_01_Q008
- REBUILT_CH2_19_6_01_Q009
- REBUILT_CH2_19_6_01_Q010
- REBUILT_CH2_19_6_01_Q011
- REBUILT_CH2_19_6_01_Q012
- REBUILT_CH2_19_6_01_Q013
- REBUILT_CH2_19_6_01_Q014
- REBUILT_CH2_19_6_01_Q015
- REBUILT_CH2_19_6_01_Q016
- REBUILT_CH2_19_6_01_Q017
- REBUILT_CH2_19_6_01_Q018
- REBUILT_CH2_19_6_01_Q019
- REBUILT_CH2_19_6_01_Q020
- REBUILT_CH2_19_6_01_Q021
- REBUILT_CH2_19_6_01_Q022
- REBUILT_CH2_19_6_01_Q023
- REBUILT_CH2_19_6_01_Q024
- REBUILT_CH2_19_6_01_Q025
- REBUILT_CH2_19_6_01_Q026
- REBUILT_CH2_19_6_01_Q027
- REBUILT_CH2_19_6_01_Q028
- REBUILT_CH2_19_6_01_Q029
- REBUILT_CH2_19_6_01_Q030

## Edge Keeps

- None. No old item was retained verbatim.
- Old/source items mentioning flame color were not retained because the inspected RAG chunks did not provide enough direct evidence for a publishable flame-color question.
- The pH questions were limited to the canonical requirement to test pH; the rebuild does not overclaim a specific pH value beyond the cited procedure.

## Evidence Insufficient List

- None. All 30 questions are evidence-sufficient and publishable under the cited experiment and theory chunks.

## Multi-Point List With Reasons

- REBUILT_CH2_19_6_01_Q004: links sodium combustion product handling with the prior combustion step.
- REBUILT_CH2_19_6_01_Q005: connects product dissolution to later pH and KMnO₄ tests.
- REBUILT_CH2_19_6_01_Q006: pH test depends on the prior dissolution/cooling step.
- REBUILT_CH2_19_6_01_Q007: acidification step belongs to the post-dissolution KMnO₄ test.
- REBUILT_CH2_19_6_01_Q008: integrates combustion product, dissolution, and acidified KMnO₄ test rationale.
- REBUILT_CH2_19_6_01_Q009: operation-sequence item spanning combustion, dissolution, and pH test.
- REBUILT_CH2_19_6_01_Q010: summarizes all four packet points.
- REBUILT_CH2_19_6_01_Q011: links peroxide-water/acid theory to later KMnO₄ testing.
- REBUILT_CH2_19_6_01_Q012: connects H₂O₂/permanganate theory with the observation step.
- REBUILT_CH2_19_6_01_Q013: checks the full operation sequence across all four points.
- REBUILT_CH2_19_6_01_Q014: places pH testing after dissolution and cooling.
- REBUILT_CH2_19_6_01_Q015: connects sodium peroxide product, dissolution/acid relation, and permanganate evidence.
- REBUILT_CH2_19_6_01_Q018: links cooled product handling with the preceding combustion step.
- REBUILT_CH2_19_6_01_Q019: links pH testing with prior product dissolution and cooling.
- REBUILT_CH2_19_6_01_Q022: links sodium combustion product theory to later peroxide-property testing.
- REBUILT_CH2_19_6_01_Q025: pH fill item depends on prior dissolution/cooling.
- REBUILT_CH2_19_6_01_Q027: scope-control item spanning all packet points.
- REBUILT_CH2_19_6_01_Q028: cooling rationale spans dissolution, pH test, and KMnO₄ test.
- REBUILT_CH2_19_6_01_Q029: operation-chain item covering all four core actions.
- REBUILT_CH2_19_6_01_Q030: learning-objective item covering all four points.

## Fill-Blank Risk List

- REBUILT_CH2_19_6_01_Q023: answer `滤纸`; low risk, tool/material noun.
- REBUILT_CH2_19_6_01_Q024: answers `停止`, `停止继续`; low risk, operation verb.
- REBUILT_CH2_19_6_01_Q025: answers `pH`, `酸碱性`; low risk, short lab term and Chinese alternative.
- REBUILT_CH2_19_6_01_Q026: answers `高锰酸钾`, `高锰酸钾溶液`; low risk, Chinese reagent name used instead of formula.

## Evidence IDs Used

- Canonical experiment chunk:
  - `expchunk_00266_c041a8c010`
- Supporting theory chunks:
  - `textbook_prose_00952_bf111b030e`
  - `textbook_prose_00956_766b576ca2`
  - `textbook_prose_00295_e1465a9872`
  - `textbook_prose_00960_559616cf6d`

## Validation

- JSON parse: passed.
- Question count: 30.
- Unique IDs: passed.
- Single-choice answer/options and option_links alignment: passed.
- True/false option_links alignment and boolean answers: passed.
- Cited evidence IDs exist in RAG sources: passed.
- Evidence-insufficient publishable questions: none.
- Student-facing visible ASCII digit formulas: none.
- Complex formula fill answers: none.

## Publish Blocker Polish Final Check

- Scope: student-visible `stem`, `options[].text`, `explanation`, fill-blank accepted/visible answers, and `diagnostic_note`.
- Scan method: rule-category scan plus manual confirmation; not example-only replacement.
- Internal/process wording after polish: 0.
- ASCII digit formula after polish: 0.
- ASCII charge/ion after polish: 0.
- caret/LaTeX/Markdown chemistry after polish: 0.
- Student-visible process note after polish: 0.
- Release JSON modification during polish: not performed.
- `question_id` / point keys / evidence ids modified during polish: not performed.
