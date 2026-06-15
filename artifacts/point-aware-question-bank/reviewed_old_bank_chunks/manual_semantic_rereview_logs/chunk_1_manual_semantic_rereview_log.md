# chunk 1 Manual Semantic Rereview Log

Change: `full-question-bank-semantic-release-repair`

Source file: `chunk_1_release_final_v1.json`

Active release questions: 443

## Guardrail

Scripts, search, and structured queries may be used only for inventory, navigation, statistics, and validation. They do not decide keep/rewrite/reject, do not generate final wording, do not assign point links, and do not create explanations. Each logged item must come from Codex manually reading the effective question, original/proposed source fields, bound video points, canonical experiment evidence, and supporting theory when necessary.

## Per-question Fields

- Question ID
- Experiment code
- Effective question type
- Manual decision: keep / rewrite / reject / repair-only
- Point binding status
- Source support status
- Mobile fill-blank status
- Formula display status
- Option-link status
- Repairs made
- Remaining risk

## Spotcheck Risk Class Checklist

Every batch entry must explicitly account for the risk classes found in the 2026-06-15 after-stage spotcheck: missing or generic explanations, ASCII digit formulas in effective displayed text or visible option-link text, English or generic option-link diagnostics, formula-heavy mobile-hostile fill blanks, accepted-answer aliases that may be visible vs hidden grading synonyms, and low-depth recognition items.

## Baseline Parse

- 2026-06-15: `chunk_1_release_final_v1.json` parsed successfully; active questions = 443.

## Batch Entries

### 2026-06-15 - `19-1-05` 次氯酸盐的氧化性

Canonical evidence read: NaClO 溶液分三份，分别与 MnSO₄ 溶液、品红溶液、酸性 KI-淀粉溶液反应并观察现象；Mn²⁺ 被 ClO⁻ 氧化生成棕黑色 MnO₂；品红被氧化漂白褪色；酸性条件下 I⁻ 被氧化为 I₂，I₂ 与淀粉显蓝，过量 NaClO 可继续把 I₂ 氧化为 IO₃⁻ 使蓝色褪去。

Validation after hand repair: active = 30; missing effective explanations = 0; generic explanations = 0; option-link text mismatches = 0; ASCII digit formulas in effective displayed text = 0; duplicate effective stems = 0.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_05_Q001 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Added concrete explanation. | none |
| CHUNK1_19_1_05_Q002 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added concrete explanation. | none |
| CHUNK1_19_1_05_Q003 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added concrete explanation. | none |
| CHUNK1_19_1_05_Q004 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added concrete explanation. | none |
| CHUNK1_19_1_05_Q005 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Added concrete explanation. | none |
| CHUNK1_19_1_05_Q006 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote negative "not main reagent" item as positive reagent-scope item; reauthored options, answer, explanation, and option links. | none |
| CHUNK1_19_1_05_Q007 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added concrete explanation. | low-depth but necessary for I₂-starch evidence |
| CHUNK1_19_1_05_Q008 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote duplicated evidence-chain item to test oxidation-property inference; normalized formula display and explanation. | none |
| CHUNK1_19_1_05_Q009 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote unsupported safety wording into source-supported sampling/observation task; updated option links. | none |
| CHUNK1_19_1_05_Q010 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Added concrete explanation. | none |
| CHUNK1_19_1_05_Q011 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added concrete false-statement explanation. | none |
| CHUNK1_19_1_05_Q012 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added concrete false-statement explanation. | none |
| CHUNK1_19_1_05_Q013 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added concrete false-statement explanation. | none |
| CHUNK1_19_1_05_Q014 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added concrete true-statement explanation. | none |
| CHUNK1_19_1_05_Q015 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added concrete true-statement explanation. | none |
| CHUNK1_19_1_05_Q016 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation distinguishing this experiment from the adjacent chlorate experiment. | none |
| CHUNK1_19_1_05_Q017 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation grounded in observed oxidation behavior. | none |
| CHUNK1_19_1_05_Q018 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation that KI supplies I⁻ and starch is only the color indicator. | none |
| CHUNK1_19_1_05_Q019 | true_false | rewrite | multi-point valid | canonical supported | n/a | clean | n/a | Rewrote meta wording about what the题目 should cover into a direct experiment statement. | none |
| CHUNK1_19_1_05_Q020 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation naming the blue/blue-fade color evidence. | none |
| CHUNK1_19_1_05_Q021 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Added concrete explanation; accepted answers remain short. | low-depth but necessary reagent source |
| CHUNK1_19_1_05_Q022 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Replaced generic explanation with I⁻ oxidation explanation. | low-depth but deterministic |
| CHUNK1_19_1_05_Q023 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Replaced generic explanation with I₂-starch explanation. | low-depth but deterministic |
| CHUNK1_19_1_05_Q024 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added concrete explanation. | low-depth but necessary phenomenon term |
| CHUNK1_19_1_05_Q025 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Replaced generic explanation with MnSO₄/MnO₂ evidence. | low-depth but deterministic |
| CHUNK1_19_1_05_Q026 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Normalized I⁻/I₂/Na⁺/MnSO₄ display and replaced generic explanation. | none |
| CHUNK1_19_1_05_Q027 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Added concrete explanation. | low-depth but core property term |
| CHUNK1_19_1_05_Q028 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote duplicate evidence-chain item to test blue-fade explanation from over-oxidation to IO₃⁻. | none |
| CHUNK1_19_1_05_Q029 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added concrete explanation. | low-depth but observation-language item |
| CHUNK1_19_1_05_Q030 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote duplicate evidence-chain item to test starch's role in I₂ color display. | none |

### 2026-06-15 - `19-2-02` 过氧化氢的制备

Canonical evidence read: 取少量 Na₂O₂ 固体于小试管中，加入少量蒸馏水，溶解后放在冰水中冷却并搅拌；用试纸检验酸碱性，再滴加冰水冷却过的 1 mol·L⁻¹ H₂SO₄ 溶液至酸性为止。Video points checked: `candidate-1-452aecdc` Na₂O₂ + 水；`candidate-2-ca62174d` 冰水冷却；`candidate-3-7f0776ff` 加入冷却过的 H₂SO₄ 酸化；`candidate-4-10e07c01` 用试纸检验酸碱性变化。Theory-dependent judgments: H₂O₂ 分解/控温类题目依赖 CHK_DOC_CH14_COURSEWARE_P035_001 or processed supporting theory for `2 H₂O₂ = 2 H₂O + O₂` and H₂O₂ decomposition risk.

Validation after hand repair: active = 30; missing effective explanations = 0; generic explanations = 0; option-link text mismatches = 0; ASCII digit formulas in effective displayed text = 0; duplicate effective stems = 0.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_2_02_Q001 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added concrete explanation naming Na₂O₂ as the solid reagent. | low-depth but core reagent source |
| CHUNK1_19_2_02_Q002 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Added explanation for ice-water cooling and stirring to reduce H₂O₂ decomposition risk. | none |
| CHUNK1_19_2_02_Q003 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added explanation naming cold H₂SO₄ as the acidifying acid. | low-depth but core operation reagent |
| CHUNK1_19_2_02_Q004 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Added explanation for acid-base paper check before acidification. | none |
| CHUNK1_19_2_02_Q005 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Added explanation that Na₂O₂ + water initially gives alkaline solution. | low-depth but necessary acidification prerequisite |
| CHUNK1_19_2_02_Q006 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Added explanation that acidification neutralizes the alkaline system and gives acidic H₂O₂ solution. | none |
| CHUNK1_19_2_02_Q007 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Added explanation for operation order: Na₂O₂ + water, cooling/stirring, cold H₂SO₄ acidification. | none |
| CHUNK1_19_2_02_Q008 | single_choice | repair-only keep | valid | theory supported | n/a | clean | valid | Added explanation that H₂O₂ decomposes to H₂O and O₂. | none |
| CHUNK1_19_2_02_Q009 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Added explanation that cold H₂SO₄ reflects temperature control during acidification. | none |
| CHUNK1_19_2_02_Q010 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote negative/exception-style item into full operation-chain item; reauthored options, answer, explanation, and option links. | none |
| CHUNK1_19_2_02_Q011 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation that Na₂O₂ + water is not already acidic and requires acid-base check/acidification. | none |
| CHUNK1_19_2_02_Q012 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation that H₂SO₄ is for acidification, not for providing Cl⁻. | none |
| CHUNK1_19_2_02_Q013 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation confirming cold 1 mol·L⁻¹ H₂SO₄ to acid. | none |
| CHUNK1_19_2_02_Q014 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation that test paper confirms acid-base change reaches requirement. | none |
| CHUNK1_19_2_02_Q015 | true_false | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | n/a | Added explanation that experiment requires cooling, not prolonged strong heating. | none |
| CHUNK1_19_2_02_Q016 | true_false | repair-only keep | valid | theory supported | n/a | clean | n/a | Added explanation linking H₂O₂ decomposition to O₂ with temperature control. | none |
| CHUNK1_19_2_02_Q017 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation distinguishing Na₂O₂ from NaClO. | none |
| CHUNK1_19_2_02_Q018 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation that acidification avoids retaining strong alkalinity. | none |
| CHUNK1_19_2_02_Q019 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Rewrote low-quality purpose item into deterministic operation-purpose question; updated options, explanation, and option links. | none |
| CHUNK1_19_2_02_Q020 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation distinguishing preparation steps from later identification reagents. | none |
| CHUNK1_19_2_02_Q021 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote mobile fill blank to single choice; replaced generic explanation and refined H₂O option link. | low-depth but core reagent source |
| CHUNK1_19_2_02_Q022 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Added concrete explanation; answer remains short mobile-safe phrase. | low-depth but core cooling operation |
| CHUNK1_19_2_02_Q023 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote mobile fill blank to single choice; replaced generic explanation and pointed correct option to acidification point. | low-depth but core operation reagent |
| CHUNK1_19_2_02_Q024 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Added concrete explanation for acid-base/pH paper check. | low-depth but core observation language |
| CHUNK1_19_2_02_Q025 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote mobile-hostile fill blank into deterministic acid-base judgment question; updated point binding and option links. | none |
| CHUNK1_19_2_02_Q026 | single_choice | rewrite | valid | theory + point supported | n/a | clean | valid | Rewrote mobile fill blank to single choice; replaced generic explanation and recorded theory dependency for H₂O₂ decomposition. | low-depth but deterministic prerequisite |
| CHUNK1_19_2_02_Q027 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Added explanation that Na₂O₂ + water initially gives alkaline solution. | low-depth but core acidification prerequisite |
| CHUNK1_19_2_02_Q028 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added explanation that cold H₂SO₄ is added until acidic. | low-depth but core endpoint term |
| CHUNK1_19_2_02_Q029 | fill_blank | repair-only keep | valid | theory supported | mobile-safe | clean | n/a | Added explanation that cooling reduces H₂O₂ decomposition. | low-depth but core control term |
| CHUNK1_19_2_02_Q030 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Added explanation that prepared H₂O₂ solution can be used for later identification/property experiments. | low-depth but experiment-scope bridge |

### 2026-06-15 - `19-3-02` 二氧化硫的性质

