# 19-4-03 Rebuild Report

This packet was manually read and semantically reconstructed question by question. This is a manual per-question reconstruction, not batch generation.

## Packet Scope

- Chunk: `chunk_2`
- Packet id: `19-4-03`
- Experiment title: `亚硝酸的还原性`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-4-03.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-4-03_rebuilt_v1.json`
- Direct release JSON modification: not performed.

## Decision Counts

- Total: 30
- Keep: 0
- Rewrite: 30
- Reject: 0

## Rewrite Id List

`REBUILT_CH2_19_4_03_Q001`, `REBUILT_CH2_19_4_03_Q002`, `REBUILT_CH2_19_4_03_Q003`, `REBUILT_CH2_19_4_03_Q004`, `REBUILT_CH2_19_4_03_Q005`, `REBUILT_CH2_19_4_03_Q006`, `REBUILT_CH2_19_4_03_Q007`, `REBUILT_CH2_19_4_03_Q008`, `REBUILT_CH2_19_4_03_Q009`, `REBUILT_CH2_19_4_03_Q010`, `REBUILT_CH2_19_4_03_Q011`, `REBUILT_CH2_19_4_03_Q012`, `REBUILT_CH2_19_4_03_Q013`, `REBUILT_CH2_19_4_03_Q014`, `REBUILT_CH2_19_4_03_Q015`, `REBUILT_CH2_19_4_03_Q016`, `REBUILT_CH2_19_4_03_Q017`, `REBUILT_CH2_19_4_03_Q018`, `REBUILT_CH2_19_4_03_Q019`, `REBUILT_CH2_19_4_03_Q020`, `REBUILT_CH2_19_4_03_Q021`, `REBUILT_CH2_19_4_03_Q022`, `REBUILT_CH2_19_4_03_Q023`, `REBUILT_CH2_19_4_03_Q024`, `REBUILT_CH2_19_4_03_Q025`, `REBUILT_CH2_19_4_03_Q026`, `REBUILT_CH2_19_4_03_Q027`, `REBUILT_CH2_19_4_03_Q028`, `REBUILT_CH2_19_4_03_Q029`, `REBUILT_CH2_19_4_03_Q030`

## Edge Keeps

None. The packet was fully rewritten. One edge issue was handled manually: the video point titles suggest a split sequence, while the canonical textbook says the KMnO4 solution is acidified first and then NaNO2 is added. Rebuilt questions therefore use the textbook procedure when asking operation order, and otherwise focus on the stable semantic core: acidic KMnO4, decolorization, and nitrite reducing behavior.

## Evidence Insufficient List

None. No publishable rebuilt question has `evidence_sufficient = false`.

## Multi-Point Questions

- `REBUILT_CH2_19_4_03_Q001`: identifies the full reaction system across NaNO2, KMnO4, and acid medium.
- `REBUILT_CH2_19_4_03_Q002`: connects KMnO4 decolorization with nitrite reducing property.
- `REBUILT_CH2_19_4_03_Q003`: links the video system to the nitrogen oxidation product.
- `REBUILT_CH2_19_4_03_Q004`: links the color change to the reduced manganese product.
- `REBUILT_CH2_19_4_03_Q006`: assigns KMnO4 the oxidant role.
- `REBUILT_CH2_19_4_03_Q007`: assigns NaNO2 the reductant role and nitrate product.
- `REBUILT_CH2_19_4_03_Q008`: checks sulfuric acid as the acidifying medium.
- `REBUILT_CH2_19_4_03_Q009`: resolves operation-order wording against the canonical textbook.
- `REBUILT_CH2_19_4_03_Q010`: summarizes the packet learning goal.
- `REBUILT_CH2_19_4_03_Q011`: true/false item tying decolorization to reducing behavior.
- `REBUILT_CH2_19_4_03_Q012`: true/false role-reversal check.
- `REBUILT_CH2_19_4_03_Q014`: true/false nitrogen-product check.
- `REBUILT_CH2_19_4_03_Q015`: distinguishes this packet from iodine generation.
- `REBUILT_CH2_19_4_03_Q016`: guards against reversing the redox direction.
- `REBUILT_CH2_19_4_03_Q017`: excludes nitrate brown-ring testing.
- `REBUILT_CH2_19_4_03_Q018`: uses theory to explain why a strong oxidant is needed.
- `REBUILT_CH2_19_4_03_Q019`: summarizes the visual observation.
- `REBUILT_CH2_19_4_03_Q020`: contrasts this packet with 19-4-02.
- `REBUILT_CH2_19_4_03_Q021`: fill blank on reducing property across both points.
- `REBUILT_CH2_19_4_03_Q024`: fill blank on dropwise addition across operation and observation.
- `REBUILT_CH2_19_4_03_Q025`: summarizes redox roles.
- `REBUILT_CH2_19_4_03_Q026`: explains decolorization as a redox result.
- `REBUILT_CH2_19_4_03_Q027`: excludes the acidified KI packet.
- `REBUILT_CH2_19_4_03_Q028`: connects acid medium in textbook operation and theory.
- `REBUILT_CH2_19_4_03_Q029`: states the packet evidence boundary.
- `REBUILT_CH2_19_4_03_Q030`: gives the final conclusion.

## Fill-Blank Risk List

- `REBUILT_CH2_19_4_03_Q021`: accepted answers `还原`, `还原性`; low risk, ordinary property word.
- `REBUILT_CH2_19_4_03_Q022`: accepted answers `褪去`, `褪色`, `变浅`, `消失`; low risk, ordinary observation word.
- `REBUILT_CH2_19_4_03_Q023`: accepted answers `硫酸`, `H₂SO₄`; low risk, Unicode formula accepted but Chinese answer is primary.
- `REBUILT_CH2_19_4_03_Q024`: accepted answers `滴加`, `逐滴`, `缓慢滴加`; low risk, ordinary operation phrase.

## Evidence Ids Used

- `expchunk_00242_2da7ff3435`: canonical experiment evidence for sulfuric-acid acidification of KMnO4, addition of sodium nitrite solution, and observation of the phenomenon.
- `textbook_prose_00548_e41b91cedc`: supporting theory that nitrous acid's reducing behavior is apparent with strong oxidants such as KMnO4.
- `textbook_prose_00549_1931138c9a`: supporting theory for nitrous acid reducing permanganate in acid, with nitrate and Mn²⁺ as products.

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
