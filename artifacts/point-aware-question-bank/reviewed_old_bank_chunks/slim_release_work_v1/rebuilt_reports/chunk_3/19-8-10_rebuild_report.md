# 19-8-10 Rebuild Report

- packet id: `EXP_19_8_10`
- experiment code: `19-8-10`
- title: `Sn、Pb、Bi 不同价态离子的氧化还原性`
- total questions: 30
- keep / rewrite / reject: 20 / 10 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-10_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_10_Q011`, `REBUILT_CH3_19_8_10_Q012`, `REBUILT_CH3_19_8_10_Q013`, `REBUILT_CH3_19_8_10_Q014`, `REBUILT_CH3_19_8_10_Q015`, `REBUILT_CH3_19_8_10_Q022`, `REBUILT_CH3_19_8_10_Q023`, `REBUILT_CH3_19_8_10_Q028`, `REBUILT_CH3_19_8_10_Q029`, `REBUILT_CH3_19_8_10_Q030`

## Borderline Keeps

- `REBUILT_CH3_19_8_10_Q002`, `Q004`, `Q005`, `Q016`, `Q018`, `Q024`: Sn(II)/HgCl2 questions retained with `textbook_prose_01090_56461596a1` as theory support.
- `REBUILT_CH3_19_8_10_Q003`, `Q017`, `Q025`: FeCl3/KSCN questions retained because expchunk_00296 directly supports the operation.
- `REBUILT_CH3_19_8_10_Q006` through `Q009`, `Q019` through `Q021`, `Q026`, `Q027`: Pb(IV) questions retained with PbO2/MnSO4 or PbO2/HCl evidence boundaries.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_10_Q001`, `Q010`, `Q023`: bind all three point keys because they cover the packet-level redox goal or evidence-boundary statement.
- `REBUILT_CH3_19_8_10_Q013`, `Q014`, `Q015`: bind cross-branch Pb/Bi or Sn/Pb comparisons.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `氯化亚锡`, `硫氰酸钾`, `二氧化铅`, `氯气`, `高锰酸根`, `水浴加热`, `铋酸盐`. Formula answers such as `SnCl2`, `KSCN`, `PbO2`, `Cl2`, `MnO4-`, `HNO3`, and `NaBiO3` were removed from visible answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00290_963bb10320`
- `expchunk_00296_a4c00bb9d1`
- `expchunk_00297_c03527ab79`
- `textbook_prose_01090_56461596a1`
- `textbook_prose_00758_5f5fd037a3`
- `textbook_prose_01241_99049758ad`
- `textbook_prose_00597_06f7e56f06`
- `textbook_prose_00598_cadca448de`

## Semantic Notes

- Sn(II) is handled through two canonical operations: FeCl3/SnCl2 checked with KSCN, and HgCl2/SnCl2 interpreted with mercury supporting theory.
- Pb(IV) is handled through PbO2 plus concentrated HCl and PbO2 plus acidified MnSO4 under water-bath heating; final redox interpretations rely on supporting theory.
- The old nitrate-acid fill blank was not retained because canonical does not support a single universal `硝酸` answer for this mixed packet.
- Bi(III)/Bi(V) items are limited to the chlorine-water/alkaline oxidation and bismuthate strong-oxidant evidence boundary.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
