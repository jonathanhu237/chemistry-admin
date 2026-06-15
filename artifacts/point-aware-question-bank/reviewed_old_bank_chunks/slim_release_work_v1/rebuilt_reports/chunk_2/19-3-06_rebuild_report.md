# 19-3-06 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-3-06`
- Experiment title: `过硫酸盐的氧化性`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-3-06.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-06_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_3_06_Q001`, `REBUILT_CH2_19_3_06_Q002`, `REBUILT_CH2_19_3_06_Q003`, `REBUILT_CH2_19_3_06_Q004`, `REBUILT_CH2_19_3_06_Q005`, `REBUILT_CH2_19_3_06_Q006`, `REBUILT_CH2_19_3_06_Q007`, `REBUILT_CH2_19_3_06_Q008`, `REBUILT_CH2_19_3_06_Q009`, `REBUILT_CH2_19_3_06_Q010`, `REBUILT_CH2_19_3_06_Q011`, `REBUILT_CH2_19_3_06_Q012`, `REBUILT_CH2_19_3_06_Q013`, `REBUILT_CH2_19_3_06_Q014`, `REBUILT_CH2_19_3_06_Q015`, `REBUILT_CH2_19_3_06_Q016`, `REBUILT_CH2_19_3_06_Q017`, `REBUILT_CH2_19_3_06_Q018`, `REBUILT_CH2_19_3_06_Q019`, `REBUILT_CH2_19_3_06_Q020`, `REBUILT_CH2_19_3_06_Q021`, `REBUILT_CH2_19_3_06_Q022`, `REBUILT_CH2_19_3_06_Q023`, `REBUILT_CH2_19_3_06_Q024`, `REBUILT_CH2_19_3_06_Q025`, `REBUILT_CH2_19_3_06_Q026`, `REBUILT_CH2_19_3_06_Q027`, `REBUILT_CH2_19_3_06_Q028`, `REBUILT_CH2_19_3_06_Q029`, `REBUILT_CH2_19_3_06_Q030`

## Edge Keeps

None. Every source item was rewritten to remove inherited chunk assumptions, bind the item to the two packet video points, and avoid formula-heavy student-facing text.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_3_06_Q001`: compares the two point records to identify the AgNO3 variable.
- `REBUILT_CH2_19_3_06_Q002`: contrasts the AgNO3 and no-AgNO3 operations as an experimental control.
- `REBUILT_CH2_19_3_06_Q003`: asks for the expected effect of adding silver nitrate by comparing both point records.
- `REBUILT_CH2_19_3_06_Q004`: fill blank on the catalytic/promoting role, grounded in the two-point comparison.
- `REBUILT_CH2_19_3_06_Q006`: uses both point records to identify the shared acidic medium.
- `REBUILT_CH2_19_3_06_Q007`: requires both packet points and supporting theory about acidity.
- `REBUILT_CH2_19_3_06_Q013`: primary evidence is the AgNO3 point, with the no-AgNO3 point as comparison context.
- `REBUILT_CH2_19_3_06_Q014`: primary evidence is the oxidant role, with the control point as comparison context.
- `REBUILT_CH2_19_3_06_Q015`: asks which statement is shared by both point records and supported by theory.
- `REBUILT_CH2_19_3_06_Q016`: fill blank on oxidizing property, applying across both point records.
- `REBUILT_CH2_19_3_06_Q017`: judges packet scope by distinguishing the two MnSO4 points from the KI operation in the same canonical source chunk.
- `REBUILT_CH2_19_3_06_Q019`: asks for the safest point binding of the two packet records.
- `REBUILT_CH2_19_3_06_Q020`: identifies the operation excluded from this packet although it appears in the canonical chunk.
- `REBUILT_CH2_19_3_06_Q022`: true/false item on the acid medium shared by both point records.
- `REBUILT_CH2_19_3_06_Q023`: true/false item on no-AgNO3 as the control condition.
- `REBUILT_CH2_19_3_06_Q025`: separates these two packet points from other experiment distractors.
- `REBUILT_CH2_19_3_06_Q026`: integrates reagent roles across both packet points.
- `REBUILT_CH2_19_3_06_Q027`: true/false item on overextending the iodine-water interpretation to both packet points.
- `REBUILT_CH2_19_3_06_Q028`: asks which shared reagent role is safe across both records.
- `REBUILT_CH2_19_3_06_Q030`: integrates the packet's learning goal across the two-point control design.

## Fill-Blank Risk List

- `REBUILT_CH2_19_3_06_Q004`: accepted answers `促进`, `催化`, `促进或催化`; low risk, no symbolic formula answer.
- `REBUILT_CH2_19_3_06_Q009`: accepted answers `水浴`, `水浴加热`; low risk, ordinary operation phrase.
- `REBUILT_CH2_19_3_06_Q012`: accepted answers `紫`, `紫红`; low risk, ordinary color word.
- `REBUILT_CH2_19_3_06_Q016`: accepted answers `氧化`, `氧化性`; low risk, ordinary property word.

## Evidence Ids Used

- `expchunk_00231_3725c0805d`: canonical experiment evidence for the MnSO4/H2SO4/AgNO3/K2S2O8 operation, water-bath heating, and no-AgNO3 control; the KI operation in the same chunk was treated as outside this packet's video points.
- `expchunk_00233_e7fe95eac0`: canonical thinking-question evidence on why the reaction needs acidic medium and how insufficient acidity affects it.
- `textbook_prose_00397_b4519b367e`: theory support for Mn2+ oxidation by S2O8^2- under heat and Ag+ catalysis, producing permanganate and sulfate.
- `textbook_prose_01241_99049758ad`: theory support for the purple color of permanganate and the same Mn2+ to permanganate reaction.

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
