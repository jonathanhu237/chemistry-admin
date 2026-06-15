# Final Question Bank Quality Spotcheck - after `19-1-08` stage wrap-up

Date: 2026-06-15

Scope: current release JSON files for chunks 1-5 after completing the manual semantic repair of chunk 1 batch `19-1-08`.

Conclusion: chunks 1-5 are not ready for import or publication as a final bank. Chunk 1 batch `19-1-08` now passes its local stage gate, but the full five-chunk bank still has unresolved release blockers in chunks 2-5 and remaining unrepaired blocker inventories in the OpenSpec change.

OpenSpec status at this checkpoint: `full-question-bank-semantic-release-repair` is 19/167 tasks complete, with 148 tasks remaining. This report is a stage checkpoint, not a spec archive or final release approval.

## Mechanical Validation

Read-only validation:

- `chunk_1_release_final_v1.json`: parses
- `chunk_2_release_final_v1.json`: parses
- `chunk_3_release_final_v1.json`: parses
- `chunk_4_release_final_v1.json`: parses
- `chunk_5_release_final_v1.json`: parses

Read-only schema-aware risk scan over active-like release records found unresolved blocker inventory:

- Template option-link diagnostics still present: `direct_corresponds` 696 records, `mixes_experiment` 282 records, `other_experiment` 289 records, `lands_on_point` 69 records, `answers_stem` 69 records, `not_match` 692 records. Counts overlap by record and are blocker inventory, not semantic decisions.
- Generic effective explanations: 365 records.
- Symbolic or formula-heavy fill blanks: 111 records.
- Visible ASCII formula hits in effective displayed fields: 40 records.

## Manual Sample Result

Manual sample size: 15 questions across chunks 1-5.

Result: 7 pass, 2 conditional, 6 fail.

| Chunk | Question ID | Result | Manual judgement |
|---|---|---|---|
| 1 | `CHUNK1_19_1_01_Q025` | PASS | Rewritten into a concrete displacement-operation evidence chain. Points and option diagnostics are specific. |
| 1 | `CHUNK1_19_1_08_Q002` | PASS | Rewritten from filter-paper name recall into purpose of carrying precipitate for key-shielding observation. |
| 1 | `CHUNK1_19_1_08_Q029` | PASS | Rewritten from title-word fill blank into conclusion single choice based on the observed key outline. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_025` | CONDITIONAL | Short color fill blank `紫` is phone-safe and logged as a low-depth observation anchor, but it remains a weak item. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_030` | FAIL | Effective fill blank still accepts visible `SO2`/`SO₂`/`二氧化硫`; explanation is generic. Needs semantic rewrite to deterministic single choice or hidden alias handling. |
| 2 | `EXP_19_4_09_SEMANTIC_FINAL_021` | FAIL | Effective fill blank asks for `Fe(NO)SO4`/`Fe(NO)SO₄`; this is mobile-hostile formula input with generic explanation. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q001` | PASS | Good operation-plus-observation item for magnesium burning. Multi-point binding is valid. |
| 3 | `OLD_CHUNK3_EXP_19_8_01_Q001` | FAIL | Low-depth reagent recall (`NaOH`), terse explanation, and template option diagnostics remain. Wrong options also carry the same point key instead of null. |
| 3 | `OLD_CHUNK3_EXP_19_8_11_Q001` | FAIL | Low-depth object/formula recall (`Pb₃O₄`) with template diagnostics. Theory support is broader than the actual object-name question needs. |
| 4 | `REV_CH4_EXP_20_1_02_Q001` | PASS | Good observation-chain rewrite for CuSO₄ + NH₃·H₂O: precipitate formation and dissolution are both required. |
| 4 | `REV_CH4_EXP_20_1_02_Q021` | PASS | Good rewrite from reagent-source recall into AgNO₃ + NH₃·H₂O over-ammonia dissolution evidence. |
| 4 | `REV_CH4_EXP_20_1_02_Q022` | FAIL | Still a low-depth fill blank asking for `硫酸铜` with visible `CuSO4`/`CuSO₄` aliases and generic explanation. |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | PASS | Concrete operation item for Cr₂(SO₄)₃ + Na₂CO₃ waterlysis observation; diagnostics are specific. |
| 5 | `CHK5_SEM_EXP_20_3_01_002` | CONDITIONAL | Better than the original risk case, but broad multi-point binding and option-link point assignment still need final audit. |
| 5 | `CHK5_SEM_EXP_20_3_14_026` | FAIL | Generic shell stem remains: “哪项判断与实验操作、现象或结论一致”. Option diagnostics are still template-level. |

## Quality Decision

The final bank should not be imported yet.

Blocking reasons:

- Formula-heavy fill blanks remain visible and phone-hostile.
- Generic explanations and template option-link diagnostics remain at scale.
- Several sampled records still test reagent/formula/object recall instead of operation, observation, comparison, or reasoning.
- Some option links still use template wording or incorrect point assignments.
- OpenSpec full-bank release tasks are not close to complete.

Local positive result:

- Chunk 1 batch `19-1-08` now has 27 active publishable records and 3 rejected records, with no active template option diagnostics in that batch, no generic answer-only explanations, four retained phone-safe short Chinese fill blanks, and explicit theory dependency only for metallic-silver mechanism questions.

Required next action:

Continue the OpenSpec repair sequence before any release approval. The next highest-value work is to repair chunk 2 and chunk 3 formula/mobile-risk fill blanks and chunk 3/5 template option-link diagnostics, then rerun a five-chunk sample only after those blocker classes are actually resolved.
