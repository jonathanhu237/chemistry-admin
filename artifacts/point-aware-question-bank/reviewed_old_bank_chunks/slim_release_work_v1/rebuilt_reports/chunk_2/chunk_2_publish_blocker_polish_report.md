# chunk_2 Publish Blocker Polish Report

## Scan Scope

- Package scope: all 15 rebuilt package JSON files under `rebuilt_packages/chunk_2`.
- Student-visible fields scanned and manually checked: `stem`, `options[].text`, `explanation`, fill-blank accepted/visible answers, `hint`, `analysis`, `feedback`, and nested `diagnostic_note`.
- Non-student locator fields were not edited: `question_id`, point keys, evidence ids, canonical/supporting chunk ids, file names, and machine metadata.
- Scan method: rule-category scan plus manual confirmation. This was not an example-only replacement pass.

## Fix Rules

- Replace internal process language such as `packet`, `canonical`, `chunk`, `supporting theory`, `theory`, `视频点`, `本题考`, and exposed locator ids with normal student-facing wording.
- Replace ambiguous `KI-CCl₄` method labels with `碘化钾-四氯化碳法` in student-visible text.
- Keep valid formulas already using Unicode subscripts/superscripts; do not rewrite locator ids or ordinary non-subscript formulas such as HCl/NaOH as chemistry errors.
- Validate that no student-visible ASCII digit formula, ASCII charge/ion form, caret chemistry, LaTeX, or Markdown math remains.

## Fixed Packets

`19-3-03`, `19-3-04`, `19-3-05`, `19-3-06`, `19-4-01`, `19-4-02`, `19-4-03`, `19-4-04`, `19-4-05`, `19-4-06`, `19-4-07`, `19-4-08`, `19-4-09`, `19-5-01`, `19-6-01`.

## Fixed Question IDs

