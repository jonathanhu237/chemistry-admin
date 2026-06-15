# Rebuild Report: chunk_3 / 19-8-02

## Packet

- Experiment code: `19-8-02`
- Experiment title: `Sn(OH)2 的生成与性质`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-8-02.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-8-02_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `15` single choice, `8` true/false, `7` fill blank
- Keep / rewrite / reject: `15 / 15 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- point bindings for `SnCl2 + NaOH`, `Sn(OH)2 + HCl`, and `Sn(OH)2 + NaOH`;
- protocol parent `expchunk_protocol_ccb6245e7635`;
- experiment purpose `expchunk_00290_963bb10320`;
- canonical operation evidence `expchunk_00295_b30319fd2c`;
- adjacent-scope guard chunks `expchunk_00297_c03527ab79` and `expchunk_00298_68f5de393c`;
- supporting amphoteric concept boundary `textbook_prose_00171_6743bd6e37`.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_8_02_Q003`
- `REBUILT_CH3_19_8_02_Q006`
- `REBUILT_CH3_19_8_02_Q007`
- `REBUILT_CH3_19_8_02_Q008`
- `REBUILT_CH3_19_8_02_Q009`
- `REBUILT_CH3_19_8_02_Q013`
- `REBUILT_CH3_19_8_02_Q014`
- `REBUILT_CH3_19_8_02_Q015`
- `REBUILT_CH3_19_8_02_Q017`
- `REBUILT_CH3_19_8_02_Q020`
- `REBUILT_CH3_19_8_02_Q024`
- `REBUILT_CH3_19_8_02_Q025`
- `REBUILT_CH3_19_8_02_Q027`
- `REBUILT_CH3_19_8_02_Q028`
- `REBUILT_CH3_19_8_02_Q029`

Major rewrite reasons:

- Canonical evidence directly supports generating the precipitate, observing it, centrifuging it, and separately testing the precipitate with hydrochloric acid and sodium hydroxide.
- Canonical evidence does not directly record a fixed dissolution result for both branches, so inherited "溶解" claims were narrowed to operation design or evidence-boundary questions.
- Old fill blanks requiring `SnCl2`, `Sn(OH)2`, `NaOH`, `HCl`, or `+2` were converted to short Chinese answers.
- Adjacent content such as Pb(IV) oxidation and SnCl2 hydrolysis is used only as a distractor/scope guard, not as direct support for this packet's final answers.

## Kept But Edge

- `REBUILT_CH3_19_8_02_Q005`: kept as the packet's core acid-base purpose question, with supporting theory used only to define "两性".
- `REBUILT_CH3_19_8_02_Q010`: keeps the old scope-exclusion idea; the adjacent Pb(IV) chunk is cited only to confirm the distractor is out of packet scope.
- `REBUILT_CH3_19_8_02_Q012` and `Q021`: keep the idea that precipitate generation alone is insufficient for discussing two-sided acid/base behavior.
- `REBUILT_CH3_19_8_02_Q030`: retains the concept answer `两性`, but avoids symbolic oxidation-state or formula input.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- Generation-step questions bind `candidate-1-f427ce6a`.
- Acid-side questions bind `candidate-2-fbc03df9`.
- Base-side questions bind `candidate-3-3c35df6d`.
- Sequence and two-sided acid-base questions bind all three point keys when the stem explicitly covers the full workflow.
- Adjacent-scope distractor questions cite adjacent RAG chunks only for exclusion, not as positive answer evidence.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_8_02_Q024` | `氢氧化钠` | low | short reagent name |
| `REBUILT_CH3_19_8_02_Q025` | `氯化亚锡` | low | short reagent name |
| `REBUILT_CH3_19_8_02_Q026` | `沉淀` | low | short phenomenon term |
| `REBUILT_CH3_19_8_02_Q027` | `离心分离` | low | short operation term |
| `REBUILT_CH3_19_8_02_Q028` | `盐酸` | low | short reagent name |
| `REBUILT_CH3_19_8_02_Q029` | `氢氧化钠` | low | short reagent name |
| `REBUILT_CH3_19_8_02_Q030` | `两性` | low | short concept term |

No visible fill-blank answer requires students to input a complex formula, ion, equation, valence symbol, or ASCII chemical abbreviation.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00295_b30319fd2c`
- `expchunk_00297_c03527ab79`
- `expchunk_00298_68f5de393c`

Supporting theory evidence:

- `textbook_prose_00171_6743bd6e37`

Rejected or narrowed inherited evidence:

- Direct "溶解" claims were narrowed to testing the generated precipitate with acid/base because the canonical chunk records the operation but not the final phenomenon.
- Formula and valence fill blanks were rejected as mobile-risk visible answers.
- Adjacent SnCl2 hydrolysis and Pb(IV) oxidation content was not allowed to replace the packet's own hydroxide-properties workflow.

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
