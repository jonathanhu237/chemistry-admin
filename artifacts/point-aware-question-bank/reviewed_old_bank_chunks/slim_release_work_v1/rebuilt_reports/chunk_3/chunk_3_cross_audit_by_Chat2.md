# chunk_3 rebuilt question bank 交叉抽审报告

## 基本信息

- 抽审 chunk：`chunk_3`
- reviewer chat：`Chat 2`
- 抽审时间：`2026-06-15 19:00:58 +08:00`
- 抽审性质：只读交叉抽审；未修改任何 rebuilt JSON、release final JSON。
- 目标目录：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3`
- 证据源：
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`

## 抽审规模

- 总 packet 数：15
- 总题数：450
- 实际抽审题数：50
- 题型覆盖：
  - single_choice：31
  - true_false：5
  - fill_blank：14
- supporting_theory_required=true 覆盖：22
- multi-point 覆盖：35
- seed 覆盖：5/5
- 全量结构扫描结果：JSON parse 通过；RAG id 缺失 0；单选 answer/options/option_links 标签错误 0；source_audit.evidence_sufficient=false 为 0。

## 抽审题列表

| experiment_code | question_id | question_type | 结论 |
|---|---|---|---|
| 19-6-02 | REBUILT_CH3_19_6_02_Q001 | single_choice | PASS |
| 19-6-02 | REBUILT_CH3_19_6_02_Q004 | single_choice | P0_BLOCKER |
| 19-6-02 | REBUILT_CH3_19_6_02_Q007 | single_choice | PASS |
| 19-6-02 | REBUILT_CH3_19_6_02_Q009 | single_choice | P0_BLOCKER |
| 19-6-02 | REBUILT_CH3_19_6_02_Q011 | single_choice | PASS |
| 19-6-02 | REBUILT_CH3_19_6_02_Q015 | true_false | PASS |
| 19-6-02 | REBUILT_CH3_19_6_02_Q023 | fill_blank | P0_BLOCKER |
| 19-6-02 | REBUILT_CH3_19_6_02_Q026 | single_choice | P2_MINOR |
| 19-6-02 | REBUILT_CH3_19_6_02_Q027 | single_choice | PASS |
| 19-6-02 | REBUILT_CH3_19_6_02_Q028 | single_choice | P0_BLOCKER |
| 19-6-02 | REBUILT_CH3_19_6_02_Q030 | single_choice | PASS |
| 19-6-03 | REBUILT_CH3_19_6_03_Q003 | single_choice | P0_BLOCKER |
| 19-6-03 | REBUILT_CH3_19_6_03_Q012 | single_choice | P0_BLOCKER |
| 19-6-03 | REBUILT_CH3_19_6_03_Q016 | single_choice | PASS |
| 19-6-03 | REBUILT_CH3_19_6_03_Q028 | fill_blank | P0_BLOCKER |
| 19-6-03 | REBUILT_CH3_19_6_03_Q029 | fill_blank | P0_BLOCKER |
| 19-6-04 | REBUILT_CH3_19_6_04_Q008 | single_choice | PASS |
| 19-6-04 | REBUILT_CH3_19_6_04_Q016 | single_choice | PASS |
| 19-8-01 | REBUILT_CH3_19_8_01_Q008 | single_choice | PASS |
| 19-8-01 | REBUILT_CH3_19_8_01_Q009 | single_choice | P0_BLOCKER |
| 19-8-01 | REBUILT_CH3_19_8_01_Q014 | single_choice | P0_BLOCKER |
| 19-8-01 | REBUILT_CH3_19_8_01_Q015 | single_choice | P0_BLOCKER |
| 19-8-01 | REBUILT_CH3_19_8_01_Q020 | true_false | PASS |
| 19-8-01 | REBUILT_CH3_19_8_01_Q028 | fill_blank | P2_MINOR |
| 19-8-01 | REBUILT_CH3_19_8_01_Q029 | fill_blank | P0_BLOCKER |
| 19-8-02 | REBUILT_CH3_19_8_02_Q011 | single_choice | P2_MINOR |
| 19-8-02 | REBUILT_CH3_19_8_02_Q022 | true_false | P2_MINOR |
| 19-8-03 | REBUILT_CH3_19_8_03_Q007 | single_choice | PASS |
| 19-8-03 | REBUILT_CH3_19_8_03_Q030 | fill_blank | PASS |
| 19-8-04 | REBUILT_CH3_19_8_04_Q007 | single_choice | P2_MINOR |
| 19-8-04 | REBUILT_CH3_19_8_04_Q008 | single_choice | PASS |
| 19-8-04 | REBUILT_CH3_19_8_04_Q014 | single_choice | P0_BLOCKER |
| 19-8-04 | REBUILT_CH3_19_8_04_Q026 | fill_blank | P0_BLOCKER |
| 19-8-05 | REBUILT_CH3_19_8_05_Q007 | single_choice | P0_BLOCKER |
| 19-8-05 | REBUILT_CH3_19_8_05_Q021 | true_false | PASS |
| 19-8-05 | REBUILT_CH3_19_8_05_Q030 | fill_blank | PASS |
| 19-8-06 | REBUILT_CH3_19_8_06_Q011 | single_choice | PASS |
| 19-8-06 | REBUILT_CH3_19_8_06_Q030 | fill_blank | P0_BLOCKER |
| 19-8-07 | REBUILT_CH3_19_8_07_Q013 | single_choice | P0_BLOCKER |
| 19-8-07 | REBUILT_CH3_19_8_07_Q024 | fill_blank | PASS |
| 19-8-08 | REBUILT_CH3_19_8_08_Q004 | single_choice | PASS |
| 19-8-08 | REBUILT_CH3_19_8_08_Q028 | fill_blank | PASS |
| 19-8-09 | REBUILT_CH3_19_8_09_Q015 | single_choice | P0_BLOCKER |
| 19-8-09 | REBUILT_CH3_19_8_09_Q020 | true_false | P2_MINOR |
| 19-8-10 | REBUILT_CH3_19_8_10_Q011 | single_choice | PASS |
| 19-8-10 | REBUILT_CH3_19_8_10_Q015 | single_choice | PASS |
| 19-8-11 | REBUILT_CH3_19_8_11_Q007 | single_choice | PASS |
| 19-8-11 | REBUILT_CH3_19_8_11_Q028 | fill_blank | PASS |
| 20-1-01 | REBUILT_CH3_20_1_01_Q025 | fill_blank | PASS |
| 20-1-01 | REBUILT_CH3_20_1_01_Q028 | fill_blank | PASS |

