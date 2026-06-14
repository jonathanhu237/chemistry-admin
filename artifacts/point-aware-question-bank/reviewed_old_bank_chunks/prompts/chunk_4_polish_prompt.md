# Chunk 4 Polished Final Prompt

你在 `E:\chemistry-admin` 工作。当前只负责 `chunk_4`，不要处理其他 chunk。

这轮不是重新批量审查，也不是关键词匹配、脚本自动改写、简单沿用 `reviewed_v1` 或 `semantic_final_v1`。这轮目标是做“终稿打磨”：去重 proposed、逐条手修 option_links、把低质量 keep 中最差的一批改写掉，并补准确 supporting theory 引用。

## 输入文件

- 原始分块 prompt：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\prompts\chunk_4_review_prompt.md`
- 初审稿：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_4_reviewed_v1.json`
- 语义终审草稿：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_4_semantic_final_v1.json`
- 语义终审草稿报告：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_4_semantic_final_report.md`
- 原始旧题库：`E:\chemistry-rag\data\generated\experiment_question_bank_v1\experiment_question_bank_v1.json`
- 实验上下文：`E:\chemistry-rag\data\generated\experiment_question_bank_v1\contexts\EXP_*.json`
- 实验点位清单：`E:\chemistry-admin\artifacts\point-aware-question-bank\formal_experiment_point_inventory.json`
- canonical 实验教材 chunks：`E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
- supporting theory chunks：`E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- 审查协议参考：`E:\chemistry-admin\artifacts\point-aware-question-bank\generation_review_protocol.md`

## 输出文件

不要覆盖任何旧文件。请新建：

- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_4_polished_final_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_4_polished_final_report.md`

## 核心要求

请基于 `chunk_4_semantic_final_v1.json` 继续，但必须重新实际阅读本 chunk 每一道题的有效版本：

- `keep`：有效版本是 `original_question`
- `rewrite` / `reject`：有效版本是 `proposed_question`

每题都要确认：

- 题干、选项、答案、解析是否被 canonical 实验原文支撑
- 若判断依赖 supporting theory，必须补准确 `supporting_theory_chunk_ids`，并在 `reviewer_note` 说明依赖 theory 的具体点
- `primary_point_keys` / `secondary_point_keys` 是否真实符合题目语义
- 是否实际涉及多个点位
- 单选题每个 `option_link` 是否具体、合理、非模板化
- 是否太简单，只是在背试剂名、方程式、颜色、标题或实验对象
- 填空题是否适合手机端短答案输入；不适合必须 rewrite
- 判断题是否存在双重否定、绝对化、靠猜也能答的问题
- rewrite / reject 必须给 concrete `proposed_question`，不允许只写 rewrite_direction
- 不允许引入 AI 改学生答案对错，题目必须机器确定性判分

## 本轮重点任务

1. **去重 proposed_question**
   - 检测本 chunk 内所有 `proposed_question.stem` 的规范化重复。
   - 同一实验内不得出现实质相同的 proposed 题干。
   - 重复题必须手工改写成不同考点角度，或在确实无价值时 reject 并给可替代题。
   - 不要用同一套题干批量替换多个原题。

2. **逐条手修 option_links**
   - 对所有单选题处理有效版本的选项。
   - `correct_evidence` 必须指向真实支撑该正确项的 point_key。
   - `adjacent_point` 如果使用，必须填真实相邻 point_key，并说明为什么是相邻而非本题点位。
   - `distractor_misconception` 要说明具体误解：试剂混淆、现象混淆、氧化还原方向混淆、点位错配、理论迁移过度等。
   - 避免泛泛写“不是该题点位的操作、现象或结论”。

3. **低质量 keep 再筛一遍**
   - 重点检查 `low_depth_retained`、`retained_low_quality`、只问名称/颜色/标题/对象/方程式机械记忆的 keep。
   - 最差的一批必须 rewrite，改成基于实验操作、现象、结论、点位比较或因果判断的题。
   - 仍保留的低质量题必须在报告列出理由，例如为了覆盖孤立点位、原题虽浅但机器判分稳定。

4. **补准确 theory 引用**
   - 只有当题目判断确实依赖教材理论时才填 `supporting_theory_chunk_ids`。
   - 只靠实验原文足够的题，`supporting_theory_chunk_ids` 应为空或保持最小必要集合。
   - 每个 theory-dependent 题都要能追到具体 chunk id，不要只写章节或泛泛说明。

5. **手机端填空风险处理**
   - 长化学式、复杂离子式、多别名答案、上下标敏感、多个等价写法的填空题要 rewrite。
   - 可以改成短唯一 token 的填空，或改成机器确定性更强的单选/判断；如改变题型，必须在 reviewer_note 说明。
   - 不要依赖“AI 判断学生答案语义是否等价”。

## JSON 要求

- 保留原有总体结构：metadata、experiments、每道 reviewed item。
- 每个原题仍对应一个 reviewed item，不要丢题。
- metadata 更新为 polished final，例如：

```json
{
  "artifact_type": "polished_final_reviewed_old_experiment_question_bank",
  "version": "chunk-4-polished-final-v1",
  "review_mode": "codex_polished_final_manual_semantic_pass"
}
```

- `review_decision` 只能是 `keep` / `rewrite` / `reject`。
- `rewrite` 和 `reject` 必须有完整、可判分的 `proposed_question`。
- `source_audit.evidence_sufficient` 要表达最终有效题是否证据充分；如果原题不足但 proposed 已修复，请在 note 里区分。
- 可以用脚本做统计和校验，但每题决定、点位绑定、source audit、option_links 必须来自实际读题后的语义判断。

## 报告必须包含

- 总题数、keep / rewrite / reject 数
- 本轮修改过的题目列表，含 review_id、实验编号、修改类型
- proposed 去重修复列表
- option_links 手修摘要，列出高风险修正题
- 仍保留但质量偏低的题目列表及理由
- evidence insufficient 题目列表，并区分“原题不足但 proposed 已修复”和“最终仍不足”
- 多点位题目列表
- 填空题手机端风险列表
- theory-dependent 题目列表，必须列 supporting theory chunk ids
- 你确认“已经逐题语义终稿打磨”的说明

## 最终校验

交付前必须至少确认：

- JSON 可被 UTF-8 正常解析。
- 输出题数等于输入题数。
- `rewrite` / `reject` 没有缺失 concrete `proposed_question`。
- 有效单选题 option 数与 `option_links` 数一致。
- 本 chunk 内无非必要重复 `proposed_question.stem`。
- 没有明显模板化 `diagnostic_note`。
- 没有覆盖 `reviewed_v1` 或 `semantic_final_v1`。
