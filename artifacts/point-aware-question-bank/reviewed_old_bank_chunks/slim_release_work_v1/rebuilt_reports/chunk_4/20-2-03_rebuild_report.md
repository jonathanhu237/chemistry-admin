# Rebuild Report: 20-2-03

- Packet id: `EXP_20_2_03`
- Experiment code: `20-2-03`
- Experiment title: 铁(III)、钴(III)和镍(III)的氧化性
- Chunk: `chunk_4`
- Source packet: `semantic_work_packets/chunk_4/20-2-03.json`
- Rebuilt JSON: `rebuilt_packages/chunk_4/20-2-03_rebuilt_v1.json`
- Release JSON direct modification: prohibited and not performed

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep after manual tightening: `0`
- Rewrite: `30`
- Reject: `0`

## Rewrite List

- `REV_CH4_EXP_20_2_03_Q001` through `REV_CH4_EXP_20_2_03_Q030`

Main rewrite reasons:
- Replaced all student-visible formulas and ion-symbol aliases with Chinese names.
- Converted surplus fill blanks into deterministic single-choice items to restore the 20/6/4 distribution.
- Added explicit supporting RAG evidence for wet potassium iodide-starch paper instead of trusting old question text.
- Removed formula aliases from accepted answers for mobile safety.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `REV_CH4_EXP_20_2_03_Q001`, `Q010`, `Q020`, `Q021`, `Q030`: bind preparation, acid reaction, gas check, and conclusion points.
- `REV_CH4_EXP_20_2_03_Q007`, `Q017`, `Q027`: bind chlorine-generation check to the supporting test-paper evidence.
- `REV_CH4_EXP_20_2_03_Q008`, `Q018`, `Q028`, `Q029`: combine concentrated hydrochloric acid, chlorine generation, and oxidizing-property interpretation.

## Fill-Blank Mobile Risk

- `REV_CH4_EXP_20_2_03_Q025`: answer `浓盐酸`; no formula alias.
- `REV_CH4_EXP_20_2_03_Q026`: answer `氯气`; no formula alias.
- `REV_CH4_EXP_20_2_03_Q027`: accepts `碘化钾-淀粉` and `碘化钾淀粉`; no KI alias.
- `REV_CH4_EXP_20_2_03_Q028`: answer `氧化性`; single Chinese concept term.

## Evidence Sources Read

- `expchunk_00320_309c0516a8`: canonical procedure for the iron(III), cobalt(III), nickel(III) oxidizing-property comparison.
- `expchunk_00162_1d49f603b8`: potassium iodide-starch test paper for chlorine and other oxidizing gases.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-2-03` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.