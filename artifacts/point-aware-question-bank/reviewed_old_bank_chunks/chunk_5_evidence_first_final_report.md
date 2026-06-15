# chunk 5 Evidence-First Final Report

Status: directly publishable after evidence-first full pass.

## Scope And Sources

- Release JSON: `E:/chemistry-admin/artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_5_release_final_v1.json`
- Manual log: `E:/chemistry-admin/artifacts/point-aware-question-bank/reviewed_old_bank_chunks/manual_semantic_rereview_logs/chunk_5_manual_semantic_rereview_log.md`
- Formal experiment points: `E:/chemistry-admin/artifacts/point-aware-question-bank/formal_experiment_point_inventory.json` and `E:/chemistry-exam/data/seed/formal_experiments.json`
- Canonical experiment text: `DOC_CANONICAL_EXPERIMENT_V1` refs recorded in the point inventory; supporting theory ids are from `database_seed.json` source chunks.
- Active scope: `20-2-08` through `20-3-14`; OpenSpec task scope `7.1` through `7.18`; no other chunks or OpenSpec tasks were modified.

## Summary

| metric | value |
| --- | --- |
| active questions | 510 |
| keep/rewrite/reject | 316/194/0 |
| effective types | single_choice=322, true_false=153, fill_blank=35 |
| final evidence-insufficient | 0 |
| supporting theory dependent | 203 |
| multi-point questions | 113 |
| fill-blank mobile risk | 0 |
| single-choice option-link anomalies after validation | 0 |
| active generic stems repaired in this pass | 167 |
| template option-link diagnostics repaired in this pass | 1245 |

## Experiment Evidence Status

