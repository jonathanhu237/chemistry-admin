# Rebuild Report: chunk_5 / 20-2-08

## Packet

- Packet id / experiment code: `20-2-08`
- Experiment title: 铬(III)盐的水解
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-2-08.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-2-08_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `5`
- Rewrite: `25`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_2_08_001`, `CHK5_SEM_EXP_20_2_08_002`, `CHK5_SEM_EXP_20_2_08_004`, `CHK5_SEM_EXP_20_2_08_005`, `CHK5_SEM_EXP_20_2_08_006`, `CHK5_SEM_EXP_20_2_08_007`, `CHK5_SEM_EXP_20_2_08_008`, `CHK5_SEM_EXP_20_2_08_009`, `CHK5_SEM_EXP_20_2_08_010`, `CHK5_SEM_EXP_20_2_08_011`, `CHK5_SEM_EXP_20_2_08_012`, `CHK5_SEM_EXP_20_2_08_014`, `CHK5_SEM_EXP_20_2_08_015`, `CHK5_SEM_EXP_20_2_08_016`, `CHK5_SEM_EXP_20_2_08_017`, `CHK5_SEM_EXP_20_2_08_018`, `CHK5_SEM_EXP_20_2_08_019`, `CHK5_SEM_EXP_20_2_08_020`, `CHK5_SEM_EXP_20_2_08_021`, `CHK5_SEM_EXP_20_2_08_022`, `CHK5_SEM_EXP_20_2_08_024`, `CHK5_SEM_EXP_20_2_08_025`, `CHK5_SEM_EXP_20_2_08_027`, `CHK5_SEM_EXP_20_2_08_028`, `CHK5_SEM_EXP_20_2_08_029`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_2_08_003`: kept as a low-threshold concept classification item because it is directly supported by the RAG section title “金属离子的水解作用”; retained as one basic anchor, not repeated.
- `CHK5_SEM_EXP_20_2_08_013`: kept as a direct true/false operation check because it exactly matches `Cr₂(SO₄)₃ + Na₂CO₃`; explanation and audit were rewritten.
- `CHK5_SEM_EXP_20_2_08_023`: kept because the visible answer is the short Chinese word `水解`, deterministic and phone-safe.
- `CHK5_SEM_EXP_20_2_08_026`: kept because the visible answer is the short Chinese word `观察`, directly supported by canonical text and phone-safe.
- `CHK5_SEM_EXP_20_2_08_030`: kept as a short answer item, but the audit now explicitly marks theory dependency for the precipitate inference.

## Evidence Insufficient

- None.

## Multi-Point Questions

- None. The packet has one video point, `candidate-1-376fa2cd` (`Cr₂(SO₄)₃ + Na₂CO₃`). Neighbor Fe(III), Ti(IV), and NaOH content is used only as distractor context or evidence-scope contrast, not as secondary point binding.

## Fill-Blank Mobile Risk

| question_id | visible answer | risk | action |
|---|---|---|---|
| `CHK5_SEM_EXP_20_2_08_023` | `水解` | low | kept |
| `CHK5_SEM_EXP_20_2_08_026` | `观察` | low | kept |
| `CHK5_SEM_EXP_20_2_08_030` | `水解` | low | kept with theory audit |

No visible fill-blank answer requires typing `Cr₂(SO₄)₃`, `Na₂CO₃`, `Cr(OH)₃`, ions, equations, or aliases.

## RAG Evidence IDs Used

- Canonical experiment: `expchunk_00322_6c10a1661c`
- Neighbor canonical context only: `expchunk_00319_b995aa9123`
- Supporting theory for Cr³⁺ hydrolysis: `textbook_table_record_table_p284_t01_r261`
- Supporting theory for Cr(OH)₃ sparingly soluble precipitate: `textbook_table_record_table_p285_t02_r092`

Rejected inherited theory ids:

- `textbook_prose_00293_6e62d1272e`: hydrogen peroxide oxidation-reduction; not needed for this packet.
- `textbook_prose_01118_9e2eabedd8`: transition-metal ion color theory; not needed for final questions.
- `textbook_prose_01119_8478df1f7f`: CrO₄²⁻ color / charge-transfer discussion; explicitly treated as off-point for this packet.

## Duplicate Resolution

The old packet had a large repeated stem cluster asking essentially the same “which statement is correct about Cr₂(SO₄)₃ and Na₂CO₃” question. The rebuilt packet splits that cluster into distinct tasks: operation identification, procedure completeness, adjacent Fe/Ti step disambiguation, evidence-scope judgement, point-key binding, mobile-fill rewrite strategy, option-link quality, and theory-id selection.

## Validation Notes

- JSON parse: passed.
- Question count: pass, `30`.
- Type count: `21` single choice, `6` true/false, `3` fill blank.
- Question ids: pass, unique.
- Single-choice answers: pass, each answer label exists in options.
- Option links: pass, every single-choice option has one concrete semantic diagnostic.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed.
- Fill-blank formula answers: pass, all visible accepted answers are short Chinese words.
- Evidence insufficient publishable items: pass, none.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `56`.
- Modified question_id list: `CHK5_SEM_EXP_20_2_08_001`, `CHK5_SEM_EXP_20_2_08_002`, `CHK5_SEM_EXP_20_2_08_003`, `CHK5_SEM_EXP_20_2_08_005`, `CHK5_SEM_EXP_20_2_08_006`, `CHK5_SEM_EXP_20_2_08_007`, `CHK5_SEM_EXP_20_2_08_008`, `CHK5_SEM_EXP_20_2_08_009`, `CHK5_SEM_EXP_20_2_08_010`, `CHK5_SEM_EXP_20_2_08_011`, `CHK5_SEM_EXP_20_2_08_012`, `CHK5_SEM_EXP_20_2_08_013`, `CHK5_SEM_EXP_20_2_08_014`, `CHK5_SEM_EXP_20_2_08_015`, `CHK5_SEM_EXP_20_2_08_016`, `CHK5_SEM_EXP_20_2_08_018`, `CHK5_SEM_EXP_20_2_08_019`, `CHK5_SEM_EXP_20_2_08_020`, `CHK5_SEM_EXP_20_2_08_022`, `CHK5_SEM_EXP_20_2_08_025`, `CHK5_SEM_EXP_20_2_08_026`, `CHK5_SEM_EXP_20_2_08_027`, `CHK5_SEM_EXP_20_2_08_028`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
