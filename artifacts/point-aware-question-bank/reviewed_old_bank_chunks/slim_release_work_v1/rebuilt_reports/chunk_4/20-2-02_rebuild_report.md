# Rebuild Report: 20-2-02

- Packet id: `EXP_20_2_02`
- Experiment code: `20-2-02`
- Experiment title: 铁(II)、钴(II)和镍(II)的还原性
- Chunk: `chunk_4`
- Source packet: `semantic_work_packets/chunk_4/20-2-02.json`
- Rebuilt JSON: `rebuilt_packages/chunk_4/20-2-02_rebuilt_v1.json`
- Release JSON direct modification: prohibited and not performed

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep after manual tightening: `0`
- Rewrite: `30`
- Reject: `0`

## Rewrite List

- `REV_CH4_EXP_20_2_02_Q001` through `REV_CH4_EXP_20_2_02_Q030`

Main rewrite reasons:
- Replaced student-visible formulas and element-symbol options with Chinese names or prose.
- Converted surplus fill blanks into deterministic single-choice or true/false items to restore the 20/6/4 distribution.
- Kept the evidence boundary within the canonical iron(II), cobalt(II), nickel(II) reducing-property subpart.
- Avoided mobile entry of chemical formulas, concentrations, and oxidation-state strings.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `REV_CH4_EXP_20_2_02_Q001`, `Q011`, `Q018`: bind the three solution-plus-bromine-water point groups.
- `REV_CH4_EXP_20_2_02_Q005`, `Q012`, `Q017`, `Q030`: bind cobalt and nickel precipitate subtests with both oxidants.
- `REV_CH4_EXP_20_2_02_Q009`, `Q020`: bind hydroxide precipitation and standing-observation steps.

## Fill-Blank Mobile Risk

- `REV_CH4_EXP_20_2_02_Q021`: answer `溴水`; no formula alias.
- `REV_CH4_EXP_20_2_02_Q022`: answer `硫酸亚铁铵`; Chinese reagent name only.
- `REV_CH4_EXP_20_2_02_Q023`: answer `氢氧化钠`; concentration expressed in prose.
- `REV_CH4_EXP_20_2_02_Q024`: answer `过氧化氢`; no formula alias.

## Evidence Sources Read

- `expchunk_00320_309c0516a8`: canonical procedure for iron(II), cobalt(II), nickel(II) reducing-property comparison.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-2-02` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.