# Final Question Bank Quality Spotcheck - 2026-06-15 Current Spec Closeout

## Scope

- Files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- Active release questions: 2,303.
- Rejected records: 7, all in chunk 1.
- Method: scripts were used only for JSON parsing, counting, and locating sample records. The quality judgments below come from manual reading of the effective question fields, options, answers, explanations, option links, bound point keys, video point titles, and canonical source previews available in `formal_experiment_point_inventory.json`.

## OpenSpec Closeout Status

- Change: `full-question-bank-semantic-release-repair`.
- Schema: `spec-driven`.
- `openspec validate full-question-bank-semantic-release-repair --strict`: passed.
- `openspec instructions apply --change full-question-bank-semantic-release-repair --json`: 14 / 121 tasks complete, 107 remaining.
- Closeout decision: stage-closeout only. The spec is structurally valid, but it is not complete, not archive-ready, and cannot be used as release approval.

## Current Read-Only Inventory

| Chunk | Active | Rejects | Missing expl | Generic expl | Template diag | ASCII displayed | ASCII link | Fill blanks | Formula/mobile-risk fill | ASCII accepted aliases | Multi-point |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 443 | 7 | 0 | 67 | 85 | 52 | 38 | 64 | 0 | 0 | 208 |
| 2 | 450 | 0 | 0 | 37 | 0 | 0 | 0 | 64 | 7 | 7 | 140 |
| 3 | 450 | 0 | 0 | 52 | 163 | 6 | 3 | 133 | 0 | 0 | 174 |
| 4 | 450 | 0 | 0 | 96 | 217 | 4 | 8 | 126 | 13 | 13 | 221 |
| 5 | 510 | 0 | 0 | 9 | 322 | 2 | 2 | 35 | 0 | 0 | 113 |
| Total | 2,303 | 7 | 0 | 261 | 787 | 64 | 51 | 422 | 20 | 20 | 856 |

Notes:

- Missing explanations are currently zero, which is a real improvement.
- Generic explanation count includes release-visible wording such as "本题答案由对应实验的操作、现象或结论直接支持" or "对应的实验操作或现象内容是...".
- Template diagnostics count visible option-link diagnostic notes that still use scaffold wording such as "该选项直接对应本题考查的实验操作、现象或结论", "该选项混淆了本实验的试剂、操作、现象或结论", "直接落在点位", or "能回答题干要求".
- Formula/mobile-risk fill blanks count fill-blank accepted answer sets that include formula symbols, ions, or ASCII formula aliases. Each still needs manual release treatment: rewrite to deterministic single choice, or retain only with a logged hidden-grading-alias reason.

## Manual Samples

### PASS: `CHUNK1_19_1_01_Q001`

- Experiment: `19-1-01 氯、溴、碘的置换次序`
- Type: single choice
- Point keys: primary `candidate-1-034a8366`
- Effective stem: asks which operation best proves chlorine is more oxidizing than bromine.
- Answer: A, `向 KBr 溶液中加入氯水后，Br⁻ 被氧化为 Br₂`
- Judgment: release-quality sample. The stem, answer, explanation, and option links all track the point semantics. The distractors are chemically meaningful rather than generic, and the formulas use Unicode display.

### PASS / Minor Wording Risk: `EXP_19_3_03_SEMANTIC_FINAL_001`

- Experiment: `19-3-03 SO₃²⁻ 的检出`
- Type: single choice
- Point keys: primary `candidate-1-26a8e36e`, `candidate-2-795f5a0b`
- Effective stem: asks why SO₄²⁻ must be removed before detecting SO₃²⁻.
- Answer: A, `SO₄²⁻ 会干扰 SO₃²⁻ 的检出`
- Judgment: content is publishable. It asks about interference control rather than only naming the target ion. The option-link text is more verbose than necessary but names the actual ions and point relation.

### FAIL: `CHUNK1_19_1_06_Q012`

- Experiment: `19-1-06 氯酸盐的氧化性`
- Type: single choice
- Point keys: primary `candidate-4-7bed40a2`, `candidate-5-9ebfbe89`
- Effective stem: `酸化 KClO3、KI、CCl4 体系时，选择 H2SO4 而不是 HCl 或 HNO3，主要为了避免什么？`
- Answer: A, `引入额外氧化还原干扰`
- Judgment: not import-ready. The chemistry idea is supportable by the experiment and acid-choice discussion, but student-facing formulas remain ASCII (`KClO3`, `CCl4`, `H2SO4`, `HNO3`, `K+`), and the explanation is generic. It needs Unicode normalization plus a concrete explanation naming HCl/HNO₃ interference.

### FAIL: `EXP_19_3_03_SEMANTIC_FINAL_030`

