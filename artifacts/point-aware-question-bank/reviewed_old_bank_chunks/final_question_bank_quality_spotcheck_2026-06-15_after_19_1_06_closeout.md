# Final Question Bank Quality Spotcheck - 2026-06-15 After 19-1-06 Closeout

## Scope

- Files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- Active release questions: 2,303.
- Rejected records: 7, all in chunk 1.
- Method: scripts were used only for JSON parsing, inventory counts, and locating candidate records. The import-readiness judgments below come from manual reading of representative effective question fields, answers, explanations, option links, point keys, and stored source-audit context.

## OpenSpec Closeout Status

- Change: `full-question-bank-semantic-release-repair`.
- Schema: `spec-driven`.
- `openspec validate full-question-bank-semantic-release-repair --strict`: passed.
- `openspec instructions apply --change full-question-bank-semantic-release-repair --json`: 15 / 141 tasks complete, 126 remaining.
- Last completed batch: task `3.6 Manually rereview and repair 19-1-06`.
- Next unfinished batch: task `3.7 Manually rereview and repair 19-1-07`.
- Closeout decision: stage closeout only. The spec is structurally valid, but it is not complete, not archive-ready, and cannot be used as release approval.

## Current Read-Only Inventory

These are candidate-risk counts, not final semantic decisions. They are high enough to block import until manually resolved or explicitly logged per question.

| Chunk | Active | Reject | Generic expl | Template diag | ASCII displayed | ASCII option-link | Fill blanks | Formula/mobile-risk fill | Multi-point |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 443 | 7 | 157 | 76 | 42 | 28 | 59 | 9 | 205 |
| 2 | 450 | 0 | 157 | 0 | 7 | 0 | 64 | 15 | 140 |
| 3 | 450 | 0 | 191 | 163 | 3 | 0 | 133 | 60 | 174 |
| 4 | 450 | 0 | 175 | 216 | 12 | 3 | 126 | 16 | 221 |
| 5 | 510 | 0 | 158 | 322 | 0 | 0 | 35 | 0 | 113 |

Positive signals:

- All five JSON files parse.
- Missing effective explanations are currently zero.
- Some repaired items are now genuinely publishable at the question level.

Blocking signals:

- Generic explanations still appear across all five chunks.
- Template option-link diagnostics remain large-scale in chunks 1, 3, 4, and 5.
- Visible ASCII chemistry remains in active effective fields, especially chunk 1.
- Formula-heavy or alias-heavy fill blanks remain in chunks 1-4.
- Multi-point bindings are common and still require positive semantic proof per item.

## Manual Spotcheck Samples

