# chunk_4 Cross Audit by Chat 3

## Scope

- Audit chunk: `chunk_4`
- Reviewer chat: `Chat 3`
- Audit time: `2026-06-15 19:01:58 +08:00`
- Source inspected: `rebuilt_packages/chunk_4/*_rebuilt_v1.json`
- Evidence sources:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Mode: cross-audit only. No rebuilt JSON, release_final JSON, or source question content was modified.

## Inventory

- Total packets: 15
- Total questions: 450
- Question types in chunk: single_choice 300, true_false 90, fill_blank 60
- Actual audited questions: 65
- Audited type coverage: single_choice 44, true_false 6, fill_blank 15
- Audited supporting-theory-required questions: 12
- Audited multi-point questions: 31
- Seed questions read: 3/3

## Audit Sample List

| experiment_code | question_id | question_type | conclusion |
|---|---|---|---|
| 20-1-02 | REV_CH4_EXP_20_1_02_Q001 | single_choice | PASS |
| 20-1-02 | REV_CH4_EXP_20_1_02_Q005 | single_choice | PASS |
| 20-1-02 | REV_CH4_EXP_20_1_02_Q021 | fill_blank | PASS |
| 20-1-02 | REV_CH4_EXP_20_1_02_Q027 | single_choice | PASS |
| 20-1-03 | REV_CH4_EXP_20_1_03_Q001 | single_choice | PASS |
| 20-1-03 | REV_CH4_EXP_20_1_03_Q021 | true_false | PASS |
| 20-1-03 | REV_CH4_EXP_20_1_03_Q027 | fill_blank | PASS |
| 20-1-03 | REV_CH4_EXP_20_1_03_Q030 | fill_blank | PASS |
| 20-1-04 | REV_CH4_EXP_20_1_04_Q001 | single_choice | PASS |
| 20-1-04 | REV_CH4_EXP_20_1_04_Q021 | true_false | PASS |
| 20-1-04 | REV_CH4_EXP_20_1_04_Q027 | fill_blank | PASS |
| 20-1-05 | REV_CH4_EXP_20_1_05_Q001 | single_choice | PASS |
| 20-1-05 | REV_CH4_EXP_20_1_05_Q009 | single_choice | PASS |
| 20-1-05 | REV_CH4_EXP_20_1_05_Q021 | true_false | PASS |
| 20-1-05 | REV_CH4_EXP_20_1_05_Q027 | fill_blank | PASS |
| 20-1-06 | REV_CH4_EXP_20_1_06_Q001 | single_choice | PASS |
| 20-1-06 | REV_CH4_EXP_20_1_06_Q021 | single_choice | PASS |
| 20-1-06 | REV_CH4_EXP_20_1_06_Q027 | single_choice | PASS |
| 20-1-07 | REV_CH4_EXP_20_1_07_Q001 | single_choice | PASS |
| 20-1-07 | REV_CH4_EXP_20_1_07_Q021 | fill_blank | PASS |
| 20-1-07 | REV_CH4_EXP_20_1_07_Q027 | single_choice | PASS |
| 20-1-08 | REV_CH4_EXP_20_1_08_Q001 | single_choice | PASS |
| 20-1-08 | REV_CH4_EXP_20_1_08_Q021 | fill_blank | PASS |
| 20-1-08 | REV_CH4_EXP_20_1_08_Q027 | single_choice | PASS |
| 20-1-09 | REV_CH4_EXP_20_1_09_Q001 | single_choice | PASS |
| 20-1-09 | REV_CH4_EXP_20_1_09_Q021 | fill_blank | PASS |
| 20-1-09 | REV_CH4_EXP_20_1_09_Q027 | single_choice | PASS |
| 20-2-01 | REV_CH4_EXP_20_2_01_Q001 | single_choice | PASS |
| 20-2-01 | REV_CH4_EXP_20_2_01_Q010 | single_choice | P2_MINOR |
| 20-2-01 | REV_CH4_EXP_20_2_01_Q021 | fill_blank | PASS |
| 20-2-01 | REV_CH4_EXP_20_2_01_Q027 | single_choice | PASS |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q001 | single_choice | PASS |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q002 | single_choice | P2_MINOR |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q006 | single_choice | P1_BLOCKER |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q007 | single_choice | P1_BLOCKER |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q021 | fill_blank | PASS |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q025 | single_choice | P1_BLOCKER |
| 20-2-02 | REV_CH4_EXP_20_2_02_Q027 | single_choice | PASS |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q001 | single_choice | PASS |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q002 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q003 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q004 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q021 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q022 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q023 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q024 | single_choice | P2_MINOR |
| 20-2-03 | REV_CH4_EXP_20_2_03_Q027 | fill_blank | PASS |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q001 | single_choice | PASS |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q003 | single_choice | P2_MINOR |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q007 | single_choice | P2_MINOR |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q008 | single_choice | P2_MINOR |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q010 | single_choice | P2_MINOR |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q019 | single_choice | P2_MINOR |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q021 | fill_blank | PASS |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q025 | single_choice | P2_MINOR |
| 20-2-04 | REV_CH4_EXP_20_2_04_Q027 | single_choice | PASS |
| 20-2-05 | REV_CH4_EXP_20_2_05_Q001 | single_choice | PASS |
| 20-2-05 | REV_CH4_EXP_20_2_05_Q021 | true_false | PASS |
| 20-2-05 | REV_CH4_EXP_20_2_05_Q027 | fill_blank | PASS |
| 20-2-06 | REV_CH4_EXP_20_2_06_Q001 | single_choice | PASS |
| 20-2-06 | REV_CH4_EXP_20_2_06_Q021 | true_false | PASS |
| 20-2-06 | REV_CH4_EXP_20_2_06_Q027 | fill_blank | PASS |
| 20-2-07 | REV_CH4_EXP_20_2_07_Q001 | single_choice | PASS |
| 20-2-07 | REV_CH4_EXP_20_2_07_Q021 | true_false | PASS |
| 20-2-07 | REV_CH4_EXP_20_2_07_Q027 | fill_blank | PASS |