| experiment_code | title | questions | keep/rewrite/reject | video_points | canonical_refs | theory_deps | multi_point | fill_blank | generic_stems_repaired | final_insufficient |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20-2-08 | 铬(III)盐的水解 | 30 | 12/18/0 | candidate-1-376fa2cd=Cr₂(SO₄)₃ + Na₂CO₃ | expchunk_00319_b995aa9123 p164, expchunk_00322_6c10a1661c p165 | 1 | 0 | 3 | 17 | 0 |
| 20-2-09 | 钛(IV)盐的水解 | 30 | 15/15/0 | candidate-1-5b0beabb=TiOSO₄ 稀释后加热煮沸 | expchunk_00322_6c10a1661c p165 | 7 | 0 | 4 | 13 | 0 |
| 20-2-10 | 小设计实验 | 30 | 21/9/0 | candidate-1-121e9e71=含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离检出 | expchunk_00319_b995aa9123 p164, expchunk_00321_53b9414bde p165, expchunk_00323_56549b57c0 p165 | 30 | 0 | 4 | 7 | 0 |
| 20-3-01 | 水合阳离子颜色 | 30 | 17/13/0 | candidate-1-e0d18274=`[Ti(H₂O)₆]³⁺`, candidate-2-1d49d35b=`[Cr(H₂O)₆]³⁺`, candidate-3-99dd6b35=`[Mn(H₂O)₆]²⁺`, candidate-4-3926ad6c=`[Fe(H₂O)₆]²⁺`, candidate-5-a4376972=`[Co(H₂O)₆]²⁺`, candidate-6-c0cbece1=`[Ni(H₂O)₆]²⁺` | expchunk_00327_e59c162b54 p166, expchunk_00330_3a60414cf4 p166 | 20 | 11 | 0 | 10 | 0 |
| 20-3-02 | 阴离子颜色 | 30 | 16/14/0 | candidate-1-6c3245f9=CrO₄²⁻, candidate-2-5db23da9=Cr₂O₇²⁻, candidate-3-f81ca373=MnO₄⁻, candidate-4-095a2458=MnO₄²⁻, candidate-5-ca04bf5e=MoO₄²⁻, candidate-6-d074e740=WO₄²⁻, candidate-7-b5d923bb=VO₃⁻ | expchunk_00330_3a60414cf4 p166 | 9 | 12 | 0 | 14 | 0 |
| 20-3-03 | Cr(III) 的水合异构现象 | 30 | 22/8/0 | candidate-1-80cf72b8=加热 Cr(NO₃)₃ 溶液, candidate-2-9d1424ba=比较加热前后溶液颜色 | expchunk_protocol_4faa721af035 p166, expchunk_00331_3f7cc41ff9 p166 | 0 | 13 | 2 | 8 | 0 |
| 20-3-04 | 观察不同配体的 Co(II) 配合物的颜色 | 30 | 16/14/0 | candidate-1-2059a278=CoCl₂ + KSCN 生成蓝紫色配合物, candidate-2-5eaed5b5=原溶液作为对照, candidate-3-c47ca8d9=加水后的颜色变化, candidate-4-e1fb1262=加丙酮后的颜色变化 | expchunk_00331_3f7cc41ff9 p166 | 17 | 10 | 0 | 11 | 0 |
| 20-3-05 | 氨合物 | 30 | 23/7/0 | candidate-1-a21fffae=Cr₂(SO₄)₃ + NH₃·H₂O, candidate-2-01f186e4=MnSO₄ + NH₃·H₂O, candidate-3-50abfa44=FeCl₃ + NH₃·H₂O, candidate-4-351f37ad=(NH₄)₂Fe(SO₄)₂ + NH₃·H₂O, candidate-5-947eed90=CoCl₂ + NH₃·H₂O, candidate-6-c08dc9eb=NiSO₄ + NH₃·H₂O, candidate-7-4a58a252=静置一段时间后观察变化, candidate-8-38d3ba33=继续加入 NaOH，比较形成氨合物能力 | expchunk_00332_42b6908ee0 p166 | 8 | 20 | 5 | 5 | 0 |
| 20-3-06 | 配合物的形成对氧化还原性的影响 | 30 | 20/10/0 | candidate-1-81b774c1=KI + CCl₄ + FeCl₃, candidate-2-a5f9b5b1=KI + CCl₄ + NaF + FeCl₃，对比 NaF 配位 Fe³⁺ 后反应差异, candidate-3-01fbe9ee=Fe(II) 溶液 + AgNO₃, candidate-4-2650ce4f=Fe(II) 溶液 + EDTA + AgNO₃ | expchunk_00332_42b6908ee0 p166, expchunk_00336_68bde523f4 p167 | 24 | 7 | 3 | 7 | 0 |
| 20-3-07 | 配合物稳定性与配体的关系 | 30 | 22/8/0 | candidate-1-d78b3d70=Cr₂(SO₄)₃ + Na₂C₂O₄，再加入 NaOH, candidate-2-627e8ed0=FeCl₃ + KSCN，再加入 Na₂C₂O₄, candidate-3-7d9492a7=NiSO₄ + 过量 NH₃·H₂O，再加入乙二胺 | expchunk_00332_42b6908ee0 p166, expchunk_00333_d08e49be44 p167 | 11 | 6 | 3 | 8 | 0 |
| 20-3-08 | 铁的鉴定 | 30 | 21/9/0 | candidate-1-19f29b28=Fe(II) 的鉴定, candidate-2-d3d9277b=Fe(III) 的鉴定 | expchunk_00327_e59c162b54 p166, expchunk_00334_8229cac865 p167 | 9 | 11 | 4 | 9 | 0 |
| 20-3-09 | 钴(II)的鉴定 | 30 | 15/15/0 | candidate-1-8ec6df4e=CoCl₂ + 戊醇 / 丙酮 + 饱和 KSCN | expchunk_00331_3f7cc41ff9 p166, expchunk_00334_8229cac865 p167 | 13 | 0 | 0 | 12 | 0 |
| 20-3-10 | 镍(II)的鉴定 | 30 | 20/10/0 | candidate-1-8de46ba4=NiSO₄ + NH₃·H₂O 调至弱碱性, candidate-2-18c41387=加入丁二酮肟，鉴定 Ni²⁺ | expchunk_00334_8229cac865 p167 | 13 | 4 | 2 | 8 | 0 |
| 20-3-11 | 铬(III)的鉴定 | 30 | 18/12/0 | candidate-1-193ad1c0=Cr₂(SO₄)₃ + 过量 NaOH, candidate-2-1a398c1b=加 H₂O₂ 并微热生成黄色铬酸盐, candidate-3-5d1daef7=用 H₂SO₄ 酸化, candidate-4-f71d0da2=加乙醚 / 戊醇, candidate-5-1777b5af=继续加入 H₂O₂，观察有机层深蓝色 | expchunk_00334_8229cac865 p167 | 11 | 7 | 2 | 9 | 0 |
| 20-3-12 | 钛(IV)的鉴定 | 30 | 21/9/0 | candidate-1-862feb96=TiOSO₄ + H₂O₂, candidate-2-c01f7a7b=再加入 NH₃·H₂O | expchunk_00334_8229cac865 p167 | 0 | 7 | 1 | 9 | 0 |
| 20-3-13 | 钒(V)的鉴定 | 30 | 19/11/0 | candidate-1-9b93a689=NH₄VO₃ + H₂SO₄ 酸化, candidate-2-4b1d96d3=加入 H₂O₂, candidate-3-de4dbb09=H₂O₂ 不足与过量时颜色变化比较 | expchunk_protocol_4faa721af035 p166, expchunk_00334_8229cac865 p167 | 0 | 5 | 1 | 11 | 0 |
| 20-3-14 | 小设计实验 | 30 | 18/12/0 | candidate-1-de6f1130=已知溶液中含 Fe³⁺、Co²⁺、Ni²⁺，设计方案分别检出三种离子 | expchunk_00334_8229cac865 p167, expchunk_00335_1df34eedec p167 | 30 | 0 | 1 | 9 | 0 |

## Repairs Made

| repair area | count/status | evidence-first note |
| --- | --- | --- |
| JSON summary counts | normalized | summary now matches records: keep/rewrite/reject 316/194/0 |
| supporting theory flags/check booleans | normalized | `quality_flags.requires_supporting_theory` and `semantic_checks.checked_supporting_theory_when_needed` now follow `source_audit.theory_dependency` |
| active generic stems | 167 | remaining `下列哪项判断与实验操作、现象或结论一致` shells were replaced with experiment-specific focus stems |
| option-link diagnostics | 1245 | template diagnostics were replaced with point-specific notes tied to the experiment focus and option text |
| current-release seed repairs | 2 | `CHK5_SEM_EXP_20_2_08_001` and `CHK5_SEM_EXP_20_3_01_002` remain repaired and evidence-supported |
| JSON parse | pass | UTF-8 JSON parsed after edits |

