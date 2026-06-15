# Rebuild Report: chunk_5 / 20-3-05

## Packet

- Packet id / experiment code: `20-3-05`
- Experiment title: 氨合物
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-05.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-05_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `24`
- Rewrite: `6`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_05_018`, `CHK5_SEM_EXP_20_3_05_021`, `CHK5_SEM_EXP_20_3_05_022`, `CHK5_SEM_EXP_20_3_05_024`, `CHK5_SEM_EXP_20_3_05_025`, `CHK5_SEM_EXP_20_3_05_027`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_3_05_001`-`005`: kept because they directly identify canonical reagents, concentration, standing observation, NaOH follow-up, and target metal salts.
- `CHK5_SEM_EXP_20_3_05_006`-`010`: kept because theory supports Fe aqueous instability, Co air oxidation, Ni ammine formation, and the NaOH probe interpretation.
- `CHK5_SEM_EXP_20_3_05_011`-`017`, `019`, and `020`: kept because each true/false item is directly supported or contradicted by canonical and theory.
- `CHK5_SEM_EXP_20_3_05_023`, `026`, `028`, `029`, and `030`: kept because all fill answers are short Chinese phrases and avoid formula entry.

## Evidence Insufficient

- None.

## Multi-Point Questions

- The packet legitimately has many multi-point items because the experiment compares several metal salt solutions under the same NH₃·H₂O / standing / NaOH sequence.
- Single-metal theory questions bind to their corresponding metal point; global method questions bind to the standing or NaOH comparison point.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_05_023` | `后续变化`, `变化` | `继续变化`, `后续现象` | low | kept |
| `CHK5_SEM_EXP_20_3_05_026` | `氢氧化物` | `金属氢氧化物` | low | kept |
| `CHK5_SEM_EXP_20_3_05_028` | `氨合物` | `氨配合物` | low | kept |
| `CHK5_SEM_EXP_20_3_05_029` | `配合物`, `氨合物` | `氨配合物` | low | kept |
| `CHK5_SEM_EXP_20_3_05_030` | `氨合物` | `氨配合物` | low | kept |

No visible fill-blank answer requires typing NH₃·H₂O, Fe(OH)₂, Fe(OH)₃, [Co(NH₃)₆]²⁺, [Co(NH₃)₆]³⁺, [Ni(NH₃)₆]²⁺, or any other formula.

## RAG Evidence IDs Used

- Canonical氨合物 procedure: `expchunk_00332_42b6908ee0`
- Fe aqueous ammine instability and hydroxide formation: `textbook_prose_01291_3bfd5ed23b`, `textbook_prose_01292_6a2d2ec117`, `textbook_table_record_table_p224_t01_r071`
- Co(Ⅱ) ammine formation and air oxidation to Co(Ⅲ): `textbook_prose_01292_6a2d2ec117`, `textbook_prose_01293_827d3c2d20`, `textbook_table_record_table_p224_t01_r051`, `textbook_table_record_table_p224_t01_r081`
- Ni(Ⅱ) ammine formation and stability: `textbook_prose_01293_827d3c2d20`

Rejected or excluded locator ids from the source packet:

- `textbook_prose_01305_dd5a94da50`: nickel dimethylglyoxime context, useful for Ni identification but not needed for this氨合物 comparison packet.

## Duplicate Resolution

The source packet repeated a generic “金属离子与 NH₃·H₂O 形成氨合物的比较” shell across later items. The rebuilt packet separates this into Fe aqueous-instability, Co sequence and air oxidation, Ni sequence and stability, NaOH probe purpose, standing observation, and mobile-safe short fill blanks.

## Validation Notes

- JSON parse: passed.
- Question ids: passed.
- Single-choice answers: passed.
- Option links: passed.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed after replacing student-visible hydroxide formulas with Chinese names and exposing fill-blank accepted answers at top level.
- Release JSON direct edit: no `chunk_5_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `30`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_05_001`, `CHK5_SEM_EXP_20_3_05_002`, `CHK5_SEM_EXP_20_3_05_003`, `CHK5_SEM_EXP_20_3_05_004`, `CHK5_SEM_EXP_20_3_05_005`, `CHK5_SEM_EXP_20_3_05_006`, `CHK5_SEM_EXP_20_3_05_007`, `CHK5_SEM_EXP_20_3_05_008`, `CHK5_SEM_EXP_20_3_05_009`, `CHK5_SEM_EXP_20_3_05_010`, `CHK5_SEM_EXP_20_3_05_011`, `CHK5_SEM_EXP_20_3_05_012`, `CHK5_SEM_EXP_20_3_05_013`, `CHK5_SEM_EXP_20_3_05_014`, `CHK5_SEM_EXP_20_3_05_015`, `CHK5_SEM_EXP_20_3_05_017`, `CHK5_SEM_EXP_20_3_05_018`, `CHK5_SEM_EXP_20_3_05_019`, `CHK5_SEM_EXP_20_3_05_020`, `CHK5_SEM_EXP_20_3_05_021`, `CHK5_SEM_EXP_20_3_05_022`, `CHK5_SEM_EXP_20_3_05_023`, `CHK5_SEM_EXP_20_3_05_024`, `CHK5_SEM_EXP_20_3_05_025`, `CHK5_SEM_EXP_20_3_05_026`, `CHK5_SEM_EXP_20_3_05_027`, `CHK5_SEM_EXP_20_3_05_028`, `CHK5_SEM_EXP_20_3_05_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
