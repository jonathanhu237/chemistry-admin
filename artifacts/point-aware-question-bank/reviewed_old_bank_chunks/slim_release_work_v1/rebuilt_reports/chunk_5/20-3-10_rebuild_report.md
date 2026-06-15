# Rebuild Report: chunk_5 / 20-3-10

## Packet

- Packet id / experiment code: `20-3-10`
- Experiment title: 镍(Ⅱ)的鉴定
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-10.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-10_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `17`
- Rewrite: `13`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_10_006`, `CHK5_SEM_EXP_20_3_10_008`, `CHK5_SEM_EXP_20_3_10_012`, `CHK5_SEM_EXP_20_3_10_018`, `CHK5_SEM_EXP_20_3_10_020`, `CHK5_SEM_EXP_20_3_10_021`, `CHK5_SEM_EXP_20_3_10_022`, `CHK5_SEM_EXP_20_3_10_023`, `CHK5_SEM_EXP_20_3_10_024`, `CHK5_SEM_EXP_20_3_10_026`, `CHK5_SEM_EXP_20_3_10_028`, `CHK5_SEM_EXP_20_3_10_029`, `CHK5_SEM_EXP_20_3_10_030`

## Evidence Insufficient

- None after rewriting generic template questions and replacing student-visible nickel-dimethylglyoxime formulas with Chinese precipitate names.

## Evidence Used

- Canonical nickel identification operation and experiment reaction: `expchunk_00334_8229cac865`
- Bright-red dimethylglyoxime nickel precipitate and use for Ni²⁺ identification: `textbook_prose_01305_dd5a94da50`
- Supporting dimethylglyoxime reaction equation: `textbook_prose_01306_0a0d67a34e`

Excluded inherited locators:

- Co, Fe, Cr, Ti, and V identification content from the same canonical chunk was used only as distractor context where directly supported.
- Table rows about cobalt and iron complexes were not needed for nickel claims.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_10_025` | `鲜红色`, `红色` | `鲜红` | low | kept |
| `CHK5_SEM_EXP_20_3_10_027` | `丁二酮肟` | `二甲基乙二肟`, `HDMG` | low | kept |

No visible fill answer requires typing `Ni(dmg)₂` or a nested coordination formula.

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
- Modified visible fields in this packet: `11`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_10_001`, `CHK5_SEM_EXP_20_3_10_002`, `CHK5_SEM_EXP_20_3_10_004`, `CHK5_SEM_EXP_20_3_10_007`, `CHK5_SEM_EXP_20_3_10_009`, `CHK5_SEM_EXP_20_3_10_011`, `CHK5_SEM_EXP_20_3_10_013`, `CHK5_SEM_EXP_20_3_10_015`, `CHK5_SEM_EXP_20_3_10_024`, `CHK5_SEM_EXP_20_3_10_027`, `CHK5_SEM_EXP_20_3_10_028`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
