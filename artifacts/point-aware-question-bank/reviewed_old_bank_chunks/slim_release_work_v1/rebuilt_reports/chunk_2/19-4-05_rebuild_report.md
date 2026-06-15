# 19-4-05 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-4-05`
- Experiment title: `亚硝酸的氧化还原性`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-4-05.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-05_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_4_05_Q001`, `REBUILT_CH2_19_4_05_Q002`, `REBUILT_CH2_19_4_05_Q003`, `REBUILT_CH2_19_4_05_Q004`, `REBUILT_CH2_19_4_05_Q005`, `REBUILT_CH2_19_4_05_Q006`, `REBUILT_CH2_19_4_05_Q007`, `REBUILT_CH2_19_4_05_Q008`, `REBUILT_CH2_19_4_05_Q009`, `REBUILT_CH2_19_4_05_Q010`, `REBUILT_CH2_19_4_05_Q011`, `REBUILT_CH2_19_4_05_Q012`, `REBUILT_CH2_19_4_05_Q013`, `REBUILT_CH2_19_4_05_Q014`, `REBUILT_CH2_19_4_05_Q015`, `REBUILT_CH2_19_4_05_Q016`, `REBUILT_CH2_19_4_05_Q017`, `REBUILT_CH2_19_4_05_Q018`, `REBUILT_CH2_19_4_05_Q019`, `REBUILT_CH2_19_4_05_Q020`, `REBUILT_CH2_19_4_05_Q021`, `REBUILT_CH2_19_4_05_Q022`, `REBUILT_CH2_19_4_05_Q023`, `REBUILT_CH2_19_4_05_Q024`, `REBUILT_CH2_19_4_05_Q025`, `REBUILT_CH2_19_4_05_Q026`, `REBUILT_CH2_19_4_05_Q027`, `REBUILT_CH2_19_4_05_Q028`, `REBUILT_CH2_19_4_05_Q029`, `REBUILT_CH2_19_4_05_Q030`

## Edge Keeps

None. This packet is a composite comparison package, so every item was rewritten to avoid collapsing it into either the KI oxidation point alone or the KMnO4 reduction point alone.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_4_05_Q001`: identifies the two point types needed for two-sided redox.
- `REBUILT_CH2_19_4_05_Q004`: summarizes different reaction objects across the two points.
- `REBUILT_CH2_19_4_05_Q008`: connects intermediate valence with two-sided behavior.
- `REBUILT_CH2_19_4_05_Q009`: diagnoses under-coverage when only the KI point is used.
- `REBUILT_CH2_19_4_05_Q010`: contrasts iodine generation and permanganate decolorization.
- `REBUILT_CH2_19_4_05_Q011`: true/false item assigning oxidation and reduction points.
- `REBUILT_CH2_19_4_05_Q014`: true/false item on intermediate valence and two-sided behavior.
- `REBUILT_CH2_19_4_05_Q015`: true/false item on coverage completeness.
- `REBUILT_CH2_19_4_05_Q017`: excludes the nitrite detection packet.
- `REBUILT_CH2_19_4_05_Q018`: explains the reduction point while contrasting the oxidation point.
- `REBUILT_CH2_19_4_05_Q019`: explains the oxidation point while contrasting the reduction point.
- `REBUILT_CH2_19_4_05_Q020`: states the evidence boundary.
- `REBUILT_CH2_19_4_05_Q025`: asks how to design a true two-point question.
- `REBUILT_CH2_19_4_05_Q026`: explains why the two point observations are not duplicates.
- `REBUILT_CH2_19_4_05_Q027`: designs a distractor from the neighboring reduction point.
- `REBUILT_CH2_19_4_05_Q028`: designs a distractor from the neighboring oxidation point.
- `REBUILT_CH2_19_4_05_Q029`: selects a safe assessment approach for the composite packet.
- `REBUILT_CH2_19_4_05_Q030`: final conclusion across both points.

## Fill-Blank Risk List

- `REBUILT_CH2_19_4_05_Q021`: accepted answers `还原`, `还原性`; low risk, ordinary property word.
- `REBUILT_CH2_19_4_05_Q022`: accepted answers `氧化`, `氧化性`; low risk, ordinary property word.
- `REBUILT_CH2_19_4_05_Q023`: accepted answers `碘`, `碘单质`; low risk, replaces symbolic iodine formula input.
- `REBUILT_CH2_19_4_05_Q024`: accepted answers `褪去`, `褪色`, `变浅`, `消失`; low risk, ordinary observation word.

## Evidence Ids Used

- `expchunk_00242_2da7ff3435`: canonical experiment evidence for acidified KI plus sodium nitrite and acidified permanganate plus sodium nitrite.
- `textbook_prose_00547_2a1f998120`: supporting theory that nitrous acid/nitrite has both oxidizing and reducing behavior.
- `textbook_prose_00548_e41b91cedc`: supporting theory for iodide oxidation and the condition that reducing behavior appears with strong oxidants.
- `textbook_prose_00549_1931138c9a`: supporting theory for nitrous acid reducing permanganate in acid, producing nitrate and Mn²⁺.

## Validation

- JSON parse: OK.
- Question count: 30.
- Question ids: unique.
- Single-choice answers and option links: aligned.
- Cited evidence ids: present in the RAG JSONL sources.
- Evidence-insufficient publishable questions: none.
- Visible ASCII digit formulas in student-facing fields: none after validation.
- Complex formula fill answers: none.

## Publish Blocker Polish Final Check

- Scope: student-visible `stem`, `options[].text`, `explanation`, fill-blank accepted/visible answers, and `diagnostic_note`.
- Scan method: rule-category scan plus manual confirmation; not example-only replacement.
- Internal/process wording after polish: 0.
- ASCII digit formula after polish: 0.
- ASCII charge/ion after polish: 0.
- caret/LaTeX/Markdown chemistry after polish: 0.
- Student-visible process note after polish: 0.
- Release JSON modification during polish: not performed.
- `question_id` / point keys / evidence ids modified during polish: not performed.
