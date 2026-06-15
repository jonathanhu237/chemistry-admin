# chunk_1-5 Student-Visible Release Gate Report

## Scope

- Target rebuilt packages:
  - `rebuilt_packages/chunk_1`
  - `rebuilt_packages/chunk_2`
  - `rebuilt_packages/chunk_3`
  - `rebuilt_packages/chunk_4`
  - `rebuilt_packages/chunk_5`
- Evidence sources:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Release-final files were not used as write targets in this pass. Current git status already shows `chunk_X_release_final_v1.json` as modified in the broader worktree, so those existing differences should be treated as pre-existing state, not as this report's edited output.

## Release Gate Rule Used

This pass fixes only student-visible P0/P1 blockers:

- student-visible review/process wording such as `考查`, `题干`, `该题`, `判分`, `要求学生`, `观察任务`
- student-visible raw/internal ids
- student-visible ASCII chemistry display such as `ClO-`, `锰(II)`, `+3`, `+6`
- wrong or unsupported answers
- non-deterministic grading or mobile-hostile visible fill blanks

Metadata-only issues are recorded but not blocking in this gate:

- `option_links[].diagnostic_note` missing or inconsistent
- `option_links` schema style differences
- `source_audit.supporting_theory_required=true` with empty `supporting_theory_chunk_ids`
- normal textbook experiment titles such as `《20-2-09 钛(Ⅳ)盐的水解》`

## Edited Student-Visible Items

| chunk | file | question ids | visible issue fixed |
|---|---|---|---|
| chunk_1 | `19-1-05_rebuilt_v1.json` | `CHUNK1_19_1_05_Q015`, `CHUNK1_19_1_05_Q025` | `锰(II)` -> `锰(Ⅱ)` |
| chunk_1 | `19-2-05_rebuilt_v1.json` | `CHUNK1_19_2_05_Q028` | removed visible `确定判分` wording |
| chunk_1 | `19-3-02_rebuilt_v1.json` | `CHUNK1_19_3_02_Q006` | changed meta `主要考查什么` to a chemistry property question |
| chunk_2 | `19-3-03_rebuilt_v1.json` | `IDEAL_CH2_19_3_03_Q009`, `Q016`, `Q018` | removed `该空` / `该题` and display-risk commentary |
| chunk_2 | `19-4-04_rebuilt_v1.json` | `REBUILT_CH2_19_4_04_Q029`, `Q030` | changed `KI-CCl₄` to `KI 与 CCl₄ 形成的紫色层` |
| chunk_2 | `19-4-07_rebuilt_v1.json` | `REBUILT_CH2_19_4_07_Q021` | removed `该空` wording |
| chunk_3 | `19-6-02_rebuilt_v1.json` | `REBUILT_CH3_19_6_02_Q009`, `Q023`, `Q028` | removed `要求学生` / `考查` phrasing |
| chunk_3 | `19-6-03_rebuilt_v1.json` | `REBUILT_CH3_19_6_03_Q012`, `Q028`, `Q029` | removed `该题` / `考查` / complex-input commentary |
| chunk_3 | `19-6-04_rebuilt_v1.json` | `REBUILT_CH3_19_6_04_Q008` | removed `该题` phrasing |
| chunk_3 | `19-8-01_rebuilt_v1.json` | `REBUILT_CH3_19_8_01_Q003`, `Q004`, `Q006`, `Q009`, `Q014`, `Q015`, `Q029` | removed review/process wording and `R-O-H`; rewrote one meta item into a normal experiment relation question |
| chunk_3 | `19-8-02_rebuilt_v1.json` | `REBUILT_CH3_19_8_02_Q007`, `Q008`, `Q030` | removed `本题`; replaced `R-O-H` wording |
| chunk_3 | `19-8-03_rebuilt_v1.json` | `REBUILT_CH3_19_8_03_Q005`, `Q010`, `Q014`, `Q030` | removed `本题` / numeric-fill avoidance language / `R-O-H` |
| chunk_3 | `19-8-04_rebuilt_v1.json` | `REBUILT_CH3_19_8_04_Q006`, `Q026` | removed `该题` / `该空考查` |
| chunk_3 | `19-8-05_rebuilt_v1.json` | `REBUILT_CH3_19_8_05_Q001`, `Q006`, `Q007`, `Q021` | removed `本题` / `考查目标`; rewrote as normal observation focus |
| chunk_3 | `19-8-06_rebuilt_v1.json` | `REBUILT_CH3_19_8_06_Q009`, `Q030` | removed `本题` / `性质考查` |
| chunk_3 | `19-8-08_rebuilt_v1.json` | `REBUILT_CH3_19_8_08_Q030` | removed `本题` / input-avoidance wording |
| chunk_3 | `19-8-09_rebuilt_v1.json` | `REBUILT_CH3_19_8_09_Q015` | rewrote `一道题...最适合考查` as direct教材步骤判断 |
| chunk_4 | `20-1-02_rebuilt_v1.json` | `REV_CH4_EXP_20_1_02_Q008`, `Q015`, `Q018`, `Q024` | changed `观察任务` to `观察内容`; removed `不要求学生输入` |
| chunk_4 | `20-1-04_rebuilt_v1.json` | `REV_CH4_EXP_20_1_04_Q016`, `Q026` | changed `观察任务` and `只考` phrasing |
| chunk_4 | `20-1-05_rebuilt_v1.json` | `REV_CH4_EXP_20_1_05_Q015`, `Q016` | changed `观察任务` to `观察内容` |
| chunk_4 | `20-1-07_rebuilt_v1.json` | `REV_CH4_EXP_20_1_07_Q022` | removed `确定判分` |
| chunk_4 | `20-1-08_rebuilt_v1.json` | `REV_CH4_EXP_20_1_08_Q022` | removed `不要求学生输入` |
| chunk_4 | `20-1-09_rebuilt_v1.json` | `REV_CH4_EXP_20_1_09_Q012` | removed visible `要求学生` |
| chunk_4 | `20-2-07_rebuilt_v1.json` | `REV_CH4_EXP_20_2_07_Q014`, `Q016` | changed `观察任务` to `观察内容` |
| chunk_5 | `20-2-08_rebuilt_v1.json` | `CHK5_SEM_EXP_20_2_08_002`, `Q017`, `Q021`, `Q024`, `Q029` | changed `观察任务`; removed `考查`; changed `+3` to `三价` |
| chunk_5 | `20-3-01_rebuilt_v1.json` | `CHK5_SEM_EXP_20_3_01_008` | removed visible `考查` |
| chunk_5 | `20-3-02_rebuilt_v1.json` | `CHK5_SEM_EXP_20_3_02_028` | removed visible `考查` |
| chunk_5 | `20-3-05_rebuilt_v1.json` | `CHK5_SEM_EXP_20_3_05_023` | changed `观察任务` to `观察内容` |
| chunk_5 | `20-3-11_rebuilt_v1.json` | `CHK5_SEM_EXP_20_3_11_020`, `Q030` | changed `+3`, `+6`, `-1` to Chinese valence wording |
| chunk_5 | `20-3-12_rebuilt_v1.json` | `CHK5_SEM_EXP_20_3_12_009`, `CHK5_SEM_EXP_20_3_12_027` | changed `+1/+2/+4/+5/0` option display to Chinese valence wording |
| chunk_5 | `20-3-13_rebuilt_v1.json` | `CHK5_SEM_EXP_20_3_13_007` | changed `考查哪一因素` to normal cause/effect wording |

