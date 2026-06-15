# Chunk 1-5 Final Tail-Fix Quality Gate

Date: 2026-06-15

## Scope

- Rebuilt package root: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages`
- Chunks checked: `chunk_1` through `chunk_5`
- Total rebuilt packages: 77
- Total questions: 2310
- Release-final files were not modified.

## Tail Fixes Applied

Five known tail issues were repaired directly in rebuilt packages:

- `chunk_1 / 19-1-02 / CHUNK1_19_1_02_Q002`: replaced `candidate-1` wording in `option_links[].diagnostic_note` with natural experiment-step wording.
- `chunk_1 / 19-1-02 / CHUNK1_19_1_02_Q003`: replaced `candidate-2` wording in `option_links[].diagnostic_note` with natural experiment-step wording.
- `chunk_1 / 19-1-03 / CHUNK1_19_1_03_Q003`: replaced `candidate-1` wording in `option_links[].diagnostic_note` with natural experiment-step wording.
- `chunk_3 / 19-8-01 / REBUILT_CH3_19_8_01_Q008`: changed the generic stem to `铅的氢氧化物酸碱性实验主要通过哪组操作体现？`
- `chunk_4 / 20-1-05 / REV_CH4_EXP_20_1_05_Q009`: changed the generic stem to `氯化亚铜形成及性质试验的核心实验目的是什么？`

No answers, point keys, or source-audit evidence ids were changed.

## Full Read-Only Validation After Tail Fix

| Gate | Result |
|---|---:|
| JSON parse errors | 0 |
| Packet size errors | 0 |
| Duplicate question ids within chunk | 0 |
| Missing package-level RAG ids | 0 |
| Missing question-level RAG ids | 0 |
| `evidence_sufficient=false` | 0 |
| Single-choice answer not in options | 0 |
| Single-choice option-link count mismatch | 0 |
| Single-choice option-link label mismatch | 0 |
| Student-visible raw id / backtick | 0 |
| Student-visible ASCII digit chemistry formula | 0 |
| Student-visible ASCII charge notation | 0 |
| Student-visible ASCII Roman valence | 0 |
| Student-visible LaTeX/caret notation | 0 |
| Student-visible abnormal Chinese spacing | 0 |
| Student-visible review/meta wording | 0 |
| Student-visible ASCII process terms | 0 |
| `option_links[].diagnostic_note` internal process terms | 0 |
| Duplicate primary/secondary point keys | 0 |
| Exact duplicate stems | 0 |

## Guarantee Boundary

This gate proves that the known blocker classes discovered in the latest rounds are now absent across all 2310 rebuilt questions:

- visible raw evidence ids;
- visible ASCII formula / charge / Roman-valence display;
- abnormal Chinese spacing;
- visible question-bank review wording;
- diagnostic-note internal process wording;
- exact duplicate stems;
- duplicate primary/secondary point bindings;
- structure and RAG-id failures.

It does not, by itself, prove that every possible chemistry-semantic issue is impossible. That level of certainty requires final manual QA after the merge into `chunk_X_release_final_v1.json`, because merge logic can introduce schema drift or expose metadata differently.

## Release Readiness

The rebuilt packages are now suitable to enter the merge stage.

Do not import yet. The next required step is a separate merge task:

1. merge rebuilt packages into `chunk_X_release_final_v1.json`, one chunk at a time;
2. run the same full quality gate on the merged release-final files;
3. manually resample merged output, including the previously failed seed records;
4. only then declare import-ready.
