# chunk_5 Cross Audit by Chat 4

- Reviewer chat: Chat 4
- Target chunk: chunk_5
- Audit time: 2026-06-15 19:03:49 +08:00
- Rebuilt JSON directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5`
- Evidence sources:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Scope note: read-only cross-audit of rebuilt JSON content. No rebuilt JSON or release JSON was edited.

## 1. Audit Coverage

- Total packets: 17
- Total questions: 510
- Actual audited questions: 52
- Audited type coverage: single_choice 31, true_false 7, fill_blank 14
- Audited supporting_theory_required=true questions: 27
- Audited multi-point questions: 24
- Required seed questions read: 5 / 5

The sample intentionally favored multi-point questions, fill_blank questions, supporting-theory questions, long explanations, adjacent-experiment distractors, and recently repaired seed/risk areas. Scripts were used only for sampling, counting, and risk location; verdicts below come from reading the sampled question stem/options/answer/explanation, point keys, option_links, source_audit, video_points/evidence fields where present.

## 2. Audited Question List and Verdicts

| experiment_code | question_id | question_type | verdict |
|---|---|---|---|
| 20-2-08 | CHK5_SEM_EXP_20_2_08_019 | single_choice | PASS |
| 20-2-08 | CHK5_SEM_EXP_20_2_08_025 | single_choice | PASS |
| 20-2-08 | CHK5_SEM_EXP_20_2_08_027 | single_choice | PASS |
| 20-2-08 | CHK5_SEM_EXP_20_2_08_030 | fill_blank | PASS |
| 20-2-09 | CHK5_SEM_EXP_20_2_09_019 | single_choice | PASS |
| 20-2-09 | CHK5_SEM_EXP_20_2_09_020 | single_choice | PASS |
| 20-2-09 | CHK5_SEM_EXP_20_2_09_025 | fill_blank | P0_BLOCKER |
| 20-2-09 | CHK5_SEM_EXP_20_2_09_030 | fill_blank | P0_BLOCKER |
| 20-2-10 | CHK5_SEM_EXP_20_2_10_011 | true_false | P0_BLOCKER |
| 20-2-10 | CHK5_SEM_EXP_20_2_10_023 | fill_blank | PASS |
| 20-2-10 | CHK5_SEM_EXP_20_2_10_024 | single_choice | PASS |
| 20-3-01 | CHK5_SEM_EXP_20_3_01_002 | single_choice | P0_BLOCKER |
| 20-3-01 | CHK5_SEM_EXP_20_3_01_017 | true_false | PASS |
| 20-3-01 | CHK5_SEM_EXP_20_3_01_028 | single_choice | PASS |
| 20-3-02 | CHK5_SEM_EXP_20_3_02_012 | true_false | PASS |
| 20-3-02 | CHK5_SEM_EXP_20_3_02_025 | single_choice | PASS |
| 20-3-02 | CHK5_SEM_EXP_20_3_02_027 | single_choice | P2_MINOR |
| 20-3-03 | CHK5_SEM_EXP_20_3_03_008 | single_choice | PASS |
| 20-3-03 | CHK5_SEM_EXP_20_3_03_016 | true_false | PASS |
| 20-3-03 | CHK5_SEM_EXP_20_3_03_024 | fill_blank | PASS |
| 20-3-04 | CHK5_SEM_EXP_20_3_04_004 | single_choice | PASS |
| 20-3-04 | CHK5_SEM_EXP_20_3_04_028 | single_choice | PASS |
| 20-3-04 | CHK5_SEM_EXP_20_3_04_030 | single_choice | PASS |
| 20-3-05 | CHK5_SEM_EXP_20_3_05_021 | single_choice | PASS |
| 20-3-05 | CHK5_SEM_EXP_20_3_05_030 | fill_blank | PASS |
| 20-3-06 | CHK5_SEM_EXP_20_3_06_005 | single_choice | P1_BLOCKER |
| 20-3-06 | CHK5_SEM_EXP_20_3_06_028 | fill_blank | PASS |
| 20-3-06 | CHK5_SEM_EXP_20_3_06_030 | single_choice | P1_BLOCKER |
| 20-3-07 | CHK5_SEM_EXP_20_3_07_014 | true_false | PASS |
| 20-3-07 | CHK5_SEM_EXP_20_3_07_017 | single_choice | P1_BLOCKER |
| 20-3-07 | CHK5_SEM_EXP_20_3_07_026 | fill_blank | PASS |
| 20-3-08 | CHK5_SEM_EXP_20_3_08_024 | fill_blank | PASS |
| 20-3-08 | CHK5_SEM_EXP_20_3_08_027 | single_choice | P1_BLOCKER |
| 20-3-08 | CHK5_SEM_EXP_20_3_08_030 | fill_blank | PASS |
| 20-3-09 | CHK5_SEM_EXP_20_3_09_015 | true_false | PASS |
| 20-3-09 | CHK5_SEM_EXP_20_3_09_028 | single_choice | P1_BLOCKER |
| 20-3-09 | CHK5_SEM_EXP_20_3_09_029 | single_choice | P1_BLOCKER |
| 20-3-10 | CHK5_SEM_EXP_20_3_10_019 | true_false | PASS |
| 20-3-10 | CHK5_SEM_EXP_20_3_10_025 | fill_blank | PASS |
| 20-3-10 | CHK5_SEM_EXP_20_3_10_030 | single_choice | P1_BLOCKER |
| 20-3-11 | CHK5_SEM_EXP_20_3_11_009 | single_choice | P1_BLOCKER |
| 20-3-11 | CHK5_SEM_EXP_20_3_11_027 | fill_blank | PASS |
| 20-3-11 | CHK5_SEM_EXP_20_3_11_030 | single_choice | P1_BLOCKER |
| 20-3-12 | CHK5_SEM_EXP_20_3_12_008 | single_choice | P1_BLOCKER |
| 20-3-12 | CHK5_SEM_EXP_20_3_12_028 | single_choice | P1_BLOCKER |
| 20-3-12 | CHK5_SEM_EXP_20_3_12_029 | fill_blank | PASS |
| 20-3-13 | CHK5_SEM_EXP_20_3_13_023 | single_choice | P1_BLOCKER |
| 20-3-13 | CHK5_SEM_EXP_20_3_13_025 | fill_blank | P2_MINOR |
| 20-3-13 | CHK5_SEM_EXP_20_3_13_026 | single_choice | P1_BLOCKER |
| 20-3-14 | CHK5_SEM_EXP_20_3_14_001 | single_choice | P1_BLOCKER |
| 20-3-14 | CHK5_SEM_EXP_20_3_14_021 | single_choice | P1_BLOCKER |
| 20-3-14 | CHK5_SEM_EXP_20_3_14_030 | single_choice | P1_BLOCKER |

Verdict counts in audited sample: PASS 30, P2_MINOR 2, P1_BLOCKER 16, P0_BLOCKER 4.

## 3. Non-PASS Findings

| question_id | severity | problem field | problem original text | why it blocks or risks import | suggested handling |
|---|---:|---|---|---|---|
| CHK5_SEM_EXP_20_2_09_025 | P0 | stem | `在《20-2-09 钛(Ⅳ)盐的水解》中，加水____是 TiOSO₄ 水解观察的重要操作。` | Student-visible raw packet code `20-2-09` appears in the question. The chemistry itself is deterministic, but the visible code is internal release metadata. | Rewrite as a normal lab task, e.g. refer to "钛(Ⅳ)盐水解实验" without the packet number. |
| CHK5_SEM_EXP_20_2_09_030 | P0 | stem | `在《20-2-09 钛(Ⅳ)盐的水解》中，钛(Ⅳ)盐水解前需要加入适量____水。` | Same P0: student-visible packet code in stem. | Remove `20-2-09`; keep short deterministic blank "蒸馏". |
| CHK5_SEM_EXP_20_2_10_011 | P0 | stem | `在《20-2-10 小设计实验》中，混合溶液含 Cr³⁺、Al³⁺、Mn²⁺。` | Student-visible packet code `20-2-10`; otherwise the true/false answer is supported. | Use natural wording such as "在分离并检出 Cr³⁺、Al³⁺、Mn²⁺ 的小设计实验中...". |
| CHK5_SEM_EXP_20_3_01_002 | P0 | stem | `记录《20-3-01 水合阳离子颜色》时，哪种做法最能避免把水合阳离子颜色与阴离子颜色混记？` | Student-visible packet code `20-3-01`; the tested skill is useful, but the stem exposes raw internal numbering. | Remove packet number and phrase as a record-keeping chemistry question. |
| CHK5_SEM_EXP_20_3_02_027 | P2 | source_audit.supporting_theory_chunk_ids | supporting theory id `textbook_prose_00789_e61f8704bd` | The answer is supported by canonical experiment evidence, but the cited theory appears to be lead/chromate context rather than necessary support for the Cr₂O₇²⁻ record-boundary question. | Either remove supporting theory requirement or replace with a directly relevant chromate/dichromate source if available. |
| CHK5_SEM_EXP_20_3_06_005 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | option_links structurally correspond to options, but diagnostics are not natural teaching notes; this violates the required option_links quality contract. | Fill each option diagnostic with a short natural reason tied to EDTA, Fe(Ⅱ), AgNO₃, and distractor chemistry. |
| CHK5_SEM_EXP_20_3_06_030 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add natural diagnostics for Fe³⁺ interference, KI/Cu²⁺, and incorrect distractors. |
| CHK5_SEM_EXP_20_3_07_017 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for ligand-stability comparison and adjacent-experiment distractors. |
| CHK5_SEM_EXP_20_3_08_027 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics distinguishing Fe(Ⅱ) and Fe(Ⅲ) tests. |
| CHK5_SEM_EXP_20_3_09_028 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue; additionally the cited theory mostly supports Fe-SCN context while the Co-SCN organic-medium explanation should be directly supported if possible. | Add diagnostics and consider a more direct Co(Ⅱ)-SCN theory/table source. |
| CHK5_SEM_EXP_20_3_09_029 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue; supporting theory is stronger for Fe-SCN than for the Co blue comparison. | Add diagnostics and cite direct Co-SCN color support if available. |
| CHK5_SEM_EXP_20_3_10_030 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for Ni(Ⅱ)-丁二酮肟 and adjacent Co/Fe/V distractors. |
| CHK5_SEM_EXP_20_3_11_009 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for the chromium identification sequence and distractor operations. |
| CHK5_SEM_EXP_20_3_11_030 | P1 | options/explanation and option_links | options include `铬由 +3 降低到 0`, `铬由 +3 升高到 +6`, `铬始终保持 -1`; explanation includes `+3` and `+6`; diagnostics are `null` | Visible chemistry display uses ASCII signed oxidation numbers. This violates the visible display rule. option_links diagnostics are also absent. | Use Chinese/full-width/superscript-friendly display such as `三价`/`六价` or `＋Ⅲ`/`＋Ⅵ` consistently, and add natural diagnostics. |
| CHK5_SEM_EXP_20_3_12_008 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for Ti(Ⅳ)-H₂O₂/NH₃·H₂O observation chain and distractors. |
| CHK5_SEM_EXP_20_3_12_028 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for the two-step Ti(Ⅳ) observation. |
| CHK5_SEM_EXP_20_3_13_023 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for the H₂O₂补加 instruction and distractors. |
| CHK5_SEM_EXP_20_3_13_025 | P2 | explanation | `填“过氧”可概括该物种特征。` while accepted visible answer is `过氧钒` | Deterministic grading is acceptable, but explanation wording names a shorter answer that is not in accepted_answers. | Change explanation to say `填“过氧钒”` or add `过氧` as an accepted answer if pedagogically intended. |
| CHK5_SEM_EXP_20_3_13_026 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for excess H₂O₂ color change and distractors. |
| CHK5_SEM_EXP_20_3_14_001 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for target-ion list Fe³⁺/Co²⁺/Ni²⁺ and distractors. |
| CHK5_SEM_EXP_20_3_14_021 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for Fe³⁺ KSCN interference in Co²⁺ judgment. |
| CHK5_SEM_EXP_20_3_14_030 | P1 | option_links[].diagnostic_note | four diagnostic_note values are `null` | Same option_links issue. | Add diagnostics for complete design requirements: target ion, reagent, positive phenomenon, interference control. |

## 4. Required Special Lists

### Student-visible review/internal-language hits

No sampled question exposed `题库`, `RAG`, `canonical`, `packet`, `evidence-first`, `机器判分`, or `移动端稳定` in student-visible fields. However, raw packet-style experiment codes are student-visible and are treated as P0 because the prompt explicitly forbids raw id exposure.

Full chunk scan found 15 visible raw-code hits:

- CHK5_SEM_EXP_20_2_08_001: `在《20-2-08 铬(Ⅲ)盐的水解》中...`
- CHK5_SEM_EXP_20_2_08_006: `与《20-2-08 铬(Ⅲ)盐的水解》相比...`
- CHK5_SEM_EXP_20_2_08_023: `在《20-2-08 铬(Ⅲ)盐的水解》中...`
- CHK5_SEM_EXP_20_2_09_001: `在《20-2-09 钛(Ⅳ)盐的水解》中...`
- CHK5_SEM_EXP_20_2_09_022: `在《20-2-09 钛(Ⅳ)盐的水解》中...`
- CHK5_SEM_EXP_20_2_09_025: `在《20-2-09 钛(Ⅳ)盐的水解》中...`
- CHK5_SEM_EXP_20_2_09_030: `在《20-2-09 钛(Ⅳ)盐的水解》中...`
- CHK5_SEM_EXP_20_2_10_001: `在《20-2-10 小设计实验》中...`
- CHK5_SEM_EXP_20_2_10_009: `下列哪项最符合《20-2-10 小设计实验》的任务要求？`
- CHK5_SEM_EXP_20_2_10_011: `在《20-2-10 小设计实验》中...`
- CHK5_SEM_EXP_20_2_10_018: `...完成《20-2-10 小设计实验》。`
- CHK5_SEM_EXP_20_3_01_001: `在《20-3-01 水合阳离子颜色》实验中...`
- CHK5_SEM_EXP_20_3_01_002: `记录《20-3-01 水合阳离子颜色》时...`
- CHK5_SEM_EXP_20_3_02_001: `在《20-3-02 阴离子颜色》实验中...`
- CHK5_SEM_EXP_20_3_03_001: `在《20-3-03 Cr(Ⅲ) 的水合异构现象》实验中...`

### Evidence insufficient

- No sampled question was judged P0 for answer unsupported by canonical evidence.
- P2 evidence/source-audit risk: CHK5_SEM_EXP_20_3_02_027 has a supporting theory id that appears unnecessary or weakly related for the actual Cr₂O₇²⁻ record-boundary question.
- Supporting-theory caution: CHK5_SEM_EXP_20_3_09_028 and CHK5_SEM_EXP_20_3_09_029 would benefit from a direct Co(Ⅱ)-SCN color/organic-medium support source; current chemistry is plausible from canonical operation plus related theory, but the theory citation is not ideal.

### Point binding issues

- No sampled P0/P1 point binding error was found.
- Multi-point audited questions generally crossed real record groups, operation chains, observation comparisons, or design requirements.
- The raw-code P0 cases should still retain their existing chemistry point binding after wording repair.

### option_links issues

- Structural one-to-one checks passed for sampled single_choice questions.
- Content quality failed broadly: full chunk scan found 672 `option_links[].diagnostic_note` values that are null, covering 168 questions. These are concentrated in packets 20-3-06 through 20-3-14.
- Sampled P1 examples: CHK5_SEM_EXP_20_3_06_005, CHK5_SEM_EXP_20_3_06_030, CHK5_SEM_EXP_20_3_07_017, CHK5_SEM_EXP_20_3_08_027, CHK5_SEM_EXP_20_3_09_028, CHK5_SEM_EXP_20_3_09_029, CHK5_SEM_EXP_20_3_10_030, CHK5_SEM_EXP_20_3_11_009, CHK5_SEM_EXP_20_3_11_030, CHK5_SEM_EXP_20_3_12_008, CHK5_SEM_EXP_20_3_12_028, CHK5_SEM_EXP_20_3_13_023, CHK5_SEM_EXP_20_3_13_026, CHK5_SEM_EXP_20_3_14_001, CHK5_SEM_EXP_20_3_14_021, CHK5_SEM_EXP_20_3_14_030.

### fill_blank mobile risk

- No sampled fill_blank question required typing a complex formula, ionic equation, LaTeX, or ambiguous long alias as the visible answer.
- Sampled safe blanks include `水解`, `稀释`, `蒸馏`, `两性`, `氨合物`, `氧化还原反应`, `配体`, `蓝色`, `配合`, `鲜红色`, `深蓝色`, `碱`, `过氧钒`.
- P2 wording issue only: CHK5_SEM_EXP_20_3_13_025 explanation says `过氧` while the accepted visible answer is `过氧钒`.

### supporting theory risks

- CHK5_SEM_EXP_20_3_02_027: supporting theory appears weakly related or unnecessary.
- CHK5_SEM_EXP_20_3_09_028 and CHK5_SEM_EXP_20_3_09_029: theory source should more directly support Co(Ⅱ)-SCN blue/organic medium if available.
- No sampled supporting_theory_required question was found to require subjective AI judgment.

### visible chemistry display risks

Full chunk scan found 15 visible ASCII signed oxidation-number hits in 5 questions:

- CHK5_SEM_EXP_20_2_08_029
- CHK5_SEM_EXP_20_3_11_020
- CHK5_SEM_EXP_20_3_11_030
- CHK5_SEM_EXP_20_3_12_009
- CHK5_SEM_EXP_20_3_12_027

Sampled confirmed issue: CHK5_SEM_EXP_20_3_11_030 uses `+3`, `+6`, `-1` in options/explanation. This should be rewritten with student-visible chemistry notation that avoids ASCII charge/oxidation display.

### Low quality but retainable

- CHK5_SEM_EXP_20_3_13_025: grading target is deterministic, but explanation should match the accepted answer exactly.
- CHK5_SEM_EXP_20_3_02_027: chemistry answer is supported by canonical evidence, but source_audit theory attachment should be cleaned.

### Seed questions with no issue found

- CHK5_SEM_EXP_20_2_08_019
- CHK5_SEM_EXP_20_2_08_025
- CHK5_SEM_EXP_20_2_08_027
- CHK5_SEM_EXP_20_2_09_019
- CHK5_SEM_EXP_20_2_09_020

## 5. Final Validation Snapshot

- JSON parse: PASS for all 17 rebuilt JSON files.
- Total question count: 510.
- Packet count: 17.
- Audited question count: 52.
- Required seed coverage: PASS.
- single_choice answer/options/option_links structural check: PASS for labels/answers/link count in scan, but FAIL for diagnostic_note content because 672 links are null.
- RAG id structural check from scan: PASS, 54 RAG references checked with 0 missing.
- No sampled machine-subjective grading issue found.
- No sampled fill_blank mobile high-risk formula answer found.
- Raw id / packet-code visible text: FAIL, 15 full-chunk hits; 4 confirmed in audited sample.
- ASCII signed oxidation-number display: FAIL, 15 visible hits in 5 questions; 1 confirmed in audited sample.
- Student-visible audit-language words such as `题库`, `RAG`, `canonical`, `evidence-first`, `机器判分`, `移动端稳定`: no sampled direct hit, but raw packet-style ids remain blocking.

## 6. Final Decision

FAIL: chunk_5 cannot enter merge/import in the current rebuilt state.

Reason: the audited sample already contains P0_BLOCKER raw packet-code exposure in student-visible stems, and the full chunk scan shows the same pattern across multiple packets. In addition, a broad option_links diagnostic_note null issue produces repeated P1 blockers, and visible ASCII oxidation-number formatting remains in several questions. These issues should be repaired in rebuilt JSON before merge/import consideration.
