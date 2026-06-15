# Rebuild Report: chunk_4 / 20-1-03 其他配体的配合物

## Packet

- Packet id: `20-1-03`
- Experiment code: `20-1-03`
- Experiment title: `其他配体的配合物`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_4\20-1-03.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_4\20-1-03_rebuilt_v1.json`
- Statement: this packet was manually rebuilt question by question; it is not a script-generated batch normalization.
- 明确声明：本 packet 已逐题语义重构，不是脚本批量生成。

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep after manual tightening: `7`
- Rewrite: `23`
- Reject: `0`

## Rewrite List

Rewritten question ids:

- `REV_CH4_EXP_20_1_03_Q002`
- `REV_CH4_EXP_20_1_03_Q003`
- `REV_CH4_EXP_20_1_03_Q005`
- `REV_CH4_EXP_20_1_03_Q006`
- `REV_CH4_EXP_20_1_03_Q007`
- `REV_CH4_EXP_20_1_03_Q008`
- `REV_CH4_EXP_20_1_03_Q009`
- `REV_CH4_EXP_20_1_03_Q010`
- `REV_CH4_EXP_20_1_03_Q011`
- `REV_CH4_EXP_20_1_03_Q014`
- `REV_CH4_EXP_20_1_03_Q015`
- `REV_CH4_EXP_20_1_03_Q016`
- `REV_CH4_EXP_20_1_03_Q017`
- `REV_CH4_EXP_20_1_03_Q018`
- `REV_CH4_EXP_20_1_03_Q019`
- `REV_CH4_EXP_20_1_03_Q020`
- `REV_CH4_EXP_20_1_03_Q021`
- `REV_CH4_EXP_20_1_03_Q022`
- `REV_CH4_EXP_20_1_03_Q023`
- `REV_CH4_EXP_20_1_03_Q024`
- `REV_CH4_EXP_20_1_03_Q025`
- `REV_CH4_EXP_20_1_03_Q026`
- `REV_CH4_EXP_20_1_03_Q027`

Main rewrite reasons:

- The source packet inherited broad theory ids and repeatedly bound silver, mercury, and copper questions to unrelated video points.
- Formula/name fill blanks such as bromide salt, hydrochloric acid, mercury and thiocyanate products were rewritten as single-choice items or short Chinese fill blanks.
- Silver halide questions were separated into NH₃·H₂O comparison, Na₂S₂O₃ comparison, solubility order, and Ag⁺ complex stability rather than one generic multi-point shell.
- Mercury iodide, Nessler reagent, mercury thiocyanate, zinc salt, and cobalt salt questions were split into their own point-bound items.
- Copper CuCl₂ / concentrated hydrochloric acid / water / bromide salt sequence was rebuilt as a three-step operation chain with corrected point bindings.

## Kept But Quality-Edge Questions

- `REV_CH4_EXP_20_1_03_Q001`: kept because the source intent of comparing AgCl/AgBr/AgI with NH₃·H₂O is valid; point bindings and distractors were rebuilt.
- `REV_CH4_EXP_20_1_03_Q004`: kept because the source broad comparison of NH₃·H₂O and Na₂S₂O₃ is a valuable multi-point item; it now cites only silver-relevant points.
- `REV_CH4_EXP_20_1_03_Q012`: kept because CuCl₂ + concentrated hydrochloric acid + warming is directly in canonical text; wrong inherited bromide-salt binding was corrected.
- `REV_CH4_EXP_20_1_03_Q013`: kept because copper chloro complex color change after water addition is directly supported by canonical text.
- `REV_CH4_EXP_20_1_03_Q028`: kept as a short concept fill blank (`配位` / `络合`) with narrowed mercury iodide evidence.
- `REV_CH4_EXP_20_1_03_Q029`: kept as a short Chinese reagent fill blank (`盐酸`) with corrected copper point binding.
- `REV_CH4_EXP_20_1_03_Q030`: kept as a short Chinese reagent fill blank (`溴化钾`) with corrected copper point binding.

## Evidence Insufficient

- None.

No question is marked publishable with `evidence_sufficient=false`.

## Multi-Point Questions

- `REV_CH4_EXP_20_1_03_Q004`: compares NH₃·H₂O and Na₂S₂O₃ in the silver halide transformation task.
- `REV_CH4_EXP_20_1_03_Q015`: checks packet scope across silver, mercury, and copper subexperiments.
- `REV_CH4_EXP_20_1_03_Q016`: asks which evidence is needed for an AgI vs AgCl explanation, spanning solubility and complex stability points.
- `REV_CH4_EXP_20_1_03_Q017`: uses Hg(NO₃)₂ + KSCN formation followed by zinc/cobalt salt applications as one coherent mercury thiocyanate workflow.
- `REV_CH4_EXP_20_1_03_Q018`: discriminates reagent-purpose pairings across silver, silver mirror, copper acid dissolution, and bromide ligand-change operations.
- `REV_CH4_EXP_20_1_03_Q024`: compares zinc salt and cobalt salt outcomes in the same mercury thiocyanate system.
- `REV_CH4_EXP_20_1_03_Q025`: checks the ordered copper workflow: concentrated hydrochloric acid, water, then bromide salt.

## Evidence IDs Used

Canonical experiment chunks:

- `expchunk_00309_5610e5bc6f`
- `expchunk_00310_822a1490b4`

Supporting theory chunks:

- `textbook_prose_00394_04911a6294`
- `textbook_prose_01058_15764ebcec`
- `textbook_prose_01062_628733419b`
- `textbook_prose_01063_0b7c13db34`
- `textbook_prose_01090_56461596a1`
- `textbook_prose_01091_6b9e310a9d`
- `textbook_prose_01093_4e1caaa871`
- `textbook_prose_00226_74aebd351e`

## Mobile Fill Blank Audit

- `REV_CH4_EXP_20_1_03_Q027`: answer `葡萄糖`; concentration omitted intentionally.
- `REV_CH4_EXP_20_1_03_Q028`: answer `配位` / `络合`; no formula aliases.
- `REV_CH4_EXP_20_1_03_Q029`: answer `盐酸`; no formula alias.
- `REV_CH4_EXP_20_1_03_Q030`: answer `溴化钾`; no formula alias.

## Direct Release JSON Rule

- The release JSON was not modified.
- Output was written only to the requested rebuilt package/report paths under `slim_release_work_v1`.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-1-03` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.