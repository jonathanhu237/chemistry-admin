# Chunk 3 Evidence-First 全量终审 Prompt

你负责 `chunk_3`，只处理 chunk 3，不修改其他 chunk，不修改 OpenSpec tasks。

## 范围

- Release JSON: `E:/chemistry-admin/artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_3_release_final_v1.json`
- Manual log: `E:/chemistry-admin/artifacts/point-aware-question-bank/reviewed_old_bank_chunks/manual_semantic_rereview_logs/chunk_3_manual_semantic_rereview_log.md`
- 输出报告: `E:/chemistry-admin/artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_3_evidence_first_final_report.md`
- 实验范围: `19-6-02` 至 `20-1-01`
- 对应 OpenSpec 任务: `5.1` 至 `5.16`

## 必须比对的证据来源

- 最终有效题: 当前 release JSON 中每道 active effective question。
- 原题/初审/旧改写参考: `chunk_3_reviewed_v1.json`, `chunk_3_semantic_final_v1.json`, `release_input_freeze_v1/chunk_3_polished_final_v1.json`, `prompts/chunk_3_review_prompt.md`。
- 实验点位/video_points: `E:/chemistry-exam/data/seed/formal_experiments.json`。
- canonical 实验教材原文: `E:/chemistry-exam/data/intermediate/chunks/DOC_EXPERIMENTS_SELECTED.json` 和 `E:/chemistry-exam/data/seed/database_seed.json`。
- supporting theory: 只在 canonical 原文不足以支撑最终判断时使用，主要来自 `database_seed.json` 中 `textbook_prose_*` 或表格记录。

## 工作方式

不要抽检推进。按实验顺序、题号顺序，全量逐题终审每一道 active 题。脚本只能用于定位、统计、抽取上下文、JSON parse 校验；不得用脚本决定 keep/rewrite/reject、点位、解析、选项诊断或题目文本。

每题必须重新判断：

- 题干、答案、解析是否被 canonical 实验原文直接支撑。
- `canonical_chunk_ids` 是否真的支撑最终 effective stem、answer、explanation、point binding。
- `supporting_theory_chunk_ids` 是否必要；如使用 theory，说明哪一项判断依赖 theory。
- `primary_point_keys` / `secondary_point_keys` 是否真实符合题目语义；多点位必须有正当语义理由。
- 单选每个 `option_link` 是否与最终选项文本一致，并说明该选项为什么对/错，不允许模板化。
- 是否仍是低深度背试剂名、颜色、方程式、标题或实验对象；若保留，写明必要性，否则 rewrite。
- 填空题是否适合手机端短答案输入；公式/复杂离子/多别名答案必须 rewrite，除非只保留隐藏判分别名并明确记录。
- 判断题是否双重否定、绝对化、靠猜可答。
- rewrite/reject 必须给 concrete `proposed_question`，不能只写 rewrite_direction。
- 不得引入 AI 改学生答案对错；题目必须机器确定性判分。

## 每题日志字段

在 manual log 中每道 active 题必须且只能出现一次，字段统一：

`question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk`

## 验收输出

完成 chunk 3 后必须输出：

- 修改后的 `chunk_3_release_final_v1.json`，且 UTF-8 JSON parse 通过。
- 更新后的 `chunk_3_manual_semantic_rereview_log.md`，覆盖 chunk 3 每道 active 题一次。
- 新建/更新 `chunk_3_evidence_first_final_report.md`，包含：
  - 总 active 题数、keep/rewrite/reject 数。
  - 每个实验的完成状态。
  - 修改过的题目列表。
  - 仍保留但质量偏低的题目及理由。
  - evidence insufficient 题目列表。
  - 使用 supporting theory 的题目列表及 theory chunk id。
  - 多点位题目列表及多点位理由。
  - 填空题手机端风险列表。
  - option_link 修复/异常列表。
  - JSON parse 校验结果。
  - 明确说明：chunk 3 已按 evidence-first 标准逐题全量终审，未用抽检替代全量检查。

## 禁止事项

- 不要修改其他 chunk。
- 不要修改 OpenSpec tasks。
- 不要声明 chunks 1-5 整体可入库。
- 不要把旧 reviewed_v1 / semantic_final / polished_final 结论当最终结论。
- 不要用 sampling 代替全量逐题检查。
