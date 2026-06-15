# Rebuild Report: chunk_3 / 19-6-02

## Packet

- Experiment code: `19-6-02`
- Experiment title: `金属镁燃烧`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-6-02.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-6-02_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `17` single choice, `8` true/false, `5` fill blank
- Keep / rewrite / reject: `6 / 24 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization. The previous script-generated output for this packet was replaced.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- `candidate-1-a3329021` / `candidate-2-ea144d3d`;
- canonical RAG evidence `expchunk_00266_c041a8c010` and `expchunk_00267_6f29b82f65`;
- supporting theory when the question goes beyond the canonical operation text.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_6_02_Q003`
- `REBUILT_CH3_19_6_02_Q004`
- `REBUILT_CH3_19_6_02_Q005`
- `REBUILT_CH3_19_6_02_Q006`
- `REBUILT_CH3_19_6_02_Q007`
- `REBUILT_CH3_19_6_02_Q008`
- `REBUILT_CH3_19_6_02_Q009`
- `REBUILT_CH3_19_6_02_Q010`
- `REBUILT_CH3_19_6_02_Q012`
- `REBUILT_CH3_19_6_02_Q013`
- `REBUILT_CH3_19_6_02_Q014`
- `REBUILT_CH3_19_6_02_Q015`
- `REBUILT_CH3_19_6_02_Q016`
- `REBUILT_CH3_19_6_02_Q017`
- `REBUILT_CH3_19_6_02_Q019`
- `REBUILT_CH3_19_6_02_Q020`
- `REBUILT_CH3_19_6_02_Q022`
- `REBUILT_CH3_19_6_02_Q023`
- `REBUILT_CH3_19_6_02_Q024`
- `REBUILT_CH3_19_6_02_Q026`
- `REBUILT_CH3_19_6_02_Q027`
- `REBUILT_CH3_19_6_02_Q028`
- `REBUILT_CH3_19_6_02_Q029`
- `REBUILT_CH3_19_6_02_Q030`

Major rewrite reasons:

- Old questions repeatedly asked white light, product color, `MgO`, oxidant, and redox category with small wording changes.
- Canonical RAG text says to ignite magnesium and observe phenomena, but does not directly provide the white-light or white-solid observation wording.
- Formula fill blanks such as `MgO` were not phone-safe.
- Several old option links were template-like and did not explain the actual wrong experiment or wrong evidence boundary.
- Some old point bindings were too broad or used theory ids where the final stem did not need theory.

## Kept But Edge

- `REBUILT_CH3_19_6_02_Q001`: kept as the package workflow anchor, but options and diagnostics were rewritten to distinguish magnesium combustion from nearby sodium, water, amalgam, and flame-test operations.
- `REBUILT_CH3_19_6_02_Q002`: kept as a low-level anchor because surface oxide removal is central and directly evidenced; retained despite low difficulty.
- `REBUILT_CH3_19_6_02_Q011`: kept because activity comparison is supported by the RAG section title and follow-up summary instruction; explanation was tightened.
- `REBUILT_CH3_19_6_02_Q018`: kept as a true/false form of the activity-summary evidence, with line-level RAG grounding.
- `REBUILT_CH3_19_6_02_Q021`: kept as phone-safe fill blank; visible answer is `氧化层`, with `氧化膜` only as hidden alias.
- `REBUILT_CH3_19_6_02_Q025`: kept as short fill blank for `活泼性`; simple but directly supported by `expchunk_00267_6f29b82f65`.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- `REBUILT_CH3_19_6_02_Q001`: requires both pre-ignition surface treatment and post-ignition observation, so both points are real.
- `REBUILT_CH3_19_6_02_Q007`: explicitly asks how to bind a stem covering both treatment and observation.
- `REBUILT_CH3_19_6_02_Q015`: true/false point-binding question; both point keys are semantically required.
- `REBUILT_CH3_19_6_02_Q027`: explains why the “directly add water” distractor fails against the full magnesium combustion workflow.
- `REBUILT_CH3_19_6_02_Q030`: package-coverage question spans operation and observation plus theory boundary.

Questions that only ask surface treatment are single-point `candidate-1-a3329021`; questions that only ask observation/product boundary are single-point `candidate-2-ea144d3d`.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_6_02_Q021` | `氧化层` | low | `氧化膜` kept only as hidden alias |
| `REBUILT_CH3_19_6_02_Q022` | `点燃` | low | short ordinary Chinese action |
| `REBUILT_CH3_19_6_02_Q023` | `观察现象` | low | replaces unsupported white-light fill |
| `REBUILT_CH3_19_6_02_Q024` | `普通氧化物` | low | replaces visible `MgO` formula fill |
| `REBUILT_CH3_19_6_02_Q025` | `活泼性` | low | short ordinary Chinese answer |

No visible fill-blank answer requires students to input a complex formula, ion, equation, or valence symbol.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_8d70481ad785`
- `expchunk_00266_c041a8c010`
- `expchunk_00267_6f29b82f65`

Supporting theory evidence:

- `textbook_table_record_table_p158_t01_r011`
- `textbook_prose_00272_faa84a49a8`

Rejected or narrowed inherited evidence:

- Old uses of `textbook_table_record_table_p158_t01_r011` were removed from questions that only ask operation sequence, surface treatment, point binding, or observation task.
- White-light and white-solid claims were not retained as direct fact questions because current RAG locators do not directly provide those observation/color statements.
- `MgO` visible fill was replaced with `普通氧化物` theory-backed short fill.

## Validation

- JSON parse: pass
- Question count: `30`
- Unique question ids: pass
- Single-choice answers align with option labels: pass
- Single-choice option_links count equals options count: pass
- All cited evidence ids found in RAG JSONL: pass
- Visible ASCII digit formula in fill answers: `0`
- Formula-like visible fill answers: `0`
- Missing explanations: `0`
- Evidence-insufficient publishable questions: `0`
- Direct release JSON modification: none


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
