# Final Question Bank Quality Spotcheck - after 19-1-03 closeout

Date: 2026-06-15

Scope: read-only spotcheck across `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`, after manual semantic repair of `19-1-03`.

Conclusion: not import-ready. The current release files still contain unresolved blocker classes: template diagnostics, visible ASCII chemistry formulas, formula-heavy/mobile-risk fill blanks, and unreviewed low-depth/semantic risks. This report is an inventory aid only; it does not replace per-question semantic rereview.

## Current Counts

| Chunk | Active | Missing explanations | Template/generic records | ASCII display records | ASCII option-link records | Mobile-risk fill blanks | Option-link label mismatch |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 443 | 0 | 210 | 102 | 83 | 11 | 0 |
| 2 | 450 | 0 | 9 | 30 | 36 | 15 | 0 |
| 3 | 450 | 0 | 29 | 0 | 0 | 70 | 0 |
| 4 | 450 | 0 | 9 | 4 | 11 | 17 | 0 |
| 5 | 510 | 0 | 63 | 2 | 2 | 0 | 0 |

## Sample Blockers

- Chunk 1: `CHUNK1_19_1_04_Q001`, `CHUNK1_19_1_04_Q002`, `CHUNK1_19_1_04_Q003`, `CHUNK1_19_1_04_Q004`, `CHUNK1_19_1_04_Q005`, `CHUNK1_19_1_04_Q006`.
- Chunk 2: `EXP_19_3_03_SEMANTIC_FINAL_030`, `EXP_19_3_04_SEMANTIC_FINAL_021`, `EXP_19_3_05_SEMANTIC_FINAL_022`, `EXP_19_3_06_SEMANTIC_FINAL_010`.
- Chunk 3: `OLD_CHUNK3_EXP_19_6_02_Q024`, `OLD_CHUNK3_EXP_19_6_03_Q021`, `EXP_19_6_04_fill_blank_01` through `EXP_19_6_04_fill_blank_07`.
- Chunk 4: several records without stable top-level review IDs were flagged as mobile-risk fill blanks; visible samples include `EXP_20_1_04_fill_blank_05`, `EXP_20_1_04_fill_blank_06`, `EXP_20_1_04_fill_blank_08`, `EXP_20_1_04_fill_blank_09`, `EXP_20_1_04_fill_blank_10`.
- Chunk 5: `CHK5_SEM_EXP_20_2_10_001` through `CHK5_SEM_EXP_20_2_10_013` show template/generic diagnostics.

## Notes

- The latest local gate for `19-1-03` is clean: 30 active questions, zero missing explanations, zero template/generic option-link diagnostics, zero visible ASCII formulas, zero option-link label mismatches, and zero unresolved formula-heavy mobile fill blanks.
- The full OpenSpec change `full-question-bank-semantic-release-repair` is still in progress: 13/121 tasks complete after marking `3.3` done.
- Next ordered task in the per-experiment rereview sequence is `3.4 Manually rereview and repair 19-1-04`.
