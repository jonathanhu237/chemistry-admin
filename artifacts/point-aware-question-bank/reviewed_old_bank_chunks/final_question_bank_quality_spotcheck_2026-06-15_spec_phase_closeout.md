# Final Question Bank Quality Spotcheck - Spec Phase Closeout

Date: 2026-06-15

Scope:

- `chunk_1_release_final_v1.json`
- `chunk_2_release_final_v1.json`
- `chunk_3_release_final_v1.json`
- `chunk_4_release_final_v1.json`
- `chunk_5_release_final_v1.json`

## Verdict

Not ready for import.

The current final release bank still contains publish-blocking risks. Some repaired samples are now good enough, but the overall bank still has visible formula formatting issues, template option-link diagnostics, mobile-hostile fill blanks, weak low-depth retained questions, and unverified broad multi-point bindings.

## Read-Only Risk Scan

This scan was used only for inventory and validation. It did not decide keep/rewrite/reject or generate fixes.

| Chunk | Active | Reject | Generic explanation hits | Template diagnostic hits | Visible ASCII digit formula hits | ASCII formula in option links | Fill/mobile-risk hits | ASCII accepted aliases | Multi-point items |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| chunk 1 | 443 | 7 | 57 | 102 | 52 | 32 | 4 | 7 | 209 |
| chunk 2 | 450 | 0 | 0 | 0 | 15 | 12 | 8 | 10 | 140 |
| chunk 3 | 450 | 0 | 0 | 163 | 104 | 29 | 25 | 16 | 174 |
| chunk 4 | 450 | 0 | 0 | 216 | 22 | 23 | 13 | 8 | 221 |
| chunk 5 | 510 | 0 | 0 | 322 | 32 | 23 | 0 | 0 | 113 |
| Total | 2303 | 7 | 57 | 803 | 225 | 119 | 50 | 41 | 857 |

These are candidate-risk counts, not final semantic decisions. They are high enough that the bank cannot be approved without the remaining manual rereview.

## Manual Spotcheck Samples

| Sample | Chunk | Experiment | Point binding | Manual judgment |
|---|---:|---|---|---|
| `CHUNK1_19_1_06_Q012` | 1 | `19-1-06 氯酸盐的氧化性` | primary: `candidate-4-7bed40a2`, `candidate-5-9ebfbe89` | Pass. The stem asks why H2SO4 is preferred over HCl/HNO3 for the KClO3/KI/CCl4 acidification system. Canonical text supports acidification with sulfuric acid and the point set genuinely covers acidification plus acid choice. Explanation and option links are concrete. |
| `CHUNK1_19_1_07_Q028` | 1 | `19-1-07 氯含氧酸盐的氧化性` | primary: `candidate-2-1046fab6`, `candidate-4-391ca911` | Fail. The answer is semantically supportable, but the final stem still contains `KClO3`, the explanation is generic, and option-link diagnostics are templated. Not import-ready. |
| `EXP_19_3_03_SEMANTIC_FINAL_001` | 2 | `19-3-03 SO3^2- 的检出` | primary: `candidate-1-26a8e36e`, `candidate-2-795f5a0b` | Borderline pass. The SO4^2- interference rationale is supported by the experiment point pair, and the multi-point binding is real. However, the option-link diagnostics are verbose and still partly scaffold-like; polish is recommended before release. |
| `EXP_19_3_03_SEMANTIC_FINAL_030` | 2 | `19-3-03 SO3^2- 的检出` | primary: `candidate-2-795f5a0b` | Fail. The fill blank expects `SO2/SO₂/二氧化硫`; this is deterministic but fragile on mobile, and the explanation only says the corresponding content is the answer. Should be rewritten to single choice or use a short Chinese-only answer with hidden aliases logged. |
| `OLD_CHUNK3_EXP_19_6_02_Q001` | 3 | `19-6-02 金属镁燃烧` | primary: `candidate-1-a3329021`, `candidate-2-ea144d3d` | Pass. The question asks for the operation chain: remove oxide film, ignite, observe burning and product. Canonical text and both points support it, and the multi-point binding is justified. |
| `OLD_CHUNK3_EXP_19_8_01_Q001` | 3 | `19-8-01 Pb(OH)2 的生成与性质` | primary: `candidate-1-356d797d` | Fail. The answer `NaOH` is likely source-supported, but the item is low-depth reagent recall. Distractor option links point to the same experiment point even when they are unrelated, and one diagnostic remains templated. Needs rewrite or concrete retention reason. |
| `REV_CH4_EXP_20_1_02_Q001` | 4 | `20-1-02 氨合物` | primary: `candidate-1-5b3e91cf` through `candidate-5-2962277d`; secondary: `candidate-6-e34dc5e9` | Fail. The stem only asks which reagent provides NH3 ligand, but the primary binding spans five metal-salt point keys. Explanation is generic, and option diagnostics include template text. Needs narrower point binding and deeper stem. |
| `REV_CH4_EXP_20_1_02_Q021` | 4 | `20-1-02 氨合物` | primary: `candidate-1-5b3e91cf` through `candidate-5-2962277d`; secondary: `candidate-6-e34dc5e9` | Fail. Fill blank accepts `氨水`, `NH3·H2O`, and `NH₃·H₂O`; symbolic aliases create mobile/input risk. The broad point binding also exceeds the actual stem. |
| `CHK5_SEM_EXP_20_2_08_001` | 5 | `20-2-08 铬(III)盐的水解` | primary: `candidate-1-376fa2cd` | Fail. Source support exists for Cr2(SO4)3 + Na2CO3, but the stem is generic, the correct answer is low-depth reagent recognition, and option-link diagnostics are templated. |
| `CHK5_SEM_EXP_20_3_14_026` | 5 | `20-3-14 小设计实验` | primary: `candidate-1-de6f1130`; supporting theory cited | Fail. The Ni2+ + 丁二酮肟 red precipitate answer is supportable, with theory dependency correctly noted, but the stem remains generic and option-link diagnostics are templated. It needs a concrete design-experiment stem and non-template option diagnostics. |

Manual sample result:

- Pass: 2
- Borderline pass / needs polish: 1
- Fail: 7

## Main Blockers

1. Template option-link diagnostics remain common, especially in chunks 3-5.
2. Visible formula formatting is still inconsistent; several final fields show ASCII digit formulas such as `KClO3`, `SO2`, `Pb(OH)2`, or `NH3·H2O`.
3. Several fill blanks still rely on symbolic formulas or multiple aliases that are fragile for phone input.
4. Some low-depth items only ask for reagent names or isolated formula recall.
5. Some multi-point bindings are broad inherited point sets rather than points required by the actual final stem.
6. Some explanations remain generic and do not name the actual reagent, operation, phenomenon, or conclusion.

## Closeout Decision

The previous spec can be closed only as a planning/specification phase. The implementation is not complete, and the final question bank cannot be imported or published yet.

Continue the OpenSpec task order from the unfinished `19-1-06` batch, then proceed through chunks 2-5. A real release approval should require a later report showing zero unresolved blockers and a clean manual rereview log for every active question.

