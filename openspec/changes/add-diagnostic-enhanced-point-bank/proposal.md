## Why

The reviewed 2,310-question bank now has point bindings, but it still inherits many old-bank limitations: questions were not designed from the start to diagnose a specific experiment video point, and fill-blank items remain less suitable for phone-based student answering. We need a small, inspectable enhanced-bank demo before committing to a full point-level default bank.

## What Changes

- Add a diagnostic enhanced question-bank artifact format generated from existing formal experiment video points.
- For each covered experiment point, require exactly `2` single-choice questions and `1` true/false question.
- Exclude fill-blank questions from the enhanced diagnostic bank.
- Require every question to cite canonical experiment source evidence and bind to one or more existing experiment video point keys.
- Require single-choice distractors to carry diagnostic option links when the option represents a recognizable misconception, adjacent point, adjacent experiment, or weak distractor.
- Produce a limited demo artifact first for product review, then use the same rules for full 77-experiment generation only after demo quality is accepted.
- Keep the enhanced bank separate from the current reviewed old-bank artifact until an explicit promotion/import decision is made.

## Capabilities

### New Capabilities

- `diagnostic-enhanced-question-bank`: Defines the per-video-point enhanced assessment bank, its required question mix, source-audit rules, option-level diagnostic links, demo-first workflow, and promotion boundaries.

### Modified Capabilities

- `experiment-question-bank-management`: Adds support for treating a validated diagnostic enhanced bank as a candidate default-bank seed/import source, separate from the reviewed old-bank artifact.

## Impact

- Affects generated question-bank artifacts under `artifacts/`.
- Affects point-aware question validation/generation scripts.
- May later affect backend import logic if the enhanced bank is promoted.
- No immediate production question-bank replacement, no student-facing publication, and no frontend UI change in the demo step.
