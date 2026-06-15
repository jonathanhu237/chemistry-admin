# 19-4-04 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-4-04`
- Experiment title: `亚硝酸根的检验方法`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-4-04.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-04_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_4_04_Q001`, `REBUILT_CH2_19_4_04_Q002`, `REBUILT_CH2_19_4_04_Q003`, `REBUILT_CH2_19_4_04_Q004`, `REBUILT_CH2_19_4_04_Q005`, `REBUILT_CH2_19_4_04_Q006`, `REBUILT_CH2_19_4_04_Q007`, `REBUILT_CH2_19_4_04_Q008`, `REBUILT_CH2_19_4_04_Q009`, `REBUILT_CH2_19_4_04_Q010`, `REBUILT_CH2_19_4_04_Q011`, `REBUILT_CH2_19_4_04_Q012`, `REBUILT_CH2_19_4_04_Q013`, `REBUILT_CH2_19_4_04_Q014`, `REBUILT_CH2_19_4_04_Q015`, `REBUILT_CH2_19_4_04_Q016`, `REBUILT_CH2_19_4_04_Q017`, `REBUILT_CH2_19_4_04_Q018`, `REBUILT_CH2_19_4_04_Q019`, `REBUILT_CH2_19_4_04_Q020`, `REBUILT_CH2_19_4_04_Q021`, `REBUILT_CH2_19_4_04_Q022`, `REBUILT_CH2_19_4_04_Q023`, `REBUILT_CH2_19_4_04_Q024`, `REBUILT_CH2_19_4_04_Q025`, `REBUILT_CH2_19_4_04_Q026`, `REBUILT_CH2_19_4_04_Q027`, `REBUILT_CH2_19_4_04_Q028`, `REBUILT_CH2_19_4_04_Q029`, `REBUILT_CH2_19_4_04_Q030`

## Edge Keeps

None. The source draft repeated the same checks several times, so every item was rewritten to separate the two methods: point-drops red-color method and KI-CCl4 purple organic-layer method.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_4_04_Q006`: identifies NO2- as the shared target ion of both methods.
- `REBUILT_CH2_19_4_04_Q007`: contrasts red point-drop color and purple CCl4 layer.
- `REBUILT_CH2_19_4_04_Q009`: distinguishes KI/CCl4 from point-drop reagents.
- `REBUILT_CH2_19_4_04_Q010`: gives the overall two-method conclusion.
- `REBUILT_CH2_19_4_04_Q016`: true/false item on acid medium shared by both methods.
- `REBUILT_CH2_19_4_04_Q018`: true/false item on target ion across both points.
- `REBUILT_CH2_19_4_04_Q019`: excludes KMnO4 decolorization from this packet.
- `REBUILT_CH2_19_4_04_Q020`: binds CCl4 purple layer to the KI-CCl4 method while contrasting point-drop red color.
- `REBUILT_CH2_19_4_04_Q026`: asks for the shared acid-condition premise.
- `REBUILT_CH2_19_4_04_Q027`: binds CCl4-layer color questions to point 2.
- `REBUILT_CH2_19_4_04_Q028`: binds sulfanilic acid/naphthylamine questions to point 1.
- `REBUILT_CH2_19_4_04_Q029`: states the evidence boundary for the packet.
- `REBUILT_CH2_19_4_04_Q030`: final conclusion covering both methods.

## Fill-Blank Risk List

- `REBUILT_CH2_19_4_04_Q021`: accepted answers `HAc`, `乙酸`, `醋酸`; low risk, short acid name rather than complex formula.
- `REBUILT_CH2_19_4_04_Q022`: accepted answer `萘胺`; low risk, ordinary reagent name.
- `REBUILT_CH2_19_4_04_Q023`: accepted answers `红`, `红色`; low risk, ordinary color word.
- `REBUILT_CH2_19_4_04_Q024`: accepted answers `碘`, `碘单质`; low risk, replaces symbolic iodine formula input.

## Evidence Ids Used

- `expchunk_00242_2da7ff3435`: canonical experiment evidence for the HAc/sulfanilic acid/naphthylamine red-color test and the acidified KI/CCl4 purple-layer test.
- `textbook_prose_00547_2a1f998120`: supporting theory that nitrous acid/nitrite oxidizes iodide to iodine in acidic solution.
- `textbook_prose_00548_e41b91cedc`: supporting theory for acid nitrous acid oxidizing iodide, used for KI-CCl4 method reasoning.

`expchunk_00248_a94cd0af07` was present in inherited metadata but was not used as core evidence because the direct procedure and positive phenomena are already in `expchunk_00242_2da7ff3435`; the thinking-question chunk is only a broad locator.

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
