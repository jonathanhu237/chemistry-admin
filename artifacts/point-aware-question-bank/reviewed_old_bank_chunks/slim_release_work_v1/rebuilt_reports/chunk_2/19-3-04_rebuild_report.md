# Rebuild Report: chunk_2 / 19-3-04 性质

## Packet

- Packet id / experiment code: `19-3-04`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-3-04.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_2\19-3-04_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `single_choice=21`, `true_false=5`, `fill_blank=4`
- Statement: this packet has been manually read and semantically reconstructed question by question. It is not a script batch generation or metadata-only normalization.
- Manual audit phrase: manual per-question reconstruction, not batch generation.

## RAG Evidence Read

- `expchunk_00230_5e24188739` (`textbook_experiment_chunks_v1.jsonl`, line 243): canonical property-test instructions. The experiment dissolves self-made Na₂S₂O₃ crystals and performs four tests: HCl, iodine water, chlorine water followed by SO₄²⁻ verification, and AgNO₃ with observation of precipitate, color change, and coordination dissolution.
- `textbook_prose_00391_2e025ffdda` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 654): sodium thiosulfate is stable in neutral or alkaline conditions but decomposes in acidic conditions to sulfur and SO₂.
- `textbook_prose_00392_f9643d7706` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 655): gives acid decomposition of S₂O₃²⁻ and states thiosulfate has reducing property used in iodometry.
- `textbook_prose_00393_2db98879c2` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 656): thiosulfate reduces iodine to iodide while forming tetrathionate.
- `textbook_prose_00394_04911a6294` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 657): strong oxidants oxidize sodium thiosulfate to sulfate; thiosulfate has good coordination ability with metal ions.
- `textbook_prose_00395_7ea078c59f` (`textbook_inorganic_lower_chunks_v1.jsonl`, line 658): silver halide dissolves in Na₂S₂O₃ by forming a stable silver thiosulfate complex.

Inherited id handling:

- `expchunk_00229_23988fd5d4` was present in the source packet as a candidate locator, but it describes preparation rather than the four property video points. It was not cited in final question audits.
- The old packet repeatedly attached all theory ids to many questions. The rebuilt package narrows theory ids question by question: acid decomposition uses `00391/00392`, iodine uses `00393`, chlorine oxidation uses `00394`, and Ag⁺ coordination uses `00394/00395`.

## Keep / Rewrite / Reject

- Keep: `0`
- Rewrite: `30`
- Reject: `0`

The source packet contained several usable surface facts, but too many items repeated the same low-depth reagent/phenomenon pattern and broad theory bindings. The rebuilt set rewrites all questions to cover operation, observation, reasoning, point binding, evidence choice, and mobile-safe fill blanks.

Actual rewritten question ids:

- `REBUILT_CH2_19_3_04_Q001`, `REBUILT_CH2_19_3_04_Q002`, `REBUILT_CH2_19_3_04_Q003`, `REBUILT_CH2_19_3_04_Q004`, `REBUILT_CH2_19_3_04_Q005`
- `REBUILT_CH2_19_3_04_Q006`, `REBUILT_CH2_19_3_04_Q007`, `REBUILT_CH2_19_3_04_Q008`, `REBUILT_CH2_19_3_04_Q009`, `REBUILT_CH2_19_3_04_Q010`
- `REBUILT_CH2_19_3_04_Q011`, `REBUILT_CH2_19_3_04_Q012`, `REBUILT_CH2_19_3_04_Q013`, `REBUILT_CH2_19_3_04_Q014`, `REBUILT_CH2_19_3_04_Q015`
- `REBUILT_CH2_19_3_04_Q016`, `REBUILT_CH2_19_3_04_Q017`, `REBUILT_CH2_19_3_04_Q018`, `REBUILT_CH2_19_3_04_Q019`, `REBUILT_CH2_19_3_04_Q020`
- `REBUILT_CH2_19_3_04_Q021`, `REBUILT_CH2_19_3_04_Q022`, `REBUILT_CH2_19_3_04_Q023`, `REBUILT_CH2_19_3_04_Q024`, `REBUILT_CH2_19_3_04_Q025`
- `REBUILT_CH2_19_3_04_Q026`, `REBUILT_CH2_19_3_04_Q027`, `REBUILT_CH2_19_3_04_Q028`, `REBUILT_CH2_19_3_04_Q029`, `REBUILT_CH2_19_3_04_Q030`

Keep but quality-edge question ids:

- None.

Evidence insufficient list:

- None.

## Evidence Insufficient List

- None.