Canonical evidence read: 教材要求依次观察 SO₂ 的性质：向酸性 KMnO₄ 溶液通入 SO₂ 观察褪色；向饱和 H₂S 水溶液中通入 SO₂ 观察生成硫；向品红溶液中通入 SO₂ 观察褪色，并加热观察颜色是否恢复。Video points checked: `candidate-1-ea27f7fc` 还原性：SO₂ + 酸性 KMnO₄；`candidate-2-7afa5538` 氧化性：SO₂ + H₂S / 硫化钠替代液；`candidate-3-a9b16396` 漂白作用：SO₂ + 品红溶液；`candidate-4-0ae7d9ba` 品红褪色后加热，观察颜色是否恢复。Theory-dependent judgments: 生成单质硫、SO₂ 在 H₂S 体系中表现氧化性，以及品红褪色后加热恢复所体现的可逆漂白特点，依赖 supporting theory `CHK_DOC_EXPERIMENTS_SELECTED_P018_001`；KMnO₄ / H₂S / 品红 / 加热恢复这些实验点位本身由 canonical 和 video points 支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0. Spotcheck risk classes checked: missing/generic explanations, ASCII formulas, English/generic option-link diagnostics, formula-heavy mobile fill blanks, accepted-answer alias visibility, and low-depth recognition items.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_3_02_Q001 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote off-point SO₂ preparation item into acidified KMnO₄ reduction-property item; reauthored proposed option links. | none |
| CHUNK1_19_3_02_Q002 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote off-point preparation reagent item into H₂S oxidation-property item; normalized proposed option-link formula display. | none |
| CHUNK1_19_3_02_Q003 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Corrected audit semantics and coverage to the acidified KMnO₄ point only. | low-depth but necessary property mapping |
| CHUNK1_19_3_02_Q004 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Added concrete explanation for SO₂ oxidizing H₂S and checked option links. | low-depth but necessary property mapping |
| CHUNK1_19_3_02_Q005 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Corrected audit semantics to 品红漂白 and heating-recovery points only. | none |
| CHUNK1_19_3_02_Q006 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote off-point SO₂ safety item into 品红漂白/加热恢复 item; normalized proposed option-link formulas and diagnostics. | none |
| CHUNK1_19_3_02_Q007 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Corrected point binding and option-link diagnostics to the acidified KMnO₄ reduction point only. | none |
| CHUNK1_19_3_02_Q008 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Replaced generic explanation/diagnostic with SO₂ + H₂S generating sulfur evidence. | low-depth but product observation is core evidence |
| CHUNK1_19_3_02_Q009 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Fixed correct option point key from H₂S to 品红溶液 and reauthored distractor diagnostics. | none |
| CHUNK1_19_3_02_Q010 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Expanded point binding and diagnostics to KMnO₄, H₂S, 品红, and 加热恢复 points. | low-depth but useful experiment overview |
| CHUNK1_19_3_02_Q011 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation distinguishing KMnO₄ reduction-property point from oxidation-property wording. | none |
| CHUNK1_19_3_02_Q012 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation that SO₂ + 品红 directly observes 漂白作用. | none |
| CHUNK1_19_3_02_Q013 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Added explanation for SO₂ showing oxidation property in the H₂S system. | none |
| CHUNK1_19_3_02_Q014 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation that 品红褪色 is the bleaching observation. | none |
| CHUNK1_19_3_02_Q015 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote duplicate/general item into heating-recovery reversibility question; updated answer, explanation, and option links. | none |
| CHUNK1_19_3_02_Q016 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation rejecting the absolute claim that SO₂ only shows oxidation property. | low-depth but checks absolute false statement across two redox points |
| CHUNK1_19_3_02_Q017 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Added explanation that heating after 品红褪色 helps judge bleaching characteristics. | none |
| CHUNK1_19_3_02_Q018 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Added explanation that KMnO₄ should fade rather than remain completely unchanged. | low-depth but checks a common phenomenon inversion |
| CHUNK1_19_3_02_Q019 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Added explanation that SO₂ + H₂S can generate single sulfur. | none |
| CHUNK1_19_3_02_Q020 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote duplicate item into reason question explaining SO₂ oxidation property in H₂S reaction. | none |
| CHUNK1_19_3_02_Q021 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote duplicate item into operation-choice question for SO₂ bleaching and heating recovery. | none |
| CHUNK1_19_3_02_Q022 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote duplicate item into acidified KMnO₄ expected-phenomenon question. | none |
| CHUNK1_19_3_02_Q023 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote duplicate item into H₂S system-property matching question. | none |
| CHUNK1_19_3_02_Q024 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added explanation; answer remains short Chinese property term. | low-depth but core property term |
| CHUNK1_19_3_02_Q025 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added explanation; answer remains short Chinese property term. | low-depth but core property term |
| CHUNK1_19_3_02_Q026 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added explanation; answer remains short Chinese property term. | low-depth but core property term |
| CHUNK1_19_3_02_Q027 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Added explanation; answer is short product name “硫”. | low-depth but product observation is core evidence |
| CHUNK1_19_3_02_Q028 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote duplicate item into reagent-system/property matching question; updated option links. | none |
| CHUNK1_19_3_02_Q029 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added explanation that KMnO₄ fading treats SO₂ as reducing agent. | low-depth but core conclusion term |
| CHUNK1_19_3_02_Q030 | fill_blank | repair-only keep | secondary point valid | canonical supported | mobile-safe | clean | n/a | Added explanation that heating after 品红褪色 checks whether color recovers. | low-depth but mobile-safe observation term |

### 2026-06-15 - `19-1-01` 氯、溴、碘的置换次序

Canonical evidence read: 教材原文要求用 0.1 mol/L KBr 溶液、0.1 mol/L KI 溶液、CCl₄、氯水、溴水等设计试管实验说明氯、溴、碘的置换次序；列明氯水 + KBr 溶液 + CCl₄ 中 CCl₄ 层呈橙红色，说明生成 Br₂；氯水 + KI 溶液 + CCl₄ 中 CCl₄ 层呈紫红色，说明生成 I₂；溴水 + KI 溶液 + CCl₄ 中 CCl₄ 层呈紫红色，说明生成 I₂；由此得到氧化性 Cl₂ > Br₂ > I₂。Video points checked: `candidate-1-034a8366` 氯水 + KBr 溶液 + CCl₄；`candidate-2-1e180c68` 氯水 + KI 溶液 + CCl₄；`candidate-3-9b8be606` 溴水 + KI 溶液 + CCl₄。Theory-dependent judgments: 卤素单质氧化性递变顺序和“较强氧化性的卤素单质可氧化较弱卤素离子”的概括由 canonical 原文同段给出，不额外依赖 supporting theory。

Validation after hand repair: active = 30; missing effective explanations = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; generic/template option-link diagnostics = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0. Spotcheck risk classes checked: missing/generic explanations, ASCII formulas, English/generic option-link diagnostics, formula-heavy mobile fill blanks, accepted-answer alias visibility, and low-depth recognition items.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_01_Q001 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Reauthored option-link diagnostics around Cl₂ oxidizing Br⁻ to Br₂. | none |
| CHUNK1_19_1_01_Q002 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Reauthored CCl₄ role diagnostics as extraction/color observation, not oxidation. | none |
| CHUNK1_19_1_01_Q003 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics for I⁻ as oxidized ion in氯水 + KI point. | none |
| CHUNK1_19_1_01_Q004 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics and corrected audit semantics to溴水 + KI point only. | none |
| CHUNK1_19_1_01_Q005 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Corrected point binding to all three displacement points and reauthored oxidation-order diagnostics. | none |
| CHUNK1_19_1_01_Q006 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Reauthored reagent-system diagnostics and removed template wording. | low-depth but core reagent-system recognition |
| CHUNK1_19_1_01_Q007 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Reauthored observation diagnostics around CCl₄ layer color. | none |
| CHUNK1_19_1_01_Q008 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Reauthored negative-question option links: A/B/C are valid bases, D is correct by exclusion because K⁺ is spectator. | none |
| CHUNK1_19_1_01_Q009 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Reauthored diagnostics for氯水 oxidizing both Br⁻ and I⁻. | none |
| CHUNK1_19_1_01_Q010 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Normalized Cl₂/Br₂/CCl₄ display and reauthored both top/proposed option links. | none |
| CHUNK1_19_1_01_Q011 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Checked statement against氯水 + KBr evidence; no edit needed. | none |
| CHUNK1_19_1_01_Q012 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Checked statement against溴水 + KI evidence; no edit needed. | none |
| CHUNK1_19_1_01_Q013 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Checked CCl₄ role as extraction/observation layer; no edit needed. | none |
| CHUNK1_19_1_01_Q014 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Checked general displacement-rule statement across three points. | none |
| CHUNK1_19_1_01_Q015 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Checked false statement about iodine replacing bromide against oxidation order. | none |
| CHUNK1_19_1_01_Q016 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Checked experiment purpose against canonical title and three point sequence. | low-depth but necessary experiment-purpose item |
| CHUNK1_19_1_01_Q017 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Checked theme classification as halogen oxidation-property experiment. | low-depth but useful prerequisite classification |
| CHUNK1_19_1_01_Q018 | true_false | rewrite | valid | canonical supported | n/a | clean | n/a | Checked rewritten statement that氯水 + KI proves Cl₂ > I₂. | none |
| CHUNK1_19_1_01_Q019 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Checked false statement that CCl₄ alone can compare displacement order. | none |
| CHUNK1_19_1_01_Q020 | true_false | rewrite | multi-point valid | canonical supported | n/a | clean | n/a | Checked rewritten spectator-ion statement for K⁺. | none |
| CHUNK1_19_1_01_Q021 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics for Br⁻ as oxidized ion in氯水 + KBr point. | none |
| CHUNK1_19_1_01_Q022 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics and corrected audit semantics to溴水 + KI point only. | none |
| CHUNK1_19_1_01_Q023 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Reauthored CCl₄ extraction-solvent diagnostics across all three points. | low-depth but core observation reagent |
| CHUNK1_19_1_01_Q024 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Corrected point binding to all three displacement points and reauthored order diagnostics. | none |
| CHUNK1_19_1_01_Q025 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Checked short answer “氧化性”; retained as experiment-theme prerequisite. | low-depth but mobile-safe core theme |
| CHUNK1_19_1_01_Q026 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics for I₂ product in氯水 + KI point. | none |
| CHUNK1_19_1_01_Q027 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics for iodide as oxidized ion in溴水 + KI point. | none |
| CHUNK1_19_1_01_Q028 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Reauthored diagnostics for试剂组合 proving Cl₂ > Br₂. | low-depth but operation-system recognition |
| CHUNK1_19_1_01_Q029 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Corrected audit semantics and point binding to all three points; reauthored weakest-oxidant diagnostics. | none |
| CHUNK1_19_1_01_Q030 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Checked short answer “颜色/颜色变化”; retained as observation-language item. | low-depth but mobile-safe observation term |

### 2026-06-15 - `19-1-02` 氯水、溴水、碘水氧化性差异的比较

Canonical evidence read: 教材要求分别向氯水、溴水、碘水中滴加 0.1 mol/L Na₂S₂O₃ 溶液及饱和硫化氢水溶液，观察现象。Video points checked: `candidate-1-656364cb` 氯水、溴水、碘水分别与 Na₂S₂O₃ 溶液反应；`candidate-2-e6c5ee5d` 氯水、溴水、碘水分别与饱和硫化氢水溶液 / 硫化钠替代液反应。Theory-dependent judgments: Na₂S₂O₃ 与 H₂S 作为还原性体系、卤素水使体系褪色并生成硫沉淀的解释，依赖基础氧化还原理论；教材和 video points 直接支撑操作对象、点位和观察要求。未引入 AI 判学生答案对错，最终题均为机器确定性判分。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; true/false invalid option links = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0. Spotcheck risk classes checked: missing/generic explanations, ASCII formulas, English/generic option-link diagnostics, formula-heavy mobile fill blanks, accepted-answer alias visibility, low-depth recognition items, weak point-link semantics, and multi-point overbinding.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_02_Q001 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Checked Na₂S₂O₃ system purpose and concrete option links. | low-depth but acceptable as property-scope entry item |
| CHUNK1_19_1_02_Q002 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Checked reagent identity and option diagnostics against Na₂S₂O₃ point. | low-depth but core reagent prerequisite |
| CHUNK1_19_1_02_Q003 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Checked H₂S reagent point and distractors. | low-depth but core second-system reagent prerequisite |
| CHUNK1_19_1_02_Q004 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Checked observation focus:褪色、硫沉淀、反应明显程度. | none |
| CHUNK1_19_1_02_Q005 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Checked oxidation-order conclusion across both systems. | low-depth but retained as conclusion bridge |
| CHUNK1_19_1_02_Q006 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Checked卤素水在 H₂S 体系中作氧化剂. | none |
| CHUNK1_19_1_02_Q007 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Checked same-reagent comparison design and variable control. | none |
| CHUNK1_19_1_02_Q008 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Checked Na₂S₂O₃ 还原性 explanation. | low-depth but necessary prerequisite property |
| CHUNK1_19_1_02_Q009 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Reauthored negative-stem option links so valid experiment focuses are marked non-answer and AgX solubility is correct by exclusion. | none |
| CHUNK1_19_1_02_Q010 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Checked knowledge-point conclusion and option diagnostics. | low-depth but retained as overview |
| CHUNK1_19_1_02_Q011 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Checked Na₂S₂O₃ comparison statement. | none |
| CHUNK1_19_1_02_Q012 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Checked false heating/decomposition distractor against教材操作. | none |
| CHUNK1_19_1_02_Q013 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Checked H₂S as reducing system. | none |
| CHUNK1_19_1_02_Q014 | true_false | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | n/a | Removed invalid A-D option links and confirmed false iodine-stronger claim. | none |
| CHUNK1_19_1_02_Q015 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Checked same-category reagent comparison across both systems. | none |
| CHUNK1_19_1_02_Q016 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Checked Na₂S₂O₃ reducing-property statement. | low-depth but necessary prerequisite property |
| CHUNK1_19_1_02_Q017 | true_false | rewrite | valid | canonical + theory supported | n/a | clean | n/a | Rewrote title/module recognition item into Na₂S₂O₃ 体系硫沉淀/褪色 evidence judgement. | none |
| CHUNK1_19_1_02_Q018 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Removed invalid A-D option links and checked observation-not-numbering false statement. | none |
| CHUNK1_19_1_02_Q019 | true_false | rewrite | multi-point valid | canonical supported | n/a | clean | n/a | Checked rewritten statement avoiding double-negative wording. | none |
| CHUNK1_19_1_02_Q020 | true_false | rewrite | multi-point valid | canonical supported | n/a | clean | n/a | Checked rewritten non-AgX relationship statement. | none |
| CHUNK1_19_1_02_Q021 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote to distinguish碘水 from氯水/溴水 in Na₂S₂O₃ system; reauthored options and links. | none |
| CHUNK1_19_1_02_Q022 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote to H₂S 系统硫沉淀/褪色 evidence; narrowed point binding to candidate-2. | none |
| CHUNK1_19_1_02_Q023 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Rewrote to combined Na₂S₂O₃ / H₂S conclusion item. | none |
| CHUNK1_19_1_02_Q024 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Retained short Chinese answer “还原/还原性”; removed accidental proposed-question carryover. | low-depth but mobile-safe prerequisite property |
| CHUNK1_19_1_02_Q025 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote to Na₂S₂O₃ 体系沉淀差异 inference; added concrete option links. | none |
| CHUNK1_19_1_02_Q026 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Rewrote to observation-evidence selection across both systems. | none |
| CHUNK1_19_1_02_Q027 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote to硫沉淀 evidence for氯水/溴水 stronger than碘水. | none |
| CHUNK1_19_1_02_Q028 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote to H₂S 体系 observation-recording item. | none |
| CHUNK1_19_1_02_Q029 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Retained short Chinese answer “还原/还原性” with prerequisite-property reason. | low-depth but mobile-safe prerequisite property |
| CHUNK1_19_1_02_Q030 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Rewrote title/object recall into evidence-chain question covering both systems. | none |

