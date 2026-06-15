# 19-4-02 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-4-02`
- Experiment title: `亚硝酸的氧化性`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-4-02.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-02_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_4_02_Q001`, `REBUILT_CH2_19_4_02_Q002`, `REBUILT_CH2_19_4_02_Q003`, `REBUILT_CH2_19_4_02_Q004`, `REBUILT_CH2_19_4_02_Q005`, `REBUILT_CH2_19_4_02_Q006`, `REBUILT_CH2_19_4_02_Q007`, `REBUILT_CH2_19_4_02_Q008`, `REBUILT_CH2_19_4_02_Q009`, `REBUILT_CH2_19_4_02_Q010`, `REBUILT_CH2_19_4_02_Q011`, `REBUILT_CH2_19_4_02_Q012`, `REBUILT_CH2_19_4_02_Q013`, `REBUILT_CH2_19_4_02_Q014`, `REBUILT_CH2_19_4_02_Q015`, `REBUILT_CH2_19_4_02_Q016`, `REBUILT_CH2_19_4_02_Q017`, `REBUILT_CH2_19_4_02_Q018`, `REBUILT_CH2_19_4_02_Q019`, `REBUILT_CH2_19_4_02_Q020`, `REBUILT_CH2_19_4_02_Q021`, `REBUILT_CH2_19_4_02_Q022`, `REBUILT_CH2_19_4_02_Q023`, `REBUILT_CH2_19_4_02_Q024`, `REBUILT_CH2_19_4_02_Q025`, `REBUILT_CH2_19_4_02_Q026`, `REBUILT_CH2_19_4_02_Q027`, `REBUILT_CH2_19_4_02_Q028`, `REBUILT_CH2_19_4_02_Q029`, `REBUILT_CH2_19_4_02_Q030`

## Edge Keeps

None. Every item was rewritten to avoid repeated template wording, clarify oxidized species and packet scope, and remove formula-style fill answers such as `I2`.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_4_02_Q001`: connects the acidified KI setup with the later observation point.
- `REBUILT_CH2_19_4_02_Q003`: links NaNO₂ addition with the required micro-heating observation.
- `REBUILT_CH2_19_4_02_Q004`: identifies iodide as the oxidized species using operation and theory.
- `REBUILT_CH2_19_4_02_Q005`: connects iodide oxidation with iodine observation.
- `REBUILT_CH2_19_4_02_Q006`: judges the property across the whole two-point workflow.
- `REBUILT_CH2_19_4_02_Q007`: excludes nitrate testing and centers HNO₂ oxidation.
- `REBUILT_CH2_19_4_02_Q008`: assigns HNO₂ the oxidant role from the observed redox change.
- `REBUILT_CH2_19_4_02_Q009`: uses color change as the observation-side evidence for iodine formation.
- `REBUILT_CH2_19_4_02_Q010`: separates this packet from the adjacent permanganate/reducing-property subexperiment.
- `REBUILT_CH2_19_4_02_Q011`: true/false item integrating acidified KI and iodine formation.
- `REBUILT_CH2_19_4_02_Q014`: distinguishes iodine evidence from potassium ion bystander behavior.
- `REBUILT_CH2_19_4_02_Q016`: guards against importing the four-chloride-carbon extraction test.
- `REBUILT_CH2_19_4_02_Q017`: summarizes operation plus micro-heating observation.
- `REBUILT_CH2_19_4_02_Q018`: diagnoses reversal of oxidation direction.
- `REBUILT_CH2_19_4_02_Q019`: contrasts the result-observation point with the setup point.
- `REBUILT_CH2_19_4_02_Q020`: uses supporting theory to distinguish HNO₂ from HNO₃.
- `REBUILT_CH2_19_4_02_Q021`: fill blank on iodine product, tied to both points.
- `REBUILT_CH2_19_4_02_Q023`: fill blank on oxidation property, tied to both points.
- `REBUILT_CH2_19_4_02_Q025`: explains the purpose of micro-heating.
- `REBUILT_CH2_19_4_02_Q026`: traces NaNO₂ to HNO₂ and then to iodide oxidation.
- `REBUILT_CH2_19_4_02_Q027`: links the observation to electron-loss reasoning.
- `REBUILT_CH2_19_4_02_Q028`: states the evidence boundary for the packet.
- `REBUILT_CH2_19_4_02_Q029`: contrasts oxidation-property and reducing-property subexperiments.
- `REBUILT_CH2_19_4_02_Q030`: gives the final two-point conclusion.

## Fill-Blank Risk List

- `REBUILT_CH2_19_4_02_Q021`: accepted answers `碘`, `碘单质`; low risk, replaces formula answer `I2`.
- `REBUILT_CH2_19_4_02_Q022`: accepted answer `微热`; low risk, ordinary operation word.
- `REBUILT_CH2_19_4_02_Q023`: accepted answers `氧化`, `氧化性`; low risk, ordinary property word.
- `REBUILT_CH2_19_4_02_Q024`: accepted answers `旁观`, `旁观离子`; low risk, ordinary concept phrase.

## Evidence Ids Used

- `expchunk_00242_2da7ff3435`: canonical experiment evidence for acidified KI, addition of sodium nitrite solution, and gentle heating/observation of product color and state changes.
- `textbook_prose_00547_2a1f998120`: supporting theory that nitrous acid/nitrite can show oxidizing behavior in acidic solution and oxidize iodide to iodine.
- `textbook_prose_00548_e41b91cedc`: supporting theory for the acidic iodide oxidation reaction and the distinction between HNO₂ and HNO₃.

`expchunk_00248_a94cd0af07` was present in inherited metadata but was not used as core evidence because it is a thinking-question locator rather than the direct video-point procedure.

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
