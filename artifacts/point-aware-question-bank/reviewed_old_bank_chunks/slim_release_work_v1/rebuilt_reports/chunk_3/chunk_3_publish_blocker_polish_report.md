# chunk_3 Publish-Blocker Polish Report

Date: 2026-06-15

## Scan Scope

Polish scope was limited to rebuilt package student-visible fields:

- `stem`
- `options[].text`
- `explanation`
- visible `answer.value` / `answer.accepted_answers[]`
- `hint`, `analysis`, `feedback` when present
- `option_links[].diagnostic_note`

Out of scope and not edited by this polish pass:

- release JSON files, including `chunk_3_release_final_v1.json`
- `question_id`
- `primary_point_keys` / `secondary_point_keys`
- `point_key`
- `canonical_chunk_ids`
- `supporting_theory_chunk_ids`
- source/evidence file locators and metadata identity fields

## Fixed Packets

- `19-6-02`
- `19-6-03`
- `19-6-04`
- `19-8-01`
- `19-8-02`
- `19-8-03`
- `19-8-04`
- `19-8-05`
- `19-8-06`
- `19-8-07`
- `19-8-08`
- `19-8-09`
- `19-8-10`
- `19-8-11`
- `20-1-01`

## Fix Rules

The pass scanned by rule categories, not by example-word replacement only.

- Internal review/process traces were removed from student-visible text: `RAG`, `canonical`, `supporting theory`, `theory`, `packet`, `expchunk`, `textbook_prose`, `textbook_table_record`, `evidence`, `locator`, `old/rebuilt/release/script/mobile/deterministic` style wording.
- Process-style Chinese wording was normalized: `旧题`, `原包`, `重构`, `证据优先`, `证据边界`, `证据层级`, `发布标准`, `隐藏别名`, `别名判分`.
- ASCII numeric-subscript formulas were converted to Unicode subscripts where formulas remained visible.
- ASCII charge notation was converted to superscript charge notation where visible.
- Visible formula prompts that were really input-risk notes were rewritten as normal student-facing Chinese.
- Chemical distractors that were not the target content were kept only as normal chemistry wording, not as source/audit traces.

## Fixed Question ID List

All fixed IDs retain their original `question_id` values. The publish-blocker scan covered every rebuilt question in the fixed packet range:

- `REBUILT_CH3_19_6_02_Q001` through `REBUILT_CH3_19_6_02_Q030`
- `REBUILT_CH3_19_6_03_Q001` through `REBUILT_CH3_19_6_03_Q030`
- `REBUILT_CH3_19_6_04_Q001` through `REBUILT_CH3_19_6_04_Q030`
- `REBUILT_CH3_19_8_01_Q001` through `REBUILT_CH3_19_8_01_Q030`
- `REBUILT_CH3_19_8_02_Q001` through `REBUILT_CH3_19_8_02_Q030`
- `REBUILT_CH3_19_8_03_Q001` through `REBUILT_CH3_19_8_03_Q030`
- `REBUILT_CH3_19_8_04_Q001` through `REBUILT_CH3_19_8_04_Q030`
- `REBUILT_CH3_19_8_05_Q001` through `REBUILT_CH3_19_8_05_Q030`
- `REBUILT_CH3_19_8_06_Q001` through `REBUILT_CH3_19_8_06_Q030`
- `REBUILT_CH3_19_8_07_Q001` through `REBUILT_CH3_19_8_07_Q030`
- `REBUILT_CH3_19_8_08_Q001` through `REBUILT_CH3_19_8_08_Q030`
- `REBUILT_CH3_19_8_09_Q001` through `REBUILT_CH3_19_8_09_Q030`
- `REBUILT_CH3_19_8_10_Q001` through `REBUILT_CH3_19_8_10_Q030`
- `REBUILT_CH3_19_8_11_Q001` through `REBUILT_CH3_19_8_11_Q030`
- `REBUILT_CH3_20_1_01_Q001` through `REBUILT_CH3_20_1_01_Q030`

## Per-Question Field Classes Fixed

The affected visible fields by rule class were:

- stems: removed process wording such as `RAG`, `canonical`, `packet`, `supporting theory`, `旧题`, `重构`.
- option text: removed process wording and normalized visible formula/charge notation.
- explanations: removed source locator names, source chunk names, review notes, mobile/grading notes, and process-language justifications.
- diagnostic notes: removed packet/point/evidence audit phrasing and converted it to normal student-facing feedback.
- visible fill answers: kept short Chinese answers where possible and removed ASCII formula-input requirements.

## Before / After Snippets

Representative fixes:

| Category | Before | After |
| --- | --- | --- |
| Internal trace | `按 RAG 实验步骤` | `按教材实验步骤` |
| Source chunk trace | `expchunk_00266 明确给出...本 packet` | `教材实验步骤明确给出...本实验` |
| Source label | `canonical 文本` | `教材文本` |
| Theory trace | `supporting theory` / `theory` | `相关理论` |
| Packet trace | `本 packet` / `本小包` | `本实验` |
| Process wording | `旧题...重构...发布标准` | `这类题...改写...命题标准` |
| Formula input risk | `HNO3`, `CaCl2`, `MnSO4`, `CCl4` | `HNO₃`, `CaCl₂`, `MnSO₄`, `CCl₄` |
| Charge notation | `Pb2+`, `Fe3+`, `MnO4-` | `Pb²⁺`, `Fe³⁺`, `MnO₄⁻` |
| Reagent abbreviation | `KSCN` | `硫氰酸钾` |
| Grading/platform trace | `手机端输入和机器判分` | `输入和稳定作答` |

## Integrity Confirmations

- Release JSON unchanged by this polish pass: confirmed; no release JSON was targeted or written.
- `question_id` unchanged: confirmed by JSON parse and unique-id validation.
- Point keys unchanged: not edited by this polish pass.
- Evidence IDs unchanged: not edited by this polish pass.
- Rebuilt package count: 15 JSON files.
- Rebuilt question count: 450 questions.
- Unique question IDs per file: 30 / 30 for every packet.

Note: the wider working tree already showed release JSON files as modified before this polish closeout. This polish pass did not write those files.

## Final Validation

Final visible-field category scan result:

- internal review traces: 0
- ASCII numeric-subscript formulas: 0
- ASCII charge/ion notation: 0
- caret/LaTeX/Markdown chemical symbols: 0
- student-visible process notes: 0

Final structural validation:

- JSON parse: pass
- rebuilt package files: 15
- total rebuilt questions: 450
- unique question IDs: pass
- release JSON direct modification: none
