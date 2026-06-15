# Rebuild Report: chunk_2 / 19-3-03 SO3(2-) 的检出

## Packet

- Packet id / experiment code: `19-3-03`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-3-03.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-03_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `single_choice=20`, `true_false=6`, `fill_blank=4`
- Statement: this packet has been manually read and semantically reconstructed question by question. It is not a script batch generation or metadata-only normalization.
- Manual audit phrase: manual per-question reconstruction, not batch generation.

## RAG Evidence Read

- `expchunk_00223_91cb040d8f` (`textbook_experiment_chunks_v1.jsonl`, line 236): experiment 19-3 preview asks students to review SO3(2-), SO4(2-), S2O3(2-), S2O8(2-), S(2-) properties and safety for experiments producing H2S or SO2.
- `expchunk_00224_166bfb5a4a` (`textbook_experiment_chunks_v1.jsonl`, line 237): SO2 safety text says SO2 is irritating and harmful; reactions producing SO2 should reduce escape and be conducted in a fume hood.
- `expchunk_00228_5e99fe31b9` (`textbook_experiment_chunks_v1.jsonl`, line 241): SO2 preparation and properties; SO2 reducing/oxidizing/bleaching operations; SO3(2-) detection text says SO4(2-) interferes and must be removed before verifying SO3(2-), and requires a separation scheme plus equations.
- `textbook_prose_01251_89ce24842f` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 1909): KMnO4 is deep purple / purple-red in water, supporting color-change reasoning.
- `textbook_prose_01253_29e4ee4b73` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 1908): in acidic medium MnO4- oxidizes SO3(2-) to SO4(2-), supporting higher-order KMnO4/SO3(2-) reasoning.
- `textbook_prose_00341_44241a0b9e` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 592): SO2 reacts with H2S to form sulfur and water, supporting SO2 oxidizing-property product reasoning.
- `textbook_prose_00344_07bf4af806` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 595): SO2 can combine with some organic dye molecules to form colorless organic substances, supporting bleaching explanation.

Rejected inherited theory ids:

- `textbook_prose_00340_77f9d61c94` and `textbook_prose_00363_d345af4100` were present in the old packet but were not used in the rebuilt package. They are related to SO2 / sulfite chemistry, but the final questions needing theory are better supported by the more specific KMnO4, H2S, and bleaching chunks listed above.

## Keep / Rewrite / Reject

- Keep: `0`
- Rewrite: `30`
- Reject: `0`

The source packet was not kept question-for-question because it contained repeated SO4(2-) interference items, repeated SO2 color/property items, formula or symbol fill blanks, generic option diagnostics, and broad point bindings. The rebuilt package replaces the source set with the manually reviewed ideal question set for this packet.

Actual rewritten question ids:

- `IDEAL_CH2_19_3_03_Q001`, `IDEAL_CH2_19_3_03_Q002`, `IDEAL_CH2_19_3_03_Q003`, `IDEAL_CH2_19_3_03_Q004`, `IDEAL_CH2_19_3_03_Q005`
- `IDEAL_CH2_19_3_03_Q006`, `IDEAL_CH2_19_3_03_Q007`, `IDEAL_CH2_19_3_03_Q008`, `IDEAL_CH2_19_3_03_Q009`, `IDEAL_CH2_19_3_03_Q010`
- `IDEAL_CH2_19_3_03_Q011`, `IDEAL_CH2_19_3_03_Q012`, `IDEAL_CH2_19_3_03_Q013`, `IDEAL_CH2_19_3_03_Q014`, `IDEAL_CH2_19_3_03_Q015`
- `IDEAL_CH2_19_3_03_Q016`, `IDEAL_CH2_19_3_03_Q017`, `IDEAL_CH2_19_3_03_Q018`, `IDEAL_CH2_19_3_03_Q019`, `IDEAL_CH2_19_3_03_Q020`
- `IDEAL_CH2_19_3_03_Q021`, `IDEAL_CH2_19_3_03_Q022`, `IDEAL_CH2_19_3_03_Q023`, `IDEAL_CH2_19_3_03_Q024`, `IDEAL_CH2_19_3_03_Q025`
- `IDEAL_CH2_19_3_03_Q026`, `IDEAL_CH2_19_3_03_Q027`, `IDEAL_CH2_19_3_03_Q028`, `IDEAL_CH2_19_3_03_Q029`, `IDEAL_CH2_19_3_03_Q030`

Keep but quality-edge question ids:

- None. Low-depth source items were rewritten into broader operation, safety, output, comparison, point-binding, or theory-dependent questions.

Evidence insufficient list:

- None.

## Evidence Insufficient List

- None.

## Per-Question Semantic Decisions

