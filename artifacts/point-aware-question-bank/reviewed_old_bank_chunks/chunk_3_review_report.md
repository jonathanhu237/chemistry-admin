# Chunk 3 Old Bank Review Report

## Scope

- Chunk: 3
- Experiment range: `19-6-02` to `20-1-01`
- Original questions reviewed: 450
- Reviewed artifact: `artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_3_reviewed_v1.json`

## Summary

- Keep: 418
- Rewrite: 32
- Reject: 0
- Replacement questions supplied: 32
- Question type counts after review: single_choice 153, true_false 150, fill_blank 147

## Rewrite Reasons

- `confusing_double_negative`: 21
- `outside_formal_video_point_scope`: 8
- `direct_concentration_recall`: 2
- `wrong_safety_polarity`: 1
- `mobile_fill_blank_too_complex`: 2

## Per-Experiment Counts

| Experiment | Title | Keep | Rewrite | Reject | Types | Points covered |
|---|---:|---:|---:|---:|---|---:|
| `19-6-02` | 金属镁燃烧 | 30 | 0 | 0 | fill_blank:10, single_choice:10, true_false:10 | 2 |
| `19-6-03` | 与水的作用 | 27 | 3 | 0 | fill_blank:10, single_choice:10, true_false:10 | 5 |
| `19-6-04` | 焰色反应 | 28 | 2 | 0 | fill_blank:10, single_choice:10, true_false:10 | 6 |
| `19-8-01` | Pb(OH)₂ 的生成与性质 | 27 | 3 | 0 | fill_blank:9, single_choice:11, true_false:10 | 3 |
| `19-8-02` | Sn(OH)₂ 的生成与性质 | 30 | 0 | 0 | fill_blank:10, single_choice:10, true_false:10 | 3 |
| `19-8-03` | Sb(OH)₃ 的生成与性质 | 29 | 1 | 0 | fill_blank:9, single_choice:11, true_false:10 | 4 |
| `19-8-04` | Bi(OH)₃ 的生成与性质 | 27 | 3 | 0 | fill_blank:10, single_choice:10, true_false:10 | 4 |
| `19-8-05` | Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性 | 28 | 2 | 0 | fill_blank:10, single_choice:10, true_false:10 | 4 |
| `19-8-06` | Sn(II) 的还原性 | 28 | 2 | 0 | fill_blank:10, single_choice:10, true_false:10 | 4 |
| `19-8-07` | Pb(IV) 的氧化性 | 30 | 0 | 0 | fill_blank:10, single_choice:10, true_false:10 | 3 |
| `19-8-08` | As(III)、Sb(III)、Bi(III) 的还原性 | 29 | 1 | 0 | fill_blank:9, single_choice:11, true_false:10 | 4 |
| `19-8-09` | As(V)、Sb(V)、Bi(V) 的氧化性 | 27 | 3 | 0 | fill_blank:10, single_choice:10, true_false:10 | 2 |
| `19-8-10` | Sn、Pb、Bi 不同价态离子的氧化还原性 | 28 | 2 | 0 | fill_blank:10, single_choice:10, true_false:10 | 3 |
| `19-8-11` | 小设计实验 | 21 | 9 | 0 | fill_blank:10, single_choice:10, true_false:10 | 3 |
| `20-1-01` | 氢氧化物的生成与性质 | 30 | 0 | 0 | fill_blank:10, single_choice:10, true_false:10 | 8 |

## Review Notes

- All 450 old-bank questions are preserved in `original_question`; rewritten items include a concrete `proposed_question`.
- Single-choice items now include option-level diagnostic links using `correct_evidence`, `adjacent_point`, `distractor_misconception`, or `unrelated_distractor`.
- Fill blanks kept in the reviewed payload use short deterministic answers; phone-unfriendly fill blanks were rewritten as single-choice items.
- Double-negative true/false stems were rewritten into positive assertions rather than silently kept.
- Items in `19-8-11` about Sb/Bi separation were rewritten back to the formal Pb₃O₄ video-point scope for this chunk.
- No database import, public-code update, or OpenSpec task update was performed.

## Point Coverage Observations

- `19-6-02` covers all 2 formal video point(s).
- `19-6-03` covers all 5 formal video point(s).
- `19-6-04` missing direct reviewed coverage for: PDF 备注：可考虑用网络视频或自制视频展示焰色反应
- `19-8-01` covers all 3 formal video point(s).
- `19-8-02` covers all 3 formal video point(s).
- `19-8-03` covers all 4 formal video point(s).
- `19-8-04` covers all 4 formal video point(s).
- `19-8-05` covers all 4 formal video point(s).
- `19-8-06` covers all 4 formal video point(s).
- `19-8-07` covers all 3 formal video point(s).
- `19-8-08` covers all 4 formal video point(s).
- `19-8-09` covers all 2 formal video point(s).
- `19-8-10` covers all 3 formal video point(s).
- `19-8-11` covers all 3 formal video point(s).
- `20-1-01` covers all 8 formal video point(s).
