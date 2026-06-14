# Point-Aware Question Demo Review: EXP_19_1_01

## Scope

- Experiment: `EXP_19_1_01`
- Code: `19-1-01`
- Title: 氯、溴、碘的置换次序
- Demo change: `demo-point-aware-question-bank`
- Review mode: manual source audit
- Production data mutation: none

This revision uses the existing experiment video points as the question binding target. It no longer invents separate `EXPPOINT_*` IDs for final bindings.

## Existing Experiment Video Points

The three point keys come from `formal_experiments.metadata.video_candidates` and the admin video-point API:

| point_key | point_title | Current video resource |
| --- | --- | ---: |
| `candidate-1-034a8366` | 氯水 + KBr 溶液 + CCl₄ | 1 published |
| `candidate-2-1e180c68` | 氯水 + KI 溶液 + CCl₄ | 0 |
| `candidate-3-9b8be606` | 溴水 + KI 溶液 + CCl₄ | 0 |

Cross-cutting ideas such as `CCl₄ observation layer` and `oxidation order` are kept only as coverage tags. They do not replace the video point key as the analytics binding.

## Source Evidence Used

Canonical experiment evidence:

- `expchunk_00193_497eb97bd6`: experiment purpose, including mastering halogen oxidizing ability and halide reducing ability.
- `expchunk_00199_8240477bff`: experiment content for halogen oxidizing ability. It lists KBr, KI, CCl4, chlorine water, bromine water, asks students to design tube experiments to explain displacement order, asks them to observe the CCl4 layer color, and asks them to explain the halogen oxidizing trend.

Supporting theory evidence:

- `textbook_prose_00028_a4c7b7c9ae`: iodine solubility and color in organic solvents including CCl4.
- `textbook_prose_00043_871f62b3d9`: chlorine water and bromine water as halogen water systems.

Boundary:

- The canonical experiment chunk supports the experiment design and intended conclusions, but it does not spell out every final product or every observed color.
- Questions requiring detailed phenomenon colors should cite additional theory or local phenomenon evidence.
- The mixed bromide/iodide oxidation-sequence task belongs to `EXP_19_1_03`, so it was deferred.

## Question Review Summary

Reviewed sample size: 12

| Type | Reviewed | Keep | Rewrite | Reject |
| --- | ---: | ---: | ---: | ---: |
| Single choice | 5 | 2 | 3 | 0 |
| True/false | 3 | 0 | 2 | 1 |
| Fill blank | 4 | 0 | 4 | 0 |
| Total | 12 | 2 | 9 | 1 |

All 9 rewrite decisions now include a concrete `proposed_question`.

## Fill Blank Rule

The bank still supports three objective types: `single_choice`, `true_false`, and `fill_blank`.

The demo does not use AI grading for correctness. Fill blanks must remain deterministic and mobile-friendly:

- OK: one ion, one substance, one relation word, or one short observation word.
- Not OK: full reagent combinations, complete equations, multi-step explanation, or open-ended reasoning.

Example rejected fill-blank shape:

> 说明 Cl2 氧化性强于 Br2 的一种试剂组合是____。

This asks the student to type a long reagent combination on a phone. The proposed replacement is a single-choice question:

> 要用本实验点位证明 Cl₂ 的氧化性强于 Br₂，下列哪一组最合适？

Correct answer: `氯水 + KBr 溶液 + CCl₄`.

## Examples

### Keep: option-level binding works

Question: "最能说明氯的氧化性强于溴的是哪一项？"

Decision: keep

Why:

- Correct option maps to `candidate-1-034a8366`.
- Wrong options expose oxidation-order misconceptions.
- The item can support analytics because a wrong selected option says something about the student's misconception.

### Rewrite: CCl4 role question was too shallow

Old question: "CCl4 的主要作用最接近下列哪一项？"

Decision: rewrite

Replacement direction:

- Bind to the relevant video point(s).
- Ask why observing the organic layer helps determine whether displacement occurred.
- Keep deterministic single-choice scoring.

### Rewrite: reagent-combination fill blank is phone-unfriendly

Old question: "说明 Cl2 氧化性强于 Br2 的一种试剂组合是____。"

Decision: rewrite

Replacement:

- Single choice over the existing video points.
- Correct option binds to `candidate-1-034a8366`.
- Distractors distinguish `Cl2 > I2`, `Br2 > I2`, and non-experiment choices.

## Recommended Full-Scale Direction

For all 77 experiments, do not start from "30 questions per experiment." Start from:

```text
formal experiment
  -> existing video points
  -> canonical evidence audit
  -> generated objective questions
  -> manual per-question review
  -> question-level and option-level video point links
```

The current 2,310-question bank should be treated as draft candidate material only. Full regeneration should produce point-aware questions from the beginning.

## Files

- `assessment_points.json`
- `reviewed_questions.json`
