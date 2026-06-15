# 19-4-08 Rebuild Report

## Packet Scope

- Packet id: 19-4-08
- Chunk: chunk_2
- Experiment: 硝酸根的检验
- Input packet: `semantic_work_packets/chunk_2/19-4-08.json`
- Rebuilt JSON output: `rebuilt_packages/chunk_2/19-4-08_rebuilt_v1.json`
- Report output: `rebuilt_reports/chunk_2/19-4-08_rebuild_report.md`
- Direct release JSON modification: not performed.

## Manual Reconstruction Statement

I manually read the source packet and the cited RAG chunks, then manually read and semantically reconstructed question by question. This report documents manual per-question reconstruction, not batch generation.

## Semantic Points Covered

- `candidate-1-b2e54d23`: FeSO₄·7H₂O + NaNO₃ + 浓 H₂SO₄ 棕色环实验。
- `candidate-2-90ed6d74`: 静置、不振荡，观察棕色环形成。

## Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite ID List

- REBUILT_CH2_19_4_08_Q001
- REBUILT_CH2_19_4_08_Q002
- REBUILT_CH2_19_4_08_Q003
- REBUILT_CH2_19_4_08_Q004
- REBUILT_CH2_19_4_08_Q005
- REBUILT_CH2_19_4_08_Q006
- REBUILT_CH2_19_4_08_Q007
- REBUILT_CH2_19_4_08_Q008
- REBUILT_CH2_19_4_08_Q009
- REBUILT_CH2_19_4_08_Q010
- REBUILT_CH2_19_4_08_Q011
- REBUILT_CH2_19_4_08_Q012
- REBUILT_CH2_19_4_08_Q013
- REBUILT_CH2_19_4_08_Q014
- REBUILT_CH2_19_4_08_Q015
- REBUILT_CH2_19_4_08_Q016
- REBUILT_CH2_19_4_08_Q017
- REBUILT_CH2_19_4_08_Q018
- REBUILT_CH2_19_4_08_Q019
- REBUILT_CH2_19_4_08_Q020
- REBUILT_CH2_19_4_08_Q021
- REBUILT_CH2_19_4_08_Q022
- REBUILT_CH2_19_4_08_Q023
- REBUILT_CH2_19_4_08_Q024
- REBUILT_CH2_19_4_08_Q025
- REBUILT_CH2_19_4_08_Q026
- REBUILT_CH2_19_4_08_Q027
- REBUILT_CH2_19_4_08_Q028
- REBUILT_CH2_19_4_08_Q029
- REBUILT_CH2_19_4_08_Q030

## Edge Keeps

- None. No old item was retained verbatim.
- The inherited `expchunk_00243_765fc7b450` also contains adjacent nitrate oxidation and nitrate thermal decomposition content, so only its nitrate-test operation and redox equation were used for this packet.

## Evidence Insufficient List

- None. All 30 questions are evidence-sufficient and publishable under the cited experiment and theory chunks.

## Multi-Point List With Reasons

- REBUILT_CH2_19_4_08_Q006: ties the post-acid addition operation to the brown-ring observation point.
- REBUILT_CH2_19_4_08_Q007: explains why the no-shaking observation condition matters for the brown-ring experiment.
- REBUILT_CH2_19_4_08_Q008: connects the expected brown-ring phenomenon with the reagent-based test.
- REBUILT_CH2_19_4_08_Q009: integrates nitrate reduction, NO formation, and static observation.
- REBUILT_CH2_19_4_08_Q011: distinguishes this packet's brown-ring method from the adjacent alkaline aluminum nitrate test.
- REBUILT_CH2_19_4_08_Q012: asks for a complete observation record combining operation and result.
- REBUILT_CH2_19_4_08_Q014: links the qualitative nitrate-test conclusion to the visible brown-ring evidence.
- REBUILT_CH2_19_4_08_Q020: checks both oxidation-reduction chemistry and brown-ring formation, not just mixing.
- REBUILT_CH2_19_4_08_Q024: fill-blank operation item tied to the observation condition and brown-ring formation.
- REBUILT_CH2_19_4_08_Q025: fill-blank color item tied to both the observation condition and brown product.
- REBUILT_CH2_19_4_08_Q027: summarizes both video points in one scope question.
- REBUILT_CH2_19_4_08_Q028: troubleshooting item linking missing ring observation to possible interface disruption.
- REBUILT_CH2_19_4_08_Q029: explicitly integrates chemistry producing the brown species with static observation of the ring.
- REBUILT_CH2_19_4_08_Q030: scope/misconception item covering reagent chemistry and observation conditions together.

## Fill-Blank Risk List

- REBUILT_CH2_19_4_08_Q023: answers `硝酸根`, `硝酸根离子`; low risk, no formula input required.
- REBUILT_CH2_19_4_08_Q024: answers `振荡`, `摇动`; low risk, operation verb.
- REBUILT_CH2_19_4_08_Q025: answers `棕`, `棕色`; low risk, color word.
- REBUILT_CH2_19_4_08_Q026: answer `一氧化氮`; low risk, Chinese name used instead of formula.

## Evidence IDs Used

- Canonical experiment chunks:
  - `expchunk_00243_765fc7b450`
  - `expchunk_00244_53c663efb4`
- Supporting theory chunks:
  - `textbook_prose_00522_c509852695`
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
