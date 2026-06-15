# 19-8-05 Rebuild Report

- packet id: `EXP_19_8_05`
- experiment code: `19-8-05`
- title: `Sn²⁺、Pb²⁺、Sb³⁺、Bi³⁺ 氢氧化物的酸碱性`
- total questions: 30
- keep / rewrite / reject: 15 / 15 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-05_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_05_Q007`, `REBUILT_CH3_19_8_05_Q008`, `REBUILT_CH3_19_8_05_Q009`, `REBUILT_CH3_19_8_05_Q010`, `REBUILT_CH3_19_8_05_Q011`, `REBUILT_CH3_19_8_05_Q012`, `REBUILT_CH3_19_8_05_Q013`, `REBUILT_CH3_19_8_05_Q014`, `REBUILT_CH3_19_8_05_Q015`, `REBUILT_CH3_19_8_05_Q019`, `REBUILT_CH3_19_8_05_Q020`, `REBUILT_CH3_19_8_05_Q021`, `REBUILT_CH3_19_8_05_Q028`, `REBUILT_CH3_19_8_05_Q029`, `REBUILT_CH3_19_8_05_Q030`

## Borderline Keeps

- `REBUILT_CH3_19_8_05_Q001` to `Q004`: reagent recognition is basic, but retained to anchor the four video point mappings and rewritten with Chinese names rather than formula-entry answers.
- `REBUILT_CH3_19_8_05_Q016` to `Q018`: kept because each directly checks a canonical operation sequence; explanations were tightened to cite the exact acid/base test design.
- `REBUILT_CH3_19_8_05_Q022` and `Q023`: kept as safety/scope checks, with wording tightened to avoid vague “inconsistent with experiment” explanations.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_05_Q009`: compares the shared `离心分离` operation across Sn, Sb, and Bi point keys.
- `REBUILT_CH3_19_8_05_Q010`, `Q011`, `Q014`, `Q015`, `Q020`, `Q022`, `Q029`: use all four point keys because the question is about the whole set of hydroxide acid/base tests or shared safety handling.
- `REBUILT_CH3_19_8_05_Q013`, `Q021`, `Q030`: bind Sb and Bi point keys because the supporting theory trend is specifically used to compare those related hydroxides.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `氢氧化钠`, `硝酸铅`, `三氯化锑`, `硝酸铋`, `离心分离`, `酸碱性`, `碱性`. Formula answers and concentration-number answers were removed from visible answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00293_a6262c57db`
- `expchunk_00295_b30319fd2c`
- `textbook_prose_00171_6743bd6e37`
- `textbook_prose_00596_462a4c7dff`
- `textbook_prose_00753_2adf53a8cc`
- `textbook_prose_00754_c66e000e5b`

## Semantic Notes

- canonical supports the four generation and acid/base test workflows, but not every fixed dissolution observation. Old dissolution-result questions were rewritten as test-design, evidence-boundary, or supporting-theory questions.
- `Sn(OH)₂` excess-base behavior is supported by `textbook_prose_00753_2adf53a8cc` and `textbook_prose_00754_c66e000e5b`.
- Sb/Bi trend questions use `textbook_prose_00596_462a4c7dff` and avoid overclaiming unrecorded direct observations.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
