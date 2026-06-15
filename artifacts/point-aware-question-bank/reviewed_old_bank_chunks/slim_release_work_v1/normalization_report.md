# Slim Release Normalization Report

This is a mechanical normalization report. It does not certify semantic quality.

Output directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1`

Evidence policy: canonical RAG source text is not copied into these files; work packets carry locators for `E:/chemistry-rag/data/rag_ready`.

## Chunk Summary

| Chunk | Experiments | Questions | Source size | Slim size | Type counts | Effective source counts |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| 1 | 15 | 450 | 2771109 B | 1500292 B | fill_blank=51, single_choice=270, true_false=129 | original_question=291, proposed_question=159 |
| 2 | 15 | 450 | 2989851 B | 1733166 B | fill_blank=64, single_choice=271, true_false=115 | original_question=178, proposed_question=272 |
| 3 | 15 | 450 | 2399851 B | 1547383 B | fill_blank=133, single_choice=164, true_false=153 | original_question=401, proposed_question=49 |
| 4 | 15 | 450 | 2336072 B | 1550500 B | fill_blank=125, single_choice=218, true_false=107 | original_question=275, proposed_question=175 |
| 5 | 17 | 510 | 2590394 B | 1845407 B | fill_blank=35, single_choice=322, true_false=153 | original_question=316, proposed_question=194 |

## Totals

- Experiments: `77`
- Questions: `2310`

## Mechanical Risk Flags

| Flag | Count |
| --- | ---: |
| ascii_formula_like_visible_text | 841 |
| english_option_link_diagnostic | 13 |
| formula_or_symbolic_fill_blank_answer | 108 |
| generic_or_answer_shell_explanation | 322 |
| multi_point_binding | 852 |
| old_or_inherited_audit_language | 1852 |
| template_option_link_diagnostic | 144 |
| uses_supporting_theory | 1008 |

## Files

- `chunk_X_release_slim_v1.json`: normalized slim per-chunk work files.
- `semantic_work_packets/chunk_X/<experiment_code>.json`: one experiment per file for Codex manual repair.
- `manifest.json`: generated file list and counts.

## Notes

- Original `chunk_X_release_final_v1.json` files were not overwritten.
- Historical review fields are reduced to minimal lineage snapshots.
- RAG evidence is represented by source file paths, chunk ids, line numbers, section paths, and search hints only.
- `mechanical_risk_flags` are locator flags only; they are not semantic decisions.