- `19-3-03`: `IDEAL_CH2_19_3_03_Q005`, `IDEAL_CH2_19_3_03_Q014`, `IDEAL_CH2_19_3_03_Q015`, `IDEAL_CH2_19_3_03_Q016`, `IDEAL_CH2_19_3_03_Q018`, `IDEAL_CH2_19_3_03_Q021`, `IDEAL_CH2_19_3_03_Q022`.
- `19-3-04`: `REBUILT_CH2_19_3_04_Q001`, `REBUILT_CH2_19_3_04_Q002`, `REBUILT_CH2_19_3_04_Q004`, `REBUILT_CH2_19_3_04_Q005`, `REBUILT_CH2_19_3_04_Q007`, `REBUILT_CH2_19_3_04_Q008`, `REBUILT_CH2_19_3_04_Q010`, `REBUILT_CH2_19_3_04_Q014`, `REBUILT_CH2_19_3_04_Q015`, `REBUILT_CH2_19_3_04_Q016`, `REBUILT_CH2_19_3_04_Q017`, `REBUILT_CH2_19_3_04_Q019`, `REBUILT_CH2_19_3_04_Q022`, `REBUILT_CH2_19_3_04_Q023`, `REBUILT_CH2_19_3_04_Q025`, `REBUILT_CH2_19_3_04_Q026`, `REBUILT_CH2_19_3_04_Q027`, `REBUILT_CH2_19_3_04_Q028`, `REBUILT_CH2_19_3_04_Q029`, `REBUILT_CH2_19_3_04_Q030`.
- `19-3-05`: `REBUILT_CH2_19_3_05_Q001`, `REBUILT_CH2_19_3_05_Q002`, `REBUILT_CH2_19_3_05_Q003`, `REBUILT_CH2_19_3_05_Q005`, `REBUILT_CH2_19_3_05_Q009`, `REBUILT_CH2_19_3_05_Q015`, `REBUILT_CH2_19_3_05_Q025`, `REBUILT_CH2_19_3_05_Q027`.
- `19-3-06`: `REBUILT_CH2_19_3_06_Q001`, `REBUILT_CH2_19_3_06_Q003`, `REBUILT_CH2_19_3_06_Q007`, `REBUILT_CH2_19_3_06_Q009`, `REBUILT_CH2_19_3_06_Q010`, `REBUILT_CH2_19_3_06_Q011`, `REBUILT_CH2_19_3_06_Q012`, `REBUILT_CH2_19_3_06_Q013`, `REBUILT_CH2_19_3_06_Q014`, `REBUILT_CH2_19_3_06_Q016`, `REBUILT_CH2_19_3_06_Q020`, `REBUILT_CH2_19_3_06_Q026`, `REBUILT_CH2_19_3_06_Q029`, `REBUILT_CH2_19_3_06_Q030`.
- `19-4-01`: `REBUILT_CH2_19_4_01_Q001`, `REBUILT_CH2_19_4_01_Q004`, `REBUILT_CH2_19_4_01_Q005`, `REBUILT_CH2_19_4_01_Q008`, `REBUILT_CH2_19_4_01_Q009`, `REBUILT_CH2_19_4_01_Q011`, `REBUILT_CH2_19_4_01_Q015`, `REBUILT_CH2_19_4_01_Q017`, `REBUILT_CH2_19_4_01_Q019`, `REBUILT_CH2_19_4_01_Q020`, `REBUILT_CH2_19_4_01_Q026`, `REBUILT_CH2_19_4_01_Q028`, `REBUILT_CH2_19_4_01_Q029`, `REBUILT_CH2_19_4_01_Q030`.
- `19-4-02`: `REBUILT_CH2_19_4_02_Q001`, `REBUILT_CH2_19_4_02_Q002`, `REBUILT_CH2_19_4_02_Q003`, `REBUILT_CH2_19_4_02_Q007`, `REBUILT_CH2_19_4_02_Q010`, `REBUILT_CH2_19_4_02_Q013`, `REBUILT_CH2_19_4_02_Q016`, `REBUILT_CH2_19_4_02_Q017`, `REBUILT_CH2_19_4_02_Q019`, `REBUILT_CH2_19_4_02_Q022`, `REBUILT_CH2_19_4_02_Q028`, `REBUILT_CH2_19_4_02_Q030`.
- `19-4-03`: `REBUILT_CH2_19_4_03_Q005`, `REBUILT_CH2_19_4_03_Q008`, `REBUILT_CH2_19_4_03_Q009`, `REBUILT_CH2_19_4_03_Q010`, `REBUILT_CH2_19_4_03_Q014`, `REBUILT_CH2_19_4_03_Q017`, `REBUILT_CH2_19_4_03_Q019`, `REBUILT_CH2_19_4_03_Q020`, `REBUILT_CH2_19_4_03_Q026`, `REBUILT_CH2_19_4_03_Q027`, `REBUILT_CH2_19_4_03_Q028`, `REBUILT_CH2_19_4_03_Q029`, `REBUILT_CH2_19_4_03_Q030`.
- `19-4-04`: `REBUILT_CH2_19_4_04_Q001`, `REBUILT_CH2_19_4_04_Q002`, `REBUILT_CH2_19_4_04_Q003`, `REBUILT_CH2_19_4_04_Q004`, `REBUILT_CH2_19_4_04_Q005`, `REBUILT_CH2_19_4_04_Q006`, `REBUILT_CH2_19_4_04_Q007`, `REBUILT_CH2_19_4_04_Q008`, `REBUILT_CH2_19_4_04_Q010`, `REBUILT_CH2_19_4_04_Q011`, `REBUILT_CH2_19_4_04_Q013`, `REBUILT_CH2_19_4_04_Q015`, `REBUILT_CH2_19_4_04_Q016`, `REBUILT_CH2_19_4_04_Q017`, `REBUILT_CH2_19_4_04_Q018`, `REBUILT_CH2_19_4_04_Q019`, `REBUILT_CH2_19_4_04_Q020`, `REBUILT_CH2_19_4_04_Q024`, `REBUILT_CH2_19_4_04_Q025`, `REBUILT_CH2_19_4_04_Q026`, `REBUILT_CH2_19_4_04_Q027`, `REBUILT_CH2_19_4_04_Q028`, `REBUILT_CH2_19_4_04_Q029`, `REBUILT_CH2_19_4_04_Q030`.
- `19-4-05`: `REBUILT_CH2_19_4_05_Q004`, `REBUILT_CH2_19_4_05_Q005`, `REBUILT_CH2_19_4_05_Q006`, `REBUILT_CH2_19_4_05_Q008`, `REBUILT_CH2_19_4_05_Q009`, `REBUILT_CH2_19_4_05_Q014`, `REBUILT_CH2_19_4_05_Q015`, `REBUILT_CH2_19_4_05_Q016`, `REBUILT_CH2_19_4_05_Q017`, `REBUILT_CH2_19_4_05_Q020`, `REBUILT_CH2_19_4_05_Q028`, `REBUILT_CH2_19_4_05_Q029`, `REBUILT_CH2_19_4_05_Q030`.
- `19-4-06`: `REBUILT_CH2_19_4_06_Q001`, `REBUILT_CH2_19_4_06_Q004`, `REBUILT_CH2_19_4_06_Q008`, `REBUILT_CH2_19_4_06_Q009`, `REBUILT_CH2_19_4_06_Q012`, `REBUILT_CH2_19_4_06_Q025`, `REBUILT_CH2_19_4_06_Q026`, `REBUILT_CH2_19_4_06_Q029`.
- `19-4-07`: `REBUILT_CH2_19_4_07_Q002`, `REBUILT_CH2_19_4_07_Q003`, `REBUILT_CH2_19_4_07_Q006`, `REBUILT_CH2_19_4_07_Q010`, `REBUILT_CH2_19_4_07_Q011`, `REBUILT_CH2_19_4_07_Q014`, `REBUILT_CH2_19_4_07_Q016`, `REBUILT_CH2_19_4_07_Q022`, `REBUILT_CH2_19_4_07_Q023`, `REBUILT_CH2_19_4_07_Q028`, `REBUILT_CH2_19_4_07_Q029`.
- `19-4-08`: `REBUILT_CH2_19_4_08_Q011`, `REBUILT_CH2_19_4_08_Q022`, `REBUILT_CH2_19_4_08_Q027`.
- `19-4-09`: `REBUILT_CH2_19_4_09_Q007`, `REBUILT_CH2_19_4_09_Q016`, `REBUILT_CH2_19_4_09_Q027`.
- `19-5-01`: `REBUILT_CH2_19_5_01_Q028`.
- `19-6-01`: `REBUILT_CH2_19_6_01_Q029`.

