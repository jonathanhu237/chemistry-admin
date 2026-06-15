# Rebuild Report: chunk_5 / 20-3-14

## Packet

- Packet id / experiment code: `20-3-14`
- Experiment title: 小设计实验
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-14.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-14_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `16`
- Rewrite: `14`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_14_003`, `CHK5_SEM_EXP_20_3_14_007`, `CHK5_SEM_EXP_20_3_14_017`, `CHK5_SEM_EXP_20_3_14_019`, `CHK5_SEM_EXP_20_3_14_020`, `CHK5_SEM_EXP_20_3_14_021`, `CHK5_SEM_EXP_20_3_14_022`, `CHK5_SEM_EXP_20_3_14_023`, `CHK5_SEM_EXP_20_3_14_024`, `CHK5_SEM_EXP_20_3_14_025`, `CHK5_SEM_EXP_20_3_14_026`, `CHK5_SEM_EXP_20_3_14_027`, `CHK5_SEM_EXP_20_3_14_029`, `CHK5_SEM_EXP_20_3_14_030`

## Keep but Quality-Edge Review

- `CHK5_SEM_EXP_20_3_14_008`: kept because it follows directly from the canonical requirement to separately detect three ions, but it is a design-principle question rather than a single reagent fact.
- `CHK5_SEM_EXP_20_3_14_009` and `CHK5_SEM_EXP_20_3_14_016`: kept with supporting theory because both Fe³⁺ and Co²⁺ involve thiocyanate chemistry; Fe³⁺ interference/masking is explicitly supported by theory.
- `CHK5_SEM_EXP_20_3_14_028`: kept as a short fill blank. The visible accepted answers are Chinese words only.

## Evidence Insufficient

- None. The canonical small-design task establishes the three target ions; adjacent canonical identification procedures and supporting theory supply the reagent/phenomenon details needed for a deterministic design question.

## Multi-Point Questions

- None. This packet has a single video point, `candidate-1-de6f1130`, and every question is bound to that design point.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_14_028` | `弱`, `弱碱性` | `微碱性` | low | kept |

No visible fill answer requires typing a complex formula or coordination expression.

## Evidence Used

- Canonical small-design task: `expchunk_00335_1df34eedec`
- Adjacent Co²⁺ and Ni²⁺ identification procedures: `expchunk_00334_8229cac865`
- Fe³⁺ thiocyanate, Fe³⁺ masking, and Co²⁺ thiocyanate supporting theory: `textbook_prose_01304_9920c29f9d`
- Ni²⁺ dimethylglyoxime red precipitate supporting theory: `textbook_prose_01305_dd5a94da50`

Excluded inherited locators:

- Table-record locators for Fe/Co/Ni complexes were not needed after using the prose theory chunks, which state the same operationally relevant colors and identification uses in a more direct form.

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