- Experiment: `19-3-03 SO₃²⁻ 的检出`
- Type: fill blank
- Point keys: primary `candidate-2-795f5a0b`
- Effective stem: asks what gas is released after acidifying SO₃²⁻.
- Accepted answers: `SO2`, `SO₂`, `二氧化硫`
- Judgment: evidence-supported but not mobile-safe. The answer set mixes ASCII, Unicode, and Chinese formula names, and the explanation is generic. This should be rewritten to single choice or changed to a Chinese-only short answer with hidden aliases logged.

### PASS: `OLD_CHUNK3_EXP_19_6_02_Q001`

- Experiment: `19-6-02 金属镁燃烧`
- Type: single choice
- Point keys: primary `candidate-1-a3329021`, `candidate-2-ea144d3d`
- Effective stem: asks for the key operation and observation task in magnesium burning.
- Answer: A, `除去镁条表面氧化膜后点燃，并观察燃烧和生成物`
- Judgment: release-quality sample. It uses two point keys because the question genuinely combines operation and observation, and the explanation and distractors are deterministic.

### FAIL: `OLD_CHUNK3_EXP_19_8_01_Q001`

- Experiment: `19-8-01 Pb(OH)₂ 的生成与性质`
- Type: single choice
- Point keys: primary `candidate-1-356d797d`
- Effective stem: asks which solution is added to Pb(NO₃)₂ to generate Pb(OH)₂.
- Answer: C, `NaOH`
- Judgment: not final-clean. The answer is supported, but the item is low-depth reagent recall and the correct option-link still says "该选项直接对应本题考查的实验操作、现象或结论". It should be rewritten around Pb(OH)₂ amphoterism/phenomena or logged as a deliberate prerequisite item with concrete retained reason.

### FAIL: `REV_CH4_EXP_20_1_02_Q001`

- Experiment: `20-1-02 氨合物`
- Type: single choice
- Point keys: primary `candidate-1-5b3e91cf` through `candidate-5-2962277d`, secondary `candidate-6-e34dc5e9`
- Effective stem: asks which reagent provides NH₃ ligand.
- Answer: C, `NH₃·H₂O`
- Judgment: evidence-supported but below release standard. It is broad multi-point reagent recognition, the explanation is thin, and two option links remain template-level. It needs either a better operation/phenomenon question or a concrete retained-risk log.

### FAIL: `REV_CH4_EXP_20_1_02_Q021`

- Experiment: `20-1-02 氨合物`
- Type: fill blank
- Point keys: primary five ammonia-complex points, secondary `candidate-6-e34dc5e9`
- Accepted answers: `氨水`, `NH3·H2O`, `NH₃·H₂O`
- Judgment: not mobile-safe as a final release fill blank. The Chinese answer is short, but the visible accepted-answer set includes ASCII formula alias and symbolic formula forms. It should be single choice or retain Chinese-only display with hidden aliases explicitly logged.

### FAIL: `CHK5_SEM_EXP_20_2_08_001`

- Experiment: `20-2-08 铬(III)盐的水解`
- Type: single choice
- Point keys: primary `candidate-1-376fa2cd`
- Effective stem: asks which judgment is consistent with chromium(III) salt hydrolysis.
- Answer: B, `Cr₂(SO₄)₃ 是本实验中用于观察铬(III)盐水解的铬盐`
- Judgment: content is supportable, but the option-link diagnostics are still scaffold templates. The item likely can be kept after rewriting diagnostics and possibly strengthening the stem beyond reagent recognition.

### FAIL / Theory-Dependent: `CHK5_SEM_EXP_20_3_14_026`

- Experiment: `20-3-14 小设计实验`
- Type: single choice
- Point keys: primary `candidate-1-de6f1130`
- Effective stem: asks which judgment matches the design experiment.
- Answer: B, `Ni²⁺ 与丁二酮肟的阳性现象是生成红色沉淀。`
- Judgment: supportable only if the final audit explicitly links the preceding Ni²⁺ identification theory to the small-design task. The current explanation is too short and the correct option-link remains template-level. It should be retained only with a theory-dependent audit note or rewritten to ask for a fuller separation/detection scheme.

## Release Decision

Chunks 1-5 are not ready for direct import/publication.

The release files are parseable and every active effective question has an explanation, but the final bank still has unresolved release blockers: visible ASCII chemistry formulas, generic explanations, template option-link diagnostics, formula/alias-heavy fill blanks, low-depth recognition questions without retained-risk evidence, and many multi-point items that still require semantic confirmation.

## Recommended Next Action

Continue the OpenSpec task order instead of archiving:

1. Finish chunk 1 task `3.6` onward, starting with `19-1-06`, because the current spotcheck found clustered ASCII/generic-explanation failures there.
2. Treat formula/mobile-risk fill blanks in chunks 2 and 4 as release blockers unless rewritten or explicitly logged as hidden deterministic aliases.
3. Reauthor option-link diagnostics for chunks 3-5 where scaffold wording remains visible.
4. Only declare import readiness after tasks `8.1` through `8.18` pass and the final all-chunk QA report shows zero unresolved blockers.
