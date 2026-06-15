# Rebuild Report: chunk_3 / 19-6-03

## Packet

- Experiment code: `19-6-03`
- Experiment title: `与水的作用`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-6-03.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-6-03_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `18` single choice, `8` true/false, `4` fill blank
- Keep / rewrite / reject: `20 / 10 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- five point bindings: `candidate-1-0b2d08c4`, `candidate-2-60fd99ae`, `candidate-3-5b0d55cf`, `candidate-4-8ec447f5`, `candidate-5-b36777e1`;
- canonical RAG evidence `expchunk_00266_c041a8c010` and `expchunk_00267_6f29b82f65`;
- supporting theory `textbook_prose_00936_0b5113eb41` and `textbook_prose_00937_503d9709b5` when a question goes beyond the canonical operation text.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_6_03_Q004`
- `REBUILT_CH3_19_6_03_Q008`
- `REBUILT_CH3_19_6_03_Q010`
- `REBUILT_CH3_19_6_03_Q012`
- `REBUILT_CH3_19_6_03_Q015`
- `REBUILT_CH3_19_6_03_Q016`
- `REBUILT_CH3_19_6_03_Q017`
- `REBUILT_CH3_19_6_03_Q018`
- `REBUILT_CH3_19_6_03_Q024`
- `REBUILT_CH3_19_6_03_Q026`

Major rewrite reasons:

- Old questions mixed canonical operation evidence with theory-only conclusions such as specific alkalinity and gas generation.
- `H₂`, `Na`, `Ca(OH)₂`, and `Fe(NO)SO₄` appeared in visible old fill blanks or unrelated distractors; these were converted to Chinese single choice, true/false, or short safe fill blanks.
- Old option links were often template-like and did not diagnose the actual wrong subexperiment.
- Some five-point bindings were overbroad; only package-goal questions retain all five point keys.
- The `candidate-2` potassium point is retained for comparison and theory questions, but not framed as a required hands-on operation.

## Kept But Edge

- `REBUILT_CH3_19_6_03_Q009`: kept as a potassium-vs-sodium comparison, but marked as supporting-theory dependent.
- `REBUILT_CH3_19_6_03_Q011`: kept for potassium reaction risk, with evidence from `textbook_prose_00936_0b5113eb41`.
- `REBUILT_CH3_19_6_03_Q013`: kept for magnesium hot-water reasoning, using canonical cold/hot setup plus theory that magnesium reacts with water under heating.
- `REBUILT_CH3_19_6_03_Q014`, `Q025`, and `Q030`: kept as package-level activity-summary questions because `expchunk_00267_6f29b82f65` explicitly asks for the activity summary.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- Sodium/potassium setup questions bind `candidate-1-0b2d08c4` and `candidate-2-60fd99ae` only when the stem explicitly covers the shared Na/K operation.
- Magnesium comparison questions bind `candidate-3-5b0d55cf` and `candidate-4-8ec447f5` only when the stem explicitly requires cold-water and hot-water contrast.
- Calcium questions are single-point `candidate-5-b36777e1` unless they are package-level comparison questions.
- All-five bindings are reserved for activity-summary or package-scope boundary questions.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_6_03_Q027` | `煤油` | low | short canonical material |
| `REBUILT_CH3_19_6_03_Q028` | `漏斗` | low | short apparatus name |
| `REBUILT_CH3_19_6_03_Q029` | `热` | low | one-character condition word |
| `REBUILT_CH3_19_6_03_Q030` | `活泼性` | low | short package-goal term |

No visible fill-blank answer requires students to input a complex formula, ion, equation, valence symbol, or ASCII chemical abbreviation.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_8d70481ad785`
- `expchunk_00266_c041a8c010`
- `expchunk_00267_6f29b82f65`

Supporting theory evidence:

- `textbook_prose_00936_0b5113eb41`
- `textbook_prose_00937_503d9709b5`

Rejected or narrowed inherited evidence:

- Direct `NaOH`/`Ca(OH)₂` formula-fill style questions were not retained as visible fill blanks.
- The old brown-ring distractor was not retained as a chemistry fact question because it is outside this water-reaction packet.
- Canonical-operation questions no longer cite theory ids unless the stem asks for products, relative violence, or reaction conditions.

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
