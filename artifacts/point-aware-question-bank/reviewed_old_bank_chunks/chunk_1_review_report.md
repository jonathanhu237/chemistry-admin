# Chunk 1 Old Bank Review Report

## Scope

- Chunk: 1
- Experiment range: `19-1-01` to `19-3-02`
- Reviewed original questions: 450
- Output artifact: `artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_1_reviewed_v1.json`

## Decision Summary

- Keep: 342
- Rewrite: 102
- Reject: 6
- Replacement questions supplied: 108

## Question Type Distribution

| Type | Original count | Keep | Rewrite | Reject |
| --- | ---: | ---: | ---: | ---: |
| `single_choice` | 150 | 108 | 40 | 2 |
| `true_false` | 150 | 128 | 20 | 2 |
| `fill_blank` | 150 | 106 | 42 | 2 |

## Required Counts

- Fill-blank rewritten or rejected: 44
- Multi-point bindings: 220
- Evidence-insufficient originals: 7

## Per-Experiment Summary

| Experiment | Title | Original | Keep | Rewrite | Reject |
| --- | --- | ---: | ---: | ---: | ---: |
| `19-1-01` | 氯、溴、碘的置换次序 | 30 | 24 | 6 | 0 |
| `19-1-02` | 氯水、溴水、碘水氧化性差异的比较 | 30 | 25 | 5 | 0 |
| `19-1-03` | 氯水对溴离子、碘离子混合溶液的氧化顺序 | 30 | 27 | 3 | 0 |
| `19-1-04` | 卤素离子的还原性（通风橱内进行） | 30 | 23 | 7 | 0 |
| `19-1-05` | 次氯酸盐的氧化性 | 30 | 24 | 6 | 0 |
| `19-1-06` | 氯酸盐的氧化性 | 30 | 22 | 8 | 0 |
| `19-1-07` | 氯含氧酸盐的氧化性 | 30 | 24 | 3 | 3 |
| `19-1-08` | 卤化银的感光性 | 30 | 25 | 2 | 3 |
| `19-2-01` | 臭氧的制备与性质 | 30 | 24 | 6 | 0 |
| `19-2-02` | 过氧化氢的制备 | 30 | 23 | 7 | 0 |
| `19-2-03` | 过氧化氢的鉴定 | 30 | 22 | 8 | 0 |
| `19-2-04` | 过氧化氢的性质 | 30 | 26 | 4 | 0 |
| `19-2-05` | 过氧化氢的氧化还原性 | 30 | 12 | 18 | 0 |
| `19-3-01` | 二氧化硫的制备（通风橱内进行） | 30 | 20 | 10 | 0 |
| `19-3-02` | 二氧化硫的性质 | 30 | 21 | 9 | 0 |

## Main Rewrite / Reject Reasons

- `direct_reagent_recognition` (19): 直接试剂名回忆
- `off_point_preparation` (17): 偏向制备点位，非本实验点位
- `off_point_so2_properties` (6): 偏向 SO2 性质，非制备点位
- `templated_true_false` (5): 判断句模板化且诊断弱
- `off_point_identification` (5): 偏向鉴定点位，非本实验点位
- `phone_unfriendly_order_expression` (4): 填空答案是完整顺序表达，不适合手机输入
- `source_point_gap_fecl3` (4): FeCl3 比较有文本证据但缺少本实验视频点位
- `formula_only_recall` (4): 只考化学式
- `off_point_properties` (4): 偏向性质实验，非本制备点位
- `off_point_ki_oxidation` (4): 酸性 H2O2 + KI 不在本小节视频点位
- `canonical_gap_kclo4` (3): KClO4 相关内容缺少 canonical chunk 支撑
- `canonical_gap_agbr_agi_photosensitivity` (3): AgBr/AgI 感光性缺少 canonical chunk 明确支撑
- `off_point_decomposition` (3): 偏向分解/保存点位，非本实验点位
- `off_point_storage` (3): 保存知识缺少本实验视频点位
- `equation_recall` (2): 方程式/产物机械回忆
- `too_numeric_drop_count` (2): 只考滴数等数字细节
- `oxidation_state_recall` (2): 只考氧化态记忆
- `formula_name_recall` (2): 只考离子/酸根名称
- `generic_not_point_bound` (2): 泛化知识，点位绑定弱
- `off_point_safety_preparation` (2): 偏向制备安全，非性质点位
- `too_basic_role_recall` (1): 角色识别过浅
- `too_basic_single_ion` (1): 只考单一离子回忆
- `phone_unfriendly_reagent_combination` (1): 填空答案是长试剂组合，不适合手机输入
- `direct_order_recall` (1): 直接顺序回忆
- `too_basic_reagent_property` (1): 只考试剂性质标签
- `direct_reagent_list` (1): 直接试剂组回忆
- `mechanical_count_recall` (1): 只考份数等机械记忆
- `adjacent_experiment_distractor_as_answer` (1): 把相邻实验内容作为答案
- `wrong_acid_choice` (1): 酸化试剂判断需要改成干扰来源诊断
- `canonical_gap_kclo4_comparison` (1): KClO4 比较缺少 canonical chunk 支撑
- `off_point_next_experiment` (1): 偏向后续鉴定点位
- `equation_product_recall` (1): equation_product_recall

## Evidence Gaps And Main-Thread Review Items

- `19-1-07` 氯含氧酸盐的氧化性: 4 original question(s) marked rewrite/reject because canonical support is insufficient. Examples: CHUNK1_19_1_07_Q006, CHUNK1_19_1_07_Q008, CHUNK1_19_1_07_Q015, CHUNK1_19_1_07_Q025.
- `19-1-08` 卤化银的感光性: 3 original question(s) marked rewrite/reject because canonical support is insufficient. Examples: CHUNK1_19_1_08_Q007, CHUNK1_19_1_08_Q016, CHUNK1_19_1_08_Q027.

Additional review notes:

- Several old questions were chemically correct but asked only for a reagent name, formula, oxidation state, or full order expression; these were rewritten rather than dropped.
- Some split-out experiments share a large canonical chunk. When an old question belonged to an adjacent split point without an existing video point in the current experiment, it was rewritten to the current experiment point set.
- Evidence-gap items are limited to cases where the old assertion relied on point inventory content that the canonical experiment chunk did not clearly support, notably KClO4 and AgBr/AgI photosensitivity claims in this chunk.

## Constraints Followed

- No database import was performed.
- No public code or OpenSpec task files were changed.
- The original question payloads remain preserved under `original_question` for auditability.