## P0 / P2 详情

| question_id | 级别 | 问题字段 | 问题原文 | 为什么影响入库 | 建议处理 |
|---|---|---|---|---|---|
| REBUILT_CH3_19_6_02_Q004 | P0_BLOCKER | stem / explanation | “如果只按教材实验文本命题…”；“因此这里考查材料依据边界…” | 学生可见题在讨论命题和考查边界，不是直接考实验操作或现象。 | 改成直接判断镁点燃后教材能支持的观察任务或结论边界。 |
| REBUILT_CH3_19_6_02_Q009 | P0_BLOCKER | stem / options / explanation | “最符合教材材料依据的问法”；“要求学生判断…”；“更适合考查…” | 出现问法、要求学生、考查等审查语义。 | 改为直接问镁燃烧观察任务与安全边界，不出现出题口吻。 |
| REBUILT_CH3_19_6_02_Q023 | P0_BLOCKER | stem | “点燃镁条后，教材文本要求学生____。” | 填空题把学生作为审查对象，题面不是实验问题。 | 改为“点燃镁条后，应进行的观察任务是____。” |
| REBUILT_CH3_19_6_02_Q028 | P0_BLOCKER | stem | “若要同时考查操作和理论结论…” | 题干直接讨论考查目标，属于题库语言。 | 改为“镁燃烧实验中，哪项组合同时包含操作和理论结论？” |
| REBUILT_CH3_19_6_03_Q003 | P0_BLOCKER | explanation | “该题考查的是实验装置控制，不要求学生推出具体反应产物。” | 解析把判题意图暴露给学生。 | 改为说明漏斗的装置控制作用和安全观察意义。 |
| REBUILT_CH3_19_6_03_Q012 | P0_BLOCKER | explanation | “这里考查现象和检验任务的组合。” | 解析是考查说明，不是化学解释。 | 改为说明钙与水反应较平稳、仍需观察并检验酸碱性。 |
| REBUILT_CH3_19_6_03_Q028 | P0_BLOCKER | explanation | “该题只考查装置…” | 学生解析中出现题库考查语言。 | 改为“漏斗用于覆盖烧杯，便于安全观察钠/钾与水反应。” |
| REBUILT_CH3_19_6_03_Q029 | P0_BLOCKER | explanation | “避免要求学生输入复杂表述。” | 学生解析讨论输入稳定性。 | 改为说明冷水/热水是镁与水作用的对照变量。 |
| REBUILT_CH3_19_8_01_Q009 | P0_BLOCKER | explanation | “用中文短答或单选考查即可确定判分。” | 直接出现考查和判分语言。 | 改为说明“生成的沉淀”对应沉淀生成现象。 |
| REBUILT_CH3_19_8_01_Q014 | P0_BLOCKER | option.A / option.D / explanation | “分别考查沉淀与硝酸、氢氧化钠的作用”；“无论考查什么…” | 选项和解析都在讨论考查安排。 | 改为“分别观察沉淀与硝酸、氢氧化钠作用”。 |
| REBUILT_CH3_19_8_01_Q015 | P0_BLOCKER | stem / options / explanation | “怎样考查…最稳定”；“继续要求学生输入…”；“输入不稳定…确定判分” | 典型学生可见审查/移动端/判分语言。 | 改为直接考 Pb(Ⅱ) 氢氧化物生成、命名或沉淀与酸碱反应，不讨论输入风险。 |
| REBUILT_CH3_19_8_01_Q029 | P0_BLOCKER | explanation | “这里考查两侧试验的判断方向。” | 解析模板化说明考查意图。 | 改为说明酸侧、碱侧都能反应体现两性。 |
| REBUILT_CH3_19_8_04_Q014 | P0_BLOCKER | explanation | “该问法用中文描述高浓度碱条件…” | 解析讨论问法和数字填空规避。 | 改为说明 40% 氢氧化钠对应最高浓度碱条件。 |
| REBUILT_CH3_19_8_04_Q026 | P0_BLOCKER | explanation | “该空考查化学式对应的中文名称…” | 学生解析使用“该空考查”题库语言。 | 改为“Bi(OH)₃ 的中文名称为氢氧化铋。” |
| REBUILT_CH3_19_8_05_Q007 | P0_BLOCKER | stem / explanation | “最稳妥的考查目标是什么”；“这类题直接写…” | 题干和解析讨论考查策略，不是实验问题。 | 改为比较两种碱浓度下氢氧化锑沉淀的作用表现。 |
| REBUILT_CH3_19_8_06_Q030 | P0_BLOCKER | stem | “不同氧化态的____性质考查。” | 填空题中残留“考查”。 | 改为“本实验属于实验 19-8 中不同氧化态的____性质比较。” |
| REBUILT_CH3_19_8_07_Q013 | P0_BLOCKER | explanation | “该问法以颜色连接到氧化方向…” | 解析讨论问法，学生可见。 | 改为说明紫色来自高锰酸根生成，体现 Pb(Ⅳ) 氧化性。 |
| REBUILT_CH3_19_8_09_Q015 | P0_BLOCKER | stem | “若要让一道题完全由教材直接支撑，最适合考查哪一项？” | 题干直接讨论一道题如何被教材支撑。 | 改为直接问哪项操作由教材直接给出。 |
| REBUILT_CH3_19_6_02_Q026 | P2_MINOR | option_links.diagnostic_note | “短中文答案也可以确定判分。” | option_links 诊断中有判分/输入策略语言；不影响学生题和答案，但不自然。 | 改为“该项偏离实验操作和产物判断。” |
| REBUILT_CH3_19_8_01_Q009 | P2_MINOR | option_links.diagnostic_note | “沉淀生成对应 point 1。” | option_links 诊断中出现内部 point 语义。 | 改为“沉淀生成对应初始加碱步骤。” |
| REBUILT_CH3_19_8_01_Q028 | P2_MINOR | stem | “实验 19-8 的目的要求…” | 目的性填空可判分且有证据，但偏低阶、像实验目的背诵。 | 可保留；若修订，改成通过酸/碱两侧操作判断酸碱性。 |
| REBUILT_CH3_19_8_02_Q011 | P2_MINOR | stem | “本小节属于哪一组元素化合物性质实验？” | 可判分、有证据，但属于模块归属题，化学实验操作性较弱。 | 可保留为范围题；建议后续改成 Sn(OH)₂ 酸碱性实验操作判断。 |
| REBUILT_CH3_19_8_02_Q022 | P2_MINOR | stem | “实验 19-8 的目的之一…” | 可判分、有证据，但仍偏实验目的背诵。 | 可保留；建议改成通过锡氢氧化物酸碱两侧反应判断酸碱性。 |
| REBUILT_CH3_19_8_04_Q007 | P2_MINOR | stem / explanation | “本实验属于实验 19-8 中的哪一模块？” | 模块归属题可判分，但实验操作或现象含量不足。 | 可保留；建议改成 Bi(OH)₃ 与酸/碱作用的操作判断。 |
| REBUILT_CH3_19_8_09_Q020 | P2_MINOR | stem | “学习目标” | 可判分、有证据，但更像学习目标确认，不是具体实验操作。 | 可保留；建议改成 As(Ⅴ)/Sb(Ⅴ)/Bi(Ⅴ) 氧化性比较的具体操作或现象判断。 |

