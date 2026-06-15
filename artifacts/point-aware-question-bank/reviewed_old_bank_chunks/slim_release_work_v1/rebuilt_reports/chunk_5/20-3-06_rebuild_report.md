# Rebuild Report: chunk_5 / 20-3-06

## Packet

- Packet id / experiment code: `20-3-06`
- Experiment title: 配合物的形成对氧化还原性的影响
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-06.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-06_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `20`
- Rewrite: `10`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_06_018`, `CHK5_SEM_EXP_20_3_06_019`, `CHK5_SEM_EXP_20_3_06_020`, `CHK5_SEM_EXP_20_3_06_021`, `CHK5_SEM_EXP_20_3_06_022`, `CHK5_SEM_EXP_20_3_06_023`, `CHK5_SEM_EXP_20_3_06_024`, `CHK5_SEM_EXP_20_3_06_026`, `CHK5_SEM_EXP_20_3_06_029`, `CHK5_SEM_EXP_20_3_06_030`

## Evidence Insufficient

- None.

## Evidence Used

- Canonical procedure and comparisons: `expchunk_00332_42b6908ee0`
- Canonical thought questions on Fe³⁺ masking and Ag recovery: `expchunk_00336_68bde523f4`
- Fe³⁺ oxidizes iodide to iodine: `textbook_prose_00037_a7dbd4c099`, `textbook_prose_00039_cb1a979cf8`
- F⁻ complexes Fe³⁺: `textbook_table_record_table_p224_t01_r071`

Excluded inherited locators:

- `textbook_prose_01297_b761f39d9a`, `textbook_prose_01340_c4d5e485b6` and adjacent Pt/Prussian-blue records: not needed for this packet's Fe/F/EDTA/Ag redox comparisons.

## Multi-Point Questions

- Q007, Q008, Q015, Q020, and Q028 intentionally bind multiple points because they summarize the whole experiment.
- EDTA/Ag questions bind to both the Fe(Ⅱ)+AgNO₃ baseline and the EDTA comparison when needed.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_06_025` | `电势`, `电极电势` | `氧化还原电势` | low | kept |
| `CHK5_SEM_EXP_20_3_06_027` | `减弱`, `降低` | `下降`, `变弱` | low | kept |
| `CHK5_SEM_EXP_20_3_06_028` | `氧化还原反应`, `氧化还原性` | `氧化还原过程` | low | kept |

No visible fill answer requires typing formulas such as Fe³⁺, Fe²⁺, I₂, CCl₄, AgNO₃, or EDTA.

## Validation Notes

- JSON parse: passed.
- Question ids: passed.
- Single-choice answers: passed.
- True/false labels and boolean answers: passed.
- Fill-blank accepted answers: passed.
- Option links: passed.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed after changing the visible `Pb(OH)₂` distractor to `氢氧化铅`.
- Release JSON direct edit: no `chunk_5_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `17`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_06_001`, `CHK5_SEM_EXP_20_3_06_002`, `CHK5_SEM_EXP_20_3_06_003`, `CHK5_SEM_EXP_20_3_06_004`, `CHK5_SEM_EXP_20_3_06_005`, `CHK5_SEM_EXP_20_3_06_007`, `CHK5_SEM_EXP_20_3_06_008`, `CHK5_SEM_EXP_20_3_06_011`, `CHK5_SEM_EXP_20_3_06_012`, `CHK5_SEM_EXP_20_3_06_014`, `CHK5_SEM_EXP_20_3_06_017`, `CHK5_SEM_EXP_20_3_06_020`, `CHK5_SEM_EXP_20_3_06_021`, `CHK5_SEM_EXP_20_3_06_022`, `CHK5_SEM_EXP_20_3_06_023`, `CHK5_SEM_EXP_20_3_06_024`, `CHK5_SEM_EXP_20_3_06_028`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