### 2026-06-15 - `19-1-04` 卤素离子的还原性（通风橱内进行）

Canonical evidence read: 教材要求分别向盛有绿豆大小 KCl、KBr、KI 固体的三支试管中加入约 0.5 mL 浓硫酸，观察现象，并选用湿醋酸铅试纸、碘化钾-淀粉试纸、pH 试纸或浓氨水检验逸出气体；教材还要求通过以上实验比较卤素离子还原性的相对强弱。安全证据来自同章安全知识：氯气、溴蒸气等有毒或强刺激性实验应在通风橱内进行。Video points checked: `candidate-1-9a665846` KI 固体 + 浓硫酸；`candidate-2-1416e2da` KBr 固体 + 浓硫酸；`candidate-3-1e08ab94` KCl 固体 + 浓硫酸；`candidate-4-a326b299` 用湿醋酸铅试纸、湿 KI-淀粉试纸、湿 pH 试纸检验产生的气体；`candidate-5-f8ac28b0` KBr 与浓硫酸反应后，用湿 KI-淀粉试纸检验生成的溴。Theory-dependent judgments: 卤素离子还原性顺序 I⁻ > Br⁻ > Cl⁻，Br₂ 氧化 I⁻ 生成 I₂ 且 I₂ 使淀粉显蓝，H₂S 与醋酸铅试纸生成黑色 PbS，浓硫酸可氧化 Br⁻/I⁻。这些 theory 只用于解释产物、显色和还原性顺序，操作、试剂、通风橱、试纸选择均由 canonical/video points 直接支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; effective option-link text mismatches = 0; invalid point keys = 0; unresolved visible ASCII ion display in effective option links = 0; formula-heavy mobile fill blanks retained only when a short Chinese accepted answer is first and ASCII forms are hidden deterministic grading aliases. Spotcheck risk classes checked: missing/generic explanations, visible ASCII formulas, English/generic option-link diagnostics, formula-heavy mobile fill blanks, accepted-answer alias visibility, low-depth recognition items, weak point-link semantics, duplicate rewrites, and multi-point overbinding.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_04_Q001 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Promoted KCl/KBr/KI reaction points to primary set; retained strongest-ion item with concrete diagnostics. | low-depth but retained as required conclusion anchor |
| CHUNK1_19_1_04_Q002 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Promoted all three solid + concentrated sulfuric acid points to primary binding. | low-depth but reagent amount/acid identity is core operation prerequisite |
| CHUNK1_19_1_04_Q003 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Kept wet lead acetate test for H₂S and concrete PbS explanation. | none |
| CHUNK1_19_1_04_Q004 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Corrected correct option link to bromine test point `candidate-5-f8ac28b0`. | none |
| CHUNK1_19_1_04_Q005 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Repaired K⁺ display and option diagnostics around gas-product testing. | none |
| CHUNK1_19_1_04_Q006 | single_choice | repair-only keep | valid | canonical safety + experiment supported | n/a | clean | valid | Confirmed fume-hood reason and distractors. | none |
| CHUNK1_19_1_04_Q007 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Included all three comparison points for KCl weakness item. | none |
| CHUNK1_19_1_04_Q008 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Confirmed wet pH paper use. | none |
| CHUNK1_19_1_04_Q009 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Included all three comparison points and retained reducing-order question. | low-depth but retained as final comparison conclusion |
| CHUNK1_19_1_04_Q010 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Confirmed concentrated sulfuric acid oxidation role in KBr/KI reactions. | none |
| CHUNK1_19_1_04_Q011 | true_false | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | n/a | Checked KI vs KCl reducing-product claim. | none |
| CHUNK1_19_1_04_Q012 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Retained false statement distinguishing ion reducing property from halogen oxidation-only framing. | low-depth but prevents experiment-theme confusion |
| CHUNK1_19_1_04_Q013 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Confirmed wet lead acetate paper for possible H₂S. | none |
| CHUNK1_19_1_04_Q014 | true_false | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | n/a | Corrected binding to KBr/bromine test points. | none |
| CHUNK1_19_1_04_Q015 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Reauthored generic explanation and all option-link diagnostics; fixed visible K⁺ text. | none |
| CHUNK1_19_1_04_Q016 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Confirmed K⁺ spectator-ion false statement across three salts. | none |
| CHUNK1_19_1_04_Q017 | true_false | repair-only keep | valid | canonical safety supported | n/a | clean | n/a | Confirmed controlled concentrated sulfuric acid use in fume hood. | none |
| CHUNK1_19_1_04_Q018 | true_false | rewrite | multi-point valid | canonical + theory supported | n/a | clean | n/a | Replaced generic explanation with I⁻ > Br⁻ > Cl⁻ evidence/theory note. | none |
| CHUNK1_19_1_04_Q019 | true_false | rewrite | valid | canonical + theory supported | n/a | clean | n/a | Replaced generic explanation with Br⁻ oxidized to Br₂ reasoning. | none |
| CHUNK1_19_1_04_Q020 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Confirmed concentrated sulfuric acid is not inert solvent. | none |
| CHUNK1_19_1_04_Q021 | fill_blank | repair-only keep | multi-point valid | canonical + theory supported | mobile-safe with hidden alias | clean | n/a | Added concrete explanation; moved Chinese answer `碘化钾` before hidden ASCII alias `KI`. | low-depth but short prerequisite/conclusion term |
| CHUNK1_19_1_04_Q022 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Added concrete wet lead acetate / PbS explanation. | low-depth but core gas-test reagent |
| CHUNK1_19_1_04_Q023 | fill_blank | repair-only keep | multi-point valid | canonical + theory supported | mobile-safe with hidden alias | clean | n/a | Added Br₂/I⁻/I₂-starch explanation; moved Chinese `碘化钾-淀粉` before hidden ASCII alias `KI-淀粉`; corrected binding to KBr/bromine test points. | low-depth but core gas-test reagent |
| CHUNK1_19_1_04_Q024 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Normalized I⁻/K⁺ display, added experiment title, added concrete explanation, and pointed correct option to bromine test point. | none |
| CHUNK1_19_1_04_Q025 | fill_blank | repair-only keep | valid | canonical safety supported | mobile-safe | clean | n/a | Added fume-hood safety explanation. | low-depth but essential safety prerequisite |
| CHUNK1_19_1_04_Q026 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Corrected correct-option point key to KCl point and reauthored diagnostics. | low-depth but retained as weakest-ion conclusion |
| CHUNK1_19_1_04_Q027 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Reauthored reducing-order explanation and diagnostics. | low-depth but retained as final comparison conclusion |
| CHUNK1_19_1_04_Q028 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Corrected binding from gas-test-only point to all three concentrated sulfuric acid addition points; added concrete explanation. | low-depth but core operation prerequisite |
| CHUNK1_19_1_04_Q029 | fill_blank | repair-only keep | valid | canonical supported | mobile-safe | clean | n/a | Added wet pH paper acidity explanation. | low-depth but core gas-test observation |
| CHUNK1_19_1_04_Q030 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Rewrote duplicate confirmation item into blue-color mechanism question; normalized I⁻/K⁺ and reauthored all option links. | none |

### 2026-06-15 - `19-1-03` 氯水对溴离子、碘离子混合溶液的氧化顺序

