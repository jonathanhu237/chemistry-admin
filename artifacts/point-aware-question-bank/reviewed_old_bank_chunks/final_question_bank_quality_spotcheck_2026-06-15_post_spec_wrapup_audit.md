# Final Question Bank Quality Spotcheck - Post Spec Wrap-up

Date: 2026-06-15

Scope:
- Release files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- OpenSpec change checked: `full-question-bank-semantic-release-repair`.
- Sampling method: risk-stratified manual spotcheck. Scripts were used only to locate records, point keys, and source references; all pass/conditional/fail judgments below come from manual semantic reading.

## OpenSpec Wrap-up Status

- `openspec validate full-question-bank-semantic-release-repair --strict` passes.
- `openspec status --change full-question-bank-semantic-release-repair --json` reports all four artifacts as `done`: proposal, design, specs, tasks.
- `openspec instructions apply --change full-question-bank-semantic-release-repair --json` reports 167 tasks total, 18 complete, 149 remaining.
- Therefore the spec is structurally valid but not implementation-complete. It should not be archived or treated as release-complete.

## Overall Spotcheck Result

- Total sampled questions: 15
- Pass: 5
- Conditional pass: 3
- Fail / not import-ready: 7

Release decision from this spotcheck: chunks 1-5 are still not ready for full import/publication as a final question bank. The failing items are not isolated formatting defects; they show the same semantic failure classes already captured in the OpenSpec blocker baseline.

## Manual Findings

| Record | Chunk | Result | Point binding | Manual judgment |
|---|---:|---|---|---|
| `CHUNK1_19_1_01_Q001` | 1 | Conditional pass | `candidate-1-034a8366` | Student-facing question is usable: Cl2 oxidizing Br- from KBr is supported by the replacement experiment point. However `source_audit.reviewer_note` describes a different KClO3/KI/CCl4 evidence chain, so audit metadata contradicts the final question. |
| `CHUNK1_19_1_08_Q001` | 1 | Fail | `candidate-1-1e83fb7a`, `candidate-4-fb906ca4` | Too low-depth: only asks for the silver salt reagent AgNO3. Explanation is only "答案为：AgNO3 溶液"; point binding is over-broad because the stem does not ask for filter-paper/key/light exposure observation. Option links remain template-like. |
| `CHUNK1_19_1_08_Q004` | 1 | Conditional pass | `candidate-4-fb906ca4` | The observation "unshielded area darkens" is supported by the experiment text and point. But explanation is still generic, and the correct option-link says "直接落在点位/能回答题干要求" instead of naming the actual light-exposed area darkening evidence. |
| `CHUNK1_19_1_08_Q015` | 1 | Fail | `candidate-1-1e83fb7a` | True/false item is guessable and absurd: "AgCl 感光性实验的关键观察对象是火焰颜色." It does not test the experiment design; explanation only states the answer is false. |
| `EXP_19_3_03_SEMANTIC_FINAL_001` | 2 | Pass | `candidate-1-26a8e36e`, `candidate-2-795f5a0b` | Supported: the canonical text states SO42- interferes with SO32- detection and must be removed first. Multi-point binding is reasonable because the item links interference removal to target-ion verification. |
| `EXP_19_3_03_SEMANTIC_FINAL_030` | 2 | Fail | `candidate-2-795f5a0b` | Formula-heavy fill blank asks for SO2/SO₂/二氧化硫. This is mobile-risk and includes visible symbolic aliases; explanation is generic. It should be rewritten to deterministic single choice or a short Chinese answer-only blank. |
| `EXP_19_4_02_SEMANTIC_FINAL_025` | 2 | Pass | `candidate-1-88b9b794` | The item was rewritten from a formula-risk blank to single choice and asks the reagent after acidified KI. It is low-depth but operationally anchored and machine-deterministic. |
| `EXP_19_4_09_SEMANTIC_FINAL_021` | 2 | Fail | `candidate-2-a452c505` | Fill blank for Fe(NO)SO4 / Fe(NO)SO₄ is formula-heavy, phone-hostile, and explanation is generic. It still exposes ASCII alias handling as visible answer content. |
| `OLD_CHUNK3_EXP_19_6_02_Q001` | 3 | Pass | `candidate-1-a3329021`, `candidate-2-ea144d3d` | Good multi-point item: asks for the operation-plus-observation chain of removing Mg oxide film, igniting Mg, and observing combustion/product. Both point keys are genuinely used. |
| `OLD_CHUNK3_EXP_19_8_01_Q001` | 3 | Fail | `candidate-1-356d797d` | Low-depth reagent recall: only asks which solution is added to Pb(NO3)2 to form Pb(OH)2. Option links also assign the same point key to unrelated distractors, and the correct diagnostic is still template-like. |
| `REV_CH4_EXP_20_1_02_Q022` | 4 | Fail | `candidate-1-5b3e91cf` | Fill blank asks only for "硫酸铜" and includes CuSO4/CuSO₄ aliases. It is a reagent-name recall item with mobile alias risk and generic explanation. |
| `REV_CH4_EXP_20_1_02_Q030` | 4 | Conditional pass | `candidate-8-31e3319e` | The inner/outer-sphere focus is relevant to the CuSO4-ammonia design task, but it depends on supporting coordination theory and the explanation is too vague. Needs theory dependency stated in the final explanation, not only metadata. |
| `CHK5_SEM_EXP_20_2_08_001` | 5 | Pass | `candidate-1-376fa2cd` | Strong repaired item: asks for Cr2(SO4)3 + Na2CO3 operation and distinguishes TiOSO4/KSCN distractors. Point binding and option diagnostics are specific. |
| `CHK5_SEM_EXP_20_3_01_002` | 5 | Pass | `candidate-1-e0d18274` through `candidate-6-c0cbece1` | Multi-point binding is justified because the item asks students to group multiple water-aqua cations separately from anions. The correct option names the grouping logic and distractors are meaningful. |
| `CHK5_SEM_EXP_20_3_14_026` | 5 | Fail | `candidate-1-de6f1130` | Still has generic shell stem ("哪项判断与实验操作、现象或结论一致"). It only tests Ni2+ with dimethylglyoxime, while the point asks for a scheme to separately identify Fe3+, Co2+, and Ni2+. Option links remain template-like, and distractor D is wrongly tied to the same point. |

