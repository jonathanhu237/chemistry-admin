# 19-8-07 Rebuild Report

- packet id: `EXP_19_8_07`
- experiment code: `19-8-07`
- title: `Pb(IV) 的氧化性`
- total questions: 30
- keep / rewrite / reject: 21 / 9 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-07_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_07_Q011`, `REBUILT_CH3_19_8_07_Q012`, `REBUILT_CH3_19_8_07_Q013`, `REBUILT_CH3_19_8_07_Q014`, `REBUILT_CH3_19_8_07_Q015`, `REBUILT_CH3_19_8_07_Q021`, `REBUILT_CH3_19_8_07_Q022`, `REBUILT_CH3_19_8_07_Q029`, `REBUILT_CH3_19_8_07_Q030`

## Borderline Keeps

- `REBUILT_CH3_19_8_07_Q001`, `Q006`, `Q007`, `Q024`, `Q026`, `Q027`: basic reagent/operation questions retained because they anchor the two canonical point branches; formulas were converted to Chinese names.
- `REBUILT_CH3_19_8_07_Q002` to `Q005`, `Q009`, `Q016`, `Q018`, `Q025`: kept only with supporting theory for chlorine/high-manganate products and redox direction.
- `REBUILT_CH3_19_8_07_Q020`, `Q023`: retained as scope-boundary checks separating Pb(IV) oxidation from Pb(II) hydroxide acid-base questions.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_07_Q001`, `Q002`, `Q003`, `Q004`, `Q005`, `Q009`, `Q012`, `Q013`, `Q016`, `Q018`, `Q021`: link a specific reaction branch to the comparison point.
- `REBUILT_CH3_19_8_07_Q010`, `Q014`, `Q030`: cover the full packet goal or both acid branches.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `二氧化铅`, `氯气`, `硫酸`, `水浴`, `氧化剂`, `锰`, `氧化性`. Formula and ion answers from the old packet were removed from visible answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00297_c03527ab79`
- `textbook_prose_00757_85fc20341a`
- `textbook_prose_00758_5f5fd037a3`
- `textbook_prose_00784_dec216b401`
- `textbook_prose_01241_99049758ad`

## Semantic Notes

- `expchunk_00297_c03527ab79` contains the terse canonical Pb(IV) protocol, but product identity and color interpretation require supporting theory.
- Chlorine-generation items cite `textbook_prose_00758_5f5fd037a3` and `textbook_prose_00784_dec216b401`.
- Purple high-manganate items cite `textbook_prose_00758_5f5fd037a3` and `textbook_prose_01241_99049758ad`.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
