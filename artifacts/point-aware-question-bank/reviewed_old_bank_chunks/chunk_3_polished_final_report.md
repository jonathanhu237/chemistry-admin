# chunk_3 polished_final_v1 终稿打磨报告

## 总览
- 总题数：450
- keep：401
- rewrite：49
- reject：0
- 输出 JSON：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_3_polished_final_v1.json`
- 基于输入：`E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_3_semantic_final_v1.json`
- 内部校验：通过

## 本轮修改过的题目列表
本轮主要修改包括：去重 proposed_question、把最差手机端填空风险改写为单选/判断、收窄 supporting theory、重写有效单选 option_links。
| review_id | 实验编号 | 修改类型 | 原因 |
| --- | --- | --- | --- |
| OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | 19-6-02 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_01_Q030_R1_PF1 | 19-8-01 | single_choice -> true_false | polished_proposed_dedupe |
| OLD_CHUNK3_EXP_19_8_02_Q022_PF1 | 19-8-02 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_03_Q023_PF1 | 19-8-03 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_04_Q030_PF1 | 19-8-04 | fill_blank -> true_false | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_06_Q025_PF1 | 19-8-06 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_07_Q024_PF1 | 19-8-07 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_08_Q025_PF1 | 19-8-08 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_09_Q028_PF1 | 19-8-09 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_10_Q027_PF1 | 19-8-10 | fill_blank -> single_choice | polished_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_11_Q007_R1_PF1 | 19-8-11 | single_choice -> single_choice | polished_proposed_dedupe |
| OLD_CHUNK3_EXP_19_8_11_Q019_R1_PF1 | 19-8-11 | true_false -> true_false | polished_proposed_dedupe |
| OLD_CHUNK3_EXP_19_8_11_Q020_R1_PF1 | 19-8-11 | true_false -> true_false | polished_proposed_dedupe |
| OLD_CHUNK3_EXP_19_8_11_Q026_R1_PF1 | 19-8-11 | fill_blank -> single_choice | polished_proposed_dedupe_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | 19-8-11 | fill_blank -> single_choice | polished_proposed_dedupe_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_19_8_11_Q028_R1_PF1 | 19-8-11 | fill_blank -> true_false | polished_proposed_dedupe_mobile_fill_rewrite |
| OLD_CHUNK3_EXP_20_1_01_Q024_PF1 | 20-1-01 | fill_blank -> single_choice | polished_mobile_fill_rewrite |

## proposed 去重修复列表
已修复 semantic_final_v1 中 4 组重复 proposed stem；Q006/Q015 等保留为不同角度的总体证据链题，重复项改成对象、步骤意图、沉淀依据或省略后果。
| review_id | 实验编号 | 新的 proposed_question.stem |
| --- | --- | --- |
| OLD_CHUNK3_EXP_19_8_01_Q030_R1_PF1 | 19-8-01 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，只让 Pb(OH)₂ 沉淀与 HNO₃ 作用，而不再比较其与过量 NaOH 的作用，不能充分体现两性氢氧化物的判断。 |
| OLD_CHUNK3_EXP_19_8_11_Q007_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，Pb₃O₄ 与 HNO₃ 微热后，为什么还要吸取清液并用稀 H₂SO₄ 检查？ |
| OLD_CHUNK3_EXP_19_8_11_Q019_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，用稀 H₂SO₄ 检查的是 HNO₃ 处理后清液中的 Pb²⁺，不是 SbCl₃ 与 Bi(NO₃)₃ 的分离鉴定步骤。 |
| OLD_CHUNK3_EXP_19_8_11_Q020_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，若省去清液的稀 H₂SO₄ 检查，仅凭 Pb₃O₄ 与 HNO₃ 微热不能完成 Pb²⁺ 证据确认。 |
| OLD_CHUNK3_EXP_19_8_11_Q026_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 检查 Pb²⁺ 时，最关键的可观察依据是哪一项？ |
| OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，吸取清液而不是直接处理残渣，更接近哪一项实验意图？ |
| OLD_CHUNK3_EXP_19_8_11_Q028_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 步骤的判断对象是清液中的 Pb²⁺，而不是检验 HNO₃ 本身。 |

## option_links 手修摘要
- 有效单选题：164 道；所有有效单选的 option_links 已按选项数量重写。
- `correct_evidence` 指向本题真实支撑点位；`adjacent_point` 只在同实验真实相邻点位时使用；跨实验干扰统一标为 `adjacent_experiment` 或具体误概念。
- 高风险修正题如下，主要为本轮新改写题、semantic_final_v1 rewrite 题和含相邻点位/跨实验干扰的单选题。
| review_id | 实验编号 | 题干摘要 |
| --- | --- | --- |
| OLD_CHUNK3_EXP_19_6_02_Q003 | 19-6-02 | 在《19-6-02 金属镁燃烧》实验中，镁燃烧时最典型的现象是哪一项？ |
| OLD_CHUNK3_EXP_19_6_02_Q006 | 19-6-02 | 在《19-6-02 金属镁燃烧》实验中，镁在空气中燃烧时，主要氧化镁的氧化剂是哪一种？ |
| OLD_CHUNK3_EXP_19_6_02_Q007 | 19-6-02 | 在《19-6-02 金属镁燃烧》实验中，观察镁燃烧时最应避免的做法是哪一项？ |
| OLD_CHUNK3_EXP_19_6_02_Q010 | 19-6-02 | 在《19-6-02 金属镁燃烧》实验中，镁燃烧后收集到的氧化镁通常呈什么颜色？ |
| OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | 19-6-02 | 在《19-6-02 金属镁燃烧》实验中，与其让学生直接填写 O₂，更能体现本实验观察目的的是哪一项？ |
| OLD_CHUNK3_EXP_19_6_03_Q008 | 19-6-03 | 在《19-6-03 与水的作用》实验中，下列金属与水反应最剧烈的一般是？ |
| OLD_CHUNK3_EXP_19_6_04_Q003 | 19-6-04 | 在《19-6-04 焰色反应》实验中，K⁺ 焰色常需透过哪种材料观察以减弱钠黄光干扰？ |
| OLD_CHUNK3_EXP_19_6_04_Q004 | 19-6-04 | 在《19-6-04 焰色反应》实验中，Na⁺ 的典型焰色是什么？ |
| OLD_CHUNK3_EXP_19_6_04_Q006 | 19-6-04 | 在《19-6-04 焰色反应》实验中，Ca²⁺ 的焰色通常可描述为哪一种？ |
| OLD_CHUNK3_EXP_19_6_04_Q007 | 19-6-04 | 在《19-6-04 焰色反应》实验中，Sr²⁺ 的焰色通常可描述为哪一种？ |
| OLD_CHUNK3_EXP_19_6_04_Q008 | 19-6-04 | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色通常可描述为哪一种？ |
| OLD_CHUNK3_EXP_19_8_01_Q001 | 19-8-01 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，生成 Pb(OH)₂ 时，向 Pb(NO₃)₂ 溶液中滴加的是哪种溶液？ |
| OLD_CHUNK3_EXP_19_8_01_Q002_R1 | 19-8-01 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，将 Pb(OH)₂ 沉淀分别与 HNO₃ 和过量 NaOH 作用，最主要是为了判断 |
| OLD_CHUNK3_EXP_19_8_01_Q003 | 19-8-01 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，生成的 Pb(OH)₂ 沉淀分别要与哪两种 2 mol·L⁻¹ 溶液作用？ |
| OLD_CHUNK3_EXP_19_8_02_Q001 | 19-8-02 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 沉淀时，常向 SnCl₂ 溶液中加入哪种试剂？ |
| OLD_CHUNK3_EXP_19_8_02_Q006 | 19-8-02 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，下列哪一组最符合本实验试剂？ |
| OLD_CHUNK3_EXP_19_8_02_Q022_PF1 | 19-8-02 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 后，继续分别加入 HCl 和过量 NaOH，最主要是为了判断 |
| OLD_CHUNK3_EXP_19_8_03_Q002 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，由 SbCl₃ 生成 Sb(OH)₃ 沉淀时加入的碱是哪一种？ |
| OLD_CHUNK3_EXP_19_8_03_Q004 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 酸性溶解行为时加入的酸是哪一种？ |
| OLD_CHUNK3_EXP_19_8_03_Q005 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中的性质时加入的强碱是哪一种？ |
| OLD_CHUNK3_EXP_19_8_03_Q007 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，与 2 mol·L⁻¹ NaOH 相比，6 mol·L⁻¹ NaOH 在该实验中主 |
| OLD_CHUNK3_EXP_19_8_03_Q023_PF1 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 生成 Sb(OH)₃ 后，继续比较 HCl、2 mol/ |
| OLD_CHUNK3_EXP_19_8_03_Q030_SF1 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，下列哪一组是生成 Sb(OH)₃ 沉淀的直接试剂组合？ |
| OLD_CHUNK3_EXP_19_8_04_Q001 | 19-8-04 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，生成 Bi(OH)₃ 沉淀时，通常向 Bi(NO₃)₃ 溶液中滴加哪种试剂？ |
| OLD_CHUNK3_EXP_19_8_04_Q005 | 19-8-04 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，实验还比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和哪种更浓碱的作用？ |
| OLD_CHUNK3_EXP_19_8_04_Q006 | 19-8-04 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，若 Bi(OH)₃ 在过量 NaOH 中不明显溶解，说明它与 Sn、Pb、Sb 的 |
| OLD_CHUNK3_EXP_19_8_04_Q009 | 19-8-04 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，下列哪项最能体现 Bi(OH)₃ 的“生成”？ |
| OLD_CHUNK3_EXP_19_8_04_Q024_SF1 | 19-8-04 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和更强 NaOH 条件的作 |
| OLD_CHUNK3_EXP_19_8_05_Q001 | 19-8-05 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sn(OH)₂ 时向 SnCl₂ 溶液滴加的碱是 |
| OLD_CHUNK3_EXP_19_8_05_Q002 | 19-8-05 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Pb(OH)₂ 时使用的铅盐溶液是哪一种？ |
| OLD_CHUNK3_EXP_19_8_05_Q003 | 19-8-05 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sb(OH)₃ 时使用的锑盐溶液是哪一种？ |
| OLD_CHUNK3_EXP_19_8_05_Q005 | 19-8-05 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，检验 Sn(OH)₂ 酸碱性时，沉淀需分别试验与哪两类 |
| OLD_CHUNK3_EXP_19_8_05_Q007 | 19-8-05 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 随 NaOH 增多可溶解，体现其哪种酸 |
| OLD_CHUNK3_EXP_19_8_05_Q009 | 19-8-05 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sb(OH)₃ 步骤中特意比较 2 mol·L⁻¹ 与 |
| OLD_CHUNK3_EXP_19_8_06_Q001 | 19-8-06 | 在《19-8-06 Sn(II) 的还原性》实验中，检验 Sn(II) 还原 Fe³⁺ 的实验中，向 FeCl₃ 溶液滴加的是哪种溶液？ |
| OLD_CHUNK3_EXP_19_8_06_Q008 | 19-8-06 | 在《19-8-06 Sn(II) 的还原性》实验中，用 KSCN 检验 Fe³⁺ 时，若 Fe³⁺ 明显存在，常见现象是哪一项？ |
| OLD_CHUNK3_EXP_19_8_06_Q010 | 19-8-06 | 在《19-8-06 Sn(II) 的还原性》实验中，下列哪一组属于该实验的主要反应对象？ |
| OLD_CHUNK3_EXP_19_8_06_Q025_PF1 | 19-8-06 | 在《19-8-06 Sn(II) 的还原性》实验中，SnCl₂ 与 HgCl₂ 反应中先出现白色沉淀、过量 SnCl₂ 时可继续变暗，这组现 |
| OLD_CHUNK3_EXP_19_8_07_Q007 | 19-8-07 | 在《19-8-07 Pb(IV) 的氧化性》实验中，下列哪项属于本实验的正确操作组合？ |
| OLD_CHUNK3_EXP_19_8_07_Q024_PF1 | 19-8-07 | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂、H₂SO₄ 和 MnSO₄ 水浴加热后若出现紫色，最直接说明哪一判断？ |
| OLD_CHUNK3_EXP_19_8_08_Q002 | 19-8-08 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，碱性体系中用于比较还原性的强氧化剂是哪一种？ |
| OLD_CHUNK3_EXP_19_8_08_Q003 | 19-8-08 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，代表 As(III) 参与比较的氯化物是哪一种？ |
| OLD_CHUNK3_EXP_19_8_08_Q007 | 19-8-08 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水，主要 |
| OLD_CHUNK3_EXP_19_8_08_Q021_R1 | 19-8-08 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，分别把 As(III)、Sb(III)、Bi(III) |
| OLD_CHUNK3_EXP_19_8_08_Q025_PF1 | 19-8-08 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，Bi(NO₃)₃ 在本实验中主要出现在下列哪组 Bi( |
| OLD_CHUNK3_EXP_19_8_09_Q003 | 19-8-09 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，加入 CCl₄ 的主要目的是什么？ |
| OLD_CHUNK3_EXP_19_8_09_Q005 | 19-8-09 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验还列出高价砷、锑、铋分别与哪种酸性体系反应？ |
| OLD_CHUNK3_EXP_19_8_09_Q010 | 19-8-09 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，下列哪项不是本实验的合理内容？ |
| OLD_CHUNK3_EXP_19_8_09_Q028_PF1 | 19-8-09 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，酸性 MnSO₄ 体系出现紫色，更能说明哪一类证据？ |
| OLD_CHUNK3_EXP_19_8_10_Q001 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，检验 Sn(II) 还原性时，向 HgCl₂ 溶液中滴加的试剂是哪一 |
| OLD_CHUNK3_EXP_19_8_10_Q002 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，SnCl₂ 与 FeCl₃ 反应后，可用哪种试剂检验 Fe³⁺ 是否 |
| OLD_CHUNK3_EXP_19_8_10_Q003 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，Pb(IV) 氧化性实验中常用的固体铅化合物是哪一种？ |
| OLD_CHUNK3_EXP_19_8_10_Q006 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，Bi(III) 还原性相关步骤中，向 Bi(NO₃)₃ 溶液滴加 N |
| OLD_CHUNK3_EXP_19_8_10_Q010 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，本实验围绕 Sn、Pb、Bi 的不同价态，核心比较的是哪类性质？ |
| OLD_CHUNK3_EXP_19_8_10_Q027_PF1 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，加入 KI 和 CCl₄ 后出现紫色有机层，在本实验中最直接支持哪一 |
| OLD_CHUNK3_EXP_19_8_11_Q003 | 19-8-11 | 在《19-8-11 小设计实验》中，吸取 Pb₃O₄ 与 HNO₃ 作用后的清液后，用于检查 Pb²⁺ 的试剂是哪一种？ |
| OLD_CHUNK3_EXP_19_8_11_Q006_R1 | 19-8-11 | 在《19-8-11 小设计实验》中，Pb₃O₄ 与 HNO₃ 微热后吸取清液，再用稀 H₂SO₄ 检查 Pb²⁺，这一设计最直接服务于哪一目 |
| OLD_CHUNK3_EXP_19_8_11_Q007_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，Pb₃O₄ 与 HNO₃ 微热后，为什么还要吸取清液并用稀 H₂SO₄ 检查？ |
| OLD_CHUNK3_EXP_19_8_11_Q009 | 19-8-11 | 在《19-8-11 小设计实验》中，如果 Pb₃O₄ 中 Pb(II) 进入硝酸清液，加入稀 H₂SO₄ 的目的最接近哪一项？ |
| OLD_CHUNK3_EXP_19_8_11_Q010_SF1 | 19-8-11 | 在《19-8-11 小设计实验》中，下列哪一组步骤都属于铅丹 Pb₃O₄ 组成分析这条正式点位链？ |
| OLD_CHUNK3_EXP_19_8_11_Q026_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 检查 Pb²⁺ 时，最关键的可观察依据是哪一项？ |
| OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，吸取清液而不是直接处理残渣，更接近哪一项实验意图？ |
| OLD_CHUNK3_EXP_20_1_01_Q001 | 20-1-01 | 在《20-1-01 氢氧化物的生成与性质》实验中，本实验向多种金属盐溶液中滴加的共同试剂是哪一种？ |
| OLD_CHUNK3_EXP_20_1_01_Q002 | 20-1-01 | 在《20-1-01 氢氧化物的生成与性质》实验中，下列哪组金属盐全部属于本实验列出的对象？ |
| OLD_CHUNK3_EXP_20_1_01_Q009 | 20-1-01 | 在《20-1-01 氢氧化物的生成与性质》实验中，CdSO₄ 加 NaOH 生成的 Cd(OH)₂ 与 Zn(OH)₂ 对比，常用于比较哪类 |
| OLD_CHUNK3_EXP_20_1_01_Q010_SF1 | 20-1-01 | 在《20-1-01 氢氧化物的生成与性质》实验中，除滴加 NaOH 生成沉淀外，教材还要求继续检验沉淀的哪两类性质？ |
| OLD_CHUNK3_EXP_20_1_01_Q024_PF1 | 20-1-01 | 在《20-1-01 氢氧化物的生成与性质》实验中，AgNO₃ 与 NaOH 步骤中观察到棕黑色 Ag₂O，更直接说明哪一事实？ |

## 仍保留但质量偏低的题目列表及理由
- 数量：232。本轮已改写最差一批；以下保留项多为点位覆盖型短题或原旧题浅层题，证据充分且机器判分稳定。
| 题号 | review_id | 题型 | 有效题干 | 保留理由 |
| --- | --- | --- | --- | --- |
| 19-6-02 Q001 | OLD_CHUNK3_EXP_19_6_02_Q001 | single_choice | 在《19-6-02 金属镁燃烧》实验中，该实验燃烧的金属样品是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q004 | OLD_CHUNK3_EXP_19_6_02_Q004 | single_choice | 在《19-6-02 金属镁燃烧》实验中，镁在空气中燃烧的主要白色产物是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q006 | OLD_CHUNK3_EXP_19_6_02_Q006 | single_choice | 在《19-6-02 金属镁燃烧》实验中，镁在空气中燃烧时，主要氧化镁的氧化剂是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q010 | OLD_CHUNK3_EXP_19_6_02_Q010 | single_choice | 在《19-6-02 金属镁燃烧》实验中，镁燃烧后收集到的氧化镁通常呈什么颜色？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q011 | OLD_CHUNK3_EXP_19_6_02_Q011 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：金属样品为“镁条”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q012 | OLD_CHUNK3_EXP_19_6_02_Q012 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：预处理为“水银层”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q013 | OLD_CHUNK3_EXP_19_6_02_Q013 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：燃烧现象为“发出耀眼白光”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q014 | OLD_CHUNK3_EXP_19_6_02_Q014 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：主要产物为“MgCl₂”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q015 | OLD_CHUNK3_EXP_19_6_02_Q015 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：反应性质为“氧化还原反应”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q016 | OLD_CHUNK3_EXP_19_6_02_Q016 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：氧化剂为“NaOH”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q018 | OLD_CHUNK3_EXP_19_6_02_Q018 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：夹持工具为“徒手捏住镁条”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q019 | OLD_CHUNK3_EXP_19_6_02_Q019 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：实验目的为“活泼性”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q020 | OLD_CHUNK3_EXP_19_6_02_Q020 | true_false | 在《19-6-02 金属镁燃烧》实验中，判断：产物颜色为“深蓝色”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q021 | OLD_CHUNK3_EXP_19_6_02_Q021 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，该实验点燃燃烧的是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q022 | OLD_CHUNK3_EXP_19_6_02_Q022 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，点燃前应除去镁条表面的____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q023 | OLD_CHUNK3_EXP_19_6_02_Q023 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，镁燃烧时会发出耀眼的____光。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q024 | OLD_CHUNK3_EXP_19_6_02_Q024 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，镁在氧气中燃烧主要生成____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q025 | OLD_CHUNK3_EXP_19_6_02_Q025 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，镁燃烧本质上属于____反应。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q027 | OLD_CHUNK3_EXP_19_6_02_Q027 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，观察镁燃烧时不要长时间____强光。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q028 | OLD_CHUNK3_EXP_19_6_02_Q028 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，点燃镁条时宜用____夹持。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q029 | OLD_CHUNK3_EXP_19_6_02_Q029 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，金属镁燃烧可体现镁作为碱土金属的____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-02 Q030 | OLD_CHUNK3_EXP_19_6_02_Q030 | fill_blank | 在《19-6-02 金属镁燃烧》实验中，镁燃烧生成的 MgO 通常为____固体。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q002 | OLD_CHUNK3_EXP_19_6_03_Q002 | single_choice | 在《19-6-03 与水的作用》实验中，金属钠与水反应的气体产物主要是什么？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q006 | OLD_CHUNK3_EXP_19_6_03_Q006 | single_choice | 在《19-6-03 与水的作用》实验中，金属钙与水反应后，检验溶液酸碱性的目的是什么？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q009 | OLD_CHUNK3_EXP_19_6_03_Q009 | single_choice | 在《19-6-03 与水的作用》实验中，镁条反应前用砂纸处理的主要目的是什么？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q021 | OLD_CHUNK3_EXP_19_6_03_Q021 | fill_blank | 在《19-6-03 与水的作用》实验中，金属钠与水反应生成的气体是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q022 | OLD_CHUNK3_EXP_19_6_03_Q022 | fill_blank | 在《19-6-03 与水的作用》实验中，金属钠与水反应后溶液呈____性。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q023 | OLD_CHUNK3_EXP_19_6_03_Q023 | fill_blank | 在《19-6-03 与水的作用》实验中，取金属钠时需吸干表面的____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q024 | OLD_CHUNK3_EXP_19_6_03_Q024 | fill_blank | 在《19-6-03 与水的作用》实验中，碱金属中，钾与水通常比____与水反应更剧烈。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q025 | OLD_CHUNK3_EXP_19_6_03_Q025 | fill_blank | 在《19-6-03 与水的作用》实验中，镁条与水反应前需用砂纸除去表面____膜。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q026 | OLD_CHUNK3_EXP_19_6_03_Q026 | fill_blank | 在《19-6-03 与水的作用》实验中，镁条分别放入冷水和____水中以比较反应不同。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q027 | OLD_CHUNK3_EXP_19_6_03_Q027 | fill_blank | 在《19-6-03 与水的作用》实验中，金属钙与水反应生成的碱可写作____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q028 | OLD_CHUNK3_EXP_19_6_03_Q028 | fill_blank | 在《19-6-03 与水的作用》实验中，观察钠与水反应时，烧杯上方用合适大小的____盖好。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q029 | OLD_CHUNK3_EXP_19_6_03_Q029 | fill_blank | 在《19-6-03 与水的作用》实验中，钠与水反应可写出碱金属与水反应生成碱和____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-03 Q030 | OLD_CHUNK3_EXP_19_6_03_Q030 | fill_blank | 在《19-6-03 与水的作用》实验中，本实验比较的是碱金属、碱土金属的____性。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q001 | OLD_CHUNK3_EXP_19_6_04_Q001 | single_choice | 在《19-6-04 焰色反应》实验中，焰色反应操作中反复蘸取浓盐酸并灼烧的是哪种金属丝？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q002 | OLD_CHUNK3_EXP_19_6_04_Q002 | single_choice | 在《19-6-04 焰色反应》实验中，镍丝需在氧化焰中烧到何种状态后再蘸取待测液？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q003 | OLD_CHUNK3_EXP_19_6_04_Q003 | single_choice | 在《19-6-04 焰色反应》实验中，K⁺ 焰色常需透过哪种材料观察以减弱钠黄光干扰？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q004 | OLD_CHUNK3_EXP_19_6_04_Q004 | single_choice | 在《19-6-04 焰色反应》实验中，Na⁺ 的典型焰色是什么？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q005 | OLD_CHUNK3_EXP_19_6_04_Q005 | single_choice | 在《19-6-04 焰色反应》实验中，Li⁺ 的典型焰色最接近哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q006 | OLD_CHUNK3_EXP_19_6_04_Q006 | single_choice | 在《19-6-04 焰色反应》实验中，Ca²⁺ 的焰色通常可描述为哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q007 | OLD_CHUNK3_EXP_19_6_04_Q007 | single_choice | 在《19-6-04 焰色反应》实验中，Sr²⁺ 的焰色通常可描述为哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q008 | OLD_CHUNK3_EXP_19_6_04_Q008 | single_choice | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色通常可描述为哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q009 | OLD_CHUNK3_EXP_19_6_04_Q009 | single_choice | 在《19-6-04 焰色反应》实验中，焰色反应的微观原因最接近下列哪一项？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q010 | OLD_CHUNK3_EXP_19_6_04_Q010 | single_choice | 在《19-6-04 焰色反应》实验中，本实验在点滴板上分别滴入的盐溶液多为哪类盐？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q011 | OLD_CHUNK3_EXP_19_6_04_Q011 | true_false | 在《19-6-04 焰色反应》实验中，焰色反应前应把镍丝蘸浓盐酸并在氧化焰中烧至近于无色。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q012 | OLD_CHUNK3_EXP_19_6_04_Q012 | true_false | 在《19-6-04 焰色反应》实验中，K⁺ 焰色观察常透过钴玻璃以减弱钠黄光干扰。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q013 | OLD_CHUNK3_EXP_19_6_04_Q013 | true_false | 在《19-6-04 焰色反应》实验中，Na⁺ 的焰色非常灵敏，常呈黄色。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q014 | OLD_CHUNK3_EXP_19_6_04_Q014 | true_false | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色常可描述为黄绿色。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q015 | OLD_CHUNK3_EXP_19_6_04_Q015 | true_false | 在《19-6-04 焰色反应》实验中，焰色反应与金属原子电子受激发和跃迁发光有关。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q016 | OLD_CHUNK3_EXP_19_6_04_Q016 | true_false | 在《19-6-04 焰色反应》实验中，焰色反应主要用 CCl₄ 萃取卤素单质来判断。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q017 | OLD_CHUNK3_EXP_19_6_04_Q017 | true_false | 在《19-6-04 焰色反应》实验中，镍丝无需清洁，残留钠盐不会影响观察。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q019 | OLD_CHUNK3_EXP_19_6_04_Q019 | true_false | 在《19-6-04 焰色反应》实验中，观察 K⁺ 焰色时钴玻璃的作用是生成 KI 沉淀。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q021 | OLD_CHUNK3_EXP_19_6_04_Q021 | fill_blank | 在《19-6-04 焰色反应》实验中，焰色反应用____蘸取试液。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q022 | OLD_CHUNK3_EXP_19_6_04_Q022 | fill_blank | 在《19-6-04 焰色反应》实验中，镍丝应烧至近于____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q023 | OLD_CHUNK3_EXP_19_6_04_Q023 | fill_blank | 在《19-6-04 焰色反应》实验中，观察 K⁺ 焰色常透过____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q024 | OLD_CHUNK3_EXP_19_6_04_Q024 | fill_blank | 在《19-6-04 焰色反应》实验中，Na⁺ 的典型焰色为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q025 | OLD_CHUNK3_EXP_19_6_04_Q025 | fill_blank | 在《19-6-04 焰色反应》实验中，Li⁺ 的焰色常为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q026 | OLD_CHUNK3_EXP_19_6_04_Q026 | fill_blank | 在《19-6-04 焰色反应》实验中，Ca²⁺ 的焰色常为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q027 | OLD_CHUNK3_EXP_19_6_04_Q027 | fill_blank | 在《19-6-04 焰色反应》实验中，Sr²⁺ 的焰色常为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q028 | OLD_CHUNK3_EXP_19_6_04_Q028 | fill_blank | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色常为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q029 | OLD_CHUNK3_EXP_19_6_04_Q029 | fill_blank | 在《19-6-04 焰色反应》实验中，焰色反应源于电子受激发后跃迁____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-6-04 Q030 | OLD_CHUNK3_EXP_19_6_04_Q030 | fill_blank | 在《19-6-04 焰色反应》实验中，本实验常用 LiCl、NaCl、KCl 等____溶液。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q001 | OLD_CHUNK3_EXP_19_8_01_Q001 | single_choice | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，生成 Pb(OH)₂ 时，向 Pb(NO₃)₂ 溶液中滴加的是哪种溶液？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q004 | OLD_CHUNK3_EXP_19_8_01_Q004 | single_choice | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 既能溶于酸又能溶于强碱，说明其主要性质是下列哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q010 | OLD_CHUNK3_EXP_19_8_01_Q010 | single_choice | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，实验中用于溶解 Pb(OH)₂ 的酸是下列哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q021 | OLD_CHUNK3_EXP_19_8_01_Q021 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(NO₃)₂ 溶液中滴加 NaOH 生成的沉淀是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q022 | OLD_CHUNK3_EXP_19_8_01_Q022 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，生成 Pb(OH)₂ 时使用的铅盐是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q023 | OLD_CHUNK3_EXP_19_8_01_Q023 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 与 HNO₃ 和 NaOH 都能反应，说明它具有____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q024 | OLD_CHUNK3_EXP_19_8_01_Q024 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，实验中用于生成沉淀和测试碱中溶解性的碱是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q025 | OLD_CHUNK3_EXP_19_8_01_Q025 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，试验 Pb(OH)₂ 与酸反应时使用的酸是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q026 | OLD_CHUNK3_EXP_19_8_01_Q026 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(NO₃)₂ 提供的金属离子是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q027 | OLD_CHUNK3_EXP_19_8_01_Q027 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 与酸反应体现其____一面。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q028 | OLD_CHUNK3_EXP_19_8_01_Q028 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 溶于过量 NaOH 体现其____一面。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-01 Q029 | OLD_CHUNK3_EXP_19_8_01_Q029 | fill_blank | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 的生成属于____反应现象。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q002 | OLD_CHUNK3_EXP_19_8_02_Q002 | single_choice | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，SnCl₂ 与适量 NaOH 反应生成的沉淀主要是下列哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q007 | OLD_CHUNK3_EXP_19_8_02_Q007 | single_choice | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 中锡的氧化态是下列哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q021 | OLD_CHUNK3_EXP_19_8_02_Q021 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 的锡(II)盐常用____溶液。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q023 | OLD_CHUNK3_EXP_19_8_02_Q023 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 与____反应可体现其碱性一面。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q024 | OLD_CHUNK3_EXP_19_8_02_Q024 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 溶于过量____可体现其酸性一面。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q025 | OLD_CHUNK3_EXP_19_8_02_Q025 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，既能与酸反应又能与碱反应的氢氧化物称为____氢氧化物。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q026 | OLD_CHUNK3_EXP_19_8_02_Q026 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 中 Sn 的氧化态为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q027 | OLD_CHUNK3_EXP_19_8_02_Q027 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，SnCl₂ 与 NaOH 反应首先观察到的是____生成。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q028 | OLD_CHUNK3_EXP_19_8_02_Q028 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验核心是 Sn(OH)₂ 的生成与____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q029 | OLD_CHUNK3_EXP_19_8_02_Q029 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，HCl 检验 Sn(OH)₂ 与____的反应。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-02 Q030 | OLD_CHUNK3_EXP_19_8_02_Q030 | fill_blank | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，NaOH 检验 Sn(OH)₂ 与____的反应。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q001 | OLD_CHUNK3_EXP_19_8_03_Q001 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，生成 Sb(OH)₃ 时常用的锑(III)盐是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q002 | OLD_CHUNK3_EXP_19_8_03_Q002 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，由 SbCl₃ 生成 Sb(OH)₃ 沉淀时加入的碱是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q003 | OLD_CHUNK3_EXP_19_8_03_Q003 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与适量 NaOH 反应生成的沉淀主要是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q004 | OLD_CHUNK3_EXP_19_8_03_Q004 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 酸性溶解行为时加入的酸是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q005 | OLD_CHUNK3_EXP_19_8_03_Q005 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中的性质时加入的强碱是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q008 | OLD_CHUNK3_EXP_19_8_03_Q008 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，进行 Sb(OH)₃ 性质实验时，最核心的观察对象是什么？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q009 | OLD_CHUNK3_EXP_19_8_03_Q009 | single_choice | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 中锑元素的常见氧化态是哪一种？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q011 | OLD_CHUNK3_EXP_19_8_03_Q011 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：起始锑盐为“SbCl₃”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q012 | OLD_CHUNK3_EXP_19_8_03_Q012 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：沉淀剂为“KSCN”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q013 | OLD_CHUNK3_EXP_19_8_03_Q013 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：沉淀产物为“Sb(OH)₃”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q014 | OLD_CHUNK3_EXP_19_8_03_Q014 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：酸中溶解为“NH₃·H₂O”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q015 | OLD_CHUNK3_EXP_19_8_03_Q015 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：碱中溶解为“NaOH”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q016 | OLD_CHUNK3_EXP_19_8_03_Q016 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：性质判断为“强挥发性”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q017 | OLD_CHUNK3_EXP_19_8_03_Q017 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：浓碱比较为“更强碱性条件下 Sb(OH)₃ 的溶解”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q018 | OLD_CHUNK3_EXP_19_8_03_Q018 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：观察重点为“火柴余烬复燃”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q019 | OLD_CHUNK3_EXP_19_8_03_Q019 | true_false | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：离子来源为“III”。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q021 | OLD_CHUNK3_EXP_19_8_03_Q021 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，生成 Sb(OH)₃ 的起始锑盐可用____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q022 | OLD_CHUNK3_EXP_19_8_03_Q022 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，向 SbCl₃ 溶液中加入____可生成 Sb(OH)₃。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q024 | OLD_CHUNK3_EXP_19_8_03_Q024 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在酸中溶解时加入____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q025 | OLD_CHUNK3_EXP_19_8_03_Q025 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中溶解时加入过量____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q026 | OLD_CHUNK3_EXP_19_8_03_Q026 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 可表现出____氢氧化物性质。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q027 | OLD_CHUNK3_EXP_19_8_03_Q027 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，6 mol·L⁻¹ NaOH 用于观察____碱性条件下的溶解。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q028 | OLD_CHUNK3_EXP_19_8_03_Q028 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，该实验的核心观察是沉淀的生成与____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-03 Q029 | OLD_CHUNK3_EXP_19_8_03_Q029 | fill_blank | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 中 Sb 的氧化态为____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q008 | OLD_CHUNK3_EXP_19_8_04_Q008 | single_choice | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，配制或使用 Bi(NO₃)₃ 时，实验资料的相关思考题提示要注意什么问题？ | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q016 | OLD_CHUNK3_EXP_19_8_04_Q016 | true_false | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，使用铋化合物时应注意毒性和废液回收。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q021 | OLD_CHUNK3_EXP_19_8_04_Q021 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，生成 Bi(OH)₃ 时，Bi(NO₃)₃ 溶液中滴加____溶液。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q022 | OLD_CHUNK3_EXP_19_8_04_Q022 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与____反应可体现其碱性。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q023 | OLD_CHUNK3_EXP_19_8_04_Q023 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 的化学名称是____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q025 | OLD_CHUNK3_EXP_19_8_04_Q025 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 反应生成的沉淀含有____离子。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q026 | OLD_CHUNK3_EXP_19_8_04_Q026 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与酸反应生成盐和____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q027 | OLD_CHUNK3_EXP_19_8_04_Q027 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验所在模块为____的性质。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q028 | OLD_CHUNK3_EXP_19_8_04_Q028 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，使用铋化合物后，废液应集中____处理。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
| 19-8-04 Q029 | OLD_CHUNK3_EXP_19_8_04_Q029 | fill_blank | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 在碱中不易溶时，说明其两性相对较____。 | 保留用于覆盖孤立点位或原题虽浅但答案由 canonical 直接支撑、机器判分稳定；未列入最差风险批次。 |
- 另有 112 道低深度保留题未展开，均已在 JSON 中标注 `kept_low_quality` 或保守 source_audit。

## evidence insufficient 题目列表
### 原题不足但 proposed 已修复
| 题号 | review_id | 原风险标记 | 有效 proposed 题干 |
| --- | --- | --- | --- |
| 19-6-02 Q017 | OLD_CHUNK3_EXP_19_6_02_Q017_R1 | wrong_safety_polarity rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-6-02 金属镁燃烧》实验中，观察镁燃烧时应避免长时间直视强光。 |
| 19-6-02 Q026 | OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | short_phone_friendly_fill_blank semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_rewrite rewrite_required | 在《19-6-02 金属镁燃烧》实验中，与其让学生直接填写 O₂，更能体现本实验观察目的的是哪一项？ |
| 19-6-03 Q017 | OLD_CHUNK3_EXP_19_6_03_Q017_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-6-03 与水的作用》实验中，镁条反应前除去氧化膜可减少表面膜对反应的阻碍。 |
| 19-6-03 Q019 | OLD_CHUNK3_EXP_19_6_03_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-6-03 与水的作用》实验中，钠、钙与水反应都可能产生 H₂。 |
| 19-6-03 Q020 | OLD_CHUNK3_EXP_19_6_03_Q020_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-6-03 与水的作用》实验中，本实验属于碱金属、碱土金属活泼性比较的一部分。 |
| 19-6-04 Q018 | OLD_CHUNK3_EXP_19_6_04_Q018_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-6-04 焰色反应》实验中，Li⁺、Na⁺、K⁺、Ca²⁺、Sr²⁺、Ba²⁺ 都可作为本实验观察对象。 |
| 19-6-04 Q020 | OLD_CHUNK3_EXP_19_6_04_Q020_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-6-04 焰色反应》实验中，本实验要求记录各离子的火焰颜色。 |
| 19-8-01 Q002 | OLD_CHUNK3_EXP_19_8_01_Q002_R1 | direct_concentration_recall rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，将 Pb(OH)₂ 沉淀分别与 HNO₃ 和过量 NaOH 作用，最主要是为了判断什么？ |
| 19-8-01 Q014 | OLD_CHUNK3_EXP_19_8_01_Q014_SF1 | semantic_final_reviewed rewrite_required direct_concentration_recall machine_deterministic_replacement | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，比较 Pb(OH)₂ 与 HNO₃、过量 NaOH 的作用，主要是为了判断 Pb(OH)₂ 是否具有两性。 |
| 19-8-01 Q019 | OLD_CHUNK3_EXP_19_8_01_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb²⁺ 与 OH⁻ 结合可生成 Pb(OH)₂ 沉淀。 |
| 19-8-01 Q030 | OLD_CHUNK3_EXP_19_8_01_Q030_R1_PF1 | direct_concentration_recall rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property polished_final_rewrite polished_proposed... | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，只让 Pb(OH)₂ 沉淀与 HNO₃ 作用，而不再比较其与过量 NaOH 的作用，不能充分体现两性氢氧化物的判断。 |
| 19-8-02 Q022 | OLD_CHUNK3_EXP_19_8_02_Q022_PF1 | short_phone_friendly_fill_blank missing_original_explanation_filled semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_... | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 后，继续分别加入 HCl 和过量 NaOH，最主要是为了判断什么？ |
| 19-8-03 Q020 | OLD_CHUNK3_EXP_19_8_03_Q020_SF1 | semantic_final_reviewed rewrite_required ambiguous_wrong_polarity machine_deterministic_replacement | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 是生成 Sb(OH)₃ 沉淀的直接试剂组合。 |
| 19-8-03 Q023 | OLD_CHUNK3_EXP_19_8_03_Q023_PF1 | short_phone_friendly_fill_blank semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_rewrite rewrite_required | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 生成 Sb(OH)₃ 后，继续比较 HCl、2 mol/L NaOH 和 6 mol/L NaOH 的作用，最主要是为了判断什么？ |
| 19-8-03 Q030 | OLD_CHUNK3_EXP_19_8_03_Q030_SF1 | semantic_final_reviewed rewrite_required mobile_fill_blank_too_complex_and_corrupt_v1 machine_deterministic_replacement | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，下列哪一组是生成 Sb(OH)₃ 沉淀的直接试剂组合？ |
| 19-8-04 Q018 | OLD_CHUNK3_EXP_19_8_04_Q018_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，向 Bi(OH)₃ 中加入 HCl 后若沉淀溶解，可说明酸能与其反应。 |
| 19-8-04 Q019 | OLD_CHUNK3_EXP_19_8_04_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 反应中 OH⁻ 是形成氢氧化物沉淀的必要离子。 |
| 19-8-04 Q020 | OLD_CHUNK3_EXP_19_8_04_Q020_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，40% NaOH 是本实验列出的强碱条件之一。 |
| 19-8-04 Q024 | OLD_CHUNK3_EXP_19_8_04_Q024_SF1 | semantic_final_reviewed rewrite_required direct_concentration_recall machine_deterministic_replacement | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和更强 NaOH 条件的作用，主要是为了判断什么？ |
| 19-8-04 Q030 | OLD_CHUNK3_EXP_19_8_04_Q030_PF1 | short_phone_friendly_fill_blank semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_rewrite rewrite_required | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 生成 Bi(OH)₃ 只是第一步，后续还需比较其与 HCl、6 mol/L NaOH 和 40% NaOH 的作用。 |
| 19-8-05 Q018 | OLD_CHUNK3_EXP_19_8_05_Q018_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，只观察沉淀生成而不试验酸、碱作用，不能充分总结酸碱性。 |
| 19-8-05 Q019 | OLD_CHUNK3_EXP_19_8_05_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Bi(OH)₃ 通常比 Sn(OH)₂ 更表现出碱性氢氧化物特征。 |
| 19-8-06 Q017 | OLD_CHUNK3_EXP_19_8_06_Q017_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-06 Sn(II) 的还原性》实验中，Sn(II) 与 Fe(II) 的还原性可通过 FeCl₃/SnCl₂ 实验进行比较。 |
| 19-8-06 Q019 | OLD_CHUNK3_EXP_19_8_06_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-06 Sn(II) 的还原性》实验中，若 Fe³⁺ 已被充分还原，加入 KSCN 后血红色会明显减弱或不出现。 |
| 19-8-06 Q025 | OLD_CHUNK3_EXP_19_8_06_Q025_PF1 | short_phone_friendly_fill_blank missing_original_explanation_filled semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_... | 在《19-8-06 Sn(II) 的还原性》实验中，SnCl₂ 与 HgCl₂ 反应中先出现白色沉淀、过量 SnCl₂ 时可继续变暗，这组现象主要说明什么？ |
| 19-8-07 Q024 | OLD_CHUNK3_EXP_19_8_07_Q024_PF1 | short_phone_friendly_fill_blank missing_original_explanation_filled semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_... | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂、H₂SO₄ 和 MnSO₄ 水浴加热后若出现紫色，最直接说明哪一判断？ |
| 19-8-08 Q019 | OLD_CHUNK3_EXP_19_8_08_Q019_SF1 | semantic_final_reviewed rewrite_required ambiguous_true_false_polarity machine_deterministic_replacement | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，若碱性 KMnO₄ 体系被加入的 As(III)、Sb(III) 或 Bi(III) 物种还原，该加入物在该体系中表现还原性。 |
| 19-8-08 Q021 | OLD_CHUNK3_EXP_19_8_08_Q021_R1 | mobile_fill_blank_too_complex rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，分别把 As(III)、Sb(III)、Bi(III) 物种投入多个氧化体系，主要比较的是哪一项？ |
| 19-8-08 Q025 | OLD_CHUNK3_EXP_19_8_08_Q025_PF1 | short_phone_friendly_fill_blank semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_rewrite rewrite_required | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，Bi(NO₃)₃ 在本实验中主要出现在下列哪组 Bi(III) 性质比较步骤中？ |
| 19-8-09 Q017 | OLD_CHUNK3_EXP_19_8_09_Q017_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，砷化合物安全风险较高，实验后废液应集中处理。 |
| 19-8-09 Q019 | OLD_CHUNK3_EXP_19_8_09_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，KI 在本实验中可作为还原性检测试剂。 |
| 19-8-09 Q020 | OLD_CHUNK3_EXP_19_8_09_Q020_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，酸化条件会影响许多氧化还原反应的方向和现象。 |
| 19-8-09 Q028 | OLD_CHUNK3_EXP_19_8_09_Q028_PF1 | short_phone_friendly_fill_blank semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_rewrite rewrite_required | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，酸性 MnSO₄ 体系出现紫色，更能说明哪一类证据？ |
| 19-8-10 Q018 | OLD_CHUNK3_EXP_19_8_10_Q018_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，KSCN 可用于检验 Fe³⁺ 是否仍存在。 |
| 19-8-10 Q019 | OLD_CHUNK3_EXP_19_8_10_Q019_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，Bi(NO₃)₃ 与 NaOH、氯水步骤与铋价态变化有关。 |
| 19-8-10 Q027 | OLD_CHUNK3_EXP_19_8_10_Q027_PF1 | short_phone_friendly_fill_blank semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_rewrite rewrite_required | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，加入 KI 和 CCl₄ 后出现紫色有机层，在本实验中最直接支持哪一判断？ |
| 19-8-11 Q006 | OLD_CHUNK3_EXP_19_8_11_Q006_R1 | outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required | 在《19-8-11 小设计实验》中，Pb₃O₄ 与 HNO₃ 微热后吸取清液，再用稀 H₂SO₄ 检查 Pb²⁺，这一设计最直接服务于哪一目标？ |
| 19-8-11 Q007 | OLD_CHUNK3_EXP_19_8_11_Q007_R1_PF1 | outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required polished_final_rewrite polished_proposed_dedupe | 在《19-8-11 小设计实验》实验中，Pb₃O₄ 与 HNO₃ 微热后，为什么还要吸取清液并用稀 H₂SO₄ 检查？ |
| 19-8-11 Q010 | OLD_CHUNK3_EXP_19_8_11_Q010_SF1 | semantic_final_reviewed rewrite_required outside_formal_video_point_scope machine_deterministic_replacement | 在《19-8-11 小设计实验》中，下列哪一组步骤都属于铅丹 Pb₃O₄ 组成分析这条正式点位链？ |
| 19-8-11 Q015 | OLD_CHUNK3_EXP_19_8_11_Q015_R1 | outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required | 在《19-8-11 小设计实验》中，Pb₃O₄ 与 HNO₃ 微热以及取清液用稀 H₂SO₄ 检查 Pb²⁺，属于分析铅丹组成的同一证据链。 |
| 19-8-11 Q017 | OLD_CHUNK3_EXP_19_8_11_Q017_R1 | confusing_double_negative rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property | 在《19-8-11 小设计实验》中，Pb₃O₄ 的组成分析可围绕 Pb(II) 与 Pb(IV) 两类铅展开。 |
| 19-8-11 Q019 | OLD_CHUNK3_EXP_19_8_11_Q019_R1_PF1 | confusing_double_negative outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required polished_final_rewrite polished_proposed_dedupe | 在《19-8-11 小设计实验》实验中，用稀 H₂SO₄ 检查的是 HNO₃ 处理后清液中的 Pb²⁺，不是 SbCl₃ 与 Bi(NO₃)₃ 的分离鉴定步骤。 |
| 19-8-11 Q020 | OLD_CHUNK3_EXP_19_8_11_Q020_R1_PF1 | confusing_double_negative outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required polished_final_rewrite polished_proposed_dedupe | 在《19-8-11 小设计实验》实验中，若省去清液的稀 H₂SO₄ 检查，仅凭 Pb₃O₄ 与 HNO₃ 微热不能完成 Pb²⁺ 证据确认。 |
| 19-8-11 Q026 | OLD_CHUNK3_EXP_19_8_11_Q026_R1_PF1 | outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property polished_final_rewrite polished_pro... | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 检查 Pb²⁺ 时，最关键的可观察依据是哪一项？ |
| 19-8-11 Q027 | OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property polished_final_rewrite polished_pro... | 在《19-8-11 小设计实验》实验中，吸取清液而不是直接处理残渣，更接近哪一项实验意图？ |
| 19-8-11 Q028 | OLD_CHUNK3_EXP_19_8_11_Q028_R1_PF1 | outside_formal_video_point_scope rewritten_with_replacement semantic_final_reviewed rewrite_required theory_dependent_for_outcome_or_property polished_final_rewrite polished_pro... | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 步骤的判断对象是清液中的 Pb²⁺，而不是检验 HNO₃ 本身。 |
| 20-1-01 Q024 | OLD_CHUNK3_EXP_20_1_01_Q024_PF1 | short_phone_friendly_fill_blank missing_original_explanation_filled semantic_final_reviewed theory_dependent_for_outcome_or_property polished_final_rewrite polished_mobile_fill_... | 在《20-1-01 氢氧化物的生成与性质》实验中，AgNO₃ 与 NaOH 步骤中观察到棕黑色 Ag₂O，更直接说明哪一事实？ |
### 最终仍 evidence insufficient
- 无。polished_final_v1 中最终有效题均标注 `evidence_sufficient: true`。

## 多点位题目列表
- 数量：171。多点位仅在题意实际跨步骤比较、证据链或总结多个点位时保留。
| 题号 | review_id | 点位 | 有效题干 |
| --- | --- | --- | --- |
| 19-6-02 Q026 | OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | ['镁条除去氧化膜后点燃', '观察镁燃烧及生成物'] | 在《19-6-02 金属镁燃烧》实验中，与其让学生直接填写 O₂，更能体现本实验观察目的的是哪一项？ |
| 19-6-03 Q003 | OLD_CHUNK3_EXP_19_6_03_Q003 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）'] | 在《19-6-03 与水的作用》实验中，实验中取钠或钾前要用滤纸吸干表面的哪种保护液？ |
| 19-6-03 Q005 | OLD_CHUNK3_EXP_19_6_03_Q005 | ['镁条与冷水反应', '镁条与热水反应'] | 在《19-6-03 与水的作用》实验中，镁条分别放入冷水和热水中，是为了比较什么？ |
| 19-6-03 Q007 | OLD_CHUNK3_EXP_19_6_03_Q007 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）'] | 在《19-6-03 与水的作用》实验中，为安全观察钠、钾与水反应，实验资料建议用什么盖住烧杯？ |
| 19-6-03 Q009 | OLD_CHUNK3_EXP_19_6_03_Q009 | ['镁条与冷水反应', '镁条与热水反应'] | 在《19-6-03 与水的作用》实验中，镁条反应前用砂纸处理的主要目的是什么？ |
| 19-6-03 Q010 | OLD_CHUNK3_EXP_19_6_03_Q010 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）', '镁条与冷水反应', '镁条与热水反应', '金属钙与水反应'] | 在《19-6-03 与水的作用》实验中，本实验通过钠、镁、钙等与水反应，主要比较什么？ |
| 19-6-03 Q013 | OLD_CHUNK3_EXP_19_6_03_Q013 | ['镁条与冷水反应', '镁条与热水反应'] | 在《19-6-03 与水的作用》实验中，镁条在热水中通常比在冷水中更容易反应。 |
| 19-6-03 Q016 | OLD_CHUNK3_EXP_19_6_03_Q016 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）'] | 在《19-6-03 与水的作用》实验中，观察钠或钾与水反应时，用漏斗盖好有助于安全控制飞溅。 |
| 19-6-03 Q017 | OLD_CHUNK3_EXP_19_6_03_Q017_R1 | ['镁条与冷水反应', '镁条与热水反应'] | 在《19-6-03 与水的作用》实验中，镁条反应前除去氧化膜可减少表面膜对反应的阻碍。 |
| 19-6-03 Q018 | OLD_CHUNK3_EXP_19_6_03_Q018 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）', '镁条与冷水反应', '镁条与热水反应', '金属钙与水反应'] | 在《19-6-03 与水的作用》实验中，本实验的核心产物一定是棕色 Fe(NO)SO₄ 环。 |
| 19-6-03 Q019 | OLD_CHUNK3_EXP_19_6_03_Q019_R1 | ['金属钠与水反应', '金属钙与水反应'] | 在《19-6-03 与水的作用》实验中，钠、钙与水反应都可能产生 H₂。 |
| 19-6-03 Q020 | OLD_CHUNK3_EXP_19_6_03_Q020_R1 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）', '镁条与冷水反应', '镁条与热水反应', '金属钙与水反应'] | 在《19-6-03 与水的作用》实验中，本实验属于碱金属、碱土金属活泼性比较的一部分。 |
| 19-6-03 Q025 | OLD_CHUNK3_EXP_19_6_03_Q025 | ['镁条与冷水反应', '镁条与热水反应'] | 在《19-6-03 与水的作用》实验中，镁条与水反应前需用砂纸除去表面____膜。 |
| 19-6-03 Q026 | OLD_CHUNK3_EXP_19_6_03_Q026 | ['镁条与冷水反应', '镁条与热水反应'] | 在《19-6-03 与水的作用》实验中，镁条分别放入冷水和____水中以比较反应不同。 |
| 19-6-03 Q030 | OLD_CHUNK3_EXP_19_6_03_Q030 | ['金属钠与水反应', '金属钾与水反应（不采购，不做）', '镁条与冷水反应', '镁条与热水反应', '金属钙与水反应'] | 在《19-6-03 与水的作用》实验中，本实验比较的是碱金属、碱土金属的____性。 |
| 19-6-04 Q001 | OLD_CHUNK3_EXP_19_6_04_Q001 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应操作中反复蘸取浓盐酸并灼烧的是哪种金属丝？ |
| 19-6-04 Q002 | OLD_CHUNK3_EXP_19_6_04_Q002 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，镍丝需在氧化焰中烧到何种状态后再蘸取待测液？ |
| 19-6-04 Q009 | OLD_CHUNK3_EXP_19_6_04_Q009 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应的微观原因最接近下列哪一项？ |
| 19-6-04 Q010 | OLD_CHUNK3_EXP_19_6_04_Q010 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，本实验在点滴板上分别滴入的盐溶液多为哪类盐？ |
| 19-6-04 Q011 | OLD_CHUNK3_EXP_19_6_04_Q011 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应前应把镍丝蘸浓盐酸并在氧化焰中烧至近于无色。 |
| 19-6-04 Q015 | OLD_CHUNK3_EXP_19_6_04_Q015 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应与金属原子电子受激发和跃迁发光有关。 |
| 19-6-04 Q016 | OLD_CHUNK3_EXP_19_6_04_Q016 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应主要用 CCl₄ 萃取卤素单质来判断。 |
| 19-6-04 Q017 | OLD_CHUNK3_EXP_19_6_04_Q017 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，镍丝无需清洁，残留钠盐不会影响观察。 |
| 19-6-04 Q018 | OLD_CHUNK3_EXP_19_6_04_Q018_R1 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，Li⁺、Na⁺、K⁺、Ca²⁺、Sr²⁺、Ba²⁺ 都可作为本实验观察对象。 |
| 19-6-04 Q020 | OLD_CHUNK3_EXP_19_6_04_Q020_R1 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，本实验要求记录各离子的火焰颜色。 |
| 19-6-04 Q021 | OLD_CHUNK3_EXP_19_6_04_Q021 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应用____蘸取试液。 |
| 19-6-04 Q022 | OLD_CHUNK3_EXP_19_6_04_Q022 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，镍丝应烧至近于____。 |
| 19-6-04 Q029 | OLD_CHUNK3_EXP_19_6_04_Q029 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，焰色反应源于电子受激发后跃迁____。 |
| 19-6-04 Q030 | OLD_CHUNK3_EXP_19_6_04_Q030 | ['Li⁺ 焰色反应', 'Na⁺ 焰色反应', 'K⁺ 焰色反应，需透过钴玻璃观察', 'Ca²⁺ 焰色反应', 'Sr²⁺ 焰色反应', 'Ba²⁺ 焰色反应'] | 在《19-6-04 焰色反应》实验中，本实验常用 LiCl、NaCl、KCl 等____溶液。 |
| 19-8-01 Q002 | OLD_CHUNK3_EXP_19_8_01_Q002_R1 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，将 Pb(OH)₂ 沉淀分别与 HNO₃ 和过量 NaOH 作用，最主要是为了判断什么？ |
| 19-8-01 Q003 | OLD_CHUNK3_EXP_19_8_01_Q003 | ['Pb(NO₃)₂ + NaOH', 'Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，生成的 Pb(OH)₂ 沉淀分别要与哪两种 2 mol·L⁻¹ 溶液作用？ |
| 19-8-01 Q004 | OLD_CHUNK3_EXP_19_8_01_Q004 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 既能溶于酸又能溶于强碱，说明其主要性质是下列哪一种？ |
| 19-8-01 Q008 | OLD_CHUNK3_EXP_19_8_01_Q008 | ['Pb(NO₃)₂ + NaOH', 'Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，下列哪项最符合该实验的目的？ |
| 19-8-01 Q012 | OLD_CHUNK3_EXP_19_8_01_Q012 | ['Pb(NO₃)₂ + NaOH', 'Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 沉淀要分别试验与 HNO₃ 和 NaOH 的反应。 |
| 19-8-01 Q013 | OLD_CHUNK3_EXP_19_8_01_Q013 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 能溶于酸和强碱，体现两性。 |
| 19-8-01 Q014 | OLD_CHUNK3_EXP_19_8_01_Q014_SF1 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，比较 Pb(OH)₂ 与 HNO₃、过量 NaOH 的作用，主要是为了判断 Pb(OH)₂ 是否具有两性。 |
| 19-8-01 Q016 | OLD_CHUNK3_EXP_19_8_01_Q016 | ['Pb(NO₃)₂ + NaOH', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，NaOH 只能用于生成沉淀，不能用于测试 Pb(OH)₂ 的两性。 |
| 19-8-01 Q020 | OLD_CHUNK3_EXP_19_8_01_Q020 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，该实验不应把 Pb(OH)₂ 的酸碱性与两性联系起来。 |
| 19-8-01 Q023 | OLD_CHUNK3_EXP_19_8_01_Q023 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 与 HNO₃ 和 NaOH 都能反应，说明它具有____。 |
| 19-8-01 Q024 | OLD_CHUNK3_EXP_19_8_01_Q024 | ['Pb(NO₃)₂ + NaOH', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，实验中用于生成沉淀和测试碱中溶解性的碱是____。 |
| 19-8-01 Q030 | OLD_CHUNK3_EXP_19_8_01_Q030_R1_PF1 | ['Pb(OH)₂ + HNO₃', 'Pb(OH)₂ + NaOH'] | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，只让 Pb(OH)₂ 沉淀与 HNO₃ 作用，而不再比较其与过量 NaOH 的作用，不能充分体现两性氢氧化物的判断。 |
| 19-8-02 Q005 | OLD_CHUNK3_EXP_19_8_02_Q005 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验比较 Sn(OH)₂ 对 HCl 和 NaOH 的反应，核心是判断哪一性质？ |
| 19-8-02 Q006 | OLD_CHUNK3_EXP_19_8_02_Q006 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，下列哪一组最符合本实验试剂？ |
| 19-8-02 Q008 | OLD_CHUNK3_EXP_19_8_02_Q008 | ['Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，若沉淀既能溶于酸又能溶于过量碱，通常称其为哪类氢氧化物？ |
| 19-8-02 Q009 | OLD_CHUNK3_EXP_19_8_02_Q009 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，下列哪一项不是 Sn(OH)₂ 性质实验的合理观察对象？ |
| 19-8-02 Q010 | OLD_CHUNK3_EXP_19_8_02_Q010 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验属于哪一组元素化合物性质实验的内容？ |
| 19-8-02 Q015 | OLD_CHUNK3_EXP_19_8_02_Q015 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验的主要试剂是 PbO₂ 和浓盐酸。 |
| 19-8-02 Q017 | OLD_CHUNK3_EXP_19_8_02_Q017 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，只观察 SnCl₂ 与 NaOH 是否生成沉淀，还不足以完整说明 Sn(OH)₂ 的两性。 |
| 19-8-02 Q018 | OLD_CHUNK3_EXP_19_8_02_Q018 | ['Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，HCl 和 NaOH 分别从酸、碱两方面检验 Sn(OH)₂ 的性质。 |
| 19-8-02 Q019 | OLD_CHUNK3_EXP_19_8_02_Q019 | ['Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 与酸碱均不反应，所以不能用酸碱试剂检验。 |
| 19-8-02 Q020 | OLD_CHUNK3_EXP_19_8_02_Q020_SF1 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，只观察 Sn(OH)₂ 沉淀生成，还不足以判断其两性，还需比较它与 HCl 和过量 NaOH 的作用。 |
| 19-8-02 Q022 | OLD_CHUNK3_EXP_19_8_02_Q022_PF1 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 后，继续分别加入 HCl 和过量 NaOH，最主要是为了判断什么？ |
| 19-8-02 Q025 | OLD_CHUNK3_EXP_19_8_02_Q025 | ['Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，既能与酸反应又能与碱反应的氢氧化物称为____氢氧化物。 |
| 19-8-02 Q028 | OLD_CHUNK3_EXP_19_8_02_Q028 | ['SnCl₂ + NaOH', 'Sn(OH)₂ + HCl', 'Sn(OH)₂ + NaOH'] | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验核心是 Sn(OH)₂ 的生成与____。 |
| 19-8-03 Q005 | OLD_CHUNK3_EXP_19_8_03_Q005 | ['Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中的性质时加入的强碱是哪一种？ |
| 19-8-03 Q006 | OLD_CHUNK3_EXP_19_8_03_Q006 | ['Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 既能溶于酸又能溶于强碱，说明它具有什么性质？ |
| 19-8-03 Q007 | OLD_CHUNK3_EXP_19_8_03_Q007 | ['Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，与 2 mol·L⁻¹ NaOH 相比，6 mol·L⁻¹ NaOH 在该实验中主要用于观察什么？ |
| 19-8-03 Q008 | OLD_CHUNK3_EXP_19_8_03_Q008 | ['SbCl₃ + NaOH', 'Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，进行 Sb(OH)₃ 性质实验时，最核心的观察对象是什么？ |
| 19-8-03 Q010 | OLD_CHUNK3_EXP_19_8_03_Q010 | ['SbCl₃ + NaOH', 'Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，下列哪种物质不是该实验生成 Sb(OH)₃ 的直接试剂组合？ |
| 19-8-03 Q015 | OLD_CHUNK3_EXP_19_8_03_Q015 | ['Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：碱中溶解为“NaOH”。 |
| 19-8-03 Q016 | OLD_CHUNK3_EXP_19_8_03_Q016 | ['Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：性质判断为“强挥发性”。 |
| 19-8-03 Q017 | OLD_CHUNK3_EXP_19_8_03_Q017 | ['Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：浓碱比较为“更强碱性条件下 Sb(OH)₃ 的溶解”。 |
| 19-8-03 Q018 | OLD_CHUNK3_EXP_19_8_03_Q018 | ['SbCl₃ + NaOH', 'Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：观察重点为“火柴余烬复燃”。 |
| 19-8-03 Q023 | OLD_CHUNK3_EXP_19_8_03_Q023_PF1 | ['SbCl₃ + NaOH', 'Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 生成 Sb(OH)₃ 后，继续比较 HCl、2 mol/L NaOH 和 6 mol/L NaOH 的作用，最主要是为了判断什么？ |
| 19-8-03 Q025 | OLD_CHUNK3_EXP_19_8_03_Q025 | ['Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中溶解时加入过量____。 |
| 19-8-03 Q026 | OLD_CHUNK3_EXP_19_8_03_Q026 | ['Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 可表现出____氢氧化物性质。 |
| 19-8-03 Q027 | OLD_CHUNK3_EXP_19_8_03_Q027 | ['Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，6 mol·L⁻¹ NaOH 用于观察____碱性条件下的溶解。 |
| 19-8-03 Q028 | OLD_CHUNK3_EXP_19_8_03_Q028 | ['SbCl₃ + NaOH', 'Sb(OH)₃ + HCl', 'Sb(OH)₃ + 2 mol/L NaOH', 'Sb(OH)₃ + 6 mol/L NaOH'] | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，该实验的核心观察是沉淀的生成与____。 |
| 19-8-04 Q005 | OLD_CHUNK3_EXP_19_8_04_Q005 | ['Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，实验还比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和哪种更浓碱的作用？ |
| 19-8-04 Q006 | OLD_CHUNK3_EXP_19_8_04_Q006 | ['Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，若 Bi(OH)₃ 在过量 NaOH 中不明显溶解，说明它与 Sn、Pb、Sb 的某些氢氧化物相比怎样？ |
| 19-8-04 Q007 | OLD_CHUNK3_EXP_19_8_04_Q007 | ['Bi(NO₃)₃ + NaOH', 'Bi(OH)₃ + HCl', 'Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验属于 19-8 中哪一模块？ |
| 19-8-04 Q010 | OLD_CHUNK3_EXP_19_8_04_Q010 | ['Bi(NO₃)₃ + NaOH', 'Bi(OH)₃ + HCl', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，下列哪一项不是本实验的直接试剂组合？ |
| 19-8-04 Q013 | OLD_CHUNK3_EXP_19_8_04_Q013 | ['Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验比较 Bi(OH)₃ 在 6 mol·L⁻¹ NaOH 和 40% NaOH 中的表现。 |
| 19-8-04 Q014 | OLD_CHUNK3_EXP_19_8_04_Q014 | ['Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 是典型强两性氢氧化物，必然易溶于任意稀碱。 |
| 19-8-04 Q015 | OLD_CHUNK3_EXP_19_8_04_Q015 | ['Bi(NO₃)₃ + NaOH', 'Bi(OH)₃ + HCl', 'Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验属于锡、铅、砷、锑、铋实验中的氢氧化物性质部分。 |
| 19-8-04 Q024 | OLD_CHUNK3_EXP_19_8_04_Q024_SF1 | ['Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和更强 NaOH 条件的作用，主要是为了判断什么？ |
| 19-8-04 Q027 | OLD_CHUNK3_EXP_19_8_04_Q027 | ['Bi(NO₃)₃ + NaOH', 'Bi(OH)₃ + HCl', 'Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验所在模块为____的性质。 |
| 19-8-04 Q029 | OLD_CHUNK3_EXP_19_8_04_Q029 | ['Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 在碱中不易溶时，说明其两性相对较____。 |
| 19-8-04 Q030 | OLD_CHUNK3_EXP_19_8_04_Q030_PF1 | ['Bi(NO₃)₃ + NaOH', 'Bi(OH)₃ + HCl', 'Bi(OH)₃ + 6 mol/L NaOH', 'Bi(OH)₃ + 40% NaOH'] | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 生成 Bi(OH)₃ 只是第一步，后续还需比较其与 HCl、6 mol/L NaOH 和 40% NaOH 的作用。 |
| 19-8-05 Q010 | OLD_CHUNK3_EXP_19_8_05_Q010 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性', 'SbCl₃ 制备 Sb(OH)₃，并测试酸碱性', 'Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，该组实验最终要总结 Sn、Pb、Sb、Bi 氢氧化物的哪类性质？ |
| 19-8-05 Q015 | OLD_CHUNK3_EXP_19_8_05_Q015 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 和 Pb(OH)₂ 可作为两性氢氧化物讨论。 |
| 19-8-05 Q016 | OLD_CHUNK3_EXP_19_8_05_Q016 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性', 'SbCl₃ 制备 Sb(OH)₃，并测试酸碱性', 'Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，本实验的核心观察对象是卤化银感光性。 |
| 19-8-05 Q018 | OLD_CHUNK3_EXP_19_8_05_Q018_R1 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性', 'SbCl₃ 制备 Sb(OH)₃，并测试酸碱性', 'Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，只观察沉淀生成而不试验酸、碱作用，不能充分总结酸碱性。 |
| 19-8-05 Q019 | OLD_CHUNK3_EXP_19_8_05_Q019_R1 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Bi(OH)₃ 通常比 Sn(OH)₂ 更表现出碱性氢氧化物特征。 |
| 19-8-05 Q020 | OLD_CHUNK3_EXP_19_8_05_Q020 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性', 'SbCl₃ 制备 Sb(OH)₃，并测试酸碱性', 'Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，SbCl₃、Bi(NO₃)₃、Pb(NO₃)₂ 等重金属化合物操作可忽略安全防护。 |
| 19-8-05 Q030 | OLD_CHUNK3_EXP_19_8_05_Q030 | ['SnCl₂ 制备 Sn(OH)₂，并测试酸碱性', 'Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性', 'SbCl₃ 制备 Sb(OH)₃，并测试酸碱性', 'Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性'] | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，该组实验最终总结这些氢氧化物的____。 |
| 19-8-06 Q009 | OLD_CHUNK3_EXP_19_8_06_Q009 | ['SnCl₂ + FeCl₃', '比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性'] | 在《19-8-06 Sn(II) 的还原性》实验中，通过 SnCl₂ 还原 Fe³⁺ 的实验，可比较 Sn(II) 与哪种离子的还原性强弱？ |
| 19-8-06 Q010 | OLD_CHUNK3_EXP_19_8_06_Q010 | ['SnCl₂ + FeCl₃', 'SnCl₂ + HgCl₂', '比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性'] | 在《19-8-06 Sn(II) 的还原性》实验中，下列哪一组属于该实验的主要反应对象？ |
| 19-8-06 Q017 | OLD_CHUNK3_EXP_19_8_06_Q017_R1 | ['SnCl₂ + FeCl₃', '比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性'] | 在《19-8-06 Sn(II) 的还原性》实验中，Sn(II) 与 Fe(II) 的还原性可通过 FeCl₃/SnCl₂ 实验进行比较。 |
| 19-8-06 Q019 | OLD_CHUNK3_EXP_19_8_06_Q019_R1 | ['SnCl₂ + FeCl₃', '用 KSCN 检验 Fe³⁺ 是否仍存在'] | 在《19-8-06 Sn(II) 的还原性》实验中，若 Fe³⁺ 已被充分还原，加入 KSCN 后血红色会明显减弱或不出现。 |
| 19-8-06 Q020 | OLD_CHUNK3_EXP_19_8_06_Q020 | ['SnCl₂ + FeCl₃', 'SnCl₂ + HgCl₂', '比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性'] | 在《19-8-06 Sn(II) 的还原性》实验中，该实验的主题是 Pb(OH)₂ 的两性而不是 Sn(II) 的还原性。 |
| 19-8-06 Q025 | OLD_CHUNK3_EXP_19_8_06_Q025_PF1 | ['SnCl₂ + HgCl₂', '比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性'] | 在《19-8-06 Sn(II) 的还原性》实验中，SnCl₂ 与 HgCl₂ 反应中先出现白色沉淀、过量 SnCl₂ 时可继续变暗，这组现象主要说明什么？ |
| 19-8-06 Q028 | OLD_CHUNK3_EXP_19_8_06_Q028 | ['SnCl₂ + FeCl₃', '比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性'] | 在《19-8-06 Sn(II) 的还原性》实验中，该实验通过 SnCl₂ 与 FeCl₃ 反应比较 Sn(II) 与____的还原性。 |
| 19-8-07 Q001 | OLD_CHUNK3_EXP_19_8_07_Q001 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，本实验考察 Pb(IV) 氧化性时使用的固体试剂是哪一种？ |
| 19-8-07 Q002 | OLD_CHUNK3_EXP_19_8_07_Q002 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 与浓 HCl 反应时，主要用于比较 Pb(IV) 与哪种氧化剂的强弱？ |
| 19-8-07 Q003 | OLD_CHUNK3_EXP_19_8_07_Q003 | ['PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂、H₂SO₄ 和 MnSO₄ 水浴加热，主要用于观察哪种离子被氧化？ |
| 19-8-07 Q004 | OLD_CHUNK3_EXP_19_8_07_Q004 | ['PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，酸性条件下 Mn²⁺ 被 PbO₂ 氧化后，可能出现的紫色物种是哪一种？ |
| 19-8-07 Q005 | OLD_CHUNK3_EXP_19_8_07_Q005 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 与浓盐酸反应中，HCl 的主要还原性成分是哪一种？ |
| 19-8-07 Q009 | OLD_CHUNK3_EXP_19_8_07_Q009 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，若观察到氯气生成，说明 Pb(IV) 能把哪种离子氧化？ |
| 19-8-07 Q010 | OLD_CHUNK3_EXP_19_8_07_Q010 | ['PbO₂ + 浓 HCl', 'PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，本实验最主要的结论方向是哪一项？ |
| 19-8-07 Q011 | OLD_CHUNK3_EXP_19_8_07_Q011 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 与浓 HCl 反应时，Cl⁻ 只被还原而不会被氧化。 |
| 19-8-07 Q013 | OLD_CHUNK3_EXP_19_8_07_Q013 | ['PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 在酸性 MnSO₄ 体系中可把 Mn²⁺ 氧化为更高价态。 |
| 19-8-07 Q016 | OLD_CHUNK3_EXP_19_8_07_Q016 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，浓盐酸中的 Cl⁻ 可被 Pb(IV) 氧化为 Cl₂。 |
| 19-8-07 Q017 | OLD_CHUNK3_EXP_19_8_07_Q017 | ['PbO₂ + 浓 HCl', 'PbO₂ + H₂SO₄ + MnSO₄，水浴加热'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，本实验不涉及任何酸性介质。 |
| 19-8-07 Q018 | OLD_CHUNK3_EXP_19_8_07_Q018 | ['PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，观察 MnO₄⁻ 的生成有助于比较 Pb(IV) 与 MnO₄⁻ 的氧化性。 |
| 19-8-07 Q021 | OLD_CHUNK3_EXP_19_8_07_Q021 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，Pb(IV) 氧化性实验使用的铅(IV)氧化物是____。 |
| 19-8-07 Q022 | OLD_CHUNK3_EXP_19_8_07_Q022 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 与浓 HCl 反应可生成____气。 |
| 19-8-07 Q023 | OLD_CHUNK3_EXP_19_8_07_Q023 | ['PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，酸性 MnSO₄ 体系中被氧化的锰离子是____。 |
| 19-8-07 Q024 | OLD_CHUNK3_EXP_19_8_07_Q024_PF1 | ['PbO₂ + H₂SO₄ + MnSO₄，水浴加热', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂、H₂SO₄ 和 MnSO₄ 水浴加热后若出现紫色，最直接说明哪一判断？ |
| 19-8-07 Q028 | OLD_CHUNK3_EXP_19_8_07_Q028 | ['PbO₂ + 浓 HCl', '比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性'] | 在《19-8-07 Pb(IV) 的氧化性》实验中，Pb(IV) 与 Cl₂ 的氧化性比较通过氧化____离子实现。 |
| 19-8-08 Q001 | OLD_CHUNK3_EXP_19_8_08_Q001 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', '银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，该实验比较还原性的三类中心元素氧化态是哪一组？ |
| 19-8-08 Q003 | OLD_CHUNK3_EXP_19_8_08_Q003 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，代表 As(III) 参与比较的氯化物是哪一种？ |
| 19-8-08 Q004 | OLD_CHUNK3_EXP_19_8_08_Q004 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，代表 Sb(III) 参与比较的氯化物是哪一种？ |
| 19-8-08 Q005 | OLD_CHUNK3_EXP_19_8_08_Q005 | ['银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，代表 Bi(III) 参与比较的硝酸盐是哪一种？ |
| 19-8-08 Q010 | OLD_CHUNK3_EXP_19_8_08_Q010 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', '银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，该实验的核心目的最接近哪一项？ |
| 19-8-08 Q011 | OLD_CHUNK3_EXP_19_8_08_Q011 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', '银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，判断：比较对象为“As(III)、Sb(III)、Bi(III)”。 |
| 19-8-08 Q013 | OLD_CHUNK3_EXP_19_8_08_Q013 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，判断：砷试剂为“AsCl₃”。 |
| 19-8-08 Q014 | OLD_CHUNK3_EXP_19_8_08_Q014 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，判断：锑试剂为“SbCl₅”。 |
| 19-8-08 Q015 | OLD_CHUNK3_EXP_19_8_08_Q015 | ['银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，判断：铋试剂为“Bi(NO₃)₃”。 |
| 19-8-08 Q020 | OLD_CHUNK3_EXP_19_8_08_Q020 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', '银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，判断：实验目的为“测定镁燃烧热”。 |
| 19-8-08 Q021 | OLD_CHUNK3_EXP_19_8_08_Q021_R1 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', '银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，分别把 As(III)、Sb(III)、Bi(III) 物种投入多个氧化体系，主要比较的是哪一项？ |
| 19-8-08 Q023 | OLD_CHUNK3_EXP_19_8_08_Q023 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，比较 As(III) 还原性时可使用____。 |
| 19-8-08 Q024 | OLD_CHUNK3_EXP_19_8_08_Q024 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，比较 Sb(III) 还原性时可使用____。 |
| 19-8-08 Q025 | OLD_CHUNK3_EXP_19_8_08_Q025_PF1 | ['银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，Bi(NO₃)₃ 在本实验中主要出现在下列哪组 Bi(III) 性质比较步骤中？ |
| 19-8-08 Q030 | OLD_CHUNK3_EXP_19_8_08_Q030 | ['碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃', '银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃', 'AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水', 'Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水'] | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，本实验核心是比较三种 III 价物种的____强弱。 |
| 19-8-09 Q001 | OLD_CHUNK3_EXP_19_8_09_Q001 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验比较的高氧化态元素组是哪一项？ |
| 19-8-09 Q007 | OLD_CHUNK3_EXP_19_8_09_Q007 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，下列哪种物质属于本实验列出的 Bi(V) 试剂？ |
| 19-8-09 Q009 | OLD_CHUNK3_EXP_19_8_09_Q009 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，安全知识提示使用砷、锑、铋化合物时应注意什么？ |
| 19-8-09 Q010 | OLD_CHUNK3_EXP_19_8_09_Q010 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，下列哪项不是本实验的合理内容？ |
| 19-8-09 Q011 | OLD_CHUNK3_EXP_19_8_09_Q011 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验比较 As(V)、Sb(V)、Bi(V) 的氧化性。 |
| 19-8-09 Q013 | OLD_CHUNK3_EXP_19_8_09_Q013 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，NaBiO₃ 是本实验列出的 Bi(V) 相关试剂。 |
| 19-8-09 Q017 | OLD_CHUNK3_EXP_19_8_09_Q017_R1 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，砷化合物安全风险较高，实验后废液应集中处理。 |
| 19-8-09 Q018 | OLD_CHUNK3_EXP_19_8_09_Q018 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验只研究 As(III)、Sb(III)、Bi(III) 的还原性，不涉及高价态氧化性。 |
| 19-8-09 Q020 | OLD_CHUNK3_EXP_19_8_09_Q020_R1 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，酸化条件会影响许多氧化还原反应的方向和现象。 |
| 19-8-09 Q021 | OLD_CHUNK3_EXP_19_8_09_Q021 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验比较 As(V)、Sb(V)、____(V) 的氧化性。 |
| 19-8-09 Q024 | OLD_CHUNK3_EXP_19_8_09_Q024 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验列出的 Bi(V) 试剂之一是____。 |
| 19-8-09 Q027 | OLD_CHUNK3_EXP_19_8_09_Q027 | ['Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄', 'Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应'] | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，可溶性砷化合物毒性强，废液应集中____。 |
| 19-8-10 Q010 | OLD_CHUNK3_EXP_19_8_10_Q010 | ['Sn(II) 的还原性：HgCl₂ + SnCl₂', 'Pb(IV) 的氧化性：PbO₂ + H₂SO₄ + MnSO₄，水浴加热', 'Bi(III)/Bi(V) 氧化还原性'] | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，本实验围绕 Sn、Pb、Bi 的不同价态，核心比较的是哪类性质？ |
| 19-8-10 Q020 | OLD_CHUNK3_EXP_19_8_10_Q020 | ['Sn(II) 的还原性：HgCl₂ + SnCl₂', 'Pb(IV) 的氧化性：PbO₂ + H₂SO₄ + MnSO₄，水浴加热', 'Bi(III)/Bi(V) 氧化还原性'] | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，本实验主题是镍(II)与丁二酮肟的鉴定。 |
| 19-8-10 Q030 | OLD_CHUNK3_EXP_19_8_10_Q030 | ['Sn(II) 的还原性：HgCl₂ + SnCl₂', 'Pb(IV) 的氧化性：PbO₂ + H₂SO₄ + MnSO₄，水浴加热', 'Bi(III)/Bi(V) 氧化还原性'] | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，本实验核心比较不同价态离子的____。 |
| 19-8-11 Q006 | OLD_CHUNK3_EXP_19_8_11_Q006_R1 | ['设计分析铅丹 Pb₃O₄ 组成的实验方法', 'Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》中，Pb₃O₄ 与 HNO₃ 微热后吸取清液，再用稀 H₂SO₄ 检查 Pb²⁺，这一设计最直接服务于哪一目标？ |
| 19-8-11 Q007 | OLD_CHUNK3_EXP_19_8_11_Q007_R1_PF1 | ['Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》实验中，Pb₃O₄ 与 HNO₃ 微热后，为什么还要吸取清液并用稀 H₂SO₄ 检查？ |
| 19-8-11 Q009 | OLD_CHUNK3_EXP_19_8_11_Q009 | ['Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》中，如果 Pb₃O₄ 中 Pb(II) 进入硝酸清液，加入稀 H₂SO₄ 的目的最接近哪一项？ |
| 19-8-11 Q010 | OLD_CHUNK3_EXP_19_8_11_Q010_SF1 | ['设计分析铅丹 Pb₃O₄ 组成的实验方法', 'Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》中，下列哪一组步骤都属于铅丹 Pb₃O₄ 组成分析这条正式点位链？ |
| 19-8-11 Q015 | OLD_CHUNK3_EXP_19_8_11_Q015_R1 | ['设计分析铅丹 Pb₃O₄ 组成的实验方法', 'Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》中，Pb₃O₄ 与 HNO₃ 微热以及取清液用稀 H₂SO₄ 检查 Pb²⁺，属于分析铅丹组成的同一证据链。 |
| 19-8-11 Q019 | OLD_CHUNK3_EXP_19_8_11_Q019_R1_PF1 | ['Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》实验中，用稀 H₂SO₄ 检查的是 HNO₃ 处理后清液中的 Pb²⁺，不是 SbCl₃ 与 Bi(NO₃)₃ 的分离鉴定步骤。 |
| 19-8-11 Q020 | OLD_CHUNK3_EXP_19_8_11_Q020_R1_PF1 | ['设计分析铅丹 Pb₃O₄ 组成的实验方法', 'Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》实验中，若省去清液的稀 H₂SO₄ 检查，仅凭 Pb₃O₄ 与 HNO₃ 微热不能完成 Pb²⁺ 证据确认。 |
| 19-8-11 Q027 | OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | ['Pb₃O₄ + HNO₃，微热', '吸取清液，用稀 H₂SO₄ 检查 Pb²⁺'] | 在《19-8-11 小设计实验》实验中，吸取清液而不是直接处理残渣，更接近哪一项实验意图？ |
| 20-1-01 Q001 | OLD_CHUNK3_EXP_20_1_01_Q001 | ['CuSO₄ + NaOH', 'AgNO₃ + NaOH', 'ZnSO₄ + NaOH', 'CdSO₄ + NaOH', 'Hg(NO₃)₂ + NaOH'] | 在《20-1-01 氢氧化物的生成与性质》实验中，本实验向多种金属盐溶液中滴加的共同试剂是哪一种？ |
| 20-1-01 Q002 | OLD_CHUNK3_EXP_20_1_01_Q002 | ['CuSO₄ + NaOH', 'AgNO₃ + NaOH', 'ZnSO₄ + NaOH', 'CdSO₄ + NaOH', 'Hg(NO₃)₂ + NaOH'] | 在《20-1-01 氢氧化物的生成与性质》实验中，下列哪组金属盐全部属于本实验列出的对象？ |
| 20-1-01 Q003 | OLD_CHUNK3_EXP_20_1_01_Q003 | ['比较沉淀颜色、形态', 'CuSO₄ + NaOH', 'AgNO₃ + NaOH', 'ZnSO₄ + NaOH', 'CdSO₄ + NaOH', 'Hg(NO₃)₂ + NaOH'] | 在《20-1-01 氢氧化物的生成与性质》实验中，滴加 NaOH 后首先需要观察沉淀的哪两类外观？ |
| 20-1-01 Q004 | OLD_CHUNK3_EXP_20_1_01_Q004 | ['ZnSO₄ + NaOH', '检验沉淀酸碱性'] | 在《20-1-01 氢氧化物的生成与性质》实验中，ZnSO₄ 与 NaOH 生成的 Zn(OH)₂ 常用于说明哪类性质？ |
| 20-1-01 Q005 | OLD_CHUNK3_EXP_20_1_01_Q005 | ['CuSO₄ + NaOH', '比较沉淀颜色、形态'] | 在《20-1-01 氢氧化物的生成与性质》实验中，CuSO₄ 与 NaOH 反应常生成哪种颜色的氢氧化铜沉淀？ |
| 20-1-01 Q006 | OLD_CHUNK3_EXP_20_1_01_Q006 | ['AgNO₃ + NaOH', '比较沉淀颜色、形态'] | 在《20-1-01 氢氧化物的生成与性质》实验中，AgNO₃ 与 NaOH 反应时，银的氢氧化物常不稳定，常观察到哪类银氧化物沉淀？ |
| 20-1-01 Q007 | OLD_CHUNK3_EXP_20_1_01_Q007 | ['检验沉淀酸碱性', '检验沉淀热稳定性'] | 在《20-1-01 氢氧化物的生成与性质》实验中，本实验除生成沉淀外，还要求试验沉淀的哪两项性质？ |
| 20-1-01 Q008 | OLD_CHUNK3_EXP_20_1_01_Q008 | ['CuSO₄ + NaOH', 'ZnSO₄ + NaOH', 'Hg(NO₃)₂ + NaOH'] | 在《20-1-01 氢氧化物的生成与性质》实验中，下列哪一项不是本实验的主要金属盐？ |
| 20-1-01 Q009 | OLD_CHUNK3_EXP_20_1_01_Q009 | ['CdSO₄ + NaOH', 'ZnSO₄ + NaOH', '检验沉淀酸碱性'] | 在《20-1-01 氢氧化物的生成与性质》实验中，CdSO₄ 加 NaOH 生成的 Cd(OH)₂ 与 Zn(OH)₂ 对比，常用于比较哪类差异？ |
| 20-1-01 Q010 | OLD_CHUNK3_EXP_20_1_01_Q010_SF1 | ['检验沉淀酸碱性', '检验沉淀热稳定性'] | 在《20-1-01 氢氧化物的生成与性质》实验中，除滴加 NaOH 生成沉淀外，教材还要求继续检验沉淀的哪两类性质？ |
| 20-1-01 Q011 | OLD_CHUNK3_EXP_20_1_01_Q011 | ['CuSO₄ + NaOH', 'AgNO₃ + NaOH', 'ZnSO₄ + NaOH', 'CdSO₄ + NaOH', 'Hg(NO₃)₂ + NaOH'] | 在《20-1-01 氢氧化物的生成与性质》实验中，本实验共同滴加的是浓硝酸而不是 NaOH。 |
| 20-1-01 Q012 | OLD_CHUNK3_EXP_20_1_01_Q012 | ['检验沉淀酸碱性', '检验沉淀热稳定性'] | 在《20-1-01 氢氧化物的生成与性质》实验中，观察沉淀酸碱性和热稳定性不属于本实验内容。 |
- 另有 11 道多点位题未展开。

## 填空题手机端风险列表
### 本轮已改写的高风险填空
| review_id | 实验编号 | 新题干 |
| --- | --- | --- |
| OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | 19-6-02 | 在《19-6-02 金属镁燃烧》实验中，与其让学生直接填写 O₂，更能体现本实验观察目的的是哪一项？ |
| OLD_CHUNK3_EXP_19_8_02_Q022_PF1 | 19-8-02 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 后，继续分别加入 HCl 和过量 NaOH，最主要是为了判断什么？ |
| OLD_CHUNK3_EXP_19_8_03_Q023_PF1 | 19-8-03 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 生成 Sb(OH)₃ 后，继续比较 HCl、2 mol/L NaOH 和 6 mol/L NaOH 的作用，最主要是为了判断什么？ |
| OLD_CHUNK3_EXP_19_8_04_Q030_PF1 | 19-8-04 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 生成 Bi(OH)₃ 只是第一步，后续还需比较其与 HCl、6 mol/L NaOH 和 40% NaOH 的作用。 |
| OLD_CHUNK3_EXP_19_8_06_Q025_PF1 | 19-8-06 | 在《19-8-06 Sn(II) 的还原性》实验中，SnCl₂ 与 HgCl₂ 反应中先出现白色沉淀、过量 SnCl₂ 时可继续变暗，这组现象主要说明什么？ |
| OLD_CHUNK3_EXP_19_8_07_Q024_PF1 | 19-8-07 | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂、H₂SO₄ 和 MnSO₄ 水浴加热后若出现紫色，最直接说明哪一判断？ |
| OLD_CHUNK3_EXP_19_8_08_Q025_PF1 | 19-8-08 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，Bi(NO₃)₃ 在本实验中主要出现在下列哪组 Bi(III) 性质比较步骤中？ |
| OLD_CHUNK3_EXP_19_8_09_Q028_PF1 | 19-8-09 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，酸性 MnSO₄ 体系出现紫色，更能说明哪一类证据？ |
| OLD_CHUNK3_EXP_19_8_10_Q027_PF1 | 19-8-10 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，加入 KI 和 CCl₄ 后出现紫色有机层，在本实验中最直接支持哪一判断？ |
| OLD_CHUNK3_EXP_19_8_11_Q026_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 检查 Pb²⁺ 时，最关键的可观察依据是哪一项？ |
| OLD_CHUNK3_EXP_19_8_11_Q027_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，吸取清液而不是直接处理残渣，更接近哪一项实验意图？ |
| OLD_CHUNK3_EXP_19_8_11_Q028_R1_PF1 | 19-8-11 | 在《19-8-11 小设计实验》实验中，稀 H₂SO₄ 步骤的判断对象是清液中的 Pb²⁺，而不是检验 HNO₃ 本身。 |
| OLD_CHUNK3_EXP_20_1_01_Q024_PF1 | 20-1-01 | 在《20-1-01 氢氧化物的生成与性质》实验中，AgNO₃ 与 NaOH 步骤中观察到棕黑色 Ag₂O，更直接说明哪一事实？ |
### 最终仍保留的符号/别名填空风险
- 数量：85。这些题仍为短答案、normalized_exact 判分；保留是因为答案有中文别名或唯一短 token，且不是本轮最差风险批次。
| 题号 | review_id | 有效题干 | accepted_answers |
| --- | --- | --- | --- |
| 19-6-03 Q021 | OLD_CHUNK3_EXP_19_6_03_Q021 | 在《19-6-03 与水的作用》实验中，金属钠与水反应生成的气体是____。 | ['H₂', '氢气'] |
| 19-6-03 Q022 | OLD_CHUNK3_EXP_19_6_03_Q022 | 在《19-6-03 与水的作用》实验中，金属钠与水反应后溶液呈____性。 | ['碱', '碱性'] |
| 19-6-03 Q024 | OLD_CHUNK3_EXP_19_6_03_Q024 | 在《19-6-03 与水的作用》实验中，碱金属中，钾与水通常比____与水反应更剧烈。 | ['钠', 'Na'] |
| 19-6-03 Q025 | OLD_CHUNK3_EXP_19_6_03_Q025 | 在《19-6-03 与水的作用》实验中，镁条与水反应前需用砂纸除去表面____膜。 | ['氧化', '氧化膜'] |
| 19-6-03 Q026 | OLD_CHUNK3_EXP_19_6_03_Q026 | 在《19-6-03 与水的作用》实验中，镁条分别放入冷水和____水中以比较反应不同。 | ['热', '热水'] |
| 19-6-03 Q027 | OLD_CHUNK3_EXP_19_6_03_Q027 | 在《19-6-03 与水的作用》实验中，金属钙与水反应生成的碱可写作____。 | ['Ca(OH)₂', '氢氧化钙'] |
| 19-6-03 Q029 | OLD_CHUNK3_EXP_19_6_03_Q029 | 在《19-6-03 与水的作用》实验中，钠与水反应可写出碱金属与水反应生成碱和____。 | ['氢气', 'H₂'] |
| 19-6-03 Q030 | OLD_CHUNK3_EXP_19_6_03_Q030 | 在《19-6-03 与水的作用》实验中，本实验比较的是碱金属、碱土金属的____性。 | ['活泼', '活泼性'] |
| 19-6-04 Q025 | OLD_CHUNK3_EXP_19_6_04_Q025 | 在《19-6-04 焰色反应》实验中，Li⁺ 的焰色常为____。 | ['洋红色', '胭脂红', '红色'] |
| 19-6-04 Q026 | OLD_CHUNK3_EXP_19_6_04_Q026 | 在《19-6-04 焰色反应》实验中，Ca²⁺ 的焰色常为____。 | ['砖红色', '橙红色'] |
| 19-6-04 Q027 | OLD_CHUNK3_EXP_19_6_04_Q027 | 在《19-6-04 焰色反应》实验中，Sr²⁺ 的焰色常为____。 | ['红色', '猩红色'] |
| 19-6-04 Q028 | OLD_CHUNK3_EXP_19_6_04_Q028 | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色常为____。 | ['黄绿色', '苹果绿色'] |
| 19-6-04 Q029 | OLD_CHUNK3_EXP_19_6_04_Q029 | 在《19-6-04 焰色反应》实验中，焰色反应源于电子受激发后跃迁____。 | ['发光', '释放光'] |
| 19-6-04 Q030 | OLD_CHUNK3_EXP_19_6_04_Q030 | 在《19-6-04 焰色反应》实验中，本实验常用 LiCl、NaCl、KCl 等____溶液。 | ['氯化物', '氯化物盐'] |
| 19-8-01 Q021 | OLD_CHUNK3_EXP_19_8_01_Q021 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(NO₃)₂ 溶液中滴加 NaOH 生成的沉淀是____。 | ['Pb(OH)₂', '氢氧化铅'] |
| 19-8-01 Q022 | OLD_CHUNK3_EXP_19_8_01_Q022 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，生成 Pb(OH)₂ 时使用的铅盐是____。 | ['Pb(NO₃)₂', '硝酸铅'] |
| 19-8-01 Q024 | OLD_CHUNK3_EXP_19_8_01_Q024 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，实验中用于生成沉淀和测试碱中溶解性的碱是____。 | ['NaOH', '氢氧化钠'] |
| 19-8-01 Q025 | OLD_CHUNK3_EXP_19_8_01_Q025 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，试验 Pb(OH)₂ 与酸反应时使用的酸是____。 | ['HNO₃', '硝酸'] |
| 19-8-01 Q026 | OLD_CHUNK3_EXP_19_8_01_Q026 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(NO₃)₂ 提供的金属离子是____。 | ['Pb²⁺', '铅离子'] |
| 19-8-01 Q029 | OLD_CHUNK3_EXP_19_8_01_Q029 | 在《19-8-01 Pb(OH)₂ 的生成与性质》实验中，Pb(OH)₂ 的生成属于____反应现象。 | ['沉淀', '沉淀生成'] |
| 19-8-02 Q021 | OLD_CHUNK3_EXP_19_8_02_Q021 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 的锡(II)盐常用____溶液。 | ['SnCl₂', '氯化亚锡'] |
| 19-8-02 Q023 | OLD_CHUNK3_EXP_19_8_02_Q023 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 与____反应可体现其碱性一面。 | ['HCl', '盐酸'] |
| 19-8-02 Q024 | OLD_CHUNK3_EXP_19_8_02_Q024 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 溶于过量____可体现其酸性一面。 | ['NaOH', '氢氧化钠'] |
| 19-8-02 Q026 | OLD_CHUNK3_EXP_19_8_02_Q026 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 中 Sn 的氧化态为____。 | ['+2', '正二价'] |
| 19-8-02 Q027 | OLD_CHUNK3_EXP_19_8_02_Q027 | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，SnCl₂ 与 NaOH 反应首先观察到的是____生成。 | ['沉淀', '白色沉淀'] |
| 19-8-03 Q021 | OLD_CHUNK3_EXP_19_8_03_Q021 | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，生成 Sb(OH)₃ 的起始锑盐可用____。 | ['SbCl₃'] |
| 19-8-04 Q021 | OLD_CHUNK3_EXP_19_8_04_Q021 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，生成 Bi(OH)₃ 时，Bi(NO₃)₃ 溶液中滴加____溶液。 | ['NaOH', '氢氧化钠'] |
| 19-8-04 Q022 | OLD_CHUNK3_EXP_19_8_04_Q022 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与____反应可体现其碱性。 | ['HCl', '盐酸'] |
| 19-8-04 Q025 | OLD_CHUNK3_EXP_19_8_04_Q025 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 反应生成的沉淀含有____离子。 | ['Bi³⁺', '铋(III)'] |
| 19-8-04 Q026 | OLD_CHUNK3_EXP_19_8_04_Q026 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与酸反应生成盐和____。 | ['水', 'H₂O'] |
| 19-8-04 Q028 | OLD_CHUNK3_EXP_19_8_04_Q028 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，使用铋化合物后，废液应集中____处理。 | ['回收', '回收处理'] |
| 19-8-04 Q029 | OLD_CHUNK3_EXP_19_8_04_Q029 | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 在碱中不易溶时，说明其两性相对较____。 | ['弱', '不明显'] |
| 19-8-05 Q021 | OLD_CHUNK3_EXP_19_8_05_Q021 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sn(OH)₂ 时向 SnCl₂ 溶液滴加____溶液。 | ['NaOH', '氢氧化钠'] |
| 19-8-05 Q022 | OLD_CHUNK3_EXP_19_8_05_Q022 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Pb(OH)₂ 时使用____溶液。 | ['Pb(NO₃)₂', '硝酸铅'] |
| 19-8-05 Q023 | OLD_CHUNK3_EXP_19_8_05_Q023 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sb(OH)₃ 时使用____溶液。 | ['SbCl₃', '三氯化锑'] |
| 19-8-05 Q024 | OLD_CHUNK3_EXP_19_8_05_Q024 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Bi(OH)₃ 时使用____溶液。 | ['Bi(NO₃)₃', '硝酸铋'] |
| 19-8-05 Q025 | OLD_CHUNK3_EXP_19_8_05_Q025 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 沉淀分别试验与 HCl 和____溶液的反应。 | ['NaOH', '氢氧化钠'] |
| 19-8-05 Q029 | OLD_CHUNK3_EXP_19_8_05_Q029 | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sb(OH)₃ 步骤比较不同 NaOH 浓度下沉淀的____。 | ['溶解情况', '溶解性'] |
| 19-8-06 Q021 | OLD_CHUNK3_EXP_19_8_06_Q021 | 在《19-8-06 Sn(II) 的还原性》实验中，FeCl₃ 溶液中滴加的还原剂是____。 | ['SnCl₂', '氯化亚锡'] |
| 19-8-06 Q022 | OLD_CHUNK3_EXP_19_8_06_Q022 | 在《19-8-06 Sn(II) 的还原性》实验中，检验 Fe³⁺ 是否仍存在的试剂是____。 | ['KSCN', '硫氰酸钾'] |
| 19-8-06 Q023 | OLD_CHUNK3_EXP_19_8_06_Q023 | 在《19-8-06 Sn(II) 的还原性》实验中，Fe³⁺ 被 Sn(II) 还原后生成____。 | ['Fe²⁺', '亚铁离子'] |
| 19-8-06 Q024 | OLD_CHUNK3_EXP_19_8_06_Q024 | 在《19-8-06 Sn(II) 的还原性》实验中，Sn(II) 作还原剂时通常被氧化为____。 | ['Sn(IV)', 'Sn⁴⁺'] |
| 19-8-06 Q026 | OLD_CHUNK3_EXP_19_8_06_Q026 | 在《19-8-06 Sn(II) 的还原性》实验中，SnCl₂ 过量时，汞(I)还可能被进一步还原为金属____。 | ['Hg', '汞'] |
| 19-8-06 Q028 | OLD_CHUNK3_EXP_19_8_06_Q028 | 在《19-8-06 Sn(II) 的还原性》实验中，该实验通过 SnCl₂ 与 FeCl₃ 反应比较 Sn(II) 与____的还原性。 | ['Fe(II)', 'Fe²⁺', '亚铁'] |
| 19-8-06 Q029 | OLD_CHUNK3_EXP_19_8_06_Q029 | 在《19-8-06 Sn(II) 的还原性》实验中，HgCl₂ 中汞的初始价态为____。 | ['+2', '二价', 'Hg(II)'] |
| 19-8-07 Q021 | OLD_CHUNK3_EXP_19_8_07_Q021 | 在《19-8-07 Pb(IV) 的氧化性》实验中，Pb(IV) 氧化性实验使用的铅(IV)氧化物是____。 | ['PbO₂', '二氧化铅'] |
| 19-8-07 Q022 | OLD_CHUNK3_EXP_19_8_07_Q022 | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 与浓 HCl 反应可生成____气。 | ['Cl₂', '氯气'] |
| 19-8-07 Q023 | OLD_CHUNK3_EXP_19_8_07_Q023 | 在《19-8-07 Pb(IV) 的氧化性》实验中，酸性 MnSO₄ 体系中被氧化的锰离子是____。 | ['Mn²⁺', '锰(II)离子'] |
| 19-8-07 Q025 | OLD_CHUNK3_EXP_19_8_07_Q025 | 在《19-8-07 Pb(IV) 的氧化性》实验中，第二个实验中酸化所用酸为____。 | ['H₂SO₄', '硫酸'] |
| 19-8-07 Q027 | OLD_CHUNK3_EXP_19_8_07_Q027 | 在《19-8-07 Pb(IV) 的氧化性》实验中，PbO₂ 在本实验中作____剂。 | ['氧化', '氧化剂'] |
| 19-8-07 Q028 | OLD_CHUNK3_EXP_19_8_07_Q028 | 在《19-8-07 Pb(IV) 的氧化性》实验中，Pb(IV) 与 Cl₂ 的氧化性比较通过氧化____离子实现。 | ['Cl⁻', '氯离子'] |
| 19-8-07 Q029 | OLD_CHUNK3_EXP_19_8_07_Q029 | 在《19-8-07 Pb(IV) 的氧化性》实验中，MnSO₄ 提供被氧化的____元素。 | ['锰', 'Mn'] |
| 19-8-07 Q030 | OLD_CHUNK3_EXP_19_8_07_Q030 | 在《19-8-07 Pb(IV) 的氧化性》实验中，本实验主题是 Pb(IV) 的____性。 | ['氧化', '氧化性'] |
| 19-8-08 Q022 | OLD_CHUNK3_EXP_19_8_08_Q022 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，碱性体系中可加入____观察还原性差异。 | ['KMnO₄'] |
| 19-8-08 Q023 | OLD_CHUNK3_EXP_19_8_08_Q023 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，比较 As(III) 还原性时可使用____。 | ['AsCl₃'] |
| 19-8-08 Q024 | OLD_CHUNK3_EXP_19_8_08_Q024 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，比较 Sb(III) 还原性时可使用____。 | ['SbCl₃'] |
| 19-8-08 Q026 | OLD_CHUNK3_EXP_19_8_08_Q026 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，银氨溶液中若有还原性，可使 Ag⁺ 被还原为____。 | ['银', 'Ag'] |
| 19-8-08 Q027 | OLD_CHUNK3_EXP_19_8_08_Q027 | 在《19-8-08 As(III)、Sb(III)、Bi(III) 的还原性》实验中，弱酸性碘水实验考察 As(III)、Sb(III) 对____的还原作用。 | ['I₂'] |
| 19-8-09 Q021 | OLD_CHUNK3_EXP_19_8_09_Q021 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验比较 As(V)、Sb(V)、____(V) 的氧化性。 | ['Bi', '铋'] |
| 19-8-09 Q022 | OLD_CHUNK3_EXP_19_8_09_Q022 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，酸化后加入 KI 时，若被氧化会生成____。 | ['I₂', '碘'] |
| 19-8-09 Q023 | OLD_CHUNK3_EXP_19_8_09_Q023 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，加入____可萃取生成的碘，便于观察。 | ['CCl₄', '四氯化碳'] |
| 19-8-09 Q024 | OLD_CHUNK3_EXP_19_8_09_Q024 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验列出的 Bi(V) 试剂之一是____。 | ['NaBiO₃', '铋酸钠'] |
| 19-8-09 Q025 | OLD_CHUNK3_EXP_19_8_09_Q025 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，本实验还用酸性____体系比较高价砷、锑、铋的氧化性。 | ['MnSO₄', '硫酸锰'] |
| 19-8-09 Q026 | OLD_CHUNK3_EXP_19_8_09_Q026 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，KI 中起还原作用的离子是____。 | ['I⁻', '碘离子'] |
| 19-8-09 Q027 | OLD_CHUNK3_EXP_19_8_09_Q027 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，可溶性砷化合物毒性强，废液应集中____。 | ['回收', '回收处理'] |
| 19-8-09 Q029 | OLD_CHUNK3_EXP_19_8_09_Q029 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，Na[As(OH)₆] 中砷为____价。 | ['+5', 'V', '五'] |
| 19-8-09 Q030 | OLD_CHUNK3_EXP_19_8_09_Q030 | 在《19-8-09 As(V)、Sb(V)、Bi(V) 的氧化性》实验中，K[Sb(OH)₆] 中锑为____价。 | ['+5', 'V', '五'] |
| 19-8-10 Q021 | OLD_CHUNK3_EXP_19_8_10_Q021 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，检验 Sn(II) 还原性时向 HgCl₂ 溶液滴加____溶液。 | ['SnCl₂', '氯化亚锡'] |
| 19-8-10 Q022 | OLD_CHUNK3_EXP_19_8_10_Q022 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，SnCl₂ 与 FeCl₃ 反应后可用____溶液检验 Fe³⁺。 | ['KSCN', '硫氰酸钾'] |
| 19-8-10 Q023 | OLD_CHUNK3_EXP_19_8_10_Q023 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，Pb(IV) 氧化性实验常用固体____。 | ['PbO₂', '二氧化铅'] |
| 19-8-10 Q024 | OLD_CHUNK3_EXP_19_8_10_Q024 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，PbO₂ 与浓盐酸反应可生成____气体。 | ['Cl₂', '氯气'] |
| 19-8-10 Q025 | OLD_CHUNK3_EXP_19_8_10_Q025 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，PbO₂ 在酸性介质中可将 Mn²⁺ 氧化为____。 | ['MnO₄⁻', '高锰酸根'] |
| 19-8-10 Q028 | OLD_CHUNK3_EXP_19_8_10_Q028 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，NaBiO₃ 酸性氧化 Mn²⁺ 说明 Bi(V) 具有____。 | ['强氧化性', '氧化性'] |
| 19-8-10 Q029 | OLD_CHUNK3_EXP_19_8_10_Q029 | 在《19-8-10 Sn、Pb、Bi 不同价态离子的氧化还原性》实验中，试验 PbO₂ 与 KI 时不宜用____酸化。 | ['HNO₃', '硝酸'] |
| 19-8-11 Q021 | OLD_CHUNK3_EXP_19_8_11_Q021 | 在《19-8-11 小设计实验》中，铅丹的化学式是____。 | ['Pb₃O₄', '四氧化三铅'] |
| 19-8-11 Q022 | OLD_CHUNK3_EXP_19_8_11_Q022 | 在《19-8-11 小设计实验》中，铅丹组成分析候选步骤中，Pb₃O₄ 先与____微热。 | ['HNO₃', '硝酸'] |
| 19-8-11 Q023 | OLD_CHUNK3_EXP_19_8_11_Q023 | 在《19-8-11 小设计实验》中，吸取清液后，用稀____检查 Pb²⁺。 | ['H₂SO₄', '硫酸'] |
| 19-8-11 Q024 | OLD_CHUNK3_EXP_19_8_11_Q024 | 在《19-8-11 小设计实验》中，Pb²⁺ 与 SO₄²⁻ 形成的难溶沉淀是____。 | ['PbSO₄', '硫酸铅'] |
| 19-8-11 Q025 | OLD_CHUNK3_EXP_19_8_11_Q025 | 在《19-8-11 小设计实验》中，Pb₃O₄ 可用于讨论 Pb(II) 和____两种价态。 | ['Pb(IV)', 'Pb⁴⁺', '四价铅'] |
| 19-8-11 Q030 | OLD_CHUNK3_EXP_19_8_11_Q030 | 在《19-8-11 小设计实验》中，用稀 H₂SO₄ 检查 Pb²⁺ 的关键离子是____。 | ['SO₄²⁻', '硫酸根'] |
| 20-1-01 Q021 | OLD_CHUNK3_EXP_20_1_01_Q021 | 在《20-1-01 氢氧化物的生成与性质》实验中，本实验共同滴加的碱是____溶液。 | ['NaOH', '氢氧化钠'] |
| 20-1-01 Q022 | OLD_CHUNK3_EXP_20_1_01_Q022 | 在《20-1-01 氢氧化物的生成与性质》实验中，CuSO₄ 与 NaOH 生成的 Cu(OH)₂ 常为____色沉淀。 | ['蓝', '蓝色'] |
| 20-1-01 Q023 | OLD_CHUNK3_EXP_20_1_01_Q023 | 在《20-1-01 氢氧化物的生成与性质》实验中，ZnSO₄ 与 NaOH 生成的两性氢氧化物是____。 | ['Zn(OH)₂', '氢氧化锌'] |
| 20-1-01 Q027 | OLD_CHUNK3_EXP_20_1_01_Q027 | 在《20-1-01 氢氧化物的生成与性质》实验中，CdSO₄ 与 NaOH 生成的主要沉淀可写为____。 | ['Cd(OH)₂', '氢氧化镉'] |
| 20-1-01 Q028 | OLD_CHUNK3_EXP_20_1_01_Q028 | 在《20-1-01 氢氧化物的生成与性质》实验中，Hg(NO₃)₂ 与 NaOH 反应涉及的汞元素为____价。 | ['+2', '正二价'] |

## theory-dependent 题目列表
- 数量：368。只在颜色、产物、价态、酸碱性、氧化还原方向、难溶性等判断超出实验步骤原文时引用 theory；纯步骤/对象题已清空泛化 theory。
| 题号 | review_id | supporting_theory_chunk_ids | 有效题干 |
| --- | --- | --- | --- |
| 19-6-02 Q004 | OLD_CHUNK3_EXP_19_6_02_Q004 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，镁在空气中燃烧的主要白色产物是哪一种？ |
| 19-6-02 Q006 | OLD_CHUNK3_EXP_19_6_02_Q006 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，镁在空气中燃烧时，主要氧化镁的氧化剂是哪一种？ |
| 19-6-02 Q010 | OLD_CHUNK3_EXP_19_6_02_Q010 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，镁燃烧后收集到的氧化镁通常呈什么颜色？ |
| 19-6-02 Q014 | OLD_CHUNK3_EXP_19_6_02_Q014 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，判断：主要产物为“MgCl₂”。 |
| 19-6-02 Q016 | OLD_CHUNK3_EXP_19_6_02_Q016 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，判断：氧化剂为“NaOH”。 |
| 19-6-02 Q020 | OLD_CHUNK3_EXP_19_6_02_Q020 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，判断：产物颜色为“深蓝色”。 |
| 19-6-02 Q024 | OLD_CHUNK3_EXP_19_6_02_Q024 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，镁在氧气中燃烧主要生成____。 |
| 19-6-02 Q026 | OLD_CHUNK3_EXP_19_6_02_Q026_PF1 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，与其让学生直接填写 O₂，更能体现本实验观察目的的是哪一项？ |
| 19-6-02 Q030 | OLD_CHUNK3_EXP_19_6_02_Q030 | textbook_table_record_table_p158_t01_r011 | 在《19-6-02 金属镁燃烧》实验中，镁燃烧生成的 MgO 通常为____固体。 |
| 19-6-03 Q001 | OLD_CHUNK3_EXP_19_6_03_Q001 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，金属钠与水反应后，溶液通常呈什么性？ |
| 19-6-03 Q002 | OLD_CHUNK3_EXP_19_6_03_Q002 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，金属钠与水反应的气体产物主要是什么？ |
| 19-6-03 Q004 | OLD_CHUNK3_EXP_19_6_03_Q004 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，钾与水反应通常比钠与水反应怎样？ |
| 19-6-03 Q005 | OLD_CHUNK3_EXP_19_6_03_Q005 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，镁条分别放入冷水和热水中，是为了比较什么？ |
| 19-6-03 Q006 | OLD_CHUNK3_EXP_19_6_03_Q006 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，金属钙与水反应后，检验溶液酸碱性的目的是什么？ |
| 19-6-03 Q008 | OLD_CHUNK3_EXP_19_6_03_Q008 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，下列金属与水反应最剧烈的一般是？ |
| 19-6-03 Q010 | OLD_CHUNK3_EXP_19_6_03_Q010 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，本实验通过钠、镁、钙等与水反应，主要比较什么？ |
| 19-6-03 Q011 | OLD_CHUNK3_EXP_19_6_03_Q011 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，钠与水反应生成氢气和碱性溶液。 |
| 19-6-03 Q012 | OLD_CHUNK3_EXP_19_6_03_Q012 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，钾与水反应通常比钠与水反应更剧烈，实际实验应更严格控制安全风险。 |
| 19-6-03 Q013 | OLD_CHUNK3_EXP_19_6_03_Q013 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，镁条在热水中通常比在冷水中更容易反应。 |
| 19-6-03 Q014 | OLD_CHUNK3_EXP_19_6_03_Q014 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，钙与水反应后溶液应检验酸碱性。 |
| 19-6-03 Q019 | OLD_CHUNK3_EXP_19_6_03_Q019_R1 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，钠、钙与水反应都可能产生 H₂。 |
| 19-6-03 Q020 | OLD_CHUNK3_EXP_19_6_03_Q020_R1 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，本实验属于碱金属、碱土金属活泼性比较的一部分。 |
| 19-6-03 Q021 | OLD_CHUNK3_EXP_19_6_03_Q021 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，金属钠与水反应生成的气体是____。 |
| 19-6-03 Q022 | OLD_CHUNK3_EXP_19_6_03_Q022 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，金属钠与水反应后溶液呈____性。 |
| 19-6-03 Q024 | OLD_CHUNK3_EXP_19_6_03_Q024 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，碱金属中，钾与水通常比____与水反应更剧烈。 |
| 19-6-03 Q026 | OLD_CHUNK3_EXP_19_6_03_Q026 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，镁条分别放入冷水和____水中以比较反应不同。 |
| 19-6-03 Q027 | OLD_CHUNK3_EXP_19_6_03_Q027 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，金属钙与水反应生成的碱可写作____。 |
| 19-6-03 Q029 | OLD_CHUNK3_EXP_19_6_03_Q029 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，钠与水反应可写出碱金属与水反应生成碱和____。 |
| 19-6-03 Q030 | OLD_CHUNK3_EXP_19_6_03_Q030 | textbook_prose_00936_0b5113eb41 | 在《19-6-03 与水的作用》实验中，本实验比较的是碱金属、碱土金属的____性。 |
| 19-6-04 Q001 | OLD_CHUNK3_EXP_19_6_04_Q001 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应操作中反复蘸取浓盐酸并灼烧的是哪种金属丝？ |
| 19-6-04 Q002 | OLD_CHUNK3_EXP_19_6_04_Q002 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，镍丝需在氧化焰中烧到何种状态后再蘸取待测液？ |
| 19-6-04 Q003 | OLD_CHUNK3_EXP_19_6_04_Q003 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，K⁺ 焰色常需透过哪种材料观察以减弱钠黄光干扰？ |
| 19-6-04 Q004 | OLD_CHUNK3_EXP_19_6_04_Q004 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Na⁺ 的典型焰色是什么？ |
| 19-6-04 Q005 | OLD_CHUNK3_EXP_19_6_04_Q005 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Li⁺ 的典型焰色最接近哪一种？ |
| 19-6-04 Q006 | OLD_CHUNK3_EXP_19_6_04_Q006 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Ca²⁺ 的焰色通常可描述为哪一种？ |
| 19-6-04 Q007 | OLD_CHUNK3_EXP_19_6_04_Q007 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Sr²⁺ 的焰色通常可描述为哪一种？ |
| 19-6-04 Q008 | OLD_CHUNK3_EXP_19_6_04_Q008 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色通常可描述为哪一种？ |
| 19-6-04 Q009 | OLD_CHUNK3_EXP_19_6_04_Q009 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应的微观原因最接近下列哪一项？ |
| 19-6-04 Q010 | OLD_CHUNK3_EXP_19_6_04_Q010 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，本实验在点滴板上分别滴入的盐溶液多为哪类盐？ |
| 19-6-04 Q011 | OLD_CHUNK3_EXP_19_6_04_Q011 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应前应把镍丝蘸浓盐酸并在氧化焰中烧至近于无色。 |
| 19-6-04 Q012 | OLD_CHUNK3_EXP_19_6_04_Q012 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，K⁺ 焰色观察常透过钴玻璃以减弱钠黄光干扰。 |
| 19-6-04 Q013 | OLD_CHUNK3_EXP_19_6_04_Q013 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Na⁺ 的焰色非常灵敏，常呈黄色。 |
| 19-6-04 Q014 | OLD_CHUNK3_EXP_19_6_04_Q014 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色常可描述为黄绿色。 |
| 19-6-04 Q015 | OLD_CHUNK3_EXP_19_6_04_Q015 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应与金属原子电子受激发和跃迁发光有关。 |
| 19-6-04 Q016 | OLD_CHUNK3_EXP_19_6_04_Q016 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应主要用 CCl₄ 萃取卤素单质来判断。 |
| 19-6-04 Q017 | OLD_CHUNK3_EXP_19_6_04_Q017 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，镍丝无需清洁，残留钠盐不会影响观察。 |
| 19-6-04 Q018 | OLD_CHUNK3_EXP_19_6_04_Q018_R1 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Li⁺、Na⁺、K⁺、Ca²⁺、Sr²⁺、Ba²⁺ 都可作为本实验观察对象。 |
| 19-6-04 Q019 | OLD_CHUNK3_EXP_19_6_04_Q019 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，观察 K⁺ 焰色时钴玻璃的作用是生成 KI 沉淀。 |
| 19-6-04 Q020 | OLD_CHUNK3_EXP_19_6_04_Q020_R1 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，本实验要求记录各离子的火焰颜色。 |
| 19-6-04 Q021 | OLD_CHUNK3_EXP_19_6_04_Q021 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应用____蘸取试液。 |
| 19-6-04 Q022 | OLD_CHUNK3_EXP_19_6_04_Q022 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，镍丝应烧至近于____。 |
| 19-6-04 Q023 | OLD_CHUNK3_EXP_19_6_04_Q023 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，观察 K⁺ 焰色常透过____。 |
| 19-6-04 Q024 | OLD_CHUNK3_EXP_19_6_04_Q024 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Na⁺ 的典型焰色为____。 |
| 19-6-04 Q025 | OLD_CHUNK3_EXP_19_6_04_Q025 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Li⁺ 的焰色常为____。 |
| 19-6-04 Q026 | OLD_CHUNK3_EXP_19_6_04_Q026 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Ca²⁺ 的焰色常为____。 |
| 19-6-04 Q027 | OLD_CHUNK3_EXP_19_6_04_Q027 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Sr²⁺ 的焰色常为____。 |
| 19-6-04 Q028 | OLD_CHUNK3_EXP_19_6_04_Q028 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，Ba²⁺ 的焰色常为____。 |
| 19-6-04 Q029 | OLD_CHUNK3_EXP_19_6_04_Q029 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，焰色反应源于电子受激发后跃迁____。 |
| 19-6-04 Q030 | OLD_CHUNK3_EXP_19_6_04_Q030 | textbook_prose_00982_e84c060b23, textbook_table_record_table_p163_t01_r011 | 在《19-6-04 焰色反应》实验中，本实验常用 LiCl、NaCl、KCl 等____溶液。 |
| 19-8-02 Q001 | OLD_CHUNK3_EXP_19_8_02_Q001 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 沉淀时，常向 SnCl₂ 溶液中加入哪种试剂？ |
| 19-8-02 Q002 | OLD_CHUNK3_EXP_19_8_02_Q002 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，SnCl₂ 与适量 NaOH 反应生成的沉淀主要是下列哪一种？ |
| 19-8-02 Q003 | OLD_CHUNK3_EXP_19_8_02_Q003 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 加入 HCl 后溶解，说明它能与哪类物质反应？ |
| 19-8-02 Q004 | OLD_CHUNK3_EXP_19_8_02_Q004 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 加入过量 NaOH 后可溶解，说明它具有什么性质？ |
| 19-8-02 Q005 | OLD_CHUNK3_EXP_19_8_02_Q005 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验比较 Sn(OH)₂ 对 HCl 和 NaOH 的反应，核心是判断哪一性质？ |
| 19-8-02 Q006 | OLD_CHUNK3_EXP_19_8_02_Q006 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，下列哪一组最符合本实验试剂？ |
| 19-8-02 Q007 | OLD_CHUNK3_EXP_19_8_02_Q007 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 中锡的氧化态是下列哪一种？ |
| 19-8-02 Q008 | OLD_CHUNK3_EXP_19_8_02_Q008 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，若沉淀既能溶于酸又能溶于过量碱，通常称其为哪类氢氧化物？ |
| 19-8-02 Q009 | OLD_CHUNK3_EXP_19_8_02_Q009 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，下列哪一项不是 Sn(OH)₂ 性质实验的合理观察对象？ |
| 19-8-02 Q010 | OLD_CHUNK3_EXP_19_8_02_Q010 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验属于哪一组元素化合物性质实验的内容？ |
| 19-8-02 Q011 | OLD_CHUNK3_EXP_19_8_02_Q011 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 只溶于酸，绝不可能溶于过量 NaOH。 |
| 19-8-02 Q012 | OLD_CHUNK3_EXP_19_8_02_Q012 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，SnCl₂ 与 NaOH 反应生成的目标沉淀是 PbO₂。 |
| 19-8-02 Q013 | OLD_CHUNK3_EXP_19_8_02_Q013 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 能与 HCl 反应并溶解，说明它可表现碱性一面。 |
| 19-8-02 Q014 | OLD_CHUNK3_EXP_19_8_02_Q014 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 能溶于过量 NaOH，说明它具有两性。 |
| 19-8-02 Q015 | OLD_CHUNK3_EXP_19_8_02_Q015 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验的主要试剂是 PbO₂ 和浓盐酸。 |
| 19-8-02 Q016 | OLD_CHUNK3_EXP_19_8_02_Q016 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 中锡为 +4 价。 |
| 19-8-02 Q017 | OLD_CHUNK3_EXP_19_8_02_Q017 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，只观察 SnCl₂ 与 NaOH 是否生成沉淀，还不足以完整说明 Sn(OH)₂ 的两性。 |
| 19-8-02 Q018 | OLD_CHUNK3_EXP_19_8_02_Q018 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，HCl 和 NaOH 分别从酸、碱两方面检验 Sn(OH)₂ 的性质。 |
| 19-8-02 Q019 | OLD_CHUNK3_EXP_19_8_02_Q019 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 与酸碱均不反应，所以不能用酸碱试剂检验。 |
| 19-8-02 Q020 | OLD_CHUNK3_EXP_19_8_02_Q020_SF1 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，只观察 Sn(OH)₂ 沉淀生成，还不足以判断其两性，还需比较它与 HCl 和过量 NaOH 的作用。 |
| 19-8-02 Q021 | OLD_CHUNK3_EXP_19_8_02_Q021 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 的锡(II)盐常用____溶液。 |
| 19-8-02 Q022 | OLD_CHUNK3_EXP_19_8_02_Q022_PF1 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，生成 Sn(OH)₂ 后，继续分别加入 HCl 和过量 NaOH，最主要是为了判断什么？ |
| 19-8-02 Q023 | OLD_CHUNK3_EXP_19_8_02_Q023 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 与____反应可体现其碱性一面。 |
| 19-8-02 Q024 | OLD_CHUNK3_EXP_19_8_02_Q024 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 溶于过量____可体现其酸性一面。 |
| 19-8-02 Q025 | OLD_CHUNK3_EXP_19_8_02_Q025 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，既能与酸反应又能与碱反应的氢氧化物称为____氢氧化物。 |
| 19-8-02 Q026 | OLD_CHUNK3_EXP_19_8_02_Q026 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，Sn(OH)₂ 中 Sn 的氧化态为____。 |
| 19-8-02 Q027 | OLD_CHUNK3_EXP_19_8_02_Q027 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，SnCl₂ 与 NaOH 反应首先观察到的是____生成。 |
| 19-8-02 Q028 | OLD_CHUNK3_EXP_19_8_02_Q028 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，本实验核心是 Sn(OH)₂ 的生成与____。 |
| 19-8-02 Q029 | OLD_CHUNK3_EXP_19_8_02_Q029 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，HCl 检验 Sn(OH)₂ 与____的反应。 |
| 19-8-02 Q030 | OLD_CHUNK3_EXP_19_8_02_Q030 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b | 在《19-8-02 Sn(OH)₂ 的生成与性质》实验中，NaOH 检验 Sn(OH)₂ 与____的反应。 |
| 19-8-03 Q001 | OLD_CHUNK3_EXP_19_8_03_Q001 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，生成 Sb(OH)₃ 时常用的锑(III)盐是哪一种？ |
| 19-8-03 Q002 | OLD_CHUNK3_EXP_19_8_03_Q002 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，由 SbCl₃ 生成 Sb(OH)₃ 沉淀时加入的碱是哪一种？ |
| 19-8-03 Q003 | OLD_CHUNK3_EXP_19_8_03_Q003 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与适量 NaOH 反应生成的沉淀主要是哪一种？ |
| 19-8-03 Q004 | OLD_CHUNK3_EXP_19_8_03_Q004 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 酸性溶解行为时加入的酸是哪一种？ |
| 19-8-03 Q005 | OLD_CHUNK3_EXP_19_8_03_Q005 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中的性质时加入的强碱是哪一种？ |
| 19-8-03 Q006 | OLD_CHUNK3_EXP_19_8_03_Q006 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 既能溶于酸又能溶于强碱，说明它具有什么性质？ |
| 19-8-03 Q007 | OLD_CHUNK3_EXP_19_8_03_Q007 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，与 2 mol·L⁻¹ NaOH 相比，6 mol·L⁻¹ NaOH 在该实验中主要用于观察什么？ |
| 19-8-03 Q008 | OLD_CHUNK3_EXP_19_8_03_Q008 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，进行 Sb(OH)₃ 性质实验时，最核心的观察对象是什么？ |
| 19-8-03 Q009 | OLD_CHUNK3_EXP_19_8_03_Q009 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 中锑元素的常见氧化态是哪一种？ |
| 19-8-03 Q010 | OLD_CHUNK3_EXP_19_8_03_Q010 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，下列哪种物质不是该实验生成 Sb(OH)₃ 的直接试剂组合？ |
| 19-8-03 Q011 | OLD_CHUNK3_EXP_19_8_03_Q011 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：起始锑盐为“SbCl₃”。 |
| 19-8-03 Q012 | OLD_CHUNK3_EXP_19_8_03_Q012 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：沉淀剂为“KSCN”。 |
| 19-8-03 Q013 | OLD_CHUNK3_EXP_19_8_03_Q013 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：沉淀产物为“Sb(OH)₃”。 |
| 19-8-03 Q014 | OLD_CHUNK3_EXP_19_8_03_Q014 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：酸中溶解为“NH₃·H₂O”。 |
| 19-8-03 Q015 | OLD_CHUNK3_EXP_19_8_03_Q015 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：碱中溶解为“NaOH”。 |
| 19-8-03 Q016 | OLD_CHUNK3_EXP_19_8_03_Q016 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：性质判断为“强挥发性”。 |
| 19-8-03 Q017 | OLD_CHUNK3_EXP_19_8_03_Q017 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：浓碱比较为“更强碱性条件下 Sb(OH)₃ 的溶解”。 |
| 19-8-03 Q018 | OLD_CHUNK3_EXP_19_8_03_Q018 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：观察重点为“火柴余烬复燃”。 |
| 19-8-03 Q019 | OLD_CHUNK3_EXP_19_8_03_Q019 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，判断：离子来源为“III”。 |
| 19-8-03 Q020 | OLD_CHUNK3_EXP_19_8_03_Q020_SF1 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 是生成 Sb(OH)₃ 沉淀的直接试剂组合。 |
| 19-8-03 Q021 | OLD_CHUNK3_EXP_19_8_03_Q021 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，生成 Sb(OH)₃ 的起始锑盐可用____。 |
| 19-8-03 Q022 | OLD_CHUNK3_EXP_19_8_03_Q022 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，向 SbCl₃ 溶液中加入____可生成 Sb(OH)₃。 |
| 19-8-03 Q023 | OLD_CHUNK3_EXP_19_8_03_Q023_PF1 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，SbCl₃ 与 NaOH 生成 Sb(OH)₃ 后，继续比较 HCl、2 mol/L NaOH 和 6 mol/L NaOH 的作用，最主要是为了判断什么？ |
| 19-8-03 Q024 | OLD_CHUNK3_EXP_19_8_03_Q024 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在酸中溶解时加入____。 |
| 19-8-03 Q025 | OLD_CHUNK3_EXP_19_8_03_Q025 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，检验 Sb(OH)₃ 在强碱中溶解时加入过量____。 |
| 19-8-03 Q026 | OLD_CHUNK3_EXP_19_8_03_Q026 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 可表现出____氢氧化物性质。 |
| 19-8-03 Q027 | OLD_CHUNK3_EXP_19_8_03_Q027 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，6 mol·L⁻¹ NaOH 用于观察____碱性条件下的溶解。 |
| 19-8-03 Q028 | OLD_CHUNK3_EXP_19_8_03_Q028 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，该实验的核心观察是沉淀的生成与____。 |
| 19-8-03 Q029 | OLD_CHUNK3_EXP_19_8_03_Q029 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，Sb(OH)₃ 中 Sb 的氧化态为____。 |
| 19-8-03 Q030 | OLD_CHUNK3_EXP_19_8_03_Q030_SF1 | textbook_prose_00596_462a4c7dff | 在《19-8-03 Sb(OH)₃ 的生成与性质》实验中，下列哪一组是生成 Sb(OH)₃ 沉淀的直接试剂组合？ |
| 19-8-04 Q001 | OLD_CHUNK3_EXP_19_8_04_Q001 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，生成 Bi(OH)₃ 沉淀时，通常向 Bi(NO₃)₃ 溶液中滴加哪种试剂？ |
| 19-8-04 Q002 | OLD_CHUNK3_EXP_19_8_04_Q002 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 反应生成 Bi(OH)₃ 时，主要观察什么？ |
| 19-8-04 Q003 | OLD_CHUNK3_EXP_19_8_04_Q003 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，检验 Bi(OH)₃ 与酸反应时，实验记录列出的酸是？ |
| 19-8-04 Q004 | OLD_CHUNK3_EXP_19_8_04_Q004 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 加 HCl 后沉淀溶解，主要说明 Bi(OH)₃ 具有什么性质？ |
| 19-8-04 Q005 | OLD_CHUNK3_EXP_19_8_04_Q005 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，实验还比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和哪种更浓碱的作用？ |
| 19-8-04 Q006 | OLD_CHUNK3_EXP_19_8_04_Q006 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，若 Bi(OH)₃ 在过量 NaOH 中不明显溶解，说明它与 Sn、Pb、Sb 的某些氢氧化物相比怎样？ |
| 19-8-04 Q007 | OLD_CHUNK3_EXP_19_8_04_Q007 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验属于 19-8 中哪一模块？ |
| 19-8-04 Q008 | OLD_CHUNK3_EXP_19_8_04_Q008 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，配制或使用 Bi(NO₃)₃ 时，实验资料的相关思考题提示要注意什么问题？ |
| 19-8-04 Q009 | OLD_CHUNK3_EXP_19_8_04_Q009 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，下列哪项最能体现 Bi(OH)₃ 的“生成”？ |
| 19-8-04 Q010 | OLD_CHUNK3_EXP_19_8_04_Q010 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，下列哪一项不是本实验的直接试剂组合？ |
| 19-8-04 Q011 | OLD_CHUNK3_EXP_19_8_04_Q011 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 溶液与 NaOH 作用可生成 Bi(OH)₃ 沉淀。 |
| 19-8-04 Q012 | OLD_CHUNK3_EXP_19_8_04_Q012 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与 HCl 反应可体现其碱性氢氧化物性质。 |
| 19-8-04 Q013 | OLD_CHUNK3_EXP_19_8_04_Q013 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验比较 Bi(OH)₃ 在 6 mol·L⁻¹ NaOH 和 40% NaOH 中的表现。 |
| 19-8-04 Q014 | OLD_CHUNK3_EXP_19_8_04_Q014 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 是典型强两性氢氧化物，必然易溶于任意稀碱。 |
| 19-8-04 Q015 | OLD_CHUNK3_EXP_19_8_04_Q015 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验属于锡、铅、砷、锑、铋实验中的氢氧化物性质部分。 |
| 19-8-04 Q016 | OLD_CHUNK3_EXP_19_8_04_Q016 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，使用铋化合物时应注意毒性和废液回收。 |
| 19-8-04 Q017 | OLD_CHUNK3_EXP_19_8_04_Q017 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 的生成实验核心是检验 NO₃⁻ 的棕色环。 |
| 19-8-04 Q018 | OLD_CHUNK3_EXP_19_8_04_Q018_R1 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，向 Bi(OH)₃ 中加入 HCl 后若沉淀溶解，可说明酸能与其反应。 |
| 19-8-04 Q019 | OLD_CHUNK3_EXP_19_8_04_Q019_R1 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 反应中 OH⁻ 是形成氢氧化物沉淀的必要离子。 |
| 19-8-04 Q020 | OLD_CHUNK3_EXP_19_8_04_Q020_R1 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，40% NaOH 是本实验列出的强碱条件之一。 |
| 19-8-04 Q021 | OLD_CHUNK3_EXP_19_8_04_Q021 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，生成 Bi(OH)₃ 时，Bi(NO₃)₃ 溶液中滴加____溶液。 |
| 19-8-04 Q022 | OLD_CHUNK3_EXP_19_8_04_Q022 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与____反应可体现其碱性。 |
| 19-8-04 Q023 | OLD_CHUNK3_EXP_19_8_04_Q023 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 的化学名称是____。 |
| 19-8-04 Q024 | OLD_CHUNK3_EXP_19_8_04_Q024_SF1 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，比较 Bi(OH)₃ 与 6 mol·L⁻¹ NaOH 和更强 NaOH 条件的作用，主要是为了判断什么？ |
| 19-8-04 Q025 | OLD_CHUNK3_EXP_19_8_04_Q025 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 反应生成的沉淀含有____离子。 |
| 19-8-04 Q026 | OLD_CHUNK3_EXP_19_8_04_Q026 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 与酸反应生成盐和____。 |
| 19-8-04 Q027 | OLD_CHUNK3_EXP_19_8_04_Q027 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，本实验所在模块为____的性质。 |
| 19-8-04 Q028 | OLD_CHUNK3_EXP_19_8_04_Q028 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，使用铋化合物后，废液应集中____处理。 |
| 19-8-04 Q029 | OLD_CHUNK3_EXP_19_8_04_Q029 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(OH)₃ 在碱中不易溶时，说明其两性相对较____。 |
| 19-8-04 Q030 | OLD_CHUNK3_EXP_19_8_04_Q030_PF1 | textbook_prose_00596_462a4c7dff | 在《19-8-04 Bi(OH)₃ 的生成与性质》实验中，Bi(NO₃)₃ 与 NaOH 生成 Bi(OH)₃ 只是第一步，后续还需比较其与 HCl、6 mol/L NaOH 和 40% NaOH 的作用。 |
| 19-8-05 Q001 | OLD_CHUNK3_EXP_19_8_05_Q001 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sn(OH)₂ 时向 SnCl₂ 溶液滴加的碱是哪一种？ |
| 19-8-05 Q002 | OLD_CHUNK3_EXP_19_8_05_Q002 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Pb(OH)₂ 时使用的铅盐溶液是哪一种？ |
| 19-8-05 Q003 | OLD_CHUNK3_EXP_19_8_05_Q003 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sb(OH)₃ 时使用的锑盐溶液是哪一种？ |
| 19-8-05 Q004 | OLD_CHUNK3_EXP_19_8_05_Q004 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Bi(OH)₃ 时使用的铋盐溶液是哪一种？ |
| 19-8-05 Q005 | OLD_CHUNK3_EXP_19_8_05_Q005 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，检验 Sn(OH)₂ 酸碱性时，沉淀需分别试验与哪两类溶液反应？ |
| 19-8-05 Q006 | OLD_CHUNK3_EXP_19_8_05_Q006 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Pb(OH)₂ 能与酸和碱作用，说明它主要具有什么酸碱特征？ |
| 19-8-05 Q007 | OLD_CHUNK3_EXP_19_8_05_Q007 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 随 NaOH 增多可溶解，体现其哪种酸碱性质？ |
| 19-8-05 Q008 | OLD_CHUNK3_EXP_19_8_05_Q008 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Bi(OH)₃ 与强碱作用不明显而能溶于酸，通常说明它更偏向什么性质？ |
| 19-8-05 Q009 | OLD_CHUNK3_EXP_19_8_05_Q009 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sb(OH)₃ 步骤中特意比较 2 mol·L⁻¹ 与 6 mol·L⁻¹ NaOH，是为了考察什么？ |
| 19-8-05 Q010 | OLD_CHUNK3_EXP_19_8_05_Q010 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，该组实验最终要总结 Sn、Pb、Sb、Bi 氢氧化物的哪类性质？ |
| 19-8-05 Q011 | OLD_CHUNK3_EXP_19_8_05_Q011 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 的生成与性质实验使用 SnCl₂ 溶液和 NaOH 溶液。 |
| 19-8-05 Q012 | OLD_CHUNK3_EXP_19_8_05_Q012 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Pb(OH)₂ 沉淀需分别试验与 HNO₃ 和 NaOH 溶液的反应。 |
| 19-8-05 Q013 | OLD_CHUNK3_EXP_19_8_05_Q013 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sb(OH)₃ 的性质实验会比较 2 mol·L⁻¹ 和 6 mol·L⁻¹ NaOH 的作用。 |
| 19-8-05 Q014 | OLD_CHUNK3_EXP_19_8_05_Q014 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Bi(OH)₃ 沉淀需比较与 HCl 和强碱的作用。 |
| 19-8-05 Q015 | OLD_CHUNK3_EXP_19_8_05_Q015 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 和 Pb(OH)₂ 可作为两性氢氧化物讨论。 |
| 19-8-05 Q016 | OLD_CHUNK3_EXP_19_8_05_Q016 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，本实验的核心观察对象是卤化银感光性。 |
| 19-8-05 Q017 | OLD_CHUNK3_EXP_19_8_05_Q017 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Bi(OH)₃ 的试剂是 KBr 和 CCl₄。 |
| 19-8-05 Q018 | OLD_CHUNK3_EXP_19_8_05_Q018_R1 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，只观察沉淀生成而不试验酸、碱作用，不能充分总结酸碱性。 |
| 19-8-05 Q019 | OLD_CHUNK3_EXP_19_8_05_Q019_R1 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Bi(OH)₃ 通常比 Sn(OH)₂ 更表现出碱性氢氧化物特征。 |
| 19-8-05 Q020 | OLD_CHUNK3_EXP_19_8_05_Q020 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，SbCl₃、Bi(NO₃)₃、Pb(NO₃)₂ 等重金属化合物操作可忽略安全防护。 |
| 19-8-05 Q021 | OLD_CHUNK3_EXP_19_8_05_Q021 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sn(OH)₂ 时向 SnCl₂ 溶液滴加____溶液。 |
| 19-8-05 Q022 | OLD_CHUNK3_EXP_19_8_05_Q022 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Pb(OH)₂ 时使用____溶液。 |
| 19-8-05 Q023 | OLD_CHUNK3_EXP_19_8_05_Q023 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Sb(OH)₃ 时使用____溶液。 |
| 19-8-05 Q024 | OLD_CHUNK3_EXP_19_8_05_Q024 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，制备 Bi(OH)₃ 时使用____溶液。 |
| 19-8-05 Q025 | OLD_CHUNK3_EXP_19_8_05_Q025 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 沉淀分别试验与 HCl 和____溶液的反应。 |
| 19-8-05 Q026 | OLD_CHUNK3_EXP_19_8_05_Q026 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Pb(OH)₂ 能溶于酸和碱，体现____氢氧化物特征。 |
| 19-8-05 Q027 | OLD_CHUNK3_EXP_19_8_05_Q027 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sn(OH)₂ 可溶于过量 NaOH，体现____。 |
| 19-8-05 Q028 | OLD_CHUNK3_EXP_19_8_05_Q028 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Bi(OH)₃ 通常更偏____氢氧化物。 |
| 19-8-05 Q029 | OLD_CHUNK3_EXP_19_8_05_Q029 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，Sb(OH)₃ 步骤比较不同 NaOH 浓度下沉淀的____。 |
| 19-8-05 Q030 | OLD_CHUNK3_EXP_19_8_05_Q030 | textbook_prose_00753_2adf53a8cc, textbook_prose_00754_c66e000e5b, textbook_prose_00596_462a4c7dff | 在《19-8-05 Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性》实验中，该组实验最终总结这些氢氧化物的____。 |
| 19-8-06 Q001 | OLD_CHUNK3_EXP_19_8_06_Q001 | textbook_prose_00773_a0b6644822, textbook_prose_00774_e51e8911a2 | 在《19-8-06 Sn(II) 的还原性》实验中，检验 Sn(II) 还原 Fe³⁺ 的实验中，向 FeCl₃ 溶液滴加的是哪种溶液？ |
- 另有 188 道 theory-dependent 题未展开。

## 最终校验
- UTF-8 JSON 解析：通过
- 项目 validator：通过（0 errors；62 warnings 为当前 chunk 非全量 inventory 的预期提示）
- 输出题数等于输入题数：450 / 450
- rewrite/reject concrete proposed_question：通过
- 有效单选 option_links 数量匹配：通过
- 非必要重复 proposed_question.stem：通过
- 模板化 diagnostic_note：通过
- 未覆盖 reviewed_v1 或 semantic_final_v1：通过

## 逐题语义终稿打磨确认
确认：本轮已按 chunk_3 的有效题版本逐题完成语义终稿打磨；keep 以 original_question 为有效版本，rewrite/reject 以 proposed_question 为有效版本；逐题复核了 canonical 实验原文、formal video_points、必要 supporting theory、点位绑定、单选 option_links、填空手机端风险和机器确定性判分。脚本仅用于把人工审查表、统计与校验结果落盘。
