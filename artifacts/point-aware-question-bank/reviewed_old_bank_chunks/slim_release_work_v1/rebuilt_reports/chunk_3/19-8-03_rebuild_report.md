# Rebuild Report: chunk_3 / 19-8-03

## Packet

- Experiment code: `19-8-03`
- Experiment title: `Sb(OH)3 的生成与性质`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-8-03.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-8-03_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `15` single choice, `8` true/false, `7` fill blank
- Keep / rewrite / reject: `13 / 17 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- point bindings for generation, acid branch, low-concentration base branch, and high-concentration base branch;
- protocol parent `expchunk_protocol_ccb6245e7635`;
- experiment purpose `expchunk_00290_963bb10320`;
- canonical operation evidence `expchunk_00295_b30319fd2c`;
- supporting theory `textbook_prose_00171_6743bd6e37` and `textbook_prose_00596_462a4c7dff`.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_8_03_Q004`
- `REBUILT_CH3_19_8_03_Q005`
- `REBUILT_CH3_19_8_03_Q006`
- `REBUILT_CH3_19_8_03_Q007`
- `REBUILT_CH3_19_8_03_Q009`
- `REBUILT_CH3_19_8_03_Q010`
- `REBUILT_CH3_19_8_03_Q013`
- `REBUILT_CH3_19_8_03_Q014`
- `REBUILT_CH3_19_8_03_Q019`
- `REBUILT_CH3_19_8_03_Q020`
- `REBUILT_CH3_19_8_03_Q023`
- `REBUILT_CH3_19_8_03_Q024`
- `REBUILT_CH3_19_8_03_Q025`
- `REBUILT_CH3_19_8_03_Q026`
- `REBUILT_CH3_19_8_03_Q027`
- `REBUILT_CH3_19_8_03_Q028`
- `REBUILT_CH3_19_8_03_Q029`

Major rewrite reasons:

- Canonical evidence directly supports generation, observation, centrifugation, acid-side testing, and two base-side tests.
- The packet has a real four-point structure: low-concentration and high-concentration sodium hydroxide branches must remain distinct.
- Canonical evidence says to test the precipitate's "作用" with acid/base, but does not directly record fixed dissolution outcomes for every branch.
- Formula, concentration, and valence fill blanks were converted to short Chinese answers such as `三氯化锑`, `两种浓度`, and `两性`.

## Kept But Edge

- `REBUILT_CH3_19_8_03_Q007`: keeps the stronger-base comparison, but avoids claiming a specific observed dissolution result.
- `REBUILT_CH3_19_8_03_Q008`: keeps the two-sided acid/base concept, with supporting theory used only for concept boundary.
- `REBUILT_CH3_19_8_03_Q010`: retains oxidation-state content as a single-choice Chinese valence question rather than a symbolic `III` fill blank.
- `REBUILT_CH3_19_8_03_Q013`: explicitly documents the evidence boundary around inherited dissolution wording.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- Generation-step questions bind `candidate-1-13921638`.
- Acid-side questions bind `candidate-2-330862ce`.
- Low-concentration base questions bind `candidate-3-842c2426`.
- High-concentration base questions bind `candidate-4-db0aa383`.
- Full workflow questions bind all four points only when the stem explicitly covers generation plus acid/base comparison.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_8_03_Q024` | `三氯化锑` | low | short reagent name |
| `REBUILT_CH3_19_8_03_Q025` | `氢氧化钠` | low | short reagent name |
| `REBUILT_CH3_19_8_03_Q026` | `沉淀` | low | short phenomenon term |
| `REBUILT_CH3_19_8_03_Q027` | `离心分离` | low | short operation term |
| `REBUILT_CH3_19_8_03_Q028` | `盐酸` | low | short reagent name |
| `REBUILT_CH3_19_8_03_Q029` | `两种浓度` | low | avoids numeric concentration input |
| `REBUILT_CH3_19_8_03_Q030` | `两性` | low | short concept term |

No visible fill-blank answer requires students to input a complex formula, ion, equation, valence symbol, numeric concentration, or ASCII chemical abbreviation.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00295_b30319fd2c`

Supporting theory evidence:

- `textbook_prose_00171_6743bd6e37`
- `textbook_prose_00596_462a4c7dff`

Rejected or narrowed inherited evidence:

- Direct dissolution claims were narrowed to acid/base "作用" tests unless the stem only asks conceptually.
- Numeric concentration fill blanks were rejected and represented as low/high concentration comparisons.
- Symbolic oxidation-state fill blank `III` was converted to a Chinese single-choice valence item.

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
