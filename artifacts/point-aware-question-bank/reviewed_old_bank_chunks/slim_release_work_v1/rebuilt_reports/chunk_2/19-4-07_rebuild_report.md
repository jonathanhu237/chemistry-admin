# 19-4-07 Rebuild Report

## Packet Scope

- Packet id: 19-4-07
- Chunk: chunk_2
- Experiment: 硝酸盐的热分解
- Input packet: `semantic_work_packets/chunk_2/19-4-07.json`
- Rebuilt JSON output: `rebuilt_packages/chunk_2/19-4-07_rebuilt_v1.json`
- Report output: `rebuilt_reports/chunk_2/19-4-07_rebuild_report.md`
- Direct release JSON modification: not performed.

## Manual Reconstruction Statement

I manually read the source packet and the cited RAG chunks, then manually read and semantically reconstructed question by question. This report documents manual per-question reconstruction, not batch generation.

## Semantic Points Covered

- `candidate-1-2241ae7a`: KNO₃ 热分解。
- `candidate-2-aa0424f2`: Cu(NO₃)₂ 热分解。
- `candidate-3-91bbea2b`: AgNO₃ 热分解。
- `candidate-4-29485ccd`: 用火柴余烬检验热分解生成的气体。

## Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite ID List

- REBUILT_CH2_19_4_07_Q001
- REBUILT_CH2_19_4_07_Q002
- REBUILT_CH2_19_4_07_Q003
- REBUILT_CH2_19_4_07_Q004
- REBUILT_CH2_19_4_07_Q005
- REBUILT_CH2_19_4_07_Q006
- REBUILT_CH2_19_4_07_Q007
- REBUILT_CH2_19_4_07_Q008
- REBUILT_CH2_19_4_07_Q009
- REBUILT_CH2_19_4_07_Q010
- REBUILT_CH2_19_4_07_Q011
- REBUILT_CH2_19_4_07_Q012
- REBUILT_CH2_19_4_07_Q013
- REBUILT_CH2_19_4_07_Q014
- REBUILT_CH2_19_4_07_Q015
- REBUILT_CH2_19_4_07_Q016
- REBUILT_CH2_19_4_07_Q017
- REBUILT_CH2_19_4_07_Q018
- REBUILT_CH2_19_4_07_Q019
- REBUILT_CH2_19_4_07_Q020
- REBUILT_CH2_19_4_07_Q021
- REBUILT_CH2_19_4_07_Q022
- REBUILT_CH2_19_4_07_Q023
- REBUILT_CH2_19_4_07_Q024
- REBUILT_CH2_19_4_07_Q025
- REBUILT_CH2_19_4_07_Q026
- REBUILT_CH2_19_4_07_Q027
- REBUILT_CH2_19_4_07_Q028
- REBUILT_CH2_19_4_07_Q029
- REBUILT_CH2_19_4_07_Q030

## Edge Keeps

- None. No old item was retained verbatim.
- `expchunk_00244_53c663efb4` appears near this textbook section but describes nitrate brown-ring style detection / Fe(NO)SO₄ content, so it was not used as core evidence for this thermal-decomposition packet.

## Evidence Insufficient List

- None. All 30 questions are evidence-sufficient and publishable under the cited experiment and theory chunks.

## Multi-Point List With Reasons

- REBUILT_CH2_19_4_07_Q003: links the gas-test operation to all three decomposition samples because the glowing match/splint is the common gas-identification step.
- REBUILT_CH2_19_4_07_Q007: links KNO₃ decomposition with the gas-test point because active nitrate decomposition is confirmed experimentally through oxygen release.
- REBUILT_CH2_19_4_07_Q008: links AgNO₃ decomposition with the gas-test point because AgNO₃ thermal decomposition produces oxygen along with NO₂ and Ag.
- REBUILT_CH2_19_4_07_Q014: asks for comparison across KNO₃, Cu(NO₃)₂, and AgNO₃, with the gas-test operation as the shared observation frame.
- REBUILT_CH2_19_4_07_Q017: links AgNO₃ products with the gas-test point because oxygen release is part of the observed decomposition result.
- REBUILT_CH2_19_4_07_Q018: compares KNO₃ and AgNO₃ decomposition patterns and keeps the gas-test point as supporting evidence.
- REBUILT_CH2_19_4_07_Q023: asks for the experiment's comparison objective across the three nitrates, with the gas-test point included as supporting context.

## Fill-Blank Risk List

- REBUILT_CH2_19_4_07_Q021: answer `硝酸盐`; low risk, concept noun directly stated by the experiment title.
- REBUILT_CH2_19_4_07_Q022: answers `火柴余烬`, `余烬`; low risk, operation wording follows canonical evidence.
- REBUILT_CH2_19_4_07_Q023: answers `异同`, `异同点`; low risk, accepted answers cover the ordinary wording variation.
- REBUILT_CH2_19_4_07_Q024: answer `加热`; low risk, simple operation verb with no formula requirement.

## Evidence IDs Used

- Canonical experiment chunk:
  - `expchunk_00243_765fc7b450`
- Supporting theory chunks:
  - `textbook_prose_00562_ef6a65a064`
  - `textbook_prose_00563_d9dcf3d136`
  - `textbook_prose_00564_d916ee2d9c`
  - `textbook_prose_00565_4ff80431a2`

## Validation

- JSON parse: passed.
- Question count: 30.
- Unique IDs: passed.
- Single-choice answer/options and option_links alignment: passed.
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