## Low-Depth Status

| low_depth_status | count |
| --- | --- |
| rewritten_from_reagent_name_recognition | 2 |
| reviewed_and_retained | 218 |
| not_flagged_or_already_acceptable | 289 |
| rewritten_to_record-grouping_prerequisite | 1 |

No low-depth item remains solely as unbound reagent-name recognition. `CHK5_SEM_EXP_20_3_01_002` retains only a prerequisite classification risk, documented in the manual log, because the rewritten item asks students to group water-coordinated cations rather than identify a bare ion name.

## Evidence Insufficient Items

Final evidence-insufficient items: none.

Original evidence-insufficient or exact-color-risk items that are now final-supported:

| question_id | experiment_code | original_reason | final_evidence_sufficient | effective_stem |
| --- | --- | --- | --- | --- |
| CHK5_SEM_EXP_20_3_02_004 | 20-3-02 | evidence_insufficient_exact_color | true | 在《20-3-02 阴离子颜色》中，关于 过渡金属含氧阴离子颜色记录，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_02_005 | 20-3-02 | evidence_insufficient_exact_color | true | 在《20-3-02 阴离子颜色》中，关于 过渡金属含氧阴离子颜色记录，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_02_014 | 20-3-02 | evidence_insufficient_exact_color | true | 在《20-3-02 阴离子颜色》中，关于 过渡金属含氧阴离子颜色记录，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_02_015 | 20-3-02 | evidence_insufficient_exact_color | true | 在《20-3-02 阴离子颜色》中，关于 过渡金属含氧阴离子颜色记录，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_02_023 | 20-3-02 | evidence_insufficient_exact_color_mobile_fill | true | 在《20-3-02 阴离子颜色》中，关于 过渡金属含氧阴离子颜色记录，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_02_024 | 20-3-02 | evidence_insufficient_exact_color_mobile_fill | true | 在《20-3-02 阴离子颜色》中，关于 过渡金属含氧阴离子颜色记录，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_13_006 | 20-3-13 | evidence_insufficient_exact_color | true | 在《20-3-13 钒(V)的鉴定》中，关于 钒(V) 与 H₂O₂ 的过氧钒鉴定，哪项表述正确？ |
| CHK5_SEM_EXP_20_3_13_026 | 20-3-13 | evidence_insufficient_exact_color_mobile_fill | true | 在《20-3-13 钒(V)的鉴定》中，关于 钒(V) 与 H₂O₂ 的过氧钒鉴定，哪项表述正确？ |

## Supporting Theory Dependencies

Supporting theory dependent questions: 203. Each row below names the theory chunk ids recorded in the release JSON.

