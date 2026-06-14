# Chunk 4 Reviewed Old Bank Report

## Scope

- Chunk: 4
- Experiment range: `20-1-02` to `20-2-07`
- Original questions reviewed: 450
- Output artifact: `artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_4_reviewed_v1.json`

## Summary Counts

- keep: 402
- rewrite: 48
- reject: 0
- replacement questions: 48
- multi-point bindings: 213
- fill_blank rewrites: 16

## Original Type Distribution

- single_choice: 150
- true_false: 150
- fill_blank: 150

## Per-Experiment Counts

| Experiment | Title | Total | Keep | Rewrite | Reject | Fill Rewrite |
|---|---|---:|---:|---:|---:|---:|
| `20-1-02` | 氨合物 | 30 | 30 | 0 | 0 | 0 |
| `20-1-03` | 其他配体的配合物 | 30 | 26 | 4 | 0 | 2 |
| `20-1-04` | 碘化亚铜的形成 | 30 | 29 | 1 | 0 | 0 |
| `20-1-05` | 氯化亚铜的形成和性质 | 30 | 26 | 4 | 0 | 1 |
| `20-1-06` | 氧化亚铜的形成和性质 | 30 | 30 | 0 | 0 | 0 |
| `20-1-07` | Hg²⁺ 转化为 Hg₂²⁺ | 30 | 30 | 0 | 0 | 0 |
| `20-1-08` | 汞(I)的歧化分解 | 30 | 28 | 2 | 0 | 0 |
| `20-1-09` | 小设计实验 | 30 | 14 | 16 | 0 | 6 |
| `20-2-01` | 氢氧化物的酸碱性 | 30 | 26 | 4 | 0 | 1 |
| `20-2-02` | 铁(II)、钴(II)和镍(II)的还原性 | 30 | 30 | 0 | 0 | 0 |
| `20-2-03` | 铁(III)、钴(III)和镍(III)的氧化性 | 30 | 29 | 1 | 0 | 1 |
| `20-2-04` | 锰化合物的氧化还原性 | 30 | 27 | 3 | 0 | 0 |
| `20-2-05` | 铬、钼、钨化合物的氧化还原性 | 30 | 28 | 2 | 0 | 0 |
| `20-2-06` | 钛、钒的氧化还原性 | 30 | 22 | 8 | 0 | 4 |
| `20-2-07` | 铁(III)盐的水解 | 30 | 27 | 3 | 0 | 1 |

## Main Rewrite Reasons

- `double_negative_true_false`: 21
- `design_scheme_overreach`: 13
- `unsupported_specific_color_sequence`: 5
- `non_phone_friendly_fill_blank`: 4
- `unsupported_specific_color_observation`: 3
- `meta_catalog_label`: 2

## Evidence And Review Notes

- Evidence-insufficient accepted items: 0. Items with weak or overly specific original evidence were rewritten with `proposed_question`.
- No `reject` items were necessary because each problematic old item had a source-grounded replacement path.
- Source support is split into `canonical_chunk_ids` for experiment procedure evidence and `supporting_theory_chunk_ids` for product identity, color, oxidation-state, hydrolysis, or coordination-theory claims.
- Retained low-depth direct-recall items are flagged as `basic_direct_recall`; they were kept only when the answer was exact, source-supported, and useful for old-bank coverage.
- Rewritten design-scheme items in `20-1-09` avoid asserting a unique separation scheme when the canonical experiment only asks students to design one.
- Rewritten exact-color items in `20-2-06` and `20-2-07` avoid claims not explicitly listed in the canonical experiment chunk while preserving the observation target.

## Validation

- JSON parsed successfully after write.
- Required reviewed-item keys are present for all 450 items.
- All `rewrite` items include `proposed_question`.
- All single-choice original/proposed questions include option links for every option label.
- All point keys used in reviewed items belong to their formal experiment in `formal_experiment_point_inventory.json`.
