## Why

This change began as a plan for a separate fixed-mix diagnostic enhanced-bank demo. Subsequent work completed a stronger production path instead: the reviewed 2,310-question default bank was rebuilt, validated, imported, displayed by experiment/video point, and connected to point-aware analytics and AI suggestion workflows.

## What Changes

- Close the obsolete standalone enhanced-bank demo plan.
- Treat the imported reviewed point-aware default bank as the current production question-bank migration target.
- Preserve the supported objective question types: `single_choice`, `true_false`, and deterministic phone-friendly `fill_blank`.
- Keep source audit, existing formal experiment video point bindings, option-level diagnostic links, and deterministic answer data as the release requirements.
- Record that the old fixed `2` single-choice plus `1` true/false per point plan is not required for the current release and should only be reopened through a future explicit change.
- Keep teacher-facing browsing and AI suggestion workflows aligned with the imported point-aware bank rather than a separate unpublished demo artifact.

## Capabilities

### New Capabilities

### Modified Capabilities

- `experiment-question-bank-management`: Clarifies that the completed point-aware reviewed default bank supersedes the older fixed-mix enhanced-bank demo path for the current release.

## Impact

- OpenSpec change cleanup and archival.
- No new question-bank data mutation.
- No new frontend or backend implementation in this cleanup change; it records the already-completed production migration path.
