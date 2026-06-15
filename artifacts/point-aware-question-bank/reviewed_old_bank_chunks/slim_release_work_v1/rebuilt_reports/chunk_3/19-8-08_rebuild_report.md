# 19-8-08 Rebuild Report

- packet id: `EXP_19_8_08`
- experiment code: `19-8-08`
- title: `As(III)、Sb(III)、Bi(III) 的还原性`
- total questions: 30
- keep / rewrite / reject: 20 / 10 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-08_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_08_Q010`, `REBUILT_CH3_19_8_08_Q011`, `REBUILT_CH3_19_8_08_Q012`, `REBUILT_CH3_19_8_08_Q013`, `REBUILT_CH3_19_8_08_Q014`, `REBUILT_CH3_19_8_08_Q015`, `REBUILT_CH3_19_8_08_Q021`, `REBUILT_CH3_19_8_08_Q022`, `REBUILT_CH3_19_8_08_Q023`, `REBUILT_CH3_19_8_08_Q029`, `REBUILT_CH3_19_8_08_Q030`

## Borderline Keeps

- `REBUILT_CH3_19_8_08_Q002`, `Q003`, `Q024`: basic reagent questions retained to anchor the alkaline permanganate point; formula answers were converted to Chinese names.
- `REBUILT_CH3_19_8_08_Q005`, `Q013`, `Q020`, `Q025`, `Q030`: silver-ammonia items were kept or rewritten only with supporting theory; fixed silver-deposit claims were avoided where canonical only says observe.
- `REBUILT_CH3_19_8_08_Q006`, `Q015`, `Q021`, `Q026`, `Q029`: iodine-water items were narrowed to As/Sb point membership and evidence boundary.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_08_Q001`, `Q009`, `Q014`, `Q016`, `Q023`, `Q028`: cover the whole packet goal across all four point keys.
- `REBUILT_CH3_19_8_08_Q004`, `Q019`: bind the two Bi(III) point keys because硝酸铋 appears in both silver-ammonia and chlorine-water branches.
- `REBUILT_CH3_19_8_08_Q018`: binds the alkaline manganese branch and the iodine-water branch because三氯化砷/三氯化锑 appear in both.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `高锰酸钾`, `微热`, `弱酸性`, `氯水`, `还原性`, `三价`, `氧化`. Formula answers such as `KMnO₄`, `AsCl₃`, `SbCl₃`, `I₂`, and `Ag` were removed from visible answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00297_c03527ab79`
- `textbook_prose_00596_462a4c7dff`
- `textbook_prose_00597_06f7e56f06`
- `textbook_prose_01063_0b7c13db34`

## Semantic Notes

- canonical gives the four experimental designs but not every final observation; silver-ammonia and iodine-water claims were therefore phrased as design or evidence-boundary questions unless supporting theory was available.
- `textbook_prose_00596_462a4c7dff` supports the As/Sb/Bi trend and reduction behavior in alkaline medium.
- `textbook_prose_00597_06f7e56f06` supports iodine reduction by arsenite and Bi(III) oxidation by chlorine water under alkaline conditions.
- `textbook_prose_01063_0b7c13db34` supports silver-ammonia as a weak oxidizing system that can be reduced to silver.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