Canonical evidence read: 教材原文在本实验步骤中列出 KBr、KI、CCl₄ 混合体系，并要求逐滴加入氯水、观察 CCl₄ 层颜色变化，以判断 I⁻、Br⁻ 被氧化的先后顺序。Video points checked: `candidate-1-f52542f6` KBr、KI、CCl₄ 混合体系中逐滴加入氯水；`candidate-2-fd1f659e` 观察 CCl₄ 层颜色变化，判断 I⁻、Br⁻ 被氧化的先后顺序。Theory-dependent judgments: I⁻ 还原性强于 Br⁻、足量氯水可继续氧化 Br⁻、以及由观察顺序概括 Cl₂ > Br₂ > I₂ 依赖基础卤素置换/氧化还原理论；试剂组成、逐滴加入、CCl₄ 层颜色观察由 canonical/video points 直接支撑。未引入 AI 判学生答案对错，最终题均为机器确定性判分。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII formulas in effective displayed fields and visible option-link text = 0; option-link label mismatches = 0; invalid point keys = 0; unresolved formula-heavy mobile fill-blank risks = 0. Spotcheck risk classes checked: ASCII formula display, generic explanations, template option-links, negative-stem link semantics, formula-heavy mobile fill blanks, true/false double-negative conflicts, low-depth reagent/color recall, and multi-point binding.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_03_Q001 | single_choice | repair-only keep | multi-point valid | canonical + theory supported | n/a | clean | valid | Replaced generic explanation and reauthored links around I⁻ being first oxidized. | none |
| CHUNK1_19_1_03_Q002 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Explained CCl₄ as extraction/color layer and reauthored solvent distractors. | low-depth but core observation reagent |
| CHUNK1_19_1_03_Q003 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Explained KBr/KI setup and repaired option-link diagnostics. | low-depth but setup prerequisite |
| CHUNK1_19_1_03_Q004 | single_choice | repair-only keep | multi-point valid | canonical supported | n/a | clean | valid | Explained why逐滴加入 and reauthored operation distractors. | none |
| CHUNK1_19_1_03_Q005 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Replaced bare color answer with I₂/CCl₄ evidence explanation. | low-depth but core color evidence |
| CHUNK1_19_1_03_Q006 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Replaced bare color answer with Br₂/CCl₄ evidence explanation. | low-depth but core color evidence |
| CHUNK1_19_1_03_Q007 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Clarified theory bridge from observed oxidation order to Cl₂ > Br₂ > I₂. | none |
| CHUNK1_19_1_03_Q008 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Normalized CCl₄/I⁻/Br⁻/K⁺ display and retained CCl₄-layer purpose item. | none |
| CHUNK1_19_1_03_Q009 | single_choice | repair-only keep | valid | canonical + theory supported | n/a | clean | valid | Explained why first oxidation indicates stronger reducing property. | none |
| CHUNK1_19_1_03_Q010 | single_choice | repair-only keep | valid | canonical supported | n/a | clean | valid | Reauthored negative-stem option links so I⁻/Br⁻ are valid non-answers and K⁺ is spectator. | none |
| CHUNK1_19_1_03_Q011 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Replaced generic true/false explanation with逐滴加入 + CCl₄ color evidence chain. | none |
| CHUNK1_19_1_03_Q012 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Explained CCl₄ role as organic extraction layer. | none |
| CHUNK1_19_1_03_Q013 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Explained I⁻ before Br⁻ oxidation statement. | none |
| CHUNK1_19_1_03_Q014 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Clarified theory dependency for halogen oxidation trend. | none |
| CHUNK1_19_1_03_Q015 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Explained K⁺ as spectator rather than comparison object. | none |
| CHUNK1_19_1_03_Q016 | true_false | repair-only keep | valid | canonical supported | n/a | clean | n/a | Explained CCl₄ is not oxidant; chlorine water supplies oxidant. | none |
| CHUNK1_19_1_03_Q017 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Explained why KBr/KI alone cannot establish order without chlorine water. | none |
| CHUNK1_19_1_03_Q018 | true_false | repair-only keep | valid | canonical + theory supported | n/a | clean | n/a | Explained I₂ purple color evidence in CCl₄. | low-depth but core color evidence |
| CHUNK1_19_1_03_Q019 | true_false | repair-only keep | multi-point valid | canonical supported | n/a | clean | n/a | Corrected reasoning around KI/KBr amounts and false Br⁻-first claim. | none |
| CHUNK1_19_1_03_Q020 | true_false | rewrite | valid | canonical + theory supported | n/a | clean | n/a | Fixed contradictory explanation for enough chlorine water oxidizing Br⁻ after I⁻. | none |
| CHUNK1_19_1_03_Q021 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Replaced formula-fill risk with single-choice first-oxidized-ion item and reauthored links. | overlaps Q001 conceptually but retained as phone-safe rewrite of prior fill |
| CHUNK1_19_1_03_Q022 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Replaced CCl₄ formula fill with phone-safe single choice and concrete CCl₄ role links. | overlaps Q002 conceptually but retained as phone-safe rewrite of prior fill |
| CHUNK1_19_1_03_Q023 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Rewrote KI formula fill into single choice about initial mixed halide setup. | none |
| CHUNK1_19_1_03_Q024 | fill_blank | repair-only keep | multi-point valid | canonical supported | mobile-safe | clean | n/a | Replaced reference-answer explanation with逐滴 operation evidence. | low-depth but short mobile-safe operation term |
| CHUNK1_19_1_03_Q025 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Replaced reference-answer explanation with I₂/CCl₄ purple evidence. | low-depth but short mobile-safe color term |
| CHUNK1_19_1_03_Q026 | single_choice | rewrite | valid | canonical + theory supported | n/a | clean | valid | Rewrote phone-risk color fill as single choice and repaired Br₂ color links. | overlaps Q006 conceptually but retained as phone-safe rewrite of prior fill |
| CHUNK1_19_1_03_Q027 | single_choice | rewrite | multi-point valid | canonical + theory supported | n/a | clean | valid | Rewrote phone-risk order fill as single choice and clarified theory bridge. | overlaps Q007 conceptually but retained as phone-safe rewrite of prior fill |
| CHUNK1_19_1_03_Q028 | single_choice | rewrite | valid | canonical supported | n/a | clean | valid | Normalized CCl₄/I⁻/Br⁻/K⁺ display and concrete explanation. | overlaps Q008 conceptually but retained as second phone-safe observation-purpose item |
| CHUNK1_19_1_03_Q029 | fill_blank | repair-only keep | valid | canonical + theory supported | mobile-safe | clean | n/a | Replaced reference-answer explanation with reducing-property inference. | overlaps Q009 conceptually but short mobile-safe concept term |
| CHUNK1_19_1_03_Q030 | single_choice | rewrite | multi-point valid | canonical supported | n/a | clean | valid | Replaced template distractors with real ion/reagent distractors and concrete K⁺ spectator explanation. | none |

### 2026-06-15 - `19-1-06` partial blocker repair started

Canonical evidence read: textbook experiment 19-1 chlorate section states: (1) add concentrated HCl to KClO₃ crystal and test the evolved gas; (2) compare saturated KClO₃ with Na₂SO₃ under neutral and acidic conditions and verify product with AgNO₃; (3) dissolve KClO₃, add CCl₄ and KI, observe phases, then acidify with H₂SO₄ and observe the change. Video points checked: `candidate-1-86b4f964` KClO₃ + concentrated HCl and wet KI-starch test for Cl₂; `candidate-2-f50a397f` KClO₃ + Na₂SO₃ neutral/acidic comparison; `candidate-3-15b87f0f` AgNO₃ product verification; `candidate-4-7bed40a2` KClO₃ + KI + CCl₄ before/after acidification; `candidate-5-9ebfbe89` acid choice H₂SO₄/HNO₃/HCl discussion. Theory-dependent judgments: HCl/HNO₃ interference and wet KI-starch blue mechanism rely on halogen/chlorate oxidizing-property theory in addition to canonical operation text.

This is a partial repair log, not completion of task 3.6. Remaining `19-1-06` questions still require full per-question semantic rereview before the task checkbox can be marked complete. Current closeout blocker classes checked for the touched items: generic explanation, template option-link diagnostic, visible ASCII formula, ASCII option-link formula, low-depth rewrite duplication, theory dependency, and point-binding semantics.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_06_Q012 | single_choice | rewrite repaired | multi-point valid | canonical + theory supported | n/a | cleaned | valid | Normalized KClO₃/CCl₄/H₂SO₄/HNO₃/K⁺ display; replaced generic explanation with HCl/HNO₃ interference reasoning; moved correct option evidence to acid-choice point. | none for this item |
| CHUNK1_19_1_06_Q014 | single_choice | rewrite repaired | valid | canonical supported | n/a | cleaned | valid | Replaced duplicate medium-effect stem with Na₂SO₃ reductant-role question; reauthored all option links around actual reagent roles. | none for this item |
| CHUNK1_19_1_06_Q016 | single_choice | rewrite repaired | valid | canonical + theory supported | n/a | cleaned | valid | Rewrote gas-test item into wet KI-starch blue mechanism question; normalized Cl₂/H₂/I₂/K⁺ display and replaced template diagnostics. | none for this item |
| CHUNK1_19_1_06_Q018 | single_choice | rewrite repaired | multi-point valid | canonical + theory supported | n/a | cleaned | valid | Replaced duplicate acid-choice item with HCl-specific interference question; added `candidate-1-86b4f964` because KClO₃ + HCl generating Cl₂ is direct evidence. | none for this item |
| CHUNK1_19_1_06_Q020 | single_choice | rewrite repaired | multi-point valid | canonical supported | n/a | cleaned | valid | Replaced duplicate medium-effect item with AgNO₃/AgCl/Cl⁻ product-verification question; added `candidate-3-15b87f0f` to the point binding. | none for this item |
| CHUNK1_19_1_06_Q021 | single_choice | rewrite repaired | multi-point valid | canonical + theory supported | n/a | cleaned | valid | Replaced low-depth KClO₃ formula fill with HNO₃-specific oxidation-interference question; retained acid-choice and KI/CCl₄ points. | none for this item |
| CHUNK1_19_1_06_Q022 | single_choice | rewrite repaired | valid | canonical + theory supported | n/a | cleaned | valid | Replaced Cl₂ formula fill with question about oxidizing property shown by wet KI-starch blue response. | none for this item |
| CHUNK1_19_1_06_Q024 | single_choice | rewrite repaired | multi-point valid | canonical supported | n/a | cleaned | valid | Replaced H₂SO₄ formula fill with acidification observation question explaining CCl₄-layer iodine color. | none for this item |
| CHUNK1_19_1_06_Q025 | single_choice | rewrite repaired | valid | canonical supported | n/a | cleaned | valid | Replaced CCl₄ formula fill with question distinguishing CCl₄ extraction from acidified KClO₃ oxidation. | none for this item |
| CHUNK1_19_1_06_Q027 | single_choice | rewrite repaired | valid | canonical supported | n/a | cleaned | valid | Replaced AgNO₃ formula fill with Ag⁺/Cl⁻/AgCl precipitation-basis question; narrowed point binding to product verification. | none for this item |

### 2026-06-15 - `19-1-06` 氯酸盐的氧化性 - final semantic completion

This final entry supersedes the partial `19-1-06` blocker log above. Codex manually reread all 30 active effective questions against the effective question text, original/proposed source fields, video points, canonical experiment text, and supporting theory where noted. Scripts were used only for parse/risk validation after the manual edits.

Canonical evidence read: KClO₃ crystal + concentrated HCl with evolved gas test; saturated KClO₃ + Na₂SO₃ neutral/acidic comparison; AgNO₃ verification of the reaction product; KClO₃ + KI + CCl₄ before/after H₂SO₄ acidification; acid-choice discussion for H₂SO₄, HNO₃, and HCl.

Video points checked: `candidate-1-86b4f964` KClO₃ + concentrated HCl and wet KI-starch test for Cl₂; `candidate-2-f50a397f` KClO₃ + Na₂SO₃ neutral/acidic comparison; `candidate-3-15b87f0f` AgNO₃ product verification; `candidate-4-7bed40a2` KClO₃ + KI + CCl₄ before/after acidification; `candidate-5-9ebfbe89` acid choice H₂SO₄/HNO₃/HCl.

Theory-dependent judgments: wet KI-starch blue mechanism, I₂ extraction into CCl₄, Ag⁺/Cl⁻/AgCl precipitation basis, HCl-generated Cl₂ interference, HNO₃ oxidation interference, and "KClO₃ as oxidant" language depend on basic oxidation-reduction / precipitation theory in addition to canonical operations. The machine-scored answers remain deterministic.

Validation after final hand repair: active = 30; missing effective explanations = 0; bad effective structure = 0; visible ASCII formulas in effective displayed fields or visible option-link text = 0; template/generic option-link diagnostics = 0; mobile-risk fill blanks = 0; rewrite primary-point mismatch = 0; effective option-link text mismatch = 0; duplicate effective stems = 0. Remaining fill blank count = 1 (`Q026`), retained because the accepted answer is the short Chinese conclusion `介质酸碱性`.