## Findings

### P1_BLOCKER: Supporting Theory Required but No Supporting Theory IDs

Several questions explicitly mark `source_audit.supporting_theory_required=true` while `supporting_theory_chunk_ids` is empty. For questions whose answer depends on theory beyond the procedural experiment chunk, this leaves the evidence chain incomplete before merge/import.

Sampled blockers:

| question_id | Problem field | Problem original | Why it affects import | Suggested handling |
|---|---|---|---|---|
| REV_CH4_EXP_20_2_02_Q006 | `source_audit.supporting_theory_required`, `source_audit.supporting_theory_chunk_ids`; stem/explanation | Stem: `铁(Ⅱ)被氧化后通常对应的较高价态是哪一种？` Explanation: `铁(Ⅱ)被氧化时通常形成铁(Ⅲ)体系。` | The canonical experiment chunk states the Fe(Ⅱ)/Co(Ⅱ)/Ni(Ⅱ) reduction experiment, but this answer relies on general oxidation-state theory. The item says supporting theory is required, yet no theory id is present. | Add a relevant supporting theory id or rewrite the item to rely only on the experiment text. |
| REV_CH4_EXP_20_2_02_Q007 | `source_audit.supporting_theory_required`, `source_audit.supporting_theory_chunk_ids` | Stem: `镍(Ⅱ)沉淀与强氧化剂作用的观察，主要用于比较哪类性质？` | The item is plausible and likely correct, but the audit metadata says theory is required and does not provide theory support. | Either add supporting theory evidence or set supporting requirement consistently if canonical text is considered sufficient. |
| REV_CH4_EXP_20_2_02_Q025 | `source_audit.supporting_theory_required`, `source_audit.supporting_theory_chunk_ids`; stem/explanation | Stem: `铁(Ⅱ)被氧化后常形成哪一种价态？` Explanation: `铁(Ⅱ)作为还原性比较对象，被氧化后通常向铁(Ⅲ)转化。` | Same evidence-chain gap as Q006; answer depends on chemistry theory not fully anchored by listed theory ids. | Add theory evidence or replace with a directly observed experiment-step question. |

Full chunk scan found the same metadata/evidence pattern in 22 questions:

