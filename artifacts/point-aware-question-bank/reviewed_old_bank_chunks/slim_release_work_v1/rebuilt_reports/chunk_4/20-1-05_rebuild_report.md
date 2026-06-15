# Rebuild Report: chunk_4 / 20-1-05 氯化亚铜的形成和性质

## Packet

- Packet id: `20-1-05`
- Experiment code: `20-1-05`
- Experiment title: `氯化亚铜的形成和性质`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_4\20-1-05.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_4\20-1-05_rebuilt_v1.json`
- Statement: this packet was manually rebuilt question by question; it is not a script-generated batch normalization.
- 明确声明：本 packet 已逐题语义重构，不是脚本批量生成。

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep after manual tightening: `14`
- Rewrite: `16`
- Reject: `0`

## Rewrite List

Rewritten question ids:

- `REV_CH4_EXP_20_1_05_Q010`
- `REV_CH4_EXP_20_1_05_Q011`
- `REV_CH4_EXP_20_1_05_Q012`
- `REV_CH4_EXP_20_1_05_Q013`
- `REV_CH4_EXP_20_1_05_Q014`
- `REV_CH4_EXP_20_1_05_Q015`
- `REV_CH4_EXP_20_1_05_Q016`
- `REV_CH4_EXP_20_1_05_Q017`
- `REV_CH4_EXP_20_1_05_Q018`
- `REV_CH4_EXP_20_1_05_Q019`
- `REV_CH4_EXP_20_1_05_Q020`
- `REV_CH4_EXP_20_1_05_Q024`
- `REV_CH4_EXP_20_1_05_Q025`
- `REV_CH4_EXP_20_1_05_Q026`
- `REV_CH4_EXP_20_1_05_Q027`
- `REV_CH4_EXP_20_1_05_Q028`

Main rewrite reasons:

- Source had eight fill blanks, several requiring formula/symbol input or low-depth reagent recall.
- Many source items over-bound the initial reaction, product formation, and both follow-up reagents even when only one operation was asked.
- Exact follow-up phenomena for CuCl with concentrated ammonia or hydrochloric acid were not overclaimed; questions ask supported operation/purpose unless theory supports more.
- Same-chunk but different packet content, especially cuprous oxide formation, was kept out except as scope-boundary distractors.

## Kept But Quality-Edge Questions

- `REV_CH4_EXP_20_1_05_Q001`: kept because it directly asks the starting reagent pair.
- `REV_CH4_EXP_20_1_05_Q002`: kept because sodium sulfite's role is meaningful, now phrased conceptually.
- `REV_CH4_EXP_20_1_05_Q003`: kept because the cuprous chloride product is central; answer is Chinese.
- `REV_CH4_EXP_20_1_05_Q004`: kept because it directly asks the two required follow-up reagents.
- `REV_CH4_EXP_20_1_05_Q005`: kept because the copper(Ⅱ) to copper(Ⅰ) redox direction is important.
- `REV_CH4_EXP_20_1_05_Q006`: kept as a supported purpose question, not an over-specific phenomenon claim.
- `REV_CH4_EXP_20_1_05_Q007`: kept as direct operation detail.
- `REV_CH4_EXP_20_1_05_Q008`: kept as direct sequence detail.
- `REV_CH4_EXP_20_1_05_Q009`: kept because it summarizes the full packet goal.
- `REV_CH4_EXP_20_1_05_Q021` through `Q023`: kept as safe true/false concepts.
- `REV_CH4_EXP_20_1_05_Q029` and `Q030`: kept as short Chinese fill blanks.

## Evidence Insufficient

- None.

No question is marked publishable with `evidence_sufficient=false`.

## Multi-Point Questions

- `REV_CH4_EXP_20_1_05_Q004`: uses both concentrated ammonia and concentrated hydrochloric acid follow-up points.
- `REV_CH4_EXP_20_1_05_Q005`: ties starting reaction to cuprous chloride product.
- `REV_CH4_EXP_20_1_05_Q009`: covers all four packet points.
- `REV_CH4_EXP_20_1_05_Q010`: combines reduction need and precipitate formation.
- `REV_CH4_EXP_20_1_05_Q014`: boundary across in-scope and out-of-scope same-chunk operations.
- `REV_CH4_EXP_20_1_05_Q016`: explicit four-point coverage check.
- `REV_CH4_EXP_20_1_05_Q017`: repairs the “just precipitation” misconception with redox and follow-up properties.
- `REV_CH4_EXP_20_1_05_Q020`: checks that follow-up points are not omitted.
- `REV_CH4_EXP_20_1_05_Q023`: true/false item binds both follow-up reagents.
- `REV_CH4_EXP_20_1_05_Q026`: scope boundary across all in-scope points.

## Evidence IDs Used

Canonical experiment chunks:

- `expchunk_00311_c770d017e2`

Supporting theory chunks:

- `textbook_prose_01036_551b4dc475`
- `textbook_prose_01043_ae32379ec7`

## Mobile Fill Blank Audit

- `REV_CH4_EXP_20_1_05_Q027`: answer `亚硫酸钠`; no formula alias.
- `REV_CH4_EXP_20_1_05_Q028`: answer `氯化亚铜`; no formula alias.
- `REV_CH4_EXP_20_1_05_Q029`: answer `浓盐酸`; no formula alias.
- `REV_CH4_EXP_20_1_05_Q030`: answer `还原剂`; concept-only Chinese answer.

## Direct Release JSON Rule

- The release JSON was not modified.
- Output was written only to the requested rebuilt package/report paths under `slim_release_work_v1`.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-1-05` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.