## 专项检查

### 学生可见审查语言命中

全量扫描命中 28 个字段，合并为 18 个 question_id，均在本轮逐题阅读范围内。主要词为“命题”“问法”“考查”“要求学生”“输入不稳定”“确定判分”。这些属于发布阻断类问题，已在 P0 表中逐题列出。

### evidence insufficient

- 结构扫描：`source_audit.evidence_sufficient=false` 为 0。
- RAG id 检查：canonical/theory ids 均可在两份证据源中定位。
- 抽审语义：未发现样本题答案与 source_audit 明显冲突；阻断问题主要不是证据缺失，而是学生可见审查语言。

### point binding 问题

- 未发现 P0/P1 级严重 point 绑定错误。
- multi-point seed 题 `REBUILT_CH3_19_6_02_Q007`、`REBUILT_CH3_19_6_02_Q015`、`REBUILT_CH3_19_6_02_Q030`、`REBUILT_CH3_19_6_03_Q016`、`REBUILT_CH3_19_8_01_Q008` 的 point keys 与题意基本一致。
- `REBUILT_CH3_19_8_01_Q028`、`REBUILT_CH3_19_8_02_Q011`、`REBUILT_CH3_19_8_04_Q007` 等目的/模块题覆盖面较宽，但未构成绑定错误，列为低质量可保留。

