# Rebuild Report: 20-2-05

- Packet id: `EXP_20_2_05`
- Experiment code: `20-2-05`
- Experiment title: 铬、钼、钨化合物的氧化还原性
- Chunk: `chunk_4`
- Source packet: `semantic_work_packets/chunk_4/20-2-05.json`
- Rebuilt JSON: `rebuilt_packages/chunk_4/20-2-05_rebuilt_v1.json`
- Release JSON direct modification: prohibited and not performed

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- rewrite: 30
- reject: 0

## Rewrite List

- `REV_CH4_EXP_20_2_05_Q001` through `REV_CH4_EXP_20_2_05_Q030`

Main rewrite reasons:
- Removed student-visible formulas, charged species, concentration notation, and formula aliases from stems, options, explanations, and fill answers.
- Rebalanced the packet to 20 single-choice, 6 true-false, and 4 fill-blank questions.
- Rebuilt generic answer-shell explanations into evidence-specific explanations tied to the canonical experiment procedure.
- Removed inherited missing locator `textbook_figure_figure_p210_01` from source audits.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `REV_CH4_EXP_20_2_05_Q001`, `Q005`, `Q016`, `Q020`, `Q021`: bind the chromium medium-conversion design points.
- `REV_CH4_EXP_20_2_05_Q008`, `Q013`, `Q020`, `Q023`, `Q030`: bind both molybdenum and tungsten acidification-zinc observation points.
- `REV_CH4_EXP_20_2_05_Q009`, `Q014`, `Q018`, `Q025`, `Q026`: bind the solution-color observation point with molybdenum/tungsten operations.

## Fill-Blank Mobile Risk

- `REV_CH4_EXP_20_2_05_Q027`: answers `硫酸铬溶液` / `硫酸铬`; no formula alias.
- `REV_CH4_EXP_20_2_05_Q028`: answers `过氧化氢` / `过氧化氢溶液`; no formula alias.
- `REV_CH4_EXP_20_2_05_Q029`: answers `盐酸` / `盐酸溶液`; no concentration or formula alias.
- `REV_CH4_EXP_20_2_05_Q030`: answers `锌` / `锌粒` / `锌粉`; all Chinese names.

## Evidence Sources Read

- `expchunk_00321_53b9414bde`: canonical procedure for chromium, molybdenum, and tungsten compound redox experiments.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-2-05` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.