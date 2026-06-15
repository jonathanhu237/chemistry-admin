# Rebuild Report: chunk_5 / 20-3-07

## Packet

- Packet id / experiment code: `20-3-07`
- Experiment title: 配合物稳定性与配体的关系
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-07.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-07_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `19`
- Rewrite: `11`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_07_006`, `CHK5_SEM_EXP_20_3_07_016`, `CHK5_SEM_EXP_20_3_07_017`, `CHK5_SEM_EXP_20_3_07_021`, `CHK5_SEM_EXP_20_3_07_022`, `CHK5_SEM_EXP_20_3_07_023`, `CHK5_SEM_EXP_20_3_07_024`, `CHK5_SEM_EXP_20_3_07_025`, `CHK5_SEM_EXP_20_3_07_027`, `CHK5_SEM_EXP_20_3_07_028`, `CHK5_SEM_EXP_20_3_07_029`

## Evidence Insufficient

- None after rewriting the unsupported “乙二胺是典型螯合配体/螯合效应” items into canonical-supported ethylenediamine-as-ligand operation items.

## Evidence Used

- Canonical Cr/oxalate and NaOH probe: `expchunk_00332_42b6908ee0`, `expchunk_00333_d08e49be44`
- Fe³⁺/SCN⁻ blood-red complex: `textbook_prose_01304_9920c29f9d`, `textbook_table_record_table_p224_t01_r071`
- Ni²⁺ ammine context: `textbook_table_record_table_p224_t01_r061`
- Appendix ligand rows for ethylenediamine and oxalate: `textbook_table_record_table_p286_t01_r201`, `textbook_table_record_table_p286_t01_r231`

Excluded inherited locators:

- `expchunk_00334_8229cac865`, `textbook_prose_01305_dd5a94da50`, `textbook_prose_01306_0a0d67a34e`: metal-ion identification / dimethylglyoxime context, not needed for this stability-vs-ligand packet.
- Co/NCS records were not used for student-visible claims because this packet’s Fe/KSCN evidence is available directly.

## Multi-Point Questions

- Q007, Q010, Q017, Q020, and Q026 intentionally bind multiple points because they summarize the experiment scope or distinguish included vs out-of-scope operations.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_07_026` | `配体` | `配体种类` | low | kept |
| `CHK5_SEM_EXP_20_3_07_027` | `乙二胺` | `1%乙二胺`, `乙二胺溶液` | low | rewritten |
| `CHK5_SEM_EXP_20_3_07_030` | `颜色`, `颜色变化` | `显色变化` | low | kept |

No visible fill answer requires typing Cr₂(SO₄)₃, Na₂C₂O₄, FeCl₃, KSCN, NiSO₄, NH₃·H₂O, or formulas with nested parentheses.

## Validation Notes

- JSON parse: passed.
- Question ids: passed.
- Single-choice answers: passed.
- True/false labels and boolean answers: passed.
- Fill-blank accepted answers: passed.
- Option links: passed.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed.
- Release JSON direct edit: no `chunk_5_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `22`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_07_001`, `CHK5_SEM_EXP_20_3_07_002`, `CHK5_SEM_EXP_20_3_07_003`, `CHK5_SEM_EXP_20_3_07_004`, `CHK5_SEM_EXP_20_3_07_005`, `CHK5_SEM_EXP_20_3_07_006`, `CHK5_SEM_EXP_20_3_07_008`, `CHK5_SEM_EXP_20_3_07_010`, `CHK5_SEM_EXP_20_3_07_011`, `CHK5_SEM_EXP_20_3_07_014`, `CHK5_SEM_EXP_20_3_07_015`, `CHK5_SEM_EXP_20_3_07_016`, `CHK5_SEM_EXP_20_3_07_017`, `CHK5_SEM_EXP_20_3_07_020`, `CHK5_SEM_EXP_20_3_07_022`, `CHK5_SEM_EXP_20_3_07_023`, `CHK5_SEM_EXP_20_3_07_024`, `CHK5_SEM_EXP_20_3_07_025`, `CHK5_SEM_EXP_20_3_07_027`, `CHK5_SEM_EXP_20_3_07_029`, `CHK5_SEM_EXP_20_3_07_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