## Supplemental Fixed Question IDs From Unicode-Escape Rescan

The first scanner pass used shell-provided Chinese literals, so I reran the process-word scan with Unicode escapes and fixed the additional explicit process terms it found. Additional qids fixed in that pass:

- `19-3-03`: `IDEAL_CH2_19_3_03_Q002`, `IDEAL_CH2_19_3_03_Q029`.
- `19-3-05`: `REBUILT_CH2_19_3_05_Q018`, `REBUILT_CH2_19_3_05_Q019`.
- `19-3-06`: `REBUILT_CH2_19_3_06_Q018`, `REBUILT_CH2_19_3_06_Q019`, `REBUILT_CH2_19_3_06_Q028`.
- `19-4-02`: `REBUILT_CH2_19_4_02_Q003`, `REBUILT_CH2_19_4_02_Q021`, `REBUILT_CH2_19_4_02_Q024`.
- `19-4-03`: `REBUILT_CH2_19_4_03_Q005`, `REBUILT_CH2_19_4_03_Q022`.
- `19-4-04`: `REBUILT_CH2_19_4_04_Q027`, `REBUILT_CH2_19_4_04_Q028`.
- `19-4-05`: `REBUILT_CH2_19_4_05_Q029`.
- `19-4-06`: `REBUILT_CH2_19_4_06_Q022`.
- `19-4-08`: `REBUILT_CH2_19_4_08_Q006`, `REBUILT_CH2_19_4_08_Q011`, `REBUILT_CH2_19_4_08_Q012`, `REBUILT_CH2_19_4_08_Q014`, `REBUILT_CH2_19_4_08_Q018`, `REBUILT_CH2_19_4_08_Q026`, `REBUILT_CH2_19_4_08_Q028`.
- `19-4-09`: `REBUILT_CH2_19_4_09_Q008`, `REBUILT_CH2_19_4_09_Q025`.
- `19-6-01`: `REBUILT_CH2_19_6_01_Q030`.