Note: earlier verified closeout fixes in the same goal already covered `CHUNK1_19_1_05_Q017`, `CHUNK1_19_1_07_Q009`, and several chunk_3 evidence-review wording residues. The final scanner below covers the current state after those fixes and this pass.

## Cross-Audit FAIL Classification

| chunk | cross-audit result | final classification |
|---|---|---|
| chunk_1 | `CHUNK1_19_1_05_Q017` review language and `ClO-`; `CHUNK1_19_1_07_Q009` display issue; option-link diagnostic wording | `student_visible_blocker_to_fix` for visible fields, now fixed. Option-link diagnostics are `metadata_backlog_not_blocking_publish`. |
| chunk_2 | no sampled P0/P1; option-link missing/diagnostic style issues | `metadata_backlog_not_blocking_publish`. Visible fields now also pass strict scan. |
| chunk_3 | multiple visible evidence-review phrases such as `考查`, `问法`, `该题`, `确定判分`, `要求学生` | `student_visible_blocker_to_fix`, now fixed in visible fields. Low-depth purpose/module questions remain retainable. |
| chunk_4 | 22 questions with `supporting_theory_required=true` and empty theory ids | `metadata_backlog_not_blocking_publish` for this gate. No student-visible evidence failure found by the final scan/structure gate. |
| chunk_5 | textbook title codes flagged as raw ids; null option-link diagnostics; visible signed oxidation numbers | textbook title codes are `false_positive_or_allowed`; null diagnostics are `metadata_backlog_not_blocking_publish`; signed oxidation display was `student_visible_blocker_to_fix`, now fixed. |

## Validation Results

| gate | result |
|---|---:|
| rebuilt JSON files parsed | 77 |
| total questions | 2310 |
| chunk_1 count | 15 files / 450 questions |
| chunk_2 count | 15 files / 450 questions |
| chunk_3 count | 15 files / 450 questions |
| chunk_4 count | 15 files / 450 questions |
| chunk_5 count | 17 files / 510 questions |
| JSON parse / packet count / chunk count errors | 0 |
| duplicate `question_id` | 0 |
| single-choice answer/options/option_links structural errors | 0 |
| missing explanations | 0 |
| `source_audit.evidence_sufficient=false` | 0 |
| RAG evidence ids missing from the two JSONL sources | 0 |
| student-visible review/internal/raw-id/display hits | 0 |
| fill_blank visible formula/symbol answer risks | 0 |

## Metadata Backlog

These are not fixed in this student-visible gate and should be handled in a later metadata-normalization pass if downstream tooling needs them.

| metadata issue | count |
|---|---:|
| questions with at least one missing/empty `option_links[].diagnostic_note` | 484 |
| missing/empty `option_links[].diagnostic_note` entries | 1880 |
| questions using `reason` style instead of `diagnostic_note` style | 104 |
| questions with internal wording inside option-link diagnostics | 127 |
| questions with `supporting_theory_required=true` and empty theory ids | 22 |

## Final Decision

`PASS_FOR_STUDENT_VISIBLE_MERGE_CANDIDATE`

The current rebuilt chunk_1-5 packages pass the student-visible release gate: no visible review/process wording, no visible raw/internal ids, no visible ASCII formula/charge/Roman-valence/signed-oxidation display hits, no structural answer errors, no missing explanations, no missing RAG evidence ids, and no `evidence_insufficient` publish rows.

This is not a claim that metadata is perfect. It is a scoped publish gate decision: the remaining known issues are metadata backlog, not student-facing blockers under this round's rules.