| Sample | Chunk | Experiment | Point binding | Judgment |
|---|---:|---|---|---|
| `CHUNK1_19_1_07_Q028` | 1 | `19-1-07 氯含氧酸盐的氧化性` | primary `candidate-2-1046fab6`, `candidate-4-391ca911` | Fail. The idea is source-supportable, but the effective stem/options still show `KClO3` and `K+`; the explanation is generic; option links partly clean the formula while the visible option text does not. Not import-ready. |
| `CHUNK1_19_1_01_Q001` | 1 | `19-1-01 氯、溴、碘的置换次序` | primary `candidate-1-034a8366` | Question-level pass, metadata risk. The student-facing stem, answer, explanation, and option links are good, but `source_audit.reviewer_note` incorrectly discusses KClO₃ from `19-1-06`, and `semantic_final_review.low_quality_reason_if_retained` discusses an unrelated Na₂S₂O₃ fill blank. Needs audit cleanup before final QA. |
| `EXP_19_3_03_SEMANTIC_FINAL_030` | 2 | `19-3-03 SO₃²⁻ 的检出` | primary `candidate-2-795f5a0b` | Fail. Fill blank accepts `SO2`, `SO₂`, and `二氧化硫`; that is deterministic but mobile-hostile and mixes visible formula aliases. Explanation is also generic. Rewrite to single choice or Chinese-only visible answer with hidden aliases logged. |
| `EXP_19_3_03_SEMANTIC_FINAL_001` | 2 | `19-3-03 SO₃²⁻ 的检出` | primary `candidate-1-26a8e36e`, `candidate-2-795f5a0b` | Borderline pass. The question asks about removing SO₄²⁻ interference before SO₃²⁻ detection and the multi-point binding is semantically real. Option diagnostics are verbose and still partly scaffold-like, so polish is recommended. |
| `OLD_CHUNK3_EXP_19_8_01_Q001` | 3 | `19-8-01 Pb(OH)₂ 的生成与性质` | primary `candidate-1-356d797d` | Fail. It is low-depth reagent recall (`NaOH`), the correct option diagnostic remains template text, and distractor option links keep the same point key even when they are adjacent-experiment distractors. Needs rewrite or concrete prerequisite-retention reason plus corrected option links. |
| `OLD_CHUNK3_EXP_19_6_02_Q001` | 3 | `19-6-02 金属镁燃烧` | primary `candidate-1-a3329021`, `candidate-2-ea144d3d` | Pass. The stem genuinely combines operation and observation: remove oxide film, ignite magnesium, observe burning and product. Explanation and distractors are concrete; multi-point binding is justified. |
| `REV_CH4_EXP_20_1_02_Q001` | 4 | `20-1-02 氨合物` | primary five metal-ammonia points; secondary `candidate-6-e34dc5e9` | Fail. The question only asks which reagent supplies NH₃ ligand, but the binding spans five primary points plus one secondary point. Explanation is thin and two option diagnostics are still template-level. |
| `REV_CH4_EXP_20_1_02_Q021` | 4 | `20-1-02 氨合物` | primary five metal-ammonia points; secondary `candidate-6-e34dc5e9` | Fail. Fill blank accepts `氨水`, `NH3·H2O`, and `NH₃·H₂O`; visible ASCII alias and symbolic formula forms create mobile/input risk. Explanation is generic and point binding is broader than the stem. |
| `CHK5_SEM_EXP_20_2_08_001` | 5 | `20-2-08 铬(III)盐的水解` | primary `candidate-1-376fa2cd` | Fail. The answer is supportable from the Cr₂(SO₄)₃ / Na₂CO₃ hydrolysis experiment, but every option-link diagnostic remains template-level. The stem is also generic enough that option diagnostics carry too much of the quality burden. |
| `CHK5_SEM_EXP_20_3_14_026` | 5 | `20-3-14 小设计实验` | primary `candidate-1-de6f1130`; theory cited | Fail / theory-dependent. Ni²⁺ + 丁二酮肟 red precipitate is supportable only by linking the design task to supporting theory. The explanation is too short for that dependency, and option diagnostics remain template-level. |

Manual sample result:

- Pass: 2
- Borderline / polish recommended: 1
- Fail: 7

## Release Decision

Chunks 1-5 are not ready for direct import or publication.

The current files are structurally valid and have no missing explanations, but final quality is still below the acceptance bar. The most important blockers are visible ASCII formulas, generic explanations, template option-link diagnostics, mobile-hostile formula fill blanks, low-depth recognition items without concrete retained reasons, broad inherited multi-point bindings, and inconsistent audit metadata.

## Required Next Action

Continue the OpenSpec task order instead of archiving:

1. Finish task `3.7` for `19-1-07`, starting with `CHUNK1_19_1_07_Q028`, `Q029`, and the remaining fill/generic-risk records in that experiment.
2. Keep using scripts only for inventory and validation; keep/rewrite/reject, point binding, explanations, and option links must remain manual semantic decisions.
3. After every remaining experiment batch is repaired, rerun the full validation gates and produce a final all-chunk QA report only when blocker counts are zero or explicitly logged as retained non-displayed grading tolerance.