`REV_CH4_EXP_20_1_04_Q029`, `REV_CH4_EXP_20_2_01_Q008`, `REV_CH4_EXP_20_2_01_Q018`, `REV_CH4_EXP_20_2_01_Q022`, `REV_CH4_EXP_20_2_01_Q029`, `REV_CH4_EXP_20_2_01_Q030`, `REV_CH4_EXP_20_2_02_Q004`, `REV_CH4_EXP_20_2_02_Q006`, `REV_CH4_EXP_20_2_02_Q007`, `REV_CH4_EXP_20_2_02_Q009`, `REV_CH4_EXP_20_2_02_Q013`, `REV_CH4_EXP_20_2_02_Q015`, `REV_CH4_EXP_20_2_02_Q025`, `REV_CH4_EXP_20_2_02_Q026`, `REV_CH4_EXP_20_2_02_Q030`, `REV_CH4_EXP_20_2_03_Q008`, `REV_CH4_EXP_20_2_03_Q009`, `REV_CH4_EXP_20_2_03_Q018`, `REV_CH4_EXP_20_2_03_Q019`, `REV_CH4_EXP_20_2_03_Q028`, `REV_CH4_EXP_20_2_03_Q029`, `REV_CH4_EXP_20_2_04_Q009`.

Not all 22 necessarily have wrong answers; the blocking issue is that `supporting_theory_required=true` is contradicted by an empty supporting-theory id list. Merge/import should not proceed until these are reconciled.

### P2_MINOR: ASCII Roman Valence Remains in option_links Diagnostic Notes

The student-facing stems/options/explanations use Chinese names and Unicode valence marks correctly, but `option_links.diagnostic_note` still contains ASCII Roman valence in 17 questions / 35 diagnostic notes. If these diagnostics are ever shown as option feedback, they violate the visible chemistry display rule.

| question_id | Problem field | Example original | Why it matters | Suggested handling |
|---|---|---|---|---|
| REV_CH4_EXP_20_2_01_Q010 | `option_links[0].diagnostic_note` | `硫酸亚铁铵用于亚铁体系，不是铁(III)氢氧化物。` | ASCII valence remains in a feedback-like field. | Use Unicode form: `铁(Ⅲ)` or Chinese valence wording. |
| REV_CH4_EXP_20_2_02_Q002 | `option_links.diagnostic_note` | `氯化铁不是该铁(II)复盐。` | Same display inconsistency. | Use `铁(Ⅱ)`. |
| REV_CH4_EXP_20_2_02_Q006 | `option_links.diagnostic_note` | `符合铁(II)作为还原剂被氧化的方向。` / `本步骤不指向铁(VI)。` | Same display inconsistency; this item also has P1 evidence metadata risk. | Use `铁(Ⅱ)` / `铁(Ⅵ)` and fix evidence metadata. |
| REV_CH4_EXP_20_2_02_Q007 | `option_links[2].diagnostic_note` | `对应镍(II)沉淀与氧化剂作用。` | Same display inconsistency; this item also has P1 evidence metadata risk. | Use `镍(Ⅱ)` and fix evidence metadata. |
| REV_CH4_EXP_20_2_02_Q025 | `option_links[0].diagnostic_note` | `对应铁(II)被氧化的方向。` | Same display inconsistency; this item also has P1 evidence metadata risk. | Use `铁(Ⅱ)` and fix evidence metadata. |
| REV_CH4_EXP_20_2_03_Q002, Q003, Q004, Q022, Q023, Q024 | `option_links.diagnostic_note` | Examples include `铁(III)`, `钴(III)`, `镍(III)`. | Feedback text is not display-polished. | Use `铁(Ⅲ)`, `钴(Ⅲ)`, `镍(Ⅲ)`. |
| REV_CH4_EXP_20_2_04_Q003, Q007, Q008, Q010, Q019, Q025 | `option_links.diagnostic_note` | Examples include `锰(VI)`, `锰(IV)`, `锰(II)`, `锰(VII)`. | Feedback text is not display-polished. | Use `锰(Ⅵ)`, `锰(Ⅳ)`, `锰(Ⅱ)`, `锰(Ⅶ)`. |

### P2_MINOR: Low-Value but Retainable Repetition