## Per-Question Semantic Decisions

| Question | Decision | Evidence and semantic judgement |
| --- | --- | --- |
| `Q001` | rewrite | HCl observation plus acid-decomposition theory; supports浑浊 and SO₂ generation. |
| `Q002` | rewrite | Product judgement:浑浊 comes from sulfur; requires `00391/00392`. |
| `Q003` | rewrite | False absolute statement about acid stability; deterministic and theory-backed. |
| `Q004` | rewrite | Mobile-safe fill blank for `硫`; no visible formula answer. |
| `Q005` | rewrite | True multi-point condition question: acid instability affects iodine-water judgement. |
| `Q006` | rewrite | Iodine water indicates reducing property; operation from canonical, property from `00393`. |
| `Q007` | rewrite | Theory product choice: iodine is reduced to I⁻; uses `00393`. |
| `Q008` | rewrite | Mobile-safe fill blank `还原/还原性`; not a formula answer. |
| `Q009` | rewrite | Rejects misconception that iodine point is coordination precipitation. |
| `Q010` | rewrite | Distinguishes HCl point from iodine point; real two-point comparison. |
| `Q011` | rewrite | Direct canonical question: chlorine-water point verifies SO₄²⁻. |
| `Q012` | rewrite | Explains chlorine as oxidant; requires `00394`. |
| `Q013` | rewrite | True/false point distinction between chlorine-water and iodine-water operations. |
| `Q014` | rewrite | Explains why SO₄²⁻ is verified after chlorine; theory-backed reasoning. |
| `Q015` | rewrite | Compares HCl acid decomposition with chlorine oxidation; true multi-point. |
| `Q016` | rewrite | AgNO₃ operation sequence from canonical experiment text. |
| `Q017` | rewrite | AgNO₃ observation requirements from canonical experiment text. |
| `Q018` | rewrite | Ag⁺ coordination/complexing property; requires `00394/00395`. |
| `Q019` | rewrite | Evidence-choice question linking AgNO₃ point to silver thiosulfate complex theory. |
| `Q020` | rewrite | Mobile-safe fill blank `配位/络合`; no complex formula input. |
| `Q021` | rewrite | False absolute statement about no precipitate; direct canonical support. |
| `Q022` | rewrite | Scope question separating true packet operations from Co²⁺ distractor. |
| `Q023` | rewrite | Complete four-point mapping; broadens coverage beyond repeated single-property recall. |
| `Q024` | rewrite | Mobile-safe fill blank `酸/酸性`; theory-backed acid-stability concept. |
| `Q025` | rewrite | Point-binding check: AgNO₃-only stem must not inherit broad multi-point binding. |
| `Q026` | rewrite | Point-binding check: four-operation comparison legitimately binds all four points. |
| `Q027` | rewrite | Integrated reagent-property mapping across all four points. |
| `Q028` | rewrite | True/false integrated property map; no double negative. |
| `Q029` | rewrite | Evidence-first question distinguishing operation text from theory-dependent product judgement. |
| `Q030` | rewrite | Requires reasoning from iodine-water observation to reducing-property meaning. |

## Multi-Point Questions

- `Q005`: compares HCl acid instability with iodine-water reducing-property judgement.
- `Q010`: distinguishes HCl point from iodine-water point.
- `Q013`: distinguishes chlorine-water point from iodine-water point.
- `Q015`: compares HCl acid decomposition products with chlorine oxidation to SO₄²⁻.
- `Q022`: scope question references the packet's true operations and distractors.
- `Q023`: maps all four property points.
- `Q026`: explicitly asks when all four point bindings are justified.
- `Q027`: integrates all four reagent-property mappings.
- `Q028`: integrated true/false property map across all four points.

## Fill-Blank Mobile Risk

| Question | Accepted visible answer | Risk | Decision |
| --- | --- | --- | --- |
| `Q004` | `硫` | low | Keep as fill blank; ordinary Chinese answer, no symbol alias exposed. |
| `Q008` | `还原`, `还原性` | low | Keep as fill blank; ordinary Chinese chemistry term. |
| `Q020` | `配位`, `络合` | low | Keep as fill blank; no complex formula required. |
| `Q024` | `酸`, `酸性` | low | Keep as fill blank; ordinary Chinese condition term. |

Formula or symbol fill blanks:

- `0`

## Option-Link Review

All 21 single-choice questions have four options and four option links. Distractors are option-specific: wrong point, reversed redox direction, unrelated experiment, impossible product, overbinding, underbinding, or incomplete scope. The report and JSON do not rely on generic option diagnostics.

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
