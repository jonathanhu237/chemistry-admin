# Final Question Bank Quality Spotcheck - 2026-06-15 After User Closeout

## Scope

- Files checked:
  - `chunk_1_release_final_v1.json`
  - `chunk_2_release_final_v1.json`
  - `chunk_3_release_final_v1.json`
  - `chunk_4_release_final_v1.json`
  - `chunk_5_release_final_v1.json`
- OpenSpec change: `full-question-bank-semantic-release-repair`
- Method:
  - Read-only Node queries were used only for inventory, counts, and locating samples.
  - No script repaired or rewrote any question.
  - The sample verdicts below come from reading the effective question text, answer, explanation, option links, bound video points, and source-audit/theory notes.

## OpenSpec Closeout Status

The spec is not complete and must not be archived as done.

- `openspec validate full-question-bank-semantic-release-repair --strict`: passed.
- `openspec instructions apply --change "full-question-bank-semantic-release-repair" --json`: 11 / 121 tasks complete.
- Current status: change package valid, implementation incomplete.
- Release decision: chunks 1-5 are not ready for import or publication.

The reason is not schema validity. The reason is that the change requires per-question manual semantic rereview for all active release questions, and that standard has not been met.

## Current Read-only Inventory

| Chunk | Total records | Active | Rejects | Missing explanations | Template option diagnostics | ASCII digit/electric-charge display hits | ASCII option-link hits | Option text mismatches | Fill blanks | Mobile-risk fill blanks | Multi-point bindings |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 450 | 443 | 7 | 0 | 97 | 56 | 36 | 0 | 68 | 0 | 210 |
| 2 | 450 | 450 | 0 | 0 | 0 | 0 | 0 | 0 | 64 | 8 | 140 |
| 3 | 450 | 450 | 0 | 0 | 0 | 3 | 0 | 0 | 133 | 50 | 174 |
| 4 | 450 | 450 | 0 | 0 | 0 | 0 | 4 | 0 | 126 | 13 | 221 |
| 5 | 510 | 510 | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 0 | 113 |
| **Total** | **2310** | **2303** | **7** | **0** | **97** | **59** | **40** | **0** | **426** | **71** | **858** |

Notes:

- Pure Unicode chemistry notation such as `Cr₂(SO₄)₃`, `CO₃²⁻`, `NH₃·H₂O`, and `CCl₄` was not counted as a formula-display error.
- ASCII issues counted here are student-facing or visible option-link forms such as `CCl4`, `I-`, `Br-`, `K+`, `SO2`, `NH4+`, `CuSO4`, or `NH3·H2O`.
- Some counts are candidate-risk counts, not automatic final judgments. The manual samples confirm that the risk classes are real and unresolved.

## Structure Risk

The five release files are not fully isomorphic:

- Chunk 1 and chunk 2 use `questions` plus `review_id`.
- Chunk 3 uses effective top-level question fields plus `question_id`.
- Chunk 4 uses `review_item_id`.
- Chunk 5 uses `reviewed_questions` plus `review_id`.

This may be acceptable if the importer explicitly supports all variants. If the importer expects one uniform schema, this is an import-readiness risk independent of question quality.

## Manual Sample Verdicts

