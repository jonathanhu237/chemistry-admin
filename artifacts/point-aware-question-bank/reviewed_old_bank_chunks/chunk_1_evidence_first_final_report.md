# Chunk 1 Evidence-First Final Report

Date: 2026-06-15

## Scope

- Release JSON: `chunk_1_release_final_v1.json`
- Manual log: `manual_semantic_rereview_logs/chunk_1_manual_semantic_rereview_log.md`
- Experiment range: `19-1-01` through `19-3-02`
- Constraint followed: chunk 1 only; no other chunk release files or OpenSpec task files were edited by this pass.

## Final Counts

| metric | value |
|---|---:|
| total release items | 450 |
| active effective items | 443 |
| rejected items | 7 |
| keep decisions | 274 |
| rewrite decisions | 169 |
| single choice / true-false / fill blank | 263 / 129 / 51 |
| option links reauthored and validated | 263 / 263 |

## Experiment Coverage

| experiment_code | title | active | rejected | keep | rewrite | effective type counts SC/TF/FB | final validation |
|---|---|---:|---:|---:|---:|---|---|
| 19-1-01 | 氯、溴、碘的置换次序 | 30 | 0 | 14 | 16 | 19/10/1 | pass |
| 19-1-02 | 氯水、溴水、碘水氧化性差异的比较 | 30 | 0 | 19 | 11 | 18/10/2 | pass |
| 19-1-03 | 氯水对溴离子、碘离子混合溶液的氧化顺序 | 30 | 0 | 21 | 9 | 17/10/3 | pass |
| 19-1-04 | 卤素离子的还原性（通风橱内进行） | 30 | 0 | 22 | 8 | 15/9/6 | pass |
| 19-1-05 | 次氯酸盐的氧化性 | 30 | 0 | 23 | 7 | 16/10/4 | pass |
| 19-1-06 | 氯酸盐的氧化性 | 30 | 0 | 19 | 11 | 25/4/1 | pass |
| 19-1-07 | 氯含氧酸盐的氧化性 | 26 | 4 | 12 | 14 | 17/9/0 | pass |
| 19-1-08 | 卤化银的感光性 | 27 | 3 | 12 | 15 | 14/9/4 | pass |
| 19-2-01 | 臭氧的制备与性质 | 30 | 0 | 21 | 9 | 16/10/4 | pass |
| 19-2-02 | 过氧化氢的制备 | 30 | 0 | 21 | 9 | 15/9/6 | pass |
| 19-2-03 | 过氧化氢的鉴定 | 30 | 0 | 21 | 9 | 17/8/5 | pass |
| 19-2-04 | 过氧化氢的性质 | 30 | 0 | 20 | 10 | 17/10/3 | pass |
| 19-2-05 | 过氧化氢的氧化还原性 | 30 | 0 | 10 | 20 | 22/5/3 | pass |
| 19-3-01 | 二氧化硫的制备（通风橱内进行） | 30 | 0 | 18 | 12 | 19/8/3 | pass |
| 19-3-02 | 二氧化硫的性质 | 30 | 0 | 21 | 9 | 16/8/6 | pass |

Manual-log coverage after completion: all 443 active effective question IDs appear in the log; missing active IDs = 0.

## Major Repairs

| area | repair summary |
|---|---|
| 19-2-01 | Closed unlogged ozone section; fixed Q028 placeholder distractors and Q030 option-link mismatch; repaired duplicate ice-cooling item as KI-淀粉检验-role question. |
| 19-2-03 | Rewrote duplicate H₂O₂ identification items into distinct observation-layer, ether-role, CrO₅, acidification, reagent-role, operation-sequence, and positive-result questions. |
| 19-2-04 | Repaired off-point H₂O₂ preparation-temperature statement into decomposition-by-heating evidence; split duplicate KI/PbS items into observation-specific questions. |
| 19-2-05 | Rebuilt repeated redox items around the two canonical points: PbS oxidation and acidified KMnO₄ reduction; fixed contradictory true/false explanations. |
| 19-3-01 | Reworked duplicate SO₂ safety/process items into distinct fume-hood, slow acid addition, heating effect, acid role, wrong safety practice, exposure, and complete-evidence questions. |
| whole chunk | Safe-normalized formula/ion display without corrupting KI-淀粉; reauthored 32 old template option-link sets from previously logged sections; updated release metadata counts. |

## Rejected / Evidence Insufficient

The active import set excludes these 7 items. They remain rejected rather than repaired because the effective question would otherwise depend on off-point or insufficient evidence.

