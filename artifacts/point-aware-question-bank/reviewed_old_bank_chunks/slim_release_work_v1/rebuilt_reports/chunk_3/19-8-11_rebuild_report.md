# 19-8-11 Rebuild Report

- packet id: `EXP_19_8_11`
- experiment code: `19-8-11`
- title: `小设计实验：分析铅丹组成`
- total questions: 30
- keep / rewrite / reject: 20 / 10 / 0
- output JSON: `rebuilt_packages/chunk_3/19-8-11_rebuilt_v1.json`

## Rewrite List

`REBUILT_CH3_19_8_11_Q006`, `REBUILT_CH3_19_8_11_Q007`, `REBUILT_CH3_19_8_11_Q008`, `REBUILT_CH3_19_8_11_Q009`, `REBUILT_CH3_19_8_11_Q010`, `REBUILT_CH3_19_8_11_Q011`, `REBUILT_CH3_19_8_11_Q012`, `REBUILT_CH3_19_8_11_Q013`, `REBUILT_CH3_19_8_11_Q014`, `REBUILT_CH3_19_8_11_Q015`

## Borderline Keeps

- `REBUILT_CH3_19_8_11_Q001`, `Q016`: retained as canonical design-goal items because expchunk_00301 directly asks for analysis of lead red composition.
- `REBUILT_CH3_19_8_11_Q002`, `Q003`, `Q017`, `Q024`, `Q028`: retained with supporting theory for lead red naming and Pb(II)/Pb(IV) structure.
- `REBUILT_CH3_19_8_11_Q004`, `Q005`, `Q018`, `Q020`, `Q025`: retained as nitric-acid/clear-solution design logic, supported by PbO forming lead nitrate.
- `REBUILT_CH3_19_8_11_Q019`, `Q022`, `Q023`, `Q026`, `Q027`, `Q029`, `Q030`: retained as sulfate/Pb(II) check items, with formula answers changed to Chinese.

## Evidence Insufficient

None. No published question is marked evidence-insufficient.

## Multi-Point Questions

- `REBUILT_CH3_19_8_11_Q009`, `Q010`, `Q013`, `Q014`, `Q015`: bind all three point keys because they cover the complete design workflow.
- `REBUILT_CH3_19_8_11_Q007`, `Q012`, `Q021`: bind composition and sulfate-check points to clean up common misconstruals.

## Fill Blank Mobile Risk

All fill blanks use short Chinese answers: `铅丹`, `硝酸`, `硫酸`, `硫酸铅`, `四价铅`, `鉴定`, `硫酸根`. Formula answers such as `Pb3O4`, `HNO3`, `H2SO4`, `PbSO4`, `Pb(IV)`, and `SO4` were removed from answer fields.

## RAG Evidence IDs Used

- `expchunk_protocol_ccb6245e7635`
- `expchunk_00301_dee65904aa`
- `textbook_prose_00756_b42e11e0c6`
- `textbook_prose_00757_85fc20341a`
- `textbook_prose_00788_cfbfaab4bc`
- `textbook_prose_00379_033ea5b92b`

## Semantic Notes

- canonical only asks for a design method; the operational sequence is treated as source-point-guided and theory-supported.
- `textbook_prose_00756_b42e11e0c6` supports the Pb(II)/Pb(IV) interpretation of lead red.
- `textbook_prose_00788_cfbfaab4bc` supports nitric acid converting PbO/Pb(II) to soluble lead nitrate and lists lead sulfate as an important insoluble lead(II) salt.
- `textbook_prose_00379_033ea5b92b` supports lead sulfate insolubility among sulfate salts.

This packet was manually rebuilt question by question; it was not script-generated or batch-normalized.


## Publish-Blocker Polish Addendum

- Student-visible field polish pass: pass.
- Scan scope: `stem`, `options[].text`, `explanation`, visible answer strings, and `option_links[].diagnostic_note`.
- Category scan after polish: internal review/process traces `0`; ASCII numeric-subscript formulas `0`; ASCII charge/ion notation `0`; caret/LaTeX/Markdown chemical symbols `0`; student-visible process notes `0`.
- Release JSON modification during this polish pass: none.
- Identity fields (`question_id`, point keys, evidence ids) were not edited by this polish pass.
