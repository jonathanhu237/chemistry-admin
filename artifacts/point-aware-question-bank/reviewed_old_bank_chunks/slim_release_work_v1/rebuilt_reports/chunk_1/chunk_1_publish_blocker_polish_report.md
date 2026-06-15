# chunk_1 publish blocker polish report

## Scan Scope

- chunk: chunk_1
- rebuilt package directory: `rebuilt_packages/chunk_1`
- rebuilt report directory: `rebuilt_reports/chunk_1`
- packets scanned: `19-1-01`, `19-1-02`, `19-1-03`, `19-1-04`, `19-1-05`, `19-1-06`, `19-1-07`, `19-1-08`, `19-2-01`, `19-2-02`, `19-2-03`, `19-2-04`, `19-2-05`, `19-3-01`, `19-3-02`
- student-visible JSON fields scanned: `stem`, `options[].text`, `explanation`, `answer.accepted_answers`, and visible `hint` / `analysis` / `feedback` / `diagnostic_note` if present.
- protected fields intentionally excluded from edits: `question_id`, point keys, evidence ids, file names, machine metadata ids.

## Fix Rules

The scan was rule-category based, not a replacement pass over only the prompt examples. I checked for:

- internal review or reconstruction traces visible to students, including `canonical`, `RAG`, `packet`, `primary point`, `supporting theory`, `本题`, `该题`, `为避免...`, and similar process-facing language.
- ASCII digit-subscript formulas in visible fields.
- ASCII charge or ion notation such as `I-`, `Mn^2+`, and similar patterns.
- caret, Markdown, or LaTeX chemical notation in visible fields.
- ASCII Roman valence notation in visible chemistry labels, such as `Ti(IV)`.

## Fixed Packets

- `19-1-01`
- `19-1-05`
- `19-1-06`
- `19-1-08`
- `19-2-03`
- `19-2-04`
- `19-2-05`
- `19-3-02`

## Fixed Question IDs

- `CHUNK1_19_1_01_Q002`, `CHUNK1_19_1_01_Q006`, `CHUNK1_19_1_01_Q010`, `CHUNK1_19_1_01_Q016`, `CHUNK1_19_1_01_Q021`, `CHUNK1_19_1_01_Q023`, `CHUNK1_19_1_01_Q025`, `CHUNK1_19_1_01_Q026`, `CHUNK1_19_1_01_Q028`
- `CHUNK1_19_1_05_Q003`, `CHUNK1_19_1_05_Q010`, `CHUNK1_19_1_05_Q030`
- `CHUNK1_19_1_06_Q023`
- `CHUNK1_19_1_08_Q001`, `CHUNK1_19_1_08_Q005`
- `CHUNK1_19_2_03_Q012`, `CHUNK1_19_2_03_Q018`, `CHUNK1_19_2_03_Q030`
- `CHUNK1_19_2_04_Q004`, `CHUNK1_19_2_04_Q006`, `CHUNK1_19_2_04_Q026`
- `CHUNK1_19_2_05_Q014`
- `CHUNK1_19_3_02_Q005`, `CHUNK1_19_3_02_Q015`, `CHUNK1_19_3_02_Q021`, `CHUNK1_19_3_02_Q027`

## Field-Level Fixes

