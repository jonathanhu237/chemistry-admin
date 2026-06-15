# Final Question Bank Quality Spotcheck - 2026-06-15 After Stage Closeout

## Scope

- Files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- Active effective questions counted: 2,303.
- OpenSpec change: `full-question-bank-semantic-release-repair`.
- OpenSpec apply progress after this stage: 8 / 111 tasks complete.
- This is a spotcheck and gate scan, not a substitute for the required full manual semantic rereview.

## Stage Closeout

`19-2-02 过氧化氢的制备` in chunk 1 was manually rereviewed and repaired in this stage. Its local validation is clean:

- active questions: 30
- missing effective explanations: 0
- generic effective explanations: 0
- option-link text mismatches: 0
- ASCII digit formulas in effective displayed fields: 0
- duplicate effective stems: 0

The OpenSpec change is not archive-ready because 103 implementation tasks remain.

## Script Gate Results

Scripts were used only for parsing, counting, and locating risk candidates. They did not decide semantic correctness.

| Chunk | Active | Missing explanations | Generic explanations | ASCII digit formula risk | Option-link mismatch | Scaffold wording | Fill-blank mobile risk candidates |
|---|---:|---:|---:|---:|---:|---:|---:|
| chunk 1 | 443 | 21 | 0 | 64 | 0 | 0 | 0 |
| chunk 2 | 450 | 0 | 0 | 4 | 0 | 0 | 2 |
| chunk 3 | 450 | 0 | 0 | 0 | 0 | 0 | 13 |
| chunk 4 | 450 | 0 | 0 | 6 | 0 | 0 | 4 |
| chunk 5 | 510 | 0 | 0 | 0 | 0 | 0 | 0 |

## Manual Spotcheck Samples

| Sample | Manual conclusion |
|---|---|
| chunk 1 `CHUNK1_19_3_02_Q003` | Not publishable as-is. The answer "还原性" is semantically supported by SO₂ reducing acidified KMnO₄, but the effective explanation is missing. This violates release explanation completeness. |
| chunk 1 `CHUNK1_19_1_06_Q012` | Not publishable as-is. The rewritten question is directionally reasonable, but the effective stem still uses ASCII formulas such as `KClO3`, `CCl4`, `H2SO4`, `HNO3`, and its explanation is still the generic template sentence. |
| chunk 2 `EXP_19_4_09_SEMANTIC_FINAL_021` | Not ideal for mobile input. The answer `Fe(NO)SO₄` is deterministic and source-supported, but a formula fill blank is harder on phones and still carries ASCII accepted-answer text `Fe(NO)SO4`. Better as single choice. |
| chunk 2 `EXP_19_5_01_SEMANTIC_FINAL_027` | Mostly deterministic, but low-depth and still includes ASCII accepted-answer synonym `Fe3+`. It is usable only if accepted answers are hidden and normalization is intentional; stricter release standard should clean it. |
| chunk 3 `OLD_CHUNK3_EXP_19_8_01_Q021` | Source-supported but mobile-risky. Asking for `Pb(OH)₂` as a fill blank is deterministic, yet formula input on phone is fragile; strict mobile standard favors rewrite to single choice. |
| chunk 3 `OLD_CHUNK3_EXP_19_8_06_Q028` | Semantically supported by SnCl₂ reducing FeCl₃ to Fe(II), and accepted answer includes "亚铁", but it remains a low-depth multi-synonym fill blank. Keep only after explicit mobile-risk acceptance or rewrite. |
| chunk 4 `20-1-05` question index 18 | Not publishable as-is. Effective question is reasonable, but visible option-link diagnostic is English and contains ASCII `Na2SO3`: "Flame-color formation is unrelated to Na2SO3...". |
| chunk 4 `20-2-02` question index 17 | Not publishable as-is. The question is semantically supported, but option-link diagnostic is English and contains ASCII `H2O2`; visible metadata quality fails. |
| chunk 5 `CHK5_SEM_EXP_20_2_08_001` | Mechanically clean and source-supported. Quality is acceptable, though option-link diagnostics are still generic rather than evidence-specific. |
| chunk 5 `CHK5_SEM_EXP_20_3_02_001` | Mechanically clean and source-supported, but low-depth: it mainly asks which anion is an observation object. It can remain only as a basic recognition item. |

## Release Decision

Chunks 1-5 should not be imported/published yet as a fully release-ready bank.

Blocking reasons:

- chunk 1 still has 21 active effective questions with missing explanations, concentrated in `19-3-02`.
- chunk 1 still has many visible ASCII digit chemistry formulas in effective fields.
- chunk 4 still has English/ASCII option-link diagnostics in visible option-link text.
- chunk 2 and chunk 3 still contain formula-heavy fill blanks that are deterministic but mobile-hostile under the stricter standard.
- The OpenSpec requirement for full manual semantic rereview of all 2,303 active questions is not met; current progress is 8 / 111.

## Recommended Next Repair Order

1. Complete task 2.3 / 3.15 for `19-3-02` in chunk 1, including all missing explanations.
2. Complete task 2.4 formula normalization for chunk 1 effective displayed fields and visible option-link text.
3. Re-check the known spotcheck items in task 2.5.
4. Repair chunk 2/3/4 fill-blank mobile risks and chunk 4 English/ASCII option-link diagnostics.
5. Continue the full per-experiment manual rereview tasks until every active question is logged exactly once.
