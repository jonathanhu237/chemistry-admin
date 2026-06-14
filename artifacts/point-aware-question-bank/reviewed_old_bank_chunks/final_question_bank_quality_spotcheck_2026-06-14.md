# Final Question Bank Quality Spotcheck - 2026-06-14

## Scope

- Files checked:
  - `chunk_1_release_final_v1.json`
  - `chunk_2_release_final_v1.json`
  - `chunk_3_release_final_v1.json`
  - `chunk_4_release_final_v1.json`
  - `chunk_5_release_final_v1.json`
- OpenSpec change closed: `finalize-question-bank-chunks-1-5-for-release`
- Archive location: `E:/chemistry-exam/openspec/changes/archive/2026-06-14-finalize-question-bank-chunks-1-5-for-release`
- Main spec sync: completed; release-grade requirements were applied to `experiment-question-bank-management`.

## Release Counts

| Chunk | Final file | Active questions |
|---|---:|---:|
| chunk_1 | `chunk_1_release_final_v1.json` | 443 |
| chunk_2 | `chunk_2_release_final_v1.json` | 450 |
| chunk_3 | `chunk_3_release_final_v1.json` | 450 |
| chunk_4 | `chunk_4_release_final_v1.json` | 450 |
| chunk_5 | `chunk_5_release_final_v1.json` | 510 |

## Manual Spotcheck Result

Manual sample size: 25 questions, 5 from each chunk.

Overall judgment:
- `chunk_2` to `chunk_5`: sampled questions are source-grounded, deterministic, point-aware, and student-facing enough for release under the current acceptance bar.
- `chunk_1`: sampled questions include good point-aware items, but full-file follow-up checks found release blockers. Do not mark chunk_1 as fully ready until the blockers below are manually repaired.

Manual fixes applied during this spotcheck:
- `CHUNK1_19_1_06_Q011`: normalized final displayed formulas to Unicode subscripts and replaced a generic explanation with a source-specific explanation.
- `CHUNK1_19_2_02_Q030`: added a concrete explanation for the effective fill-blank item.
- `REV_CH4_EXP_20_2_01_Q030`: replaced the weak distractor `章节小标题中的“一”` with a student-facing distractor.
- `REV_CH4_EXP_20_2_06_Q030`: replaced internal wording such as `问观察颜色变化这一类现象` with student-facing option text and updated explanation/diagnostic notes.

## Full-File Follow-Up Checks

These checks were run only against effective release questions: `rewrite` uses `proposed_question`; otherwise the effective original question is used.

| Chunk | Structural bad | Option text mismatch when link text exists | Stale student text | Missing or empty effective explanation | ASCII digit formulas in effective displayed text |
|---|---:|---:|---:|---:|---:|
| chunk_1 | 0 | 0 | 0 | 68 | 137 |
| chunk_2 | 0 | 0 | 0 | 0 | 0 |
| chunk_3 | 0 | 0 | 0 | 0 | 0 |
| chunk_4 | 0 | 0 | 0 | 0 | 0 |
| chunk_5 | 0 | 0 | 0 | 0 | 0 |

Chunk 1 blocker distribution:
- Missing or empty explanations: `19-1-05` has 23, `19-2-02` has 24, `19-3-02` has 21.
- ASCII digit formulas in effective displayed fields are concentrated in `19-3-02`, `19-3-01`, `19-1-06`, `19-2-05`, `19-2-03`, and `19-2-04`.

This means chunk_1 still needs a semantic hand-repair pass before release. The repair should add concrete explanations and normalize displayed formulas such as `CCl4`, `KClO3`, `Na2SO3`, `H2SO4`, `SO2`, and `H2O2` to the expected Unicode presentation where they appear in final effective stems, options, explanations, and visible option-link text.

## Sampled Questions With Point Bindings

