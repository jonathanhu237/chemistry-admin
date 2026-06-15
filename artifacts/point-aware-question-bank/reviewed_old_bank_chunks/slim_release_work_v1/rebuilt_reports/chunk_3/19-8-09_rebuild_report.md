# 19-8-09 Rebuild Report

- packet id: `EXP_19_8_09`
- experiment code: `19-8-09`
- title: `As(V)、Sb(V)、Bi(V) 的氧化性`
- total questions: 30
- keep / rewrite / reject: 19 / 11 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-09_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_09_Q011`, `REBUILT_CH3_19_8_09_Q012`, `REBUILT_CH3_19_8_09_Q013`, `REBUILT_CH3_19_8_09_Q014`, `REBUILT_CH3_19_8_09_Q015`, `REBUILT_CH3_19_8_09_Q021`, `REBUILT_CH3_19_8_09_Q022`, `REBUILT_CH3_19_8_09_Q023`, `REBUILT_CH3_19_8_09_Q028`, `REBUILT_CH3_19_8_09_Q029`, `REBUILT_CH3_19_8_09_Q030`

## Borderline Keeps

- `REBUILT_CH3_19_8_09_Q002`, `Q003`, `Q005`, `Q010`: retained as canonical operation and reagent questions; visible formulas were shifted toward Chinese names where practical.
- `REBUILT_CH3_19_8_09_Q004`, `Q006`, `Q007`, `Q008`, `Q009`, `Q018`, `Q019`: retained only with supporting-theory boundaries because canonical gives operations but not every final observation.
- `REBUILT_CH3_19_8_09_Q024` through `Q027`: fill blanks retained as mobile-safe Chinese answers instead of formula-heavy answers.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_09_Q001`, `Q007`, `Q011`, `Q012`, `Q013`, `Q014`, `Q018`, `Q020`, `Q021`, `Q023`, `Q024`, `Q029`, `Q030`: bind both video points because they cover the shared As(V)/Sb(V)/Bi(V) comparison goal or trend.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `氧化性`, `四氯化碳`, `硫酸`, `高锰酸根`, `紫色`, `依次增强`, `五价`. Formula answers such as `CCl4`, `H2SO4`, `MnO4-`, `+5`, and `V` were removed from answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00297_c03527ab79`
- `textbook_prose_00597_06f7e56f06`
- `textbook_prose_00598_cadca448de`
- `textbook_prose_01241_99049758ad`

## Semantic Notes

- canonical supports the two experimental designs: acidify high-valent As/Sb/Bi solids then add KI and CCl4, and add those solids to acidified MnSO4 solution.
- `textbook_prose_00597_06f7e56f06` supports the increasing oxidizing power trend and the strong-acid boundary for arsenate/antimonate.
- `textbook_prose_00598_cadca448de` and `textbook_prose_01241_99049758ad` support bismuthate oxidizing Mn(II) to purple permanganate.
- Specific per-tube endpoint colors were not treated as canonical unless supported by theory.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
