# Rebuild Report: chunk_5 / 20-3-01

## Packet

- Packet id / experiment code: `20-3-01`
- Experiment title: 水合阳离子颜色
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-01.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-01_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `13`
- Rewrite: `17`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_01_002`, `CHK5_SEM_EXP_20_3_01_005`, `CHK5_SEM_EXP_20_3_01_006`, `CHK5_SEM_EXP_20_3_01_008`, `CHK5_SEM_EXP_20_3_01_015`, `CHK5_SEM_EXP_20_3_01_018`, `CHK5_SEM_EXP_20_3_01_020`, `CHK5_SEM_EXP_20_3_01_021`, `CHK5_SEM_EXP_20_3_01_022`, `CHK5_SEM_EXP_20_3_01_023`, `CHK5_SEM_EXP_20_3_01_024`, `CHK5_SEM_EXP_20_3_01_025`, `CHK5_SEM_EXP_20_3_01_026`, `CHK5_SEM_EXP_20_3_01_027`, `CHK5_SEM_EXP_20_3_01_028`, `CHK5_SEM_EXP_20_3_01_029`, `CHK5_SEM_EXP_20_3_01_030`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_3_01_001`: kept because it directly distinguishes a listed water hydrated cation from the separately listed anions.
- `CHK5_SEM_EXP_20_3_01_003`: kept because [Co(H₂O)₆]²⁺ pink is supported by both the hydrated-ion color table and cobalt complex table.
- `CHK5_SEM_EXP_20_3_01_004`: kept because [Ni(H₂O)₆]²⁺ green is supported by both the hydrated-ion color table and nickel complex table.
- `CHK5_SEM_EXP_20_3_01_007`: kept because the Cr(III) hydrated-complex color claim is supported by the chromium complex prose, with anion color confusion removed.
- `CHK5_SEM_EXP_20_3_01_009`: kept because it directly restates the canonical experiment purpose.
- `CHK5_SEM_EXP_20_3_01_010`: kept because it is a valid list-scope discrimination question.
- `CHK5_SEM_EXP_20_3_01_011`: kept because the listed Ti/Cr hydrated cations are directly present in canonical.
- `CHK5_SEM_EXP_20_3_01_012`: kept because CrO₄²⁻ is explicitly outside the hydrated-cation list.
- `CHK5_SEM_EXP_20_3_01_013`: kept because the Co color statement is table-supported.
- `CHK5_SEM_EXP_20_3_01_014`: kept because the Ni color statement is table-supported.
- `CHK5_SEM_EXP_20_3_01_016`: kept as a false statement because table 20.5 supports Mn²⁺ as flesh color rather than deep black.
- `CHK5_SEM_EXP_20_3_01_017`: kept because it maps directly to the experiment purpose and transition-metal color theory.
- `CHK5_SEM_EXP_20_3_01_019`: kept because it cleanly rejects the wrong halogen/CCl₄ experiment context.

## Evidence Insufficient

- None in the rebuilt packet.
- The old Ti color question was not kept as a color question because the reviewed RAG evidence for this packet directly supports Ti membership and charge, but not a specific Ti hydrated-cation color with the same confidence as Co, Ni, Fe, Mn, and Cr.

## Multi-Point Questions

- `CHK5_SEM_EXP_20_3_01_002`, `009`, `017`, and `021` deliberately bind multiple water hydrated cation point keys because they test list-level recording or experiment-purpose understanding rather than one ion color.
- Single-ion color questions bind to the corresponding ion point only.

## Fill-Blank Mobile Risk

- None. This rebuilt packet uses only single-choice and true/false items.
- Former formula-reading fill blanks were converted to single-choice items to avoid mobile formula or element-symbol input.

## RAG Evidence IDs Used

- Experiment purpose and canonical list: `expchunk_00327_e59c162b54`, `expchunk_00330_3a60414cf4`
- General color theory and anion color boundary: `textbook_prose_01118_9e2eabedd8`, `textbook_prose_01119_8478df1f7f`
- Hydrated ion color table context: `textbook_table_context_p196_3d43037f75`
- Table 20.5 colors: `textbook_table_record_table_p196_t01_r011`, `textbook_table_record_table_p196_t01_r031`, `textbook_table_record_table_p196_t01_r041`, `textbook_table_record_table_p196_t01_r051`
- Cr(III) hydrated complex color support: `textbook_prose_01215_9d0be2f325`
- Co/Ni complex table support: `textbook_table_record_table_p224_t01_r051`, `textbook_table_record_table_p224_t01_r061`

Rejected or excluded locator ids from the source packet:

- `textbook_prose_01305_dd5a94da50`: cobalt/nickel complex chemistry context, but not needed for this packet's direct hydrated-cation color questions beyond the more precise table records.
- Any inherited locator that only asserted generic d-block chemistry without supporting the specific color, category, or purpose tested by the final question.

## Duplicate Resolution

The source packet repeated a generic “which statement is correct” shell across items 21-30. The rebuilt packet separates this into color theory, anion/cation category boundaries, Mn/Fe/Co/Ni table pairings, Fe color correction, evidence sufficiency for Ni, overgeneralization feedback, Ti membership without unsupported color, and phone-safe formula reading.

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
- Modified visible fields in this packet: `15`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_01_002`, `CHK5_SEM_EXP_20_3_01_005`, `CHK5_SEM_EXP_20_3_01_007`, `CHK5_SEM_EXP_20_3_01_008`, `CHK5_SEM_EXP_20_3_01_010`, `CHK5_SEM_EXP_20_3_01_011`, `CHK5_SEM_EXP_20_3_01_015`, `CHK5_SEM_EXP_20_3_01_018`, `CHK5_SEM_EXP_20_3_01_020`, `CHK5_SEM_EXP_20_3_01_021`, `CHK5_SEM_EXP_20_3_01_022`, `CHK5_SEM_EXP_20_3_01_025`, `CHK5_SEM_EXP_20_3_01_026`, `CHK5_SEM_EXP_20_3_01_027`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
