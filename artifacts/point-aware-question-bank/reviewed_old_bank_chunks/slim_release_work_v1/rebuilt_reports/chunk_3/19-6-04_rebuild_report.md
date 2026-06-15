# Rebuild Report: chunk_3 / 19-6-04

## Packet

- Experiment code: `19-6-04`
- Experiment title: `焰色反应`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_3\19-6-04.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_3\19-6-04_rebuilt_v1.json`
- Total questions: `30`
- Type counts: `16` single choice, `8` true/false, `6` fill blank
- Keep / rewrite / reject: `21 / 9 / 0`

## Manual Reconstruction Statement

This packet has been manually rebuilt question by question. It is not a script-batch generation and not a metadata-only normalization.

Each final question was rechecked against:

- original question and source intent;
- options, answer, and explanation;
- point bindings for Li, Na, K, Ca, Sr, Ba flame-test points plus the PDF note point;
- canonical operation evidence `expchunk_00271_54351c5c05`;
- potassium cobalt-glass note `expchunk_00274_a3569c9bb8`;
- supporting theory `textbook_prose_00982_e84c060b23`;
- table evidence `textbook_table_record_table_p163_t01_r011`.

## Rewrite List

Actual rewritten question ids:

- `REBUILT_CH3_19_6_04_Q006`
- `REBUILT_CH3_19_6_04_Q010`
- `REBUILT_CH3_19_6_04_Q011`
- `REBUILT_CH3_19_6_04_Q014`
- `REBUILT_CH3_19_6_04_Q015`
- `REBUILT_CH3_19_6_04_Q016`
- `REBUILT_CH3_19_6_04_Q021`
- `REBUILT_CH3_19_6_04_Q024`
- `REBUILT_CH3_19_6_04_Q029`

Major rewrite reasons:

- Old color answers were sometimes broader than the RAG table wording. The rebuilt packet uses table 18.4 exactly: Li `深红`, Na `黄`, K `紫`, Ca `橙红`, Sr `洋红`, Ba `绿`.
- Old operation questions over-bound all six ion points even when the stem asked for one ion's color.
- The potassium cobalt-glass fact is supported by experiment note `[3]`, not by the color table itself.
- Old distractors such as `CCl₄`, silver mirror, and brown ring were retained only as clearly diagnosed adjacent-experiment distractors.
- Visible fill blanks no longer require students to input ion symbols such as `Li+` or `Ca2+`.

## Kept But Edge

- `REBUILT_CH3_19_6_04_Q008`: kept as a combined K color plus cobalt-glass question; it deliberately uses both table evidence and note evidence.
- `REBUILT_CH3_19_6_04_Q012` and `Q013`: kept as theory questions, with source limited to the electronic excitation explanation in `textbook_prose_00982_e84c060b23`.
- `REBUILT_CH3_19_6_04_Q015`: kept as point-binding audit because this packet had systematic over-broad inherited bindings.
- `REBUILT_CH3_19_6_04_Q021`: uses a false statement to document that current RAG table says Ba is `绿`, not `黄绿色`.

## Evidence Insufficient

- 0

No final publishable question is marked `evidence_sufficient=false`.

## Multi-Point Questions

- Shared operation questions about nickel wire cleaning, chloride salt solutions, and recording all flame colors bind the six ion point keys.
- Specific color questions bind only the corresponding ion point.
- Potassium cobalt-glass questions bind `candidate-3-f31dc033` and may include `candidate-7-1ca24ae3` as a secondary PDF-note point.
- Theory questions bind all six ion points only when the stem explicitly asks about the general mechanism.

## Fill-Blank Mobile Risk

| Question | Visible answer | Risk | Action |
| --- | --- | --- | --- |
| `REBUILT_CH3_19_6_04_Q025` | `镍丝` | low | short tool name |
| `REBUILT_CH3_19_6_04_Q026` | `无色` | low | short state word |
| `REBUILT_CH3_19_6_04_Q027` | `钴玻璃` | low | short apparatus/material name |
| `REBUILT_CH3_19_6_04_Q028` | `黄` | low | table wording |
| `REBUILT_CH3_19_6_04_Q029` | `深红` | low | table wording |
| `REBUILT_CH3_19_6_04_Q030` | `焰色` | low | short observation term |

No visible fill-blank answer requires students to input a complex formula, ion, equation, valence symbol, or ASCII chemical abbreviation.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_protocol_8d70481ad785`
- `expchunk_00262_997e0530ee`
- `expchunk_00271_54351c5c05`
- `expchunk_00274_a3569c9bb8`

Supporting theory evidence:

- `textbook_prose_00982_e84c060b23`
- `textbook_table_context_p163_639c656c64`
- `textbook_table_record_table_p163_t01_r011`

Rejected or narrowed inherited evidence:

- Table colors were narrowed to the exact RAG table row rather than old broader aliases.
- Canonical operation questions no longer cite the theory paragraph unless the stem asks why flame colors occur.
- The cobalt-glass observation is tied to the experiment note instead of being treated as a generic table fact.

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
