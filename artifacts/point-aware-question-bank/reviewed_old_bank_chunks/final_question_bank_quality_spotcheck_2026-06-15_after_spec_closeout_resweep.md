# Final Question Bank Quality Spotcheck - 2026-06-15 After Spec Closeout Resweep

## Scope

- Files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- Active release questions: 2,303.
- Raw records: 2,310, including 7 rejected records in chunk 1.
- Method: scripts were used only for JSON parsing, inventory, and risk counting. Sample quality judgments below come from manual reading of the effective question, point binding, release record, video points, and canonical/source previews available in `formal_experiment_point_inventory.json`.

## OpenSpec Closeout Status

- Change: `full-question-bank-semantic-release-repair`.
- `openspec validate full-question-bank-semantic-release-repair --strict`: passed.
- `openspec instructions apply --change full-question-bank-semantic-release-repair --json`: 11 / 117 tasks complete.
- Status: stage-closeout only. The change is valid but not complete, not archived, and not a release approval.

## Release Decision

Chunks 1-5 are not ready for direct import/publication.

The bank is structurally parseable and no active effective question is missing an explanation, but the final release artifacts still contain release blockers: residual template option-link diagnostics, visible ASCII chemistry formulas, formula-heavy or alias-heavy fill blanks, low-depth recognition items without per-question retained-risk evidence, and some weak traceability between broad point bindings and narrow question semantics.

## Read-Only Inventory

| Chunk | Active | Rejects | Missing explanations | Template diagnostics | ASCII displayed formulas | ASCII option-link formulas | Fill blanks | Mobile-risk fill blanks | ASCII accepted aliases | Multi-point items |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 443 | 7 | 0 | 195 | 54 | 34 | 68 | 7 | 0 | 214 |
| 2 | 450 | 0 | 0 | 0 | 7 | 0 | 64 | 14 | 7 | 140 |
| 3 | 450 | 0 | 0 | 163 | 3 | 0 | 133 | 28 | 0 | 174 |
| 4 | 450 | 0 | 0 | 216 | 12 | 4 | 126 | 32 | 12 | 221 |
| 5 | 510 | 0 | 0 | 322 | 0 | 0 | 35 | 7 | 0 | 113 |
| Total | 2,303 | 7 | 0 | 896 | 76 | 38 | 426 | 88 | 19 | 862 |

Notes:

- `Template diagnostics` counts active questions with at least one option-link text or diagnostic matching scaffold-style wording such as `该选项直接对应...`, `该选项混淆...`, `属于其他实验或无关情境`, `直接落在点位`, or `能回答题干要求`.
- `ASCII displayed formulas` counts active questions whose effective displayed fields still contain formula-like ASCII tokens, for example `CCl4`, `KClO3`, `H2SO4`, `SO2`, `NH3·H2O`, `CuSO4`.
- `Mobile-risk fill blanks` is a candidate-risk inventory, not a final rejection list. Each item still needs manual rereview, but symbolic formulas, multi-alias answers, equation fragments, and formula/ion notation are not safe by default for phone input.

## Manual Samples

### 1. PASS After Repair: `CHUNK1_19_1_01_Q010`

- Chunk/experiment: chunk 1, `19-1-01 氯、溴、碘的置换次序`
- Effective type: single choice
- Point: `candidate-1-034a8366` / `氯水 + KBr 溶液 + CCl₄`
- Effective stem: `要用本实验点位证明 Cl₂ 的氧化性强于 Br₂，下列哪组体系最合适？`
- Answer: A, `氯水 + KBr 溶液 + CCl₄`
- Canonical support: inventory source preview for page 139 lists KBr, KI, CCl₄, chlorine water, bromine water and asks students to design tube experiments for the chlorine/bromine/iodine displacement order.
- Judgment: import-quality sample. It tests point discrimination, has Unicode formulas, deterministic answer, concrete explanation, and option links that distinguish the adjacent `溴水 + KI + CCl₄` point.

### 2. FAIL: `CHUNK1_19_1_02_Q021`

- Chunk/experiment: chunk 1, `19-1-02 氯水、溴水、碘水氧化性差异的比较`
- Effective type: single choice
- Point: `candidate-1-656364cb` / `氯水、溴水、碘水分别与 Na₂S₂O₃ 溶液反应`
- Effective stem: asks which reducing reagent is used with chlorine water, bromine water, and iodine water.
- Answer: A, `Na₂S₂O₃`
- Canonical support: page 139 source preview states that chlorine water, bromine water, and iodine water are each treated with `Na₂S₂O₃` solution and saturated hydrogen sulfide water, then phenomena are observed.
- Judgment: evidence-supported but not release-quality. It is a low-depth reagent-name recognition item, explanation is generic, and the correct option-link still says `直接落在点位...能回答题干要求`. It should be rewritten to ask about the differentiated phenomena, for example iodine water fading without sulfur precipitate versus chlorine/bromine systems producing sulfur turbidity.

### 3. FAIL: `EXP_19_3_03_SEMANTIC_FINAL_030`

- Chunk/experiment: chunk 2, `19-3-03 SO₃²⁻ 的检出`
- Effective type: fill blank
- Point: `candidate-2-795f5a0b` / `验证样品中 SO₃²⁻ 的存在`
- Effective stem: `酸化 SO₃²⁻ 可放出____用于后续性质验证。`
- Accepted answers: `SO2`, `SO₂`, `二氧化硫`
- Canonical support: source previews for experiment 19-3 cover SO₃²⁻/SO₄²⁻/SO₂ theory and SO₂ properties; the sample is chemically supported.
- Judgment: not mobile-safe enough for final release. The visible effective answer set mixes ASCII and Unicode formulas plus Chinese text, and the explanation is generic. This should be rewritten to deterministic single choice or changed to Chinese-only short answer if the platform clearly hides formula aliases from students.