## Per-Question Field and Snippet Log

Rows below group question ids that received the same visible-field rule fix; each listed question id was manually confirmed in the stated field type.

| Packet | Question ids | Fields | Before snippet | After snippet |
|---|---|---|---|---|
| 19-3-03 | Q005 | `stem` | `两个视频点位` | `两个观察步骤` |
| 19-3-03 | Q014, Q015, Q016, Q018, Q021, Q022 | `stem`, `explanation`, `diagnostic_note` | `supporting theory`, `theory` | `理论说明`, `理论依据` |
| 19-3-04 | Q001, Q002, Q004, Q005, Q007, Q008, Q015, Q019, Q029 | `stem`, `explanation`, `diagnostic_note` | `supporting theory`, `theory`, `点位` | `理论说明`, `理论支撑`, `步骤` |
| 19-3-04 | Q010, Q022, Q023, Q025, Q026, Q027, Q028, Q030 | `options`, `explanation`, `diagnostic_note` | `本 packet`, `视频点位` | `本实验`, `观察步骤` |
| 19-3-05 | Q001, Q002, Q003, Q005, Q009, Q015, Q025, Q027 | `explanation` | `theory` | `理论说明`, `理论反应式` |
| 19-3-06 | Q001, Q003, Q007, Q009, Q010, Q011, Q012, Q013, Q014, Q016, Q020, Q026, Q029, Q030 | `stem`, `explanation`, `diagnostic_note` | `theory`, `canonical`, `视频点位`, `reasoning` | `理论说明`, `教材操作`, `观察体系`, `核心推理` |
| 19-4-01 | Q001, Q004, Q005, Q008, Q009, Q011, Q015, Q017, Q019, Q020, Q026, Q028, Q029, Q030 | `stem`, `options`, `explanation`, `diagnostic_note` | `本 packet`, `canonical chunk`, `chunk id`, `视频点位`, `本题考查` | `本实验`, `教材段`, `教材段落编号`, `观察步骤`, `观察范围` |
| 19-4-02 | Q001, Q002, Q003, Q007, Q010, Q013, Q016, Q017, Q019, Q022, Q028, Q030 | `stem`, `explanation`, `diagnostic_note` | `本 packet`, `canonical 实验`, `同 chunk`, `视频点位`, `上一 packet` | `本实验`, `教材实验`, `同一教材段`, `观察步骤`, `上一组实验内容` |
| 19-4-03 | Q005, Q008, Q009, Q010, Q014, Q017, Q019, Q020, Q026, Q027, Q028, Q029, Q030 | `stem`, `explanation`, `diagnostic_note` | `本 packet`, `canonical`, `supporting theory`, `相邻 packet` | `本实验`, `教材`, `理论说明`, `相邻实验` |
| 19-4-04 | Q001-Q008, Q010-Q011, Q013, Q015-Q020, Q024-Q030 | `stem`, `options`, `explanation`, `diagnostic_note` | `KI-CCl₄ 法`, `本 packet`, `canonical`, `supporting theory`, `视频点位` | `碘化钾-四氯化碳法`, `本实验`, `教材实验`, `理论说明`, `检验方法` |
| 19-4-05 | Q004-Q006, Q008-Q009, Q014-Q017, Q020, Q028-Q030 | `stem`, `explanation`, `diagnostic_note` | `本 packet`, `supporting theory`, `本包核心`, `视频点位` | `本实验`, `理论说明`, `本实验的核心内容`, `实验观察` |
| 19-4-06 | Q001, Q004, Q008, Q009, Q012, Q025, Q026, Q029 | `stem`, `options`, `explanation`, `diagnostic_note` | `canonical 实验`, `本 packet`, `KI-CCl₄ 法`, `视频点位`, `相关 packet` | `教材实验`, `本实验`, `碘化钾-四氯化碳法`, `观察内容`, `相关实验` |
| 19-4-07 | Q002, Q003, Q006, Q010, Q011, Q014, Q016, Q022, Q023, Q028, Q029 | `stem`, `options`, `explanation`, `diagnostic_note` | `canonical 实验`, `本 packet`, `expchunk_00244`, `热分解 packet` | `教材实验`, `本热分解实验`, `硝酸根检验内容`, `热分解实验` |
| 19-4-08 | Q011, Q022, Q027 | `stem`, `explanation` | `本 packet`, `视频点` | `本实验`, `观察要点` |
| 19-4-09 | Q007, Q016, Q027 | `stem`, `explanation` | `该 packet`, `本 packet`, `点位` | `本实验`, `试剂组合要求` |
| 19-5-01 | Q028 | `stem` | `本 packet 的八个盐类点位` | `本实验的八个盐类观察内容` |
| 19-6-01 | Q029 | `stem` | `本 packet 的核心检测或处理动作` | `本实验的核心检测或处理动作` |

