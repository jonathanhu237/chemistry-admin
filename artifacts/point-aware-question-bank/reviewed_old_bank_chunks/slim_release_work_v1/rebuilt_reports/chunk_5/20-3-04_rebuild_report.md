# Rebuild Report: chunk_5 / 20-3-04

## Packet

- Packet id / experiment code: `20-3-04`
- Experiment title: 观察不同配体的 Co(Ⅱ) 配合物的颜色
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-04.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-04_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `19`
- Rewrite: `11`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_04_018`, `CHK5_SEM_EXP_20_3_04_021`, `CHK5_SEM_EXP_20_3_04_022`, `CHK5_SEM_EXP_20_3_04_023`, `CHK5_SEM_EXP_20_3_04_024`, `CHK5_SEM_EXP_20_3_04_025`, `CHK5_SEM_EXP_20_3_04_026`, `CHK5_SEM_EXP_20_3_04_027`, `CHK5_SEM_EXP_20_3_04_028`, `CHK5_SEM_EXP_20_3_04_029`, `CHK5_SEM_EXP_20_3_04_030`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_3_04_001`-`010`: kept because each maps to canonical setup, reagent source, water/acetone effects, control purpose, or directly supported Co color information.
- `CHK5_SEM_EXP_20_3_04_011`-`017`, `019`, and `020`: kept because the true/false statements are directly determined by the canonical procedure or equation; formula-heavy wording was normalized to phone-safe text where needed.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `CHK5_SEM_EXP_20_3_04_002`, `005`, `007`, `011`, `016`, `018`, `020`, `021`, `026`, and `030` bind multiple points because they test the three-tube comparison or the relationship between water and acetone treatments.
- Single-condition questions bind to the relevant initial, control, water, or acetone point.

## Fill-Blank Mobile Risk

- None. This rebuilt packet uses only single-choice and true/false items.
- Formula-reading items were converted to single-choice or Chinese wording so students do not need to type complex formulas.

## RAG Evidence IDs Used

- Canonical Co(Ⅱ) procedure and equation: `expchunk_00331_3f7cc41ff9`
- Common iron-group complex table context: `textbook_table_context_p224_0e08e79e44`
- Co(Ⅱ) water and thiocyanate complex colors: `textbook_table_record_table_p224_t01_r051`
- Fe(Ⅲ)-thiocyanate blood-red contrast, used only to avoid wrong-context confusion: `textbook_table_record_table_p224_t01_r071`

Rejected or excluded locator ids from the source packet:

- None. The inherited table row for Fe(Ⅲ)-thiocyanate is kept only as a contrast source, not as primary evidence for the cobalt experiment.

## Duplicate Resolution

The source packet repeated a generic “Co(Ⅱ)-SCN 配合物在水和丙酮条件下” shell across later items. The rebuilt packet separates this into water/acetone shift, three-tube setup, evidence sufficiency, ligand color contrast, record completeness, water ligand count, Fe/Co thiocyanate confusion, experiment conclusion, and missing-control diagnosis.

## Validation Notes

- JSON parse: passed.
- Question ids: unique.
- Single-choice answers: aligned with option labels.
- Option links: every single-choice option has one concrete semantic diagnostic.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed.
- Release JSON direct edit: no `chunk_5_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `23`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_04_001`, `CHK5_SEM_EXP_20_3_04_002`, `CHK5_SEM_EXP_20_3_04_003`, `CHK5_SEM_EXP_20_3_04_004`, `CHK5_SEM_EXP_20_3_04_006`, `CHK5_SEM_EXP_20_3_04_007`, `CHK5_SEM_EXP_20_3_04_009`, `CHK5_SEM_EXP_20_3_04_011`, `CHK5_SEM_EXP_20_3_04_012`, `CHK5_SEM_EXP_20_3_04_013`, `CHK5_SEM_EXP_20_3_04_014`, `CHK5_SEM_EXP_20_3_04_018`, `CHK5_SEM_EXP_20_3_04_019`, `CHK5_SEM_EXP_20_3_04_020`, `CHK5_SEM_EXP_20_3_04_021`, `CHK5_SEM_EXP_20_3_04_023`, `CHK5_SEM_EXP_20_3_04_024`, `CHK5_SEM_EXP_20_3_04_026`, `CHK5_SEM_EXP_20_3_04_027`, `CHK5_SEM_EXP_20_3_04_028`, `CHK5_SEM_EXP_20_3_04_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