Spotcheck risk classes checked: missing/generic explanation, template option-link diagnostic, visible ASCII formula, ASCII option-link formula, formula/mobile-risk fill blank, ASCII accepted-answer alias, low-depth recognition, true/false template wording, duplicate rewrite, and multi-point binding semantics.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_06_Q001 | single_choice | repair-only keep | multi-point valid: candidate-1 + candidate-4 | canonical + theory supported | n/a | clean | valid | Replaced generic explanation; added candidate-4 and removed unrelated coverage from the effective binding. | none |
| CHUNK1_19_1_06_Q002 | single_choice | keep | valid: candidate-1 | canonical + theory supported | n/a | clean | valid | Confirmed Cl₂ gas identification as prerequisite for later interference/mechanism items. | low-depth but necessary gas-identification prerequisite |
| CHUNK1_19_1_06_Q003 | single_choice | repair-only keep | narrowed to candidate-1 | canonical + theory supported | n/a | clean | valid | Removed over-broad KI/CCl₄ and acid-choice bindings; added concrete retained reason. | low-depth but necessary test-paper prerequisite |
| CHUNK1_19_1_06_Q004 | single_choice | keep | multi-point valid: candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Confirmed H₂SO₄ selection and HCl/HNO₃ interference logic. | none |
| CHUNK1_19_1_06_Q005 | single_choice | keep | valid: candidate-4 | canonical + theory supported | n/a | clean | valid | Confirmed CCl₄ extraction role. | low-depth but required to interpret organic phase color |
| CHUNK1_19_1_06_Q006 | single_choice | keep | valid: candidate-2 | canonical supported | n/a | clean | valid | Confirmed medium-effect comparison. | none |
| CHUNK1_19_1_06_Q007 | single_choice | keep | multi-point valid: candidate-2 + candidate-3 | canonical + theory supported | n/a | clean | valid | Confirmed AgNO₃ product-verification reagent and Cl⁻/AgCl basis. | low-depth but required product-verification prerequisite |
| CHUNK1_19_1_06_Q008 | single_choice | keep | multi-point valid: candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Confirmed acidification phenomenon and I₂/CCl₄ observation. | none |
| CHUNK1_19_1_06_Q009 | single_choice | keep | multi-point valid: candidate-1 + candidate-4; secondary candidate-5 | canonical + theory supported | n/a | clean | valid | Confirmed HCl-generated Cl₂ interference in KI/CCl₄ system. | none |
| CHUNK1_19_1_06_Q010 | single_choice | keep | valid: candidate-4 | canonical + theory supported | n/a | clean | valid | Confirmed oxidation-property inference from I⁻ -> I₂. | none |
| CHUNK1_19_1_06_Q011 | single_choice | rewrite | valid: candidate-2 | canonical supported | n/a | clean | valid | Retained repaired medium-effect single choice. | overlaps Q006 conceptually but remains deterministic |
| CHUNK1_19_1_06_Q012 | single_choice | rewrite | multi-point valid: candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Retained acid-choice interference item with concrete explanation. | none |
| CHUNK1_19_1_06_Q013 | true_false | repair-only keep | narrowed to candidate-1 | canonical + theory supported | n/a | clean | n/a | Rewrote field-like true/false wording into a full gas-test statement. | none |
| CHUNK1_19_1_06_Q014 | single_choice | rewrite | valid: candidate-2 | canonical supported | n/a | clean | valid | Synced top-level option links with effective options and corrected correct-option point key. | none |
| CHUNK1_19_1_06_Q015 | true_false | repair-only keep | valid: candidate-4 | canonical + theory supported | n/a | clean | n/a | Rewrote field-like true/false wording into a CCl₄ extraction statement. | none |
| CHUNK1_19_1_06_Q016 | single_choice | rewrite | valid: candidate-1 | canonical + theory supported | n/a | clean | valid | Synced top-level option links with effective wet KI-starch mechanism options. | none |
| CHUNK1_19_1_06_Q017 | true_false | repair-only keep | valid: candidate-3 | canonical + theory supported | n/a | clean | n/a | Rewrote field-like true/false wording into AgNO₃ product-verification statement. | none |
| CHUNK1_19_1_06_Q018 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Confirmed HCl-specific Cl₂ interference item. | none |
| CHUNK1_19_1_06_Q019 | true_false | repair-only keep | multi-point valid: candidate-1 + candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | n/a | Rewrote field-like true/false wording and added candidate-4 for the affected KI/CCl₄ system. | none |
| CHUNK1_19_1_06_Q020 | single_choice | rewrite | multi-point valid: candidate-2 + candidate-3 | canonical + theory supported | n/a | clean | valid | Fixed top/effective point mismatch and synced option-link text. | none |
| CHUNK1_19_1_06_Q021 | single_choice | rewrite | multi-point valid: candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Retained HNO₃ oxidation-interference rewrite. | none |
| CHUNK1_19_1_06_Q022 | single_choice | rewrite | valid: candidate-1 | canonical + theory supported | n/a | clean | valid | Synced option-link text and retained oxidizing-property rewrite. | none |
| CHUNK1_19_1_06_Q023 | single_choice | repair-only keep | valid: candidate-1 | canonical + theory supported | phone-safe rewrite | clean | valid | Converted former fragile KI-starch fill blank into single choice. | low-depth but necessary test-paper prerequisite |
| CHUNK1_19_1_06_Q024 | single_choice | rewrite | multi-point valid: candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Retained CCl₄-layer iodine-color explanation. | none |
| CHUNK1_19_1_06_Q025 | single_choice | rewrite | valid: candidate-4 | canonical + theory supported | n/a | clean | valid | Retained distinction that CCl₄ extracts I₂ but does not oxidize I⁻. | none |
| CHUNK1_19_1_06_Q026 | fill_blank | repair-only keep | valid: candidate-2 | canonical supported | mobile-safe short Chinese answer | clean | n/a | Replaced generic explanation and logged retention reason for `介质酸碱性`. | low-depth but retained as medium-variable conclusion anchor |
| CHUNK1_19_1_06_Q027 | single_choice | rewrite | valid: candidate-3 | canonical + theory supported | n/a | clean | valid | Retained Ag⁺/Cl⁻/AgCl precipitation-basis rewrite. | none |
| CHUNK1_19_1_06_Q028 | single_choice | repair-only rewrite-from-fill | multi-point valid: candidate-1 + candidate-4 | canonical + theory supported | n/a | clean | valid | Rewrote low-depth color fill into a comparison of wet KI-starch and CCl₄ iodine-color evidence. | none |
| CHUNK1_19_1_06_Q029 | single_choice | repair-only rewrite-from-fill | multi-point valid: candidate-1 + candidate-4 + candidate-5 | canonical + theory supported | n/a | clean | valid | Rewrote fragile HCl fill blank into single choice and added candidate-4 for the affected KI/CCl₄ system. | none |
| CHUNK1_19_1_06_Q030 | single_choice | repair-only rewrite-from-fill | valid: candidate-4 | canonical + theory supported | n/a | clean | valid | Rewrote low-depth `氧化性` fill blank into evidence interpretation of KClO₃ as oxidant. | none |

### 2026-06-15 - `19-1-07` 氯含氧酸盐的氧化性 - final semantic completion

Codex manually reread all 30 records and all 26 active effective questions against the effective question text, original/proposed source fields, video points, canonical experiment text, and supporting theory where noted. Scripts were used only for JSON navigation and validation after manual edits.

Canonical evidence read: the experiment asks students to add NaClO, KClO3, and KClO4 solutions separately to KI-starch solution, observe phenomena, then add H2SO4 to tubes that do not react and observe again, finally comparing the oxidizing ability of the three chlorine oxyacid salts.

Video points checked: `candidate-1-02621b6d` NaClO + KI-starch solution; `candidate-2-1046fab6` KClO3 + KI-starch solution; `candidate-3-596e8eff` KClO4 + KI-starch solution; `candidate-4-391ca911` add H2SO4 to non-reacting systems and compare oxidizing ability.

Theory-dependent judgments: KI-starch blue as evidence for I- oxidized to I2, HNO3 oxidizing-acid interference, and HCl/Cl- redox interference require basic oxidation-reduction / iodine-starch indicator theory in addition to the canonical operation text. Machine-scored answers remain deterministic.

Validation after final hand repair: active = 26; missing effective explanations = 0; active fill blanks = 0; visible ASCII formula in effective displayed fields = 0; template/generic option-link diagnostics = 0; effective option-link text mismatches = 0; rewrite primary/secondary point mismatches = 0; effective stem/explanation contamination by fuchsin or CCl4 = 0.

Spotcheck risk classes checked: missing/generic explanation, template option-link diagnostic, visible ASCII formula, ASCII option-link formula, formula/mobile-risk fill blank, ASCII accepted-answer alias, low-depth recognition, true/false double negative, audit metadata contradiction, effective option-link drift, and multi-point binding semantics.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_07_Q001 | single_choice | repair-only keep | multi-point valid: candidate-1 + candidate-2 + candidate-3 | canonical supported | n/a | clean | valid | Added candidate-2/3 coverage for the shared KI-starch indicator and reauthored all option-link diagnostics. | low-depth but necessary indicator-system prerequisite |
| CHUNK1_19_1_07_Q002 | single_choice | repair-only keep | valid: candidate-1 | canonical + theory supported | n/a | clean | valid | Reauthored option links around NaClO oxidizing I- to I2 rather than template correspondence. | none |
| CHUNK1_19_1_07_Q003 | single_choice | repair-only keep | multi-point valid: candidate-4 primary + candidate-2 secondary | canonical supported | n/a | clean | valid | Corrected point binding to acidification step and removed template diagnostics. | none |
| CHUNK1_19_1_07_Q004 | single_choice | repair-only keep | multi-point valid: candidate-4 primary + candidate-2 secondary | canonical + theory supported | n/a | clean | valid | Reauthored HCl/Cl- interference diagnostics and moved correct evidence to acidification point. | none |
| CHUNK1_19_1_07_Q005 | single_choice | repair-only keep | valid: candidate-4 | canonical + theory supported | n/a | clean | valid | Reauthored HNO3 oxidizing-acid interference diagnostics. | none |
| CHUNK1_19_1_07_Q006 | single_choice | reject | n/a | evidence insufficient for active bank | n/a | n/a | n/a | Kept rejected; not part of active import set. | rejected |
| CHUNK1_19_1_07_Q007 | single_choice | rewrite | multi-point valid: candidate-2 + candidate-4 | canonical + theory supported | n/a | clean | valid | Earlier CCl4-contaminated item retained as acidified KClO3/KI-starch blue evidence question. | none |
| CHUNK1_19_1_07_Q008 | single_choice | reject | n/a | evidence insufficient for active bank | n/a | n/a | n/a | Kept rejected; not part of active import set. | rejected |
| CHUNK1_19_1_07_Q009 | single_choice | rewrite | valid: candidate-1 | canonical + theory supported | n/a | clean | valid | Rewrote fuchsin bleaching item into NaClO + KI-starch blue evidence question; synced top/proposed points and links. | none |
| CHUNK1_19_1_07_Q010 | single_choice | repair-only keep | valid: candidate-4 | canonical supported | n/a | clean | valid | Replaced generic H2SO4 explanation and reauthored acid-choice option links. | none |
| CHUNK1_19_1_07_Q011 | true_false | keep | valid: candidate-1 | canonical + theory supported | n/a | clean | n/a | Confirmed NaClO + KI-starch blue statement against point 1. | none |
| CHUNK1_19_1_07_Q012 | true_false | keep | valid: candidate-2 | canonical + theory supported | n/a | clean | n/a | Confirmed false medium-independence statement for KClO3 oxidation. | none |
| CHUNK1_19_1_07_Q013 | true_false | keep | multi-point valid: candidate-2 + candidate-4 | canonical + theory supported | n/a | clean | n/a | Confirmed H2SO4 vs HNO3 acid-interference statement; theory dependency logged. | none |
| CHUNK1_19_1_07_Q014 | true_false | keep | multi-point valid: candidate-1 + candidate-2 + candidate-4 | canonical + theory supported | n/a | clean | n/a | Confirmed KI-starch blue as iodine evidence across active indicator points. | none |
| CHUNK1_19_1_07_Q015 | true_false | reject | n/a | evidence insufficient for active bank | n/a | n/a | n/a | Kept rejected; not part of active import set. | rejected |
| CHUNK1_19_1_07_Q016 | true_false | rewrite | valid: candidate-1 | canonical + theory supported | n/a | clean | n/a | Rewrote fuchsin bleaching true/false into NaClO + KI-starch blue evidence statement. | none |
| CHUNK1_19_1_07_Q017 | true_false | keep | valid: candidate-4 | canonical + theory supported | n/a | clean | n/a | Confirmed false statement that HCl/HNO3 can freely replace H2SO4. | none |
| CHUNK1_19_1_07_Q018 | true_false | rewrite | multi-point valid: candidate-4 primary + candidate-2/candidate-3 secondary | canonical supported | n/a | clean | n/a | Rewrote CCl4 extraction contamination into H2SO4 acidification-and-observe statement. | none |
| CHUNK1_19_1_07_Q019 | true_false | rewrite | multi-point valid: candidate-1 + candidate-2 + candidate-3, secondary candidate-4 | canonical supported | n/a | clean | n/a | Rewrote low-depth module/title item into observation-chain necessity statement and synced points. | none |
| CHUNK1_19_1_07_Q020 | true_false | keep | multi-point valid: candidate-1 + candidate-2 + candidate-4 | canonical supported | n/a | clean | n/a | Confirmed false K+ color statement as spectator-ion distractor. | none |
| CHUNK1_19_1_07_Q021 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-2 + candidate-3, secondary candidate-4 | canonical + theory supported | n/a | clean | valid | Retained phone-safe single choice about KI-starch role across comparison. | none |
| CHUNK1_19_1_07_Q022 | single_choice | rewrite | multi-point valid: candidate-4 primary + candidate-2/candidate-3 secondary | canonical supported | n/a | clean | valid | Corrected point primary/secondary and reauthored acidification-option diagnostics. | none |
| CHUNK1_19_1_07_Q023 | single_choice | rewrite | valid: candidate-1 | canonical + theory supported | n/a | clean | valid | Rewrote fuchsin fill blank into NaClO oxidizing-agent role single choice. | none |
| CHUNK1_19_1_07_Q024 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-2, secondary candidate-4 | canonical + theory supported | n/a | clean | valid | Completed phone-safe rewrite; removed CCl4 distractor from effective options and reauthored I2 diagnostics. | none |
| CHUNK1_19_1_07_Q025 | fill_blank | reject | n/a | evidence insufficient for active bank | n/a | n/a | n/a | Kept rejected; not part of active import set. | rejected |
| CHUNK1_19_1_07_Q026 | single_choice | rewrite | multi-point valid: candidate-4 primary + candidate-2 secondary | canonical + theory supported | n/a | clean | valid | Rewrote HNO3 fill blank to single choice; logged acid-interference theory dependency and synced point links. | none |
| CHUNK1_19_1_07_Q027 | single_choice | rewrite | multi-point valid: candidate-2 + candidate-4 | canonical + theory supported | n/a | clean | valid | Retained HCl interference single choice with concrete explanation. | none |
| CHUNK1_19_1_07_Q028 | single_choice | rewrite | multi-point valid: candidate-2 + candidate-4 | canonical supported | n/a | clean | valid | Retained repaired KClO3 acidification diagnostic item with concrete option links. | none |
| CHUNK1_19_1_07_Q029 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-2 | canonical + theory supported | n/a | clean | valid | Retained KI-starch blue mechanism item with concrete I- to I2 explanation. | none |
| CHUNK1_19_1_07_Q030 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-2 + candidate-3, secondary candidate-4 | canonical supported | n/a | clean | valid | Retained rewritten comparison-purpose item covering all three salts and acidification. | none |

