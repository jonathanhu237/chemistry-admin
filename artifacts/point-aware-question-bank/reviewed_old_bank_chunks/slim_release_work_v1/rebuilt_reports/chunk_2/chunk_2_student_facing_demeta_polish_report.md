# chunk_2 学生可见去审查化语义修复报告

## 范围复述

- 负责 chunk：`chunk_2`
- 负责 packet：`19-3-03`、`19-3-04`、`19-3-05`、`19-3-06`、`19-4-01`、`19-4-02`、`19-4-03`、`19-4-04`、`19-4-05`、`19-4-06`、`19-4-07`、`19-4-08`、`19-4-09`、`19-5-01`、`19-6-01`
- 修改输出路径：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2`
- 报告输出路径：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_2\chunk_2_student_facing_demeta_polish_report.md`
- 禁止项：本 pass 未直接修改任何 `chunk_X_release_final_v1.json`。

## 总体统计

- 总题数：450
- 扫描到的 meta-risk 候选题数：119
  - 口径：学生可见 `stem`、`options.text`、`explanation` 中命中严格审查词、广义审查/发布/考查/判分语义、需人工判断的“设计/题目/题干/点位”等语义，以及 raw/internal/ASCII 数字公式等发布阻断格式风险后，合并去重。
- 实际修改题数：113
- 保留但说明理由的题数：7
  - 其中 `IDEAL_CH2_19_3_03_Q004` 同时做了去审查化修改，并保留了教材实验设计语义。
- 答案改动：0 题
- point keys 改动：0 题
- option_links 结构改动：0 题；仅同步确认可见选项文字修改后仍与原证据链一致。
- supporting theory 状态：未新增、未删除、未改动；修改题中 69 题原本依赖 supporting theory，44 题不依赖。

## 所有修改 question_id

