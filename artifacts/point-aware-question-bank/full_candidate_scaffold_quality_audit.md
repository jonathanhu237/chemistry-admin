# Full Candidate Scaffold Quality Audit

## Conclusion

This artifact is a complete point-coverage scaffold, not a production-quality default question bank.

It covers all 77 formal experiments and all 300 formal video points, and it validates point bindings, source-audit plumbing, option-link shape, and staging-import metadata. However, the questions are intentionally low-depth point-recognition items. They should not be promoted as the student-facing default bank.

## Quantitative Findings

- Experiments covered: 77
- Questions generated: 300
- Video point keys covered: 300
- Question types: 300 single-choice, 0 true/false, 0 fill-blank
- Review decisions: 300 keep
- Quality flags: 300 `coverage_scaffold`, 300 `basic_point_recognition`
- Unique stems: 77
- Answer distribution: A 76, B 75, C 74, D 75
- Experiments with only one scaffold question: 8

## Main Quality Problems

1. The stem is repeated per experiment: most questions ask which option matches a formal video point.
2. The correct answer is often just a reagent/operation point title, not a phenomenon, reasoning, method, safety, or misconception check.
3. All questions are single-choice, so the final bank type mix is not represented.
4. Distractors are often adjacent point titles rather than carefully designed misconceptions.
5. The scaffold does not meet the desired student-facing depth for default bank usage.

## What Is Actually Useful

- Verifies every formal video point can receive a stable question binding.
- Verifies every accepted item can carry `primary_point_keys`, `coverage_tags`, `option_links`, and `source_audit`.
- Verifies the staging import path can preserve point-aware metadata.
- Gives Codex a deterministic checklist for the real full generation pass.

## Required Next Pass

The production full-bank pass should generate reviewed questions per experiment point using the representative batch quality bar:

- Keep the three student-facing types: single-choice, true/false, fill-blank.
- Keep fill blanks short and phone-friendly only.
- Prefer phenomenon, observation, operation purpose, method discrimination, and misconception items.
- Avoid asking students to type reagent combinations, full equations, or full design plans.
- Bind each question to one or more existing video point keys.
- Add option-level diagnostic links for meaningful single-choice distractors.
- Require concrete replacement questions for every rewrite decision.

