# chunk_3 Evidence-First Final Report

Status: evidence-first closeout complete for chunk 3 only. Student-facing effective questions were retained; release JSON was updated with evidence-first metadata/review-state only.

## Scope

- Release JSON: `chunk_3_release_final_v1.json`
- Manual log: `manual_semantic_rereview_logs/chunk_3_manual_semantic_rereview_log.md`
- Experiment range: `19-6-02` through `20-1-01`
- OpenSpec task range referenced by prompt: `5.1` through `5.16`; no OpenSpec files were modified.
- Evidence sources: effective release JSON, `chunk_3_reviewed_v1.json`, `chunk_3_semantic_final_v1.json`, `release_input_freeze_v1/chunk_3_polished_final_v1.json`, `prompts/chunk_3_review_prompt.md`, formal experiment video points, canonical experiment refs in `formal_experiment_point_inventory.json`, `DOC_EXPERIMENTS_SELECTED.json`, `database_seed.json`, and broader RAG canonical chunk ids for cross-chapter theory references.

## Summary

- Active questions: 450
- keep/rewrite/reject: 401/49/0
- Types: single_choice 164, true_false 153, fill_blank 133
- Evidence sufficient final: 450/450
- Questions using supporting theory: 368
- Multi-point effective questions: 174
- Evidence-first student-facing repairs in this pass: 0

## Per-Experiment Completion

| experiment_code | title | active | keep | rewrite | single_choice | true_false | fill_blank | supporting_theory_qs | multi_point_qs | status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 19-6-02 | 金属镁燃烧 | 30 | 28 | 2 | 11 | 10 | 9 | 9 | 4 | complete |
| 19-6-03 | 与水的作用 | 30 | 27 | 3 | 10 | 10 | 10 | 20 | 14 | complete |
| 19-6-04 | 焰色反应 | 30 | 28 | 2 | 10 | 10 | 10 | 30 | 14 | complete |
| 19-8-01 | Pb(OH)₂ 的生成与性质 | 30 | 26 | 4 | 10 | 11 | 9 | 0 | 12 | complete |
| 19-8-02 | Sn(OH)₂ 的生成与性质 | 30 | 28 | 2 | 11 | 10 | 9 | 30 | 13 | complete |
| 19-8-03 | Sb(OH)₃ 的生成与性质 | 30 | 27 | 3 | 12 | 10 | 8 | 30 | 14 | complete |
| 19-8-04 | Bi(OH)₃ 的生成与性质 | 30 | 25 | 5 | 11 | 11 | 8 | 30 | 11 | complete |
| 19-8-05 | Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性 | 30 | 28 | 2 | 10 | 10 | 10 | 30 | 7 | complete |
| 19-8-06 | Sn(II) 的还原性 | 30 | 27 | 3 | 11 | 10 | 9 | 26 | 7 | complete |
| 19-8-07 | Pb(IV) 的氧化性 | 30 | 29 | 1 | 11 | 10 | 9 | 30 | 17 | complete |
| 19-8-08 | As(III)、Sb(III)、Bi(III) 的还原性 | 30 | 27 | 3 | 12 | 10 | 8 | 30 | 15 | complete |
| 19-8-09 | As(V)、Sb(V)、Bi(V) 的氧化性 | 30 | 26 | 4 | 11 | 10 | 9 | 30 | 12 | complete |
| 19-8-10 | Sn、Pb、Bi 不同价态离子的氧化还原性 | 30 | 27 | 3 | 11 | 10 | 9 | 26 | 3 | complete |
| 19-8-11 | 小设计实验 | 30 | 20 | 10 | 12 | 11 | 7 | 27 | 8 | complete |
| 20-1-01 | 氢氧化物的生成与性质 | 30 | 28 | 2 | 11 | 10 | 9 | 20 | 23 | complete |

## Modified Questions

- No stem/options/answer/explanation/point-binding edits were required during this evidence-first pass.
- JSON modifications were evidence-first metadata/review-state only: `metadata.evidence_first_final`, `metadata.release_final.evidence_first_*`, and per-question `release_final_review.evidence_first_*`.
- The 49 effective rewrite questions from the release final pass were reread and retained as the active effective versions; no new rewrite/reject decisions were introduced.

