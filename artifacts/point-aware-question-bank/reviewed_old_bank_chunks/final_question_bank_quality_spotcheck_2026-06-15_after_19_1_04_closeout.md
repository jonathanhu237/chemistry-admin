# Final Question Bank Quality Spotcheck - 2026-06-15 after 19-1-04 closeout

## Scope

- Spotcheck target: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- OpenSpec change: `full-question-bank-semantic-release-repair`.
- Current OpenSpec progress after this closeout: 14/121 tasks complete, 107 remaining.
- Newly closed batch: `19-1-04` in chunk 1, task `3.4`.

## Closeout Status

- `19-1-04` local hand-repair gate: 30 active questions, 0 missing effective explanations, 0 template option diagnostics, 0 option-link text mismatches, 0 invalid point keys.
- `openspec validate full-question-bank-semantic-release-repair --strict`: passed.
- The OpenSpec change is not archive-ready. Most full-bank manual rereview tasks remain pending, so chunks 1-5 cannot yet be declared fully import-ready.

## Inventory Scan

The following counts are inventory/navigation gates only. They do not replace semantic review, but they identify blocker classes still present in the final release artifacts.

| Chunk | Active questions | Missing explanations | Template/generic explanations | Option-link mismatches | Generic option diagnostics | Visible ASCII formula/ion hits | ASCII formula/ion in option links | Fill mobile/symbol risk | ASCII accepted-answer aliases | Invalid point keys |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 450 | 0 | 87 | 2 | 168 | 57 | 38 | 11 | 11 | 0 |
| 2 | 450 | 0 | 37 | 0 | 0 | 0 | 0 | 14 | 15 | 0 |
| 3 | 450 | 0 | 52 | 0 | 0 | 0 | 0 | 68 | 70 | 0 |
| 4 | 450 | 0 | 96 | 0 | 0 | 0 | 3 | 17 | 18 | 0 |
| 5 | 510 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Manual Sample Findings

| Chunk | Sample | Manual quality judgment |
|---|---|---|
| 1 | `CHUNK1_19_1_06_Q012` | Not import-ready. The effective stem uses `KClO3`, `CCl4`, `H2SO4`, `HNO3` instead of Unicode formula display; explanation is a generic template; option links contain template diagnostics and `K+`/`CCl4` visible text. Semantics are plausible, but presentation and diagnostics fail the final standard. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_030` | Not import-ready as-is. The fill blank asks for `SO₂/二氧化硫` and retains `SO2` as an accepted answer; explanation is only “对应的实验操作或现象内容是...”. This should be rewritten to deterministic single choice or retain only with Chinese-first display and logged hidden alias. |
| 3 | `OLD_CHUNK3_EXP_19_8_01_Q021` | Low-depth/mobile risk. The item asks students to fill `Pb(OH)₂` for a precipitate name, keeps a symbolic accepted answer, and uses a template explanation. It is source-supported but should be rewritten toward operation/phenomenon reasoning or justified as a necessary prerequisite. |
| 4 | `CHUNK4_20-1-02_IDX021` | Not final-quality yet. The answer includes `NH3·H2O` as an ASCII hidden alias and the explanation is generic. The item may be retained as a reagent prerequisite only after Chinese-first display, hidden-alias logging, and a concrete explanation tied to ammonia-water addition. |
| 5 | `CHK5_SEM_EXP_20_3_06_025` | Mechanically clean but semantically thin. It asks for the short term “电势/电极电势” and relies on supporting theory about EDTA complexing Fe³⁺ and changing the Fe³⁺/Fe²⁺ couple. It can likely be retained, but needs a concrete theory-dependent explanation instead of the current template sentence. |

## Release Decision

Chunks 1-5 are not yet safe to import and publish as a whole.

The newly repaired `19-1-04` batch is locally clean, but the all-chunk spotcheck still finds release blockers in every chunk: template explanations, unresolved formula/mobile fill blanks, ASCII accepted-answer aliases that are not fully logged, chunk 1 option-link mismatches, and residual visible ASCII chemistry notation. Continue the OpenSpec full-bank semantic repair rather than closing or archiving the change.
