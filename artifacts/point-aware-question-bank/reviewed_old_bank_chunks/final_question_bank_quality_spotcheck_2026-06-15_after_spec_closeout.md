# Final Question Bank Quality Spotcheck - 2026-06-15 After Spec Closeout

## Scope

- Files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- Active effective questions counted: 2,303.
- OpenSpec change: `full-question-bank-semantic-release-repair`.
- OpenSpec apply progress at closeout: 8 / 111 tasks complete.
- This spotcheck is not a replacement for the required full manual semantic rereview. Scripts were used only for parsing, counting, and locating risk candidates.

## Stage Closeout Result

The previous spec stage is closed as a valid but incomplete OpenSpec change. It is not archive-ready and not release-complete.

- `openspec validate full-question-bank-semantic-release-repair --strict` passed.
- `stage_closeout_2026-06-15.md` now reflects the current 8 / 111 task count.
- The task list now treats spotcheck-discovered risk classes as full release blockers: missing explanations, ASCII formula display, English or generic option-link diagnostics, formula-heavy mobile fill blanks, accepted-answer alias visibility, and low-depth recognition items.

## Gate Scan Results

The scan below is a risk inventory, not a semantic decision engine.

| Chunk | Active | Missing explanations | Generic explanations | ASCII formula display risk | English option-link diagnostics | Generic option-link diagnostics | Scaffold wording | Fill-blank mobile risk candidates |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| chunk 1 | 443 | 19 | 0 | 61 | 0 | 246 | 0 | 4 |
| chunk 2 | 450 | 0 | 18 | 0 | 0 | 271 | 0 | 9 |
| chunk 3 | 450 | 0 | 4 | 0 | 0 | 163 | 0 | 50 |
| chunk 4 | 450 | 0 | 5 | 0 | 6 | 214 | 0 | 15 |
| chunk 5 | 510 | 0 | 0 | 0 | 0 | 322 | 0 | 0 |
| **Total** | **2,303** | **19** | **27** | **61** | **6** | **1,216** | **0** | **78** |

## Manual Spotcheck Samples

| Sample | Point binding checked | Manual quality conclusion |
|---|---|---|
| chunk 1 `CHUNK1_19_3_02_Q003` | primary `candidate-1-ea27f7fc` = SO₂ + 酸性 KMnO₄；secondary none | Answer `还原性` is supported by the canonical SO₂ + acidified KMnO₄ operation and the point binding is now semantically right, but `explanation` is still null. This is a hard release blocker. |
| chunk 1 `CHUNK1_19_1_01_Q010` | primary `candidate-1-034a8366` = 氯水 + KBr 溶液 + CCl₄；secondary none | The chemistry is source-supported, but the displayed stem/options/option-links still contain ASCII `Cl2`, `Br2`, `CCl4`; option diagnostics are also template-like. Not import-ready under the current formula/diagnostic standard. |
| chunk 2 `EXP_19_3_03_SEMANTIC_FINAL_001` | primary `candidate-1-26a8e36e` = 除去 SO₄²⁻ 干扰；primary `candidate-2-795f5a0b` = 验证 SO₃²⁻；secondary none | The question is semantically valid and genuinely multi-point, but option-link notes still use generic scaffold wording such as “直接支撑题干所问” and do not fully read like final student-facing diagnostics. Needs option-link polish before release. |
| chunk 2 `EXP_19_3_03_SEMANTIC_FINAL_030` | primary `candidate-2-795f5a0b` = 验证 SO₃²⁻；secondary none | The answer is deterministic if `二氧化硫` is accepted, but the fill blank also exposes `SO2`/`SO₂` aliases and has a generic explanation. This is a mobile-input and accepted-answer-display risk unless rewritten or explicitly logged as hidden grading tolerance. |
| chunk 3 `OLD_CHUNK3_EXP_19_6_02_Q003` | primary `candidate-2-ea144d3d` = 观察镁燃烧及生成物；secondary none | The answer `发出耀眼白光` is supported, but the item is low-depth observation recall. Explanation is too terse and the correct option-link says only “直接对应本题考查的实验操作、现象或结论”. Keep only with a retained low-depth reason and evidence-specific diagnostics. |
| chunk 3 `OLD_CHUNK3_EXP_19_6_03_Q027` | primary `candidate-5-b36777e1` = 金属钙与水反应；secondary none | The answer `Ca(OH)₂/氢氧化钙` relies on supporting theory for product identity. As a fill blank, formula input is phone-hostile; should be rewritten to single choice or logged with a concrete retained-risk reason. |
| chunk 4 `20-1-03` experiment index 28 | primary `candidate-10-441a164c` = Co[Hg(SCN)₄]；secondary `candidate-8-2db27325` = Hg(NO₃)₂ + KSCN | The correct answer is source/theory-supported, but option A diagnostic is English and uses ASCII `Zn[Hg(SCN)4]`. This is a hard visible-metadata blocker. |
| chunk 4 `20-1-05` experiment index 18 | primary `candidate-1-5a316034` = CuCl₂ + NaSO₃ / Na₂SO₃；secondary `candidate-2-0a590e08` = 生成 CuCl 沉淀 | The answer `作还原剂，使 Cu(II) 转化为 Cu(I)` is reasonable, with theory dependency for the redox conclusion. Option D diagnostic is English and uses ASCII `Na2SO3`; visible option-link quality fails. |
| chunk 5 `CHK5_SEM_EXP_20_2_08_001` | primary `candidate-1-376fa2cd` = Cr₂(SO₄)₃ + Na₂CO₃；secondary none | The question and answer are source-supported, but option-link diagnostics remain generic: “混淆了本实验的试剂、操作、现象或结论” / “直接对应本题考查…”. It needs evidence-specific diagnostics before final import. |
| chunk 5 `CHK5_SEM_EXP_20_3_02_001` | primary `candidate-1-6c3245f9` = CrO₄²⁻；secondary none | The answer is supported by the experiment object list, but the item is low-depth recognition and its explanation is generic. It can remain only if the manual log records why this prerequisite recognition item is necessary. |

## Release Decision

Chunks 1-5 are **not** ready for import or publication.

Blocking reasons:

- chunk 1 still has missing explanations in active final questions.
- chunk 1 still has visible ASCII chemistry formulas in final displayed text.
- chunk 4 still has English and ASCII option-link diagnostics.
- chunks 2, 3, and 4 still contain formula-heavy or alias-heavy fill blanks that are risky on mobile.
- all chunks still show many generic option-link diagnostics; manual samples confirm this is not just a scan artifact.
- chunk 3 and chunk 5 still contain low-depth recognition or observation items without sufficient retained-quality reasons in the manual logs.
- the full per-question semantic rereview required by OpenSpec has not been completed.

## Next Repair Order

1. Finish chunk 1 `19-3-02` by adding concrete explanations, rechecking point bindings, and cleaning option-link diagnostics.
2. Normalize chunk 1 student-facing ASCII chemistry formulas after semantic confirmation.
3. Repair chunk 4 English/ASCII option-link diagnostics, especially `20-1-03`, `20-1-05`, and `20-2-02`.
4. Rewrite or explicitly log mobile-risk formula fill blanks in chunks 2, 3, and 4.
5. Continue full manual rereview experiment by experiment until every active question appears exactly once in a manual log.

