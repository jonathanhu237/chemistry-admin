# Chunk 5 Reviewed Old Bank Prompt

你在 `E:\chemistry-admin` 工作。任务是逐题审查旧实验题库，不是重新出题，不是使用 scaffold 模板。

## 本块范围

- Chunk: 5
- 实验范围：`20-2-08` 到 `20-3-14`
- 目标原题数：510
- 输出 reviewed artifact：`artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_5_reviewed_v1.json`
- 输出 review report：`artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_5_review_report.md`

## 必读输入

- `E:\chemistry-rag\data\generated\experiment_question_bank_v1\experiment_question_bank_v1.json`
- `artifacts/point-aware-question-bank/formal_experiment_point_inventory.json`
- `artifacts/point-aware-question-bank/generation_review_protocol.md`
- `artifacts/point-aware-question-bank/representative_batch_v1.json`
- `artifacts/point-aware-question-bank/representative_batch_v1_review.md`
- `artifacts/point-aware-question-bank/full_candidate_scaffold_quality_audit.md`

## 只处理这些实验

`20-2-08`, `20-2-09`, `20-2-10`, `20-3-01`, `20-3-02`, `20-3-03`, `20-3-04`, `20-3-05`, `20-3-06`, `20-3-07`, `20-3-08`, `20-3-09`, `20-3-10`, `20-3-11`, `20-3-12`, `20-3-13`, `20-3-14`

## 逐题审查规则

对本块每一道旧题逐题审查，不能只做批量关键词匹配。

每题必须判断：

- 化学事实和答案是否正确。
- 题干、选项、答案、解析是否能被 canonical experiment chunk 支撑。
- 应绑定到哪个或哪些已有实验视频点位 `primary_point_keys`。
- 是否需要 `secondary_point_keys` 表示多点位证据。
- 单选题每个选项是否需要 `option_links`，错误选项标注为相邻点位、误区、弱干扰项或无关干扰项。
- 填空题是否适合手机端输入。
- 是否太浅，例如只问直接试剂名、方程式、机械记忆。

## 决策标准

- `keep`：旧题质量可用，补齐点位、证据、选项诊断和审查记录后保留。
- `rewrite`：旧题思路可用但题干/选项/答案/填空形式不合适，必须给 `proposed_question`。
- `reject`：旧题无法被资料支撑或方向不适合，必须给 replacement `proposed_question`，除非报告中说明证据缺失导致无法替换。

不要简单丢题。目标是保留旧 2310 题的有效劳动，形成 reviewed 版本。

## 填空题手机端规则

填空题只允许短 token 或短词，例如一个离子、一个短观察词、一个短关系词。

必须 rewrite 的情况：

- 答案是长试剂组合。
- 答案是完整化学方程式。
- 答案是多句话解释。
- 答案需要学生在手机端输入复杂上下标、长配合物或方案。

## 输出 JSON 形状

顶层：

```json
{
  "metadata": {
    "artifact_type": "reviewed_old_experiment_question_bank",
    "version": "chunk-5-reviewed-v1",
    "source_bank": "experiment_question_bank_v1",
    "review_mode": "codex_question_by_question"
  },
  "experiments": []
}
```

每个 reviewed item 至少包含：

```json
{
  "original_question": {},
  "review_decision": "keep | rewrite | reject",
  "quality_flags": [],
  "primary_point_keys": [],
  "secondary_point_keys": [],
  "coverage_tags": [],
  "option_links": [],
  "source_audit": {
    "canonical_chunk_ids": [],
    "supporting_theory_chunk_ids": [],
    "evidence_sufficient": true,
    "reviewer_note": ""
  },
  "proposed_question": {}
}
```

`keep` 可以没有 `proposed_question`。`rewrite` 和 `reject` 必须有 `proposed_question`。

## Review Report 必须包含

- 原题数。
- keep / rewrite / reject 数。
- replacement 数。
- 题型分布。
- 填空题改写数量。
- 多点位绑定数量。
- 证据不足或需要主线程复核的问题。

完成后不要导入数据库，不要改公共代码，不要改 OpenSpec tasks。