| Question | Decision | Evidence and semantic judgement |
| --- | --- | --- |
| `Q001` | rewrite | Directly asks why SO4(2-) is removed before SO3(2-) detection; supported by `expchunk_00228`; bound only to point 1. |
| `Q002` | rewrite | Converts repeated interference wording into a sequence question covering point 1 plus point 2; supported by `expchunk_00228`. |
| `Q003` | rewrite | True/false checks the false claim that SO4(2-) is irrelevant; deterministic and supported by `expchunk_00228`. |
| `Q004` | rewrite | Covers the required final deliverable, separation scheme and equations; supported by `expchunk_00228`; true multi-point. |
| `Q005` | rewrite | Explicit point-binding question distinguishing removal from verification; supported by `expchunk_00228`; true multi-point. |
| `Q006` | rewrite | Reverse-choice item where every option can be judged against experiment text; supported by `expchunk_00228`; true multi-point. |
| `Q007` | rewrite | Safety location for SO2 work; supported by `expchunk_00224` plus SO2 operation in `expchunk_00228`; bound to point 2. |
| `Q008` | rewrite | Safety reason for reducing SO2 escape; supported by `expchunk_00224`; replaces shallow SO2 location recall with rationale. |
| `Q009` | rewrite | Fill blank retained because answer is short ordinary Chinese `通风橱`; supported by `expchunk_00224`; phone safe. |
| `Q010` | rewrite | SO2 preparation apparatus reagent placement; supported by `expchunk_00228`; avoids unrelated distractors. |
| `Q011` | rewrite | True/false for slow acid addition into Na2SO3 setup; supported by `expchunk_00228`; no double negative. |
| `Q012` | rewrite | Integrates slow addition with fume-hood safety; supported by `expchunk_00224` and `expchunk_00228`. |
| `Q013` | rewrite | Operation matching for SO2 reducing-property observation; experiment evidence alone sufficient. |
| `Q014` | rewrite | Requires supporting theory for KMnO4 color and acidic oxidation; cites `01251` and `01253`. |
| `Q015` | rewrite | True/false reaction judgement from `01253`; theory-dependent and deterministic. |
| `Q016` | rewrite | Higher-order reaction equation choice using Unicode subscripts/superscripts; theory-dependent on `01253`. |
| `Q017` | rewrite | Operation matching for SO2 oxidizing-property observation; supported by `expchunk_00228`. |
| `Q018` | rewrite | Product judgement for SO2 + H2S; canonical operation plus theory chunk `00341`. |
| `Q019` | rewrite | Distinguishes SO2 oxidizing operation from SO4(2-) interference removal; true cross-point comparison. |
| `Q020` | rewrite | Operation matching for SO2 bleaching; supported by `expchunk_00228`. |
| `Q021` | rewrite | Theory explanation for bleaching; cites `00344`, not merely experiment operation. |
| `Q022` | rewrite | Fill blank retained because answer `漂白` / `漂白作用` is a short Chinese word; cites `00344`. |
| `Q023` | rewrite | Integrates three SO2 property observations; supported by `expchunk_00228`; reduces duplicate single-property recall. |
| `Q024` | rewrite | Checks completeness of the SO3(2-) detection task; true multi-point and supported by `expchunk_00228`. |
| `Q025` | rewrite | Filters out cross-experiment distractors; supported by SO2 reducing-property operation in `expchunk_00228`. |
| `Q026` | rewrite | Uses preview chunk to broaden coverage beyond the same experiment paragraph; true multi-point preparation relevance. |
| `Q027` | rewrite | Fill blank retained because answer `示意图` is short Chinese; supported by `expchunk_00228`; multi-point deliverable. |
| `Q028` | rewrite | Fill blank retained because answer `方程式` / `反应方程式` is short Chinese; supported by `expchunk_00228`. |
| `Q029` | rewrite | Explicitly tests when multi-point binding is warranted; supported by `expchunk_00228`; true multi-point. |
| `Q030` | rewrite | Role distinction between target SO3(2-) and interfering SO4(2-); supported by `expchunk_00228`; true multi-point. |

## Multi-Point Questions

- `Q002`: point 1 removes SO4(2-) interference; point 2 verifies SO3(2-) afterward.
- `Q004`: asks the complete final deliverable, which includes separation and verification output.
- `Q005`: directly asks how the two video points differ.
- `Q006`: judges the full SO3(2-) detection task, including both separation and verification.
- `Q019`: contrasts SO2 property observation with SO4(2-) interference removal.
- `Q024`: states that SO2 property observation alone is insufficient without the SO4(2-) handling task.
- `Q026`: preview knowledge supports both interference removal and target verification.
- `Q027`: final written separation schematic belongs to the combined detection task.
- `Q028`: final equation requirement belongs to the combined detection task.
- `Q029`: asks explicitly which point binding is correct for a two-step stem.
- `Q030`: distinguishes target ion and interference ion, so both points are semantically relevant.

## Fill-Blank Mobile Risk

| Question | Accepted visible answer | Risk | Decision |
| --- | --- | --- | --- |
| `Q009` | `通风橱` | low | Keep as fill blank; ordinary Chinese noun, no formula input. |
| `Q022` | `漂白`, `漂白作用` | low | Keep as fill blank; ordinary Chinese term, deterministic aliases. |
| `Q027` | `示意图` | low | Keep as fill blank; ordinary Chinese term, direct from source text. |
| `Q028` | `方程式`, `反应方程式` | low | Keep as fill blank; ordinary Chinese term, no formula required. |

Formula or symbol fill blanks:

- `0`

## Option-Link Review

All 20 single-choice questions have four options and four option links. Correct options point to the relevant experiment point where applicable; distractors are concrete wrong-experiment or misconception choices, such as Fe3+/KSCN, CCl4 iodine extraction, brown-ring nitrate testing, BaSO4 precipitation, or irrelevant apparatus/reagent choices. No option link is accepted as a generic "unrelated" template without option-specific meaning.

## Validation

- JSON parse: pass.
- Question count: pass, `30`.
- Unique question ids: pass.
- Single-choice answer labels align with options: pass.
- Single-choice option_links count equals options count: pass.
- All cited evidence ids resolve in the two required RAG JSONL files: pass.
- No publishable question has `evidence_sufficient=false`: pass.
- Visible ASCII digit formula check: pass. Student-facing formulas in the rebuilt JSON use Unicode subscripts/superscripts; reaction coefficients are not used as formula subscripts.
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