## Retained Keep/Rewrite Rationale

- Keep items were retained where the effective original question is supported by the listed canonical experiment chunk(s), formal video point(s), and optional theory ids in `source_audit`.
- Rewrite items were retained where the proposed/effective question is the safer, clearer version already present in the release and has `evidence_sufficient=true`.
- Low-depth items marked `reviewed_and_retained` were kept when they anchor a necessary reagent, operation, color, product, or observation term and are deterministic for mobile grading or single-choice/true-false display.

## Evidence Insufficient Items

| count | question_ids | action |
|---:|---|---|
| 0 | none | no reject or new rewrite needed |

## Supporting Theory Usage

| experiment_code | supporting_theory_question_count | theory_chunk_ids_used | reason |
|---|---:|---|---|
| 19-6-02 | 9 | textbook_table_record_table_p158_t01_r011 | property/color/product/acid-base/redox inference beyond procedure text |
| 19-6-03 | 20 | textbook_prose_00936_0b5113eb41 | property/color/product/acid-base/redox inference beyond procedure text |
| 19-6-04 | 30 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-01 | 0 | none | not needed; canonical procedure/point evidence sufficient |
| 19-8-02 | 30 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-03 | 30 | textbook_prose_00596_462a4c7dff | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-04 | 30 | textbook_prose_00596_462a4c7dff | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-05 | 30 | textbook_prose_00596_462a4c7dff, textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-06 | 26 | textbook_prose_00773_a0b6644822, textbook_prose_00774_e51e8911a2, textbook_prose_01090_56461596a1, textbook_prose_01304_9920c29f9d | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-07 | 30 | textbook_prose_00757_85fc20341a, textbook_prose_00758_5f5fd037a3, textbook_prose_00784_dec216b401, textbook_prose_01241_99049758ad | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-08 | 30 | textbook_prose_00596_462a4c7dff, textbook_prose_00597_06f7e56f06 | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-09 | 30 | textbook_prose_00597_06f7e56f06, textbook_prose_00598_cadca448de, textbook_prose_01241_99049758ad | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-10 | 26 | textbook_prose_00597_06f7e56f06, textbook_prose_00598_cadca448de, textbook_prose_00758_5f5fd037a3, textbook_prose_01090_56461596a1, textbook_prose_01241_99049758ad | property/color/product/acid-base/redox inference beyond procedure text |
| 19-8-11 | 27 | textbook_prose_00379_033ea5b92b, textbook_prose_00756_b42e11e0c6, textbook_prose_00757_85fc20341a, textbook_prose_00788_cfbfaab4bc | property/color/product/acid-base/redox inference beyond procedure text |
| 20-1-01 | 20 | textbook_prose_01042_cb5178e401, textbook_prose_01057_8ebcc2ce77, textbook_prose_01079_0f2609f8ca, textbook_prose_01087_3a6c1c97ff | property/color/product/acid-base/redox inference beyond procedure text |

## Multi-Point Effective Questions