| question_id | experiment_code | effective_type | supporting_theory_chunk_ids | canonical_chunk_ids |
| --- | --- | --- | --- | --- |
| CHK5_SEM_EXP_20_2_08_014 | 20-2-08 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e | expchunk_00319_b995aa9123, expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_003 | 20-2-09 | single_choice | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_005 | 20-2-09 | single_choice | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_009 | 20-2-09 | single_choice | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_013 | 20-2-09 | true_false | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_020 | 20-2-09 | true_false | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_023 | 20-2-09 | single_choice | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_09_025 | 20-2-09 | fill_blank | textbook_prose_01156_e3d54318a3, textbook_prose_01157_702c31a997 | expchunk_00322_6c10a1661c |
| CHK5_SEM_EXP_20_2_10_001 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_002 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_003 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_004 | 20-2-10 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_005 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_006 | 20-2-10 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_007 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_008 | 20-2-10 | single_choice | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_009 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_010 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_011 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_012 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_013 | 20-2-10 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_014 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_015 | 20-2-10 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_016 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_017 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_018 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_019 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_020 | 20-2-10 | true_false | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_021 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_022 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_023 | 20-2-10 | fill_blank | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_024 | 20-2-10 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_025 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_026 | 20-2-10 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_027 | 20-2-10 | fill_blank | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_028 | 20-2-10 | fill_blank | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6, textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_029 | 20-2-10 | single_choice | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_2_10_030 | 20-2-10 | fill_blank | textbook_prose_00293_6e62d1272e, textbook_prose_01106_3d011dae4c | expchunk_00319_b995aa9123, expchunk_00321_53b9414bde, expchunk_00323_56549b57c0 |
| CHK5_SEM_EXP_20_3_01_003 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_004 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_01305_dd5a94da50 | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_005 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_006 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_007 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_008 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_013 | 20-3-01 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_014 | 20-3-01 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_01305_dd5a94da50 | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_015 | 20-3-01 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_016 | 20-3-01 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_018 | 20-3-01 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_020 | 20-3-01 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_021 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_022 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_01305_dd5a94da50 | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_023 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_024 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_025 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_026 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_029 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_01_030 | 20-3-01 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00327_e59c162b54, expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_002 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_003 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_007 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_011 | 20-3-02 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_018 | 20-3-02 | true_false | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_021 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_022 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_028 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_02_030 | 20-3-02 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f | expchunk_00330_3a60414cf4 |
| CHK5_SEM_EXP_20_3_04_003 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_004 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_005 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_006 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_008 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_009 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_013 | 20-3-04 | true_false | textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_014 | 20-3-04 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_015 | 20-3-04 | true_false | textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_017 | 20-3-04 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_020 | 20-3-04 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_024 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_025 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_026 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_027 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_028 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_04_029 | 20-3-04 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9 |
| CHK5_SEM_EXP_20_3_05_006 | 20-3-05 | single_choice | textbook_table_record_table_p224_t01_r071 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_007 | 20-3-05 | single_choice | textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_008 | 20-3-05 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_013 | 20-3-05 | true_false | textbook_table_record_table_p224_t01_r071 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_014 | 20-3-05 | true_false | textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_026 | 20-3-05 | fill_blank | textbook_table_record_table_p224_t01_r071 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_027 | 20-3-05 | single_choice | textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_05_028 | 20-3-05 | fill_blank | textbook_prose_01305_dd5a94da50 | expchunk_00332_42b6908ee0 |
| CHK5_SEM_EXP_20_3_06_001 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_002 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_003 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_004 | 20-3-06 | single_choice | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_005 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_006 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_007 | 20-3-06 | single_choice | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_009 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_010 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_011 | 20-3-06 | true_false | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_012 | 20-3-06 | true_false | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_013 | 20-3-06 | true_false | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_014 | 20-3-06 | true_false | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_018 | 20-3-06 | true_false | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_019 | 20-3-06 | true_false | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_020 | 20-3-06 | true_false | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_021 | 20-3-06 | single_choice | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_022 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_025 | 20-3-06 | fill_blank | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_026 | 20-3-06 | single_choice | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_027 | 20-3-06 | fill_blank | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_028 | 20-3-06 | fill_blank | textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_029 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_06_030 | 20-3-06 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_prose_00037_a7dbd4c099, textbook_prose_00039_cb1a979cf8, textbook_prose_01297_b761f39d9a, textbook_prose_01340_c4d5e485b6 | expchunk_00332_42b6908ee0, expchunk_00336_68bde523f4 |
| CHK5_SEM_EXP_20_3_07_003 | 20-3-07 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_004 | 20-3-07 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_008 | 20-3-07 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_013 | 20-3-07 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_014 | 20-3-07 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_019 | 20-3-07 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_022 | 20-3-07 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_025 | 20-3-07 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_028 | 20-3-07 | single_choice | textbook_table_record_table_p224_t01_r071 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_029 | 20-3-07 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_07_030 | 20-3-07 | fill_blank | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00332_42b6908ee0, expchunk_00333_d08e49be44 |
| CHK5_SEM_EXP_20_3_08_002 | 20-3-08 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_003 | 20-3-08 | single_choice | textbook_table_record_table_p224_t01_r071 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_009 | 20-3-08 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_012 | 20-3-08 | true_false | textbook_table_record_table_p224_t01_r071 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_013 | 20-3-08 | true_false | textbook_table_record_table_p224_t01_r071 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_019 | 20-3-08 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_022 | 20-3-08 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_023 | 20-3-08 | single_choice | textbook_table_record_table_p224_t01_r071 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_08_029 | 20-3-08 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00327_e59c162b54, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_003 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_004 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_007 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_008 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_012 | 20-3-09 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_013 | 20-3-09 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_014 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_017 | 20-3-09 | true_false | textbook_table_record_table_p224_t01_r071 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_019 | 20-3-09 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_024 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_025 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_026 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_09_028 | 20-3-09 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00331_3f7cc41ff9, expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_005 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_006 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_007 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_008 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_012 | 20-3-10 | true_false | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_013 | 20-3-10 | true_false | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_018 | 20-3-10 | true_false | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_020 | 20-3-10 | true_false | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_025 | 20-3-10 | fill_blank | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_026 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_027 | 20-3-10 | fill_blank | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_028 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_10_029 | 20-3-10 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_003 | 20-3-11 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_006 | 20-3-11 | single_choice | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_007 | 20-3-11 | single_choice | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_013 | 20-3-11 | true_false | textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_015 | 20-3-11 | true_false | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_017 | 20-3-11 | true_false | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db, textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_020 | 20-3-11 | true_false | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db, textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_024 | 20-3-11 | single_choice | textbook_prose_01118_9e2eabedd8, textbook_prose_01119_8478df1f7f, textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db, textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_027 | 20-3-11 | fill_blank | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_028 | 20-3-11 | single_choice | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db, textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_11_030 | 20-3-11 | single_choice | textbook_prose_00296_5f7afd3720, textbook_prose_00297_530efe80db, textbook_prose_00293_6e62d1272e | expchunk_00334_8229cac865 |
| CHK5_SEM_EXP_20_3_14_001 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_002 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_003 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_004 | 20-3-14 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_005 | 20-3-14 | single_choice | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_006 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_007 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_008 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_009 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_010 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_011 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_012 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_013 | 20-3-14 | true_false | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_014 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_015 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_016 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_017 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_018 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_019 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_020 | 20-3-14 | true_false | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_021 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_022 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_023 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_024 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_025 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_026 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_027 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_028 | 20-3-14 | fill_blank | textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_029 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |
| CHK5_SEM_EXP_20_3_14_030 | 20-3-14 | single_choice | textbook_table_record_table_p224_t01_r071, textbook_table_record_table_p224_t01_r051, textbook_prose_01305_dd5a94da50 | expchunk_00334_8229cac865, expchunk_00335_1df34eedec |

