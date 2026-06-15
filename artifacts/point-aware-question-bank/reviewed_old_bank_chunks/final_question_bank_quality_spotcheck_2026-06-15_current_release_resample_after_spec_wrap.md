# Current Release Resample After Spec Wrap

Date: 2026-06-15

Scope: current `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.

## OpenSpec Wrap Status

`full-question-bank-semantic-release-repair` is valid under `openspec validate --strict`, but it is not archive-ready as a completed implementation. `openspec list` shows `19/182` tasks complete. `openspec status --json` marks proposal/design/spec/task artifacts as present, but that is artifact readiness only; the task checklist and release QA gates remain incomplete.

Decision: keep the spec open. Do not archive it and do not treat the final bank as import-ready.

## Read-Only Structural Check

All five release JSON files parse.

Current risk radar, used only for navigation and not as semantic judgement:

| Chunk | Records Scanned | Visible ASCII Formula Indicators | Formula/Phone Fill-Blank Indicators | Multi-Point Indicators |
|---|---:|---:|---:|---:|
| 1 | 450 | 63 | 20 | 201 |
| 2 | 450 | 44 | 43 | 140 |
| 3 | 450 | 126 | 104 | 174 |
| 4 | 450 | 46 | 105 | 221 |
| 5 | 510 | 36 | 24 | 113 |

These counts are risk indicators, not final defect counts. They are enough to show that the current final bank still needs manual semantic repair before release.

## Manual Resample Result

Sample size: 18 questions across chunks 1-5.

Result: 7 pass, 2 conditional, 9 fail.

| Chunk | Question | Effective Stem Summary | Point Keys Checked | Result | Judgement |
|---|---|---|---|---|---|
| 1 | `CHUNK1_19_1_08_Q002` | 滤纸承载卤化银沉淀并便于钥匙遮光轮廓观察 | `candidate-4-fb906ca4` | PASS | 题干、答案、解析和 option links 都围绕教材步骤；不是单纯材料名回忆。 |
| 1 | `CHUNK1_19_1_08_Q015` | 判断钥匙遮挡作用和受光/遮光区差异 | `candidate-4-fb906ca4` | PASS | 判断题不靠双重否定，能由 canonical 步骤直接支撑。 |
| 1 | `CHUNK1_19_1_08_Q029` | 由钥匙轮廓推出卤化银感光性 | `candidate-4-fb906ca4` | PASS | 从现象推结论，点位和 option links 具体。 |
| 1 | `CHUNK1_19_2_01_Q030` | KI-淀粉试纸中 I⁻ 被氧化生成 I₂ | `candidate-2-dbd095b4` | FAIL | 解析仍是泛化模板；option text 中 D 是 `K⁺`，option_link 中 D 却写 `CCl₄`，存在选项漂移，不能入库。 |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_001` | 检出 SO₃²⁻ 前先除去 SO₄²⁻ 的原因 | `candidate-1-26a8e36e`, `candidate-2-795f5a0b` | FAIL | 题干只问“除去 SO₄²⁻ 干扰”的原因，应主要绑定 candidate-1；当前多绑定 candidate-2 过宽，option diagnostics 仍偏模板化。 |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_025` | SO₂ 使酸性 KMnO₄ 溶液紫色褪去 | `candidate-2-795f5a0b` | CONDITIONAL | `紫` 是手机端可判短答案，但只是低深度颜色锚点；可保留但必须在批次日志中标明低深度保留理由和 theory 依赖。 |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_030` | 酸化 SO₃²⁻ 放出 SO₂ | `candidate-2-795f5a0b` | FAIL | 仍是公式/符号填空，接受 `SO2`、`SO₂`、`二氧化硫`，且解析泛化；应改成确定性单选或只显示中文答案并隐藏符号别名。 |
| 2 | `EXP_19_4_09_SEMANTIC_FINAL_021` | 棕色环棕色物质写作 Fe(NO)SO₄ | `candidate-2-a452c505` | FAIL | 手机端公式填空风险高， visible answer aliases 包含 ASCII/Unicode 公式，解析泛化。 |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q001` | 除氧化膜、点燃镁条并观察燃烧和生成物 | `candidate-1-a3329021`, `candidate-2-ea144d3d` | PASS | 多点位绑定真实对应操作链和观察链，option links 具体。 |
| 3 | `OLD_CHUNK3_EXP_19_8_01_Q001` | Pb(NO₃)₂ 中滴加哪种溶液生成 Pb(OH)₂ | `candidate-1-356d797d` | FAIL | 低深度试剂名回忆；错误选项也绑定同一 point_key；正确项诊断仍是模板句。 |
| 3 | `OLD_CHUNK3_EXP_19_8_11_Q001` | 铅丹组成分析的研究对象化学式 | `candidate-1-bca363dc` | FAIL | 低深度对象/化学式回忆；错误选项全部绑定同一 point_key；supporting theory 和题目实际要求不匹配。 |
| 4 | `REV_CH4_EXP_20_1_02_Q001` | CuSO₄ + NH₃·H₂O 的沉淀生成与过量氨水溶解观察链 | `candidate-1-5b3e91cf`, `candidate-6-e34dc5e9` | PASS | 从试剂名回忆改成现象链判断，证据、点位、option links 具体。 |
| 4 | `REV_CH4_EXP_20_1_02_Q021` | AgNO₃ + NH₃·H₂O 后继续观察过量氨水中的沉淀溶解 | `candidate-2-167c639f`, `candidate-6-e34dc5e9` | PASS | 题目考查“为什么继续观察”，不是背氨水来源；多点位合理。 |
| 4 | `REV_CH4_EXP_20_1_02_Q022` | 铜氨配合物生成可用硫酸铜溶液 | `candidate-1-5b3e91cf` | FAIL | 仍是低深度试剂名填空，接受 `CuSO4`/`CuSO₄` 别名，解析泛化。 |
| 4 | `REV_CH4_EXP_20_2_01_Q030` | 概括氢氧化物酸碱性实验目的和操作 | eight candidate keys | FAIL | 题干过泛，正确项 option diagnostic 是英文且缺少 text 字段；多点位绑定过宽。 |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | Cr₂(SO₄)₃ + Na₂CO₃ 的铬(III)盐水解观察 | `candidate-1-376fa2cd` | PASS | 操作、试剂和观察任务具体，option links 能区分钛盐水解和其他离子检验。 |
| 5 | `CHK5_SEM_EXP_20_3_01_002` | 将水合阳离子颜色与阴离子颜色分组记录 | `candidate-1-e0d18274`, `candidate-2-1d49d35b`, `candidate-3-99dd6b35`, `candidate-4-3926ad6c`, `candidate-5-a4376972`, `candidate-6-c0cbece1` | CONDITIONAL | 题目质量比原始列表题好，分组意图清楚；但多点位较宽，最终入库前仍需确认各候选点位都真实服务于题干。 |
| 5 | `CHK5_SEM_EXP_20_3_14_026` | 泛化壳：“哪项判断与实验操作、现象或结论一致” | `candidate-1-de6f1130` | FAIL | 仍是 generic shell stem；option diagnostics 泛化，错误项 D 还绑定了正确 point_key；不能入库。 |

## Quality Decision

The current final bank is not ready for import.

The strongest remaining blockers are:

- Formula-heavy or symbolic fill blanks still appear in active effective questions.
- Several explanations are still generic and do not name the actual operation, reagent, phenomenon, product, or conclusion.
- Option-link diagnostics still have text drift, English diagnostics, template notes, or wrong point_key assignment.
- Some questions remain low-depth reagent/formula/object recall.
- Multi-point bindings are sometimes inherited too broadly instead of matching the final stem semantics.

Recommended next execution order:

1. Continue `full-question-bank-semantic-release-repair` rather than archiving it.
2. Repair the failed samples above in their exact batches.
3. Re-audit adjacent structurally similar questions in those batches.
4. Only after every chunk has a complete manual semantic log and zero known blocker classes, run a new final import-readiness resample.
