# Final Question Bank Quality Spotcheck - 2026-06-15 After 19-1-02 Closeout

## Scope

- Files checked:
  - `chunk_1_release_final_v1.json`
  - `chunk_2_release_final_v1.json`
  - `chunk_3_release_final_v1.json`
  - `chunk_4_release_final_v1.json`
  - `chunk_5_release_final_v1.json`
- Active effective questions found: 2,303.
- Chunk 5 uses `reviewed_questions` rather than `questions`; the spotcheck parser handled both structures.

## Spec Closeout Status

- OpenSpec change: `full-question-bank-semantic-release-repair`
- Current progress after this pass: 12 / 121 tasks complete.
- `19-1-02` in chunk 1 is now manually rereviewed, repaired, logged, and Unicode-safe local-gate clean:
  - active = 30
  - missing effective explanations = 0
  - template option-link diagnostics = 0
  - visible ASCII chemistry formulas in effective displayed fields / option-link text = 0
  - option-link text mismatches = 0
  - invalid point keys = 0
  - true/false invalid option links = 0
  - unresolved mobile fill-blank risks = 0
- The OpenSpec package validates with `openspec validate full-question-bank-semantic-release-repair --strict`.
- The change is not complete and must not be archived; 109 tasks remain.

## Release Decision

The final question bank is not ready for import or publication.

Reason: even after the `19-1-02` closeout, a Unicode-safe read-only sweep plus manual spotcheck still finds large unresolved classes across the five release files: template option-link diagnostics, visible ASCII chemistry notation, formula/mobile-risk fill blanks, duplicate effective stems, and low-depth/generic questions marked publishable.

## Read-Only Risk Sweep

The following counts are navigation/validation signals only. They do not replace manual semantic review.

| Chunk | Active | Missing explanations | Template option-link records | ASCII display records | ASCII option-link records | Mobile-risk fill records | Duplicate-stem groups | Duplicate-stem records |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| chunk 1 | 443 | 0 | 194 | 121 | 98 | 4 | 10 | 33 |
| chunk 2 | 450 | 0 | 0 | 37 | 42 | 7 | 0 | 0 |
| chunk 3 | 450 | 0 | 163 | 38 | 33 | 42 | 0 | 0 |
| chunk 4 | 450 | 0 | 216 | 18 | 20 | 14 | 0 | 0 |
| chunk 5 | 510 | 0 | 322 | 110 | 88 | 0 | 17 | 168 |

Aggregate blocker signals:

- Template option-link records: 895
- ASCII display records: 324
- ASCII option-link records: 281
- Mobile-risk fill records: 67
- Duplicate-stem groups: 27
- Duplicate-stem records: 201

## Manual Spotcheck Samples

| Sample | Point keys | Manual verdict | Reason |
|---|---|---|---|
| `CHUNK1_19_1_02_Q017` | `candidate-1-656364cb` | Pass | Rewritten into Na₂S₂O₃-system phenomenon judgment; answer/explanation are deterministic and point-bound. |
| `CHUNK1_19_1_03_Q008` | `candidate-2-fd1f659e` | Fail | Effective stem/options still show `CCl4`, `I-`, `Br-`, `K+`; option diagnostics still use template wording such as “直接落在点位 / 能回答题干要求”. |
| `CHUNK1_19_1_03_Q001` | `candidate-1-f52542f6`, `candidate-2-fd1f659e` | Fail | Explanation is only “答案为：I⁻。”; option links contain template wording and the correct option points only to the first point despite needing the color-change point. |
| `EXP_19_3_03_SEMANTIC_FINAL_004` | `candidate-2-795f5a0b` | Fail | Semantics are mostly supportable, but option-link diagnostics are scaffold-like (“本题焦点…不匹配”) rather than concrete student-facing evidence. |
| `EXP_19_4_02_SEMANTIC_FINAL_021` | `candidate-1-88b9b794` | Fail | Marked rewrite but remains fill blank asking for `I₂ / I2 / 碘`; this is formula/mobile-input fragile and should be single choice or short Chinese-only. |
| `OLD_CHUNK3_EXP_19_6_02_Q006` | `candidate-2-ea144d3d` | Fail | Correct answer is supportable, but diagnostics include template text and odd adjacent-experiment wording; ASCII formula display also remains in options. |
| `OLD_CHUNK3_EXP_19_6_03_Q007` | `candidate-1-0b2d08c4`, `candidate-2-60fd99ae` | Fail | Safety operation is supportable, but all option diagnostics are generic; distractor point keys are over-attached to the correct point. |
| `REV_CH4_EXP_20_1_02_Q001` | `candidate-1-5b3e91cf` through `candidate-5-2962277d`; secondary `candidate-6-e34dc5e9` | Fail | Low-depth reagent recall; overbroad point binding; explanation only says metal salts react with ammonia water; option links remain template/generic. |
| `REV_CH4_EXP_20_1_02_Q021` | `candidate-1-5b3e91cf` through `candidate-5-2962277d`; secondary `candidate-6-e34dc5e9` | Fail | Fill blank asks for `NH₃` source and retains ASCII alias `NH3·H2O`; mobile input and hidden/visible alias policy are not resolved. |
| `CHK5_SEM_EXP_20_2_08_001` | `candidate-1-376fa2cd` | Fail | Generic “下列哪项判断…” rewrite, template option diagnostics, low-depth reagent recognition, and ASCII option-link formula aliases. |
| `CHK5_SEM_EXP_20_2_08_002` | `candidate-1-376fa2cd` | Fail | Same effective stem pattern as Q001 with different options; duplicate-stem risk plus template diagnostics. |
| `CHK5_SEM_EXP_20_2_08_010` | `candidate-1-376fa2cd` | Fail | Answer is supportable, but explanation is too generic (“沉淀是…表现”), and option links are still template statements. |

Manual sample result: 1 pass, 11 fail.

## Main Quality Risks

1. `19-1-02` is now closed cleanly, but the surrounding chunk 1 experiments still carry unresolved template diagnostics and ASCII formula display.
2. Chunk 5 is structurally the riskiest: 322 template option-link records and 168 duplicate-stem records, with repeated “下列哪项判断与实验操作、现象或结论一致？” stems across the same experiment.
3. Chunk 4 still contains overbroad point bindings and formula-heavy fill blanks even when items are marked `publishable`.
4. Chunks 2 and 3 have fewer template flags than chunks 1/4/5, but still contain formula/mobile-input risks and scaffold-like diagnostics in sampled items.
5. The lack of missing explanations is good, but explanation presence alone is not enough: several sampled explanations are generic and do not meet the source-specific evidence standard.

## Conclusion

Do not import or publish chunks 1-5 yet.

The next repair pass should continue OpenSpec task order, starting with remaining chunk 1 batches and the blocker inventory tasks. Every completed experiment batch should use the Unicode-safe template scan, because the earlier Chinese-literal scan can miss residual template wording under PowerShell/Node encoding.
