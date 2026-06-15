# Chunk 4 Publish Blocker Polish Report

Date: 2026-06-15

## Scope

- Chunk: `chunk_4`.
- Packets scanned: `20-1-02`, `20-1-03`, `20-1-04`, `20-1-05`, `20-1-06`, `20-1-07`, `20-1-08`, `20-1-09`, `20-2-01`, `20-2-02`, `20-2-03`, `20-2-04`, `20-2-05`, `20-2-06`, `20-2-07`.
- Rebuilt JSON directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_4`.
- Rebuilt report directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_4`.
- Student-visible fields scanned and fixed: `stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`.
- `option_links[].diagnostic_note` status: internal option diagnostic metadata only; not included in the student-visible field scan or polish target.

## Rules Applied

- Removed internal review/reconstruction wording from student-visible fields: `canonical`, `supporting theory`, `packet`, `video point(s)`, `section path`, `alias`, and related source-boundary wording.
- Replaced those with normal student-facing wording such as `实验步骤`, `实验文本`, `实验原文`, `本实验`, `实验观察点`, `相关化学原理`, and `化学式别名`.
- Converted ASCII valence display such as `(II)`, `(III)`, `(IV)`, `(VI)`, `(VII)` to Unicode `Ⅱ`, `Ⅲ`, `Ⅳ`, `Ⅵ`, `Ⅶ` in student-visible fields.
- Scanned for ASCII digit formulas, ASCII ion/charge forms, caret syntax, LaTeX, and Markdown chemistry display leftovers.
- Did not modify `question_id`, `primary_point_keys`, `secondary_point_keys`, evidence ids, file names, or metadata locator ids.
- Did not modify any `chunk_X_release_final_v1.json` file.

## Modified Packets

Modified rebuilt JSON packets: `20-1-02`, `20-1-03`, `20-1-04`, `20-1-05`, `20-1-06`, `20-1-07`, `20-1-08`, `20-1-09`, `20-2-01`, `20-2-02`, `20-2-03`, `20-2-04`, `20-2-05`.

No JSON edits were needed for `20-2-06` or `20-2-07` after visible-field scanning.

## Question And Field Fix List