### 2026-06-15 - Current-release audit revisit for `19-1-01`

Trigger: `final_question_bank_quality_spotcheck_2026-06-15_spec_closeout_current_release_audit.md` found that `CHUNK1_19_1_01_Q025` was a low-depth title/theme fill blank and that `CHUNK1_19_1_01_Q007` needed point-binding scope correction.

Manual evidence reread: original/effective question fields, video points `candidate-1-034a8366` 氯水 + KBr 溶液 + CCl₄, `candidate-2-1e180c68` 氯水 + KI 溶液 + CCl₄, `candidate-3-9b8be606` 溴水 + KI 溶液 + CCl₄, and canonical text `expchunk_00199_8240477bff`, which asks students to use KBr, KI, CCl₄, chlorine water, and bromine water to design test-tube experiments explaining the displacement order of chlorine, bromine, and iodine. The CCl₄ extraction/color interpretation for Br₂/I₂ uses supporting theory where noted.

Scripts used: JSON navigation and parse validation only. The keep/rewrite decisions, point bindings, option diagnostics, and final wording below were made by manual semantic review.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_01_Q007 | single_choice | repair-only keep | multi-point corrected: candidate-1 + candidate-2 + candidate-3 | canonical + theory supported | n/a | clean | valid | Kept the observation question but changed the binding from candidate-3 only to all three CCl₄ color-observation displacement points; added `point_keys` to the correct option and rewrote the correct-option diagnostic to name all three evidence points. | none |
| CHUNK1_19_1_01_Q025 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-2 + candidate-3 | canonical supported | rewritten from fill blank | clean | valid | Rewrote the low-depth fill blank “卤素的____” into a single-choice evidence-chain question asking which operations and CCl₄-layer observations support the Cl₂/Br₂/I₂ oxidation order; added concrete option links and removed mobile short-answer risk. | none |

### 2026-06-15 - `19-1-08` 卤化银的感光性 - wrap-up seed repair partial

Trigger: `final_question_bank_quality_spotcheck_2026-06-15_post_spec_wrapup_audit.md` and the preceding wrap-up audit both found import-blocking failures in this batch, especially `CHUNK1_19_1_08_Q001` and `CHUNK1_19_1_08_Q015`. This section records the first manual semantic repair slice for task `3.8`; the full `19-1-08` batch is not yet complete.

Manual evidence reread: effective/original/proposed question fields, current video points, and canonical experiment text for the silver halide photosensitivity experiment. The canonical operation states that AgCl, AgBr, and AgI precipitates are spread evenly on filter paper, a key is placed on the filter paper, the paper is exposed to light for about ten minutes, and the key outline is observed. It also states that silver halides decompose on exposure to light, with AgCl faster and AgI slowest.

Video points checked: `candidate-1-1e83fb7a` AgCl 沉淀感光性; `candidate-2-2e6322c8` AgBr 沉淀感光性; `candidate-3-991233a2` AgI 沉淀感光性; `candidate-4-fb906ca4` AgCl、AgBr、AgI 涂在滤纸上，用钥匙遮挡后光照，观察钥匙轮廓.

Scripts used: JSON navigation, parse validation, option-link drift validation, and OpenSpec validation only. The keep/rewrite decisions, point bindings, option diagnostics, and final wording below were made by manual semantic review.

Spotcheck risk classes checked in this partial slice: low-depth reagent/object recall, guessable true/false, double-negative true/false, mobile-risk symbolic fill blank, generic explanation, template option-link diagnostic, over-broad point binding, and theory-dependency logging.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_08_Q001 | single_choice | rewrite | narrowed to candidate-4 | canonical supported | n/a | clean | valid | Rewrote low-depth AgNO₃ reagent-name recall into an operation-chain item covering AgNO₃/halide precipitate preparation, filter-paper coating, key shielding, light exposure, and key-outline observation; reauthored all option links. | none |
| CHUNK1_19_1_08_Q015 | true_false | rewrite | changed to candidate-4 | canonical supported | n/a | clean | n/a | Replaced guessable false statement about flame color with a deterministic judgment about the key acting as a light shield to create a bright/dark comparison. | none |
| CHUNK1_19_1_08_Q019 | true_false | repair-only rewrite | valid: candidate-4 | canonical supported | n/a | clean | n/a | Corrected the proposed true/false explanation so it matches the true answer; removed unnecessary theory dependency. | none |
| CHUNK1_19_1_08_Q021 | single_choice | rewrite | narrowed to candidate-4 | canonical supported | rewritten from formula/reagent fill blank | clean | valid | Rewrote the remaining AgNO₃ name-recognition item into a reagent-role-in-operation-chain question; reauthored all option links and removed broad point binding. | none |
| CHUNK1_19_1_08_Q025 | single_choice | rewrite | narrowed to candidate-4 | canonical + theory supported | rewritten from symbolic fill blank | clean | valid | Rewrote the metal-silver mechanism fill blank into single choice; removed visible `Ag` answer alias and explicitly logged that the metallic-silver mechanism depends on supporting theory. | none |

### 2026-06-15 - `19-1-08` 卤化银的感光性 - final semantic completion

This final entry supersedes the partial slice above. Codex manually reread all 30 records and all 27 active effective questions against the original/effective question text, proposed rewrites where present, video points, canonical experiment text, and supporting theory where noted. Scripts were used only for JSON navigation, parse validation, contamination checks, and mechanical blocker scans; every keep/rewrite/reject decision, point binding, option diagnostic, and retained-risk reason below came from manual semantic review.

Canonical evidence read: the experiment lists AgNO₃ solution and KCl/KBr/KI solutions for preparing AgCl, AgBr, and AgI precipitates, then requires spreading the precipitates evenly on filter paper, placing a key on the filter paper, exposing it to light for about ten minutes, removing the key, and observing the outline. The canonical note states that silver halides decompose on exposure to light, with AgCl faster and AgI slowest.

Video points checked: `candidate-1-1e83fb7a` AgCl 沉淀感光性; `candidate-2-2e6322c8` AgBr 沉淀感光性; `candidate-3-991233a2` AgI 沉淀感光性; `candidate-4-fb906ca4` AgCl、AgBr、AgI 涂在滤纸上，用钥匙遮挡后光照，观察钥匙轮廓.

Theory-dependent judgments: only `CHUNK1_19_1_08_Q013` and `CHUNK1_19_1_08_Q025` depend on supporting theory for the metallic-silver mechanism behind darkening. The remaining active questions are supported by the canonical experiment text and points alone.

Validation after final hand repair: active publishable = 27; rejected = 3; JSON parse = pass; active template/generic option-link diagnostics = 0; active generic answer-only explanations = 0; active fill blanks = 4 and all are short Chinese answers (`变深/变暗`, `轮廓`, `浅/较浅`, `遮挡`); active contamination by the earlier key-role rewrite metadata outside Q023 = 0.

Spotcheck risk classes checked: low-depth reagent/object/title recall, guessable true/false, double-negative true/false, mobile-risk symbolic fill blank, generic explanation, template option-link diagnostic, over-broad point binding, wrong distractor point link, formula display, accepted-answer alias visibility, audit metadata contradiction, effective option-link drift, and multi-point binding semantics.

| Question ID | Type | Manual decision | Point binding status | Source support status | Mobile fill-blank status | Formula display status | Option-link status | Repairs made | Remaining risk |
|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_1_08_Q001 | single_choice | rewrite | valid: candidate-4 | canonical supported | n/a | clean | valid | Rewrote AgNO₃ reagent-name recall into the full precipitate-preparation, filter-paper, key-shielding, light-exposure operation chain. | none |
| CHUNK1_19_1_08_Q002 | single_choice | rewrite | narrowed to candidate-4 | canonical supported | n/a | clean | valid | Reframed filter-paper recall into the purpose of carrying precipitate for key-shielded outline observation; synced metadata and option diagnostics. | none |
| CHUNK1_19_1_08_Q003 | single_choice | rewrite | narrowed to candidate-4 | canonical supported | n/a | clean | valid | Reframed key-name recall into the direct consequence of omitting the key: no clear outline or light/shadow contrast. | none |
| CHUNK1_19_1_08_Q004 | single_choice | keep | valid: candidate-4 | canonical supported | n/a | clean | valid | Reauthored explanation for unshielded area darkening after light exposure. | none |
| CHUNK1_19_1_08_Q005 | single_choice | rewrite | multi-point valid: candidate-1 + candidate-2 + candidate-3 | canonical supported | n/a | clean | valid | Rewrote as AgCl/AgBr/AgI photosensitivity-rate comparison from the canonical note. | none |
| CHUNK1_19_1_08_Q006 | single_choice | keep | valid: candidate-4 | canonical supported | n/a | clean | valid | Confirmed key-outline observation and concrete distractor diagnostics. | none |
| CHUNK1_19_1_08_Q007 | single_choice | reject | n/a | not in active bank | n/a | n/a | n/a | Kept rejected; duplicate/generic active replacement exists in adjacent repaired items. | rejected |
| CHUNK1_19_1_08_Q008 | single_choice | keep | valid: candidate-4 | canonical supported | n/a | clean | valid | Reauthored all option diagnostics around the shielded area being lighter than the unshielded area; removed unnecessary theory dependency. | none |
| CHUNK1_19_1_08_Q009 | single_choice | rewrite | narrowed to candidate-4 | canonical supported | n/a | clean | valid | Reframed title-word recall into evidence-based conclusion from the observed key outline and light/dark contrast. | none |
| CHUNK1_19_1_08_Q010 | single_choice | keep | valid: candidate-4 | canonical supported | n/a | clean | valid | Confirmed pre-exposure coating and shielding as operation control to reduce stray light. | none |
| CHUNK1_19_1_08_Q011 | true_false | keep | multi-point valid: candidate-1 + candidate-4 | canonical supported | n/a | clean | n/a | Confirmed AgCl is part of the filter-paper key-shielding photosensitivity observation. | none |
| CHUNK1_19_1_08_Q012 | true_false | keep | multi-point valid: candidate-1 + candidate-2 + candidate-3 | canonical supported | n/a | clean | n/a | Retained AgNO₃/halide precipitate prerequisite with explicit reason: it identifies the silver source needed before the light experiment. | basic prerequisite item retained intentionally |
| CHUNK1_19_1_08_Q013 | true_false | keep | valid: candidate-4 | canonical + theory supported | n/a | clean | n/a | Logged that darkening is canonical but the fine metallic-silver mechanism requires supporting theory. | theory-dependent mechanism |
| CHUNK1_19_1_08_Q014 | true_false | keep | valid: candidate-4 | canonical supported | n/a | clean | n/a | Confirmed the key's role as a light shield forming the outline. | none |
| CHUNK1_19_1_08_Q015 | true_false | rewrite | valid: candidate-4 | canonical supported | n/a | clean | n/a | Rewrote guessable false flame-color statement into deterministic key-shielding comparison. | none |
| CHUNK1_19_1_08_Q016 | single_choice | reject | n/a | not in active bank | n/a | n/a | n/a | Kept rejected; overlaps with repaired key-shielding role items. | rejected |
| CHUNK1_19_1_08_Q017 | true_false | rewrite | valid: candidate-4 | canonical supported | n/a | clean | n/a | Rewrote into a positive statement that light-driven color change helps form the key outline. | none |
| CHUNK1_19_1_08_Q018 | true_false | rewrite | valid: candidate-4 | canonical supported | n/a | clean | n/a | Rewrote into a positive contrast statement; removed double-negative risk. | none |
| CHUNK1_19_1_08_Q019 | true_false | rewrite | valid: candidate-4 | canonical supported | n/a | clean | n/a | Replaced double-negative true/false with a direct statement that the shielded/unshielded light-dark difference is useful. | none |
| CHUNK1_19_1_08_Q020 | true_false | rewrite | multi-point valid: candidate-1 + candidate-2 + candidate-3 | canonical supported | n/a | clean | n/a | Retained AgNO₃ as Ag⁺ source for all three silver-halide precipitates with prerequisite rationale. | basic prerequisite item retained intentionally |
| CHUNK1_19_1_08_Q021 | single_choice | rewrite | valid: candidate-4 | canonical supported | rewritten from fill blank | clean | valid | Rewrote AgNO₃ name recognition into why reagent naming alone is not the full photosensitivity operation. | none |
| CHUNK1_19_1_08_Q022 | single_choice | rewrite | valid: candidate-4 | canonical supported | rewritten from fill blank | clean | valid | Reframed coating/key-light operation as an observation-design question. | none |
| CHUNK1_19_1_08_Q023 | single_choice | rewrite | valid: candidate-4 | canonical supported | rewritten from fill blank | clean | valid | Rewrote key-object fill blank into a key-shielding role single choice; removed phone input risk. | none |
| CHUNK1_19_1_08_Q024 | fill_blank | keep | valid: candidate-4 | canonical supported | safe short Chinese answer | clean | n/a | Reauthored explanation for unshielded area becoming darker; kept `变深/变暗` as deterministic aliases. | retained observation short answer |
| CHUNK1_19_1_08_Q025 | single_choice | rewrite | valid: candidate-4 | canonical + theory supported | rewritten from symbolic fill blank | clean | valid | Rewrote visible `Ag` alias fill blank into single choice; logged metallic-silver mechanism theory dependency. | theory-dependent mechanism |
| CHUNK1_19_1_08_Q026 | fill_blank | keep | valid: candidate-4 | canonical supported | safe short Chinese answer | clean | n/a | Reauthored explanation for observing the key outline; retained `轮廓` as deterministic short answer. | retained observation short answer |
| CHUNK1_19_1_08_Q027 | single_choice | reject | n/a | not in active bank | n/a | n/a | n/a | Kept rejected; duplicate/generic comparison item replaced by repaired active questions. | rejected |
| CHUNK1_19_1_08_Q028 | fill_blank | keep | valid: candidate-4 | canonical supported | safe short Chinese answer | clean | n/a | Reauthored explanation for shielded area being relatively lighter; retained `浅/较浅` as deterministic aliases. | retained observation comparison short answer |
| CHUNK1_19_1_08_Q029 | single_choice | rewrite | valid: candidate-4 | canonical supported | rewritten from fill blank | clean | valid | Rewrote `感光性` title-word fill blank into a conclusion single choice based on the observed outline. | none |
| CHUNK1_19_1_08_Q030 | fill_blank | keep | valid: candidate-4 | canonical supported | safe short Chinese answer | clean | n/a | Reauthored explanation for completing coating and shielding before formal light exposure; retained `遮挡` as operation-control answer. | retained operation-control short answer |


