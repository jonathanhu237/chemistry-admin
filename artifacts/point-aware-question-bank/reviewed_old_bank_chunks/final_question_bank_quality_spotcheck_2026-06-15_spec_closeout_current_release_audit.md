# Final Question Bank Quality Spotcheck - Spec Closeout Current Release Audit

生成时间：2026-06-15（Asia/Shanghai）

## 1. OpenSpec 收束状态

- Change：`full-question-bank-semantic-release-repair`
- `openspec validate full-question-bank-semantic-release-repair --strict`：通过。
- `openspec status --change full-question-bank-semantic-release-repair --json`：proposal、design、specs、tasks 四类 artifact 均为 `done`。
- `openspec instructions apply --change full-question-bank-semantic-release-repair --json`：153 个任务中完成 16 个，剩余 137 个。

结论：本 spec 可以阶段性收束为“规范与任务清单有效，实施未完成”。不能按完成状态归档，也不能据此声明 chunks 1-5 已可发布入库。若强制归档，会带着大量未完成 blocker 进入 archive，不符合当前题库发布目标。

## 2. 当前 release JSON 只读风险盘点

说明：以下为只读启发式盘点，用于定位风险，不替代逐题语义判断。题库文件未因本次抽检被修改。

| Chunk | Active questions | Template option-link hits | Visible ASCII formula hits | Formula/mobile fill risks | Multi-point bindings | Low-depth sample-pattern hits |
|---|---:|---:|---:|---:|---:|---:|
| chunk 1 | 443 | 73 | 152 | 56 | 204 | 1 |
| chunk 2 | 450 | 0 | 103 | 64 | 140 | 0 |
| chunk 3 | 450 | 163 | 135 | 133 | 174 | 0 |
| chunk 4 | 450 | 216 | 74 | 126 | 221 | 2 |
| chunk 5 | 510 | 322 | 49 | 35 | 113 | 0 |

这些计数已经足以说明：当前 release JSON 仍存在系统性风险，尤其是 template option-link、多点位泛绑定、手机端填空风险和学生可见公式显示风险。

## 3. 抽检方法

- 覆盖 chunks 1-5，每个 chunk 抽 2 道，共 10 道。
- 样本刻意覆盖：单选、填空、keep、rewrite、多点位、公式/手机输入风险、模板 option-link 风险、低深度识别题。
- 每道题阅读了 effective question、答案/解析、option_links、primary/secondary point keys、video_points、source_audit，并用 formal experiment point inventory 中的 canonical source refs 做证据校对。

## 4. 抽检样本结论

| Chunk | Question ID | 实验 | 点位绑定 | 终审抽检结论 | 主要理由 |
|---|---|---|---|---|---|
| 1 | `CHUNK1_19_1_01_Q007` | 19-1-01 氯、溴、碘的置换次序 | primary `candidate-3-9b8be606` | 条件保留 | 题目考 CCl₄ 有机层颜色观察，教材原文支持 KBr/KI/CCl₄/氯水/溴水设计实验和观察 CCl₄ 层颜色。但题干是泛化现象观察，语义覆盖 candidate 1/2/3，当前只绑 candidate 3 偏窄。 |
| 1 | `CHUNK1_19_1_01_Q025` | 19-1-01 氯、溴、碘的置换次序 | primary `candidate-1-034a8366`, `candidate-2-1e180c68`; secondary `candidate-3-9b8be606` | 不建议入库 | 填空题只问“所属主题是卤素的____”，实质是背标题/分类词“氧化性”，不考操作、现象或结论。多点位绑定也被题目语义弱化为实验标题级信息。 |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_001` | 19-3-03 SO₃²⁻ 的检出 | primary `candidate-1-26a8e36e`, `candidate-2-795f5a0b` | 可入库，建议小修 option_links | 题目问检出 SO₃²⁻ 前除去 SO₄²⁻ 干扰的原因，正式点位清单有“设计方法除去 SO₄²⁻ 干扰 / 验证样品中 SO₃²⁻ 的存在”，双点位成立。部分 distractor 诊断仍偏模板化，但题干、答案、解析可支撑。 |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_025` | 19-3-03 SO₃²⁻ 的检出 | primary `candidate-2-795f5a0b` | 质量偏低但可条件保留 | 填“紫”短答案手机端可判分，教材 SO₂ 还原性点位和酸性 KMnO₄ 观察能支撑。但本题偏颜色记忆，解析依赖 SO₂ 还原性 supporting theory，不是强实验推理题。 |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q001` | 19-6-02 金属镁燃烧 | primary `candidate-1-a3329021`, `candidate-2-ea144d3d` | 可入库 | 题目同时问“除去氧化膜后点燃”和“观察燃烧及生成物”，教材原文直接支持“用砂纸除去表面氧化层，点燃，观察现象”。多点位绑定真实。 |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q021` | 19-6-02 金属镁燃烧 | primary `candidate-1-a3329021`, `candidate-2-ea144d3d` | 可入库 | 填空答案“燃烧/燃烧现象”短、确定，题干把除膜、点燃和观察任务连起来，不是单纯试剂名记忆。 |
| 4 | `REV_CH4_EXP_20_1_02_Q001` | 20-1-02 氨合物 | primary `candidate-1` 至 `candidate-5`; secondary `candidate-6` | 不建议入库 | 题目只问提供 NH₃ 配体的试剂，属于试剂名识别；primary 绑定五个金属盐点位过宽；解析只有“多种金属盐与氨水反应”；option_links 仍有模板句。 |
| 4 | `REV_CH4_EXP_20_1_02_Q021` | 20-1-02 氨合物 | primary `candidate-1` 至 `candidate-5`; secondary `candidate-6` | 不建议入库 | 填空“____作为 NH₃ 来源”仍是试剂名回忆；accepted_answers 同时展示/保留 `NH3·H2O` 与 `NH₃·H₂O`，存在手机输入和可见 alias 风险；点位绑定过宽。 |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | 20-2-08 铬(III)盐的水解 | primary `candidate-1-376fa2cd` | 不建议入库 | 教材支持 Cr₂(SO₄)₃ + Na₂CO₃ 观察铬(III)盐水解，但题干仍是“哪项判断与实验操作、现象或结论一致”的泛化壳，答案偏铬盐名称识别，option_links 仍是模板诊断。 |
| 5 | `CHK5_SEM_EXP_20_3_01_002` | 20-3-01 水合阳离子颜色 | primary `candidate-1-e0d18274`; secondary candidates 2-6 | 不建议按现状入库 | 教材原文列出水合阳离子和阴离子，答案 CrO₄²⁻ 有依据；但题目本质是列表分类识别，正确选项 D 的 point_key 却指向 Ti 水合阳离子 candidate 1，点位语义错误，option_links 仍模板化。 |

## 5. 抽检统计

- 抽检总数：10
- 可直接入库：3
- 条件保留或质量偏低：2
- 不建议入库：5

按这轮样本，当前最终题库不能声明“完全符合验收标准，可以入库发布”。问题不是个别字段小瑕疵，而是仍有成批的低深度题、模板 option_links、过宽点位绑定、填空手机端风险和 metadata 与最终有效题不一致。

## 6. 收束结论

1. 上一个 spec 当前只能阶段性收束，不能完成归档：OpenSpec artifact 有效，但 137 个实施任务未完成。
2. 当前 chunks 1-5 release JSON 不应直接入库发布。
3. 下一步应继续按 OpenSpec 任务顺序执行逐实验手工语义修复，优先处理 template option-link、过宽多点位、低深度试剂名/标题题、手机端填空风险和有效题 metadata 反映旧题的问题。

