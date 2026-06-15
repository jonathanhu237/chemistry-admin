# 19-5-01 Rebuild Report

## Packet Scope

- Packet id: 19-5-01
- Chunk: chunk_2
- Experiment: 难溶性硅酸盐的生成——“水中花园”
- Input packet: `semantic_work_packets/chunk_2/19-5-01.json`
- Rebuilt JSON output: `rebuilt_packages/chunk_2/19-5-01_rebuilt_v1.json`
- Report output: `rebuilt_reports/chunk_2/19-5-01_rebuild_report.md`
- Direct release JSON modification: not performed.

## Manual Reconstruction Statement

I manually read the source packet and the cited RAG chunks, then manually read and semantically reconstructed question by question. This report documents manual per-question reconstruction, not batch generation.

## Semantic Points Covered

- `candidate-1-397a1298`: 水玻璃 + CaCl₂。
- `candidate-2-df9b9095`: 水玻璃 + CuSO₄。
- `candidate-3-97208db2`: 水玻璃 + Co(NO₃)₂。
- `candidate-4-b89f131c`: 水玻璃 + NiSO₄。
- `candidate-5-5855225d`: 水玻璃 + MnSO₄。
- `candidate-6-8f1b6ad6`: 水玻璃 + ZnSO₄。
- `candidate-7-d1ef41c4`: 水玻璃 + FeCl₂。
- `candidate-8-2b740a96`: 水玻璃 + FeCl₃。

## Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite ID List

- REBUILT_CH2_19_5_01_Q001
- REBUILT_CH2_19_5_01_Q002
- REBUILT_CH2_19_5_01_Q003
- REBUILT_CH2_19_5_01_Q004
- REBUILT_CH2_19_5_01_Q005
- REBUILT_CH2_19_5_01_Q006
- REBUILT_CH2_19_5_01_Q007
- REBUILT_CH2_19_5_01_Q008
- REBUILT_CH2_19_5_01_Q009
- REBUILT_CH2_19_5_01_Q010
- REBUILT_CH2_19_5_01_Q011
- REBUILT_CH2_19_5_01_Q012
- REBUILT_CH2_19_5_01_Q013
- REBUILT_CH2_19_5_01_Q014
- REBUILT_CH2_19_5_01_Q015
- REBUILT_CH2_19_5_01_Q016
- REBUILT_CH2_19_5_01_Q017
- REBUILT_CH2_19_5_01_Q018
- REBUILT_CH2_19_5_01_Q019
- REBUILT_CH2_19_5_01_Q020
- REBUILT_CH2_19_5_01_Q021
- REBUILT_CH2_19_5_01_Q022
- REBUILT_CH2_19_5_01_Q023
- REBUILT_CH2_19_5_01_Q024
- REBUILT_CH2_19_5_01_Q025
- REBUILT_CH2_19_5_01_Q026
- REBUILT_CH2_19_5_01_Q027
- REBUILT_CH2_19_5_01_Q028
- REBUILT_CH2_19_5_01_Q029
- REBUILT_CH2_19_5_01_Q030

## Edge Keeps

- None. No old item was retained verbatim.
- RAG does not provide per-salt color or morphology details for the water-garden products, so the rebuild does not ask unsupported color/shape questions.
- The supporting theory chunks were used only for sodium silicate/silicate background; operational facts come from `expchunk_00258_f50c9441d1`.

## Evidence Insufficient List

- None. All 30 questions are evidence-sufficient and publishable under the cited experiment and theory chunks.

## Multi-Point List With Reasons

- REBUILT_CH2_19_5_01_Q001: covers all eight salts through the common product class,难溶性硅酸盐.
- REBUILT_CH2_19_5_01_Q002: water glass is the common main solution across all eight salt points.
- REBUILT_CH2_19_5_01_Q006: groups the four listed sulfate salts into one point-list recognition item.
- REBUILT_CH2_19_5_01_Q007: uses all eight points because position tracking applies to every salt.
- REBUILT_CH2_19_5_01_Q008: sample-size rule applies to all listed solid salts.
- REBUILT_CH2_19_5_01_Q009: observation-time rule applies after all listed salts are placed.
- REBUILT_CH2_19_5_01_Q010: compares the two iron salt points, FeCl₂ and FeCl₃.
- REBUILT_CH2_19_5_01_Q011: exact-list negative item referencing listed Ca, Zn, and Fe salts.
- REBUILT_CH2_19_5_01_Q012: position-recording quality applies across all eight salts.
- REBUILT_CH2_19_5_01_Q013: experiment design item covering multi-salt comparison.
- REBUILT_CH2_19_5_01_Q014: scope-control item covering the whole water-garden packet.
- REBUILT_CH2_19_5_01_Q015: compares CuSO₄ and ZnSO₄ point handling through the position rule.
- REBUILT_CH2_19_5_01_Q016: interprets the water-garden phenomenon across all salt points.
- REBUILT_CH2_19_5_01_Q017: true/false operation item covering all listed solids.
- REBUILT_CH2_19_5_01_Q018: placement rule covering all salts.
- REBUILT_CH2_19_5_01_Q019: exact-list true/false item for the four sulfate salts.
- REBUILT_CH2_19_5_01_Q020: exact-list true/false item for the two iron chloride salts.
- REBUILT_CH2_19_5_01_Q021: rejects mixing all salts because the protocol needs separate positions.
- REBUILT_CH2_19_5_01_Q022: observation-time statement applying to all placed salts.
- REBUILT_CH2_19_5_01_Q023: scope statement tying all points to难溶性硅酸盐 formation.
- REBUILT_CH2_19_5_01_Q024: water-glass fill item applies across the whole setup.
- REBUILT_CH2_19_5_01_Q025: position fill item applies to all salts.
- REBUILT_CH2_19_5_01_Q026: observation-time fill item applies to all salts.
- REBUILT_CH2_19_5_01_Q027: product-class fill item applies to all salts.
- REBUILT_CH2_19_5_01_Q028: exact-list item covering all eight salt points.
- REBUILT_CH2_19_5_01_Q029: position-recording rationale across all eight salt points.
- REBUILT_CH2_19_5_01_Q030: packet learning objective across all eight salt points.

## Fill-Blank Risk List

- REBUILT_CH2_19_5_01_Q024: answer `水玻璃`; low risk, reagent name.
- REBUILT_CH2_19_5_01_Q025: answers `不同`, `不同的`; low risk, operation adjective.
- REBUILT_CH2_19_5_01_Q026: answers `一小时`, `约一小时`; low risk, Chinese time phrase.
- REBUILT_CH2_19_5_01_Q027: answer `硅酸盐`; low risk, concept noun.

## Evidence IDs Used

- Canonical experiment chunk:
  - `expchunk_00258_f50c9441d1`
- Supporting theory chunks:
  - `textbook_prose_00731_22ff2d736a`
  - `textbook_prose_00739_3b9f1f082f`

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
