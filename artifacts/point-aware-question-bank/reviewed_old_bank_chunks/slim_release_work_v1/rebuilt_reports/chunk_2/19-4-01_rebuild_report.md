# 19-4-01 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-4-01`
- Experiment title: `亚硝酸的生成与分解`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-4-01.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-01_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_4_01_Q001`, `REBUILT_CH2_19_4_01_Q002`, `REBUILT_CH2_19_4_01_Q003`, `REBUILT_CH2_19_4_01_Q004`, `REBUILT_CH2_19_4_01_Q005`, `REBUILT_CH2_19_4_01_Q006`, `REBUILT_CH2_19_4_01_Q007`, `REBUILT_CH2_19_4_01_Q008`, `REBUILT_CH2_19_4_01_Q009`, `REBUILT_CH2_19_4_01_Q010`, `REBUILT_CH2_19_4_01_Q011`, `REBUILT_CH2_19_4_01_Q012`, `REBUILT_CH2_19_4_01_Q013`, `REBUILT_CH2_19_4_01_Q014`, `REBUILT_CH2_19_4_01_Q015`, `REBUILT_CH2_19_4_01_Q016`, `REBUILT_CH2_19_4_01_Q017`, `REBUILT_CH2_19_4_01_Q018`, `REBUILT_CH2_19_4_01_Q019`, `REBUILT_CH2_19_4_01_Q020`, `REBUILT_CH2_19_4_01_Q021`, `REBUILT_CH2_19_4_01_Q022`, `REBUILT_CH2_19_4_01_Q023`, `REBUILT_CH2_19_4_01_Q024`, `REBUILT_CH2_19_4_01_Q025`, `REBUILT_CH2_19_4_01_Q026`, `REBUILT_CH2_19_4_01_Q027`, `REBUILT_CH2_19_4_01_Q028`, `REBUILT_CH2_19_4_01_Q029`, `REBUILT_CH2_19_4_01_Q030`

## Edge Keeps

None. The existing draft was template-heavy, so every item was rewritten with packet-specific wording, clearer scope boundaries, and short explanations.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_4_01_Q001`: links the starting reagent pair to the later generation/decomposition observation.
- `REBUILT_CH2_19_4_01_Q003`: connects cooling with the need to observe unstable product behavior.
- `REBUILT_CH2_19_4_01_Q004`: asks for the first target product while keeping the later decomposition point in view.
- `REBUILT_CH2_19_4_01_Q008`: orders point 1 as operation and point 2 as observation.
- `REBUILT_CH2_19_4_01_Q009`: separates this packet from adjacent KI operations in the same canonical chunk.
- `REBUILT_CH2_19_4_01_Q010`: uses the starting operation and standing-time observation together.
- `REBUILT_CH2_19_4_01_Q012`: distinguishes the salt byproduct from the packet's decomposition focus.
- `REBUILT_CH2_19_4_01_Q015`: guards against over-including the KI oxidation subexperiment.
- `REBUILT_CH2_19_4_01_Q016`: ties instability to the required observation after standing.
- `REBUILT_CH2_19_4_01_Q017`: summarizes both packet points as generation followed by decomposition.
- `REBUILT_CH2_19_4_01_Q019`: combines cold generation, blue intermediate, and brown gas as report keywords.
- `REBUILT_CH2_19_4_01_Q020`: diagnoses the error of stopping at the generation step.
- `REBUILT_CH2_19_4_01_Q021`: distinguishes sulfuric acid's starting role from later products.
- `REBUILT_CH2_19_4_01_Q025`: fill blank uses the experiment title and both video points.
- `REBUILT_CH2_19_4_01_Q026`: explicitly tests evidence boundary rather than chunk-wide inclusion.
- `REBUILT_CH2_19_4_01_Q027`: forms a safe conclusion covering generation and decomposition.
- `REBUILT_CH2_19_4_01_Q029`: chooses point 2 as the result-observation point while contrasting point 1.
- `REBUILT_CH2_19_4_01_Q030`: summarizes the allowed evidence boundary across both points.

## Fill-Blank Risk List

- `REBUILT_CH2_19_4_01_Q022`: accepted answers `冰水`, `冰水冷却`, `冰水冷冻`; low risk, ordinary operation phrase.
- `REBUILT_CH2_19_4_01_Q023`: accepted answers `蓝`, `蓝色`; low risk, ordinary color word.
- `REBUILT_CH2_19_4_01_Q024`: accepted answers `棕`, `棕色`, `红棕`, `红棕色`; low risk, ordinary color word.
- `REBUILT_CH2_19_4_01_Q025`: accepted answer `分解`; low risk, ordinary concept word.

## Evidence Ids Used

- `expchunk_00242_2da7ff3435`: canonical experiment evidence for ice-cooled saturated sodium nitrite solution mixed with sulfuric acid, nitrous acid generation, blue intermediate formation, and NO / NO₂ gas production.

No supporting-theory chunk was required because the canonical experiment chunk directly states the operation, colors, and decomposition sequence used in every rebuilt item.

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