### 4. FAIL: `OLD_CHUNK3_EXP_19_8_01_Q001`

- Chunk/experiment: chunk 3, `19-8-01 Pb(OH)₂ 的生成与性质`
- Effective type: single choice
- Point: `candidate-1-356d797d` / `Pb(NO₃)₂ + NaOH`
- Effective stem: asks which solution is added to `Pb(NO₃)₂` to generate `Pb(OH)₂`.
- Answer: C, `NaOH`
- Canonical support: point title and source audit support the operation; however the stored canonical preview for `expchunk_00295_b30319fd2c` truncates before the Pb subsection, so this sample needs full canonical text/page-image confirmation during final rereview.
- Judgment: not release-quality as-is. The correct option-link diagnostic remains generic (`该选项直接对应本题考查的实验操作、现象或结论`), and the item only asks for a reagent name. It should either be reauthored around the acid/base behavior of the generated hydroxide or logged as a deliberate prerequisite item with concrete retained-risk reason.

### 5. FAIL: `REV_CH4_EXP_20_1_02_Q021`

- Chunk/experiment: chunk 4, `20-1-02 氨合物`
- Effective type: fill blank
- Points: primary `candidate-1-5b3e91cf` through `candidate-5-2962277d`, secondary `candidate-6-e34dc5e9`
- Effective stem: asks what is added as the NH₃ source when forming ammine complexes.
- Accepted answers: `氨水`, `NH3·H2O`, `NH₃·H₂O`
- Canonical support: page 162 preview states that CuSO₄, AgNO₃, ZnSO₄, CdSO₄, and HgCl₂ solutions are treated with `NH₃·H₂O`, observing precipitate formation and dissolution.
- Judgment: evidence-supported but not release-quality. It is a broad multi-point reagent-name fill blank with ASCII formula alias. For mobile release it should become single choice about the shared role of ammonia water or retain only a Chinese short answer while logging formula aliases as hidden deterministic grading synonyms.

### 6. FAIL: `CHK5_SEM_EXP_20_2_08_001`

- Chunk/experiment: chunk 5, `20-2-08 铬(III)盐的水解`
- Effective type: single choice
- Point: `candidate-1-376fa2cd` / `Cr₂(SO₄)₃ + Na₂CO₃`
- Effective answer: B, `Cr₂(SO₄)₃ 是本实验中用于观察铬(III)盐水解的铬盐`
- Canonical support: page 165 preview says chromium(III) salt hydrolysis is tested by adding `Na₂CO₃` solution to `Cr₂(SO₄)₃` solution and observing phenomena.
- Judgment: content is basically supportable, but not final-clean. All option-link diagnostics are scaffold templates (`该选项混淆...`, `该选项直接对应...`, `属于其他实验...`). This can likely be kept after reauthoring diagnostics and reviewing whether the stem is too generic.

### 7. FAIL / Theory-Dependent: `CHK5_SEM_EXP_20_3_14_026`

- Chunk/experiment: chunk 5, `20-3-14 小设计实验`
- Effective type: single choice
- Point: `candidate-1-de6f1130` / `已知溶液中含 Fe³⁺、Co²⁺、Ni²⁺，设计方案分别检出三种离子`
- Effective answer: B, `Ni²⁺ 与丁二酮肟的阳性现象是生成红色沉淀。`
- Canonical support: page 167 preview for the preceding metal-ion identification section describes adding ammonia water and dimethylglyoxime to NiSO₄ and gives the nickel dimethylglyoxime reaction; the small design experiment then asks for separate detection of Fe³⁺, Co²⁺, and Ni²⁺.
- Theory dependency: yes. The item relies on applying the Ni²⁺ identification method to the small-design task, not on the small-design sentence alone.
- Judgment: supportable only with explicit theory/source linkage, but not final-clean. Option-link diagnostics are still scaffold templates, and the point binding is broad. It should either be kept with a clear theory-dependent audit note and concrete option diagnostics or rewritten to ask about designing a complete separate-detection scheme.

## Blocker Classes Confirmed

- Template option-link diagnostics remain at large scale, especially chunks 1, 3, 4, and 5.
- ASCII formulas remain in effective displayed fields and option links, especially chunk 1.
- Formula-heavy or alias-heavy fill blanks remain in chunks 2-4; some include ASCII formula aliases in accepted answers.
- Several retained items are low-depth reagent/formula/name recall rather than observation or reasoning, and many do not yet have concrete retained-risk reasons in the manual logs.
- Multi-point bindings are common. Some are semantically valid because a stem asks for a shared reagent or cross-point conclusion, but others need rereview to ensure the question actually uses all bound points.
- For some samples, source previews are insufficiently complete for final proof even though point titles and source audits indicate support. Final release review must use full canonical text or page-image confirmation, not preview-only evidence.

## Conclusion

This resweep confirms the previous OpenSpec blocker decision: the final question bank is not yet import-ready. The next release-quality path is still the full per-question semantic repair required by `full-question-bank-semantic-release-repair`, starting with the unfinished chunk 1 `19-1-02` batch and then continuing through chunks 2-5.
