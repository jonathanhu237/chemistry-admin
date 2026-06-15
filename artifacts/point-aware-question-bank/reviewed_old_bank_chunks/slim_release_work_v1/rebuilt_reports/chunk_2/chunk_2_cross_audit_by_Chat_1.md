# chunk_2 cross audit by Chat 1

## Audit Scope

- Audit chunk: `chunk_2`
- Reviewer chat: `Chat 1`
- Audit time: `2026-06-15 18:59:52 +08:00`
- Target directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2`
- Evidence sources:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Mode: read-only cross audit. No rebuilt JSON or release-final JSON was modified.

## Inventory

- Total packets: 15
- Total rebuilt questions: 450
- Type counts: 287 single_choice, 103 true_false, 60 fill_blank
- Actual audited questions: 30
- Coverage in audited sample:
  - Every packet: 2 questions each
  - single_choice: 13
  - true_false: 5
  - fill_blank: 12
  - supporting-theory-dependent: 23
  - multi-point: 23
  - Required seeds / historical risks included: 4

Full-JSON structural scan also found:

- JSON parse: pass
- Single-choice option count / answer label / option_links count: pass, 0 failures
- Cited RAG ids: pass, 0 missing
- Student-visible review-language/raw-id hits: 0
- Student-visible ASCII digit formula hits: 0
- Student-visible ASCII valence / charge / LaTeX/caret hits: 0
- Formula-like fill_blank answer risk: 0
- option_links entries missing `diagnostic_note`: 76 questions, 304 option entries
- option_links text containing internal terms such as "点位": 120 questions, 178 option entries

## Audited Question List

| experiment_code | question_id | question_type | conclusion |
|---|---|---|---|
| 19-3-03 | IDEAL_CH2_19_3_03_Q022 | fill_blank | PASS |
| 19-3-03 | IDEAL_CH2_19_3_03_Q027 | fill_blank | PASS |
| 19-3-04 | REBUILT_CH2_19_3_04_Q014 | single_choice | P2_MINOR |
| 19-3-04 | REBUILT_CH2_19_3_04_Q020 | fill_blank | PASS |
| 19-3-05 | REBUILT_CH2_19_3_05_Q003 | fill_blank | PASS |
| 19-3-05 | REBUILT_CH2_19_3_05_Q017 | true_false | PASS |
| 19-3-06 | REBUILT_CH2_19_3_06_Q004 | fill_blank | PASS |
| 19-3-06 | REBUILT_CH2_19_3_06_Q027 | true_false | PASS |
| 19-4-01 | REBUILT_CH2_19_4_01_Q012 | true_false | PASS |
| 19-4-01 | REBUILT_CH2_19_4_01_Q022 | fill_blank | PASS |
| 19-4-02 | REBUILT_CH2_19_4_02_Q005 | single_choice | PASS |
| 19-4-02 | REBUILT_CH2_19_4_02_Q029 | single_choice | PASS |
| 19-4-03 | REBUILT_CH2_19_4_03_Q029 | single_choice | PASS |
| 19-4-03 | REBUILT_CH2_19_4_03_Q030 | single_choice | PASS |
| 19-4-04 | REBUILT_CH2_19_4_04_Q027 | single_choice | PASS |
| 19-4-04 | REBUILT_CH2_19_4_04_Q028 | single_choice | P2_MINOR |
| 19-4-05 | REBUILT_CH2_19_4_05_Q022 | fill_blank | PASS |
| 19-4-05 | REBUILT_CH2_19_4_05_Q024 | fill_blank | PASS |
| 19-4-06 | REBUILT_CH2_19_4_06_Q014 | true_false | PASS |
| 19-4-06 | REBUILT_CH2_19_4_06_Q020 | single_choice | P2_MINOR |
| 19-4-07 | REBUILT_CH2_19_4_07_Q021 | fill_blank | PASS |
| 19-4-07 | REBUILT_CH2_19_4_07_Q024 | fill_blank | PASS |
| 19-4-08 | REBUILT_CH2_19_4_08_Q025 | fill_blank | PASS |
| 19-4-08 | REBUILT_CH2_19_4_08_Q030 | single_choice | P2_MINOR |
| 19-4-09 | REBUILT_CH2_19_4_09_Q012 | single_choice | P2_MINOR |
| 19-4-09 | REBUILT_CH2_19_4_09_Q029 | single_choice | P2_MINOR |
| 19-5-01 | REBUILT_CH2_19_5_01_Q014 | single_choice | P2_MINOR |
| 19-5-01 | REBUILT_CH2_19_5_01_Q024 | fill_blank | PASS |
| 19-6-01 | REBUILT_CH2_19_6_01_Q010 | single_choice | P2_MINOR |
| 19-6-01 | REBUILT_CH2_19_6_01_Q022 | true_false | P2_MINOR |

## Non-PASS Findings

| severity | question_id | issue field | original text / structure | Why it matters | Suggested handling |
|---|---|---|---|---|---|
| P2_MINOR | REBUILT_CH2_19_3_04_Q014 | option_links.B.diagnostic_note | `碘水点位不以 SO₄²⁻ 作为唯一产物判断。` | The option feedback is semantically aligned, but "点位" is internal annotation language. | Reword as "碘水实验不以 SO₄²⁻ 作为唯一产物判断。" |
| P2_MINOR | REBUILT_CH2_19_4_04_Q028 | option_links.B.diagnostic_note | `第二点位用 KI 和 CCl₄。` | The note is aligned with the adjacent method, but "第二点位" is internal wording. | Reword as "另一种检验方法使用 KI 和 CCl₄。" |
| P2_MINOR | REBUILT_CH2_19_4_06_Q020 | option_links.A/C.diagnostic_note | `解释验证点位。`; `锌点位属于本实验。` | The links point to the correct zinc product-verification content, but the feedback still speaks in internal point labels. | Reword around "验证产物的实验环节" and "锌与稀硝酸反应属于本实验内容。" |
| P2_MINOR | REBUILT_CH2_19_4_08_Q030 | option_links structure | option_links use `label, linked, reason` and omit `diagnostic_note`, `point_key`, `role`. | Options are one-to-one and the reasons are natural, but the structure is inconsistent with the expected diagnostic-note schema. | Normalize option_links to include `point_key`, `role`, and `diagnostic_note`. |
| P2_MINOR | REBUILT_CH2_19_4_09_Q012 | option_links structure | option_links use `label, linked, reason` and omit `diagnostic_note`, `point_key`, `role`. | Same schema inconsistency; semantic link is acceptable. | Normalize option_links schema before merge/import if downstream expects the canonical shape. |
| P2_MINOR | REBUILT_CH2_19_4_09_Q029 | option_links structure | option_links use `label, linked, reason` and omit `diagnostic_note`, `point_key`, `role`. | Same schema inconsistency; semantic link is acceptable. | Normalize option_links schema before merge/import if downstream expects the canonical shape. |
| P2_MINOR | REBUILT_CH2_19_5_01_Q014 | option_links structure | option_links use `label, linked, reason` and omit `diagnostic_note`, `point_key`, `role`. | Same schema inconsistency; semantic link is acceptable. | Normalize option_links schema before merge/import if downstream expects the canonical shape. |
| P2_MINOR | REBUILT_CH2_19_6_01_Q010 | option_links structure | option_links use `label, linked, reason` and omit `diagnostic_note`, `point_key`, `role`. | Same schema inconsistency; semantic link is acceptable. | Normalize option_links schema before merge/import if downstream expects the canonical shape. |
| P2_MINOR | REBUILT_CH2_19_6_01_Q022 | option_links structure | true_false option_links use `label, linked, reason` and omit `diagnostic_note`, `point_key`, `role`. | It is not a single-choice mismatch, but the metadata shape is inconsistent. | Normalize if true/false feedback is imported through the same option_links path. |

No P0/P1 issue was found in the 30-question semantic audit.

## Required Risk Categories

### Student-visible Review Language

- Sampled questions: none found.
- Full visible-field scan: 0 hits for student-visible `题目/题干/点位绑定/证据范围/教材依据核对/选项反馈/机器判分/移动端稳定/RAG/canonical/packet/evidence-first/raw id/backticks`.

### Evidence Insufficient

- Sampled questions: none found.
- Full RAG id existence scan: 0 missing ids.
- Semantic spot-check: sampled source_audit ids support the operation, phenomenon, answer, and explanation claims.

### Point Binding

- No severe point binding mismatch found.
- Sampled multi-point items genuinely cross operations, observations, comparison groups, or integrated conclusions.
- Note: some internal `coverage_tags` / `source_audit.reviewer_note` still use `point_binding` or "点位绑定题"; this is metadata-only and not student-visible.

### option_links

- P2 findings in sampled questions are listed above.
- Full structural scan found a broader pattern:
  - 76 questions use `linked/reason` instead of the richer `point_key/role/diagnostic_note` shape.
  - 120 questions have option feedback text containing internal terms such as "点位".
- This did not create answer mismatch in the audited sample, but it is worth normalizing before merge/import if option feedback is exposed or imported.

### fill_blank Mobile Risk

- Sampled fill blanks were mobile-safe: `漂白`, `示意图`, `配位/络合`, `紫色`, `促进/催化`, `冰水`, `氧化/氧化性`, `褪去/褪色/变浅/消失`, `硝酸盐`, `加热`, `棕/棕色`, `水玻璃`.
- No sampled fill_blank required formulas, ions, equations, or high-alias symbolic input.
- Full structural scan found 0 formula-like fill_blank answer risk by visible answer pattern.

### Supporting Theory Risk

- No sampled supporting-theory failure found.
- Theory-dependent sampled questions cite relevant supporting chunks for:
  - SO₂ bleaching and sulfur chemistry
  - thiosulfate acid decomposition, iodine reduction, sulfate formation, and silver thiosulfate complexing
  - peroxydisulfate oxidation and Ag⁺ promotion/catalysis
  - nitrous acid/nitrite redox behavior
  - nitrate brown-ring chemistry
  - silicate/water-glass chemistry
  - sodium peroxide formation and peroxide reactions

### Low-quality But Retainable

These sampled fill blanks are low-depth but retainable because they are ordinary short Chinese answers, directly evidence-backed, and deterministic:

- `REBUILT_CH2_19_4_01_Q022`: answer `冰水`; procedural control detail.
- `REBUILT_CH2_19_4_07_Q021`: answer `硝酸盐`; broad category check across three samples.
- `REBUILT_CH2_19_4_07_Q024`: answer `加热`; operation check across three samples.
- `REBUILT_CH2_19_4_08_Q025`: answer `棕/棕色`; direct positive observation.
- `REBUILT_CH2_19_5_01_Q024`: answer `水玻璃`; central reagent and safe input.

### Seeds / Historical Risk Checks

- `REBUILT_CH2_19_3_04_Q014`: P2 only, option_links wording uses "点位"; student-facing stem/options/explanation are clean.
- `REBUILT_CH2_19_3_06_Q027`: PASS.
- `REBUILT_CH2_19_4_04_Q027`: PASS; no "如果题目只问" remains.
- `REBUILT_CH2_19_4_04_Q028`: P2 only, option_links wording uses "第二点位"; no "如果题目只问" remains.

Seeds with no issue found: `REBUILT_CH2_19_3_06_Q027`, `REBUILT_CH2_19_4_04_Q027`.

## Final Conclusion

CONDITIONAL

No P0/P1 blockers were found in the 30-question semantic cross-audit, and the student-facing question text appears merge-candidate quality. However, option_links metadata has P2 consistency issues: internal "点位" wording remains in many diagnostic notes, and later packets use `linked/reason` instead of `diagnostic_note`/`point_key`/`role`. Recommendation: normalize option_links metadata before final merge/import if that feedback is surfaced or schema-sensitive.
