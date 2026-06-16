## Context

This change originally proposed a separate enhanced diagnostic bank with a fixed `2` single-choice plus `1` true/false item mix per video point. The later production work took a different, more complete route: the existing 2,310-question bank was slimmed, rebuilt in small packets, semantically polished, validated, imported over the old default bank, and exposed through a point-aware teacher UI.

The released shape supports all current deterministic objective types (`single_choice`, `true_false`, `fill_blank`) and stores point bindings, source audit, option links, coverage tags, and review lineage in question metadata. That makes the old separate demo path redundant for the current release.

## Goals / Non-Goals

**Goals:**

- Close the stale fixed-mix enhanced-bank demo plan.
- Align this change with the already-completed production point-aware default-bank migration.
- Preserve the quality rules that still matter: source audit, existing video point bindings, deterministic grading, option-level diagnostics, and teacher-visible evidence.
- Keep future fixed-mix diagnostic generation available only as a future explicit change if product needs it.

**Non-Goals:**

- Do not regenerate or mutate the current imported question bank.
- Do not introduce a new published question type.
- Do not remove `fill_blank` from the current default bank.
- Do not add AI semantic grading.

## Decisions

### Decision: Supersede the separate fixed-mix enhanced-bank demo

The current release uses the reviewed point-aware default bank as the canonical production bank. The fixed `2` single-choice plus `1` true/false per point target is not archived as a current requirement because it would conflict with the imported bank's actual deterministic type mix.

### Decision: Keep point-aware diagnostics as metadata, not a new bank family

The imported bank already carries primary point keys, point titles, source refs, source audit metadata, option links, coverage tags, and review lineage. Teacher browsing, analytics, and AI suggestion workflows consume that metadata directly.

### Decision: Preserve fill blanks only when deterministic and phone-friendly

Fill blanks remain valid in the production bank when they use short accepted answers and deterministic matching. Long equation entry, reagent combinations, and free-form explanations remain out of scope.

## Risks / Trade-offs

- The current bank is not evenly fixed to three questions per video point -> acceptable for this release because it prioritizes reviewed source-grounded coverage and preserves validated migrated content.
- A future diagnostic-only drill bank may still be useful -> reopen as a separate future change with explicit product approval and no conflict with the published default bank.