| Chunk | Question | Point binding | Verdict | Reason |
|---|---|---|---|---|
| 1 | `CHUNK1_19_1_03_Q008` | `candidate-2-fd1f659e` | Fail | Student-facing text still has `CCl4`, `I-`, `Br-`, `K+`; option diagnostics use template wording such as “直接落在点位 / 能回答题干要求”. Point selection is semantically plausible, but presentation and diagnostics are not release-clean. |
| 1 | `CHUNK1_19_1_02_Q028` | `candidate-1-656364cb`, `candidate-2-e6c5ee5d` | Fail | The effective question only asks the weakest halogen `I₂`, with explanation “卤素氧化性顺序中碘最弱”. It does not actually require the Na₂S₂O₃ or H₂S experimental phenomena, and the option links are template-like. This is low-depth recall overbound to two points. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_030` | `candidate-2-795f5a0b` | Fail | Fill blank asks for `SO₂` but accepted answers include `SO2`; answer is formula-heavy for phone input, and explanation is generic: “对应的实验操作或现象内容是...”. Needs rewrite or a logged mobile-safe reason. |
| 2 | `EXP_19_5_01_SEMANTIC_FINAL_030` | `candidate-2-df9b9095` | Fail | Fill blank asks students to write `CuSO₄`; accepted answers include `CuSO4`. This is mainly reagent/formula recall and mobile-fragile, not a strong operation/phenomenon/reasoning item. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q004` | `candidate-2-ea144d3d` | Fail | Asks for the white product `MgO`. It is deterministic but low-depth formula/product recall. Distractor option links all carry the same point key and use generic notes; the correct option note is template text. Source audit properly notes supporting theory dependency, but item quality is below release standard. |
| 3 | `OLD_CHUNK3_EXP_19_6_03_Q011` | `candidate-1-0b2d08c4` | Pass with caution | True/false item “钠与水反应生成氢气和碱性溶液” is source/theory supported and machine-deterministic. It depends on supporting theory for NaOH/H₂ generation, which is recorded. Explanation could be richer, but this sample is not a blocker by itself. |
| 4 | `REV_CH4_EXP_20_1_02_Q001` | `candidate-1-5b3e91cf`, `candidate-2-167c639f`, `candidate-3-ee066dec`, `candidate-4-968503d0`, `candidate-5-2962277d`; secondary `candidate-6-e34dc5e9` | Fail | The question asks which reagent provides `NH₃` ligand, but explanation only says multiple metal salts react with ammonia. Option links B/C/D contain generic diagnostics. It is overbroadly bound to many points and still low-depth reagent recall. |
| 4 | `REV_CH4_EXP_20_1_02_Q012` | `candidate-1-5b3e91cf` | Fail | Deterministic true/false, but still pure reagent-name recognition: “铜盐为 CuCl” false. It may be retainable only with a concrete prerequisite reason; current release metadata marks it publishable without that reason. |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | `candidate-1-376fa2cd` | Fail | Effective stem is generic: “下列哪项判断与实验操作、现象或结论一致”. Option diagnostics are still template-like. The item tests broad recognition more than the actual hydrolysis observation. Several neighboring questions reuse the same generic stem pattern. |
| 5 | `CHK5_SEM_EXP_20_2_08_005` | `candidate-1-376fa2cd` | Fail | The chemistry idea is useful, but it relies on hydrolysis theory: carbonate consumes H⁺ and promotes Cr(III) hydrolysis. Source audit says no theory dependency, which is inaccurate. Option diagnostics are generic. |
| 5 | `CHK5_SEM_EXP_20_3_14_026` | `candidate-1-de6f1130` | Fail | The correct answer about Ni²⁺ and dimethylglyoxime is plausible and theory dependency is recorded, but the stem is generic and option diagnostics are template-like. This is not ready as final polished release text. |

Manual sample result: 10 fail / 1 pass-with-caution.

## Quality Conclusion

The final bank still cannot be imported as a publishable production question bank.

Confirmed blocker classes:

- Residual template option-link diagnostics remain in active questions.
- Student-facing ASCII chemistry notation remains in active effective fields and visible option-link text.
- Formula-heavy fill blanks remain, especially in chunks 2, 3, and 4.
- Some questions are too low-depth: reagent name, formula, color, or title/object recognition without a concrete release reason.
- Some point bindings are overbroad or option-level point links are generic.
- Several records claim `publish_status: publishable` even when the current effective question still violates the spec standard.
- The five JSON files use inconsistent question identifier/array fields.

Positive findings:

- All five release JSON files parse.
- Current read-only scan found zero missing effective explanations.
- Current read-only scan found zero option-link text mismatches where option-link text and effective options are directly comparable.
- Pure Unicode chemical notation was not treated as an error.

## Required Before Release

The current OpenSpec change should remain open. Before declaring chunks 1-5 ready, the team must complete the pending full-bank semantic tasks:

- Manual per-question rereview and log coverage for all 2,303 active questions.
- Zero unresolved template diagnostics.
- Zero unresolved student-facing ASCII digit/electric-charge chemistry notation.
- Zero unlogged or unreworked mobile-risk formula fill blanks.
- Concrete retained reasons for any low-depth recognition item.
- Verified point bindings for all 858 multi-point items.
- A final all-chunk QA report referencing the earlier 2026-06-15 blocker inventories and this current spotcheck.