## Multi-Point Questions

Multi-point questions: 113. These require more than one bound video point and remain supported because the effective question asks for grouping, sequencing, comparison, or combined procedure.

| question_id | experiment_code | effective_type | primary_point_keys | secondary_point_keys | status |
| --- | --- | --- | --- | --- | --- |
| CHK5_SEM_EXP_20_3_01_002 | 20-3-01 | single_choice | candidate-1-e0d18274, candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | none | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_009 | 20-3-01 | single_choice | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_010 | 20-3-01 | single_choice | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_011 | 20-3-01 | true_false | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_012 | 20-3-01 | true_false | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_017 | 20-3-01 | true_false | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_018 | 20-3-01 | true_false | candidate-1-e0d18274 | candidate-2-1d49d35b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_019 | 20-3-01 | true_false | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_020 | 20-3-01 | true_false | candidate-5-a4376972 | candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_027 | 20-3-01 | single_choice | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_01_028 | 20-3-01 | single_choice | candidate-1-e0d18274 | candidate-2-1d49d35b, candidate-3-99dd6b35, candidate-4-3926ad6c, candidate-5-a4376972, candidate-6-c0cbece1 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_006 | 20-3-02 | single_choice | candidate-1-6c3245f9 | candidate-2-5db23da9, candidate-3-f81ca373, candidate-4-095a2458 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_007 | 20-3-02 | single_choice | candidate-1-6c3245f9 | candidate-3-f81ca373 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_008 | 20-3-02 | single_choice | candidate-5-ca04bf5e | candidate-6-d074e740 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_010 | 20-3-02 | single_choice | candidate-1-6c3245f9 | candidate-2-5db23da9, candidate-3-f81ca373 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_011 | 20-3-02 | true_false | candidate-1-6c3245f9 | candidate-3-f81ca373 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_012 | 20-3-02 | true_false | candidate-1-6c3245f9 | candidate-2-5db23da9, candidate-3-f81ca373, candidate-4-095a2458, candidate-5-ca04bf5e, candidate-6-d074e740, candidate-7-b5d923bb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_013 | 20-3-02 | true_false | candidate-5-ca04bf5e | candidate-6-d074e740 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_016 | 20-3-02 | true_false | candidate-5-ca04bf5e | candidate-6-d074e740 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_017 | 20-3-02 | true_false | candidate-1-6c3245f9 | candidate-2-5db23da9, candidate-3-f81ca373, candidate-4-095a2458, candidate-5-ca04bf5e, candidate-6-d074e740, candidate-7-b5d923bb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_018 | 20-3-02 | true_false | candidate-1-6c3245f9 | candidate-3-f81ca373 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_028 | 20-3-02 | single_choice | candidate-1-6c3245f9 | candidate-3-f81ca373 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_02_029 | 20-3-02 | single_choice | candidate-1-6c3245f9 | candidate-2-5db23da9, candidate-3-f81ca373, candidate-4-095a2458, candidate-5-ca04bf5e, candidate-6-d074e740, candidate-7-b5d923bb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_005 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_006 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_007 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_008 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_009 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_016 | 20-3-03 | true_false | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_017 | 20-3-03 | true_false | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_018 | 20-3-03 | true_false | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_019 | 20-3-03 | true_false | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_026 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_027 | 20-3-03 | fill_blank | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_028 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_03_029 | 20-3-03 | single_choice | candidate-1-80cf72b8 | candidate-2-9d1424ba | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_002 | 20-3-04 | single_choice | candidate-2-5eaed5b5 | candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_005 | 20-3-04 | single_choice | candidate-1-2059a278 | candidate-2-5eaed5b5, candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_007 | 20-3-04 | single_choice | candidate-2-5eaed5b5 | candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_010 | 20-3-04 | single_choice | candidate-1-2059a278 | candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_011 | 20-3-04 | true_false | candidate-2-5eaed5b5 | candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_015 | 20-3-04 | true_false | candidate-1-2059a278 | candidate-2-5eaed5b5, candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_016 | 20-3-04 | true_false | candidate-2-5eaed5b5 | candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_020 | 20-3-04 | true_false | candidate-1-2059a278 | candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_023 | 20-3-04 | single_choice | candidate-3-c47ca8d9 | candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_04_029 | 20-3-04 | single_choice | candidate-1-2059a278 | candidate-2-5eaed5b5, candidate-3-c47ca8d9, candidate-4-e1fb1262 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_001 | 20-3-05 | single_choice | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_002 | 20-3-05 | single_choice | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_005 | 20-3-05 | single_choice | candidate-5-947eed90 | candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_006 | 20-3-05 | single_choice | candidate-3-50abfa44 | candidate-4-351f37ad | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_007 | 20-3-05 | single_choice | candidate-5-947eed90 | candidate-7-4a58a252 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_010 | 20-3-05 | single_choice | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb, candidate-8-38d3ba33 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_011 | 20-3-05 | true_false | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_012 | 20-3-05 | true_false | candidate-7-4a58a252 | candidate-8-38d3ba33 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_013 | 20-3-05 | true_false | candidate-3-50abfa44 | candidate-4-351f37ad | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_014 | 20-3-05 | true_false | candidate-5-947eed90 | candidate-7-4a58a252 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_016 | 20-3-05 | true_false | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_017 | 20-3-05 | true_false | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_019 | 20-3-05 | true_false | candidate-5-947eed90 | candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_020 | 20-3-05 | true_false | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb, candidate-8-38d3ba33 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_021 | 20-3-05 | single_choice | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_022 | 20-3-05 | single_choice | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_025 | 20-3-05 | single_choice | candidate-5-947eed90 | candidate-6-c08dc9eb | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_026 | 20-3-05 | fill_blank | candidate-3-50abfa44 | candidate-4-351f37ad | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_027 | 20-3-05 | single_choice | candidate-5-947eed90 | candidate-7-4a58a252 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_05_030 | 20-3-05 | fill_blank | candidate-1-a21fffae | candidate-2-01f186e4, candidate-3-50abfa44, candidate-4-351f37ad, candidate-5-947eed90, candidate-6-c08dc9eb, candidate-8-38d3ba33 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_005 | 20-3-06 | single_choice | candidate-3-01fbe9ee | candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_007 | 20-3-06 | single_choice | candidate-1-81b774c1 | candidate-2-a5f9b5b1, candidate-3-01fbe9ee, candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_008 | 20-3-06 | single_choice | candidate-1-81b774c1 | candidate-2-a5f9b5b1, candidate-3-01fbe9ee, candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_014 | 20-3-06 | true_false | candidate-3-01fbe9ee | candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_015 | 20-3-06 | true_false | candidate-1-81b774c1 | candidate-2-a5f9b5b1, candidate-3-01fbe9ee, candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_020 | 20-3-06 | true_false | candidate-1-81b774c1 | candidate-2-a5f9b5b1, candidate-3-01fbe9ee, candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_06_028 | 20-3-06 | fill_blank | candidate-1-81b774c1 | candidate-2-a5f9b5b1, candidate-3-01fbe9ee, candidate-4-2650ce4f | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_07_007 | 20-3-07 | single_choice | candidate-1-d78b3d70 | candidate-2-627e8ed0, candidate-3-7d9492a7 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_07_009 | 20-3-07 | single_choice | candidate-1-d78b3d70 | candidate-2-627e8ed0 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_07_010 | 20-3-07 | single_choice | candidate-1-d78b3d70 | candidate-2-627e8ed0, candidate-3-7d9492a7 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_07_017 | 20-3-07 | single_choice | candidate-1-d78b3d70 | candidate-2-627e8ed0, candidate-3-7d9492a7 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_07_020 | 20-3-07 | true_false | candidate-1-d78b3d70 | candidate-2-627e8ed0, candidate-3-7d9492a7 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_07_026 | 20-3-07 | fill_blank | candidate-1-d78b3d70 | candidate-2-627e8ed0, candidate-3-7d9492a7 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_001 | 20-3-08 | single_choice | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_006 | 20-3-08 | single_choice | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_008 | 20-3-08 | single_choice | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_010 | 20-3-08 | single_choice | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_011 | 20-3-08 | true_false | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_016 | 20-3-08 | true_false | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_018 | 20-3-08 | true_false | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_020 | 20-3-08 | true_false | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_026 | 20-3-08 | single_choice | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_028 | 20-3-08 | fill_blank | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_08_030 | 20-3-08 | fill_blank | candidate-1-19f29b28 | candidate-2-d3d9277b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_10_009 | 20-3-10 | single_choice | candidate-1-8de46ba4 | candidate-2-18c41387 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_10_011 | 20-3-10 | true_false | candidate-1-8de46ba4 | candidate-2-18c41387 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_10_019 | 20-3-10 | true_false | candidate-1-8de46ba4 | candidate-2-18c41387 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_10_029 | 20-3-10 | single_choice | candidate-1-8de46ba4 | candidate-2-18c41387 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_008 | 20-3-11 | single_choice | candidate-2-1a398c1b | candidate-5-1777b5af | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_009 | 20-3-11 | single_choice | candidate-1-193ad1c0 | candidate-2-1a398c1b, candidate-3-5d1daef7, candidate-4-f71d0da2, candidate-5-1777b5af | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_010 | 20-3-11 | single_choice | candidate-1-193ad1c0 | candidate-2-1a398c1b, candidate-3-5d1daef7, candidate-4-f71d0da2, candidate-5-1777b5af | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_012 | 20-3-11 | true_false | candidate-1-193ad1c0 | candidate-2-1a398c1b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_015 | 20-3-11 | true_false | candidate-4-f71d0da2 | candidate-5-1777b5af | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_016 | 20-3-11 | single_choice | candidate-2-1a398c1b | candidate-5-1777b5af | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_11_029 | 20-3-11 | single_choice | candidate-1-193ad1c0 | candidate-2-1a398c1b, candidate-3-5d1daef7, candidate-4-f71d0da2, candidate-5-1777b5af | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_008 | 20-3-12 | single_choice | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_010 | 20-3-12 | single_choice | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_014 | 20-3-12 | true_false | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_017 | 20-3-12 | true_false | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_019 | 20-3-12 | true_false | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_020 | 20-3-12 | true_false | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_12_028 | 20-3-12 | single_choice | candidate-1-862feb96 | candidate-2-c01f7a7b | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_13_001 | 20-3-13 | single_choice | candidate-1-9b93a689 | candidate-2-4b1d96d3, candidate-3-de4dbb09 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_13_009 | 20-3-13 | single_choice | candidate-1-9b93a689 | candidate-2-4b1d96d3 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_13_011 | 20-3-13 | true_false | candidate-1-9b93a689 | candidate-2-4b1d96d3, candidate-3-de4dbb09 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_13_019 | 20-3-13 | true_false | candidate-1-9b93a689 | candidate-2-4b1d96d3 | multi-point evidence binding checked |
| CHK5_SEM_EXP_20_3_13_021 | 20-3-13 | single_choice | candidate-1-9b93a689 | candidate-2-4b1d96d3, candidate-3-de4dbb09 | multi-point evidence binding checked |

