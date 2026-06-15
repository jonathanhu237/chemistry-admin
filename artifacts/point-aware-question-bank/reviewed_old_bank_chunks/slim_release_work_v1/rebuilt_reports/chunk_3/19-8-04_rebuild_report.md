# Rebuild Report: chunk_3 / 19-8-04

## Packet

- Experiment code: `19-8-04`
- Experiment title: `Bi(OH)3 的生成与性质`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-8-04.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-8-04_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `15` single choice, `8` true/false, `7` fill blank
- Keep / rewrite / reject: `19 / 11 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- point bindings for generation, acid branch, 6 mol/L sodium hydroxide branch, and 40% sodium hydroxide branch;
- protocol parent `expchunk_protocol_ccb6245e7635`;
- experiment purpose `expchunk_00290_963bb10320`;
- safety evidence `expchunk_00293_a6262c57db`;
- canonical operation evidence `expchunk_00295_b30319fd2c`;
- supporting theory `textbook_prose_00596_462a4c7dff`.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_8_04_Q004`
- `REBUILT_CH3_19_8_04_Q006`
- `REBUILT_CH3_19_8_04_Q009`
- `REBUILT_CH3_19_8_04_Q012`
- `REBUILT_CH3_19_8_04_Q013`
- `REBUILT_CH3_19_8_04_Q014`
- `REBUILT_CH3_19_8_04_Q017`
- `REBUILT_CH3_19_8_04_Q024`
- `REBUILT_CH3_19_8_04_Q025`
- `REBUILT_CH3_19_8_04_Q027`
- `REBUILT_CH3_19_8_04_Q030`

Major rewrite reasons:

- Canonical evidence directly supports generation, observation, centrifugation, acid-side testing, and two strong-base conditions.
- Old direct dissolution wording was narrowed to "作用" or to supporting-theory-backed acid/base tendencies.
- Safety questions were tied to the experiment safety chunk rather than reaction-operation evidence.
- Formula, ion, and concentration fill blanks were converted to short Chinese answers.

## Kept But Edge

- `REBUILT_CH3_19_8_04_Q004`: keeps the "偏碱性" idea, but treats it as acid-side action plus supporting theory, not as a direct phenomenon quote.
- `REBUILT_CH3_19_8_04_Q006` and `Q030`: use supporting theory for the As/Sb/Bi acid-base trend.
- `REBUILT_CH3_19_8_04_Q012`: keeps the strong-base comparison purpose while avoiding a fixed base-solubility claim.
- `REBUILT_CH3_19_8_04_Q013`: explicitly records the evidence boundary around inherited acid-side dissolution wording.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- Generation-step questions bind `candidate-1-a4e9dd30`.
- Acid-side questions bind `candidate-2-7e4abe55`.
- Regular strong-base questions bind `candidate-3-fa887f71`.
- Highest-concentration strong-base questions bind `candidate-4-6daac070`.
- Full workflow questions bind all four points only when the stem explicitly covers the complete sequence.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_8_04_Q024` | `氢氧化钠` | low | short reagent name |
| `REBUILT_CH3_19_8_04_Q025` | `盐酸` | low | short reagent name |
| `REBUILT_CH3_19_8_04_Q026` | `氢氧化铋` | low | short compound name |
| `REBUILT_CH3_19_8_04_Q027` | `沉淀` | low | short phenomenon term |
| `REBUILT_CH3_19_8_04_Q028` | `氢氧化物` | low | short module name |
| `REBUILT_CH3_19_8_04_Q029` | `回收` | low | short safety action |
| `REBUILT_CH3_19_8_04_Q030` | `较弱` | low | short concept comparison |

No visible fill-blank answer requires students to input a complex formula, ion, equation, valence symbol, numeric concentration, or ASCII chemical abbreviation.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00293_a6262c57db`
- `expchunk_00295_b30319fd2c`

Supporting theory evidence:

- `textbook_prose_00596_462a4c7dff`

Rejected or narrowed inherited evidence:

- Direct acid-side dissolution language was narrowed to a salt-acid action test.
- "任意稀碱易溶" was rejected as an overclaim.
- `Bi3+`, formula, and numeric concentration fill blanks were rejected as mobile-risk answers.

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
