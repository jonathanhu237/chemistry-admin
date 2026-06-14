# Point-Aware Question Generation And Review Protocol

## Scope

This protocol applies to the regenerated default bank for all formal experiments. The current 2,310-question bank is candidate material only; it is not a source of truth.

## Required Inputs Per Experiment

- Formal experiment id, code, and title.
- Existing video point keys and titles from `formal_experiments.metadata.video_candidates`.
- Canonical experiment chunk ids and source references.
- Optional supporting theory chunk ids and source references.
- Current old-bank candidates, if useful for rewrite ideas.

## Generation Rules

1. Start from existing video points, not from a generic experiment title.
2. Generate only `single_choice`, `true_false`, and `fill_blank`.
3. Every candidate question must include:
   - `question_id`
   - `question_type`
   - `stem`
   - deterministic `answer`
   - `explanation`
   - `primary_point_keys`
   - `coverage_tags`
   - `source_audit`
   - `review_decision`
   - `quality_flags`
4. Every single-choice question must include four options and `option_links`.
5. Every fill blank must be answerable by a short phone-friendly accepted answer.
6. Do not ask students to fill long reagent combinations, full equations, or open explanations.
7. Do not use AI semantic grading for correctness.
8. Do not claim a phenomenon, color, product, or safety fact unless the source audit cites adequate evidence.

## Review Rules

Codex must review every generated candidate one by one.

For each candidate, check:

- Chemical correctness.
- Whether the canonical experiment chunk supports the stem, answer, and explanation.
- Whether supporting theory is needed and cited separately.
- Whether every `primary_point_key` belongs to the formal experiment.
- Whether single-choice distractors diagnose a misconception, adjacent point, or unrelated distractor.
- Whether fill-blank answers are deterministic and phone-friendly.
- Whether the item is too shallow, such as direct equation recitation or reagent-combination recall.

Review decision:

- `keep`: candidate is acceptable as an objective point-aware item.
- `rewrite`: candidate has a usable idea but must include `proposed_question`.
- `reject`: candidate should not enter the default bank.

## Output Shape

The generated artifact must follow:

```json
{
  "metadata": {
    "artifact_type": "point_aware_question_bank",
    "version": "point-aware-question-bank-v1"
  },
  "experiments": [
    {
      "experiment_id": "EXP_...",
      "experiment_code": "...",
      "experiment_title": "...",
      "video_points": [
        {"point_key": "...", "point_title": "..."}
      ],
      "questions": []
    }
  ]
}
```

Before import, run:

```powershell
python -X utf8 scripts\point_aware_question_bank.py validate --file <artifact>
```