| Chunk | Question | Type | Answer | Point binding | Spotcheck judgment |
|---|---|---|---|---|---|
| 1 | `CHUNK1_19_1_01_Q001` | single_choice | A | `candidate-1-034a8366`: 氯水 + KBr 溶液 + CCl₄ | Good. Directly tests chlorine oxidizing bromide through the bound experiment point. |
| 1 | `CHUNK1_19_1_01_Q023` | single_choice | A | `candidate-1-034a8366`: 氯水 + KBr 溶液 + CCl₄; `candidate-2-1e180c68`: 氯水 + KI 溶液 + CCl₄; `candidate-3-9b8be606`: 溴水 + KI 溶液 + CCl₄ | Acceptable but lower-depth. Tests the role of CCl₄ as extraction/observation support across related points. |
| 1 | `CHUNK1_19_1_04_Q023` | fill_blank | KI-淀粉 / 碘化钾-淀粉 | `candidate-1-9a665846`: KI 固体 + 浓硫酸; `candidate-2-1416e2da`: KBr 固体 + 浓硫酸; `candidate-4-a326b299`: 湿试纸检验产生气体; `candidate-5-f8ac28b0`: KBr 与浓硫酸反应后用湿 KI-淀粉试纸检验生成的溴 | Good. Short answer is mobile-safe and deterministic. |
| 1 | `CHUNK1_19_1_06_Q011` | single_choice | A | `candidate-2-f50a397f`: KClO₃ + Na₂SO₃：中性条件与酸性条件对比 | Fixed during spotcheck. Now source-specific and formula presentation is clean. |
| 1 | `CHUNK1_19_2_02_Q030` | fill_blank | 鉴定 / 性质鉴定 | `candidate-1-452aecdc`: Na₂O₂ + 水; `candidate-2-ca62174d`: 冰水冷却; `candidate-3-7f0776ff`: 加入冷却过的 H₂SO₄ 酸化; `candidate-4-10e07c01`: 用试纸检验酸碱性变化 | Fixed during spotcheck by adding a concrete explanation. Still a low-depth short-answer item. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_001` | single_choice | A | `candidate-1-26a8e36e`: 设计方法除去 SO₄²⁻ 干扰; `candidate-2-795f5a0b`: 验证样品中 SO₃²⁻ 的存在 | Good. Tests interference control before sulfite detection. |
| 2 | `EXP_19_4_03_SEMANTIC_FINAL_001` | single_choice | C | `candidate-2-72cbedf8`: 再加入 H₂SO₄ 酸化，观察 KMnO₄ 褪色 | Acceptable. Basic but source-supported. |
| 2 | `EXP_19_4_03_SEMANTIC_FINAL_023` | fill_blank | 还原 / 还原性 | `candidate-2-72cbedf8`: 再加入 H₂SO₄ 酸化，观察 KMnO₄ 褪色 | Acceptable low-depth item; deterministic and mobile-safe. |
| 2 | `EXP_19_4_08_SEMANTIC_FINAL_010` | single_choice | B | `candidate-1-b2e54d23`: FeSO₄·7H₂O + NaNO₃ + 浓 H₂SO₄ 棕色环实验 | Good. Correctly categorizes the nitrate brown-ring test. |
| 2 | `EXP_19_5_01_SEMANTIC_FINAL_004` | single_choice | D | `candidate-1-397a1298`: 水玻璃 + CaCl₂ | Acceptable. Product-category recall, but source-supported. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q001` | single_choice | A | `candidate-1-a3329021`: 镁条除去氧化膜后点燃; `candidate-2-ea144d3d`: 观察镁燃烧及生成物 | Good. Connects operation and observation task. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q011` | true_false | True | `candidate-1-a3329021`: 镁条除去氧化膜后点燃; `candidate-2-ea144d3d`: 观察镁燃烧及生成物 | Good. Not a guess-only true/false item. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q021` | fill_blank | 燃烧 / 燃烧现象 | `candidate-1-a3329021`: 镁条除去氧化膜后点燃; `candidate-2-ea144d3d`: 观察镁燃烧及生成物 | Acceptable. Short, deterministic, but lower cognitive depth. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q026_PF1` | single_choice | A | `candidate-1-a3329021`: 镁条除去氧化膜后点燃; `candidate-2-ea144d3d`: 观察镁燃烧及生成物 | Good. Rewrite avoids asking for a bare product/formula and focuses on experiment purpose. |
| 3 | `OLD_CHUNK3_EXP_19_8_10_Q010` | single_choice | B | `candidate-1-409f5477`: Sn(II) 的还原性; `candidate-2-16bf61f8`: Pb(IV) 的氧化性; `candidate-3-45280201`: Bi(III)/Bi(V) 氧化还原性 | Acceptable. Broad conceptual comparison across multiple points. |
| 4 | `REV_CH4_EXP_20_1_02_Q011` | true_false | True | `candidate-1-5b3e91cf`: CuSO₄ + NH₃·H₂O; `candidate-2-167c639f`: AgNO₃ + NH₃·H₂O; `candidate-3-ee066dec`: ZnSO₄ + NH₃·H₂O; `candidate-4-968503d0`: CdSO₄ + NH₃·H₂O; `candidate-5-2962277d`: HgCl₂ + NH₃·H₂O; `candidate-6-e34dc5e9`: 沉淀与过量氨水溶解观察 | Good. True/false item is grounded by multiple concrete operations. |
| 4 | `REV_CH4_EXP_20_1_03_Q018` | single_choice | A | Multiple points covering Ag halides, Hg(II), Cu(II), Co(II), Ni(II), and Fe(III) ligand reactions | Good as a broad experiment-summary item; multi-point binding is real. |
| 4 | `REV_CH4_EXP_20_1_04_Q006` | single_choice | D | `candidate-1-062b9ba9`: CuSO₄ + KI; `candidate-2-90599e67`: 验证生成 CuI 及副产物 | Good. Tests precipitation driving equilibrium rather than rote reagent naming. |
| 4 | `REV_CH4_EXP_20_2_01_Q030` | single_choice | A | Points for adding NaOH to Ti, Cr, Mn, Fe, Co, Ni salts and comparing hydroxide behavior | Fixed during spotcheck. Current item is student-facing and broad enough. |
| 4 | `REV_CH4_EXP_20_2_06_Q030` | single_choice | A | `candidate-5-26c4b173`: 观察钒不同价态颜色变化; `candidate-7-17ba9ee5`: 各价态钒颜色; `candidate-6-eec2106f`: KMnO₄ 逐步氧化 V²⁺ | Fixed during spotcheck. Now asks an experiment-supported observation task without forcing unsupported color memorization. |
| 5 | `CHK5_SEM_EXP_20_3_04_021` | single_choice | B | `candidate-1-2059a278`: CoCl₂ + KSCN 生成蓝紫色配合物 | Good. Scaffold residue is gone; point binding is direct. |
| 5 | `CHK5_SEM_EXP_20_3_09_014` | single_choice | B | `candidate-1-8ec6df4e`: CoCl₂ + 戊醇 / 丙酮 + 饱和 KSCN | Good. Tests organic solvent plus KSCN observation role. |
| 5 | `CHK5_SEM_EXP_20_3_12_024` | single_choice | B | `candidate-1-862feb96`: TiOSO₄ + H₂O₂ | Good. Complex formula text is preserved and source-grounded. |
| 5 | `CHK5_SEM_EXP_20_3_13_028` | single_choice | B | `candidate-2-4b1d96d3`: 加入 H₂O₂ | Good. Tests peroxide addition and vanadium(V) identification. |
| 5 | `CHK5_SEM_EXP_20_3_14_029` | single_choice | B | `candidate-1-de6f1130`: 设计方案分别检出 Fe³⁺、Co²⁺、Ni²⁺ | Good. Tests interference-aware design rather than a single reagent label. |

## Final QA Decision

Not all five chunks should be declared fully ready as a set yet.

- Ready under current spotcheck: `chunk_2`, `chunk_3`, `chunk_4`, `chunk_5`.
- Needs manual semantic repair before release: `chunk_1`.

Required next action for chunk_1:
1. Manually add concrete explanations for the 68 effective questions with missing or empty explanations.
2. Manually normalize ASCII digit formulas in effective student-facing text and visible option-link text.
3. Re-run the same effective-question checks and then re-sample chunk_1.