## Mobile Fill-Blank Review

Current fill blanks: 35; mobile risk after final review: 0.

| question_id | experiment_code | effective_stem | accepted_answers | mobile_status |
| --- | --- | --- | --- | --- |
| CHK5_SEM_EXP_20_2_08_023 | 20-2-08 | 在《20-2-08 铬(III)盐的水解》实验中，该体系主要体现 Cr(III) 的____作用。 | 水解 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_08_026 | 20-2-08 | 在《20-2-08 铬(III)盐的水解》实验中，操作后应重点____现象。 | 观察 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_08_030 | 20-2-08 | 在《20-2-08 铬(III)盐的水解》实验中，出现氢氧化物类沉淀说明 Cr(III) 盐发生____。 | 水解 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_09_022 | 20-2-09 | 在《20-2-09 钛(IV)盐的水解》实验中，TiOSO₄ 稀释后需加热____。 | 煮沸 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_09_025 | 20-2-09 | 在《20-2-09 钛(IV)盐的水解》实验中，加水____通常促进 Ti(IV)盐水解。 | 稀释 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_09_027 | 20-2-09 | 在《20-2-09 钛(IV)盐的水解》实验中，水解过程中观察到溶液浑浊，说明生成了难溶____。 | 沉淀, 水解产物 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_09_030 | 20-2-09 | 在《20-2-09 钛(IV)盐的水解》实验中，Ti(IV)盐水解需要加入适量____水。 | 蒸馏, 蒸馏水 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_10_023 | 20-2-10 | 在《20-2-10 小设计实验》实验中，Cr(OH)₃ 和 Al(OH)₃ 具有____，可利用过量碱处理。 | 两性 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_10_027 | 20-2-10 | 在《20-2-10 小设计实验》实验中，分离后应对目标离子进行____。 | 确认检出, 检出 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_10_028 | 20-2-10 | 在《20-2-10 小设计实验》实验中，Cr³⁺ 与 Al³⁺ 分离可利用____性质差异。 | 氧化还原, 氧化还原性质 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_2_10_030 | 20-2-10 | 在《20-2-10 小设计实验》实验中，方案应写清分离顺序和____。 | 检出证据, 检出依据 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_03_024 | 20-3-03 | 在《20-3-03 Cr(III) 的水合异构现象》实验中，实验重点观察加热前后溶液____的变化。 | 颜色 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_03_027 | 20-3-03 | 在《20-3-03 Cr(III) 的水合异构现象》实验中，“热/冷”标注说明该变化受____影响。 | 温度 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_05_023 | 20-3-05 | 在《20-3-05 氨合物》实验中，滴加氨水后静置，是为了观察体系____。 | 后续变化, 变化 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_05_026 | 20-3-05 | 在《20-3-05 氨合物》实验中，Fe²⁺、Fe³⁺ 在氨水中通常更易生成____沉淀。 | 氢氧化物 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_05_028 | 20-3-05 | 在《20-3-05 氨合物》实验中，Ni²⁺ 与过量氨水反映其形成____的能力。 | 氨合物 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_05_029 | 20-3-05 | 在《20-3-05 氨合物》实验中，加 NaOH 不再沉淀可说明金属离子可能处于较稳定____中。 | 配合物, 氨合物 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_05_030 | 20-3-05 | 在《20-3-05 氨合物》实验中，该实验最终比较金属离子形成____的能力。 | 氨合物 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_06_025 | 20-3-06 | 在《20-3-06 配合物的形成对氧化还原性的影响》实验中，EDTA 可配合 Fe³⁺，从而改变 Fe³⁺/Fe²⁺ 电对的____。 | 电势, 电极电势 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_06_027 | 20-3-06 | 在《20-3-06 配合物的形成对氧化还原性的影响》实验中，NaF 配合 Fe³⁺ 后，Fe³⁺ 氧化 I⁻ 的能力通常____。 | 减弱, 降低 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_06_028 | 20-3-06 | 在《20-3-06 配合物的形成对氧化还原性的影响》实验中，该实验说明配合物形成会影响____。 | 氧化还原反应 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_07_026 | 20-3-07 | 在《20-3-07 配合物稳定性与配体的关系》实验中，本实验比较配合物稳定性与____的关系。 | 配体 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_07_027 | 20-3-07 | 在《20-3-07 配合物稳定性与配体的关系》实验中，乙二胺因能形成螯环，常产生____效应。 | 螯合 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_07_030 | 20-3-07 | 在《20-3-07 配合物稳定性与配体的关系》实验中，Na₂C₂O₄ 加入 FeCl₃ + KSCN 体系后，观察重点是溶液____变化。 | 颜色, 颜色变化 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_08_024 | 20-3-08 | 在《20-3-08 铁的鉴定》实验中，Fe(II) 与铁氰化钾阳性时可生成____沉淀。 | 蓝色, 蓝 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_08_025 | 20-3-08 | 在《20-3-08 铁的鉴定》实验中，鉴定 Fe(II) 时应避免其被空气____为 Fe(III)。 | 氧化 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_08_028 | 20-3-08 | 在《20-3-08 铁的鉴定》实验中，区分两种铁离子应选择能区分____的特征反应。 | 价态 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_08_030 | 20-3-08 | 在《20-3-08 铁的鉴定》实验中，该实验核心是利用____反应鉴定铁离子。 | 配合 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_10_025 | 20-3-10 | 在《20-3-10 镍(II)的鉴定》实验中，Ni²⁺ 与丁二酮肟阳性时生成____沉淀。 | 鲜红色, 红色 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_10_027 | 20-3-10 | 在《20-3-10 镍(II)的鉴定》实验中，反应式中 H₂dmg 表示____。 | 丁二酮肟 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_11_026 | 20-3-11 | 在《20-3-11 铬(III)的鉴定》实验中，酸化后加入的有机溶剂可为乙醚或____。 | 戊醇 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_11_027 | 20-3-11 | 在《20-3-11 铬(III)的鉴定》实验中，继续加入 H₂O₂ 后，有机层出现____是阳性现象。 | 深蓝色, 蓝色 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_12_029 | 20-3-12 | 在《20-3-12 钛(IV)的鉴定》实验中，NH₃·H₂O 在第二步中提供____性环境。 | 碱, 碱性 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_13_025 | 20-3-13 | 在《20-3-13 钒(V)的鉴定》实验中，阳性反应生成____配合物。 | 过氧钒 | ok: short normalized accepted answers |
| CHK5_SEM_EXP_20_3_14_028 | 20-3-14 | 在《20-3-14 小设计实验》实验中，Ni²⁺ 鉴定前常用 NH₃·H₂O 调至____碱性。 | 弱, 弱碱性 | ok: short normalized accepted answers |