## Evidence-First Coverage Completion Addendum - 2026-06-15

This addendum closes the five active experiment-code gaps found after inventory. Columns follow the chunk prompt: `question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk`.

### 2026-06-15 - `19-2-01` 臭氧的制备与性质 - evidence-first completion

Canonical evidence read: 取少量 BaO₂·2H₂O 固体于小试管，慢慢加入约 2 mL 浓硫酸，反应物置冰水中冷却，用 KI-淀粉试纸检验逸出气体；反应式给出 BaO₂ 与 H₂SO₄ 生成 H₂O₂，浓硫酸条件下 H₂O₂ 可生成 O₃ 和 H₂O。

Video points checked: `candidate-1-7d7dd3ef` BaO₂·2H₂O + 浓 H₂SO₄ 制备臭氧；`candidate-2-dbd095b4` 用 KI-淀粉试纸检验逸出气体。

Theory-dependent judgments: KI-淀粉显色、I⁻ 被 O₃ 氧化为 I₂、低温减少分解属于基础氧化还原/稳定性解释；试剂、操作和方程式由 canonical 直接支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0.

| question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_2_01_Q001 | 19-2-01 | single_choice | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q002 | 19-2-01 | single_choice | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q003 | 19-2-01 | single_choice | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q004 | 19-2-01 | single_choice | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q005 | 19-2-01 | single_choice | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q006 | 19-2-01 | single_choice | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q007 | 19-2-01 | single_choice | rewrite | candidate-1-7d7dd3ef | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | resolved | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_01_Q008 | 19-2-01 | single_choice | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q009 | 19-2-01 | single_choice | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q010 | 19-2-01 | single_choice | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_01_Q011 | 19-2-01 | true_false | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q012 | 19-2-01 | true_false | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | low-temperature decomposition control | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q013 | 19-2-01 | true_false | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | n/a | n/a | clean | low-depth but source-anchored | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q014 | 19-2-01 | true_false | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q015 | 19-2-01 | true_false | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q016 | 19-2-01 | true_false | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q017 | 19-2-01 | true_false | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q018 | 19-2-01 | true_false | rewrite | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | none | true | n/a | n/a | clean | resolved | Repaired rewrite: direct true/false statement and concrete explanation checked. | none |
| CHUNK1_19_2_01_Q019 | 19-2-01 | true_false | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | n/a | n/a | clean | low-depth but source-anchored | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_01_Q020 | 19-2-01 | true_false | rewrite | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | n/a | n/a | clean | low-depth but source-anchored | Repaired rewrite: direct true/false statement and concrete explanation checked. | none |
| CHUNK1_19_2_01_Q021 | 19-2-01 | single_choice | rewrite | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_01_Q022 | 19-2-01 | fill_blank | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_01_Q023 | 19-2-01 | fill_blank | repair-only keep | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | low-temperature decomposition control | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_01_Q024 | 19-2-01 | fill_blank | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_01_Q025 | 19-2-01 | fill_blank | repair-only keep | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_01_Q026 | 19-2-01 | single_choice | rewrite | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_01_Q027 | 19-2-01 | single_choice | rewrite | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_01_Q028 | 19-2-01 | single_choice | rewrite | candidate-1-7d7dd3ef, candidate-2-dbd095b4 | none | canonical + theory supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_01_Q029 | 19-2-01 | single_choice | rewrite | candidate-2-dbd095b4 | candidate-1-7d7dd3ef | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate ice-cooling item into KI-淀粉试纸检验角色 question; reauthored options and links. | none |
| CHUNK1_19_2_01_Q030 | 19-2-01 | single_choice | rewrite | candidate-2-dbd095b4 | none | canonical + theory supported | O₃ oxidation / I₂-starch color | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Fixed option-link text mismatch and replaced generic explanation with I⁻ -> I₂ starch evidence. | none |

### 2026-06-15 - `19-2-03` 过氧化氢的鉴定 - evidence-first completion

Canonical evidence read: H₂O₂ 溶液加入 0.5 mL 乙醚，用 H₂SO₄ 酸化，再滴加 K₂CrO₄，振荡并观察水层和乙醚层颜色；乙醚萃取蓝色 CrO₅ 类物质，是鉴定 H₂O₂ 的关键阳性现象。

Video points checked: `candidate-1-dcc53e2a` H₂O₂ + 乙醚 + H₂SO₄ + K₂CrO₄；`candidate-2-181dfe62` 观察水层和乙醚层颜色变化；`candidate-3-06f59206` 蓝色过氧化铬 / 乙醚层蓝色鉴定 H₂O₂。

Theory-dependent judgments: CrO₅/过氧化铬蓝色、乙醚萃取稳定显色、酸性条件必要性属于 supporting theory；操作顺序和观察对象由 canonical 直接支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0.

| question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_2_03_Q001 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a | none | canonical + theory supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q002 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q003 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a | none | canonical supported | none | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q004 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a | none | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q005 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q006 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q007 | 19-2-03 | single_choice | rewrite | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Kept observation-layer question; normalized formula display and concrete explanation/link evidence. | none |
| CHUNK1_19_2_03_Q008 | 19-2-03 | single_choice | rewrite | candidate-3-06f59206 | candidate-1-dcc53e2a | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote ether-role item with CrO₅ extraction/stability evidence. | none |
| CHUNK1_19_2_03_Q009 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q010 | 19-2-03 | single_choice | repair-only keep | candidate-1-dcc53e2a, candidate-3-06f59206 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_03_Q011 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a | none | canonical supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q012 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q013 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a | none | canonical supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q014 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a | none | canonical + theory supported | none | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q015 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q016 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q017 | 19-2-03 | single_choice | rewrite | candidate-2-181dfe62, candidate-3-06f59206 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate observation item into乙醚层蓝色 positive-evidence question. | none |
| CHUNK1_19_2_03_Q018 | 19-2-03 | single_choice | rewrite | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate ether-role item into why CCl₄ is not the source solvent. | none |
| CHUNK1_19_2_03_Q019 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q020 | 19-2-03 | true_false | repair-only keep | candidate-1-dcc53e2a, candidate-3-06f59206 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_03_Q021 | 19-2-03 | single_choice | rewrite | candidate-3-06f59206 | candidate-1-dcc53e2a | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate observation item into blue过氧化铬类物质 question. | none |
| CHUNK1_19_2_03_Q022 | 19-2-03 | fill_blank | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_03_Q023 | 19-2-03 | single_choice | rewrite | candidate-1-dcc53e2a, candidate-3-06f59206 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate observation item into K₂CrO₄ reagent-role question. | none |
| CHUNK1_19_2_03_Q024 | 19-2-03 | single_choice | rewrite | candidate-1-dcc53e2a | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate ether-role item into acidification-condition question. | none |
| CHUNK1_19_2_03_Q025 | 19-2-03 | fill_blank | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_03_Q026 | 19-2-03 | fill_blank | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_03_Q027 | 19-2-03 | single_choice | rewrite | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate observation item into operation-sequence question. | none |
| CHUNK1_19_2_03_Q028 | 19-2-03 | single_choice | rewrite | candidate-3-06f59206 | candidate-2-181dfe62 | canonical + theory supported | CrO₅ formation and ether extraction | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate ether-role item into positive-result criterion question. | none |
| CHUNK1_19_2_03_Q029 | 19-2-03 | fill_blank | repair-only keep | candidate-1-dcc53e2a, candidate-2-181dfe62 | candidate-3-06f59206 | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_03_Q030 | 19-2-03 | fill_blank | repair-only keep | candidate-1-dcc53e2a, candidate-3-06f59206 | none | canonical + theory supported | CrO₅ formation and ether extraction | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |

### 2026-06-15 - `19-2-04` 过氧化氢的性质 - evidence-first completion

Canonical evidence read: 性质小节覆盖碱性 H₂O₂ + NaOH/乙醇，酸性 H₂O₂ + KI，PbS + H₂O₂ 黑转白，酸性 H₂O₂ + KMnO₄ 褪色，AgNO₃/NaOH 生成 Ag₂O 后再加 H₂O₂，MnSO₄/MnO₂ 介质影响，以及加热、MnO₂、铁粉促进 H₂O₂ 分解。

Video points checked: `candidate-1` 至 `candidate-12` 分别覆盖碱性行为、氧化性、还原性、介质影响和分解点位。

Theory-dependent judgments: I⁻ 氧化、PbS 到 PbSO₄、KMnO₄ 褪色、Ag₂O/Ag 以及 Mn 价态变化使用基础氧化还原 theory；各操作和现象由 canonical/video points 支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0.

