# Rebuild Report: chunk_4 / 20-1-04 碘化亚铜的形成

## Packet

- Packet id: `20-1-04`
- Experiment code: `20-1-04`
- Experiment title: `碘化亚铜的形成`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_4\20-1-04.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_4\20-1-04_rebuilt_v1.json`
- Statement: this packet was manually rebuilt question by question; it is not a script-generated batch normalization.
- 明确声明：本 packet 已逐题语义重构，不是脚本批量生成。

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep after manual tightening: `11`
- Rewrite: `19`
- Reject: `0`

## Rewrite List

Rewritten question ids:

- `REV_CH4_EXP_20_1_04_Q002`
- `REV_CH4_EXP_20_1_04_Q004`
- `REV_CH4_EXP_20_1_04_Q005`
- `REV_CH4_EXP_20_1_04_Q009`
- `REV_CH4_EXP_20_1_04_Q011`
- `REV_CH4_EXP_20_1_04_Q012`
- `REV_CH4_EXP_20_1_04_Q013`
- `REV_CH4_EXP_20_1_04_Q014`
- `REV_CH4_EXP_20_1_04_Q015`
- `REV_CH4_EXP_20_1_04_Q016`
- `REV_CH4_EXP_20_1_04_Q017`
- `REV_CH4_EXP_20_1_04_Q018`
- `REV_CH4_EXP_20_1_04_Q019`
- `REV_CH4_EXP_20_1_04_Q020`
- `REV_CH4_EXP_20_1_04_Q021`
- `REV_CH4_EXP_20_1_04_Q025`
- `REV_CH4_EXP_20_1_04_Q026`
- `REV_CH4_EXP_20_1_04_Q030`

Main rewrite reasons:

- The source packet had 10 fill blanks, several requiring formula/symbolic answers such as cuprous iodide formula or iodine formula.
- Many source questions repeated the same reagent/product recall with inherited audit language rather than testing operation, product verification, and evidence boundaries.
- Product color, difficult solubility, and redox direction require supporting theory; these were separated from direct canonical operation questions.
- The iodine verification questions need a separate general experiment-method source for starch blue color.
- Questions about later CuCl and Cu₂O subexperiments were kept out of this packet except as explicit scope-boundary distractors.

## Kept But Quality-Edge Questions

- `REV_CH4_EXP_20_1_04_Q001`: kept because it directly asks the operation pair CuSO₄ + KI; wording and distractors were rebuilt.
- `REV_CH4_EXP_20_1_04_Q003`: kept because the cuprous iodide product is central; answer is now the Chinese name.
- `REV_CH4_EXP_20_1_04_Q006`: kept because iodide reducing property is a useful explanation point, not just reagent recall.
- `REV_CH4_EXP_20_1_04_Q007`: kept because cuprous iodide precipitation driving the reaction is conceptually important.
- `REV_CH4_EXP_20_1_04_Q008`: kept because starch-blue iodine verification is valid, with added supporting evidence.
- `REV_CH4_EXP_20_1_04_Q010`: kept because it asks the value of combining observation and product verification.
- `REV_CH4_EXP_20_1_04_Q023`: kept because it correctly states the redox direction.
- `REV_CH4_EXP_20_1_04_Q024`: kept because it checks the iodine verification method.
- `REV_CH4_EXP_20_1_04_Q027`: kept as short Chinese fill blank `碘化钾`, not formula input.
- `REV_CH4_EXP_20_1_04_Q028`: kept as short Chinese fill blank `碘化亚铜`, not formula input.
- `REV_CH4_EXP_20_1_04_Q029`: kept as short Chinese fill blank `淀粉` / `淀粉溶液`.

## Evidence Insufficient

- None.

No question is marked publishable with `evidence_sufficient=false`.

## Multi-Point Questions

- `REV_CH4_EXP_20_1_04_Q009`: operation plus product verification theory boundary.
- `REV_CH4_EXP_20_1_04_Q010`: experiment value across the KI operation and product verification.
- `REV_CH4_EXP_20_1_04_Q012`: packet-scope check across operation, observation, and product verification.
- `REV_CH4_EXP_20_1_04_Q014`: combines operation text with theory needed for cuprous iodide difficult solubility.
- `REV_CH4_EXP_20_1_04_Q015`: checks redox direction and product formation together.
- `REV_CH4_EXP_20_1_04_Q016`: checks both video points as a record/observation pair.
- `REV_CH4_EXP_20_1_04_Q020`: repairs the misconception that KI is only a precipitating reagent.
- `REV_CH4_EXP_20_1_04_Q023`: true/false redox role across copper and iodide.
- `REV_CH4_EXP_20_1_04_Q025`: scope boundary across both packet points.

## Evidence IDs Used

Canonical experiment chunks:

- `expchunk_00311_c770d017e2`

Supporting experiment chunks:

- `expchunk_00162_1d49f603b8`

Supporting theory chunks:

- `textbook_prose_01036_551b4dc475`

## Mobile Fill Blank Audit

- `REV_CH4_EXP_20_1_04_Q027`: answer `碘化钾`; no KI alias.
- `REV_CH4_EXP_20_1_04_Q028`: answer `碘化亚铜`; no formula alias.
- `REV_CH4_EXP_20_1_04_Q029`: answer `淀粉` / `淀粉溶液`; no iodine formula input.
- `REV_CH4_EXP_20_1_04_Q030`: answer `碘`; no I₂ alias.

## Direct Release JSON Rule

- The release JSON was not modified.
- Output was written only to the requested rebuilt package/report paths under `slim_release_work_v1`.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-1-04` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.