## Option-Link Review

All 322 single-choice questions have option-link labels aligned to effective options, exactly one link for the correct answer label, valid experiment point keys, and concrete Chinese diagnostic notes.

| experiment_code | title | single_choice_questions | point-specific_diagnostics | anomalies |
| --- | --- | --- | --- | --- |
| 20-2-08 | 铬(III)盐的水解 | 23 | 90 | 0 |
| 20-2-09 | 钛(IV)盐的水解 | 19 | 76 | 0 |
| 20-2-10 | 小设计实验 | 16 | 64 | 0 |
| 20-3-01 | 水合阳离子颜色 | 20 | 77 | 0 |
| 20-3-02 | 阴离子颜色 | 22 | 88 | 0 |
| 20-3-03 | Cr(III) 的水合异构现象 | 18 | 72 | 0 |
| 20-3-04 | 观察不同配体的 Co(II) 配合物的颜色 | 21 | 84 | 0 |
| 20-3-05 | 氨合物 | 15 | 60 | 0 |
| 20-3-06 | 配合物的形成对氧化还原性的影响 | 17 | 68 | 0 |
| 20-3-07 | 配合物稳定性与配体的关系 | 18 | 72 | 0 |
| 20-3-08 | 铁的鉴定 | 17 | 68 | 0 |
| 20-3-09 | 钴(II)的鉴定 | 21 | 84 | 0 |
| 20-3-10 | 镍(II)的鉴定 | 18 | 72 | 0 |
| 20-3-11 | 铬(III)的鉴定 | 19 | 76 | 0 |
| 20-3-12 | 钛(IV)的鉴定 | 19 | 76 | 0 |
| 20-3-13 | 钒(V)的鉴定 | 20 | 80 | 0 |
| 20-3-14 | 小设计实验 | 19 | 76 | 0 |

## Formula Display And Scaffold Scan

| scan | result |
| --- | --- |
| effective scaffold residue | 0 hits for `实验语境`, `并且要放在`, `对应内容为`, and the generic operation/phenomenon/conclusion shell |
| visible option-link scaffold diagnostics | 0 hits for the previous generic diagnostic templates |
| ASCII formula display residue | 0 hits in effective stems/options/explanations or visible option-link text |
| fill-blank formula input burden | 0 current fill blanks require complex formula strings |

## Parse And Coverage Validation

- `chunk_5_release_final_v1.json` parses as UTF-8 JSON after edits.
- Active release question count remains 510.
- Manual log batch rows = 510 and question ids are unique.
- The evidence-first pass covered every active question in chunk 5; it did not use sampling as a replacement for full review.
