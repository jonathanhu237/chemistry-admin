# Rebuild Report: chunk_2 / 19-3-05 过二硫酸盐的氧化性

## Packet

- Packet id / experiment code: `19-3-05`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-3-05.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-05_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `single_choice=21`, `true_false=5`, `fill_blank=4`
- Statement: this packet has been manually read and semantically reconstructed question by question. It is not a script batch generation or metadata-only normalization.
- Manual audit phrase: manual per-question reconstruction, not batch generation.

## RAG Evidence Read

- `expchunk_00231_3725c0805d` (`textbook_experiment_chunks_v1.jsonl`, line 244): canonical experiment for K₂S₂O₈ oxidizing property. It specifies the MnSO₄/H₂SO₄/AgNO₃/K₂S₂O₈ heated system, the no-AgNO₃ control, and acidified KI plus K₂S₂O₈ observation.
- `expchunk_00233_e7fe95eac0` (`textbook_experiment_chunks_v1.jsonl`, line 246): thinking questions on S₂O₈²⁻ versus MnO₄⁻ oxidizing strength, S₂O₈²⁻ versus I⁻ reducing strength, and why K₂S₂O₈/Mn²⁺ needs acidic medium.
- `textbook_prose_00397_b4519b367e` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 659): theory reaction showing Mn²⁺ oxidized by S₂O₈²⁻ under heat and Ag⁺ catalysis to MnO₄⁻, while S₂O₈²⁻ becomes SO₄²⁻.
- `textbook_prose_01241_99049758ad` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 1898): repeats the Mn²⁺ to MnO₄⁻ reaction and states MnO₄⁻ is purple, making the phenomenon clear.

Evidence note:

- I did not find a separate theory chunk explicitly spelling out `S₂O₈²⁻ + I⁻ -> I₂`. For the KI point, the rebuilt questions cite the canonical experiment chunk and the thinking-question chunk; they do not invent a supporting-theory id.
- `textbook_prose_00398_7d32d54ebf` was present in the old packet area but was not used because it describes thermal decomposition of K₂S₂O₈, not the final rebuilt question judgements.

## Keep / Rewrite / Reject

- Keep: `0`
- Rewrite: `30`
- Reject: `0`

The source packet had several correct raw facts, but it repeated low-depth reagent/color/formula questions and often attached broad or inherited point and theory bindings. The rebuilt package replaces every item with a manually reviewed question covering controls, evidence roles, point binding, reaction reasoning, and mobile-safe fill blanks.

Actual rewritten question ids:

- `REBUILT_CH2_19_3_05_Q001`, `REBUILT_CH2_19_3_05_Q002`, `REBUILT_CH2_19_3_05_Q003`, `REBUILT_CH2_19_3_05_Q004`, `REBUILT_CH2_19_3_05_Q005`
- `REBUILT_CH2_19_3_05_Q006`, `REBUILT_CH2_19_3_05_Q007`, `REBUILT_CH2_19_3_05_Q008`, `REBUILT_CH2_19_3_05_Q009`, `REBUILT_CH2_19_3_05_Q010`
- `REBUILT_CH2_19_3_05_Q011`, `REBUILT_CH2_19_3_05_Q012`, `REBUILT_CH2_19_3_05_Q013`, `REBUILT_CH2_19_3_05_Q014`, `REBUILT_CH2_19_3_05_Q015`
- `REBUILT_CH2_19_3_05_Q016`, `REBUILT_CH2_19_3_05_Q017`, `REBUILT_CH2_19_3_05_Q018`, `REBUILT_CH2_19_3_05_Q019`, `REBUILT_CH2_19_3_05_Q020`
- `REBUILT_CH2_19_3_05_Q021`, `REBUILT_CH2_19_3_05_Q022`, `REBUILT_CH2_19_3_05_Q023`, `REBUILT_CH2_19_3_05_Q024`, `REBUILT_CH2_19_3_05_Q025`
- `REBUILT_CH2_19_3_05_Q026`, `REBUILT_CH2_19_3_05_Q027`, `REBUILT_CH2_19_3_05_Q028`, `REBUILT_CH2_19_3_05_Q029`, `REBUILT_CH2_19_3_05_Q030`

Keep but quality-edge question ids:

- None.

Evidence insufficient list:

- None.

## Evidence Insufficient List

- None.

## Per-Question Semantic Decisions

