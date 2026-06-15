# 19-4-06 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-4-06`
- Experiment title: `硝酸的氧化性`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-4-06.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-06_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_4_06_Q001`, `REBUILT_CH2_19_4_06_Q002`, `REBUILT_CH2_19_4_06_Q003`, `REBUILT_CH2_19_4_06_Q004`, `REBUILT_CH2_19_4_06_Q005`, `REBUILT_CH2_19_4_06_Q006`, `REBUILT_CH2_19_4_06_Q007`, `REBUILT_CH2_19_4_06_Q008`, `REBUILT_CH2_19_4_06_Q009`, `REBUILT_CH2_19_4_06_Q010`, `REBUILT_CH2_19_4_06_Q011`, `REBUILT_CH2_19_4_06_Q012`, `REBUILT_CH2_19_4_06_Q013`, `REBUILT_CH2_19_4_06_Q014`, `REBUILT_CH2_19_4_06_Q015`, `REBUILT_CH2_19_4_06_Q016`, `REBUILT_CH2_19_4_06_Q017`, `REBUILT_CH2_19_4_06_Q018`, `REBUILT_CH2_19_4_06_Q019`, `REBUILT_CH2_19_4_06_Q020`, `REBUILT_CH2_19_4_06_Q021`, `REBUILT_CH2_19_4_06_Q022`, `REBUILT_CH2_19_4_06_Q023`, `REBUILT_CH2_19_4_06_Q024`, `REBUILT_CH2_19_4_06_Q025`, `REBUILT_CH2_19_4_06_Q026`, `REBUILT_CH2_19_4_06_Q027`, `REBUILT_CH2_19_4_06_Q028`, `REBUILT_CH2_19_4_06_Q029`, `REBUILT_CH2_19_4_06_Q030`

## Edge Keeps

None. The packet was rewritten to separate concentrated nitric acid, dilute nitric acid, copper, zinc, sulfur/sulfide, and the NH3/NH4+ verification point. Zinc-product questions were phrased as “the experiment requires verification” rather than overclaiming a single exclusive product.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_4_06_Q001`: scopes all six video points.
- `REBUILT_CH2_19_4_06_Q003`: compares dilute nitric acid/copper with concentrated nitric acid/copper.
- `REBUILT_CH2_19_4_06_Q004`: links zinc reaction and NH3/NH4+ verification.
- `REBUILT_CH2_19_4_06_Q007`: verifies ammonium by releasing ammonia from the zinc-product context.
- `REBUILT_CH2_19_4_06_Q008`: summarizes concentrated/dilute nitric-acid comparison.
- `REBUILT_CH2_19_4_06_Q009`: excludes nitrite point-drop testing.
- `REBUILT_CH2_19_4_06_Q010`: contrasts nitric acid oxidizing behavior with ordinary acid metal reactions.
- `REBUILT_CH2_19_4_06_Q012`: true/false item on zinc-product verification.
- `REBUILT_CH2_19_4_06_Q014`: true/false item on sulfur and sulfide as reductants.
- `REBUILT_CH2_19_4_06_Q015`: excludes PbO2/concentrated HCl.
- `REBUILT_CH2_19_4_06_Q016`: compares concentrated and dilute nitric acid reduction products.
- `REBUILT_CH2_19_4_06_Q017`: excludes the sodium nitrite/sulfuric acid packet.
- `REBUILT_CH2_19_4_06_Q019`: compares concentrated and dilute nitric acid with copper.
- `REBUILT_CH2_19_4_06_Q020`: explains why zinc has a separate product-verification point.
- `REBUILT_CH2_19_4_06_Q021`: fill blank on oxidizing property across several points.
- `REBUILT_CH2_19_4_06_Q024`: fill blank on concentrated/dilute comparison.
- `REBUILT_CH2_19_4_06_Q025`: safe wording for zinc product verification.
- `REBUILT_CH2_19_4_06_Q026`: identifies the best concentrated/dilute copper comparison.
- `REBUILT_CH2_19_4_06_Q027`: designs a distractor for concentrated nitric acid points.
- `REBUILT_CH2_19_4_06_Q028`: designs a distractor for zinc points.
- `REBUILT_CH2_19_4_06_Q029`: states the packet evidence boundary.
- `REBUILT_CH2_19_4_06_Q030`: final conclusion across all points.

## Fill-Blank Risk List

- `REBUILT_CH2_19_4_06_Q021`: accepted answers `氧化`, `氧化性`; low risk, ordinary property word.
- `REBUILT_CH2_19_4_06_Q022`: accepted answer `一氧化氮`; low risk, replaces formula answer `NO`.
- `REBUILT_CH2_19_4_06_Q023`: accepted answers `棕`, `棕色`, `红棕`, `红棕色`; low risk, ordinary color word.
- `REBUILT_CH2_19_4_06_Q024`: accepted answer `稀`; low risk, ordinary descriptor.

## Evidence Ids Used

- `expchunk_00243_765fc7b450`: canonical experiment evidence for nitric acid reactions with sulfur, hydrogen sulfide/sulfide, copper, dilute nitric acid with copper, zinc, and NH3/NH4+ verification.
- `textbook_prose_00558_9cffe40305`: supporting theory that nitric acid is strongly oxidizing and concentrated nitric acid can be reduced to NO2, NO, ammonium, etc.
- `textbook_prose_00559_03c424ac53`: supporting theory for concentrated nitric acid with copper and sulfur.
- `textbook_prose_00562_ef6a65a064`: supporting theory for dilute nitric acid with copper and active-metal reduction products.

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
