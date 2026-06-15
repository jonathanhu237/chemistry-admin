# 19-3-02 rebuild report

## Packet

- chunk: chunk_1
- packet: 19-3-02
- rebuilt JSON: `rebuilt_packages/chunk_1/19-3-02_rebuilt_v1.json`
- source packet: `semantic_work_packets/chunk_1/19-3-02.json`
- release JSON was not modified.

## Counts

- total questions: 30
- single_choice: 19
- true_false: 8
- fill_blank: 3
- keep: 19
- rewrite: 11
- reject: 0

## RAG Evidence IDs

- `expchunk_00228_5e99fe31b9`: 二氧化硫性质实验；酸性 KMnO₄ 体系对应还原性，饱和硫化氢水溶液体系对应氧化性，品红溶液体系对应漂白作用。
- `textbook_prose_00339_d6cda7bf18`: 二氧化硫中硫为中间价态，既有还原性又有氧化性。
- `textbook_prose_00340_77f9d61c94`: 二氧化硫还原性实例，并引出遇强还原剂时表现氧化性。
- `textbook_prose_00341_44241a0b9e`: 二氧化硫与硫化氢反应生成单质硫和水。
- `textbook_prose_00344_07bf4af806`: 二氧化硫可与有机色素分子结合形成无色物质，可用作漂白剂。

## Rewrite List

- Q010: 重写为三类性质总览题，去除原选项中的无关 ASCII 公式干扰。
- Q015: 重写为“加热后颜色是否恢复”对应可逆特点，避免加入复杂机理。
- Q018: 重写为证据逻辑题，避免“完全无颜色变化也可证明”的错误判据。
- Q020: 重写为硫化氢体系的氧化还原理由题，而不只是背产物。
- Q021: 重写为品红漂白及加热恢复的操作选择题。
- Q022: 重写为酸性 KMnO₄ 颜色变化的证据归类题。
- Q023: 重写为“试剂体系—性质”配对题，明确 H₂S 点位。
- Q027: 由符号填空改为中文单选，避免“S/硫”判定漂移。
- Q028: 重写为三组体系交叉配对题。
- Q029: 由“还原剂”填空改为单选，降低表述差异风险。
- Q030: 由“恢复/复原”填空改为单选，限定为漂白可逆判断。

## Keep But Edge

- Q001, Q003, Q007, Q011, Q024: 保留为酸性 KMnO₄ 还原性锚点。
- Q002, Q004, Q008, Q013, Q019, Q025: 保留为 H₂S 体系氧化性及生成硫的锚点；生成硫由 `textbook_prose_00341_44241a0b9e` 支撑。
- Q005, Q006, Q009, Q012, Q014, Q017, Q026: 保留为品红漂白和加热恢复锚点。
- Q016: 保留为综合判断题，用于确认 SO₂ 既可表现还原性又可表现氧化性。
- 边缘风险：canonical 实验 chunk 对部分颜色细节只写“观察现象”，因此本轮尽量将题目收束到“体系—性质—证据归类”，不发布复杂颜色机理题。

## Evidence Insufficient

- none. 本 packet 发布题均有 RAG 证据支撑。

## Multipoint Questions

- Q005, Q006, Q010, Q016, Q017, Q021, Q028, Q030 涉及两个或三个 point 的交叉关系。
- 多点题的理由：本实验本身以三组体系对比 SO₂ 的还原性、氧化性和漂白作用，少量交叉题有助于防止只背单一试剂名。

## Fill Blank Risk

- Q024 accepted answers: 还原, 还原性。风险低，直接对应酸性 KMnO₄ 点位。
- Q025 accepted answers: 氧化, 氧化性。风险低，直接对应 H₂S 点位。
- Q026 accepted answers: 漂白, 漂白作用。风险低，直接对应品红点位。
- 原 Q027, Q029, Q030 的符号/多表述填空风险已通过改写为单选消除。

## Manual Reconstruction Statement

本 packet 已逐题人工阅读原题、选项、答案、解析、point keys、video_points 和 RAG 证据后重建；rebuilt JSON 与本报告不是脚本生成结果。脚本/命令仅用于只读检查、计数、RAG id 查找和 JSON 结构校验。


## Publish Blocker Polish Validation

- Scope: student-visible fields in this packet rebuilt JSON: stem, options[].text, explanation, fill_blank accepted_answers, and visible feedback-like fields if present.
- Fixed question_ids: Q005, Q015, Q021, Q027.
- Rules checked: internal process traces, ASCII digit-subscript formulas, ASCII charge/ion notation, caret/LaTeX/Markdown chemical notation, and visible process notes.
- Final remaining blockers in this packet: 0.
- Protected fields unchanged by this polish pass: question_id, point keys, option_links point keys, canonical/supporting evidence ids.
- Release JSON unchanged by this polish pass.