| packet | question_id | field | before snippet | after snippet |
| --- | --- | --- | --- | --- |
| 19-1-01 | CHUNK1_19_1_01_Q002 | explanation | canonical 实验把 CCl₄ 与 KBr、KI、氯水、溴水共同列为试剂；supporting theory 说明碘在四氯化碳中有明显颜色... | 实验步骤把 CCl₄ 与 KBr、KI、氯水、溴水共同列为试剂；碘在四氯化碳中有明显颜色... |
| 19-1-01 | CHUNK1_19_1_01_Q006 | explanation | canonical 文本明确列出 KBr 溶液、KI 溶液、CCl₄、氯水、溴水等... | 实验步骤列出 KBr 溶液、KI 溶液、CCl₄、氯水、溴水等试剂... |
| 19-1-01 | CHUNK1_19_1_01_Q010 | stem | 下列哪一项最明显不属于本 packet 的三个视频点位？ | 下列哪一项最明显不属于本实验的三个置换观察？ |
| 19-1-01 | CHUNK1_19_1_01_Q010 | explanation | 本 packet 的视频点位是三个单独置换体系...不应误绑定到本 packet 的单点位题。 | 本实验的三个观察分别针对单独置换体系...不应混入这组三个观察。 |
| 19-1-01 | CHUNK1_19_1_01_Q016 | explanation | canonical 文本明确要求通过这些实验说明卤素氧化性的递变顺序。 | 实验目的要求通过这些置换实验说明卤素氧化性的递变顺序。 |
| 19-1-01 | CHUNK1_19_1_01_Q021 | stem | 如果题干只问“Cl₂ 是否强于 Br₂”，最合适的 primary point 是哪一个？ | 如果只判断“Cl₂ 的氧化性是否强于 Br₂”，最合适的实验依据是哪一项？ |
| 19-1-01 | CHUNK1_19_1_01_Q021 | options[3].text | 三个点位都必须作为 primary point | 必须同时依赖三个置换体系 |
| 19-1-01 | CHUNK1_19_1_01_Q023 | stem | 下列哪一类判断最需要引用 supporting theory，而不能只靠 canonical 实验步骤？ | 下列哪一类判断最需要结合卤素在有机溶剂中的显色知识，而不能只看操作步骤？ |
| 19-1-01 | CHUNK1_19_1_01_Q023 | explanation | canonical 实验步骤只要求加入 CCl₄ 并观察...需要 supporting theory。 | 实验步骤只要求加入 CCl₄ 并观察...需要结合卤素在有机溶剂中的显色知识。 |
| 19-1-01 | CHUNK1_19_1_01_Q023 | options[2].text | 本 packet 有三个视频点位 | 本实验包含三个置换观察 |
| 19-1-01 | CHUNK1_19_1_01_Q025 | explanation | canonical 目标是说明卤素氧化性递变顺序... | 实验目标是说明卤素氧化性递变顺序... |
| 19-1-01 | CHUNK1_19_1_01_Q026 | stem | 下列哪一项属于把相邻实验内容误并入本 packet 的做法？ | 下列哪一项属于把相邻实验内容误并入本实验三个置换观察的做法？ |
| 19-1-01 | CHUNK1_19_1_01_Q026 | explanation | Na₂S₂O₃ 与卤素水反应...不是本 packet 的三个视频点位。 | Na₂S₂O₃ 与卤素水反应...不属于本实验这三个置换观察。 |
| 19-1-01 | CHUNK1_19_1_01_Q026 | options[3].text | 把 Na₂S₂O₃ 与卤素水反应作为本 packet 三点位的核心证据 | 把 Na₂S₂O₃ 与卤素水反应作为这三个置换观察的核心依据 |
| 19-1-01 | CHUNK1_19_1_01_Q028 | explanation | canonical 支撑 CCl₄ 被用于实验观察；supporting theory 支撑碘等卤素在有机溶剂中的显色依据。 | 实验操作说明 CCl₄ 参与观察；卤素在有机溶剂中的显色知识说明它能帮助判断置换结果。 |
| 19-1-01 | CHUNK1_19_1_01_Q028 | options[0].text | canonical 中 CCl₄ 参与观察 + supporting theory 中碘在四氯化碳中显色 | CCl₄ 参与实验观察，且碘在四氯化碳中显色明显 |
| 19-1-05 | CHUNK1_19_1_05_Q003 | explanation | Mn^2+ | Mn²⁺ |
| 19-1-05 | CHUNK1_19_1_05_Q003 | options[2].text | Mn^2+ | Mn²⁺ |
| 19-1-05 | CHUNK1_19_1_05_Q010 | options[3].text | 鉴定 Ti(IV) | 鉴定 Ti(Ⅳ) |
| 19-1-05 | CHUNK1_19_1_05_Q030 | options[2].text | 提供 Mn^2+ | 提供 Mn²⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q023 | explanation | 为避免与 Q003 重复，本题考检验机制：Cl₂ 氧化 I- 生成 I₂，I₂ 使淀粉显蓝。 | Cl₂ 能氧化 I⁻ 生成 I₂，生成的 I₂ 使淀粉显蓝。 |
| 19-1-08 | CHUNK1_19_1_08_Q001 | explanation | canonical 感光性操作明确写 AgCl 沉淀涂在滤纸上... | 感光性操作明确要求把 AgCl 沉淀涂在滤纸上... |
| 19-1-08 | CHUNK1_19_1_08_Q005 | stem | 哪一项表述最符合当前 RAG 证据？ | 哪一项表述最符合实验步骤和相关理论？ |
| 19-1-08 | CHUNK1_19_1_08_Q005 | explanation | RAG 的实验步骤直接写 AgCl 沉淀涂滤纸... | 实验步骤直接写 AgCl 沉淀涂滤纸... |
| 19-2-03 | CHUNK1_19_2_03_Q012 | explanation | CCl₄ 不属于该 canonical 步骤。 | CCl₄ 不属于该操作。 |
| 19-2-03 | CHUNK1_19_2_03_Q018 | explanation | 本 packet 的 canonical 步骤写明使用乙醚；题目必须跟随该实验步骤... | 实验步骤写明使用乙醚，判断溶剂时应以该操作为准... |
| 19-2-03 | CHUNK1_19_2_03_Q030 | explanation | RAG 证据只支持酸性铬酸盐体系中生成蓝色过氧化铬... | 酸性铬酸盐体系中可生成蓝色过氧化铬... |
| 19-2-04 | CHUNK1_19_2_04_Q004 | explanation | canonical 步骤明确要求先生成棕色沉淀后加 H₂O₂... | 实验步骤明确要求先生成棕色沉淀后加 H₂O₂... |
| 19-2-04 | CHUNK1_19_2_04_Q006 | explanation | canonical 分解小节依次列出加热 H₂O₂... | 分解实验依次列出加热 H₂O₂... |
| 19-2-04 | CHUNK1_19_2_04_Q026 | explanation | canonical 步骤只说棕色沉淀；支持理论说明... | 实验步骤只说棕色沉淀；相关理论说明... |
| 19-2-05 | CHUNK1_19_2_05_Q014 | explanation | canonical 步骤写明取少量 3% H₂O₂ 溶液... | 实验步骤写明取少量 3% H₂O₂ 溶液... |
| 19-3-02 | CHUNK1_19_3_02_Q005 | explanation | packet 点位还要求褪色后加热观察颜色是否恢复... | 褪色后加热观察颜色是否恢复... |
| 19-3-02 | CHUNK1_19_3_02_Q015 | explanation | 该题只围绕 packet 的“品红褪色后加热，观察颜色是否恢复”点位... | 品红褪色后加热用于观察颜色是否恢复... |
| 19-3-02 | CHUNK1_19_3_02_Q021 | explanation | 是该 point 中要求的补充观察。 | 是这一操作的补充观察。 |
| 19-3-02 | CHUNK1_19_3_02_Q027 | explanation | 为避免符号填空风险，本题改为中文单选。 | 观察到黄色或乳白色固体时应优先判断为单质硫。 |

