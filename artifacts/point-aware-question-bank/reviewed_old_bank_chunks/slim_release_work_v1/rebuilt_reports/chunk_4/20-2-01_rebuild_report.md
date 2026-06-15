# Rebuild Report: 20-2-01

- Packet id: `EXP_20_2_01`
- Experiment code: `20-2-01`
- Experiment title: 氢氧化物的酸碱性
- Chunk: `chunk_4`
- Source packet: `semantic_work_packets/chunk_4/20-2-01.json`
- Rebuilt JSON: `rebuilt_packages/chunk_4/20-2-01_rebuilt_v1.json`
- Release JSON direct modification: prohibited and not performed

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep after manual tightening: `10`
- Rewrite: `20`
- Reject: `0`

## Rewrite List

- `REV_CH4_EXP_20_2_01_Q001`
- `REV_CH4_EXP_20_2_01_Q002`
- `REV_CH4_EXP_20_2_01_Q004`
- `REV_CH4_EXP_20_2_01_Q007`
- `REV_CH4_EXP_20_2_01_Q008`
- `REV_CH4_EXP_20_2_01_Q009`
- `REV_CH4_EXP_20_2_01_Q010`
- `REV_CH4_EXP_20_2_01_Q011`
- `REV_CH4_EXP_20_2_01_Q014`
- `REV_CH4_EXP_20_2_01_Q016`
- `REV_CH4_EXP_20_2_01_Q017`
- `REV_CH4_EXP_20_2_01_Q018`
- `REV_CH4_EXP_20_2_01_Q019`
- `REV_CH4_EXP_20_2_01_Q020`
- `REV_CH4_EXP_20_2_01_Q025`
- `REV_CH4_EXP_20_2_01_Q026`
- `REV_CH4_EXP_20_2_01_Q027`
- `REV_CH4_EXP_20_2_01_Q028`
- `REV_CH4_EXP_20_2_01_Q029`
- `REV_CH4_EXP_20_2_01_Q030`

Main rewrite reasons:
- Replaced student-visible formulas and ion symbols with Chinese names or prose.
- Converted surplus fill blanks into single-choice items to restore the 20/6/4 packet distribution.
- Bound reagent identity, sample list, heating-after-dissolution, and air-exclusion details to RAG canonical chunks.
- Avoided asking for numeric/formula entry on mobile; retained only four low-risk Chinese fill blanks.

## Kept But Quality Edge

- `REV_CH4_EXP_20_2_01_Q003`: kept as the post-dissolution heating operation.
- `REV_CH4_EXP_20_2_01_Q005`: kept as boiling distilled water to remove air.
- `REV_CH4_EXP_20_2_01_Q006`: kept as direct purpose recognition.
- `REV_CH4_EXP_20_2_01_Q012` through `Q013`: kept as true/false operation checks.
- `REV_CH4_EXP_20_2_01_Q015`: kept as the boiling-water air-removal check.
- `REV_CH4_EXP_20_2_01_Q021` through `Q024`: kept as four low-risk Chinese fill blanks.
- `REV_CH4_EXP_20_2_01_Q022`: kept as purpose-level acid/base behavior check.

## Evidence Insufficient

- None.

## Multi-Point Questions

- `REV_CH4_EXP_20_2_01_Q001`: binds the shared reagent to the multiple metal-salt systems.
- `REV_CH4_EXP_20_2_01_Q008`, `Q018`, `Q029`, `Q030`: use the metal-salt list plus the acid/base precipitate test.
- `REV_CH4_EXP_20_2_01_Q022`: uses experiment purpose plus the canonical operation.

## Fill-Blank Mobile Risk

- `REV_CH4_EXP_20_2_01_Q021`: answer `氢氧化钠`; no formula alias accepted.
- `REV_CH4_EXP_20_2_01_Q023`: answer `氢氧化物`; no formula alias accepted.
- `REV_CH4_EXP_20_2_01_Q024`: answer `加热`; single common Chinese term.
- `REV_CH4_EXP_20_2_01_Q025`: answer `空气`; single common Chinese term.

## Evidence Sources Read

- `expchunk_00316_2998c6990c`: experiment purpose for d 区 hydroxide acid/base behavior.
- `expchunk_00319_b995aa9123`: canonical procedure for the hydroxide acid/base experiment.
- `expchunk_00324_5148cfb68c`: titanium solution preparation and ferrous hydroxide air-exclusion notes.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-2-01` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.