`REV_CH4_EXP_20_2_03_Q002`, `Q003`, `Q004`, `Q022`, `Q023`, and `Q024` are mostly repetitive recognition items asking which precipitate corresponds to Fe(Ⅲ), Co(Ⅲ), or Ni(Ⅲ). They are deterministic and evidence-supported, but they add limited depth. They can remain as basic checks, but the packet would be stronger if some were replaced by operation/observation/conclusion questions about the concentrated hydrochloric acid test and chlorine detection.

## Required Risk Buckets

### Student-Visible Review Language Hits

None found in audited sample or full-chunk visible scan. The scan checked stems, options, answers, explanations, and option-link diagnostic notes for terms such as `题目`, `题干`, `点位绑定`, `证据范围`, `教材依据核对`, `选项反馈`, `机器判分`, `移动端稳定`, `RAG`, `canonical`, `packet`, and `evidence-first`.

### Evidence Insufficient

P1 evidence/audit insufficiency found: 22 questions mark supporting theory as required but provide no supporting theory ids. The sampled blockers are `REV_CH4_EXP_20_2_02_Q006`, `REV_CH4_EXP_20_2_02_Q007`, and `REV_CH4_EXP_20_2_02_Q025`.

### Point Binding Problems

No severe point-binding mismatch found in the audited sample. Multi-point audited items generally correspond to real cross-operation, cross-observation, cross-comparison, or cross-conclusion tasks.

### option_links Problems

No A/B/C/D label mismatch and no missing point keys were found. P2 display issue remains in option-link diagnostics: 17 questions contain ASCII Roman valence in diagnostic text.

### fill_blank Mobile Risk

No high-risk formula, ion, equation, or complex alias fill_blank was found in the audited fill blanks. Sampled fill blanks used short Chinese answers such as `热`, `葡萄糖`, `溴化钾`, `碘化钾`, `亚硫酸钠`, `氢氧化钠`, `氯气`, and `煮沸`. `REV_CH4_EXP_20_2_03_Q027` accepts both `碘化钾-淀粉` and `碘化钾淀粉`, so the hyphen does not create a hard mobile-input blocker.

### Supporting Theory Risk

Supporting theory risk is present. Some items correctly include theory ids, for example `REV_CH4_EXP_20_1_09_Q027` uses theory ids for silver-thiosulfate complexes. However, the 22 questions listed above declare supporting theory required while omitting supporting ids.

### Low-Quality but Retainable

The repetitive Fe/Co/Ni precipitate recognition items in `20-2-03` are low-depth but deterministic and evidence-supported. They are P2, not blockers by themselves.

### Seeds With No Issue Found

- `REV_CH4_EXP_20_1_03_Q030`: PASS. Short Chinese fill_blank `溴化钾`, canonical operation supported.
- `REV_CH4_EXP_20_1_04_Q021`: PASS. True/false direct operation question, deterministic and canonical-supported.
- `REV_CH4_EXP_20_1_05_Q009`: PASS. Multi-point experiment-purpose question, answer and point keys match formation plus concentrated ammonia/concentrated hydrochloric acid follow-up.

## Read-Only Validation Notes

- JSON parse: all 15 rebuilt JSON files parse successfully.
- Total question count: 450.
- Per-packet question count: 30 each.
- Single-choice structure: no option label or answer-label errors found.
- Non-choice structure: no non-choice options/option_links errors found.
- option_links: no missing point_key references found.
- primary/secondary point key overlap: 0.
- RAG ids: all listed canonical/supporting ids resolve inside package evidence sources and in external RAG JSONL.
- Student-facing display scan over stem/options/answer/explanation: no ASCII numeric formula, ASCII charge, ASCII Roman valence, LaTeX, or caret found.
- Student-facing audit-language scan: 0 hits.

## Final Conclusion

FAIL: chunk_4 should not enter merge/import yet.

Reason: no P0 was found, but P1 evidence/audit blockers are present. Specifically, multiple questions declare `supporting_theory_required=true` while providing no supporting theory ids, and sampled theory-dependent questions depend on chemistry-theory claims not fully supported by the listed evidence ids. Fix the supporting-theory evidence metadata or rewrite those questions to rely only on canonical experiment text, then rerun audit.