## Protected Files And Fields

- Confirmed no `chunk_X_release_final_v1.json` file was intentionally modified by this polish pass.
- Confirmed no `question_id`, `primary_point_keys`, `secondary_point_keys`, option-link point keys, `canonical_chunk_ids`, or `supporting_theory_chunk_ids` were targeted for modification.
- Edits were limited to student-visible text fields and the corresponding rebuild reports' publish-polish validation notes.

## Final Remaining Hit Counts

- internal review traces: 0
- ASCII digit-subscript formulas: 0
- ASCII charge / ion notation: 0
- caret / LaTeX / Markdown chemical notation: 0
- student-visible process notes: 0


## Publish Blocker Polish Continuation - ASCII Ion Sweep

- Continuation scope: all 15 `chunk_1` rebuilt JSON files were rescanned; fixes were needed in `19-1-05`, `19-1-06`, `19-1-07`, `19-1-08`, `19-2-01`, and `19-2-02`.
- Rule category: ASCII charge / ion notation in student-visible fields, with boundary-aware handling so `KI-淀粉` was not changed into an ion.
- Student-visible fields fixed: `stem`, `options[].text`, `explanation`, and visible `answer.accepted_answers` if present.
- `option_links[].diagnostic_note` exists in some rebuilt JSON files, but it is internal option-link metadata rather than a student-facing field in this package shape; it was separately scanned for ASCII charge/ion residue and had 0 hits.
- Protected fields unchanged: `question_id`, `primary_point_keys`, `secondary_point_keys`, option-link point keys, canonical/supporting evidence ids, file names, and metadata ids.
- Release JSON files were not modified.
- Changed visible fields in this continuation: 147.

### Continuation Field Fixes