| Packet | Question ids and fields fixed | Fix category | Before snippet(s) | After snippet(s) |
|---|---|---|---|---|
| `20-1-02` | `Q017` stem/explanation; `Q018` stem/explanation; `Q026` explanation/options.A; `Q030` stem/explanation | process wording; valence display | `canonical 操作文字`; `supporting theory`; `氯化汞(II)` | `实验操作文字`; `相关化学原理`; `氯化汞(Ⅱ)` |
| `20-1-03` | `Q015` stem/explanation; `Q016` explanation; `Q019` stem; `Q020` stem/explanation; `Q022` explanation; `Q025` explanation; `Q027` explanation; `Q029` explanation; `Q030` explanation | process wording | `本 packet`; `video point`; `canonical 文本`; `canonical 操作` | `本实验`; `实验观察点`; `实验文本`; `实验步骤` |
| `20-1-03` | `Q003` package evidence declaration | evidence closure | source_audit cited `textbook_prose_00394_04911a6294` without package declaration | added supporting theory source declaration for `textbook_prose_00394_04911a6294` |
| `20-1-04` | `Q001` explanation; `Q002` explanation; `Q009` explanation; `Q011` explanation/options.A; `Q012` stem/explanation; `Q013` stem/explanation; `Q016` stem/explanation; `Q019` stem; `Q021` stem/explanation; `Q025` stem/explanation; `Q026` stem/explanation | process wording | `canonical`; `本 packet`; `canonical chunk`; `video points` | `实验步骤`; `本实验`; `实验原文段落`; `实验观察点` |
| `20-1-05` | `Q001` explanation; `Q003` explanation; `Q004` stem; `Q007` explanation; `Q008` stem; `Q009` stem/explanation; `Q011` stem/explanation; `Q014` stem/explanation; `Q015` explanation/options.A; `Q016` stem/explanation; `Q018` explanation/options.A/options.B; `Q019` stem; `Q020` explanation/options.B; `Q021` explanation; `Q023` explanation; `Q024` stem/explanation; `Q026` stem/explanation; `Q027` explanation | process wording | `canonical`; `本 packet`; `video points`; `canonical 直接支持` | `实验步骤`; `本实验`; `实验观察点`; `实验步骤直接支持` |
| `20-1-06` | `Q001` explanation; `Q003` explanation; `Q005` explanation; `Q008` explanation; `Q010` explanation; `Q013` explanation; `Q017` explanation; `Q018` explanation; `Q020` explanation; `Q022` explanation; `Q024` explanation; `Q026` explanation | process wording | `canonical 操作`; `本 packet` | `实验步骤`; `本实验` |
| `20-1-07` | `Q001` explanation; `Q011` explanation; `Q012` explanation; `Q018` explanation; `Q021` explanation | process wording | `canonical 操作`; `alias` | `实验步骤`; `别名` |
| `20-1-08` | `Q001` explanation; `Q010` explanation; `Q011` explanation; `Q015` explanation; `Q019` stem/explanation; `Q021` explanation; `Q025` explanation | process wording | `canonical 操作`; `本 packet` | `实验步骤`; `本实验` |
| `20-1-09` | `Q001` explanation; `Q004` explanation; `Q008` explanation; `Q011` explanation; `Q014` explanation; `Q015` explanation; `Q016` explanation; `Q017` explanation; `Q021` explanation; `Q022` explanation; `Q026` explanation; `Q028` explanation | process wording | `canonical 小设计题`; `canonical 原文`; `canonical 目标` | `实验设计要求`; `实验原文`; `实验目标` |
| `20-2-01` | `Q001` explanation; `Q003` explanation; `Q007` explanation; `Q010` options.A/options.B; `Q011` explanation; `Q012` explanation; `Q013` explanation; `Q017` explanation; `Q020` stem; `Q024` explanation | process wording; valence display | `canonical 内容`; `本 packet`; `铁(III)` / `铬(III)` | `实验内容`; `本实验`; `铁(Ⅲ)` / `铬(Ⅲ)` |
| `20-2-02` | `Q001` stem/explanation; `Q002` stem/explanation; `Q003` explanation; `Q005` stem/explanation; `Q006` stem/explanation/options.B/options.C; `Q007` stem/explanation/options.C/options.D; `Q008` explanation/options.A-D; `Q010` explanation/options.A/options.C; `Q012` stem/explanation; `Q014` stem/explanation; `Q015` stem/explanation; `Q016` explanation; `Q017` explanation; `Q018` explanation; `Q019` stem/explanation; `Q020` explanation; `Q022` stem/explanation; `Q023` explanation; `Q024` stem; `Q025` stem/explanation/options.A; `Q027` stem; `Q028` explanation; `Q029` explanation; `Q030` explanation | process wording; valence display | `canonical 步骤`; `本 packet`; `(II)/(III)/(IV)/(V)/(VI)` | `实验步骤`; `本实验`; `(Ⅱ)/(Ⅲ)/(Ⅳ)/(Ⅴ)/(Ⅵ)` |
| `20-2-03` | `Q001` explanation/options.A-D; `Q002` stem/explanation/options.B-D; `Q003` stem/explanation/options.A-C; `Q004` stem/explanation/options.A-C; `Q005` explanation; `Q006` explanation; `Q010` explanation; `Q011` stem/explanation; `Q012` stem/explanation; `Q013` stem/explanation; `Q014` stem/explanation; `Q015` explanation; `Q020` explanation; `Q021` options.A-D; `Q022` stem/explanation/options.A/options.B/options.D; `Q023` stem/explanation/options.A-C; `Q024` stem/explanation/options.A-C; `Q025` explanation; `Q026` explanation; `Q030` explanation | process wording; valence display | `canonical`; `(II)/(III)/(IV)/(V)/(VI)/(VII)` | `实验步骤` / `实验内容`; `(Ⅱ)/(Ⅲ)/(Ⅳ)/(Ⅴ)/(Ⅵ)/(Ⅶ)` |
| `20-2-04` | `Q001` explanation; `Q002` explanation; `Q003` explanation/options.C; `Q004` stem/explanation; `Q005` explanation; `Q006` explanation; `Q007` stem/explanation; `Q008` stem/explanation; `Q009` explanation; `Q010` stem/explanation; `Q011` explanation; `Q012` stem/explanation; `Q013` stem/explanation; `Q014` stem/explanation; `Q015` explanation; `Q016` explanation; `Q017` explanation; `Q018` explanation; `Q019` stem/explanation; `Q020` stem/explanation; `Q021` explanation; `Q022` explanation; `Q023` explanation; `Q024` stem/explanation; `Q025` stem/explanation; `Q026` stem/explanation; `Q027` stem/explanation; `Q028` explanation; `Q029` stem/explanation; `Q030` stem/explanation | process wording; valence display | `canonical`; `本 packet`; `canonical section path`; `(II)/(IV)/(VI)/(VII)` | `实验步骤`; `本实验`; `实验小节`; `(Ⅱ)/(Ⅳ)/(Ⅵ)/(Ⅶ)` |
| `20-2-05` | `Q015` explanation; `Q020` stem/explanation | process wording | `本 packet` | `本实验` |

## Representative Before And After Snippets

- `canonical 实验文本说明...` -> `实验文本说明...`
- `canonical 步骤要求...` -> `实验步骤要求...`
- `本 packet 的点位...` -> `本实验的观察/操作...`
- `video points` -> `实验观察点`
- `supporting theory` -> `相关化学原理`
- `canonical section path` -> `实验小节`
- `alias` -> `别名` / `化学式别名`
- `铁(III)` / `钴(II)` / `锰(VII)` -> `铁(Ⅲ)` / `钴(Ⅱ)` / `锰(Ⅶ)`

## Release JSON Protection

- Release final file checked: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\chunk_4_release_final_v1.json`.
- SHA256 before polish edits: `3CC7F9DEDEB4F6E191A3CD9478CA14F2E16BB81E21006634AEB211EE15369812`.
- SHA256 after polish edits: `3CC7F9DEDEB4F6E191A3CD9478CA14F2E16BB81E21006634AEB211EE15369812`.
- Result: release final JSON was not modified by this polish pass.

## Final Validation

- Student-visible internal review/process hits: `0`.
- Student-visible ASCII digit subscript formula hits: `0`.
- Student-visible ASCII charge / ASCII valence hits: `0`.
- Student-visible caret / LaTeX / Markdown chemistry symbol hits: `0`.
- JSON parse: pass for all 15 rebuilt packet JSON files.
- Packet question count: pass; every packet has `30` questions.
- Single-choice answer/options/option_links: pass.
- RAG evidence id closure: pass; all cited ids are declared in package evidence sources and source files exist.
- Packet reports updated: `13` modified packet reports contain `Publish Blocker Polish Validation`.
- `question_id`, point keys, evidence ids, file names, and metadata locator ids: unchanged except for adding the missing package-level declaration for existing cited evidence id `textbook_prose_00394_04911a6294` in `20-1-03`.