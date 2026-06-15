# Final Question Bank Quality Spotcheck - Spec Closeout Resample

Date: 2026-06-15

Scope:
- Release files: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`
- OpenSpec change: `E:/chemistry-exam/openspec/changes/full-question-bank-semantic-release-repair`
- Method: scripts were used only for JSON navigation, inventory counts, and validation. The 10 sampled question decisions below are manual semantic judgments from reading the effective question, point binding, canonical experiment evidence, and option-link/audit metadata.

## OpenSpec Closeout Status

- `openspec validate full-question-bank-semantic-release-repair --strict`: passed.
- `openspec instructions apply --change full-question-bank-semantic-release-repair --json`: 15/153 tasks complete, 138 remaining.
- Artifact status is structurally complete, but the implementation is not release-complete and should not be archived as finished.
- Import readiness remains blocked until every active question is manually rereviewed and final validation tasks 8.1-8.24 pass.

## Read-Only Inventory Scan

These counts are candidate blockers for navigation and validation only. They do not replace manual semantic review.

| Chunk | Active | Missing exp. | Generic exp. candidates | Template diagnostic candidates | ASCII display candidates | ASCII option-link candidates | Fill blank | Formula/mobile-risk fill | Multi-point candidates | Option-link text mismatch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 443 | 0 | 24 | 76 | 38 | 17 | 57 | 2 | 205 | 2 |
| 2 | 450 | 0 | 46 | 0 | 4 | 0 | 64 | 8 | 140 | 0 |
| 3 | 450 | 0 | 56 | 163 | 0 | 0 | 133 | 50 | 174 | 0 |
| 4 | 450 | 0 | 106 | 216 | 2 | 3 | 126 | 14 | 221 | 0 |
| 5 | 510 | 0 | 48 | 322 | 0 | 0 | 35 | 0 | 113 | 0 |

Inventory conclusion: all five chunks still have unresolved release-risk classes. The current final bank cannot be approved from `publish_status` or prior reports alone.

## Manual Resample Result

Manual sample size: 10 questions, covering all five chunks.

Pass: 3  
Fail/blocking: 7

### Sample Decisions

| Chunk | Question ID | Experiment | Effective type | Bound point keys | Manual result | Reason |
|---|---|---|---|---|---|---|
| 1 | `CHUNK1_19_1_07_Q009` | 19-1-07 氯含氧酸盐的氧化性 | single_choice | primary: `candidate-1-02621b6d`, `candidate-2-1046fab6` | Fail | Effective stem asks about NaClO + 品红漂白, but the 19-1-07 canonical point is NaClO/KClO₃/KClO₄ + KI-淀粉 and H₂SO₄ acidification. Point binding is overbroad and audit note contradicts the effective item by mentioning a different CCl₄ repair. |
| 1 | `CHUNK1_19_1_07_Q028` | 19-1-07 氯含氧酸盐的氧化性 | single_choice | primary: `candidate-2-1046fab6`, `candidate-4-391ca911` | Pass | Effective stem, answer, explanation, and option links now match the KClO₃/KI-淀粉 neutral-to-H₂SO₄ acidification comparison. Canonical evidence is sufficient. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_001` | 19-3-03 SO₃²⁻ 的检出 | single_choice | primary: `candidate-1-26a8e36e`, `candidate-2-795f5a0b` | Pass | Asks why SO₄²⁻ interference is removed before SO₃²⁻ detection. Both point keys are used: interference-removal design and target verification. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_030` | 19-3-03 SO₃²⁻ 的检出 | fill_blank | primary: `candidate-2-795f5a0b` | Fail | Formula-heavy/mobile-risk fill blank accepts `SO2`, `SO₂`, and `二氧化硫`; explanation is generic: “对应的实验操作或现象内容是…”. Should be rewritten to deterministic single choice or logged with hidden aliases only. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q001` | 19-6-02 金属镁燃烧 | single_choice | primary: `candidate-1-a3329021`, `candidate-2-ea144d3d` | Pass | The question combines the operation chain: remove Mg oxide film, ignite, and observe combustion/product. Multi-point binding is semantically justified. |
| 3 | `OLD_CHUNK3_EXP_19_8_01_Q001` | 19-8-01 Pb(OH)₂ 的生成与性质 | single_choice | primary: `candidate-1-356d797d` | Fail | Low-depth reagent-name recall: “向 Pb(NO₃)₂ 溶液中滴加的是哪种溶液？” Correct option diagnostic is still template-like, and distractor option links are incorrectly tied to the same point. |
| 4 | `REV_CH4_EXP_20_1_02_Q001` | 20-1-02 氨合物 | single_choice | primary: `candidate-1` through `candidate-5`; secondary: `candidate-6` | Fail | Stem only asks which reagent provides NH₃ ligand, but point binding covers five metal-salt reactions plus observation. Explanation is generic and option diagnostics still contain template language. |
| 4 | `REV_CH4_EXP_20_1_02_Q021` | 20-1-02 氨合物 | fill_blank | primary: `candidate-1` through `candidate-5`; secondary: `candidate-6` | Fail | Mobile-risk fill blank with visible symbolic aliases `NH3·H2O`/`NH₃·H₂O`; explanation is generic. Point binding is broader than the final answer, which is only “氨水/NH₃·H₂O”. |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | 20-2-08 铬(III)盐的水解 | single_choice | primary: `candidate-1-376fa2cd` | Fail | Canonical support exists for Cr₂(SO₄)₃ + Na₂CO₃, but the stem is generic (“哪项判断与实验操作、现象或结论一致”) and option diagnostics remain template-level. |
| 5 | `CHK5_SEM_EXP_20_3_14_026` | 20-3-14 小设计实验 | single_choice | primary: `candidate-1-de6f1130` | Fail | Uses supporting theory from Ni²⁺/丁二酮肟 identification, but the bound point is a full design for Fe³⁺、Co²⁺、Ni²⁺. The effective item tests only a Ni²⁺ partial fact, while the diagnostics are still template-level. |

## Canonical Evidence Used

- 19-1-07: canonical procedure adds NaClO, KClO₃, and KClO₄ solutions separately to KI-淀粉, observes, then acidifies non-reacting tubes with H₂SO₄ and compares oxidizing ability.
- 19-3-03: canonical/video points require removing SO₄²⁻ interference and verifying SO₃²⁻.
- 19-6-02: canonical procedure says to remove the surface oxide layer from a Mg strip, ignite it, and observe.
- 19-8-01: point sequence is Pb(NO₃)₂ + NaOH, then Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH.
- 20-1-02: canonical procedure adds NH₃·H₂O to CuSO₄, AgNO₃, ZnSO₄, CdSO₄, and HgCl₂, observes precipitate formation/dissolution, and then tests stability/designs CuSO₄ complex evidence.
- 20-2-08: canonical procedure is Cr₂(SO₄)₃ + Na₂CO₃ for chromium(III) salt hydrolysis.
- 20-3-14: canonical point asks for a design to identify Fe³⁺, Co²⁺, and Ni²⁺ separately. The Ni²⁺/丁二酮肟 red precipitate judgment depends on the adjacent/supporting identification theory, not only the small-design sentence.

## Release Decision

Not import-ready.

The previous spec can be considered structurally closed/validated, but not implementation-complete. The final bank still contains blocking quality issues in all five chunks: unsupported or cross-experiment questions, formula/mobile-hostile fill blanks, low-depth recall items, overbroad point bindings, generic explanations, template option diagnostics, and audit metadata contradictions.

Next execution should resume the manual semantic repair tasks rather than archive the change.
