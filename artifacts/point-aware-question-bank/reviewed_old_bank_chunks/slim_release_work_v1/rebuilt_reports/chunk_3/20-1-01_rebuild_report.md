# 20-1-01 Rebuild Report

- packet id: `EXP_20_1_01`
- experiment code: `20-1-01`
- title: `氢氧化物的生成与性质`
- total questions: 30
- keep / rewrite / reject: 22 / 8 / 0
- output JSON: `rebuilt_packages/chunk_3/20-1-01_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_20_1_01_Q010`, `REBUILT_CH3_20_1_01_Q011`, `REBUILT_CH3_20_1_01_Q012`, `REBUILT_CH3_20_1_01_Q013`, `REBUILT_CH3_20_1_01_Q014`, `REBUILT_CH3_20_1_01_Q015`, `REBUILT_CH3_20_1_01_Q022`, `REBUILT_CH3_20_1_01_Q023`

## Borderline Keeps

- `REBUILT_CH3_20_1_01_Q001`, `Q002`, `Q003`, `Q016`, `Q017`, `Q024`: retained as canonical operation and observation-scope questions.
- `REBUILT_CH3_20_1_01_Q004`, `Q005`, `Q008`, `Q018`, `Q019`, `Q021`, `Q025`, `Q028`: retained with supporting theory for concrete colors and unstable hydroxide boundaries.
- `REBUILT_CH3_20_1_01_Q006`, `Q007`, `Q020`, `Q026`, `Q027`, `Q029`, `Q030`: retained as Zn/Cd identity, acid-base, or heat-stability questions with formula answers converted to Chinese.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_20_1_01_Q001`, `Q002`, `Q015`, `Q016`, `Q023`, `Q024`: bind all or most salt-addition points because they cover the shared NaOH operation and evidence boundary.
- `REBUILT_CH3_20_1_01_Q010`, `Q011`: bind Zn/Cd comparison points.
- `REBUILT_CH3_20_1_01_Q012`, `Q013`, `Q029`, `Q030`: bind property-test points for acid-base behavior and heat stability.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `氢氧化钠`, `蓝色`, `氢氧化锌`, `氢氧化镉`, `氧化汞`, `酸碱性`, `热稳定性`. Formula answers such as `NaOH`, `Zn(OH)2`, `Cd(OH)2`, `HgO`, and `+2` were removed from answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_b45d333c798a`
- `expchunk_00308_f319652f01`
- `textbook_prose_01042_cb5178e401`
- `textbook_prose_01057_8ebcc2ce77`
- `textbook_prose_01079_0f2609f8ca`
- `textbook_prose_01087_3a6c1c97ff`

## Semantic Notes

- canonical directly supports the shared operation and the categories to observe/test, but not every specific color.
- `textbook_prose_01042_cb5178e401` supports blue copper hydroxide and black copper oxide on heating.
- `textbook_prose_01057_8ebcc2ce77` supports unstable AgOH and brown-black silver oxide.
- `textbook_prose_01079_0f2609f8ca` supports Zn/Cd hydroxide formation, amphoterism differences, and relative heat stability.
- `textbook_prose_01087_3a6c1c97ff` supports yellow mercury oxide rather than stable mercury hydroxide.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