| experiment_code | count | question_ids | reason |
|---|---:|---|---|
| 19-6-02 | 4 | OLD_CHUNK3_EXP_19_6_02_Q001, OLD_CHUNK3_EXP_19_6_02_Q011, OLD_CHUNK3_EXP_19_6_02_Q021, OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-6-03 | 14 | OLD_CHUNK3_EXP_19_6_03_Q003, OLD_CHUNK3_EXP_19_6_03_Q005, OLD_CHUNK3_EXP_19_6_03_Q007, OLD_CHUNK3_EXP_19_6_03_Q009, OLD_CHUNK3_EXP_19_6_03_Q010, OLD_CHUNK3_EXP_19_6_03_Q013, OLD_CHUNK3_EXP_19_6_03_Q016, OLD_CHUNK3_EXP_19_6_03_Q017_R1, OLD_CHUNK3_EXP_19_6_03_Q018, OLD_CHUNK3_EXP_19_6_03_Q019_R1, OLD_CHUNK3_EXP_19_6_03_Q020_R1, OLD_CHUNK3_EXP_19_6_03_Q025, OLD_CHUNK3_EXP_19_6_03_Q026, OLD_CHUNK3_EXP_19_6_03_Q030 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-6-04 | 14 | OLD_CHUNK3_EXP_19_6_04_Q001, OLD_CHUNK3_EXP_19_6_04_Q002, OLD_CHUNK3_EXP_19_6_04_Q009, OLD_CHUNK3_EXP_19_6_04_Q010, OLD_CHUNK3_EXP_19_6_04_Q011, OLD_CHUNK3_EXP_19_6_04_Q015, OLD_CHUNK3_EXP_19_6_04_Q016, OLD_CHUNK3_EXP_19_6_04_Q017, OLD_CHUNK3_EXP_19_6_04_Q018_R1, OLD_CHUNK3_EXP_19_6_04_Q020_R1, OLD_CHUNK3_EXP_19_6_04_Q021, OLD_CHUNK3_EXP_19_6_04_Q022, OLD_CHUNK3_EXP_19_6_04_Q029, OLD_CHUNK3_EXP_19_6_04_Q030 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-01 | 12 | OLD_CHUNK3_EXP_19_8_01_Q002_R1, OLD_CHUNK3_EXP_19_8_01_Q003, OLD_CHUNK3_EXP_19_8_01_Q004, OLD_CHUNK3_EXP_19_8_01_Q008, OLD_CHUNK3_EXP_19_8_01_Q012, OLD_CHUNK3_EXP_19_8_01_Q013, OLD_CHUNK3_EXP_19_8_01_Q014_SF1, OLD_CHUNK3_EXP_19_8_01_Q016, OLD_CHUNK3_EXP_19_8_01_Q020, OLD_CHUNK3_EXP_19_8_01_Q023, OLD_CHUNK3_EXP_19_8_01_Q024, OLD_CHUNK3_EXP_19_8_01_Q030_R1_PF1 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-02 | 13 | OLD_CHUNK3_EXP_19_8_02_Q005, OLD_CHUNK3_EXP_19_8_02_Q006, OLD_CHUNK3_EXP_19_8_02_Q008, OLD_CHUNK3_EXP_19_8_02_Q009, OLD_CHUNK3_EXP_19_8_02_Q010, OLD_CHUNK3_EXP_19_8_02_Q015, OLD_CHUNK3_EXP_19_8_02_Q017, OLD_CHUNK3_EXP_19_8_02_Q018, OLD_CHUNK3_EXP_19_8_02_Q019, OLD_CHUNK3_EXP_19_8_02_Q020_SF1, OLD_CHUNK3_EXP_19_8_02_Q022_PF1, OLD_CHUNK3_EXP_19_8_02_Q025, OLD_CHUNK3_EXP_19_8_02_Q028 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-03 | 14 | OLD_CHUNK3_EXP_19_8_03_Q005, OLD_CHUNK3_EXP_19_8_03_Q006, OLD_CHUNK3_EXP_19_8_03_Q007, OLD_CHUNK3_EXP_19_8_03_Q008, OLD_CHUNK3_EXP_19_8_03_Q010, OLD_CHUNK3_EXP_19_8_03_Q015, OLD_CHUNK3_EXP_19_8_03_Q016, OLD_CHUNK3_EXP_19_8_03_Q017, OLD_CHUNK3_EXP_19_8_03_Q018, OLD_CHUNK3_EXP_19_8_03_Q023_PF1, OLD_CHUNK3_EXP_19_8_03_Q025, OLD_CHUNK3_EXP_19_8_03_Q026, OLD_CHUNK3_EXP_19_8_03_Q027, OLD_CHUNK3_EXP_19_8_03_Q028 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-04 | 11 | OLD_CHUNK3_EXP_19_8_04_Q005, OLD_CHUNK3_EXP_19_8_04_Q006, OLD_CHUNK3_EXP_19_8_04_Q007, OLD_CHUNK3_EXP_19_8_04_Q010, OLD_CHUNK3_EXP_19_8_04_Q013, OLD_CHUNK3_EXP_19_8_04_Q014, OLD_CHUNK3_EXP_19_8_04_Q015, OLD_CHUNK3_EXP_19_8_04_Q024_SF1, OLD_CHUNK3_EXP_19_8_04_Q027, OLD_CHUNK3_EXP_19_8_04_Q029, OLD_CHUNK3_EXP_19_8_04_Q030_PF1 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-05 | 7 | OLD_CHUNK3_EXP_19_8_05_Q010, OLD_CHUNK3_EXP_19_8_05_Q015, OLD_CHUNK3_EXP_19_8_05_Q016, OLD_CHUNK3_EXP_19_8_05_Q018_R1, OLD_CHUNK3_EXP_19_8_05_Q019_R1, OLD_CHUNK3_EXP_19_8_05_Q020, OLD_CHUNK3_EXP_19_8_05_Q030 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-06 | 7 | OLD_CHUNK3_EXP_19_8_06_Q009, OLD_CHUNK3_EXP_19_8_06_Q010, OLD_CHUNK3_EXP_19_8_06_Q017_R1, OLD_CHUNK3_EXP_19_8_06_Q019_R1, OLD_CHUNK3_EXP_19_8_06_Q020, OLD_CHUNK3_EXP_19_8_06_Q025_PF1, OLD_CHUNK3_EXP_19_8_06_Q028 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-07 | 17 | OLD_CHUNK3_EXP_19_8_07_Q001, OLD_CHUNK3_EXP_19_8_07_Q002, OLD_CHUNK3_EXP_19_8_07_Q003, OLD_CHUNK3_EXP_19_8_07_Q004, OLD_CHUNK3_EXP_19_8_07_Q005, OLD_CHUNK3_EXP_19_8_07_Q009, OLD_CHUNK3_EXP_19_8_07_Q010, OLD_CHUNK3_EXP_19_8_07_Q011, OLD_CHUNK3_EXP_19_8_07_Q013, OLD_CHUNK3_EXP_19_8_07_Q016, OLD_CHUNK3_EXP_19_8_07_Q017, OLD_CHUNK3_EXP_19_8_07_Q018, OLD_CHUNK3_EXP_19_8_07_Q021, OLD_CHUNK3_EXP_19_8_07_Q022, OLD_CHUNK3_EXP_19_8_07_Q023, OLD_CHUNK3_EXP_19_8_07_Q024_PF1, OLD_CHUNK3_EXP_19_8_07_Q028 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-08 | 15 | OLD_CHUNK3_EXP_19_8_08_Q001, OLD_CHUNK3_EXP_19_8_08_Q003, OLD_CHUNK3_EXP_19_8_08_Q004, OLD_CHUNK3_EXP_19_8_08_Q005, OLD_CHUNK3_EXP_19_8_08_Q010, OLD_CHUNK3_EXP_19_8_08_Q011, OLD_CHUNK3_EXP_19_8_08_Q013, OLD_CHUNK3_EXP_19_8_08_Q014, OLD_CHUNK3_EXP_19_8_08_Q015, OLD_CHUNK3_EXP_19_8_08_Q020, OLD_CHUNK3_EXP_19_8_08_Q021_R1, OLD_CHUNK3_EXP_19_8_08_Q023, OLD_CHUNK3_EXP_19_8_08_Q024, OLD_CHUNK3_EXP_19_8_08_Q025_PF1, OLD_CHUNK3_EXP_19_8_08_Q030 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-09 | 12 | OLD_CHUNK3_EXP_19_8_09_Q001, OLD_CHUNK3_EXP_19_8_09_Q007, OLD_CHUNK3_EXP_19_8_09_Q009, OLD_CHUNK3_EXP_19_8_09_Q010, OLD_CHUNK3_EXP_19_8_09_Q011, OLD_CHUNK3_EXP_19_8_09_Q013, OLD_CHUNK3_EXP_19_8_09_Q017_R1, OLD_CHUNK3_EXP_19_8_09_Q018, OLD_CHUNK3_EXP_19_8_09_Q020_R1, OLD_CHUNK3_EXP_19_8_09_Q021, OLD_CHUNK3_EXP_19_8_09_Q024, OLD_CHUNK3_EXP_19_8_09_Q027 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-10 | 3 | OLD_CHUNK3_EXP_19_8_10_Q010, OLD_CHUNK3_EXP_19_8_10_Q020, OLD_CHUNK3_EXP_19_8_10_Q030 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 19-8-11 | 8 | OLD_CHUNK3_EXP_19_8_11_Q006_R1, OLD_CHUNK3_EXP_19_8_11_Q007_R1_PF1, OLD_CHUNK3_EXP_19_8_11_Q009, OLD_CHUNK3_EXP_19_8_11_Q010_SF1, OLD_CHUNK3_EXP_19_8_11_Q015_R1, OLD_CHUNK3_EXP_19_8_11_Q019_R1_PF1, OLD_CHUNK3_EXP_19_8_11_Q020_R1_PF1, OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | effective stem spans an operation chain, comparison, or multi-step evidence relation |
| 20-1-01 | 23 | OLD_CHUNK3_EXP_20_1_01_Q001, OLD_CHUNK3_EXP_20_1_01_Q002, OLD_CHUNK3_EXP_20_1_01_Q003, OLD_CHUNK3_EXP_20_1_01_Q004, OLD_CHUNK3_EXP_20_1_01_Q005, OLD_CHUNK3_EXP_20_1_01_Q006, OLD_CHUNK3_EXP_20_1_01_Q007, OLD_CHUNK3_EXP_20_1_01_Q008, OLD_CHUNK3_EXP_20_1_01_Q009, OLD_CHUNK3_EXP_20_1_01_Q010_SF1, OLD_CHUNK3_EXP_20_1_01_Q011, OLD_CHUNK3_EXP_20_1_01_Q012, OLD_CHUNK3_EXP_20_1_01_Q013, OLD_CHUNK3_EXP_20_1_01_Q014, OLD_CHUNK3_EXP_20_1_01_Q015, OLD_CHUNK3_EXP_20_1_01_Q016, OLD_CHUNK3_EXP_20_1_01_Q018, OLD_CHUNK3_EXP_20_1_01_Q021, OLD_CHUNK3_EXP_20_1_01_Q022, OLD_CHUNK3_EXP_20_1_01_Q023, OLD_CHUNK3_EXP_20_1_01_Q024_PF1, OLD_CHUNK3_EXP_20_1_01_Q026, OLD_CHUNK3_EXP_20_1_01_Q030 | effective stem spans an operation chain, comparison, or multi-step evidence relation |

