# 19-1-03 手工语义重建报告

## Packet

- chunk：chunk_1
- packet：19-1-03
- 标题：氯水对溴离子、碘离子混合溶液的氧化顺序
- 输入：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_1\19-1-03.json`
- 输出 JSON：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_1\19-1-03_rebuilt_v1.json`
- 本次未修改任何 `chunk_X_release_final_v1.json`。

## Manual Statement

本包为逐题人工语义重建，不是脚本生成。重建时逐题核对了原题、选项、答案、解析、point key、video point、RAG canonical 实验文本与必要的无机化学理论文本。

## Counts

- 总题数：30
- 保留：24
- 重写：6
- 废弃：0
- 题型：17 道单选、10 道判断、3 道填空

## RAG Evidence

- `expchunk_00193_497eb97bd6`：实验目的，掌握卤素氧化性和卤素离子还原性。
- `expchunk_00198_1c405139fa`：卤素在四氯化碳中的溶解性观察，为 CCl₄ 显色判断提供背景。
- `expchunk_00199_8240477bff`：本步骤：KBr、KI、CCl₄ 混合体系中逐滴加入氯水，仔细观察四氯化碳液层颜色变化，并说明卤素氧化性递变。
- `textbook_prose_00023_a92d0d217e`：溴单质红棕色、碘单质紫黑色等物理颜色背景。
- `textbook_prose_00028_a4c7b7c9ae`：碘在四氯化碳中溶液呈紫色。
- `textbook_prose_00030_522edfaa72`：卤素单质氧化性 Cl₂ > Br₂ > I₂，卤离子还原性 Cl⁻ < Br⁻ < I⁻。

## Rewrite List

- Q008：旧题只问 CCl₄ 层颜色变化用途；重写为“紫色到溴色特征”与氧化先后相连。
- Q019：旧题只纠正滴数事实；重写为“不是因为 KI 加得更多，而是 I⁻ 还原性更强”的判断。
- Q021：旧题与 Q001 重复；重写为从紫色特征判断 I₂ 生成。
- Q022：旧题仅识别 CCl₄；重写为解释为什么要观察 CCl₄ 层。
- Q023：旧填空答案 KI 有移动端符号输入风险且深度低；重写为 KBr 多于 KI 仍能观察 I⁻ 先被氧化的推理题。
- Q028：旧题重复“颜色变化用于判断先后”；重写为只记录滴数而不记录颜色时缺少什么证据。

## Keep But Edge

- Q006、Q026：Br₂ 在 CCl₄ 中橙色/红棕色为常规实验观察；本包用 `textbook_prose_00023_a92d0d217e` 支撑溴单质红棕色，用 `expchunk_00198_1c405139fa` 和 `expchunk_00199_8240477bff` 支撑 CCl₄ 观察背景。RAG 未像 I₂ 那样直接给出 Br₂-CCl₄ 溶液精确色表，故列为边界保留题。
- Q007、Q014、Q020、Q027、Q029 需要 `textbook_prose_00030_522edfaa72` 支撑氧化/还原性顺序。

## Evidence Insufficient List

- 未发现必须废弃的题。
- 仅 Br₂ 在 CCl₄ 中具体色调属于间接支撑；已在对应题 `source_audit` 中注明，并避免把该颜色作为唯一高强度证据。

## Multipoint Bindings

- Q001、Q003、Q004、Q011、Q017、Q019、Q023、Q027、Q030 同时绑定 candidate-1 和 candidate-2，因为这些题同时涉及混合体系操作和 CCl₄ 层颜色判读。
- Q002、Q005、Q006、Q008、Q009、Q010、Q012、Q013、Q014、Q016、Q018、Q020、Q021、Q022、Q026、Q028、Q029 主要绑定 candidate-2，因为它们围绕 CCl₄ 层颜色、氧化先后和结论判断。
- Q024 绑定两点位，因为“逐滴加入”来自操作点位，“观察 CCl₄ 层颜色”来自观察点位。

## Fill Blank Risk

- Q024：答案为“逐滴/逐滴地”，中文短答案，风险低。
- Q025：答案为“紫色”，中文颜色词，风险低。
- Q029：答案为“还原性”，中文短答案，风险低。
- 原 Q023 的 KI 符号填空已改为单选，避免移动端公式输入风险。

## Final Check

- 手工重建题数：30。
- 所有单选题均有 4 个选项和 option_links。
- 判断题答案为布尔值。
- 填空题为 normalized exact 短中文答案。
- 未修改任何 release JSON。
