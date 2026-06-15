# Rebuild Report: chunk_5 / 20-3-08

## Packet

- Packet id / experiment code: `20-3-08`
- Experiment title: 铁的鉴定
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-08.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-08_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `18`
- Rewrite: `12`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_08_006`, `CHK5_SEM_EXP_20_3_08_007`, `CHK5_SEM_EXP_20_3_08_014`, `CHK5_SEM_EXP_20_3_08_017`, `CHK5_SEM_EXP_20_3_08_019`, `CHK5_SEM_EXP_20_3_08_020`, `CHK5_SEM_EXP_20_3_08_021`, `CHK5_SEM_EXP_20_3_08_022`, `CHK5_SEM_EXP_20_3_08_023`, `CHK5_SEM_EXP_20_3_08_026`, `CHK5_SEM_EXP_20_3_08_027`, `CHK5_SEM_EXP_20_3_08_029`

## Evidence Insufficient

- None after rewriting noisy generic template questions and the visible `Ni(dmg)₂` distractor wording.

## Evidence Used

- Canonical experiment purpose and iron identification scope: `expchunk_00327_e59c162b54`, `expchunk_00334_8229cac865`
- Fe(Ⅲ) / thiocyanate blood-red identification: `textbook_prose_01304_9920c29f9d`, `textbook_table_record_table_p224_t01_r071`
- Fe(Ⅱ) / ferricyanide blue precipitate: `textbook_prose_01296_e1b954e16b`, `textbook_prose_01297_b761f39d9a`
- Fe(Ⅱ) oxidation risk: `textbook_prose_01156_e3d54318a3`

Excluded inherited locators:

- Co/Ni table rows and metal-ion identification chunks not directly used for iron claims, except as out-of-scope distractor context when needed.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_3_08_024` | `蓝色`, `蓝` | `滕氏蓝`, `蓝色的滕氏蓝` | low | kept |
| `CHK5_SEM_EXP_20_3_08_025` | `氧化` | `氧化成`, `氧化为` | low | kept |
| `CHK5_SEM_EXP_20_3_08_028` | `价态` | `氧化态` | low | kept |
| `CHK5_SEM_EXP_20_3_08_030` | `配合` | `配位`, `配合物` | low | kept |

No visible fill answer requires typing Fe(Ⅱ), Fe(Ⅲ), KSCN, ferricyanide formulas, or nested coordination formulas.

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
- Modified visible fields in this packet: `10`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_08_001`, `CHK5_SEM_EXP_20_3_08_002`, `CHK5_SEM_EXP_20_3_08_004`, `CHK5_SEM_EXP_20_3_08_006`, `CHK5_SEM_EXP_20_3_08_011`, `CHK5_SEM_EXP_20_3_08_013`, `CHK5_SEM_EXP_20_3_08_017`, `CHK5_SEM_EXP_20_3_08_021`, `CHK5_SEM_EXP_20_3_08_024`, `CHK5_SEM_EXP_20_3_08_027`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