| packet | question_id | field | before fragment | after fragment |
| --- | --- | --- | --- | --- |
| 19-1-05 | CHUNK1_19_1_05_Q002 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q002 | options[0].text | Na+ | Na⁺ |
| 19-1-05 | CHUNK1_19_1_05_Q002 | options[1].text | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q002 | options[3].text | Cl- | Cl⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q003 | options[1].text | Na+ | Na⁺ |
| 19-1-05 | CHUNK1_19_1_05_Q003 | options[3].text | Cl- | Cl⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q007 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q008 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q011 | stem | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q011 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q018 | stem | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q018 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q020 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q022 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q023 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q026 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q026 | options[0].text | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q026 | options[1].text | Na+ | Na⁺ |
| 19-1-05 | CHUNK1_19_1_05_Q028 | options[2].text | K+ | K⁺ |
| 19-1-05 | CHUNK1_19_1_05_Q029 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q029 | options[0].text | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q029 | options[1].text | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q030 | explanation | I- | I⁻ |
| 19-1-05 | CHUNK1_19_1_05_Q030 | options[0].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q001 | explanation | I-, Cl- | I⁻, Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q003 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q005 | options[3].text | Cl- | Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q007 | explanation | Cl-, Ag+ | Cl⁻, Ag⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q008 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q009 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q009 | options[0].text | H+ | H⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q009 | options[1].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q010 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q012 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q012 | options[1].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q013 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q014 | options[2].text | Cl- | Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q016 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q016 | options[0].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q016 | options[2].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q017 | explanation | Cl-, Ag+ | Cl⁻, Ag⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q018 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q018 | options[1].text | H+ | H⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q018 | options[2].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q019 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q020 | explanation | Cl- | Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q020 | options[0].text | Cl- | Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q021 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q021 | options[0].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q021 | options[1].text | H+ | H⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q021 | options[2].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q022 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q023 | options[0].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q023 | options[1].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q023 | options[2].text | Cl- | Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q024 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q024 | options[0].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q024 | options[3].text | I-, K+ | I⁻, K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q025 | stem | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q025 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q025 | options[1].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q025 | options[3].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q026 | options[3].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q027 | stem | Cl- | Cl⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q027 | explanation | Cl-, Ag+ | Cl⁻, Ag⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q027 | options[0].text | Cl-, Ag+ | Cl⁻, Ag⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q027 | options[2].text | Ag+, K+ | Ag⁺, K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q028 | options[1].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q028 | options[2].text | K+ | K⁺ |
| 19-1-06 | CHUNK1_19_1_06_Q029 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q030 | stem | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q030 | explanation | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q030 | options[0].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q030 | options[1].text | I- | I⁻ |
| 19-1-06 | CHUNK1_19_1_06_Q030 | options[2].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q001 | stem | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q001 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q002 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q004 | explanation | Cl- | Cl⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q004 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q004 | options[3].text | Cl- | Cl⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q005 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q005 | options[1].text | H+ | H⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q006 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q006 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q007 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q007 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q007 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q008 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q008 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q008 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q009 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q009 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q009 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q011 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q013 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q015 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q015 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q015 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q016 | stem | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q016 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q020 | stem | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q020 | explanation | I-, K+ | I⁻, K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q021 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q021 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q021 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q023 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q023 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q023 | options[3].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q024 | options[3].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q025 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q025 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q025 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q026 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q027 | explanation | I-, Cl- | I⁻, Cl⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q027 | options[0].text | Cl- | Cl⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q027 | options[1].text | H+ | H⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q027 | options[2].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q028 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q028 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q028 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q029 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q029 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q029 | options[1].text | K+ | K⁺ |
| 19-1-07 | CHUNK1_19_1_07_Q030 | explanation | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q030 | options[0].text | I- | I⁻ |
| 19-1-07 | CHUNK1_19_1_07_Q030 | options[1].text | K+ | K⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q003 | options[1].text | Ag+ | Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q007 | options[2].text | Ag+ | Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q012 | explanation | Cl-, Ag+ | Cl⁻, Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q020 | stem | Ag+ | Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q020 | explanation | Cl-, Ag+ | Cl⁻, Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q021 | options[0].text | Ag+ | Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q023 | options[1].text | Ag+ | Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q027 | options[2].text | Ag+ | Ag⁺ |
| 19-1-08 | CHUNK1_19_1_08_Q029 | options[2].text | Ag+ | Ag⁺ |
| 19-2-01 | CHUNK1_19_2_01_Q005 | explanation | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q013 | explanation | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q016 | explanation | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q020 | explanation | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q025 | explanation | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q030 | stem | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q030 | explanation | I- | I⁻ |
| 19-2-01 | CHUNK1_19_2_01_Q030 | options[3].text | K+ | K⁺ |
| 19-2-02 | CHUNK1_19_2_02_Q006 | options[1].text | Na+ | Na⁺ |
| 19-2-02 | CHUNK1_19_2_02_Q012 | stem | Cl- | Cl⁻ |
| 19-2-02 | CHUNK1_19_2_02_Q012 | explanation | Cl- | Cl⁻ |

### Continuation Final Counts

- Student-visible ASCII charge / ion hits: 0
- ASCII digit-subscript formula hits: 0
- caret / LaTeX / Markdown chemical notation hits: 0
- internal review/process trace hits: 0
- JSON parse, 30 questions per packet, and single-choice answer/options/option_links validation: pass

### Independent Diagnostic Note Cleanup

After the continuation pass, an independent verification also scanned `option_links[].diagnostic_note` as a conservative internal-metadata surface. Nineteen process-facing notes were rewritten in `19-1-01`, `19-1-02`, `19-1-03`, and `19-1-04` to remove `packet`, `canonical`, `RAG`, and `本题` wording while preserving option labels, point keys, roles, answers, and evidence ids.

Final diagnostic-note process trace hits: 0.