`IDEAL_CH2_19_3_03_Q004`, `IDEAL_CH2_19_3_03_Q009`, `IDEAL_CH2_19_3_03_Q022`,
`REBUILT_CH2_19_3_04_Q001`, `REBUILT_CH2_19_3_04_Q003`, `REBUILT_CH2_19_3_04_Q004`, `REBUILT_CH2_19_3_04_Q008`, `REBUILT_CH2_19_3_04_Q010`, `REBUILT_CH2_19_3_04_Q012`, `REBUILT_CH2_19_3_04_Q013`, `REBUILT_CH2_19_3_04_Q014`, `REBUILT_CH2_19_3_04_Q015`, `REBUILT_CH2_19_3_04_Q016`, `REBUILT_CH2_19_3_04_Q017`, `REBUILT_CH2_19_3_04_Q018`, `REBUILT_CH2_19_3_04_Q020`, `REBUILT_CH2_19_3_04_Q023`, `REBUILT_CH2_19_3_04_Q027`, `REBUILT_CH2_19_3_04_Q028`, `REBUILT_CH2_19_3_04_Q029`, `REBUILT_CH2_19_3_04_Q030`,
`REBUILT_CH2_19_3_05_Q003`, `REBUILT_CH2_19_3_05_Q007`, `REBUILT_CH2_19_3_05_Q010`, `REBUILT_CH2_19_3_05_Q011`, `REBUILT_CH2_19_3_05_Q013`, `REBUILT_CH2_19_3_05_Q014`, `REBUILT_CH2_19_3_05_Q016`, `REBUILT_CH2_19_3_05_Q017`, `REBUILT_CH2_19_3_05_Q025`, `REBUILT_CH2_19_3_05_Q028`, `REBUILT_CH2_19_3_05_Q030`,
`REBUILT_CH2_19_3_06_Q004`, `REBUILT_CH2_19_3_06_Q009`, `REBUILT_CH2_19_3_06_Q027`,
`REBUILT_CH2_19_4_01_Q002`, `REBUILT_CH2_19_4_01_Q003`, `REBUILT_CH2_19_4_01_Q008`, `REBUILT_CH2_19_4_01_Q012`, `REBUILT_CH2_19_4_01_Q020`, `REBUILT_CH2_19_4_01_Q022`, `REBUILT_CH2_19_4_01_Q027`, `REBUILT_CH2_19_4_01_Q028`, `REBUILT_CH2_19_4_01_Q029`, `REBUILT_CH2_19_4_01_Q030`,
`REBUILT_CH2_19_4_02_Q005`, `REBUILT_CH2_19_4_02_Q006`, `REBUILT_CH2_19_4_02_Q019`, `REBUILT_CH2_19_4_02_Q028`, `REBUILT_CH2_19_4_02_Q029`,
`REBUILT_CH2_19_4_03_Q029`, `REBUILT_CH2_19_4_03_Q030`,
`REBUILT_CH2_19_4_04_Q027`, `REBUILT_CH2_19_4_04_Q028`,
`REBUILT_CH2_19_4_05_Q001`, `REBUILT_CH2_19_4_05_Q002`, `REBUILT_CH2_19_4_05_Q003`, `REBUILT_CH2_19_4_05_Q005`, `REBUILT_CH2_19_4_05_Q006`, `REBUILT_CH2_19_4_05_Q007`, `REBUILT_CH2_19_4_05_Q009`, `REBUILT_CH2_19_4_05_Q010`, `REBUILT_CH2_19_4_05_Q011`, `REBUILT_CH2_19_4_05_Q015`, `REBUILT_CH2_19_4_05_Q018`, `REBUILT_CH2_19_4_05_Q019`, `REBUILT_CH2_19_4_05_Q022`, `REBUILT_CH2_19_4_05_Q024`, `REBUILT_CH2_19_4_05_Q025`, `REBUILT_CH2_19_4_05_Q026`, `REBUILT_CH2_19_4_05_Q027`, `REBUILT_CH2_19_4_05_Q028`, `REBUILT_CH2_19_4_05_Q029`,
`REBUILT_CH2_19_4_06_Q008`, `REBUILT_CH2_19_4_06_Q014`, `REBUILT_CH2_19_4_06_Q015`, `REBUILT_CH2_19_4_06_Q019`, `REBUILT_CH2_19_4_06_Q020`, `REBUILT_CH2_19_4_06_Q025`, `REBUILT_CH2_19_4_06_Q026`, `REBUILT_CH2_19_4_06_Q027`, `REBUILT_CH2_19_4_06_Q028`, `REBUILT_CH2_19_4_06_Q030`,
`REBUILT_CH2_19_4_07_Q001`, `REBUILT_CH2_19_4_07_Q005`, `REBUILT_CH2_19_4_07_Q007`, `REBUILT_CH2_19_4_07_Q008`, `REBUILT_CH2_19_4_07_Q015`, `REBUILT_CH2_19_4_07_Q018`, `REBUILT_CH2_19_4_07_Q021`, `REBUILT_CH2_19_4_07_Q024`, `REBUILT_CH2_19_4_07_Q028`,
`REBUILT_CH2_19_4_08_Q001`, `REBUILT_CH2_19_4_08_Q002`, `REBUILT_CH2_19_4_08_Q011`, `REBUILT_CH2_19_4_08_Q014`, `REBUILT_CH2_19_4_08_Q015`, `REBUILT_CH2_19_4_08_Q016`, `REBUILT_CH2_19_4_08_Q021`, `REBUILT_CH2_19_4_08_Q030`,
`REBUILT_CH2_19_4_09_Q001`, `REBUILT_CH2_19_4_09_Q003`, `REBUILT_CH2_19_4_09_Q008`, `REBUILT_CH2_19_4_09_Q012`, `REBUILT_CH2_19_4_09_Q014`, `REBUILT_CH2_19_4_09_Q016`, `REBUILT_CH2_19_4_09_Q029`,
`REBUILT_CH2_19_5_01_Q004`, `REBUILT_CH2_19_5_01_Q006`, `REBUILT_CH2_19_5_01_Q014`, `REBUILT_CH2_19_5_01_Q015`,
`REBUILT_CH2_19_6_01_Q010`, `REBUILT_CH2_19_6_01_Q013`

## 修复明细

