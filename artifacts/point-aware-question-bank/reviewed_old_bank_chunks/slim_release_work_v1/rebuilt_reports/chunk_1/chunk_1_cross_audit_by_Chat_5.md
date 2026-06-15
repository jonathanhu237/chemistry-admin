# chunk_1 cross audit by Chat 5

## Audit Metadata

- Audit chunk: `chunk_1`
- Reviewer chat: `Chat 5`
- Audit time: `2026-06-15 19:07:11 +08:00`
- Target directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_1`
- Evidence sources:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Mode: read-only cross-audit of rebuilt JSON content. No JSON or release file was edited.

## Coverage

- Total packets: 15
- Total questions in chunk: 450
- Actually audited questions: 68
- Per-packet coverage: every packet has at least 3 audited questions.
- Question-type coverage: 27 `single_choice`, 15 `true_false`, 26 `fill_blank`
- Supporting-theory coverage: 38 audited questions use `supporting_theory_required=true` or cite supporting theory ids.
- Multi-point coverage: 42 audited questions bind more than one primary/secondary point.
- Required seed coverage: all 6 required chunk_1 seed questions were read directly from rebuilt JSON.

Auxiliary full-chunk scans were also run for student-visible review language, raw ids, diagnostic internal terms, display notation, structural consistency, and exact RAG id presence. Semantic judgments below are based on direct question reading, not only report text.

## Audited Question List

| experiment_code | question_id | question_type | conclusion |
|---|---|---|---|
| 19-1-01 | CHUNK1_19_1_01_Q013 | true_false | PASS |
| 19-1-01 | CHUNK1_19_1_01_Q021 | single_choice | P2_MINOR |
| 19-1-01 | CHUNK1_19_1_01_Q022 | single_choice | P2_MINOR |
| 19-1-01 | CHUNK1_19_1_01_Q027 | single_choice | PASS |
| 19-1-01 | CHUNK1_19_1_01_Q030 | fill_blank | PASS |
| 19-1-02 | CHUNK1_19_1_02_Q002 | single_choice | PASS |
| 19-1-02 | CHUNK1_19_1_02_Q003 | single_choice | PASS |
| 19-1-02 | CHUNK1_19_1_02_Q007 | single_choice | P2_MINOR |
| 19-1-02 | CHUNK1_19_1_02_Q014 | true_false | PASS |
| 19-1-02 | CHUNK1_19_1_02_Q024 | fill_blank | PASS |
| 19-1-03 | CHUNK1_19_1_03_Q003 | single_choice | PASS |
| 19-1-03 | CHUNK1_19_1_03_Q011 | true_false | PASS |
| 19-1-03 | CHUNK1_19_1_03_Q023 | single_choice | PASS |
| 19-1-03 | CHUNK1_19_1_03_Q024 | fill_blank | PASS |
| 19-1-03 | CHUNK1_19_1_03_Q025 | fill_blank | PASS |
| 19-1-04 | CHUNK1_19_1_04_Q011 | true_false | PASS |
| 19-1-04 | CHUNK1_19_1_04_Q022 | fill_blank | PASS |
| 19-1-04 | CHUNK1_19_1_04_Q024 | single_choice | PASS |
| 19-1-04 | CHUNK1_19_1_04_Q025 | fill_blank | PASS |
| 19-1-04 | CHUNK1_19_1_04_Q030 | single_choice | PASS |
| 19-1-05 | CHUNK1_19_1_05_Q002 | single_choice | PASS |
| 19-1-05 | CHUNK1_19_1_05_Q003 | single_choice | PASS |
| 19-1-05 | CHUNK1_19_1_05_Q010 | single_choice | PASS |
| 19-1-05 | CHUNK1_19_1_05_Q017 | true_false | P0_BLOCKER |
| 19-1-05 | CHUNK1_19_1_05_Q027 | fill_blank | PASS |
| 19-1-06 | CHUNK1_19_1_06_Q011 | single_choice | PASS |
| 19-1-06 | CHUNK1_19_1_06_Q019 | true_false | PASS |
| 19-1-06 | CHUNK1_19_1_06_Q023 | single_choice | PASS |
| 19-1-07 | CHUNK1_19_1_07_Q003 | single_choice | PASS |
| 19-1-07 | CHUNK1_19_1_07_Q009 | single_choice | P2_MINOR |
| 19-1-07 | CHUNK1_19_1_07_Q013 | true_false | PASS |
| 19-1-07 | CHUNK1_19_1_07_Q018 | true_false | PASS |
| 19-1-08 | CHUNK1_19_1_08_Q005 | single_choice | PASS |
| 19-1-08 | CHUNK1_19_1_08_Q011 | true_false | PASS |
| 19-1-08 | CHUNK1_19_1_08_Q016 | single_choice | PASS |
| 19-1-08 | CHUNK1_19_1_08_Q022 | single_choice | PASS |
| 19-1-08 | CHUNK1_19_1_08_Q024 | fill_blank | PASS |
| 19-2-01 | CHUNK1_19_2_01_Q022 | fill_blank | PASS |
| 19-2-01 | CHUNK1_19_2_01_Q025 | fill_blank | PASS |
| 19-2-01 | CHUNK1_19_2_01_Q027 | single_choice | PASS |
| 19-2-02 | CHUNK1_19_2_02_Q020 | true_false | PASS |
| 19-2-02 | CHUNK1_19_2_02_Q022 | fill_blank | PASS |
| 19-2-02 | CHUNK1_19_2_02_Q027 | fill_blank | PASS |
| 19-2-02 | CHUNK1_19_2_02_Q028 | fill_blank | PASS |
| 19-2-03 | CHUNK1_19_2_03_Q012 | true_false | PASS |
| 19-2-03 | CHUNK1_19_2_03_Q015 | true_false | PASS |
| 19-2-03 | CHUNK1_19_2_03_Q022 | fill_blank | PASS |
| 19-2-03 | CHUNK1_19_2_03_Q026 | fill_blank | PASS |
| 19-2-03 | CHUNK1_19_2_03_Q030 | single_choice | PASS |
| 19-2-04 | CHUNK1_19_2_04_Q004 | single_choice | PASS |
| 19-2-04 | CHUNK1_19_2_04_Q015 | true_false | PASS |
| 19-2-04 | CHUNK1_19_2_04_Q026 | single_choice | PASS |
| 19-2-04 | CHUNK1_19_2_04_Q027 | fill_blank | PASS |
| 19-2-04 | CHUNK1_19_2_04_Q030 | fill_blank | PASS |
| 19-2-05 | CHUNK1_19_2_05_Q011 | true_false | PASS |
| 19-2-05 | CHUNK1_19_2_05_Q021 | fill_blank | PASS |
| 19-2-05 | CHUNK1_19_2_05_Q027 | single_choice | PASS |
| 19-2-05 | CHUNK1_19_2_05_Q028 | fill_blank | PASS |
| 19-2-05 | CHUNK1_19_2_05_Q030 | single_choice | PASS |
| 19-3-01 | CHUNK1_19_3_01_Q022 | fill_blank | PASS |
| 19-3-01 | CHUNK1_19_3_01_Q024 | fill_blank | PASS |
| 19-3-01 | CHUNK1_19_3_01_Q027 | fill_blank | PASS |
| 19-3-02 | CHUNK1_19_3_02_Q016 | true_false | PASS |
| 19-3-02 | CHUNK1_19_3_02_Q024 | fill_blank | PASS |
| 19-3-02 | CHUNK1_19_3_02_Q025 | fill_blank | PASS |
| 19-3-02 | CHUNK1_19_3_02_Q026 | fill_blank | PASS |
| 19-3-02 | CHUNK1_19_3_02_Q027 | single_choice | PASS |
| 19-3-02 | CHUNK1_19_3_02_Q030 | single_choice | PASS |

## Findings

### P0_BLOCKER

| question_id | issue field | problem text | why it blocks import | suggested handling |
|---|---|---|---|---|
| CHUNK1_19_1_05_Q017 | `explanation` | `该判断可保留。教材理论说明 ClO- 氧化性较强，实验则用三条支路观察 NaClO 的氧化性表现。` | The explanation exposes review/disposition language (`该判断可保留`) to students. It also contains ASCII ion notation `ClO-`. Student-facing review language is a publish/import blocker. | Rewrite explanation as chemistry only, e.g. explain that hypochlorite can oxidize I⁻/Mn²⁺ or bleach fuchsin, and display hypochlorite as `ClO⁻` if mentioned. |

### P2_MINOR

| question_id | issue field | problem text | why it matters | suggested handling |
|---|---|---|---|---|
| CHUNK1_19_1_07_Q009 | `options[D].text` | `淀粉直接沉淀 ClO-` | Visible chemistry display uses ASCII ion notation. The answer remains deterministic and option D is clearly wrong, so this is minor display polish rather than a scoring blocker. | Change `ClO-` to `ClO⁻`. |
| CHUNK1_19_1_01_Q021 | `option_links[].diagnostic_note` | Examples include `这个点位直接对应 Cl₂ 与 Br₂。` and `只问 Cl₂ 与 Br₂ 时不需要把三个点位都作为 primary。` | `option_links` are internal, but this audit requires diagnostic notes to be natural and free of internal terms. | Replace `点位/primary` with student-facing experiment terms such as `这组操作` and `主要依据`. |
| CHUNK1_19_1_01_Q022 | `option_links[].diagnostic_note` | Examples include `该点位直接比较 Br₂ 与 I₂。` | Same `点位` leakage in internal diagnostic note. | Replace with `这组操作直接比较 Br₂ 与 I₂。` |
| CHUNK1_19_1_02_Q007 | `option_links[].diagnostic_note` | `两组点位均采用三种卤素水分别与同类试剂反应的横向比较。` | Same `点位` leakage in internal diagnostic note. | Replace with `两组实验均采用...` |

## Special Risk Lists

### Student-visible review-language hits

- `CHUNK1_19_1_05_Q017`: `explanation` contains `该判断可保留。`

### Evidence insufficient

- None found in audited questions. Exact `chunk_id` checks were used to avoid false positives from `prev_chunk_id` / `next_chunk_id` matches. The 33 unique evidence ids cited by audited questions were found in the RAG source files.

### Point binding issues

- None found in audited questions. Multi-point questions checked in the sample genuinely cross operations, observations, comparisons, or conclusions.

### Option_links issues

- P2 internal diagnostic wording appears in 41 questions across `19-1-01` through `19-1-04`; 57 diagnostic-note occurrences contain terms such as `点位`, `本点位`, `primary`, or `题干`.
- Affected question IDs: `CHUNK1_19_1_01_Q001`, `CHUNK1_19_1_01_Q002`, `CHUNK1_19_1_01_Q003`, `CHUNK1_19_1_01_Q004`, `CHUNK1_19_1_01_Q005`, `CHUNK1_19_1_01_Q006`, `CHUNK1_19_1_01_Q007`, `CHUNK1_19_1_01_Q008`, `CHUNK1_19_1_01_Q009`, `CHUNK1_19_1_01_Q021`, `CHUNK1_19_1_01_Q022`, `CHUNK1_19_1_01_Q024`, `CHUNK1_19_1_01_Q025`, `CHUNK1_19_1_01_Q029`, `CHUNK1_19_1_02_Q001`, `CHUNK1_19_1_02_Q004`, `CHUNK1_19_1_02_Q006`, `CHUNK1_19_1_02_Q007`, `CHUNK1_19_1_02_Q008`, `CHUNK1_19_1_02_Q009`, `CHUNK1_19_1_02_Q010`, `CHUNK1_19_1_02_Q021`, `CHUNK1_19_1_02_Q022`, `CHUNK1_19_1_02_Q023`, `CHUNK1_19_1_02_Q026`, `CHUNK1_19_1_02_Q027`, `CHUNK1_19_1_02_Q028`, `CHUNK1_19_1_02_Q030`, `CHUNK1_19_1_03_Q001`, `CHUNK1_19_1_03_Q002`, `CHUNK1_19_1_03_Q004`, `CHUNK1_19_1_03_Q007`, `CHUNK1_19_1_03_Q021`, `CHUNK1_19_1_03_Q022`, `CHUNK1_19_1_04_Q001`, `CHUNK1_19_1_04_Q002`, `CHUNK1_19_1_04_Q006`, `CHUNK1_19_1_04_Q007`, `CHUNK1_19_1_04_Q008`, `CHUNK1_19_1_04_Q015`, `CHUNK1_19_1_04_Q023`.
- These were classified as P2 because `option_links` are metadata and no option-label mismatch was found; they should still be polished before import if diagnostic notes can surface in downstream review or feedback.

### Fill_blank mobile-input risk

- None found in audited fill blanks. The 26 audited fill blanks use short Chinese answers such as `颜色`, `逐滴`, `通风橱`, `氧化性`, `还原性`, `浓硫酸`, `冰水浴`, `乙醚`, or `分液漏斗`. No audited fill blank requires typing a complex formula, ion, equation, or long alias.

### Supporting theory risk

- None found in audited questions. Supporting-theory questions used theory for oxidation order, solvent color, hypochlorite/oxidation behavior, peroxide redox duality, Ag₂O identification, or SO₂ redox/bleaching explanation. Evidence ids resolved by exact `chunk_id`.

### Low-quality but retainable

- `CHUNK1_19_1_05_Q010`: asks for the core ability/learning target rather than a concrete observation. It is low-value but still deterministic and tied to the three NaClO reaction branches.
- `CHUNK1_19_2_01_Q027`: mostly identifies `BaSO₄` as the insoluble barium salt in the ozone-preparation equation. Low cognitive load, but supported and machine-deterministic.
- `CHUNK1_19_3_01_Q022`, `CHUNK1_19_3_01_Q027`: apparatus/reagent recall fill blanks. Low depth, but anchored to the SO₂ preparation operation and safe for machine grading.

### Seeds with no detected issue

- `CHUNK1_19_1_01_Q027`
- `CHUNK1_19_1_02_Q002`
- `CHUNK1_19_1_02_Q003`
- `CHUNK1_19_1_03_Q003`
- `CHUNK1_19_2_01_Q027`

Seed note: `CHUNK1_19_1_01_Q022` has no student-visible issue, but its `option_links[].diagnostic_note` contains `点位`, so it is listed as P2 metadata wording risk.

## Validation Notes

- JSON parse: 15/15 rebuilt JSON files parsed.
- Total question count: 450.
- Sample structure: 68/68 audited questions had valid answer shape for their type.
- Single-choice sample: 27/27 had answer labels present in options and matching option-link labels.
- RAG exact id presence: 33 unique sampled evidence ids found by exact `chunk_id` lookup.
- Student-visible raw ids in full-chunk scan: 0.
- Student-visible review-language in full-chunk scan: 1 question (`CHUNK1_19_1_05_Q017`).
- Student-visible ASCII chemistry display in full-chunk scan: 2 questions (`CHUNK1_19_1_05_Q017`, `CHUNK1_19_1_07_Q009`).
- Abnormal CJK spacing / LaTeX / caret leakage in audited visible fields: none observed.

## Final Conclusion

FAIL: chunk_1 should not enter merge/import yet because `CHUNK1_19_1_05_Q017` contains student-visible review language in the explanation. The remaining issues are P2-level display or internal diagnostic-note wording risks, but the P0 blocker alone is sufficient to fail the merge/import readiness check.