## Supplemental Per-Question Field and Snippet Log

| Packet | Question ids | Fields | Before snippet | After snippet |
|---|---|---|---|---|
| 19-3-03 | Q002 | `diagnostic_note` | `检出流程` | `检出任务` |
| 19-3-03 | Q029 | `stem`, `options`, `explanation` | `点位绑定`, `绑定到`, `多点位绑定` | `实验内容对应`, `对应到`, `多项实验内容` |
| 19-3-05 | Q018, Q019, Q027 | `stem`, `options`, `explanation` | `点位绑定`, `不绑定任何点位` | `实验内容对应`, `不对应任何实验内容` |
| 19-3-06 | Q018, Q019, Q028 | `stem`, `options`, `explanation` | `点位绑定`, `绑定到`, `模板化绑定` | `实验内容对应`, `对应到`, `套入` |
| 19-4-02 | Q003, Q021, Q024 | `explanation`, `diagnostic_note` | `本题`, `为避免公式输入风险` | `这里`, `不要求输入化学式` |
| 19-4-03 | Q005, Q022 | `explanation` | `视频点位` | `实验观察` |
| 19-4-04 | Q027, Q028 | `diagnostic_note` | `绑定第一/第二点位` | `对应第一/第二种检验方法` |
| 19-4-05 | Q029 | `explanation` | `本包的价值` | `本实验的价值` |
| 19-4-06 | Q022 | `explanation` | `为避免公式型答案` | `不要求输入化学式` |
| 19-4-08 | Q006, Q011, Q012, Q014, Q018, Q026, Q028 | `stem`, `explanation` | `视频点`, `本包`, `本题`, `为避免` | `观察要求`, `本实验`, `答案只接受中文名称` |
| 19-4-09 | Q008, Q025 | `explanation` | `视频点` | `实验观察` |
| 19-6-01 | Q030 | `explanation` | `四个视频点` | `四个观察环节` |

## Release JSON and ID Safety

- Direct release JSON modification: not performed.
- `chunk_2_release_final_v1.json` was not edited by this polish pass.
- `question_id` values were not modified.
- Point keys and point-key arrays were not modified.
- Evidence ids, canonical/supporting chunk ids, source files, and line-number locators were not modified.

## Final Remaining Hit Counts

- Internal review traces: 0.
- ASCII digit subscript formulas: 0.
- ASCII charge/ion forms: 0.
- caret/LaTeX/Markdown chemistry symbols: 0.
- Student-visible process note: 0.

## Final Validation Summary

- JSON parse for all 15 rebuilt packages: pass.
- Student-visible publish-blocker scan: pass, 0 hits.
- Extra student-visible internal-word scan for `本题`, `为避免`, `本包`, `绑定`, `视频点`, `流程`, and `证据边界`: pass, 0 hits.
- Per-packet rebuild reports updated with final polish check: pass.