| question_id | 修复前问题 | 修复后学生题方向 | 答案改动 | point keys 改动 | supporting theory |
|---|---|---|---|---|---|
| IDEAL_CH2_19_3_03_Q004 | 题干含“要求学生”的题库口吻 | 改为实验任务中需要给出的内容判断 | 否 | 否 | 否 |
| IDEAL_CH2_19_3_03_Q009 | 解析含“手机端输入稳定” | 改为 SO₂ 安全操作与通风橱必要性解释 | 否 | 否 | 否 |
| IDEAL_CH2_19_3_03_Q022 | 解析含“手机端输入稳定” | 改为 SO₂ 漂白作用的实验现象解释 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q001 | 可见字段含“点位” | 改为氯水处理后干扰与检验环节判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q003 | 可见字段含“点位” | 改为硫代硫酸根检验操作目的判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q004 | 解析含移动端/输入稳定性 | 改为氯水氧化后硫酸根验证的化学解释 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q008 | 解析含移动端/输入稳定性 | 改为沉淀或离子检验现象的客观判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q010 | 选项含“考查”命题口吻 | 改为反应体现的实验性质判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q012 | 可见字段含“点位” | 改为氯水处理步骤中的操作意义判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q013 | 可见字段含“点位” | 改为该实验观察环节的结果判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_04_Q014 | 题干讨论“题目问什么” | 改为氯水处理 Na₂S₂O₃ 后验证 SO₄²⁻ 的实验意义 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q015 | 可见字段含“点位” | 改为氧化处理与硫酸根检验关系判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q016 | 可见字段含“点位” | 改为实验步骤与现象对应判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_04_Q017 | 可见字段含“点位” | 改为操作环节中的离子检验判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_04_Q018 | 可见字段含“点位” | 改为该组观察对应的化学结论 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q020 | 可见字段含“点位” | 改为实验环节间的证据链判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q023 | 可见字段含“点位” | 改为硫代硫酸根被氧化后的验证逻辑 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q027 | 可见字段含“点位” | 改为实验现象与离子结论匹配 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q028 | 可见字段含“点位” | 改为干扰排除与确认检验的顺序判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q029 | 选项含“让学生” | 改为实验任务内容本身的选择 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_04_Q030 | 题干含“若学生” | 改为直接的操作或结论判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q003 | 解析含移动端/判分稳定性 | 改为 K₂S₂O₈ 氧化性实验结论解释 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q007 | 选项含“本点位” | 改为“该组观察”的实验语义 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q010 | 可见字段含“点位” | 改为过二硫酸根性质判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_05_Q011 | 可见字段含“点位” | 改为反应对象与现象对应判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_05_Q013 | 可见字段含“点位” | 改为 Mn²⁺ 体系观察判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_05_Q014 | 可见字段含“点位” | 改为酸性 KI 体系观察判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q016 | 可见字段含“点位” | 改为氧化还原产物和现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q017 | 可见字段含“点位” | 改为实验条件对反应的影响判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q025 | 可见字段含“点位” | 改为观察体系与结论的对应判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_05_Q028 | 可见字段含“点位” | 改为该操作或现象的实验意义判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_05_Q030 | 题干含“从点位看” | 改为比较 MnSO₄ 对照和酸性 KI 两类对象体现的核心性质 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_06_Q004 | 题干/解析含“考查、手机端、判分” | 改为 Ag⁺ 促进/催化 K₂S₂O₈ 氧化 Mn²⁺ 的实验判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_3_06_Q009 | 解析含“无需学生输入化学式” | 改为实验现象与催化判断解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_3_06_Q027 | 题干含“只要题干明确比较” | 改为比较加 AgNO₃ 与不加 AgNO₃ 两支试管时应关注的观察体系 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q002 | 解析含“题目只考查” | 改为 NaNO₂ 与酸生成 HNO₂ 的实验条件解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q003 | 题干含“点位 1” | 改为 NaNO₂/H₂SO₄ 预冷操作判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q008 | 可见字段含“点位” | 改为亚硝酸生成与温度控制判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q012 | 可见字段含“点位” | 改为 HNO₂ 不稳定性的实验判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q020 | 题干含“若学生” | 改为实验操作目的判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q022 | 可见字段含“点位” | 改为该反应现象与产物判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q027 | 可见字段含“点位” | 改为预冷、加酸和观察关系判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q028 | 题干含“安全考查” | 改为实验安全操作判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q029 | 可见字段含“点位” | 改为 HNO₂ 制备条件与现象判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_01_Q030 | 题干/选项含“可考、考查范围” | 改为实验范围内的操作结论判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_02_Q005 | 解析含“点位” | 改为亚硝酸分解或气体生成现象解释 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_02_Q006 | 题干含“考查” | 改为反应体现的化学性质判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_02_Q019 | 解析含“点位” | 改为实验现象对应的反应判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_02_Q028 | 题干/选项含“边界判断、只考” | 改为实验能推出的结论范围判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_02_Q029 | 题干含“最稳妥判断点” | 改为最关键判断依据 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_03_Q029 | 题干含“哪些内容最稳妥” | 改为哪些内容最符合该实验 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_03_Q030 | 题干含“可发布” | 改为本实验最简洁的化学结论判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_04_Q027 | 题干含“如果题目只问” | 改为 CCl₄ 层呈紫色对应的亚硝酸根检验方法 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_04_Q028 | 题干含“如果题目只问” | 改为对氨基苯磺酸和萘胺共同参与显色对应的检验方法 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_05_Q001 | 可见字段含“点位” | 改为 HNO₂ 氧化性实验现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q002 | 可见字段含“点位” | 改为 HNO₂ 还原性实验现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q003 | 可见字段含“点位” | 改为氧化还原角色辨析 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q005 | 可见字段含“点位” | 改为酸性条件下亚硝酸反应判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q006 | 可见字段含“点位” | 改为反应现象与氧化性对应 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q007 | 可见字段含“点位” | 改为反应现象与还原性对应 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q009 | 可见字段含“点位” | 改为两类体系对照判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q010 | 可见字段含“点位” | 改为 HNO₂ 双重性质判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q011 | 可见字段含“点位” | 改为产物或颜色变化判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q015 | 可见字段含“点位” | 改为还原性实验中的观察依据 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q018 | 可见字段含“点位” | 改为氧化性和还原性比较 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q019 | 可见字段含“点位” | 改为试剂作用与现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q022 | 可见字段含“点位” | 改为实验环节中的结论判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q024 | 可见字段含“点位” | 改为酸性亚硝酸体系的性质判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q025 | 题干含“设计一道题” | 改为同时说明 HNO₂ 氧化性和还原性的实验比较 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q026 | 可见字段含“点位” | 改为实验现象和反应角色判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q027 | 可见字段含“点位” | 改为两组反应中的 HNO₂ 作用判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q028 | 可见字段含“点位” | 改为干扰辨析或结论边界判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_05_Q029 | 题干含比较题库化口吻 | 改为比较 HNO₂ 在两个体系中的氧化还原角色 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q008 | 选项含“考查点” | 改为“实验内容”范围判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q014 | 可见字段含“点位” | 改为亚硝酸盐反应现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q015 | 可见字段含“点位” | 改为该反应操作或现象判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_06_Q019 | 可见字段含“点位” | 改为产物验证与观察判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q020 | 可见字段含“点位” | 改为反应步骤目的判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q025 | 可见字段含“点位” | 改为实验环节中的证据判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q026 | 可见字段含“点位” | 改为操作链与结论判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q027 | 可见字段含“点位” | 改为观察现象和产物验证判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q028 | 可见字段含“点位” | 改为实验步骤间因果关系判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_06_Q030 | 可见字段含“点位” | 改为反应整体结论判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_07_Q001 | 解析含“点位” | 改为硝酸根棕色环检验步骤解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_07_Q005 | 解析含“点位” | 改为 FeSO₄ 与浓硫酸操作意义解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_07_Q007 | 题干含“点位” | 改为棕色环检验现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_07_Q008 | 题干含“点位” | 改为硝酸根检验步骤判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_07_Q015 | 解析含“点位” | 改为检验操作与现象关系解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_07_Q018 | 题干含“点位” | 改为棕色环形成条件判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_07_Q021 | 解析含“点位” | 改为硝酸根验证依据解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_07_Q024 | 解析含“点位” | 改为检验方法边界解释 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_07_Q028 | 题干含“题目问” | 改为直接判断棕色环检验的操作要点 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q001 | 选项/解析含可见 ASCII 数字公式 | 改为七水合硫酸亚铁、硝酸钠、浓硫酸等中文试剂名判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q002 | 题干/选项/解析含可见 ASCII 数字公式 | 改为七水合硫酸亚铁、硝酸钠、浓硫酸的操作顺序判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q011 | 选项含可见 ASCII 数字公式 | 改为棕色环实验试剂组合的中文表述 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q014 | 题干含“判断点”口吻 | 改为判断是否检出硝酸根时最有判据价值的现象 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q015 | 题干/选项/解析含可见 ASCII 数字公式 | 改为浓硫酸必要性和亚铁来源的中文试剂名判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_08_Q016 | 题干含可见 ASCII 数字公式 | 改为棕色环实验试剂组合的中文表述 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q021 | 题干/解析含可见 ASCII 数字公式 | 改为七水合硫酸亚铁与硝酸钠的试剂角色判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_08_Q030 | 题干含题库式总结口吻，选项含可见 ASCII 数字公式 | 改为关于硝酸根棕色环检验的不恰当结论判断，并用中文试剂名 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_09_Q001 | 选项/解析含可见 ASCII 数字公式 | 改为提供亚铁离子的中文试剂名判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_09_Q003 | 题干/选项含可见 ASCII 数字公式 | 改为浓硫酸作用和亚铁来源的中文试剂名判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_09_Q008 | 选项/解析含可见 ASCII 数字公式 | 改为棕色环检验试剂组合的中文试剂名判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_09_Q012 | 题干含“可发布结论” | 改为实验可推出的化学结论 | 否 | 否 | 是 |
| REBUILT_CH2_19_4_09_Q014 | 题干含“要求学生” | 改为试剂或现象对应判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_09_Q016 | 题干含可见 ASCII 数字公式 | 改为硝酸根棕色环检验试剂组合的中文表述 | 否 | 否 | 否 |
| REBUILT_CH2_19_4_09_Q029 | 题干含“若学生” | 改为直接的硝酸盐热分解现象判断 | 否 | 否 | 是 |
| REBUILT_CH2_19_5_01_Q004 | 题干含“CaCl₂ 点位” | 改为 CaCl₂ 固体在水玻璃实验中的作用判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_5_01_Q006 | 题干/解析含“硫酸盐点位” | 改为硫酸盐固体在实验中的作用或现象判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_5_01_Q014 | 题干含“可发布结论” | 改为水中花园实验可得出的结论 | 否 | 否 | 是 |
| REBUILT_CH2_19_5_01_Q015 | 题干含“若学生” | 改为直接的现象与原理判断 | 否 | 否 | 否 |
| REBUILT_CH2_19_6_01_Q010 | 解析含“四个点位” | 改为四个实验环节的操作链解释 | 否 | 否 | 是 |
| REBUILT_CH2_19_6_01_Q013 | 题干含“可发布操作结论” | 改为燃烧产物处理的操作结论判断 | 否 | 否 | 否 |