| question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_2_04_Q001 | 19-2-04 | single_choice | repair-only keep | candidate-2-7b250a5b | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q002 | 19-2-04 | single_choice | repair-only keep | candidate-3-27767a1e | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q003 | 19-2-04 | single_choice | repair-only keep | candidate-4-ea1c2157 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q004 | 19-2-04 | single_choice | repair-only keep | candidate-1-194f4e08, candidate-5-3ac5384d | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q005 | 19-2-04 | single_choice | repair-only keep | candidate-1-194f4e08, candidate-7-852be99e | candidate-11-7ecd5177, candidate-9-dc20f4a5 | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q006 | 19-2-04 | single_choice | repair-only keep | candidate-11-7ecd5177, candidate-10-f9f14866 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q007 | 19-2-04 | single_choice | repair-only keep | candidate-11-7ecd5177 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q008 | 19-2-04 | single_choice | rewrite | candidate-3-27767a1e | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q009 | 19-2-04 | single_choice | rewrite | candidate-4-ea1c2157 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q010 | 19-2-04 | single_choice | repair-only keep | candidate-1-194f4e08, candidate-2-7b250a5b | candidate-3-27767a1e, candidate-4-ea1c2157, candidate-5-3ac5384d, candidate-6-c75d6ab1, candidate-7-852be99e, candidate-8-e2d7f131, candidate-9-dc20f4a5, candidate-10-f9f14866, candidate-11-7ecd5177, candidate-12-4f2280de | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_04_Q011 | 19-2-04 | true_false | repair-only keep | candidate-2-7b250a5b | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q012 | 19-2-04 | true_false | repair-only keep | candidate-4-ea1c2157 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q013 | 19-2-04 | true_false | repair-only keep | candidate-11-7ecd5177 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q014 | 19-2-04 | true_false | repair-only keep | candidate-3-27767a1e | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q015 | 19-2-04 | true_false | repair-only keep | candidate-9-dc20f4a5 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q016 | 19-2-04 | true_false | repair-only keep | candidate-5-3ac5384d | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q017 | 19-2-04 | true_false | repair-only keep | candidate-11-7ecd5177, candidate-10-f9f14866 | candidate-12-4f2280de | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q018 | 19-2-04 | true_false | repair-only keep | candidate-10-f9f14866 | candidate-11-7ecd5177, candidate-12-4f2280de | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Repaired off-point 制备 temperature statement into H₂O₂ decomposition-by-heating statement. | none |
| CHUNK1_19_2_04_Q019 | 19-2-04 | true_false | rewrite | candidate-4-ea1c2157 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Repaired rewrite: direct true/false statement and concrete explanation checked. | none |
| CHUNK1_19_2_04_Q020 | 19-2-04 | true_false | repair-only keep | candidate-1-194f4e08, candidate-2-7b250a5b | candidate-3-27767a1e, candidate-4-ea1c2157, candidate-5-3ac5384d, candidate-6-c75d6ab1, candidate-7-852be99e, candidate-8-e2d7f131, candidate-9-dc20f4a5, candidate-10-f9f14866, candidate-11-7ecd5177, candidate-12-4f2280de | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_04_Q021 | 19-2-04 | single_choice | rewrite | candidate-2-7b250a5b | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q022 | 19-2-04 | single_choice | rewrite | candidate-3-27767a1e | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q023 | 19-2-04 | fill_blank | repair-only keep | candidate-4-ea1c2157 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_04_Q024 | 19-2-04 | single_choice | rewrite | candidate-1-194f4e08, candidate-2-7b250a5b | candidate-3-27767a1e, candidate-4-ea1c2157, candidate-5-3ac5384d, candidate-6-c75d6ab1, candidate-7-852be99e, candidate-8-e2d7f131, candidate-9-dc20f4a5, candidate-10-f9f14866, candidate-11-7ecd5177, candidate-12-4f2280de | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q025 | 19-2-04 | single_choice | rewrite | candidate-11-7ecd5177 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q026 | 19-2-04 | single_choice | rewrite | candidate-1-194f4e08, candidate-5-3ac5384d | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_2_04_Q027 | 19-2-04 | fill_blank | repair-only keep | candidate-9-dc20f4a5 | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_04_Q028 | 19-2-04 | single_choice | rewrite | candidate-2-7b250a5b | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate role item into KI oxidation observation question. | none |
| CHUNK1_19_2_04_Q029 | 19-2-04 | single_choice | rewrite | candidate-3-27767a1e | none | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate PbS role item into black-to-white observation question. | none |
| CHUNK1_19_2_04_Q030 | 19-2-04 | fill_blank | repair-only keep | candidate-1-194f4e08, candidate-2-7b250a5b | candidate-3-27767a1e, candidate-4-ea1c2157, candidate-5-3ac5384d, candidate-6-c75d6ab1, candidate-7-852be99e, candidate-8-e2d7f131, candidate-9-dc20f4a5, candidate-10-f9f14866, candidate-11-7ecd5177, candidate-12-4f2280de | canonical + theory supported | basic H₂O₂ redox/decomposition theory | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |

### 2026-06-15 - `19-2-05` 过氧化氢的氧化还原性 - evidence-first completion

Canonical evidence read: 本小节直接安排两个点位：Pb(Ac)₂ 试纸 + H₂S 生成 PbS 后滴加 H₂O₂，观察 H₂O₂ 的氧化性；酸性 H₂O₂ 中滴加 KMnO₄，观察紫色褪去以体现 H₂O₂ 的还原性。

Video points checked: `candidate-1-266194d0` 氧化性：Pb(Ac)₂ 试纸 + H₂S 生成 PbS，再滴加 H₂O₂；`candidate-2-75a263a3` 还原性：酸性 H₂O₂ + KMnO₄。

Theory-dependent judgments: H₂O₂ 中氧为 -1 中间价态、PbS 被氧化为硫酸盐、KMnO₄ 被还原褪色并放出 O₂ 属 supporting theory；两条实验点位由 canonical 直接支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0.

| question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_2_05_Q001 | 19-2-05 | single_choice | repair-only keep | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_05_Q002 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Repaired KMnO₄ reduction-property item with concrete explanation and links. | none |
| CHUNK1_19_2_05_Q003 | 19-2-05 | single_choice | repair-only keep | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_05_Q004 | 19-2-05 | single_choice | repair-only keep | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_05_Q005 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate KMnO₄ role item into O₂ product question. | none |
| CHUNK1_19_2_05_Q006 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote comparison item to explicitly bind both redox point roles. | none |
| CHUNK1_19_2_05_Q007 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired PbS observation item with concrete black-to-white evidence. | none |
| CHUNK1_19_2_05_Q008 | 19-2-05 | single_choice | repair-only keep | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_2_05_Q009 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0 | candidate-2-75a263a3 | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate comparison item into oxidation-point identification. | none |
| CHUNK1_19_2_05_Q010 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate PbS item into why PbS is first generated. | none |
| CHUNK1_19_2_05_Q011 | 19-2-05 | true_false | repair-only keep | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_05_Q012 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | candidate-1-266194d0 | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate comparison item into reduction-point identification. | none |
| CHUNK1_19_2_05_Q013 | 19-2-05 | true_false | repair-only keep | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_05_Q014 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate KMnO₄ role item into H₂SO₄ acidification question. | none |
| CHUNK1_19_2_05_Q015 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate comparison item into paired-observation evidence question. | none |
| CHUNK1_19_2_05_Q016 | 19-2-05 | true_false | repair-only keep | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_2_05_Q017 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate KMnO₄ role item into purple-fade observation question. | none |
| CHUNK1_19_2_05_Q018 | 19-2-05 | true_false | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | n/a | clean | resolved | Repaired off-section ether-layer true/false into exclusion of H₂O₂ identification evidence. | none |
| CHUNK1_19_2_05_Q019 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate PbS item into H₂O₂ oxidant-role question. | none |
| CHUNK1_19_2_05_Q020 | 19-2-05 | true_false | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | n/a | clean | resolved | Repaired rewrite: direct true/false statement and concrete explanation checked. | none |
| CHUNK1_19_2_05_Q021 | 19-2-05 | fill_blank | repair-only keep | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_05_Q022 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate PbS item into sulfate product question. | none |
| CHUNK1_19_2_05_Q023 | 19-2-05 | fill_blank | repair-only keep | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_05_Q024 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0 | candidate-2-75a263a3 | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote placeholder distractor item into sulfur-in-PbS oxidation target question. | none |
| CHUNK1_19_2_05_Q025 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate PbS item into not-this-section evidence question. | none |
| CHUNK1_19_2_05_Q026 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate KMnO₄ item into H₂O₂ -> O₂ product question. | none |
| CHUNK1_19_2_05_Q027 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate comparison item into -1 oxygen valence rationale question. | none |
| CHUNK1_19_2_05_Q028 | 19-2-05 | fill_blank | repair-only keep | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_2_05_Q029 | 19-2-05 | single_choice | rewrite | candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate KMnO₄ item into acid-medium purpose question. | none |
| CHUNK1_19_2_05_Q030 | 19-2-05 | single_choice | rewrite | candidate-1-266194d0, candidate-2-75a263a3 | none | canonical + theory supported | H₂O₂ -1 oxygen valence and two redox point mechanisms | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate comparison item into final two-point conclusion question. | none |

### 2026-06-15 - `19-3-01` 二氧化硫的制备（通风橱内进行） - evidence-first completion

Canonical evidence read: 蒸馏瓶内放入 5.0 g Na₂SO₃ 固体，分液漏斗内装浓硫酸，缓慢滴加并点燃酒精灯；滴酸后产生无色、有刺激性气味的 SO₂，加热时气体产生速率加快。

Video points checked: `candidate-1-eaf08062` Na₂SO₃ + 浓 H₂SO₄ 制备 SO₂。

Theory-dependent judgments: SO₂ 的刺激性和毒性、通风橱/减少逸出属于 safety theory；制备试剂、装置操作、加热和气体生成由 canonical 直接支撑。

Validation after hand repair: active = 30; missing effective explanations = 0; generic/template option-link diagnostics = 0; visible ASCII digit formulas in effective displayed fields and visible option-link text = 0; option-link text mismatches = 0; invalid point keys = 0; duplicate effective stems = 0; unresolved mobile fill-blank risks = 0.

| question_id | experiment_code | effective_type | decision | primary_point_keys | secondary_point_keys | canonical_support | supporting_theory_dependency | evidence_sufficient_final | option_link_status | mobile_input_status | formula_display_status | low_depth_status | repairs_made | remaining_risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHUNK1_19_3_01_Q001 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q002 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q003 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q004 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q005 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q006 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Repaired SO₂ safety item with toxicity/stimulus evidence. | none |
| CHUNK1_19_3_01_Q007 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Repaired slow-acid/heating item with source operation evidence. | none |
| CHUNK1_19_3_01_Q008 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q009 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q010 | 19-3-01 | single_choice | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Evidence-first keep: concrete explanation checked and option links reauthored. | none |
| CHUNK1_19_3_01_Q011 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | low-depth but source-anchored | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q012 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q013 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q014 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate safety item into分液漏斗 slow-addition operation question. | none |
| CHUNK1_19_3_01_Q015 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate process item into heating effect question. | none |
| CHUNK1_19_3_01_Q016 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q017 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q018 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | resolved | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q019 | 19-3-01 | true_false | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | resolved | Repaired rewrite: direct true/false statement and concrete explanation checked. | none |
| CHUNK1_19_3_01_Q020 | 19-3-01 | true_false | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | n/a | clean | low-depth but source-anchored | Evidence-first keep: statement, answer, and explanation checked. | none |
| CHUNK1_19_3_01_Q021 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_3_01_Q022 | 19-3-01 | fill_blank | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_3_01_Q023 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_3_01_Q024 | 19-3-01 | fill_blank | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_3_01_Q025 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Rewrote duplicate process item into浓硫酸提供 H⁺ role question. | none |
| CHUNK1_19_3_01_Q026 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate safety item into wrong-safety-practice question. | none |
| CHUNK1_19_3_01_Q027 | 19-3-01 | fill_blank | repair-only keep | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | n/a | mobile-safe | clean | low-depth but short/deterministic | Evidence-first keep: accepted answer is short/deterministic and explanation checked. | none |
| CHUNK1_19_3_01_Q028 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate safety item into导气口 exposure question. | none |
| CHUNK1_19_3_01_Q029 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | low-depth but source-anchored | Repaired rewrite: normalized formula display, concrete explanation, and reauthored option links. | none |
| CHUNK1_19_3_01_Q030 | 19-3-01 | single_choice | rewrite | candidate-1-eaf08062 | none | canonical + safety theory supported | SO₂ safety/toxicity | true | valid / reauthored | n/a | clean | resolved | Rewrote duplicate safety item into complete source-evidence set question. | none |


### 2026-06-15 - post-validation option-link normalization

After the five-gap completion addendum, a whole-chunk validation found old template option-link diagnostics or text mismatches in previously logged items. The following single-choice items kept their effective stems/answers and had only option-link text/diagnostics reauthored so each link matches the visible option text and explains the evidence without template wording.

| question_id | repair | remaining_risk |
|---|---|---|
| CHUNK1_19_1_01_Q022 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_03_Q008 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_03_Q023 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_03_Q028 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q001 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q002 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q003 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q004 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q005 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q007 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q010 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q022 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q023 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q025 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_05_Q026 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_1_07_Q023 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q001 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q002 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q003 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q004 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q005 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q006 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q007 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q008 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q009 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q019 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q021 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q023 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_2_02_Q026 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_3_02_Q001 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_3_02_Q004 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
| CHUNK1_19_3_02_Q008 | Reauthored option links against the already logged canonical/video-point evidence; no stem/answer change. | none |
