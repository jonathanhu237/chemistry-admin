# Rebuild Report: chunk_5 / 20-2-09

## Packet

- Packet id / experiment code: `20-2-09`
- Experiment title: 钛(IV)盐的水解
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-2-09.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-2-09_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `5`
- Rewrite: `25`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_2_09_001`, `CHK5_SEM_EXP_20_2_09_003`, `CHK5_SEM_EXP_20_2_09_004`, `CHK5_SEM_EXP_20_2_09_005`, `CHK5_SEM_EXP_20_2_09_006`, `CHK5_SEM_EXP_20_2_09_007`, `CHK5_SEM_EXP_20_2_09_008`, `CHK5_SEM_EXP_20_2_09_009`, `CHK5_SEM_EXP_20_2_09_011`, `CHK5_SEM_EXP_20_2_09_013`, `CHK5_SEM_EXP_20_2_09_014`, `CHK5_SEM_EXP_20_2_09_015`, `CHK5_SEM_EXP_20_2_09_016`, `CHK5_SEM_EXP_20_2_09_017`, `CHK5_SEM_EXP_20_2_09_018`, `CHK5_SEM_EXP_20_2_09_019`, `CHK5_SEM_EXP_20_2_09_020`, `CHK5_SEM_EXP_20_2_09_021`, `CHK5_SEM_EXP_20_2_09_023`, `CHK5_SEM_EXP_20_2_09_024`, `CHK5_SEM_EXP_20_2_09_025`, `CHK5_SEM_EXP_20_2_09_026`, `CHK5_SEM_EXP_20_2_09_027`, `CHK5_SEM_EXP_20_2_09_028`, `CHK5_SEM_EXP_20_2_09_029`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_2_09_002`: kept because it asks the exact next operation after adding water; option diagnostics were rewritten.
- `CHK5_SEM_EXP_20_2_09_010`: kept as an operation-discrimination item because A/B/C are all canonical steps and D is clearly off-point.
- `CHK5_SEM_EXP_20_2_09_012`: kept as a direct true/false check of the core operation, with the explanation rewritten.
- `CHK5_SEM_EXP_20_2_09_022`: kept because `煮沸` is a short deterministic Chinese answer.
- `CHK5_SEM_EXP_20_2_09_030`: kept because the visible answer `蒸馏` is short and phone-safe; `蒸馏水` is hidden as a grading alias only.

## Evidence Insufficient

- None.

## Multi-Point Questions

- None. The packet has one video point, `candidate-1-5b0beabb` (`TiOSO₄ 稀释后加热煮沸`). Fe(III), Cr(III), Co/KSCN, and TiO²⁺/H₂O₂ contexts are used only as distractors or theory-scope contrasts, not as secondary point bindings.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_2_09_022` | `煮沸` | none | low | kept |
| `CHK5_SEM_EXP_20_2_09_025` | `稀释` | none | low | rewritten with theory audit |
| `CHK5_SEM_EXP_20_2_09_027` | `沉淀` | `水解产物` | low | rewritten from broader product fill |
| `CHK5_SEM_EXP_20_2_09_030` | `蒸馏` | `蒸馏水` | low | kept with visible answer narrowed |

No visible fill-blank answer requires typing `TiOSO₄`, `H₂TiO₃`, `TiO₂`, ions, equations, or formula aliases.

## RAG Evidence IDs Used

- Canonical experiment: `expchunk_00322_6c10a1661c`
- Supporting theory for TiOSO₄ hydrolysis to H₂TiO₃: `textbook_prose_01156_e3d54318a3`
- Supporting reaction evidence for TiOSO₄ hydrolysis: `textbook_prose_01157_702c31a997`

Rejected or excluded candidate ids:

- `textbook_prose_01179_863cead3f0`: TiO²⁺ / H₂O₂ color reaction; real RAG id but not the main evidence for this hydrolysis packet.
- Appendix TiO₂ thermodynamic table records: real but not canonical experiment evidence.
- Fe(III) and Cr(III) steps inside `expchunk_00322_6c10a1661c`: used only as neighbor distractor context, not as point bindings.

## Duplicate Resolution

The old packet had a repeated generic stem asking which statement about TiOSO₄ dilution/heating was correct. The rebuilt packet separates that cluster into operation sequence, adjacent Fe/Cr disambiguation, evidence-scope judgement, theory-id selection, product-theory dependency, point-key binding, mobile-fill rewrite strategy, and option-link diagnostic quality.

## Validation Notes

- JSON parse: passed.
- Question ids: unique.
- Single-choice answers: aligned with option labels.
- Option links: every single-choice option has one concrete semantic diagnostic.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `63`.
- Modified question_id list: `CHK5_SEM_EXP_20_2_09_001`, `CHK5_SEM_EXP_20_2_09_002`, `CHK5_SEM_EXP_20_2_09_003`, `CHK5_SEM_EXP_20_2_09_004`, `CHK5_SEM_EXP_20_2_09_005`, `CHK5_SEM_EXP_20_2_09_006`, `CHK5_SEM_EXP_20_2_09_007`, `CHK5_SEM_EXP_20_2_09_008`, `CHK5_SEM_EXP_20_2_09_009`, `CHK5_SEM_EXP_20_2_09_010`, `CHK5_SEM_EXP_20_2_09_011`, `CHK5_SEM_EXP_20_2_09_012`, `CHK5_SEM_EXP_20_2_09_013`, `CHK5_SEM_EXP_20_2_09_014`, `CHK5_SEM_EXP_20_2_09_015`, `CHK5_SEM_EXP_20_2_09_016`, `CHK5_SEM_EXP_20_2_09_018`, `CHK5_SEM_EXP_20_2_09_019`, `CHK5_SEM_EXP_20_2_09_020`, `CHK5_SEM_EXP_20_2_09_021`, `CHK5_SEM_EXP_20_2_09_022`, `CHK5_SEM_EXP_20_2_09_023`, `CHK5_SEM_EXP_20_2_09_024`, `CHK5_SEM_EXP_20_2_09_025`, `CHK5_SEM_EXP_20_2_09_026`, `CHK5_SEM_EXP_20_2_09_028`, `CHK5_SEM_EXP_20_2_09_029`, `CHK5_SEM_EXP_20_2_09_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