| question_id | experiment_code | final status |
|---|---|---|
| CHUNK1_19_1_07_Q006 | 19-1-07 | rejected; evidence insufficient or off-scope for active import after evidence-first review |
| CHUNK1_19_1_07_Q008 | 19-1-07 | rejected; evidence insufficient or off-scope for active import after evidence-first review |
| CHUNK1_19_1_07_Q015 | 19-1-07 | rejected; evidence insufficient or off-scope for active import after evidence-first review |
| CHUNK1_19_1_07_Q025 | 19-1-07 | rejected; evidence insufficient or off-scope for active import after evidence-first review |
| CHUNK1_19_1_08_Q007 | 19-1-08 | rejected; evidence insufficient or off-scope for active import after evidence-first review |
| CHUNK1_19_1_08_Q016 | 19-1-08 | rejected; evidence insufficient or off-scope for active import after evidence-first review |
| CHUNK1_19_1_08_Q027 | 19-1-08 | rejected; evidence insufficient or off-scope for active import after evidence-first review |

## Supporting Theory Used

Supporting theory was used only where canonical experiment text/video points established the operation and observation but chemical interpretation required theory, such as halogen displacement order, I₂-starch color, H₂O₂ redox duality, CrO₅ ether extraction, SO₂ safety, and decomposition/medium effects.

| experiment_code | active theory-dependent items | supporting theory chunk ids | examples |
|---|---:|---|---|
| 19-1-01 | 13 | textbook_prose_00028_a4c7b7c9ae | CHUNK1_19_1_01_Q002, CHUNK1_19_1_01_Q003, CHUNK1_19_1_01_Q004, CHUNK1_19_1_01_Q006, CHUNK1_19_1_01_Q007, CHUNK1_19_1_01_Q009 |
| 19-1-03 | 15 | textbook_prose_00028_a4c7b7c9ae, textbook_prose_00043_871f62b3d9 | CHUNK1_19_1_03_Q002, CHUNK1_19_1_03_Q004, CHUNK1_19_1_03_Q005, CHUNK1_19_1_03_Q006, CHUNK1_19_1_03_Q008, CHUNK1_19_1_03_Q011 |
| 19-1-06 | 7 | textbook_prose_00028_a4c7b7c9ae, textbook_prose_00114_be4a779fba, textbook_prose_00006_872b19158c | CHUNK1_19_1_06_Q005, CHUNK1_19_1_06_Q007, CHUNK1_19_1_06_Q012, CHUNK1_19_1_06_Q015, CHUNK1_19_1_06_Q017, CHUNK1_19_1_06_Q018 |
| 19-1-07 | 1 | expchunk_00202_c686014843 | CHUNK1_19_1_07_Q026 |
| 19-1-08 | 2 | textbook_prose_00114_be4a779fba | CHUNK1_19_1_08_Q013, CHUNK1_19_1_08_Q025 |
| 19-2-02 | 1 | CHK_DOC_CH14_COURSEWARE_P035_001 | CHUNK1_19_2_02_Q026 |
| 19-2-03 | 2 | textbook_prose_00028_a4c7b7c9ae, textbook_prose_00114_be4a779fba | CHUNK1_19_2_03_Q012, CHUNK1_19_2_03_Q016 |
| 19-2-05 | 2 | textbook_prose_00291_440e726030 | CHUNK1_19_2_05_Q018, CHUNK1_19_2_05_Q020 |

## Multi-Point Bindings

| experiment_code | active multi-point items | rationale |
|---|---:|---|
| 19-1-01 | 16 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-02 | 12 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-03 | 11 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-04 | 22 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-05 | 11 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-06 | 13 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-07 | 17 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-1-08 | 4 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-2-01 | 19 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-2-02 | 17 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-2-03 | 24 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-2-04 | 10 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-2-05 | 14 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |
| 19-3-02 | 8 | Multi-point binding retained only where the stem needs combined operations/observations or cross-point comparison. |

## Mobile Fill-Blanks

| experiment_code | active fill blanks | status |
|---|---:|---|
| 19-1-01 | 1 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-1-02 | 2 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-1-03 | 3 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-1-04 | 6 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-1-05 | 4 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-1-06 | 1 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-1-08 | 4 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-2-01 | 4 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-2-02 | 6 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-2-03 | 5 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-2-04 | 3 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-2-05 | 3 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-3-01 | 3 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |
| 19-3-02 | 6 | Short normalized Chinese or compact symbolic answer; no mobile-hostile formula-heavy visible blank remains. |

## Final Validation

Validation script role: inventory/statistics/serialization only; manual evidence reading and repairs drove keep/rewrite/reject decisions.

- UTF-8 JSON parse: pass
- Active count: 443
- Missing effective explanations: 0
- Generic/template option-link diagnostics: 0
- Option-link text mismatches: 0
- Invalid point keys: 0
- Duplicate effective stems: 0
- Visible ASCII formula/ion display in effective displayed fields or option-link text: 0
- Unresolved mobile fill-blank risks: 0
- Rejected item count: 7

Conclusion: chunk 1 has completed the evidence-first global rereview and is ready for downstream import as the current chunk 1 release artifact.
