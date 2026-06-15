# Rebuild Report: chunk_3 / 19-8-01

## Packet

- Experiment code: `19-8-01`
- Experiment title: `Pb(OH)2 的生成与性质`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-8-01.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-8-01_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `15` single choice, `8` true/false, `7` fill blank
- Keep / rewrite / reject: `13 / 17 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- point bindings for `Pb(NO3)2 + NaOH`, `Pb(OH)2 + HNO3`, and `Pb(OH)2 + NaOH`;
- canonical protocol parent `expchunk_protocol_ccb6245e7635`;
- experiment purpose `expchunk_00290_963bb10320`;
- canonical operation evidence `expchunk_00295_b30319fd2c`;
- supporting amphoteric concept boundary `textbook_prose_00171_6743bd6e37`.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_8_01_Q002`
- `REBUILT_CH3_19_8_01_Q005`
- `REBUILT_CH3_19_8_01_Q006`
- `REBUILT_CH3_19_8_01_Q007`
- `REBUILT_CH3_19_8_01_Q011`
- `REBUILT_CH3_19_8_01_Q013`
- `REBUILT_CH3_19_8_01_Q014`
- `REBUILT_CH3_19_8_01_Q015`
- `REBUILT_CH3_19_8_01_Q021`
- `REBUILT_CH3_19_8_01_Q022`
- `REBUILT_CH3_19_8_01_Q023`
- `REBUILT_CH3_19_8_01_Q024`
- `REBUILT_CH3_19_8_01_Q025`
- `REBUILT_CH3_19_8_01_Q026`
- `REBUILT_CH3_19_8_01_Q027`
- `REBUILT_CH3_19_8_01_Q029`
- `REBUILT_CH3_19_8_01_Q030`

Major rewrite reasons:

- Canonical evidence directly supports adding sodium hydroxide solution to lead nitrate solution, observing the generated precipitate, and separately testing that precipitate with nitric acid and sodium hydroxide.
- Canonical evidence does not explicitly state the observed dissolution result in acid or excess base, so inherited direct claims such as "溶解" were rewritten as test-design, operation-order, or evidence-boundary questions.
- Old visible fill blanks requiring formulas or ions such as `Pb(OH)2`, `Pb(NO3)2`, `NaOH`, `HNO3`, and `Pb2+` were converted to short Chinese terms.
- Supporting theory is used only for the general amphoteric/acidity-basicity concept boundary and not as a substitute for missing direct observation evidence.

## Kept But Edge

- `REBUILT_CH3_19_8_01_Q004`: kept as a two-branch test question because the canonical operation explicitly says to test the generated precipitate with both nitric acid and sodium hydroxide.
- `REBUILT_CH3_19_8_01_Q008`: kept as an evidence-boundary question; it teaches that the current RAG supports testing the acid/base behavior rather than recording a fixed dissolution phenomenon.
- `REBUILT_CH3_19_8_01_Q009` and `Q010`: kept as concept questions because the experiment purpose asks students to master acidity/basicity of hydroxides, but they cite supporting theory where needed.
- `REBUILT_CH3_19_8_01_Q028`: kept as a short concept fill blank, not as a formula input.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- Generation-step questions bind `candidate-1-356d797d`.
- Acid-test questions bind `candidate-2-38e31e57`.
- Base-test questions bind `candidate-3-2d7041d5`.
- Comparison and evidence-boundary questions bind both acid-test and base-test points.
- Overall acid-base property questions may bind all three points when the stem covers the full design.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_8_01_Q024` | `氢氧化钠` | low | short reagent name |
| `REBUILT_CH3_19_8_01_Q025` | `硝酸铅` | low | short reagent name |
| `REBUILT_CH3_19_8_01_Q026` | `沉淀` | low | short phenomenon term |
| `REBUILT_CH3_19_8_01_Q027` | `硝酸` | low | short reagent name |
| `REBUILT_CH3_19_8_01_Q028` | `酸碱性` | low | short concept term |
| `REBUILT_CH3_19_8_01_Q029` | `两性` | low | short concept term |
| `REBUILT_CH3_19_8_01_Q030` | `碱` | low | one-character reagent class |

No visible fill-blank answer requires students to input a complex formula, ion, equation, valence symbol, or ASCII chemical abbreviation.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00295_b30319fd2c`

Supporting theory evidence:

- `textbook_prose_00171_6743bd6e37`

Rejected or narrowed inherited evidence:

- Direct "溶解" observation claims were narrowed to testing the generated precipitate with acid/base because the canonical chunk records the operation but not the final phenomenon.
- Formula-heavy fill blanks were rejected as mobile-risk visible answers.
- Supporting theory was not used to invent Pb-specific observations absent from the canonical experiment chunk.

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
