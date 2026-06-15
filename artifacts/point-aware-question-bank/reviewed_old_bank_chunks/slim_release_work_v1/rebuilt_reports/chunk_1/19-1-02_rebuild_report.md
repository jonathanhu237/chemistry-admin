# 19-1-02 手工语义重建报告

## Packet

- chunk：chunk_1
- packet：19-1-02
- 标题：氯水、溴水、碘水氧化性差异的比较
- 输入：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_1\19-1-02.json`
- 输出 JSON：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_1\19-1-02_rebuilt_v1.json`
- 本次未修改任何 `chunk_X_release_final_v1.json`。

## Manual Statement

本包为逐题人工语义重建，不是脚本生成。重建时逐题核对了原题、选项、答案、解析、point key、video point、RAG canonical 实验文本与必要的无机化学理论文本。

## Counts

- 总题数：30
- 保留：19
- 重写：11
- 废弃：0
- 题型：18 道单选、10 道判断、2 道填空

## RAG Evidence

- `expchunk_00193_497eb97bd6`：实验目的，掌握卤素氧化性和卤素离子还原性。
- `expchunk_00199_8240477bff`：实验 19-1 卤素氧化性内容；本包对应“分别向氯水、溴水、碘水中滴加 Na₂S₂O₃ 溶液及饱和硫化氢水溶液，观察现象”。
- `textbook_prose_00030_522edfaa72`：同浓度下卤素单质氧化性顺序为 F₂ >> Cl₂ > Br₂ > I₂。
- `textbook_prose_00036_1c17542905`：卤素氧化 H₂S、硫代硫酸根等还原性物质；I₂ 与硫代硫酸盐反应产物不同于 Cl₂、Br₂。

## Rewrite List

- Q009：旧题答案方向可用，但 reviewer_note 串入“保密信钥匙”内容；重写为本实验范围边界题。
- Q017：旧题直接断言 Na₂S₂O₃ 体系氯水、溴水生成硫沉淀，RAG 支撑不足；重写为证据边界判断。
- Q019：旧题仅作卤素水名称判断，深度偏浅；重写为本实验比较对象判断。
- Q021：旧题“碘水只褪色无硫沉淀”证据不足；重写为 I₂ 与硫代硫酸盐产物差异题。
- Q022：重写措辞，将硫沉淀明确放入 H₂S 体系并由理论反应支撑。
- Q023：重写为两组体系共同支持 Cl₂ > Br₂ > I₂ 的证据链题。
- Q025：旧题依赖 Na₂S₂O₃ 体系硫沉淀断言；重写为观察记录与产物差异的稳妥写法。
- Q026：重写细化观察对象，将硫浑浊/沉淀主要归入 H₂S 体系。
- Q027：重写为同一还原性试剂下“现象与产物差异”推理题。
- Q028：重写为 H₂S 体系可观察记录题。
- Q030：重写为“两组体系现象 + 理论顺序”的证据类型题。

## Keep But Edge

- Q004：保留核心但修订选项文字，将“快慢和明显程度”扩为“褪色、沉淀和反应明显程度等现象”；教材只写“观察现象”，未逐项列出现象，因此解析以观察类型表达，不把具体硫沉淀套到 Na₂S₂O₃ 体系。
- Q005、Q014、Q023、Q030：需要 `textbook_prose_00030_522edfaa72` 支撑 Cl₂ > Br₂ > I₂ 的理论顺序。
- Q006、Q013、Q016、Q022、Q024、Q028、Q029：需要 `textbook_prose_00036_1c17542905` 支撑 H₂S 或硫代硫酸盐的还原性。

## Evidence Insufficient List

- 旧 Q017、Q021、Q025、Q027 中“Na₂S₂O₃ 体系氯水/溴水出现硫沉淀而碘水只褪色无沉淀”的可见现象，canonical 只给操作和观察要求，理论块只稳定支持硫代硫酸盐被氧化及 I₂ 产物不同，不能直接作为稳定教材证据；新版已改写。
- “硫化钠替代液”只出现在 video point 标题，canonical 实验文本为饱和硫化氢水溶液；新版题干优先使用 canonical 说法。

## Multipoint Bindings

- Q004、Q005、Q007、Q009、Q010、Q015、Q018、Q019、Q020、Q023、Q026、Q030 同时绑定 candidate-1 和 candidate-2，因为这些题讨论两组体系的共同设计、比较对象、实验边界或综合证据。
- 单体系题只绑定对应点位：Na₂S₂O₃ 体系绑定 candidate-1；H₂S 体系绑定 candidate-2。

## Fill Blank Risk

- Q024：答案为“还原/还原性”，中文短答案，风险低。
- Q029：答案为“还原/还原性”，中文短答案，风险低。
- 本包没有要求学生输入复杂公式或上下标；公式相关内容均放入单选或解析。

## Final Check

- 手工重建题数：30。
- 所有单选题均有 4 个选项和 option_links。
- 判断题不设选项，答案为布尔值。
- 填空题为 normalized exact 短中文答案。
- 未修改任何 release JSON。