| Question | Decision | Evidence and semantic judgement |
| --- | --- | --- |
| `Q001` | rewrite | Compares AgNO₃ and no-AgNO₃ MnSO₄ systems; true two-point control question. |
| `Q002` | rewrite | Links observed color to MnO₄⁻ product; requires `00397/01241`. |
| `Q003` | rewrite | Mobile-safe color fill blank; short Chinese answer, theory-backed. |
| `Q004` | rewrite | Explains acidic medium requirement using operation text, thinking question, and theory. |
| `Q005` | rewrite | Water-bath heating purpose tied to reaction condition, not a generic speed claim. |
| `Q006` | rewrite | True/false on no-AgNO₃ control; direct experiment evidence. |
| `Q007` | rewrite | Clarifies Ag⁺ as catalyst/promoter rather than purple product. |
| `Q008` | rewrite | Mobile-safe fill blank for `催化/促进`; no Ag⁺ symbol answer. |
| `Q009` | rewrite | Reaction-choice item for Mn²⁺ to MnO₄⁻; uses Unicode formulas and theory ids. |
| `Q010` | rewrite | KI point observation target, supported by experiment and thinking question. |
| `Q011` | rewrite | I⁻ redox-role question; supported by KI point and thinking question. |
| `Q012` | rewrite | Mobile-safe fill blank `还原/还原性`; avoids I₂ formula input. |
| `Q013` | rewrite | Corrects reversed redox-direction claim for KI point. |
| `Q014` | rewrite | Cross-point oxidant role for K₂S₂O₈ in Mn²⁺ and I⁻ systems. |
| `Q015` | rewrite | S₂O₈²⁻ reduced product SO₄²⁻; theory-dependent. |
| `Q016` | rewrite | Distinguishes MnSO₄ and KI products; true multi-point comparison. |
| `Q017` | rewrite | Integrated true/false statement: K₂S₂O₈ oxidizes Mn²⁺ and I⁻. |
| `Q018` | rewrite | Point-binding check: KI-only stem should bind only KI point. |
| `Q019` | rewrite | Point-binding check: AgNO₃/no-AgNO₃ comparison must bind both MnSO₄ control points. |
| `Q020` | rewrite | Complete three-point mapping for the packet. |
| `Q021` | rewrite | Mobile-safe fill blank `氧化/氧化性`; avoids K₂S₂O₈ formula answer. |
| `Q022` | rewrite | Cross-experiment distractor filter; keeps packet scope clean. |
| `Q023` | rewrite | Control-design true/false item, not just reagent recall. |
| `Q024` | rewrite | Explains why the no-AgNO₃ control exists. |
| `Q025` | rewrite | Turns color recall into product-based reasoning via MnO₄⁻. |
| `Q026` | rewrite | Option-diagnostic question for KI point; identifies MnO₄⁻ purple as wrong-point transfer. |
| `Q027` | rewrite | Multi-point binding reasoning for S₂O₈²⁻ to SO₄²⁻ generalization. |
| `Q028` | rewrite | True/false point-mismatch item for KI versus Ag⁺/Mn²⁺ systems. |
| `Q029` | rewrite | Evidence-first question distinguishing operation text from theory-dependent product/color judgement. |
| `Q030` | rewrite | Learning-goal synthesis: Mn²⁺/I⁻ systems plus Ag⁺ control, not mere reagent/color recall. |

## Multi-Point Questions

- `Q001`: compares AgNO₃ and no-AgNO₃ MnSO₄ systems.
- `Q006`: mentions the no-AgNO₃ control as a comparison to the AgNO₃ system.
- `Q014`: generalizes K₂S₂O₈ as oxidant across Mn²⁺ and I⁻ systems.
- `Q016`: contrasts MnSO₄ product with KI product.
- `Q017`: integrated true/false across Mn²⁺ and I⁻ oxidation.
- `Q019`: asks which point bindings are justified for AgNO₃/no-AgNO₃ comparison.
- `Q020`: maps all three packet points.
- `Q023`: explains the purpose of comparing the two MnSO₄ systems.
- `Q024`: explains the no-AgNO₃ control relative to the AgNO₃ system.
- `Q026`: diagnoses KI-point confusion with the MnSO₄ purple MnO₄⁻ point.
- `Q027`: explains why S₂O₈²⁻ to SO₄²⁻ is a cross-point generalization.
- `Q028`: distinguishes KI point from Ag⁺/Mn²⁺ point.
- `Q030`: packet-level learning-goal synthesis across all points.

## Fill-Blank Mobile Risk

| Question | Accepted visible answer | Risk | Decision |
| --- | --- | --- | --- |
| `Q003` | `紫色`, `紫` | low | Keep as fill blank; ordinary color word, no formula. |
| `Q008` | `催化`, `催化作用`, `促进` | low | Keep as fill blank; ordinary Chinese term. |
| `Q012` | `还原`, `还原性` | low | Keep as fill blank; no I₂ formula answer. |
| `Q021` | `氧化`, `氧化性` | low | Keep as fill blank; no K₂S₂O₈ formula answer. |

Formula or symbol fill blanks:

- `0`

## Option-Link Review

All 21 single-choice questions have four options and four option links. Distractors are option-specific: wrong point, reversed redox direction, reagent-not-product, unrelated experiment, low-depth recall, overbinding, or underbinding. No option link is a generic unrelated-template diagnosis.

## Validation

- JSON parse: pass.
- Question count: pass, `30`.
- Unique question ids: pass.
- Single-choice answer labels align with options: pass.
- Single-choice option_links count equals options count: pass.
- All cited evidence ids resolve in the two required RAG JSONL files: pass.
- No publishable question has `evidence_sufficient=false`: pass.
- Visible ASCII digit formula check in student-facing stems/options/explanations: pass.
- Formula-like fill blank answer check: pass.
- Direct release JSON modification: not performed.

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
