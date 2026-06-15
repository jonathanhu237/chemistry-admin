# Rebuild Report: chunk_5 / 20-3-13

## Packet

- Packet id / experiment code: `20-3-13`
- Experiment title: 钒(Ⅴ)的鉴定
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-13.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-13_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `14`
- Rewrite: `16`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_13_001`, `CHK5_SEM_EXP_20_3_13_006`, `CHK5_SEM_EXP_20_3_13_008`, `CHK5_SEM_EXP_20_3_13_011`, `CHK5_SEM_EXP_20_3_13_016`, `CHK5_SEM_EXP_20_3_13_017`, `CHK5_SEM_EXP_20_3_13_018`, `CHK5_SEM_EXP_20_3_13_021`, `CHK5_SEM_EXP_20_3_13_022`, `CHK5_SEM_EXP_20_3_13_023`, `CHK5_SEM_EXP_20_3_13_024`, `CHK5_SEM_EXP_20_3_13_026`, `CHK5_SEM_EXP_20_3_13_027`, `CHK5_SEM_EXP_20_3_13_028`, `CHK5_SEM_EXP_20_3_13_029`, `CHK5_SEM_EXP_20_3_13_030`

## Keep but Quality-Edge Review

- `CHK5_SEM_EXP_20_3_13_025`: kept as fill blank because the visible accepted answer is the short Chinese term `过氧钒`; complex formula aliases were not exposed.
- Several reagent identity items were kept because they are directly supported by the canonical operation and use concrete distractors, but their scope remains intentionally narrow.

## Evidence Insufficient

- None. All published questions are supported by the canonical experiment protocol and the metal-ion identification chunk.

## Multi-Point Questions

| question_id | point keys | reason |
|---|---|---|
| `CHK5_SEM_EXP_20_3_13_001` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | asks target valence for the acidified NH₄VO₃ plus H₂O₂ route |
| `CHK5_SEM_EXP_20_3_13_006` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | tests the ordered acidification and peroxide-addition workflow |
| `CHK5_SEM_EXP_20_3_13_009` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | asks the sequence from acidification to peroxide addition |
| `CHK5_SEM_EXP_20_3_13_011` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | judgment spans acidification and peroxide reagent |
| `CHK5_SEM_EXP_20_3_13_013` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | asks acidification before peroxide addition |
| `CHK5_SEM_EXP_20_3_13_016` | `candidate-2-4b1d96d3`, `candidate-3-de4dbb09` | connects color criterion with the H₂O₂ amount comparison |
| `CHK5_SEM_EXP_20_3_13_019` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | validates sequence across both steps |
| `CHK5_SEM_EXP_20_3_13_021` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | combines vanadium source, acid, and peroxide reagent |
| `CHK5_SEM_EXP_20_3_13_022` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | asks the handling after acidification and before peroxide addition |
| `CHK5_SEM_EXP_20_3_13_023` | `candidate-2-4b1d96d3`, `candidate-3-de4dbb09` | uses the optional extra H₂O₂ drop and amount effect |
| `CHK5_SEM_EXP_20_3_13_024` | `candidate-2-4b1d96d3`, `candidate-3-de4dbb09` | distinguishes valid peroxide route and amount comparison from a wrong replacement |
| `CHK5_SEM_EXP_20_3_13_026` | `candidate-3-de4dbb09`, `candidate-2-4b1d96d3` | excess H₂O₂ color belongs to the amount comparison after peroxide addition |
| `CHK5_SEM_EXP_20_3_13_029` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | tests workflow error against acidification plus peroxide addition |
| `CHK5_SEM_EXP_20_3_13_030` | `candidate-1-9b93a689`, `candidate-2-4b1d96d3` | asks the directly supported conclusion from acidified NH₄VO₃ and H₂O₂ |

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_13_025` | `过氧钒` | `含钒过氧`, `过氧钒配合物` | low | kept |

No visible fill answer requires typing a nested coordination formula.

## Evidence Used

- Canonical protocol parent: `expchunk_protocol_4faa721af035`
- Canonical vanadium(Ⅴ) identification operation, reaction, and H₂O₂ amount color comparison: `expchunk_00334_8229cac865`

Excluded inherited locators:

- No supporting theory chunks were needed. Neighboring metal-ion identification reactions in the same canonical chunk were used only as distractor context where the question explicitly contrasted them with the vanadium route.

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
- Modified visible fields in this packet: `1`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_13_029`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
