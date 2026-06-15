# 19-8-06 Rebuild Report

- packet id: `EXP_19_8_06`
- experiment code: `19-8-06`
- title: `Sn(II) 的还原性`
- total questions: 30
- keep / rewrite / reject: 22 / 8 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-06_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_06_Q011`, `REBUILT_CH3_19_8_06_Q012`, `REBUILT_CH3_19_8_06_Q013`, `REBUILT_CH3_19_8_06_Q014`, `REBUILT_CH3_19_8_06_Q015`, `REBUILT_CH3_19_8_06_Q021`, `REBUILT_CH3_19_8_06_Q029`, `REBUILT_CH3_19_8_06_Q030`

All kept items still had wording, evidence, option links, or mobile-answer risks manually tightened.

## Borderline Keeps

- `REBUILT_CH3_19_8_06_Q001`, `Q002`, `Q024`, `Q025`: reagent-recognition items are basic, but retained because they anchor the FeCl₃/SnCl₂ and KSCN point keys; formula answers were converted to Chinese names.
- `REBUILT_CH3_19_8_06_Q003`, `Q004`, `Q018`, `Q020`, `Q026`, `Q027`: kept only after adding supporting theory for actual redox products and using Chinese visible answers instead of formula/ion input.
- `REBUILT_CH3_19_8_06_Q006`, `Q007`, `Q022`, `Q028`: retained because the HgCl₂ and Fe³⁺ phenomena are evidence-supported, but the evidence source is supporting theory rather than the terse canonical protocol.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_06_Q009`, `Q013`, `Q030`: link the Fe branch to the explicit comparison point.
- `REBUILT_CH3_19_8_06_Q010`, `Q012`, `Q014`, `Q023`: cover the Fe and Hg branches or distinguish this packet from adjacent packets.
- `REBUILT_CH3_19_8_06_Q011`: uses the FeCl₃/SnCl₂ reaction and the KSCN detection point together.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `氯化亚锡`, `硫氰酸钾`, `亚铁离子`, `四价锡`, `血红色`, `汞`, `氧化还原性`. Formula aliases from the old packet are not visible answers.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00296_a4c00bb9d1`
- `expchunk_00297_c03527ab79`
- `textbook_prose_00773_a0b6644822`
- `textbook_prose_00774_e51e8911a2`
- `textbook_prose_01090_56461596a1`
- `textbook_prose_01304_9920c29f9d`

## Semantic Notes

- canonical supports the operation sequence and comparison targets but is terse on products and visible phenomena.
- Fe(III) to Fe(II), Sn(II) to Sn(IV), and Fe³⁺/SCN blood-red detection use supporting theory.
- HgCl₂ white precipitate and blackening under excess SnCl₂ use `textbook_prose_01090_56461596a1`.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