### option_links 问题

- 标签结构：单选 answer/options/option_links 标签均无越界或缺失。
- 诊断文本：发现 2 个 P2 级内部词问题：
  - `REBUILT_CH3_19_6_02_Q026`：diagnostic_note 含“确定判分”。
  - `REBUILT_CH3_19_8_01_Q009`：diagnostic_note 含“point 1”。

### fill_blank 手机端风险

- 抽审 fill_blank 14 题。
- 未发现要求输入公式、离子、方程式或复杂别名的高风险填空。
- 但 `REBUILT_CH3_19_6_02_Q023`、`REBUILT_CH3_19_6_03_Q028`、`REBUILT_CH3_19_6_03_Q029`、`REBUILT_CH3_19_8_01_Q029`、`REBUILT_CH3_19_8_04_Q026`、`REBUILT_CH3_19_8_06_Q030` 因 stem/explanation 含审查语言被判为 P0，不是因为答案输入不可控。

### supporting theory 风险

- 抽审 supporting_theory_required=true 题 22 题。
- 未发现 theory id 不存在或明显不足以支撑答案的情况。
- 有些 supporting 题的化学判断本身可成立，但学生可见文本仍含审查语言，例如 `REBUILT_CH3_19_6_02_Q028`、`REBUILT_CH3_19_8_01_Q029`、`REBUILT_CH3_19_8_05_Q007`。

### visible chemistry display

- 未发现 ASCII 电荷、ASCII 罗马价态、LaTeX/caret。
- 脚本命中的若干“19-6-02 / 实验 19-8”等为实验编号，不按 ASCII 化学式 blocker 处理。
- 抽审中可见公式多使用 Unicode 上下标或中文名称；建议后续仍优先中文化学生可见字段中的复杂公式，但本轮主要 blocker 是审查语言。

### 低质量但可保留题

- `REBUILT_CH3_19_8_01_Q028`：目的性填空，可判分但低阶。
- `REBUILT_CH3_19_8_02_Q011`：模块归属题，化学实验操作性弱。
- `REBUILT_CH3_19_8_02_Q022`：实验目的判断，偏背诵。
- `REBUILT_CH3_19_8_04_Q007`：模块归属题，操作性弱。
- `REBUILT_CH3_19_8_09_Q020`：学习目标判断，偏课程目标确认。

### 未发现问题的 seed 列表

- `REBUILT_CH3_19_6_02_Q007`
- `REBUILT_CH3_19_6_02_Q015`
- `REBUILT_CH3_19_6_02_Q030`
- `REBUILT_CH3_19_6_03_Q016`
- `REBUILT_CH3_19_8_01_Q008`

## 最终结论

**FAIL：存在 P0_BLOCKER，不能进入 merge/import。**

主要原因是学生可见字段中仍有多处题库审查语言，尤其是“命题”“问法”“考查”“要求学生”“输入不稳定”“确定判分”。这些问题不影响 JSON parse 或 RAG id 定位，但属于发布阻断，必须在 merge/import 前修复。
