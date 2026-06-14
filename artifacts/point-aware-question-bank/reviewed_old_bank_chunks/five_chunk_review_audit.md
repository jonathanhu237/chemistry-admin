# Five-Chunk Reviewed Old Bank Audit

Generated after reviewing the five reviewed old-bank chunks for `regenerate-point-aware-question-bank`.

## Scope

- Source old bank: `E:/chemistry-rag/data/generated/experiment_question_bank_v1/experiment_question_bank_v1.json`
- Reviewed artifacts:
  - `chunk_1_reviewed_v1.json`
  - `chunk_2_reviewed_v1.json`
  - `chunk_3_reviewed_v1.json`
  - `chunk_4_reviewed_v1.json`
  - `chunk_5_reviewed_v1.json`

## Result

- Original-question coverage: `2310/2310`, no missing and no extra reviewed source questions.
- Reviewed chunk structure: `0` hard errors after audit.
- Backend payload validation: `2310/2310` passed through `server.app.experiment_admin._validate_question_payload`.
- Phone-friendly fill blanks: `667` effective fill-blank questions, `0` without at least one easy accepted answer.
- OpenSpec validation: `openspec validate regenerate-point-aware-question-bank --strict` passed.
- Validator syntax check: `python -m py_compile scripts/point_aware_question_bank.py` passed.

## Chunk Summary

| Chunk | Experiments | Questions | Keep | Rewrite | Reject | Effective Types |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 15 | 450 | 342 | 102 | 6 | 216 single choice, 128 true/false, 106 fill blank |
| 2 | 15 | 450 | 284 | 166 | 0 | 150 single choice, 150 true/false, 150 fill blank |
| 3 | 15 | 450 | 418 | 32 | 0 | 153 single choice, 150 true/false, 147 fill blank |
| 4 | 15 | 450 | 402 | 48 | 0 | 170 single choice, 146 true/false, 134 fill blank |
| 5 | 17 | 510 | 442 | 68 | 0 | 210 single choice, 170 true/false, 130 fill blank |

## Corrections Made During Audit

- Rewrote `chunk_3` / `19-8-03` / question 30 from a phone-unfriendly fill blank requiring `AgNO3 + NaCl` into a single-choice point-match question.
- Added easier accepted answers `正一价` and `一价` to `chunk_4` / `20-1-07` / question 26.
- Added `adjacent_experiment` to the allowed option-link role set because chunk 5 uses it for adjacent-experiment distractors.

## Remaining Work

- Merge the five reviewed chunks into one reviewed old-bank artifact.
- Run the final merged-artifact validator and produce the publication/import report.
