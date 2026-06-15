# 19-1-04 手工语义重建报告

## Packet

- chunk：chunk_1
- packet：19-1-04
- 标题：卤素离子的还原性（通风橱内进行）
- 输入：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_1\19-1-04.json`
- 输出 JSON：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_1\19-1-04_rebuilt_v1.json`
- 本次未修改任何 `chunk_X_release_final_v1.json`。

## Manual Statement

本包为逐题人工语义重建，不是脚本生成。重建时逐题核对了原题、选项、答案、解析、point key、video point、RAG canonical 实验文本、实验报告模板和必要的无机化学理论文本。

## Counts

- 总题数：30
- 保留：27
- 重写：3
- 废弃：0
- 题型：17 道单选、9 道判断、4 道填空

## RAG Evidence

- `expchunk_00193_497eb97bd6`：实验目的，掌握卤素氧化性和卤素离子还原性。
- `expchunk_00200_b534720bf8`：KCl、KBr、KI 固体分别加浓硫酸，观察并选用醋酸铅、碘化钾-淀粉、pH 试纸等检验逸出气体，比较卤素离子还原性。
- `expchunk_00012_8133802620`：实验报告示例表，列出 KI+浓硫酸/湿醋酸铅试纸、KBr+浓硫酸/湿碘-淀粉试纸、KCl+浓硫酸/湿 pH 试纸。
- `expchunk_00161_dee462b3bd`：醋酸铅试纸用于检验 H₂S，生成黑色 PbS。
- `expchunk_00162_1d49f603b8`：碘化钾-淀粉试纸用于检验 Cl₂、Br₂ 等氧化性气体，I₂ 与淀粉作用显蓝。
- `textbook_prose_00030_522edfaa72`：卤离子还原性顺序为 F⁻ << Cl⁻ < Br⁻ < I⁻。

## Rewrite List

- Q015：原题与 Q005 重复；重写为三组“卤化物 + 浓硫酸 + 试纸”配对综合题。
- Q021：原填空要求输入“碘化钾/KI”，含符号输入风险；重写为单选题。
- Q023：原填空要求输入“碘化钾-淀粉/KI-淀粉”，含符号输入风险；重写为单选题。

## Keep But Edge

- Q010、Q020 涉及浓硫酸氧化性，需要结合卤离子还原性顺序解释；canonical 给出操作和比较目的，理论块补强反应角色。
- Q006、Q017 为安全题，canonical 标题已标注通风橱内进行，但具体“刺激性或有毒气体”属于实验安全常识性推断。

## Evidence Insufficient List

- 当前重建未保留任何缺少点位支撑的 FeCl₃ 设计题；旧包中已将这类方向替换为当前视频点位覆盖的浓硫酸/试纸体系。
- 未发现必须废弃的题。

## Multipoint Bindings

- Q001、Q005、Q009、Q015、Q018、Q021、Q026、Q027 绑定多组 KCl/KBr/KI 点位，因为这些题比较三种卤离子还原性。
- Q003、Q013、Q022 重点绑定 candidate-4 与 KI/醋酸铅试纸证据。
- Q004、Q014、Q023、Q024、Q030 重点绑定 KBr 与湿 KI-淀粉试纸检验 Br₂ 的点位。

## Fill Blank Risk

- Q022：答案“湿醋酸铅/醋酸铅”，中文短答案，风险低。
- Q025：答案“通风橱”，中文短答案，风险低。
- Q028：答案“浓硫酸”，中文短答案，风险低。
- Q029：答案“酸性”，中文短答案，风险低。
- 原 Q021、Q023 的公式/符号型填空已改写为单选。

## Final Check

- 手工重建题数：30。
- 所有单选题均有 4 个选项和 option_links。
- 判断题答案为布尔值。
- 填空题为 normalized exact 短中文答案。
- 未修改任何 release JSON。
