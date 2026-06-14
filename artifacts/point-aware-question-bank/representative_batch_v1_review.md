# Representative Point-Aware Batch Review

## Scope

This batch tests the full-bank workflow on three experiments beyond `EXP_19_1_01`:

- `EXP_19_1_03` 氯水对溴离子、碘离子混合溶液的氧化顺序
- `EXP_20_2_07` 铁(III)盐的水解
- `EXP_20_3_14` 小设计实验

The batch intentionally covers:

- multi-point observation and sequence judgment,
- single-point hydrolysis operation discrimination,
- design-type metal ion identification.

## Result

- Total reviewed: 9
- Keep: 8
- Rewrite: 1
- Reject: 0
- Validator errors: 0

## Question-By-Question Review

### EXP_19_1_03

`REP_EXP_19_1_03_Q001` is kept because it asks students to identify the purpose of observing the CCl4 layer in a mixed KBr/KI system, rather than merely recall a reagent list. The correct option binds to the observation-order point, while distractors capture CCl4-as-oxidant and unrelated ion misconceptions.

`REP_EXP_19_1_03_Q002` is kept because it is a clear positive/negative concept check: CCl4 is observation support, not the oxidant. It avoids double-negative wording.

`REP_EXP_19_1_03_Q003` is kept as a fill blank because the accepted answers are short words: `颜色` and `颜色变化`. It does not ask for a full reagent combination or equation.

### EXP_20_2_07

`REP_EXP_20_2_07_Q001` is kept because it distinguishes the Fe(III) hydrolysis point from adjacent Cr(III), Ti(IV), and metal-ion-identification content in the same or nearby source material.

`REP_EXP_20_2_07_Q002` is kept because it checks whether students confuse adjacent hydrolysis operations. It is source-grounded and phrased positively.

`REP_EXP_20_2_07_Q003` is marked rewrite. The original fill blank only asks students to recall `FeCl3`, which is too shallow. The proposed replacement is a single-choice point-discrimination item.

### EXP_20_3_14

`REP_EXP_20_3_14_Q001` is kept because it tests the design nature of the experiment: combine Fe, Co, and Ni identification methods rather than use a single unrelated reagent.

`REP_EXP_20_3_14_Q002` is kept because it checks the design-goal understanding directly and avoids an open-answer scheme.

`REP_EXP_20_3_14_Q003` is kept as a basic fill blank because the answer is a short token and identifies the third target ion in the design experiment. It is acceptable as a low-level coverage item, but full-bank generation should not overuse this pattern.

## Rule Adjustments For Full Generation

- Keep fill blanks rare and short.
- Prefer single-choice when the answer would be a reagent combination.
- Use adjacent points as distractors when a source chunk includes several neighboring experiments.
- For design experiments, avoid asking students to type a full plan; use objective items that test plan structure and method selection.
- For source chunks that include several subexperiments, option links should make adjacent-point confusion explicit.

## Validation

Command:

```powershell
python -X utf8 scripts\point_aware_question_bank.py validate --file artifacts\point-aware-question-bank\representative_batch_v1.json --report artifacts\point-aware-question-bank\representative_batch_v1_validation_report.json
```

Result: valid, 0 errors.
