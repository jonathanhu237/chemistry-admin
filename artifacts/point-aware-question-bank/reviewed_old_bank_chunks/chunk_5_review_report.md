# Chunk 5 Reviewed Old Bank Report

## Scope

- Chunk: 5
- Experiments: `20-2-08`, `20-2-09`, `20-2-10`, `20-3-01`, `20-3-02`, `20-3-03`, `20-3-04`, `20-3-05`, `20-3-06`, `20-3-07`, `20-3-08`, `20-3-09`, `20-3-10`, `20-3-11`, `20-3-12`, `20-3-13`, `20-3-14`
- Source bank: `E:\chemistry-rag\data\generated\experiment_question_bank_v1\experiment_question_bank_v1.json`
- Reviewed artifact: `artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_5_reviewed_v1.json`

## Summary

- Original questions: 510
- Keep: 442
- Rewrite: 68
- Reject: 0
- Replacement/proposed questions: 68
- Type distribution: single_choice 170, true_false 170, fill_blank 170
- Fill-blank rewrites: 40
- Multi-point bindings: 67
- Evidence insufficient: 0
- Items using supporting theory chunks: 391

## By Experiment

| Experiment | Title | Original | Keep | Rewrite | Reject | Fill rewrites | Multi-point |
|---|---:|---:|---:|---:|---:|---:|---:|
| `20-2-08` | 铬(III)盐的水解 | 30 | 26 | 4 | 0 | 4 | 0 |
| `20-2-09` | 钛(IV)盐的水解 | 30 | 23 | 7 | 0 | 4 | 0 |
| `20-2-10` | 小设计实验 | 30 | 26 | 4 | 0 | 1 | 0 |
| `20-3-01` | 水合阳离子颜色 | 30 | 28 | 2 | 0 | 0 | 0 |
| `20-3-02` | 阴离子颜色 | 30 | 27 | 3 | 0 | 3 | 1 |
| `20-3-03` | Cr(III) 的水合异构现象 | 30 | 27 | 3 | 0 | 3 | 9 |
| `20-3-04` | 观察不同配体的 Co(II) 配合物的颜色 | 30 | 23 | 7 | 0 | 4 | 8 |
| `20-3-05` | 氨合物 | 30 | 23 | 7 | 0 | 5 | 5 |
| `20-3-06` | 配合物的形成对氧化还原性的影响 | 30 | 27 | 3 | 0 | 0 | 10 |
| `20-3-07` | 配合物稳定性与配体的关系 | 30 | 30 | 0 | 0 | 0 | 6 |
| `20-3-08` | 铁的鉴定 | 30 | 29 | 1 | 0 | 1 | 2 |
| `20-3-09` | 钴(II)的鉴定 | 30 | 21 | 9 | 0 | 5 | 0 |
| `20-3-10` | 镍(II)的鉴定 | 30 | 27 | 3 | 0 | 1 | 2 |
| `20-3-11` | 铬(III)的鉴定 | 30 | 25 | 5 | 0 | 2 | 13 |
| `20-3-12` | 钛(IV)的鉴定 | 30 | 26 | 4 | 0 | 4 | 2 |
| `20-3-13` | 钒(V)的鉴定 | 30 | 28 | 2 | 0 | 2 | 9 |
| `20-3-14` | 小设计实验 | 30 | 26 | 4 | 0 | 1 | 0 |

## Rewrite Categories

- `shallow_reagent_or_formula_fill_blank`: 29
- `awkward_true_false_double_negative`: 25
- `mobile_unfriendly_fill_blank`: 15
- `metadata_recall_not_point_diagnostic`: 5

## Review Notes

- All reviewed items preserve the full `original_question` object and add point bindings, option diagnostics, and source audit notes.
- `rewrite` was used instead of `reject` when the old item had a salvageable idea but was too shallow, awkward, or unsuitable for mobile fill-blank input.
- Exact colors, precipitates, valence, and complex-formation explanations are cited with supporting theory chunks where the canonical experiment chunk only gives the operation/observation task.
- No database import was performed. No public code or OpenSpec task files were changed.

## Evidence Or Main-Thread Review

- Evidence-insufficient items: 0.
- Suggested main-thread spot checks: exact color claims in `20-3-01`/`20-3-02` and kept direct-recall items flagged `basic_direct_recall`, if the final production bank wants a stricter depth bar.
