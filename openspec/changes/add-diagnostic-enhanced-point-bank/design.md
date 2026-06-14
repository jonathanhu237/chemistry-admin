## Context

The current reviewed old-bank artifact keeps the original 2,310-question shape and adds point-aware metadata. It is valuable as a cleaned migration candidate, but it was not authored around experiment video points as first-class diagnostic targets. Some old items are still too broad, too easy, or less useful for analyzing why a student chose a wrong option.

The enhanced bank is a new authored artifact. It starts from formal experiment video points and canonical experiment source chunks. The intended full target is every existing formal experiment point with `2` single-choice questions and `1` true/false question per point, but this change MUST first produce a small demo artifact for product review.

## Goals / Non-Goals

**Goals:**

- Define a diagnostic enhanced bank format that is point-first rather than old-question-first.
- Produce a demo artifact that can be inspected manually before full generation.
- Keep only single-choice and true/false questions in the enhanced bank.
- Make single-choice distractors useful for learning analytics through option-level diagnostic links.
- Require source audit against canonical experiment material for every accepted item.
- Preserve multi-point binding when a question legitimately spans multiple video points.

**Non-Goals:**

- Do not delete or replace the reviewed old-bank artifact.
- Do not publish enhanced questions to students in this change.
- Do not add AI semantic grading or AI correction for student answers.
- Do not use keyword matching as the final source or point-binding authority.
- Do not require frontend UI changes for the demo artifact.

## Decisions

### Decision: Generate point-first questions

Each enhanced item is authored for one primary experiment video point, then may add secondary point keys when the stem, answer, or explanation depends on another point. This makes the artifact useful for weak-point analytics without pretending every question belongs to exactly one point.

Alternative considered: keep reviewing the old bank until every old question is point-perfect. That remains useful for migration, but it cannot guarantee even diagnostic coverage per point.

### Decision: Use 2 single-choice plus 1 true/false per point

The full target is three objective diagnostic items per point: two single-choice questions for misconception-level diagnosis and one true/false question for fast concept checking. Fill blanks are excluded because many chemistry answers are awkward on mobile and the user does not want AI-based answer correction.

Alternative considered: keep the old `10 + 10 + 10` per experiment mix. That produces more volume but less predictable point coverage and weaker per-point analytics.

### Decision: Use source audit and manual demo review as quality gates

The generator may use structured data and source chunks to draft questions, but accepted demo items MUST include canonical chunk ids, evidence sufficiency, and a reviewer note. Keyword matching MAY help locate candidates but SHALL NOT decide bindings.

Alternative considered: automatically assign points based on title or reagent overlap. That is too risky because a question can involve multiple points and option-level misconceptions may refer to adjacent points.

### Decision: Keep enhanced bank as a separate candidate source

The enhanced artifact is stored separately from the reviewed old-bank merge. Import and promotion remain explicit later steps so product review can decide whether the enhanced bank should become the default student bank, coexist with reviewed old-bank questions, or be used only for diagnostics.

## Risks / Trade-offs

- Manual review is slower than automatic generation -> limit this change to a demo and use the result to estimate full generation effort.
- Some video points may lack enough canonical evidence for high-quality distractors -> mark evidence as insufficient and do not invent unsupported content.
- Per-point target counts may reveal weak point definitions -> report points that need better source material or point splitting before full generation.
- Full generation volume depends on point count -> compute expected counts from the current inventory before producing the full plan.
