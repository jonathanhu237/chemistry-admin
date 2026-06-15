# Rebuild Report: chunk_5 / 20-3-03

## Packet

- Packet id / experiment code: `20-3-03`
- Experiment title: Cr(Ⅲ) 的水合异构现象
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-03.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-03_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `22`
- Rewrite: `8`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_03_021`, `CHK5_SEM_EXP_20_3_03_022`, `CHK5_SEM_EXP_20_3_03_023`, `CHK5_SEM_EXP_20_3_03_025`, `CHK5_SEM_EXP_20_3_03_026`, `CHK5_SEM_EXP_20_3_03_028`, `CHK5_SEM_EXP_20_3_03_029`, `CHK5_SEM_EXP_20_3_03_030`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_3_03_001`-`010`: kept because the source items directly map to the canonical operation, observation, reversible equation, initial complex, product complex, entering nitrate ligand, and departing water ligand.
- `CHK5_SEM_EXP_20_3_03_011`-`020`: kept because the true/false items are all directly determined by the canonical procedure or equation and do not require unsupported theory.
- `CHK5_SEM_EXP_20_3_03_024`: kept because `颜色` is a short, deterministic, phone-safe fill answer and directly matches the observation target.
- `CHK5_SEM_EXP_20_3_03_027`: kept because `温度` is a short, deterministic, phone-safe fill answer and directly matches the heat/cold labels.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `CHK5_SEM_EXP_20_3_03_003`, `007`, `010`, `017`, `019`, `020`, `021`, `026`, `028`, and `029` bind both video points because they require connecting heating with before/after color comparison.
- Formula-only or reagent-only items bind the heating point; observation-only items bind the color-comparison point.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_03_024` | `颜色` | `颜色变化` | low | kept |
| `CHK5_SEM_EXP_20_3_03_027` | `温度` | `加热和冷却`, `热冷条件` | low | kept |

No visible fill-blank answer requires typing Cr(NO₃)₃, [Cr(H₂O)₆](NO₃)₃, [Cr(H₂O)₅NO₃](NO₃)₂, H₂O, NO₃⁻, or any other formula.

## RAG Evidence IDs Used

- Parent experiment protocol: `expchunk_protocol_4faa721af035`
- Canonical Cr(III) hydration isomerism procedure and equation: `expchunk_00331_3f7cc41ff9`
- Supporting chromium(Ⅲ) hydration-isomer color background: `textbook_prose_01215_9d0be2f325`

Rejected or excluded locator ids from the source packet:

- None required. The source packet had no additional supporting-theory hints; `textbook_prose_01215_9d0be2f325` was added manually because it directly explains Cr(III) water/ligand substitution and color differences.

## Duplicate Resolution

The source packet was mostly semantically aligned with canonical, but items 21-23, 25-26, and 28-30 repeated a generic shell. The rebuilt packet separates them into observation/explanation integration, invalid conclusion boundary, adjacent Co(II) experiment boundary, outer nitrate count, heat/cold direction, record completeness, inner-sphere ligand change, and oxidation-state boundary.

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
- Modified visible fields in this packet: `22`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_03_001`, `CHK5_SEM_EXP_20_3_03_002`, `CHK5_SEM_EXP_20_3_03_003`, `CHK5_SEM_EXP_20_3_03_004`, `CHK5_SEM_EXP_20_3_03_005`, `CHK5_SEM_EXP_20_3_03_007`, `CHK5_SEM_EXP_20_3_03_010`, `CHK5_SEM_EXP_20_3_03_011`, `CHK5_SEM_EXP_20_3_03_012`, `CHK5_SEM_EXP_20_3_03_013`, `CHK5_SEM_EXP_20_3_03_014`, `CHK5_SEM_EXP_20_3_03_015`, `CHK5_SEM_EXP_20_3_03_016`, `CHK5_SEM_EXP_20_3_03_018`, `CHK5_SEM_EXP_20_3_03_020`, `CHK5_SEM_EXP_20_3_03_021`, `CHK5_SEM_EXP_20_3_03_022`, `CHK5_SEM_EXP_20_3_03_024`, `CHK5_SEM_EXP_20_3_03_026`, `CHK5_SEM_EXP_20_3_03_028`, `CHK5_SEM_EXP_20_3_03_029`, `CHK5_SEM_EXP_20_3_03_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