## Fill-Blank Mobile Handling

| experiment_code | fill_blank_count | question_ids | status |
|---|---:|---|---|
| 19-6-02 | 9 | OLD_CHUNK3_EXP_19_6_02_Q021, OLD_CHUNK3_EXP_19_6_02_Q022, OLD_CHUNK3_EXP_19_6_02_Q023, OLD_CHUNK3_EXP_19_6_02_Q024, OLD_CHUNK3_EXP_19_6_02_Q025, OLD_CHUNK3_EXP_19_6_02_Q027, OLD_CHUNK3_EXP_19_6_02_Q028, OLD_CHUNK3_EXP_19_6_02_Q029, OLD_CHUNK3_EXP_19_6_02_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-6-03 | 10 | OLD_CHUNK3_EXP_19_6_03_Q021, OLD_CHUNK3_EXP_19_6_03_Q022, OLD_CHUNK3_EXP_19_6_03_Q023, OLD_CHUNK3_EXP_19_6_03_Q024, OLD_CHUNK3_EXP_19_6_03_Q025, OLD_CHUNK3_EXP_19_6_03_Q026, OLD_CHUNK3_EXP_19_6_03_Q027, OLD_CHUNK3_EXP_19_6_03_Q028, OLD_CHUNK3_EXP_19_6_03_Q029, OLD_CHUNK3_EXP_19_6_03_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-6-04 | 10 | OLD_CHUNK3_EXP_19_6_04_Q021, OLD_CHUNK3_EXP_19_6_04_Q022, OLD_CHUNK3_EXP_19_6_04_Q023, OLD_CHUNK3_EXP_19_6_04_Q024, OLD_CHUNK3_EXP_19_6_04_Q025, OLD_CHUNK3_EXP_19_6_04_Q026, OLD_CHUNK3_EXP_19_6_04_Q027, OLD_CHUNK3_EXP_19_6_04_Q028, OLD_CHUNK3_EXP_19_6_04_Q029, OLD_CHUNK3_EXP_19_6_04_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-01 | 9 | OLD_CHUNK3_EXP_19_8_01_Q021, OLD_CHUNK3_EXP_19_8_01_Q022, OLD_CHUNK3_EXP_19_8_01_Q023, OLD_CHUNK3_EXP_19_8_01_Q024, OLD_CHUNK3_EXP_19_8_01_Q025, OLD_CHUNK3_EXP_19_8_01_Q026, OLD_CHUNK3_EXP_19_8_01_Q027, OLD_CHUNK3_EXP_19_8_01_Q028, OLD_CHUNK3_EXP_19_8_01_Q029 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-02 | 9 | OLD_CHUNK3_EXP_19_8_02_Q021, OLD_CHUNK3_EXP_19_8_02_Q023, OLD_CHUNK3_EXP_19_8_02_Q024, OLD_CHUNK3_EXP_19_8_02_Q025, OLD_CHUNK3_EXP_19_8_02_Q026, OLD_CHUNK3_EXP_19_8_02_Q027, OLD_CHUNK3_EXP_19_8_02_Q028, OLD_CHUNK3_EXP_19_8_02_Q029, OLD_CHUNK3_EXP_19_8_02_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-03 | 8 | OLD_CHUNK3_EXP_19_8_03_Q021, OLD_CHUNK3_EXP_19_8_03_Q022, OLD_CHUNK3_EXP_19_8_03_Q024, OLD_CHUNK3_EXP_19_8_03_Q025, OLD_CHUNK3_EXP_19_8_03_Q026, OLD_CHUNK3_EXP_19_8_03_Q027, OLD_CHUNK3_EXP_19_8_03_Q028, OLD_CHUNK3_EXP_19_8_03_Q029 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-04 | 8 | OLD_CHUNK3_EXP_19_8_04_Q021, OLD_CHUNK3_EXP_19_8_04_Q022, OLD_CHUNK3_EXP_19_8_04_Q023, OLD_CHUNK3_EXP_19_8_04_Q025, OLD_CHUNK3_EXP_19_8_04_Q026, OLD_CHUNK3_EXP_19_8_04_Q027, OLD_CHUNK3_EXP_19_8_04_Q028, OLD_CHUNK3_EXP_19_8_04_Q029 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-05 | 10 | OLD_CHUNK3_EXP_19_8_05_Q021, OLD_CHUNK3_EXP_19_8_05_Q022, OLD_CHUNK3_EXP_19_8_05_Q023, OLD_CHUNK3_EXP_19_8_05_Q024, OLD_CHUNK3_EXP_19_8_05_Q025, OLD_CHUNK3_EXP_19_8_05_Q026, OLD_CHUNK3_EXP_19_8_05_Q027, OLD_CHUNK3_EXP_19_8_05_Q028, OLD_CHUNK3_EXP_19_8_05_Q029, OLD_CHUNK3_EXP_19_8_05_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-06 | 9 | OLD_CHUNK3_EXP_19_8_06_Q021, OLD_CHUNK3_EXP_19_8_06_Q022, OLD_CHUNK3_EXP_19_8_06_Q023, OLD_CHUNK3_EXP_19_8_06_Q024, OLD_CHUNK3_EXP_19_8_06_Q026, OLD_CHUNK3_EXP_19_8_06_Q027, OLD_CHUNK3_EXP_19_8_06_Q028, OLD_CHUNK3_EXP_19_8_06_Q029, OLD_CHUNK3_EXP_19_8_06_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-07 | 9 | OLD_CHUNK3_EXP_19_8_07_Q021, OLD_CHUNK3_EXP_19_8_07_Q022, OLD_CHUNK3_EXP_19_8_07_Q023, OLD_CHUNK3_EXP_19_8_07_Q025, OLD_CHUNK3_EXP_19_8_07_Q026, OLD_CHUNK3_EXP_19_8_07_Q027, OLD_CHUNK3_EXP_19_8_07_Q028, OLD_CHUNK3_EXP_19_8_07_Q029, OLD_CHUNK3_EXP_19_8_07_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-08 | 8 | OLD_CHUNK3_EXP_19_8_08_Q022, OLD_CHUNK3_EXP_19_8_08_Q023, OLD_CHUNK3_EXP_19_8_08_Q024, OLD_CHUNK3_EXP_19_8_08_Q026, OLD_CHUNK3_EXP_19_8_08_Q027, OLD_CHUNK3_EXP_19_8_08_Q028, OLD_CHUNK3_EXP_19_8_08_Q029, OLD_CHUNK3_EXP_19_8_08_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-09 | 9 | OLD_CHUNK3_EXP_19_8_09_Q021, OLD_CHUNK3_EXP_19_8_09_Q022, OLD_CHUNK3_EXP_19_8_09_Q023, OLD_CHUNK3_EXP_19_8_09_Q024, OLD_CHUNK3_EXP_19_8_09_Q025, OLD_CHUNK3_EXP_19_8_09_Q026, OLD_CHUNK3_EXP_19_8_09_Q027, OLD_CHUNK3_EXP_19_8_09_Q029, OLD_CHUNK3_EXP_19_8_09_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-10 | 9 | OLD_CHUNK3_EXP_19_8_10_Q021, OLD_CHUNK3_EXP_19_8_10_Q022, OLD_CHUNK3_EXP_19_8_10_Q023, OLD_CHUNK3_EXP_19_8_10_Q024, OLD_CHUNK3_EXP_19_8_10_Q025, OLD_CHUNK3_EXP_19_8_10_Q026, OLD_CHUNK3_EXP_19_8_10_Q028, OLD_CHUNK3_EXP_19_8_10_Q029, OLD_CHUNK3_EXP_19_8_10_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 19-8-11 | 7 | OLD_CHUNK3_EXP_19_8_11_Q021, OLD_CHUNK3_EXP_19_8_11_Q022, OLD_CHUNK3_EXP_19_8_11_Q023, OLD_CHUNK3_EXP_19_8_11_Q024, OLD_CHUNK3_EXP_19_8_11_Q025, OLD_CHUNK3_EXP_19_8_11_Q029, OLD_CHUNK3_EXP_19_8_11_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |
| 20-1-01 | 9 | OLD_CHUNK3_EXP_20_1_01_Q021, OLD_CHUNK3_EXP_20_1_01_Q022, OLD_CHUNK3_EXP_20_1_01_Q023, OLD_CHUNK3_EXP_20_1_01_Q025, OLD_CHUNK3_EXP_20_1_01_Q026, OLD_CHUNK3_EXP_20_1_01_Q027, OLD_CHUNK3_EXP_20_1_01_Q028, OLD_CHUNK3_EXP_20_1_01_Q029, OLD_CHUNK3_EXP_20_1_01_Q030 | mobile-safe: short accepted answers or Chinese aliases; no formula-chain/equation fill blank retained |

## Option-Link Status

- Single-choice questions checked: 164
- Option-link label/text mismatches: 0
- English/generic diagnostic note hits: 0
- New option-link fixes in this pass: 0. Existing option links were retained after label/text/diagnostic checks.

## JSON Parse And Validation

- active_questions: 450
- missing_effective_explanations: 0
- generic_effective_explanations: 0
- evidence_sufficient_false: 0
- empty_canonical_audits: 0
- canonical_id_misses_against_formal_inventory: 0
- supporting_theory_id_misses_against_inventory_or_rag: 0
- invalid_point_keys: 0
- single_choice_option_link_mismatches: 0
- english_generic_option_link_notes: 0
- ascii_digit_formula_display_hits: 0
- duplicate_effective_stems: 0
- UTF-8 JSON parse after write: passed.

## Final Confirmation

Chunk 3 has been completed under the evidence-first standard. The review covered every active effective question exactly once in the manual log and did not use sampling as a substitute for full review. Other chunks and OpenSpec task files were not modified. This report does not assert that chunks 1-5 as a whole can enter the bank; it only closes the scoped chunk 3 evidence-first review.
