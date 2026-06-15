# Rebuild Report: 20-2-04

- Packet id: `EXP_20_2_04`
- Experiment code: `20-2-04`
- Experiment title: 锰化合物的氧化还原性
- Chunk: `chunk_4`
- Source packet: `semantic_work_packets/chunk_4/20-2-04.json`
- Rebuilt JSON: `rebuilt_packages/chunk_4/20-2-04_rebuilt_v1.json`
- Release JSON direct modification: prohibited and not performed

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- kept_after_manual_tightening: 0
- rewrite: 30
- reject: 0

## Rewrite List

- `REV_CH4_EXP_20_2_04_Q001` through `REV_CH4_EXP_20_2_04_Q030`

Main rewrite reasons:
- Replaced all student-visible formulas and charged ion symbols with Chinese reagent/species names.
- Rebuilt unsupported product-recall items into canonical procedure, medium, and observation questions.
- Converted surplus fill blanks into deterministic single-choice items to restore 20/6/4.
- Kept only four low-risk Chinese fill blanks.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `REV_CH4_EXP_20_2_04_Q005`, `Q009`, `Q019`, `Q028`, `Q030`: bind the acid/neutral/basic high-permanganate-sulfite comparison points.
- `REV_CH4_EXP_20_2_04_Q003`, `Q013`, `Q017`, `Q027`: bind preparation, separation, and observation of the manganese(VI) system.
- `REV_CH4_EXP_20_2_04_Q004`, `Q014`, `Q020`, `Q024`, `Q029`: bind manganese(VI) acidification and observation.

## Fill-Blank Mobile Risk

- `REV_CH4_EXP_20_2_04_Q021`: answer `氯气`; no formula alias.
- `REV_CH4_EXP_20_2_04_Q022`: answer `溴水`; no formula alias.
- `REV_CH4_EXP_20_2_04_Q023`: answer `碱性`; single Chinese medium term.
- `REV_CH4_EXP_20_2_04_Q024`: answer `沉淀`; single Chinese observation term.

## Evidence Sources Read

- `expchunk_00320_309c0516a8`: canonical procedure for the manganese-compound oxidation-reduction experiment.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-2-04` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.