## 保留但说明理由

| question_id | 命中词/字段 | 保留理由 |
|---|---|---|
| IDEAL_CH2_19_3_03_Q002 | 解析中的“设计分离步骤”语义 | 教材任务要求设计分离步骤，属于实验方案设计，不是题库审查语言。 |
| IDEAL_CH2_19_3_03_Q003 | 题干中的“检出设计” | 指实验检出方案设计，学生判断的是化学实验方案。 |
| IDEAL_CH2_19_3_03_Q004 | 解析中的“设计分离步骤”语义 | 已移除题干“要求学生”，保留部分是教材实验设计要求。 |
| IDEAL_CH2_19_3_03_Q006 | 解析和选项 D 的“设计分离步骤” | 判断是否需要分离步骤是实验设计内容，不是出题审查内容。 |
| IDEAL_CH2_19_3_03_Q024 | 解析中的“设计分离步骤” | 语义指实验分离方案，与教材实验任务一致。 |
| REBUILT_CH2_19_3_06_Q023 | 解析中的“对照设计” | 指加 AgNO₃ 与不加 AgNO₃ 的对照实验设计，保留。 |
| REBUILT_CH2_19_5_01_Q013 | 题干中的“观察设计” | 指“水中花园”实验如何观察现象，属于实验观察方案。 |

## 验证结果

- JSON parse：通过，15 个 rebuilt JSON 均可解析。
- 题数：450，与 chunk_2 总题数一致。
- 题型结构：
  - single_choice：287
  - true_false：103
  - fill_blank：60
- 单选 answer/options/option_links：通过，未发现 answer 标签缺失、选项标签不匹配或 option_links 标签越界。
- RAG id：通过，检查 canonical ids 494 个、supporting ids 432 个，均可在两个证据源中定位。
- 无 raw id：通过，学生可见字段未检出 raw id 或内部 token。
- 无 ASCII 数字公式：通过，学生可见字段未检出可见 ASCII 数字公式。
- 无 ASCII 价态：通过，学生可见字段未检出 ASCII 价态。
- 无中文异常空格：通过。
- 无学生可见审查语言：通过，blocking hits 为 0。
- duplicate stem groups：0。
- warnings：0。
- errors：0。

## 写入文件

- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-03_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-04_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-05_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-06_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-01_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-02_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-03_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-04_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-05_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-06_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-07_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-08_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-09_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-5-01_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-6-01_rebuilt_v1.json`
- `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_2\chunk_2_student_facing_demeta_polish_report.md`
