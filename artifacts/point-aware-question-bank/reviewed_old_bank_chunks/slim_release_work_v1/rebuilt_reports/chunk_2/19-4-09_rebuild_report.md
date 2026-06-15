# 19-4-09 Rebuild Report

## Packet Scope

- Packet id: 19-4-09
- Chunk: chunk_2
- Experiment: 硝酸根的检验
- Input packet: `semantic_work_packets/chunk_2/19-4-09.json`
- Rebuilt JSON output: `rebuilt_packages/chunk_2/19-4-09_rebuilt_v1.json`
- Report output: `rebuilt_reports/chunk_2/19-4-09_rebuild_report.md`
- Direct release JSON modification: not performed.

## Manual Reconstruction Statement

I manually read the source packet and the cited RAG chunks, then manually read and semantically reconstructed question by question. This report documents manual per-question reconstruction, not batch generation.

## Semantic Points Covered

- `candidate-1-520f0192`: FeSO₄·7H₂O + NaNO₃ + 浓 H₂SO₄。
- `candidate-2-a452c505`: 观察棕色环。

## Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite ID List

- REBUILT_CH2_19_4_09_Q001
- REBUILT_CH2_19_4_09_Q002
- REBUILT_CH2_19_4_09_Q003
- REBUILT_CH2_19_4_09_Q004
- REBUILT_CH2_19_4_09_Q005
- REBUILT_CH2_19_4_09_Q006
- REBUILT_CH2_19_4_09_Q007
- REBUILT_CH2_19_4_09_Q008
- REBUILT_CH2_19_4_09_Q009
- REBUILT_CH2_19_4_09_Q010
- REBUILT_CH2_19_4_09_Q011
- REBUILT_CH2_19_4_09_Q012
- REBUILT_CH2_19_4_09_Q013
- REBUILT_CH2_19_4_09_Q014
- REBUILT_CH2_19_4_09_Q015
- REBUILT_CH2_19_4_09_Q016
- REBUILT_CH2_19_4_09_Q017
- REBUILT_CH2_19_4_09_Q018
- REBUILT_CH2_19_4_09_Q019
- REBUILT_CH2_19_4_09_Q020
- REBUILT_CH2_19_4_09_Q021
- REBUILT_CH2_19_4_09_Q022
- REBUILT_CH2_19_4_09_Q023
- REBUILT_CH2_19_4_09_Q024
- REBUILT_CH2_19_4_09_Q025
- REBUILT_CH2_19_4_09_Q026
- REBUILT_CH2_19_4_09_Q027
- REBUILT_CH2_19_4_09_Q028
- REBUILT_CH2_19_4_09_Q029
- REBUILT_CH2_19_4_09_Q030

## Edge Keeps

- None. No old item was retained verbatim.
- `expchunk_00243_765fc7b450` also includes neighboring nitrate oxidation and nitrate thermal decomposition material; those neighboring topics were used only for scope exclusion, not as core content for new questions.
- Unlike 19-4-08, this packet's point list does not explicitly make `静置、不振荡` a core point, so the rebuild focuses on reagent combination and brown-ring observation.

## Evidence Insufficient List

- None. All 30 questions are evidence-sufficient and publishable under the cited experiment and theory chunks.

## Multi-Point List With Reasons

- REBUILT_CH2_19_4_09_Q005: links the visible brown-ring observation to the reagent/reaction source of the brown species.
- REBUILT_CH2_19_4_09_Q008: asks for the complete reagent set while tying it to the brown-ring packet scope.
- REBUILT_CH2_19_4_09_Q010: prevents reducing the packet to only concentrated sulfuric acid by requiring reagent plus observation logic.
- REBUILT_CH2_19_4_09_Q011: identifies the brown species and connects it to the underlying reagent chemistry.
- REBUILT_CH2_19_4_09_Q012: checks valid and invalid conclusions across reagent role and observation.
- REBUILT_CH2_19_4_09_Q013: summarizes acid redox and brown species formation in one principle item.
- REBUILT_CH2_19_4_09_Q015: distinguishes this brown-ring nitrate test from the adjacent nitrate thermal-decomposition packet.
- REBUILT_CH2_19_4_09_Q017: links observed brown ring to NO/Fe²⁺ related species formation.
- REBUILT_CH2_19_4_09_Q021: combines reagent roles, acidic medium, and brown-ring observation.
- REBUILT_CH2_19_4_09_Q022: scope-control item separating this packet from nitrate thermal decomposition.
- REBUILT_CH2_19_4_09_Q027: pairs the reagent-combination point with the observation point.
- REBUILT_CH2_19_4_09_Q028: connects observed brown ring with the nitrate-test conclusion.
- REBUILT_CH2_19_4_09_Q029: requires the brown observation to be interpreted under the specified reagent/acid conditions.
- REBUILT_CH2_19_4_09_Q030: integrates the two video points into the packet learning objective.

## Fill-Blank Risk List

- REBUILT_CH2_19_4_09_Q023: answers `硝酸根`, `硝酸根离子`; low risk, no formula input required.
- REBUILT_CH2_19_4_09_Q024: answer `一氧化氮`; low risk, Chinese name used instead of formula.
- REBUILT_CH2_19_4_09_Q025: answers `棕色环`, `棕环`; low risk, observation phrase.
- REBUILT_CH2_19_4_09_Q026: answer `浓硫酸`; low risk, Chinese reagent name used instead of formula.

## Evidence IDs Used

- Canonical experiment chunks:
  - `expchunk_00243_765fc7b450`
  - `expchunk_00244_53c663efb4`
- Supporting theory chunks:
  - `textbook_prose_00522_c509852695`
  - `textbook_prose_00556_a4150c286e`
  - `textbook_prose_00558_9cffe40305`

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