## Failure Classes Still Present

- Low-depth reagent/object recall: `CHUNK1_19_1_08_Q001`, `OLD_CHUNK3_EXP_19_8_01_Q001`, `REV_CH4_EXP_20_1_02_Q022`.
- Guessable or absurd true/false: `CHUNK1_19_1_08_Q015`.
- Formula-heavy/mobile-risk fill blanks: `EXP_19_3_03_SEMANTIC_FINAL_030`, `EXP_19_4_09_SEMANTIC_FINAL_021`, `REV_CH4_EXP_20_1_02_Q022`.
- Template or non-semantic option diagnostics: `CHUNK1_19_1_08_Q001`, `CHUNK1_19_1_08_Q004`, `OLD_CHUNK3_EXP_19_8_01_Q001`, `CHK5_SEM_EXP_20_3_14_026`.
- Over-broad or wrong point binding: `CHUNK1_19_1_08_Q001`, `CHK5_SEM_EXP_20_3_14_026`; distractor point-link misuse in `OLD_CHUNK3_EXP_19_8_01_Q001`.
- Audit metadata contradiction: `CHUNK1_19_1_01_Q001`.

## Evidence Notes

- Direct canonical support was confirmed for the silver halide photosensitivity operation: AgCl/AgBr/AgI precipitates are spread on filter paper, covered with a key, exposed to light, and the key outline is observed.
- Direct canonical support was confirmed for SO42- interference before SO32- detection, Cr2(SO4)3 + Na2CO3 hydrolysis observation, magnesium strip ignition after oxide-film removal, CuSO4 + ammonia complex formation, and the Fe3+/Co2+/Ni2+ design experiment prompt.
- Theory dependency remains necessary for inner/outer coordination-sphere interpretation and for some ion-identification chemistry in design experiments. Those dependencies must be stated in final explanations when retained.

## Conclusion

I confirm this was a manual semantic spotcheck of each sampled item, not a script-generated approval. The final release bank still contains import-blocking semantic quality issues. The OpenSpec change is valid as a repair plan and blocker baseline, but the implementation tasks are not complete and the current release files should not be declared ready for production import.
