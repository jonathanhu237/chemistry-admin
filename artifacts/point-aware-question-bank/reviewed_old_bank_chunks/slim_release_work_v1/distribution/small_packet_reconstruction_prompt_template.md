# Small-Packet Reconstruction Prompt Template

Copy this prompt into a new Codex chat. Replace `<CHUNK_N>` and `<PACKET_LIST>` with that chat's allocation from `five_chat_work_allocation.md`.

```text
请按 OpenSpec 小包重构流程执行，不要审稿语气，不要只做抽检，不要只修 metadata。

你负责：

- chunk: <CHUNK_N>
- packets: <PACKET_LIST>

必须读取并遵守：

- OpenSpec change:
  E:\chemistry-exam\openspec\changes\full-question-bank-semantic-release-repair
- 小包重构 spec:
  E:\chemistry-exam\openspec\changes\full-question-bank-semantic-release-repair\small_packet_reconstruction_spec.md
- 理想样包：
  E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\ideal_packages\chunk_2_19-3-03_ideal_package_v1.json
- 理想样包预览：
  E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\ideal_packages\chunk_2_19-3-03_ideal_package_preview.md

输入小包位置：

E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\<CHUNK_N>\<experiment_code>.json

证据源头只能回到 RAG 原始语料：

- E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl
- E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl

重要原则：

1. 不要直接修改 `chunk_X_release_final_v1.json`。
2. 不要把 RAG 原文大段嵌入输出；只记录 chunk id、source file、line number、简短 evidence role。
3. 小包里的 `canonical_chunk_ids` / `supporting_theory_chunk_ids` 只是旧系统候选 locator，不是可信证据。必须逐题读 RAG 原文比对。
4. id 在 RAG 中存在不等于语义支持成立。
5. 脚本只能用于读取、定位、统计、校验；keep/rewrite/reject、题干、答案、解析、点位、option_links、source_audit 必须来自你逐题阅读后的语义判断。
6. 如果实验原文只写“观察现象”，而题目要问预期现象或原因，必须找 supporting theory，并说明哪些判断依赖 theory。
7. 不允许开放式或 AI 判分题；所有题必须机器确定性判分。
8. 填空题只保留手机端稳定的普通中文短答案；化学式、离子式、方程式、价态、多别名符号答案一律改成单选，除非明确作为隐藏 grading alias 且不展示。
9. 单选题每个 option_link 必须针对真实选项语义，不允许模板化说明。
10. 多点位绑定必须由题干真实语义支撑；否则收窄到一个点位。
11. 重复题必须重构，不要只是换说法。把重复题改成实验操作、现象、顺序、安全、输出要求、比较、证据选择或 theory 推理。

每个 packet 的输出：

1. 重构 JSON：

E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\<CHUNK_N>\<experiment_code>_rebuilt_v1.json

2. 重构报告：

E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\<CHUNK_N>\<experiment_code>_rebuild_report.md

重构 JSON 必须至少包含：

- metadata
- video_points
- evidence_sources
- questions

每道题必须包含：

- question_id
- question_type
- stem
- options（单选必须 4 个）
- answer
- explanation
- difficulty
- primary_point_keys
- secondary_point_keys
- coverage_tags
- option_links（单选必须每个选项 1 条）
- source_audit:
  - canonical_chunk_ids
  - supporting_theory_chunk_ids
  - evidence_sufficient
  - supporting_theory_required
  - reviewer_note
- mobile_input_risk
- machine_grading

报告必须包含：

- 总题数和题型统计
- 相对原包 keep/rewrite/reject 数
- 发现的重复簇及如何重构
- 使用的 canonical evidence ids
- 使用的 supporting theory ids 及依赖理由
- 被拒绝或替换的旧 evidence ids
- 多点位题目列表及理由
- 填空题手机端风险表
- 低质量但保留题目及理由
- unresolved blockers，如果没有写 `0`
- validation 结果

每个 packet 完成后必须校验：

- JSON parse OK
- 题数等于原小包 active question 数，除非报告明确说明证据不足导致短缺
- question_id 唯一
- 单选 answer label 存在于 options
- 单选 option_links 数量等于 options 数量
- cited evidence ids 都能在 RAG JSONL 中找到
- 无缺失 explanation
- 无公式/离子/方程式作为可见填空答案
- 无未说明的 visible ASCII digit formula
- 无 evidence_insufficient 却标为可发布的题

建议命令环境：

在 PowerShell 里读中文/RAG 时先设置：

`$env:PYTHONIOENCODING='utf-8'`

按 packets 顺序逐个执行。每完成一个 packet，简短汇报输出文件和 validation 结果，然后继续下一个。
```
