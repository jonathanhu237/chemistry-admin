# Final Question Bank Quality Spotcheck - 2026-06-15 after `19-3-02` closeout

## Scope

- Files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- OpenSpec change: `full-question-bank-semantic-release-repair`.
- OpenSpec progress at this checkpoint: 10 / 111 tasks complete.
- Method: scripts were used only for JSON parsing, risk inventory, and candidate selection. The quality judgments below come from manually reading sampled effective questions, options, answers, explanations, point bindings, option links, source audit fields, and the relevant experiment context already used by the repair spec.

## Release Decision

Chunks 1-5 are **not yet import-ready / publish-ready** under the current full-bank semantic-release standard.

Reason: the current spec explicitly requires full manual rereview and logged evidence for every active effective question. That work is not complete, and this spotcheck still finds blocker classes in the final release artifacts: visible ASCII digit chemistry formulas, formula-heavy mobile fill blanks, hidden-vs-visible accepted-answer alias risk, generic option-link diagnostics, low-depth recognition items without sufficient retained-risk reasoning, and traceability gaps in some records.

## Mechanical Inventory

| Chunk | Records scanned | Missing effective explanations | ASCII digit formula candidates | Mobile fill-blank candidates | Generic option-link candidates by scan | Top option mismatch candidates |
|---|---:|---:|---:|---:|---:|---:|
| chunk 1 | 450 | 0 | 274 | 0 | 0 | 0 |
| chunk 2 | 450 | 0 | 7 | 7 | 0 | 0 |
| chunk 3 | 450 | 0 | 3 | 0 | 0 | 0 |
| chunk 4 | 450 | 0 | 25 | 12 | 0 | 0 |
| chunk 5 | 510 | 0 | 0 | 0 | 0 | 0 |

Notes:

- The generic option-link scan undercounts template diagnostics because several templates use Chinese wording such as “该选项直接对应本题考查的实验操作、现象或结论。” Manual samples still found these.
- The ASCII formula scan is an inventory signal, not a final semantic decision. Each occurrence still requires manual confirmation before repair.

## Manual Samples

| Chunk | Sample | Manual result | Finding |
|---|---|---|---|
| 1 | `CHUNK1_19_1_01_Q010` | blocker | Effective stem/options still show `Cl2`, `Br2`, `CCl4`; option-link diagnostics still contain template wording such as “直接落在点位 / 能回答题干要求.” This violates formula-display and option-link standards. |
| 1 | `CHUNK1_19_3_02_Q020` | pass | Repaired item is source-supported and deterministic: SO₂ + H₂S generates sulfur; options and point binding match the H₂S oxidation-property point. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_030` | blocker | Fill blank expects `SO2/SO₂/二氧化硫`. It is short, but the visible stem asks for a formula/name alias and accepted answers include ASCII `SO2`; this needs hidden-alias logging or rewrite under the mobile/alias rule. |
| 2 | `EXP_19_4_09_SEMANTIC_FINAL_021` | blocker | Fill blank expects `Fe(NO)SO4 / Fe(NO)SO₄`, a formula-heavy mobile-hostile answer. The reviewer note says ASCII is for phone input, which conflicts with the spec’s default rewrite requirement. |
| 3 | `19-8-01` first sampled record | quality risk | Question is answerable, but option-link diagnostics include generic “该选项直接对应本题考查的实验操作、现象或结论.” Traceability also lacks stable `review_id` in sampled records. |
| 3 | `19-8-11` sampled records | quality risk | Questions are source-supported, but several are low-depth recognition items about formula/object/acid choice. They need concrete retained-risk reasons and non-template option-link diagnostics. |
| 4 | `20-1-02` sampled records | blocker | Several fill/choice records keep formula-heavy accepted aliases such as `NH3·H2O`, `CuSO4`, `AgNO3`, etc. The sampled option-link diagnostics remain template-like. |
| 4 | `20-1-05` sampled records | blocker | The questions are source-supported, but diagnostics such as “该选项直接对应...” / “该选项混淆...” are still template diagnostics. The chunk also has mobile fill candidates around CuCl₂ / Na₂SO₃ concentration and reagent names. |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | quality risk | Effective question is better than pure recall, but option-link diagnostics are still generic templates. |
| 5 | `CHK5_SEM_EXP_20_3_14_001/002` | quality risk | Source support is present, but items lean on recognition of ion set / KSCN reagent; retained low-depth justification and option-link diagnostics are not yet strong enough for the final standard. |

## Current Good News

- `19-3-02` in chunk 1 is now locally clean after manual repair:
  - 30 records checked.
  - 0 missing explanations.
  - 0 generic option-link diagnostics in the checked batch.
  - 0 visible ASCII digit formulas in effective fields or visible option-link text.
  - 0 option-link text mismatches.
  - 0 invalid point keys.
  - 0 duplicate effective stems.

## Blocker Classes Still Present

1. **Visible ASCII digit formulas**: especially chunk 1 `Cl2/Br2/CCl4` style display.
2. **Formula-heavy mobile fill blanks**: especially chunk 2 `Fe(NO)SO4`, `SO2`, `I2`, `NH4+`, and chunk 4 metal salt aliases.
3. **Accepted-answer alias visibility risk**: ASCII aliases may be useful as hidden deterministic grading synonyms, but they must not be treated as visible display text without manual logging.
4. **Generic option-link diagnostics**: especially chunks 3-5, where mechanical scans are clean but manual reading still finds reusable template explanations.
5. **Low-depth retained items**: recognition-only questions remain in chunks 3 and 5 without enough per-item retained-risk reasoning.
6. **Traceability gaps**: sampled chunk 3/4 records did not expose stable `review_id` in the same way chunk 1/2/5 records do, which weakens per-question audit mapping.

## Conclusion

Do not import or publish chunks 1-5 as a final bank yet. The current safe status is: OpenSpec artifacts are valid, `19-3-02` is closed as a clean manually rereviewed batch, but the full release set remains blocked until the remaining 101 OpenSpec tasks and final all-chunk QA checks are completed.
