# chunk_5 Publish Blocker Polish Report

## Scope

- Rebuilt package directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5`.
- Reports directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_5`.
- Student-visible fields scanned and polished: `stem`, `options[].text`, `explanation`, fill-blank `answer.accepted_answers` / top-level visible accepted answers.
- `option_links[].diagnostic_note` was not changed: repository usage shows it is internal diagnostic metadata collected into attempt/analytics metadata, not rendered as the student-facing question text.
- Release JSON guard: no `chunk_X_release_final_v1.json` file was opened for writing; `chunk_5_release_final_v1.json` mtime was unchanged during this pass.

## Repair Rules

- Replaced internal workflow terms such as `RAG`, `canonical`, `packet`, `supporting theory`, `point keys`, `option_link`, `evidence id`, `expchunk_*`, `textbook_*`, and `candidate-*` with normal student-facing wording.
- Normalized ASCII Roman valence markers, e.g. `(III)` and `(IV)`, to Unicode forms `(Ⅲ)` and `(Ⅳ)`.
- Rechecked ASCII digit-subscript formulas and common ASCII ion/charge spellings; no remaining student-visible hits are allowed.
- Preserved identifiers and grading metadata: `question_id`, point keys, evidence ids, file names, source audit ids, and option-link labels/point keys/roles were invariant-checked before and after each packet edit.

## Modified Packets

- `20-2-08`: 56 visible-field fixes across 23 questions.
- `20-2-09`: 63 visible-field fixes across 28 questions.
- `20-2-10`: 30 visible-field fixes across 23 questions.
- `20-3-01`: 15 visible-field fixes across 14 questions.
- `20-3-02`: 34 visible-field fixes across 29 questions.
- `20-3-03`: 22 visible-field fixes across 22 questions.
- `20-3-04`: 23 visible-field fixes across 21 questions.
- `20-3-05`: 30 visible-field fixes across 28 questions.
- `20-3-06`: 17 visible-field fixes across 17 questions.
- `20-3-07`: 22 visible-field fixes across 21 questions.
- `20-3-08`: 10 visible-field fixes across 10 questions.
- `20-3-09`: 6 visible-field fixes across 6 questions.
- `20-3-10`: 11 visible-field fixes across 11 questions.
- `20-3-11`: 8 visible-field fixes across 8 questions.
- `20-3-12`: 4 visible-field fixes across 4 questions.
- `20-3-13`: 1 visible-field fixes across 1 questions.

Unmodified clean packet: `20-3-14`.

## Modified Question IDs

- `20-2-08`: `CHK5_SEM_EXP_20_2_08_001`, `CHK5_SEM_EXP_20_2_08_002`, `CHK5_SEM_EXP_20_2_08_003`, `CHK5_SEM_EXP_20_2_08_005`, `CHK5_SEM_EXP_20_2_08_006`, `CHK5_SEM_EXP_20_2_08_007`, `CHK5_SEM_EXP_20_2_08_008`, `CHK5_SEM_EXP_20_2_08_009`, `CHK5_SEM_EXP_20_2_08_010`, `CHK5_SEM_EXP_20_2_08_011`, `CHK5_SEM_EXP_20_2_08_012`, `CHK5_SEM_EXP_20_2_08_013`, `CHK5_SEM_EXP_20_2_08_014`, `CHK5_SEM_EXP_20_2_08_015`, `CHK5_SEM_EXP_20_2_08_016`, `CHK5_SEM_EXP_20_2_08_018`, `CHK5_SEM_EXP_20_2_08_019`, `CHK5_SEM_EXP_20_2_08_020`, `CHK5_SEM_EXP_20_2_08_022`, `CHK5_SEM_EXP_20_2_08_025`, `CHK5_SEM_EXP_20_2_08_026`, `CHK5_SEM_EXP_20_2_08_027`, `CHK5_SEM_EXP_20_2_08_028`
- `20-2-09`: `CHK5_SEM_EXP_20_2_09_001`, `CHK5_SEM_EXP_20_2_09_002`, `CHK5_SEM_EXP_20_2_09_003`, `CHK5_SEM_EXP_20_2_09_004`, `CHK5_SEM_EXP_20_2_09_005`, `CHK5_SEM_EXP_20_2_09_006`, `CHK5_SEM_EXP_20_2_09_007`, `CHK5_SEM_EXP_20_2_09_008`, `CHK5_SEM_EXP_20_2_09_009`, `CHK5_SEM_EXP_20_2_09_010`, `CHK5_SEM_EXP_20_2_09_011`, `CHK5_SEM_EXP_20_2_09_012`, `CHK5_SEM_EXP_20_2_09_013`, `CHK5_SEM_EXP_20_2_09_014`, `CHK5_SEM_EXP_20_2_09_015`, `CHK5_SEM_EXP_20_2_09_016`, `CHK5_SEM_EXP_20_2_09_018`, `CHK5_SEM_EXP_20_2_09_019`, `CHK5_SEM_EXP_20_2_09_020`, `CHK5_SEM_EXP_20_2_09_021`, `CHK5_SEM_EXP_20_2_09_022`, `CHK5_SEM_EXP_20_2_09_023`, `CHK5_SEM_EXP_20_2_09_024`, `CHK5_SEM_EXP_20_2_09_025`, `CHK5_SEM_EXP_20_2_09_026`, `CHK5_SEM_EXP_20_2_09_028`, `CHK5_SEM_EXP_20_2_09_029`, `CHK5_SEM_EXP_20_2_09_030`
- `20-2-10`: `CHK5_SEM_EXP_20_2_10_001`, `CHK5_SEM_EXP_20_2_10_003`, `CHK5_SEM_EXP_20_2_10_004`, `CHK5_SEM_EXP_20_2_10_005`, `CHK5_SEM_EXP_20_2_10_006`, `CHK5_SEM_EXP_20_2_10_007`, `CHK5_SEM_EXP_20_2_10_009`, `CHK5_SEM_EXP_20_2_10_011`, `CHK5_SEM_EXP_20_2_10_012`, `CHK5_SEM_EXP_20_2_10_013`, `CHK5_SEM_EXP_20_2_10_014`, `CHK5_SEM_EXP_20_2_10_015`, `CHK5_SEM_EXP_20_2_10_016`, `CHK5_SEM_EXP_20_2_10_018`, `CHK5_SEM_EXP_20_2_10_019`, `CHK5_SEM_EXP_20_2_10_021`, `CHK5_SEM_EXP_20_2_10_022`, `CHK5_SEM_EXP_20_2_10_023`, `CHK5_SEM_EXP_20_2_10_024`, `CHK5_SEM_EXP_20_2_10_025`, `CHK5_SEM_EXP_20_2_10_026`, `CHK5_SEM_EXP_20_2_10_027`, `CHK5_SEM_EXP_20_2_10_030`
- `20-3-01`: `CHK5_SEM_EXP_20_3_01_002`, `CHK5_SEM_EXP_20_3_01_005`, `CHK5_SEM_EXP_20_3_01_007`, `CHK5_SEM_EXP_20_3_01_008`, `CHK5_SEM_EXP_20_3_01_010`, `CHK5_SEM_EXP_20_3_01_011`, `CHK5_SEM_EXP_20_3_01_015`, `CHK5_SEM_EXP_20_3_01_018`, `CHK5_SEM_EXP_20_3_01_020`, `CHK5_SEM_EXP_20_3_01_021`, `CHK5_SEM_EXP_20_3_01_022`, `CHK5_SEM_EXP_20_3_01_025`, `CHK5_SEM_EXP_20_3_01_026`, `CHK5_SEM_EXP_20_3_01_027`
- `20-3-02`: `CHK5_SEM_EXP_20_3_02_001`, `CHK5_SEM_EXP_20_3_02_002`, `CHK5_SEM_EXP_20_3_02_003`, `CHK5_SEM_EXP_20_3_02_004`, `CHK5_SEM_EXP_20_3_02_005`, `CHK5_SEM_EXP_20_3_02_006`, `CHK5_SEM_EXP_20_3_02_007`, `CHK5_SEM_EXP_20_3_02_008`, `CHK5_SEM_EXP_20_3_02_009`, `CHK5_SEM_EXP_20_3_02_010`, `CHK5_SEM_EXP_20_3_02_011`, `CHK5_SEM_EXP_20_3_02_012`, `CHK5_SEM_EXP_20_3_02_013`, `CHK5_SEM_EXP_20_3_02_014`, `CHK5_SEM_EXP_20_3_02_015`, `CHK5_SEM_EXP_20_3_02_016`, `CHK5_SEM_EXP_20_3_02_017`, `CHK5_SEM_EXP_20_3_02_018`, `CHK5_SEM_EXP_20_3_02_019`, `CHK5_SEM_EXP_20_3_02_020`, `CHK5_SEM_EXP_20_3_02_021`, `CHK5_SEM_EXP_20_3_02_022`, `CHK5_SEM_EXP_20_3_02_023`, `CHK5_SEM_EXP_20_3_02_024`, `CHK5_SEM_EXP_20_3_02_025`, `CHK5_SEM_EXP_20_3_02_026`, `CHK5_SEM_EXP_20_3_02_027`, `CHK5_SEM_EXP_20_3_02_028`, `CHK5_SEM_EXP_20_3_02_030`
- `20-3-03`: `CHK5_SEM_EXP_20_3_03_001`, `CHK5_SEM_EXP_20_3_03_002`, `CHK5_SEM_EXP_20_3_03_003`, `CHK5_SEM_EXP_20_3_03_004`, `CHK5_SEM_EXP_20_3_03_005`, `CHK5_SEM_EXP_20_3_03_007`, `CHK5_SEM_EXP_20_3_03_010`, `CHK5_SEM_EXP_20_3_03_011`, `CHK5_SEM_EXP_20_3_03_012`, `CHK5_SEM_EXP_20_3_03_013`, `CHK5_SEM_EXP_20_3_03_014`, `CHK5_SEM_EXP_20_3_03_015`, `CHK5_SEM_EXP_20_3_03_016`, `CHK5_SEM_EXP_20_3_03_018`, `CHK5_SEM_EXP_20_3_03_020`, `CHK5_SEM_EXP_20_3_03_021`, `CHK5_SEM_EXP_20_3_03_022`, `CHK5_SEM_EXP_20_3_03_024`, `CHK5_SEM_EXP_20_3_03_026`, `CHK5_SEM_EXP_20_3_03_028`, `CHK5_SEM_EXP_20_3_03_029`, `CHK5_SEM_EXP_20_3_03_030`
- `20-3-04`: `CHK5_SEM_EXP_20_3_04_001`, `CHK5_SEM_EXP_20_3_04_002`, `CHK5_SEM_EXP_20_3_04_003`, `CHK5_SEM_EXP_20_3_04_004`, `CHK5_SEM_EXP_20_3_04_006`, `CHK5_SEM_EXP_20_3_04_007`, `CHK5_SEM_EXP_20_3_04_009`, `CHK5_SEM_EXP_20_3_04_011`, `CHK5_SEM_EXP_20_3_04_012`, `CHK5_SEM_EXP_20_3_04_013`, `CHK5_SEM_EXP_20_3_04_014`, `CHK5_SEM_EXP_20_3_04_018`, `CHK5_SEM_EXP_20_3_04_019`, `CHK5_SEM_EXP_20_3_04_020`, `CHK5_SEM_EXP_20_3_04_021`, `CHK5_SEM_EXP_20_3_04_023`, `CHK5_SEM_EXP_20_3_04_024`, `CHK5_SEM_EXP_20_3_04_026`, `CHK5_SEM_EXP_20_3_04_027`, `CHK5_SEM_EXP_20_3_04_028`, `CHK5_SEM_EXP_20_3_04_030`
- `20-3-05`: `CHK5_SEM_EXP_20_3_05_001`, `CHK5_SEM_EXP_20_3_05_002`, `CHK5_SEM_EXP_20_3_05_003`, `CHK5_SEM_EXP_20_3_05_004`, `CHK5_SEM_EXP_20_3_05_005`, `CHK5_SEM_EXP_20_3_05_006`, `CHK5_SEM_EXP_20_3_05_007`, `CHK5_SEM_EXP_20_3_05_008`, `CHK5_SEM_EXP_20_3_05_009`, `CHK5_SEM_EXP_20_3_05_010`, `CHK5_SEM_EXP_20_3_05_011`, `CHK5_SEM_EXP_20_3_05_012`, `CHK5_SEM_EXP_20_3_05_013`, `CHK5_SEM_EXP_20_3_05_014`, `CHK5_SEM_EXP_20_3_05_015`, `CHK5_SEM_EXP_20_3_05_017`, `CHK5_SEM_EXP_20_3_05_018`, `CHK5_SEM_EXP_20_3_05_019`, `CHK5_SEM_EXP_20_3_05_020`, `CHK5_SEM_EXP_20_3_05_021`, `CHK5_SEM_EXP_20_3_05_022`, `CHK5_SEM_EXP_20_3_05_023`, `CHK5_SEM_EXP_20_3_05_024`, `CHK5_SEM_EXP_20_3_05_025`, `CHK5_SEM_EXP_20_3_05_026`, `CHK5_SEM_EXP_20_3_05_027`, `CHK5_SEM_EXP_20_3_05_028`, `CHK5_SEM_EXP_20_3_05_030`
- `20-3-06`: `CHK5_SEM_EXP_20_3_06_001`, `CHK5_SEM_EXP_20_3_06_002`, `CHK5_SEM_EXP_20_3_06_003`, `CHK5_SEM_EXP_20_3_06_004`, `CHK5_SEM_EXP_20_3_06_005`, `CHK5_SEM_EXP_20_3_06_007`, `CHK5_SEM_EXP_20_3_06_008`, `CHK5_SEM_EXP_20_3_06_011`, `CHK5_SEM_EXP_20_3_06_012`, `CHK5_SEM_EXP_20_3_06_014`, `CHK5_SEM_EXP_20_3_06_017`, `CHK5_SEM_EXP_20_3_06_020`, `CHK5_SEM_EXP_20_3_06_021`, `CHK5_SEM_EXP_20_3_06_022`, `CHK5_SEM_EXP_20_3_06_023`, `CHK5_SEM_EXP_20_3_06_024`, `CHK5_SEM_EXP_20_3_06_028`
- `20-3-07`: `CHK5_SEM_EXP_20_3_07_001`, `CHK5_SEM_EXP_20_3_07_002`, `CHK5_SEM_EXP_20_3_07_003`, `CHK5_SEM_EXP_20_3_07_004`, `CHK5_SEM_EXP_20_3_07_005`, `CHK5_SEM_EXP_20_3_07_006`, `CHK5_SEM_EXP_20_3_07_008`, `CHK5_SEM_EXP_20_3_07_010`, `CHK5_SEM_EXP_20_3_07_011`, `CHK5_SEM_EXP_20_3_07_014`, `CHK5_SEM_EXP_20_3_07_015`, `CHK5_SEM_EXP_20_3_07_016`, `CHK5_SEM_EXP_20_3_07_017`, `CHK5_SEM_EXP_20_3_07_020`, `CHK5_SEM_EXP_20_3_07_022`, `CHK5_SEM_EXP_20_3_07_023`, `CHK5_SEM_EXP_20_3_07_024`, `CHK5_SEM_EXP_20_3_07_025`, `CHK5_SEM_EXP_20_3_07_027`, `CHK5_SEM_EXP_20_3_07_029`, `CHK5_SEM_EXP_20_3_07_030`
- `20-3-08`: `CHK5_SEM_EXP_20_3_08_001`, `CHK5_SEM_EXP_20_3_08_002`, `CHK5_SEM_EXP_20_3_08_004`, `CHK5_SEM_EXP_20_3_08_006`, `CHK5_SEM_EXP_20_3_08_011`, `CHK5_SEM_EXP_20_3_08_013`, `CHK5_SEM_EXP_20_3_08_017`, `CHK5_SEM_EXP_20_3_08_021`, `CHK5_SEM_EXP_20_3_08_024`, `CHK5_SEM_EXP_20_3_08_027`
- `20-3-09`: `CHK5_SEM_EXP_20_3_09_002`, `CHK5_SEM_EXP_20_3_09_011`, `CHK5_SEM_EXP_20_3_09_015`, `CHK5_SEM_EXP_20_3_09_018`, `CHK5_SEM_EXP_20_3_09_022`, `CHK5_SEM_EXP_20_3_09_028`
- `20-3-10`: `CHK5_SEM_EXP_20_3_10_001`, `CHK5_SEM_EXP_20_3_10_002`, `CHK5_SEM_EXP_20_3_10_004`, `CHK5_SEM_EXP_20_3_10_007`, `CHK5_SEM_EXP_20_3_10_009`, `CHK5_SEM_EXP_20_3_10_011`, `CHK5_SEM_EXP_20_3_10_013`, `CHK5_SEM_EXP_20_3_10_015`, `CHK5_SEM_EXP_20_3_10_024`, `CHK5_SEM_EXP_20_3_10_027`, `CHK5_SEM_EXP_20_3_10_028`
- `20-3-11`: `CHK5_SEM_EXP_20_3_11_001`, `CHK5_SEM_EXP_20_3_11_002`, `CHK5_SEM_EXP_20_3_11_004`, `CHK5_SEM_EXP_20_3_11_005`, `CHK5_SEM_EXP_20_3_11_011`, `CHK5_SEM_EXP_20_3_11_012`, `CHK5_SEM_EXP_20_3_11_014`, `CHK5_SEM_EXP_20_3_11_026`
- `20-3-12`: `CHK5_SEM_EXP_20_3_12_001`, `CHK5_SEM_EXP_20_3_12_004`, `CHK5_SEM_EXP_20_3_12_005`, `CHK5_SEM_EXP_20_3_12_014`
- `20-3-13`: `CHK5_SEM_EXP_20_3_13_029`

## Field-Level Fix Log

### 20-2-08

- `CHK5_SEM_EXP_20_2_08_001`
  - `stem` before: `在《20-2-08 铬(III)盐的水解》中，哪一组操作与视频点位“Cr₂(SO₄)₃ + Na₂CO₃”完全对应？`
  - `stem` after: `在《20-2-08 铬(Ⅲ)盐的水解》中，哪一组操作与视频点位“Cr₂(SO₄)₃ + Na₂CO₃”完全对应？`
  - `explanation` before: `教材在金属离子水解作用小节中把铬(III)盐水解写为向 Cr₂(SO₄)₃ 溶液中滴加 Na₂CO₃ 溶液并观察现象；B、C 分别是钛(IV)盐和铁(III)盐水解，D 是其他离子鉴定语境。`
  - `explanation` after: `教材在金属离子水解作用小节中把铬(Ⅲ)盐水解写为向 Cr₂(SO₄)₃ 溶液中滴加 Na₂CO₃ 溶液并观察现象；B、C 分别是钛(Ⅳ)盐和铁(Ⅲ)盐水解，D 是其他离子鉴定语境。`

- `CHK5_SEM_EXP_20_2_08_002`
  - `options[2].text` before: `只写“出现沉淀”，不写铬(III)盐来源`
  - `options[2].text` after: `只写“出现沉淀”，不写铬(Ⅲ)盐来源`
  - `explanation` before: `RAG 实验步骤明确限定了底物 Cr₂(SO₄)₃、加入试剂 Na₂CO₃ 和观察任务。省略任一关键要素都会让题目退化成泛泛记忆或相邻实验混淆。`
  - `explanation` after: `实验步骤明确限定了底物 Cr₂(SO₄)₃、加入试剂 Na₂CO₃ 和观察任务。省略任一关键要素都会让题目退化成泛泛记忆或相邻实验混淆。`

- `CHK5_SEM_EXP_20_2_08_003`
  - `stem` before: `本 packet 的核心考点应归入哪类实验任务？`
  - `stem` after: `本实验 的核心考点应归入哪类实验任务？`
  - `explanation` before: `RAG 小节标题和步骤都属于“金属离子的水解作用”，其中 Cr₂(SO₄)₃ 与 Na₂CO₃ 对应铬(III)盐水解。`
  - `explanation` after: `教材小节标题和步骤都属于“金属离子的水解作用”，其中 Cr₂(SO₄)₃ 与 Na₂CO₃ 对应铬(Ⅲ)盐水解。`

- `CHK5_SEM_EXP_20_2_08_005`
  - `stem` before: `下列哪项属于本 packet 中不应被当作“铬(III)盐水解”直接证据的相邻实验内容？`
  - `stem` after: `下列哪项属于本实验 中不应被当作“铬(Ⅲ)盐水解”直接证据的相邻实验内容？`
  - `explanation` before: `同一 RAG chunk 中列出了铁、铬、钛三种盐的水解步骤；TiOSO₄ 稀释煮沸是钛(IV)盐水解，不能替代铬(III)盐水解。`
  - `explanation` after: `教材同一小节 中列出了铁、铬、钛三种盐的水解步骤；TiOSO₄ 稀释煮沸是钛(Ⅳ)盐水解，不能替代铬(Ⅲ)盐水解。`

- `CHK5_SEM_EXP_20_2_08_006`
  - `stem` before: `与《20-2-08 铬(III)盐的水解》相比，'expchunk_00319_b995aa9123' 更适合支撑哪类题目？`
  - `stem` after: `与《20-2-08 铬(Ⅲ)盐的水解》相比，氢氧化物酸碱性实验 更适合支撑哪类题目？`
  - `explanation` before: `'expchunk_00319_b995aa9123' 的标题是“氢氧化物的酸碱性”，内容是多种金属盐溶液滴加 NaOH 后观察并检验沉淀酸碱性；它只能作为相邻背景，不是本 packet 的主操作证据。`
  - `explanation` after: `氢氧化物酸碱性实验 的标题是“氢氧化物的酸碱性”，内容是多种金属盐溶液滴加 NaOH 后观察并检验沉淀酸碱性；它只能作为相邻背景，不是本实验 的主操作证据。`

- `CHK5_SEM_EXP_20_2_08_007`
  - `stem` before: `一个题目若只问“铬(III)盐水解用什么盐”，最主要的质量问题是什么？`
  - `stem` after: `一个题目若只问“铬(Ⅲ)盐水解用什么盐”，最主要的质量问题是什么？`
  - `options[1].text` before: `它自动覆盖了铁(III)盐和钛(IV)盐水解`
  - `options[1].text` after: `它自动覆盖了铁(Ⅲ)盐和钛(Ⅳ)盐水解`
  - `options[3].text` before: `它可以不绑定视频点位`
  - `options[3].text` after: `它可以不围绕视频点位`

- `CHK5_SEM_EXP_20_2_08_008`
  - `options[2].text` before: `问 CrO₄²⁻ 的颜色，并绑定本视频点位`
  - `options[2].text` after: `问 CrO₄²⁻ 的颜色，并围绕本视频点位`
  - `explanation` before: `实验 canonical 只明确给出 Cr₂(SO₄)₃ + Na₂CO₃ 并观察现象；因此 B 的证据闭合。精确颜色、铬酸根颜色或 KSCN 鉴定都超出本点位。`
  - `explanation` after: `实验 教材资料 只明确给出 Cr₂(SO₄)₃ + Na₂CO₃ 并观察现象；因此 B 的证据闭合。精确颜色、铬酸根颜色或 KSCN 鉴定都超出本点位。`

- `CHK5_SEM_EXP_20_2_08_009`
  - `stem` before: `关于 point keys，本 packet 的题目通常应如何绑定？`
  - `stem` after: `关于 实验内容，本实验 的题目通常应如何围绕？`
  - `options[0].text` before: `只绑定 candidate-1-376fa2cd，因为题目均围绕 Cr₂(SO₄)₃ + Na₂CO₃`
  - `options[0].text` after: `只围绕 本实验的 Cr₂(SO₄)₃ 与 Na₂CO₃ 观察点，因为题目均围绕 Cr₂(SO₄)₃ + Na₂CO₃`
  - `options[1].text` before: `同时绑定铁(III)盐水解点位，因为它在同一 RAG chunk`
  - `options[1].text` after: `同时围绕铁(Ⅲ)盐水解点位，因为它在教材同一小节`
  - `options[2].text` before: `同时绑定钛(IV)盐水解点位，因为它也是水解`
  - `options[2].text` after: `同时围绕钛(Ⅳ)盐水解点位，因为它也是水解`
  - `options[3].text` before: `不绑定任何点位，只引用章节标题`
  - `options[3].text` after: `不围绕任何点位，只引用章节标题`
  - `explanation` before: `源 packet 只有一个视频点位：Cr₂(SO₄)₃ + Na₂CO₃。相邻文本中的 FeCl₃ 和 TiOSO₄ 只能用于排除混淆，不能扩展为本题的 secondary point。`
  - `explanation` after: `原实验资料 只有一个视频点位：Cr₂(SO₄)₃ + Na₂CO₃。相邻文本中的 FeCl₃ 和 TiOSO₄ 只能用于排除混淆，不能扩展为本题的 额外实验点。`

- `CHK5_SEM_EXP_20_2_08_010`
  - `explanation` before: `本 canonical 实验步骤的措辞是“观察现象”，没有在该步骤给出血红色、有机层深蓝色或铬酸根黄色等具体结果。题目若问具体颜色，需要另找匹配证据。`
  - `explanation` after: `本 实验步骤的措辞是“观察现象”，没有在该步骤给出血红色、有机层深蓝色或铬酸根黄色等具体结果。如果问题涉及具体颜色，需要另找匹配证据。`

- `CHK5_SEM_EXP_20_2_08_011`
  - `stem` before: `若需要判断“Cr³⁺ 确实有水解倾向”，最合适的 supporting theory id 是哪一个？`
  - `stem` after: `若需要判断“Cr³⁺ 确实有水解倾向”，最合适的 相关化学原理依据是哪一项？`
  - `options[0].text` before: `textbook_table_record_table_p284_t01_r261`
  - `options[0].text` after: `Cr³⁺ 水解表格记录`
  - `options[1].text` before: `textbook_prose_00293_6e62d1272e`
  - `options[1].text` after: `过氧化氢氧化还原资料`
  - `options[2].text` before: `textbook_prose_01119_8478df1f7f`
  - `options[2].text` after: `铬酸根颜色资料`
  - `options[3].text` before: `expchunk_00319_b995aa9123`
  - `options[3].text` after: `氢氧化物酸碱性实验`
  - `explanation` before: `'textbook_table_record_table_p284_t01_r261' 是附录中 Cr³⁺ 水解的表格记录。过氧化氢氧化还原、离子颜色或 NaOH 酸碱性实验都不能直接证明 Cr³⁺ 水解倾向。`
  - `explanation` after: `Cr³⁺ 水解表格记录 是附录中 Cr³⁺ 水解的表格记录。过氧化氢氧化还原、离子颜色或 NaOH 酸碱性实验都不能直接证明 Cr³⁺ 水解倾向。`

- `CHK5_SEM_EXP_20_2_08_012`
  - `options[0].text` before: `textbook_table_record_table_p285_t02_r092 中 Cr(OH)₃ 的难溶化合物记录`
  - `options[0].text` after: `Cr(OH)₃ 难溶化合物记录 中 Cr(OH)₃ 的难溶化合物记录`
  - `options[1].text` before: `textbook_prose_01118_9e2eabedd8 中 d-d 跃迁与颜色解释`
  - `options[1].text` after: `d-d 跃迁与颜色解释资料 中 d-d 跃迁与颜色解释`
  - `options[2].text` before: `expchunk_00322_6c10a1661c 中 TiOSO₄ 的水解步骤`
  - `options[2].text` after: `金属离子水解实验步骤 中 TiOSO₄ 的水解步骤`
  - `options[3].text` before: `expchunk_00319_b995aa9123 中“加热可溶于稀碱的溶液”`
  - `options[3].text` after: `氢氧化物酸碱性实验 中“加热可溶于稀碱的溶液”`

- `CHK5_SEM_EXP_20_2_08_013`
  - `explanation` before: `判断正确。这句话与 canonical 实验步骤和视频点位标题完全一致。`
  - `explanation` after: `判断正确。这句话与 实验步骤和视频点位标题完全一致。`

- `CHK5_SEM_EXP_20_2_08_014`
  - `stem` before: `判断：仅凭 'expchunk_00322_6c10a1661c'，可以断言该步骤的具体沉淀颜色。`
  - `stem` after: `判断：仅凭 金属离子水解实验步骤，可以断言该步骤的具体沉淀颜色。`
  - `explanation` before: `判断错误。该 canonical 步骤只写“观察现象”，未给出具体颜色；涉及颜色或沉淀成分时需要额外匹配证据。`
  - `explanation` after: `判断错误。该 实验步骤只写“观察现象”，未给出具体颜色；涉及颜色或沉淀成分时需要额外匹配证据。`

- `CHK5_SEM_EXP_20_2_08_015`
  - `explanation` before: `判断正确。RAG 中同一小节列出铁(III)、铬(III)、钛(IV)三种盐的水解步骤；本 packet 只取中间的铬(III)盐水解点位。`
  - `explanation` after: `判断正确。教材资料中同一小节列出铁(Ⅲ)、铬(Ⅲ)、钛(Ⅳ)三种盐的水解步骤；本实验 只取中间的铬(Ⅲ)盐水解点位。`

- `CHK5_SEM_EXP_20_2_08_016`
  - `stem` before: `判断：把 NaOH 酸碱性实验中的操作直接当成本 packet 的 Na₂CO₃ 水解操作，是证据错配。`
  - `stem` after: `判断：把 NaOH 酸碱性实验中的操作直接当成本实验 的 Na₂CO₃ 水解操作，是证据错配。`
  - `explanation` before: `判断正确。'expchunk_00319' 是 NaOH 和沉淀酸碱性测试；本 packet 的主操作来自 'expchunk_00322' 中 Cr₂(SO₄)₃ 加 Na₂CO₃ 的水解观察。`
  - `explanation` after: `判断正确。氢氧化物酸碱性实验 是 NaOH 和沉淀酸碱性测试；本实验 的主操作来自 金属离子水解实验步骤 中 Cr₂(SO₄)₃ 加 Na₂CO₃ 的水解观察。`

- `CHK5_SEM_EXP_20_2_08_018`
  - `stem` before: `判断：本 packet 中没有真实跨多个视频点位的题目需求。`
  - `stem` after: `判断：本实验 中没有跨多个视频点位的判断需求。`
  - `explanation` before: `判断正确。源 packet 只有一个视频点位 candidate-1-376fa2cd，题目最多引用相邻 RAG 文本作排除项，不应模板化绑定 secondary point。`
  - `explanation` after: `判断正确。原实验资料 只有一个视频点位 本实验的 Cr₂(SO₄)₃ 与 Na₂CO₃ 观察点，最多引用相邻 教材内容作排除项，不应机械加入 额外实验点。`

- `CHK5_SEM_EXP_20_2_08_019`
  - `stem` before: `以下哪种题干最不适合直接发布为本 packet 的高质量题？`
  - `stem` after: `以下哪种说法最不适合直接发布为本实验 的准确结论题？`
  - `options[0].text` before: `“为什么 Cr₂(SO₄)₃ 与 Na₂CO₃ 的组合能代表铬(III)盐水解？”`
  - `options[0].text` after: `“为什么 Cr₂(SO₄)₃ 与 Na₂CO₃ 的组合能代表铬(Ⅲ)盐水解？”`

- `CHK5_SEM_EXP_20_2_08_020`
  - `explanation` before: `RAG 对本点位给出的试剂组合是 Cr₂(SO₄)₃ 和 Na₂CO₃。KSCN 血红色反应不在该步骤中，不能作为本实验结论。`
  - `explanation` after: `教材资料 对本点位给出的试剂组合是 Cr₂(SO₄)₃ 和 Na₂CO₃。KSCN 血红色反应不在该步骤中，不能作为本实验结论。`

- `CHK5_SEM_EXP_20_2_08_022`
  - `stem` before: `哪项最能说明“CrO₄²⁻ 黄色”不应作为本 packet 的正确答案？`
  - `stem` after: `哪项最能说明“CrO₄²⁻ 黄色”不应作为本实验 的正确答案？`
  - `explanation` before: `即使其他章节讨论 CrO₄²⁻ 颜色，它也不等于本实验的 Cr₂(SO₄)₃ + Na₂CO₃ 水解观察；本 packet 的正确证据应回到该操作体系。`
  - `explanation` after: `即使其他章节讨论 CrO₄²⁻ 颜色，它也不等于本实验的 Cr₂(SO₄)₃ + Na₂CO₃ 水解观察；本实验 的正确证据应回到该操作体系。`

- `CHK5_SEM_EXP_20_2_08_025`
  - `stem` before: `下列哪项解释最符合“为什么不能只靠原 packet 继承的 theory ids”？`
  - `stem` after: `下列哪项解释最符合“为什么不能只靠原实验资料 继承的 相关化学原理依据”？`
  - `options[0].text` before: `因为 theory id 只要存在于 RAG，就一定能支撑任意题目`
  - `options[0].text` after: `因为 相关化学原理依据 只要存在于 教材资料，就一定能支撑任意题目`
  - `options[1].text` before: `因为必须读 RAG 文本，确认该 theory 是否真的支撑最终题干的判断`
  - `options[1].text` after: `因为必须读 教材内容，确认该 相关化学原理 是否真的支撑最终题干的判断`
  - `options[2].text` before: `因为所有题目都只能引用 canonical，不能引用 theory`
  - `options[2].text` after: `因为所有题目都只能引用 教材资料，不能引用 相关化学原理`
  - `options[3].text` before: `因为 option_links 可以替代 evidence ids`
  - `options[3].text` after: `因为 选项反馈 可以替代 教材依据`
  - `explanation` before: `原 packet 中继承了离子颜色和过氧化氢氧化还原等 theory ids，但这些并不自动支撑铬(III)盐水解题。最终题目只在 Cr³⁺ 水解或 Cr(OH)₃ 难溶判断处使用匹配 theory。`
  - `explanation` after: `原实验资料 中继承了离子颜色和过氧化氢氧化还原等 相关化学原理依据，但这些并不自动支撑铬(Ⅲ)盐水解题。题目只在 Cr³⁺ 水解或 Cr(OH)₃ 难溶判断处使用匹配 相关化学原理。`

- `CHK5_SEM_EXP_20_2_08_026`
  - `explanation` before: `RAG 实验步骤的最后任务是“观察现象”。答案为短中文词，不要求学生输入化学式。`
  - `explanation` after: `实验步骤的最后任务是“观察现象”。答案为短中文词，不要求学生输入化学式。`

- `CHK5_SEM_EXP_20_2_08_027`
  - `stem` before: `关于选项诊断，下列哪条 option_link 写法最符合本题语义？`
  - `stem` after: `关于选项诊断，下列哪条 选项反馈 写法最符合本题语义？`
  - `options[1].text` before: `“TiOSO₄ 稀释煮沸是钛(IV)盐水解，属于同小节相邻步骤，不是本铬(III)点位”`
  - `options[1].text` after: `“TiOSO₄ 稀释煮沸是钛(Ⅳ)盐水解，属于同小节相邻步骤，不是本铬(Ⅲ)点位”`
  - `explanation` before: `高质量 option_link 必须对具体选项说明错配来源。TiOSO₄ 是相邻钛(IV)盐水解，诊断应写明它与本铬(III)盐水解点位的关系。`
  - `explanation` after: `高质量 选项反馈 必须对具体选项说明错配来源。TiOSO₄ 是相邻钛(Ⅳ)盐水解，诊断应写明它与本铬(Ⅲ)盐水解点位的关系。`

- `CHK5_SEM_EXP_20_2_08_028`
  - `explanation` before: `canonical 步骤的动作不是只取铬盐或背价态，而是向 Cr₂(SO₄)₃ 溶液中加入 Na₂CO₃ 并观察现象。`
  - `explanation` after: `实验步骤的动作不是只取铬盐或背价态，而是向 Cr₂(SO₄)₃ 溶液中加入 Na₂CO₃ 并观察现象。`

### 20-2-09

- `CHK5_SEM_EXP_20_2_09_001`
  - `stem` before: `在《20-2-09 钛(IV)盐的水解》中，哪组操作完整对应视频点位“TiOSO₄ 稀释后加热煮沸”？`
  - `stem` after: `在《20-2-09 钛(Ⅳ)盐的水解》中，哪组操作完整对应视频点位“TiOSO₄ 稀释后加热煮沸”？`
  - `explanation` before: `canonical 实验步骤明确写到钛(IV)盐水解是取 TiOSO₄ 溶液，加入适量蒸馏水，加热煮沸并观察现象；C、D 分别是相邻的铁(III)盐和铬(III)盐水解步骤。`
  - `explanation` after: `实验步骤明确写到钛(Ⅳ)盐水解是取 TiOSO₄ 溶液，加入适量蒸馏水，加热煮沸并观察现象；C、D 分别是相邻的铁(Ⅲ)盐和铬(Ⅲ)盐水解步骤。`

- `CHK5_SEM_EXP_20_2_09_002`
  - `explanation` before: `canonical 步骤为“加入适量蒸馏水，加热煮沸，观察现象”，因此加水之后的关键操作是加热煮沸。`
  - `explanation` after: `实验步骤为“加入适量蒸馏水，加热煮沸，观察现象”，因此加水之后的关键操作是加热煮沸。`

- `CHK5_SEM_EXP_20_2_09_003`
  - `stem` before: `如果题目问 TiOSO₄ 水解的产物判断，哪项说法有 theory 证据支撑？`
  - `stem` after: `如果题目问 TiOSO₄ 水解的产物判断，哪项说法有 相关化学原理 证据支撑？`
  - `explanation` before: `supporting theory 明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，并进一步煅烧得到 TiO₂；其他选项不属于该水解体系。`
  - `explanation` after: `相关化学原理 明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，并进一步煅烧得到 TiO₂；其他选项不属于该水解体系。`

- `CHK5_SEM_EXP_20_2_09_004`
  - `explanation` before: `canonical 步骤要求加入适量蒸馏水，supporting theory 进一步说明稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，因此 B 的判断有证据闭合。`
  - `explanation` after: `实验步骤要求加入适量蒸馏水，相关化学原理 进一步说明稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，因此 B 的判断有证据闭合。`

- `CHK5_SEM_EXP_20_2_09_005`
  - `stem` before: `关于“加热煮沸”的作用，哪项最符合本实验与 theory 的结合？`
  - `stem` after: `关于“加热煮沸”的作用，哪项最符合本实验与 相关化学原理 的结合？`
  - `explanation` before: `canonical 要求加热煮沸并观察现象；supporting theory 明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃。C 才把操作和目的连起来。`
  - `explanation` after: `教材资料 要求加热煮沸并观察现象；相关化学原理 明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃。C 才把操作和目的连起来。`

- `CHK5_SEM_EXP_20_2_09_006`
  - `stem` before: `下列哪项是本 packet 的相邻实验干扰项，而不是钛(IV)盐水解？`
  - `stem` after: `下列哪项是本实验 的相邻实验干扰项，而不是钛(Ⅳ)盐水解？`
  - `explanation` before: `D 是同一小节中铬(III)盐水解的步骤。A、B、C 都是 TiOSO₄ 水解点位的一部分。`
  - `explanation` after: `D 是同一小节中铬(Ⅲ)盐水解的步骤。A、B、C 都是 TiOSO₄ 水解点位的一部分。`

- `CHK5_SEM_EXP_20_2_09_007`
  - `options[3].text` before: `它可以不绑定视频点位`
  - `options[3].text` after: `它可以不围绕视频点位`
  - `explanation` before: `本 packet 的语义是 TiOSO₄ 稀释后加热煮沸并观察水解，而不是孤立记忆 TiOSO₄ 名称。`
  - `explanation` after: `本实验 的语义是 TiOSO₄ 稀释后加热煮沸并观察水解，而不是孤立记忆 TiOSO₄ 名称。`

- `CHK5_SEM_EXP_20_2_09_008`
  - `stem` before: `哪项题目设计最符合 evidence-first 原则？`
  - `stem` after: `哪项题目设计最符合 依据明确 原则？`
  - `options[1].text` before: `引用实验步骤判断 TiOSO₄ 加水、煮沸、观察现象；涉及 H₂TiO₃ 时另引 theory`
  - `options[1].text` after: `引用实验步骤判断 TiOSO₄ 加水、煮沸、观察现象；涉及 H₂TiO₃ 时另引 相关化学原理`
  - `options[3].text` before: `只看 packet 中 inherited ids，不读 RAG 原文`
  - `options[3].text` after: `只看 实验 中 继承依据，不读 教材内容`
  - `explanation` before: `canonical 支撑操作步骤；产物 H₂TiO₃ 的判断需要 'textbook_prose_01156' 和 'textbook_prose_01157'。B 明确区分这两类证据。`
  - `explanation` after: `教材资料 支撑操作步骤；产物 H₂TiO₃ 的判断需要 TiOSO₄ 水解产物资料 和 TiO₂ 转化资料。B 明确区分这两类证据。`

- `CHK5_SEM_EXP_20_2_09_009`
  - `options[0].text` before: `canonical 只要求观察现象；若写白色沉淀或 H₂TiO₃，应另有 theory 支撑`
  - `options[0].text` after: `教材资料 只要求观察现象；若写白色沉淀或 H₂TiO₃，应另有 相关化学原理 支撑`
  - `options[1].text` before: `canonical 已逐字写明“红色沉淀”`
  - `options[1].text` after: `教材资料 已逐字写明“红色沉淀”`
  - `options[2].text` before: `canonical 已逐字写明“CCl₄ 层变紫”`
  - `options[2].text` after: `教材资料 已逐字写明“CCl₄ 层变紫”`
  - `options[3].text` before: `canonical 已逐字写明“金属钠熔成小球”`
  - `options[3].text` after: `教材资料 已逐字写明“金属钠熔成小球”`
  - `explanation` before: `实验步骤只写观察现象，没有直接给出具体颜色。白色水解产物或 H₂TiO₃ 需要 supporting theory；B、C、D 都是无证据或错实验语境。`
  - `explanation` after: `实验步骤只写观察现象，没有直接给出具体颜色。白色水解产物或 H₂TiO₃ 需要 相关化学原理；B、C、D 都是无证据或错实验语境。`

- `CHK5_SEM_EXP_20_2_09_010`
  - `explanation` before: `A、B、C 直接来自 canonical 的钛(IV)盐水解步骤；D 是钴离子鉴定或配合物显色语境，不属于本 packet。`
  - `explanation` after: `A、B、C 直接来自 教材资料 的钛(Ⅳ)盐水解步骤；D 是钴离子鉴定或配合物显色语境，不属于本实验。`

- `CHK5_SEM_EXP_20_2_09_011`
  - `stem` before: `关于 point keys，本 packet 的题目应如何绑定？`
  - `stem` after: `关于 实验内容，本实验 的题目应如何围绕？`
  - `options[0].text` before: `只绑定 candidate-1-5b0beabb，因为题目围绕 TiOSO₄ 稀释后加热煮沸`
  - `options[0].text` after: `只围绕 本实验的 TiOSO₄ 稀释煮沸观察点，因为题目围绕 TiOSO₄ 稀释后加热煮沸`
  - `options[1].text` before: `同时绑定铁(Ⅲ)盐水解点位，因为它在同一 RAG chunk`
  - `options[1].text` after: `同时围绕铁(Ⅲ)盐水解点位，因为它在教材同一小节`
  - `options[2].text` before: `同时绑定铬(Ⅲ)盐水解点位，因为它也在同一小节`
  - `options[2].text` after: `同时围绕铬(Ⅲ)盐水解点位，因为它也在同一小节`
  - `options[3].text` before: `不绑定任何点位，只引用章节标题`
  - `options[3].text` after: `不围绕任何点位，只引用章节标题`
  - `explanation` before: `源 packet 只有一个视频点位：TiOSO₄ 稀释后加热煮沸。铁(Ⅲ)和铬(Ⅲ)步骤只能作为相邻干扰项，不是真实 secondary point。`
  - `explanation` after: `原实验资料 只有一个视频点位：TiOSO₄ 稀释后加热煮沸。铁(Ⅲ)和铬(Ⅲ)步骤只能作为相邻干扰项，不是真实 额外实验点。`

- `CHK5_SEM_EXP_20_2_09_012`
  - `stem` before: `判断：TiOSO₄ 溶液加入蒸馏水后加热煮沸，是本实验观察钛(IV)盐水解的核心操作。`
  - `stem` after: `判断：TiOSO₄ 溶液加入蒸馏水后加热煮沸，是本实验观察钛(Ⅳ)盐水解的核心操作。`
  - `explanation` before: `判断正确。这句话概括了 canonical 钛(IV)盐水解步骤。`
  - `explanation` after: `判断正确。这句话概括了 教材资料 钛(Ⅳ)盐水解步骤。`

- `CHK5_SEM_EXP_20_2_09_013`
  - `stem` before: `判断：TiOSO₄ 水解得到 H₂TiO₃ 的判断需要 supporting theory，而不是只靠实验步骤中的“观察现象”。`
  - `stem` after: `判断：TiOSO₄ 水解得到 H₂TiO₃ 的判断需要 相关化学原理，而不是只靠实验步骤中的“观察现象”。`
  - `explanation` before: `判断正确。canonical 只写观察现象；'textbook_prose_01156' 和 'textbook_prose_01157' 才明确给出 TiOSO₄ 水解得到 H₂TiO₃。`
  - `explanation` after: `判断正确。教材资料 只写观察现象；TiOSO₄ 水解产物资料 和 TiO₂ 转化资料 才明确给出 TiOSO₄ 水解得到 H₂TiO₃。`

- `CHK5_SEM_EXP_20_2_09_014`
  - `explanation` before: `判断错误。canonical 明确要求加入适量蒸馏水，supporting theory 也说明稀释、加热使 TiOSO₄ 水解。`
  - `explanation` after: `判断错误。教材资料 明确要求加入适量蒸馏水，相关化学原理 也说明稀释、加热使 TiOSO₄ 水解。`

- `CHK5_SEM_EXP_20_2_09_015`
  - `stem` before: `判断：只知道标题含“钛(IV)盐”，还不足以回答本实验的具体操作。`
  - `stem` after: `判断：只知道标题含“钛(Ⅳ)盐”，还不足以回答本实验的具体操作。`

- `CHK5_SEM_EXP_20_2_09_016`
  - `stem` before: `判断：同一 RAG 小节还列出铁(Ⅲ)盐和铬(Ⅲ)盐水解，但它们只能作相邻背景，不能替代钛(Ⅳ)盐点位。`
  - `stem` after: `判断：同一 教材小节还列出铁(Ⅲ)盐和铬(Ⅲ)盐水解，但它们只能作相邻背景，不能替代钛(Ⅳ)盐点位。`
  - `explanation` before: `判断正确。同一小节中 Fe、Cr、Ti 三个水解步骤并列；本 packet 只绑定 TiOSO₄ 稀释煮沸点位。`
  - `explanation` after: `判断正确。同一小节中 Fe、Cr、Ti 三个水解步骤并列；本实验 只围绕 TiOSO₄ 稀释煮沸点位。`

- `CHK5_SEM_EXP_20_2_09_018`
  - `stem` before: `以下哪条 option_link 诊断最符合本 packet 的语义？`
  - `stem` after: `以下哪条 选项反馈 诊断最符合本实验 的语义？`
  - `explanation` before: `高质量 option_link 要说明具体错配来源。A 指出了 FeCl₃ 是相邻水解步骤，不是本 TiOSO₄ 点位；B 是模板话，C、D 是事实错误。`
  - `explanation` after: `高质量 选项反馈 要说明具体错配来源。A 指出了 FeCl₃ 是相邻水解步骤，不是本 TiOSO₄ 点位；B 是模板话，C、D 是事实错误。`

- `CHK5_SEM_EXP_20_2_09_019`
  - `stem` before: `若需要证明“TiOSO₄ 稀释、加热后水解得到 H₂TiO₃”，应优先使用哪组 evidence ids？`
  - `stem` after: `若需要证明“TiOSO₄ 稀释、加热后水解得到 H₂TiO₃”，应优先使用哪组 教材依据？`
  - `options[0].text` before: `只用 expchunk_00322_6c10a1661c`
  - `options[0].text` after: `只用 金属离子水解实验步骤`
  - `options[1].text` before: `expchunk_00322_6c10a1661c 加 textbook_prose_01156_e3d54318a3 和 textbook_prose_01157_702c31a997`
  - `options[1].text` after: `金属离子水解实验步骤 加 TiOSO₄ 水解产物资料 和 TiO₂ 转化资料`
  - `options[2].text` before: `textbook_prose_01179_863cead3f0 单独作为水解产物证据`
  - `options[2].text` after: `钛(Ⅳ)过氧化氢鉴定资料 单独作为水解产物证据`
  - `options[3].text` before: `任意存在于 RAG 的钛相关 id 都可`
  - `options[3].text` after: `任意存在于 教材资料 的钛相关 依据 都可`
  - `explanation` before: `canonical 支撑实验操作，'01156' 和 '01157' 支撑 TiOSO₄ 水解得到 H₂TiO₃ 的产物判断。只用 canonical 不足以证明产物，任意钛相关 id 也不等于语义支持。`
  - `explanation` after: `教材资料 支撑实验操作，'01156' 和 '01157' 支撑 TiOSO₄ 水解得到 H₂TiO₃ 的产物判断。只用 教材资料 不足以证明产物，任意钛相关 依据 也不等于语义支持。`

- `CHK5_SEM_EXP_20_2_09_020`
  - `stem` before: `下列哪项最能说明 'textbook_prose_01179_863cead3f0' 不适合作为本 packet 的主要水解产物证据？`
  - `stem` after: `下列哪项最能说明 钛(Ⅳ)过氧化氢鉴定资料 不适合作为本实验 的主要水解产物证据？`
  - `options[1].text` before: `它不是 RAG 中的真实 id`
  - `options[1].text` after: `它不是 教材资料中的真实 依据`

- `CHK5_SEM_EXP_20_2_09_021`
  - `explanation` before: `canonical 明确给出本实验试剂和操作为 TiOSO₄ 加水、煮沸、观察。CoCl₂ 与 KSCN 不属于该步骤。`
  - `explanation` after: `教材资料 明确给出本实验试剂和操作为 TiOSO₄ 加水、煮沸、观察。CoCl₂ 与 KSCN 不属于该步骤。`

- `CHK5_SEM_EXP_20_2_09_022`
  - `stem` before: `在《20-2-09 钛(IV)盐的水解》中，TiOSO₄ 稀释后需加热____。`
  - `stem` after: `在《20-2-09 钛(Ⅳ)盐的水解》中，TiOSO₄ 稀释后需加热____。`
  - `explanation` before: `canonical 步骤写明加入适量蒸馏水后加热煮沸。答案是短中文词，适合手机端输入。`
  - `explanation` after: `实验步骤写明加入适量蒸馏水后加热煮沸。答案是短中文词，适合手机端输入。`

- `CHK5_SEM_EXP_20_2_09_023`
  - `stem` before: `如果原题要求填入 TiOSO₄，最安全的发布改法是什么？`
  - `stem` after: `如果这种说法要求填入 TiOSO₄，最安全的发布改法是什么？`

- `CHK5_SEM_EXP_20_2_09_024`
  - `options[0].text` before: `canonical 只写观察现象；白色 H₂TiO₃ 或水合 TiO₂ 判断要依赖 theory`
  - `options[0].text` after: `教材资料 只写观察现象；白色 H₂TiO₃ 或水合 TiO₂ 判断要依赖 相关化学原理`
  - `options[1].text` before: `canonical 已经逐字写明白色 H₂TiO₃`
  - `options[1].text` after: `教材资料 已经逐字写明白色 H₂TiO₃`
  - `explanation` before: `canonical 没有写具体颜色或产物；supporting theory 支撑 TiOSO₄ 水解得到 H₂TiO₃，因而沉淀/产物题必须标明 theory 依赖。`
  - `explanation` after: `教材资料 没有写具体颜色或产物；相关化学原理 支撑 TiOSO₄ 水解得到 H₂TiO₃，因而沉淀/产物题必须标明 相关化学原理 依赖。`

- `CHK5_SEM_EXP_20_2_09_025`
  - `stem` before: `在《20-2-09 钛(IV)盐的水解》中，加水____是 TiOSO₄ 水解观察的重要操作。`
  - `stem` after: `在《20-2-09 钛(Ⅳ)盐的水解》中，加水____是 TiOSO₄ 水解观察的重要操作。`
  - `explanation` before: `canonical 要求加入适量蒸馏水，supporting theory 也写到稀释、加热使 TiOSO₄ 水解。答案“稀释”短且确定。`
  - `explanation` after: `教材资料 要求加入适量蒸馏水，相关化学原理 也写到稀释、加热使 TiOSO₄ 水解。答案“稀释”短且确定。`

- `CHK5_SEM_EXP_20_2_09_026`
  - `explanation` before: `B 完整复述了 canonical 中钛(IV)盐水解的顺序；A 和 C 是同小节相邻 Fe/Cr 步骤，D 是无关鉴定操作。`
  - `explanation` after: `B 完整复述了 教材资料 中钛(Ⅳ)盐水解的顺序；A 和 C 是同小节相邻 Fe/Cr 步骤，D 是无关鉴定操作。`

- `CHK5_SEM_EXP_20_2_09_028`
  - `options[0].text` before: `canonical 还要求加入适量蒸馏水、加热煮沸并观察现象`
  - `options[0].text` after: `教材资料 还要求加入适量蒸馏水、加热煮沸并观察现象`

- `CHK5_SEM_EXP_20_2_09_029`
  - `stem` before: `如果题目要求学生选出本实验的 canonical evidence id，哪项最合适？`
  - `stem` after: `如果题目要求学生选出本实验的 教材资料 教材依据，哪项最合适？`
  - `options[0].text` before: `expchunk_00322_6c10a1661c`
  - `options[0].text` after: `金属离子水解实验步骤`
  - `options[1].text` before: `textbook_prose_01179_863cead3f0`
  - `options[1].text` after: `钛(Ⅳ)过氧化氢鉴定资料`
  - `options[2].text` before: `textbook_table_record_table_p283_t01_r091`
  - `options[2].text` after: `钛化合物表格资料`
  - `explanation` before: `'expchunk_00322_6c10a1661c' 是实验教材中金属离子水解作用的 canonical chunk，直接包含 TiOSO₄ 加水、煮沸、观察现象的步骤。其他 id 可作特定 theory 背景，但不是本实验步骤主证据。`
  - `explanation` after: `金属离子水解实验步骤 是实验教材中金属离子水解作用的 教材实验步骤，直接包含 TiOSO₄ 加水、煮沸、观察现象的步骤。其他 依据 可作特定 相关化学原理 背景，但不是本实验步骤主证据。`

- `CHK5_SEM_EXP_20_2_09_030`
  - `explanation` before: `canonical 步骤写明加入适量蒸馏水。可见答案只保留“蒸馏”，避免在“____水”结构中暴露重复别名。`
  - `explanation` after: `实验步骤写明加入适量蒸馏水。可见答案只保留“蒸馏”，避免在“____水”结构中暴露重复别名。`

### 20-2-10

- `CHK5_SEM_EXP_20_2_10_001`
  - `explanation` before: `canonical 小设计实验的任务就是把含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离并检出；其他选项属于不同离子组。`
  - `explanation` after: `教材资料 小设计实验的任务就是把含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离并检出；其他选项属于不同离子组。`

- `CHK5_SEM_EXP_20_2_10_003`
  - `explanation` before: `theory 明确说明 Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似；这个性质可与锰(Ⅱ)氢氧化物的处理差异结合，用于设计分离。`
  - `explanation` after: `相关化学原理 明确说明 Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似；这个性质可与锰(Ⅱ)氢氧化物的处理差异结合，用于设计分离。`

- `CHK5_SEM_EXP_20_2_10_004`
  - `explanation` before: `前置铬氧化还原实验和 theory 都指向碱性过氧化氢可把铬(Ⅲ)氧化为 CrO₄²⁻；颜色 theory 说明 CrO₄²⁻ 呈黄色。`
  - `explanation` after: `前置铬氧化还原实验和 相关化学原理 都指向碱性过氧化氢可把铬(Ⅲ)氧化为 CrO₄²⁻；颜色 相关化学原理 说明 CrO₄²⁻ 呈黄色。`

- `CHK5_SEM_EXP_20_2_10_005`
  - `explanation` before: `theory 的铬(Ⅲ)/铝(Ⅲ)分离示意说明，NH₃/H₂O₂ 条件下 Al 生成 Al(OH)₃ 沉淀，而铬(Ⅲ)被氧化为 CrO₄²⁻ 留在溶液中。`
  - `explanation` after: `相关化学原理 的铬(Ⅲ)/铝(Ⅲ)分离示意说明，NH₃/H₂O₂ 条件下 Al 生成 Al(OH)₃ 沉淀，而铬(Ⅲ)被氧化为 CrO₄²⁻ 留在溶液中。`

- `CHK5_SEM_EXP_20_2_10_006`
  - `explanation` before: `锰(Ⅱ) theory 说明，强氧化剂可把 Mn²⁺ 氧化为 MnO₄⁻，且 MnO₄⁻ 呈紫色，现象明显，可用于鉴定 Mn²⁺。`
  - `explanation` after: `锰(Ⅱ) 相关化学原理 说明，强氧化剂可把 Mn²⁺ 氧化为 MnO₄⁻，且 MnO₄⁻ 呈紫色，现象明显，可用于鉴定 Mn²⁺。`

- `CHK5_SEM_EXP_20_2_10_007`
  - `explanation` before: `canonical 要求“分离检出”，因此设计方案不只写分离操作，还要给出每种目标离子的检出依据或确认现象。`
  - `explanation` after: `教材资料 要求“分离检出”，因此设计方案不只写分离操作，还要给出每种目标离子的检出依据或确认现象。`

- `CHK5_SEM_EXP_20_2_10_009`
  - `explanation` before: `canonical 任务的关键词是“分离检出”三种离子，因此合格题目应考查分步分离与分别检出，而不是套用无关铁显色或只处理其中一种离子。`
  - `explanation` after: `教材资料 任务的关键词是“分离检出”三种离子，因此合格题目应考查分步分离与分别检出，而不是套用无关铁显色或只处理其中一种离子。`

- `CHK5_SEM_EXP_20_2_10_011`
  - `explanation` before: `canonical 明确给出小设计实验的目标混合溶液含 Cr³⁺、Al³⁺、Mn²⁺。`
  - `explanation` after: `教材资料 明确给出小设计实验的目标混合溶液含 Cr³⁺、Al³⁺、Mn²⁺。`

- `CHK5_SEM_EXP_20_2_10_012`
  - `explanation` before: `theory 对铬(Ⅲ)/铝(Ⅲ)分离的说明正是：Al(OH)₃ 沉淀，铬(Ⅲ)被氧化为 CrO₄²⁻；这可支撑本小设计实验中的 Cr/Al 分离环节。`
  - `explanation` after: `相关化学原理 对铬(Ⅲ)/铝(Ⅲ)分离的说明正是：Al(OH)₃ 沉淀，铬(Ⅲ)被氧化为 CrO₄²⁻；这可支撑本小设计实验中的 Cr/Al 分离环节。`

- `CHK5_SEM_EXP_20_2_10_013`
  - `explanation` before: `theory 给出碱性过氧化氢将铬(Ⅲ)羟基配合物氧化为 CrO₄²⁻ 的反应证据，因此该判断正确。`
  - `explanation` after: `相关化学原理 给出碱性过氧化氢将铬(Ⅲ)羟基配合物氧化为 CrO₄²⁻ 的反应证据，因此该判断正确。`

- `CHK5_SEM_EXP_20_2_10_014`
  - `stem` before: `分离 Cr³⁺ 与 Al³⁺ 时，只加氨水、不加入 H₂O₂，就足以体现 theory 中的推荐分离思路。`
  - `stem` after: `分离 Cr³⁺ 与 Al³⁺ 时，只加氨水、不加入 H₂O₂，就足以体现 相关化学原理 中的推荐分离思路。`
  - `explanation` before: `theory 明确说 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，先把铬(Ⅲ)氧化。`
  - `explanation` after: `相关化学原理 明确说 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，先把铬(Ⅲ)氧化。`

- `CHK5_SEM_EXP_20_2_10_015`
  - `explanation` before: `锰(Ⅱ) theory 明确指出，把 Mn²⁺ 氧化成 MnO₄⁻ 且因紫色现象明显，可用于鉴定 Mn²⁺。`
  - `explanation` after: `锰(Ⅱ) 相关化学原理 明确指出，把 Mn²⁺ 氧化成 MnO₄⁻ 且因紫色现象明显，可用于鉴定 Mn²⁺。`

- `CHK5_SEM_EXP_20_2_10_016`
  - `explanation` before: `canonical 指定的是 Cr³⁺、Al³⁺、Mn²⁺，不是 Ag⁺、Pb²⁺、Zn²⁺、Cu²⁺。`
  - `explanation` after: `教材资料 指定的是 Cr³⁺、Al³⁺、Mn²⁺，不是 Ag⁺、Pb²⁺、Zn²⁺、Cu²⁺。`

- `CHK5_SEM_EXP_20_2_10_018`
  - `explanation` before: `canonical 要求分离检出。方案只列试剂不能证明每种目标离子已被分别确认，因此不完整。`
  - `explanation` after: `教材资料 要求分离检出。方案只列试剂不能证明每种目标离子已被分别确认，因此不完整。`

- `CHK5_SEM_EXP_20_2_10_019`
  - `explanation` before: `前置实验要求滴加 NaOH 并检验沉淀酸碱性；theory 也支持 Cr(OH)₃、Al(OH)₃、Mn(OH)₂ 等性质差异可服务于分离设计。`
  - `explanation` after: `前置实验要求滴加 NaOH 并检验沉淀酸碱性；相关化学原理 也支持 Cr(OH)₃、Al(OH)₃、Mn(OH)₂ 等性质差异可服务于分离设计。`

- `CHK5_SEM_EXP_20_2_10_021`
  - `options[3].text` before: `无法判断，因为 canonical 没有给出目标离子`
  - `options[3].text` after: `无法判断，因为 教材资料 没有给出目标离子`
  - `explanation` before: `canonical 已明确目标离子为 Cr³⁺、Al³⁺、Mn²⁺。Fe³⁺-KSCN 显色是错误语境，不能替代三种目标离子的分离检出。`
  - `explanation` after: `教材资料 已明确目标离子为 Cr³⁺、Al³⁺、Mn²⁺。Fe³⁺-KSCN 显色是错误语境，不能替代三种目标离子的分离检出。`

- `CHK5_SEM_EXP_20_2_10_022`
  - `stem` before: `关于 Mn²⁺ 在碱性分离步骤中的表现，哪项说法有 theory 支撑？`
  - `stem` after: `关于 Mn²⁺ 在碱性分离步骤中的表现，哪项说法有 相关化学原理 支撑？`
  - `explanation` before: `锰(Ⅱ) theory 说明 Mn²⁺ 与 OH⁻ 先生成 Mn(OH)₂ 沉淀，放置后可被氧化为棕色沉淀；这可作为分离和后续检出的线索。`
  - `explanation` after: `锰(Ⅱ) 相关化学原理 说明 Mn²⁺ 与 OH⁻ 先生成 Mn(OH)₂ 沉淀，放置后可被氧化为棕色沉淀；这可作为分离和后续检出的线索。`

- `CHK5_SEM_EXP_20_2_10_023`
  - `explanation` before: `theory 明确写到 Al(OH)₃ 呈酸碱两性，Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似。答案是短中文词，适合手机端输入。`
  - `explanation` after: `相关化学原理 明确写到 Al(OH)₃ 呈酸碱两性，Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似。答案是短中文词，适合手机端输入。`

- `CHK5_SEM_EXP_20_2_10_024`
  - `options[1].text` before: `用小设计任务定位目标，再用碱性 H₂O₂ 氧化铬(Ⅲ)的 theory 解释转化`
  - `options[1].text` after: `用小设计任务定位目标，再用碱性 H₂O₂ 氧化铬(Ⅲ)的 相关化学原理 解释转化`
  - `explanation` before: `小设计任务只规定要分离检出 Cr³⁺、Al³⁺、Mn²⁺；铬(Ⅲ)到 CrO₄²⁻ 的转化需要前置铬氧化还原实验和 supporting theory 才能证据闭合。`
  - `explanation` after: `小设计任务只规定要分离检出 Cr³⁺、Al³⁺、Mn²⁺；铬(Ⅲ)到 CrO₄²⁻ 的转化需要前置铬氧化还原实验和 相关化学原理 才能证据闭合。`

- `CHK5_SEM_EXP_20_2_10_025`
  - `options[0].text` before: `因为 canonical 不允许使用任何碱`
  - `options[0].text` after: `因为 教材资料 不允许使用任何碱`
  - `options[1].text` before: `因为 theory 指出 Cr³⁺ 与 Al³⁺ 分离需结合 H₂O₂ 氧化铬(Ⅲ)，而不是只靠氨水`
  - `options[1].text` after: `因为 相关化学原理 指出 Cr³⁺ 与 Al³⁺ 分离需结合 H₂O₂ 氧化铬(Ⅲ)，而不是只靠氨水`
  - `options[2].text` before: `因为 Al(III) 必须用 KSCN 检出`
  - `options[2].text` after: `因为 Al(Ⅲ) 必须用 KSCN 检出`
  - `explanation` before: `theory 明确说明 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，将铬(Ⅲ)氧化后实现分离。`
  - `explanation` after: `相关化学原理 明确说明 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，将铬(Ⅲ)氧化后实现分离。`

- `CHK5_SEM_EXP_20_2_10_026`
  - `explanation` before: `theory 指出 Mn²⁺ 可被强氧化剂氧化为 MnO₄⁻，且紫色现象明显，因此可作为 Mn²⁺ 的确认检出思路。`
  - `explanation` after: `相关化学原理 指出 Mn²⁺ 可被强氧化剂氧化为 MnO₄⁻，且紫色现象明显，因此可作为 Mn²⁺ 的确认检出思路。`

- `CHK5_SEM_EXP_20_2_10_027`
  - `explanation` before: `canonical 的要求不是单纯分离，而是分离检出；答案为短中文词，适合手机端输入。`
  - `explanation` after: `教材资料 的要求不是单纯分离，而是分离检出；答案为短中文词，适合手机端输入。`

- `CHK5_SEM_EXP_20_2_10_030`
  - `explanation` before: `因为 canonical 要求“分离检出”，方案必须既有分离顺序，也有能确认目标离子的检出依据或证据。`
  - `explanation` after: `因为 教材资料 要求“分离检出”，方案必须既有分离顺序，也有能确认目标离子的检出依据或证据。`

### 20-3-01

- `CHK5_SEM_EXP_20_3_01_002`
  - `explanation` before: `canonical 明确把水合阳离子和阴离子分成两组列出；分栏记录能避免把 CrO₄²⁻、MnO₄⁻ 等阴离子颜色误当作水合阳离子颜色。`
  - `explanation` after: `教材资料 明确把水合阳离子和阴离子分成两组列出；分栏记录能避免把 CrO₄²⁻、MnO₄⁻ 等阴离子颜色误当作水合阳离子颜色。`

- `CHK5_SEM_EXP_20_3_01_005`
  - `explanation` before: `表 20.5 对 Fe²⁺ 水合离子的颜色记录为浅蓝色；旧题中的浅绿色说法不采用。`
  - `explanation` after: `表 20.5 对 Fe²⁺ 水合离子的颜色记录为浅蓝色；这种说法中的浅绿色说法不采用。`

- `CHK5_SEM_EXP_20_3_01_007`
  - `explanation` before: `铬(III) 配合物材料支持 [Cr(H₂O)₆]³⁺ 相关水合铬(III)体系可呈紫色；黄色更容易对应 CrO₄²⁻ 阴离子。`
  - `explanation` after: `铬(Ⅲ) 配合物材料支持 [Cr(H₂O)₆]³⁺ 相关水合铬(Ⅲ)体系可呈紫色；黄色更容易对应 CrO₄²⁻ 阴离子。`

- `CHK5_SEM_EXP_20_3_01_008`
  - `explanation` before: `canonical 实验内容把 [Ti(H₂O)₆]³⁺ 列在水合阳离子观察对象中；本题只考查原文可直接支撑的对象归属和价态。`
  - `explanation` after: `教材资料 实验内容把 [Ti(H₂O)₆]³⁺ 列在水合阳离子观察对象中；本题只考查原文可直接支撑的对象归属和价态。`

- `CHK5_SEM_EXP_20_3_01_010`
  - `explanation` before: `D 中三项都在 canonical 水合阳离子列表中；其他选项混入了阴离子。`
  - `explanation` after: `D 中三项都在 教材资料 水合阳离子列表中；其他选项混入了阴离子。`

- `CHK5_SEM_EXP_20_3_01_011`
  - `explanation` before: `canonical 水合阳离子列表中确有 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺。`
  - `explanation` after: `教材资料 水合阳离子列表中确有 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺。`

- `CHK5_SEM_EXP_20_3_01_015`
  - `explanation` before: `RAG 表 20.5 对 Fe²⁺ 水合离子的颜色记录为浅蓝色；因此不沿用旧题的浅绿色说法。`
  - `explanation` after: `教材资料 表 20.5 对 Fe²⁺ 水合离子的颜色记录为浅蓝色；因此不沿用这种说法的浅绿色说法。`

- `CHK5_SEM_EXP_20_3_01_018`
  - `explanation` before: `canonical 水合阳离子列表中同时列出 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺，二者均带三价正电荷。`
  - `explanation` after: `教材资料 水合阳离子列表中同时列出 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺，二者均带三价正电荷。`

- `CHK5_SEM_EXP_20_3_01_020`
  - `explanation` before: `canonical 水合阳离子列表中包括 [Ni(H₂O)₆]²⁺ 和 [Co(H₂O)₆]²⁺，二者均带二价正电荷。`
  - `explanation` after: `教材资料 水合阳离子列表中包括 [Ni(H₂O)₆]²⁺ 和 [Co(H₂O)₆]²⁺，二者均带二价正电荷。`

- `CHK5_SEM_EXP_20_3_01_021`
  - `stem` before: `关于过渡金属水合离子颜色，哪项表述最符合 theory？`
  - `stem` after: `关于过渡金属水合离子颜色，哪项表述最符合 相关化学原理？`
  - `explanation` before: `theory 说明许多过渡金属水合离子或配离子的颜色与 d 轨道分裂和 d-d 跃迁有关，并且具体颜色随离子与氧化态而变。`
  - `explanation` after: `相关化学原理 说明许多过渡金属水合离子或配离子的颜色与 d 轨道分裂和 d-d 跃迁有关，并且具体颜色随离子与氧化态而变。`

- `CHK5_SEM_EXP_20_3_01_022`
  - `explanation` before: `canonical 把 CrO₄²⁻、MnO₄⁻ 等列为阴离子；theory 也说明 CrO₄²⁻ 为黄色、MnO₄⁻ 为紫色，不能把它们当作水合阳离子。`
  - `explanation` after: `教材资料 把 CrO₄²⁻、MnO₄⁻ 等列为阴离子；相关化学原理 也说明 CrO₄²⁻ 为黄色、MnO₄⁻ 为紫色，不能把它们当作水合阳离子。`

- `CHK5_SEM_EXP_20_3_01_025`
  - `explanation` before: `canonical 列出 [Fe(H₂O)₆]²⁺，但具体颜色要按表 20.5：Fe²⁺ 水合离子为浅蓝色。`
  - `explanation` after: `教材资料 列出 [Fe(H₂O)₆]²⁺，但具体颜色要按表 20.5：Fe²⁺ 水合离子为浅蓝色。`

- `CHK5_SEM_EXP_20_3_01_026`
  - `explanation` before: `canonical 证明 [Ni(H₂O)₆]²⁺ 属于观察对象；表 20.5 和镍配合物表支持其颜色为绿色。`
  - `explanation` after: `教材资料 证明 [Ni(H₂O)₆]²⁺ 属于观察对象；表 20.5 和镍配合物表支持其颜色为绿色。`

- `CHK5_SEM_EXP_20_3_01_027`
  - `explanation` before: `theory 说明过渡金属水合离子和配离子颜色与具体离子、氧化态等有关；不能把所有 d 区水合阳离子记成同一种颜色。`
  - `explanation` after: `相关化学原理 说明过渡金属水合离子和配离子颜色与具体离子、氧化态等有关；不能把所有 d 区水合阳离子记成同一种颜色。`

### 20-3-02

- `CHK5_SEM_EXP_20_3_02_001`
  - `explanation` before: `canonical 阴离子列表中包括 CrO₄²⁻；[Co(H₂O)₆]²⁺ 属于水合阳离子，Cl⁻ 和 NO₃⁻ 不在该阴离子列表中。`
  - `explanation` after: `教材阴离子列表中包括 CrO₄²⁻；[Co(H₂O)₆]²⁺ 属于水合阳离子，Cl⁻ 和 NO₃⁻ 不在该阴离子列表中。`

- `CHK5_SEM_EXP_20_3_02_002`
  - `explanation` before: `theory 明确说明 CrO₄²⁻ 呈黄色；粉红色属于 Co²⁺ 水合离子语境，紫色容易与 MnO₄⁻ 混淆。`
  - `explanation` after: `相关化学原理 明确说明 CrO₄²⁻ 呈黄色；粉红色属于 Co²⁺ 水合离子语境，紫色容易与 MnO₄⁻ 混淆。`

- `CHK5_SEM_EXP_20_3_02_003`
  - `explanation` before: `theory 明确说明 MnO₄⁻ 呈紫色；黄色更容易对应 CrO₄²⁻。`
  - `explanation` after: `相关化学原理 明确说明 MnO₄⁻ 呈紫色；黄色更容易对应 CrO₄²⁻。`

- `CHK5_SEM_EXP_20_3_02_004`
  - `explanation` before: `canonical 阴离子列表同时列出 CrO₄²⁻ 和 Cr₂O₇²⁻；theory 还说明二者可随条件相互转化，因此应区分为相关但不同的含铬含氧阴离子。`
  - `explanation` after: `教材阴离子列表同时列出 CrO₄²⁻ 和 Cr₂O₇²⁻；相关化学原理 还说明二者可随条件相互转化，因此应区分为相关但不同的含铬含氧阴离子。`

- `CHK5_SEM_EXP_20_3_02_005`
  - `explanation` before: `canonical 阴离子列表同时列出 MnO₄²⁻ 与 MnO₄⁻；二者均为阴离子，但电荷不同，不能混写。`
  - `explanation` after: `教材阴离子列表同时列出 MnO₄²⁻ 与 MnO₄⁻；二者均为阴离子，但电荷不同，不能混写。`

- `CHK5_SEM_EXP_20_3_02_006`
  - `explanation` before: `CrO₄²⁻、MnO₄⁻、VO₃⁻ 均在 canonical 阴离子列表中；A 是水合阳离子，C 和 D 不属于本实验阴离子颜色列表。`
  - `explanation` after: `CrO₄²⁻、MnO₄⁻、VO₃⁻ 均在 教材阴离子列表中；A 是水合阳离子，C 和 D 不属于本实验阴离子颜色列表。`

- `CHK5_SEM_EXP_20_3_02_007`
  - `explanation` before: `theory 指出一些高氧化态过渡金属含氧酸根阴离子虽然无 d 电子也能显色，原因是 O²⁻ 到金属中心的荷移跃迁。`
  - `explanation` after: `相关化学原理 指出一些高氧化态过渡金属含氧酸根阴离子虽然无 d 电子也能显色，原因是 O²⁻ 到金属中心的荷移跃迁。`

- `CHK5_SEM_EXP_20_3_02_008`
  - `explanation` before: `canonical 阴离子列表中同时列出 MoO₄²⁻ 和 WO₄²⁻。`
  - `explanation` after: `教材阴离子列表中同时列出 MoO₄²⁻ 和 WO₄²⁻。`

- `CHK5_SEM_EXP_20_3_02_009`
  - `explanation` before: `canonical 阴离子列表中列出 VO₃⁻，因此它属于含氧阴离子观察对象。`
  - `explanation` after: `教材阴离子列表中列出 VO₃⁻，因此它属于含氧阴离子观察对象。`

- `CHK5_SEM_EXP_20_3_02_010`
  - `explanation` before: `[Ni(H₂O)₆]²⁺ 属于上一组水合阳离子颜色对象，不属于本 packet 的阴离子颜色重点。`
  - `explanation` after: `[Ni(H₂O)₆]²⁺ 属于上一组水合阳离子颜色对象，不属于本实验 的阴离子颜色重点。`

- `CHK5_SEM_EXP_20_3_02_011`
  - `explanation` before: `theory 给出的对应关系相反：CrO₄²⁻ 为黄色，MnO₄⁻ 为紫色。`
  - `explanation` after: `相关化学原理 给出的对应关系相反：CrO₄²⁻ 为黄色，MnO₄⁻ 为紫色。`

- `CHK5_SEM_EXP_20_3_02_012`
  - `explanation` before: `canonical 列出的是 Cr、Mn、Mo、W、V 的含氧阴离子；theory 还明确 CrO₄²⁻ 与 MnO₄⁻ 是有色的。`
  - `explanation` after: `教材资料 列出的是 Cr、Mn、Mo、W、V 的含氧阴离子；相关化学原理 还明确 CrO₄²⁻ 与 MnO₄⁻ 是有色的。`

- `CHK5_SEM_EXP_20_3_02_013`
  - `explanation` before: `canonical 阴离子列表中明确列出 MoO₄²⁻ 和 WO₄²⁻，因此该说法错误。`
  - `explanation` after: `教材阴离子列表中明确列出 MoO₄²⁻ 和 WO₄²⁻，因此该说法错误。`

- `CHK5_SEM_EXP_20_3_02_014`
  - `explanation` before: `本 packet 的核心是区分 CrO₄²⁻、Cr₂O₇²⁻、MnO₄²⁻、MnO₄⁻ 等具体阴离子；记录时应把具体离子式和颜色配对。`
  - `explanation` after: `本实验 的核心是区分 CrO₄²⁻、Cr₂O₇²⁻、MnO₄²⁻、MnO₄⁻ 等具体阴离子；记录时应把具体离子式和颜色配对。`

- `CHK5_SEM_EXP_20_3_02_015`
  - `stem` before: `下列哪一项颜色对应关系可以由 theory 直接支撑？`
  - `stem` after: `下列哪一项颜色对应关系可以由 相关化学原理 直接支撑？`
  - `explanation` before: `theory 原文直接给出 CrO₄²⁻ 呈黄色、MnO₄⁻ 呈紫色，并把显色解释为荷移跃迁。`
  - `explanation` after: `相关化学原理 原文直接给出 CrO₄²⁻ 呈黄色、MnO₄⁻ 呈紫色，并把显色解释为荷移跃迁。`

- `CHK5_SEM_EXP_20_3_02_016`
  - `explanation` before: `canonical 阴离子列表中同时列出 MoO₄²⁻ 和 WO₄²⁻。`
  - `explanation` after: `教材阴离子列表中同时列出 MoO₄²⁻ 和 WO₄²⁻。`

- `CHK5_SEM_EXP_20_3_02_017`
  - `explanation` before: `canonical 在水合阳离子之后另列了阴离子观察对象，本 packet 正是阴离子颜色。`
  - `explanation` after: `教材资料 在水合阳离子之后另列了阴离子观察对象，本实验 正是阴离子颜色。`

- `CHK5_SEM_EXP_20_3_02_018`
  - `explanation` before: `theory 明确把 CrO₄²⁻、MnO₄⁻ 等含氧阴离子的颜色解释为 O²⁻ 到金属中心的荷移跃迁。`
  - `explanation` after: `相关化学原理 明确把 CrO₄²⁻、MnO₄⁻ 等含氧阴离子的颜色解释为 O²⁻ 到金属中心的荷移跃迁。`

- `CHK5_SEM_EXP_20_3_02_019`
  - `explanation` before: `canonical 阴离子列表没有 Cl⁻；本实验关注 Cr、Mn、Mo、W、V 的含氧阴离子。`
  - `explanation` after: `教材阴离子列表没有 Cl⁻；本实验关注 Cr、Mn、Mo、W、V 的含氧阴离子。`

- `CHK5_SEM_EXP_20_3_02_020`
  - `explanation` before: `canonical 阴离子列表末项列出 VO₃⁻。`
  - `explanation` after: `教材阴离子列表末项列出 VO₃⁻。`

- `CHK5_SEM_EXP_20_3_02_021`
  - `options[1].text` before: `先确认它们在 canonical 列表中，再依据实际观察或更精确颜色证据记录`
  - `options[1].text` after: `先确认它们在 教材资料 列表中，再依据实际观察或更精确颜色证据记录`
  - `explanation` before: `canonical 能证明这些离子属于观察对象，但本轮直接 theory 颜色证据只明确给出 CrO₄²⁻ 黄色和 MnO₄⁻ 紫色；其他阴离子的具体颜色不能随意套用。`
  - `explanation` after: `教材资料 能证明这些离子属于观察对象，但本轮直接 相关化学原理 颜色证据只明确给出 CrO₄²⁻ 黄色和 MnO₄⁻ 紫色；其他阴离子的具体颜色不能随意套用。`

- `CHK5_SEM_EXP_20_3_02_022`
  - `options[1].text` before: `错误；theory 只明确 MnO₄⁻ 为紫色，CrO₄²⁻ 为黄色，不能一概而论`
  - `options[1].text` after: `错误；相关化学原理 只明确 MnO₄⁻ 为紫色，CrO₄²⁻ 为黄色，不能一概而论`
  - `options[3].text` before: `无法判断，因为 canonical 没有列任何阴离子`
  - `options[3].text` after: `无法判断，因为 教材资料 没有列任何阴离子`
  - `explanation` before: `theory 明确 CrO₄²⁻ 黄色、MnO₄⁻ 紫色；因此不能把所有含氧阴离子统一记为紫色。`
  - `explanation` after: `相关化学原理 明确 CrO₄²⁻ 黄色、MnO₄⁻ 紫色；因此不能把所有含氧阴离子统一记为紫色。`

- `CHK5_SEM_EXP_20_3_02_023`
  - `explanation` before: `Cr₂O₇²⁻ 位于 canonical 阴离子列表；其余选项都是水合阳离子。`
  - `explanation` after: `Cr₂O₇²⁻ 位于 教材阴离子列表；其余选项都是水合阳离子。`

- `CHK5_SEM_EXP_20_3_02_024`
  - `stem` before: `关于 CrO₄²⁻ 的黄色和 MnO₄⁻ 的紫色，哪项解释最贴近 theory？`
  - `stem` after: `关于 CrO₄²⁻ 的黄色和 MnO₄⁻ 的紫色，哪项解释最贴近 相关化学原理？`
  - `explanation` before: `theory 把 CrO₄²⁻ 和 MnO₄⁻ 这类含氧阴离子的颜色归因于 O²⁻ 到金属中心的荷移跃迁。`
  - `explanation` after: `相关化学原理 把 CrO₄²⁻ 和 MnO₄⁻ 这类含氧阴离子的颜色归因于 O²⁻ 到金属中心的荷移跃迁。`

- `CHK5_SEM_EXP_20_3_02_025`
  - `explanation` before: `canonical 阴离子列表包含 Cr、Mn、Mo、W、V 的多个含氧阴离子；完整记录应逐项区分，而不是只写一个代表。`
  - `explanation` after: `教材阴离子列表包含 Cr、Mn、Mo、W、V 的多个含氧阴离子；完整记录应逐项区分，而不是只写一个代表。`

- `CHK5_SEM_EXP_20_3_02_026`
  - `explanation` before: `[Co(H₂O)₆]²⁺ 是水合阳离子，不属于本 packet 阴离子列表；不能用它的颜色替代含氧阴离子的颜色。`
  - `explanation` after: `[Co(H₂O)₆]²⁺ 是水合阳离子，不属于本实验 阴离子列表；不能用它的颜色替代含氧阴离子的颜色。`

- `CHK5_SEM_EXP_20_3_02_027`
  - `explanation` before: `canonical 阴离子列表列出 Cr₂O₇²⁻；它与 CrO₄²⁻ 相关但式子和电荷组成不同，应分开记录。`
  - `explanation` after: `教材阴离子列表列出 Cr₂O₇²⁻；它与 CrO₄²⁻ 相关但式子和电荷组成不同，应分开记录。`

- `CHK5_SEM_EXP_20_3_02_028`
  - `explanation` before: `canonical 阴离子列表直接列出 VO₃⁻；本题只考查原文可直接支撑的归属，不强行外推具体颜色。`
  - `explanation` after: `教材阴离子列表直接列出 VO₃⁻；本题只考查原文可直接支撑的归属，不强行外推具体颜色。`

- `CHK5_SEM_EXP_20_3_02_030`
  - `explanation` before: `Cr₂O₇²⁻ 是 canonical 列出的阴离子，右上角 ²⁻ 表示二负电荷。`
  - `explanation` after: `Cr₂O₇²⁻ 是 教材资料 列出的阴离子，右上角 ²⁻ 表示二负电荷。`

### 20-3-03

- `CHK5_SEM_EXP_20_3_03_001`
  - `explanation` before: `canonical 小节标题直接写明本实验观察 Cr(Ⅲ) 的水合异构现象。`
  - `explanation` after: `教材小节标题直接写明本实验观察 Cr(Ⅲ) 的水合异构现象。`

- `CHK5_SEM_EXP_20_3_03_002`
  - `explanation` before: `canonical 要求取少量 Cr(NO₃)₃ 溶液加热，观察加热前后颜色变化。`
  - `explanation` after: `教材资料 要求取少量 Cr(NO₃)₃ 溶液加热，观察加热前后颜色变化。`

- `CHK5_SEM_EXP_20_3_03_003`
  - `explanation` before: `canonical 指定操作是加热少量 Cr(NO₃)₃ 溶液，并观察加热前后颜色变化。`
  - `explanation` after: `教材资料 指定操作是加热少量 Cr(NO₃)₃ 溶液，并观察加热前后颜色变化。`

- `CHK5_SEM_EXP_20_3_03_004`
  - `explanation` before: `canonical 明确要求观察加热前后溶液颜色的变化。`
  - `explanation` after: `教材资料 明确要求观察加热前后溶液颜色的变化。`

- `CHK5_SEM_EXP_20_3_03_005`
  - `explanation` before: `canonical 方程式左侧为 [Cr(H₂O)₆](NO₃)₃，是加热前的配合物写法。`
  - `explanation` after: `教材方程式左侧为 [Cr(H₂O)₆](NO₃)₃，是加热前的配合物写法。`

- `CHK5_SEM_EXP_20_3_03_007`
  - `explanation` before: `canonical 方程式用双向箭头并在两侧标注热、冷，说明加热和冷却影响该水合异构平衡。`
  - `explanation` after: `教材方程式用双向箭头并在两侧标注热、冷，说明加热和冷却影响该水合异构平衡。`

- `CHK5_SEM_EXP_20_3_03_010`
  - `explanation` before: `canonical 方程式显示加热使内界由六水合形式转为五水一硝酸根形式；颜色变化用于观察这种水合异构。`
  - `explanation` after: `教材方程式显示加热使内界由六水合形式转为五水一硝酸根形式；颜色变化用于观察这种水合异构。`

- `CHK5_SEM_EXP_20_3_03_011`
  - `explanation` before: `canonical 小节标题为 Cr(Ⅲ) 的水合异构现象。`
  - `explanation` after: `教材小节标题为 Cr(Ⅲ) 的水合异构现象。`

- `CHK5_SEM_EXP_20_3_03_012`
  - `explanation` before: `canonical 指定起始溶液为 Cr(NO₃)₃ 溶液，不是 Cr₂(SO₄)₃ 加 Na₂CO₃。`
  - `explanation` after: `教材资料 指定起始溶液为 Cr(NO₃)₃ 溶液，不是 Cr₂(SO₄)₃ 加 Na₂CO₃。`

- `CHK5_SEM_EXP_20_3_03_013`
  - `explanation` before: `canonical 明确写到取 Cr(NO₃)₃ 溶液进行加热。`
  - `explanation` after: `教材资料 明确写到取 Cr(NO₃)₃ 溶液进行加热。`

- `CHK5_SEM_EXP_20_3_03_014`
  - `explanation` before: `canonical 要求观察的是加热前后溶液颜色变化，不是质量变化。`
  - `explanation` after: `教材资料 要求观察的是加热前后溶液颜色变化，不是质量变化。`

- `CHK5_SEM_EXP_20_3_03_015`
  - `explanation` before: `canonical 方程式左侧为 [Cr(H₂O)₆](NO₃)₃。`
  - `explanation` after: `教材方程式左侧为 [Cr(H₂O)₆](NO₃)₃。`

- `CHK5_SEM_EXP_20_3_03_016`
  - `explanation` before: `canonical 方程式右侧为 [Cr(H₂O)₅NO₃](NO₃)₂ 和 H₂O，说明加热后内界组成改变。`
  - `explanation` after: `教材方程式右侧为 [Cr(H₂O)₅NO₃](NO₃)₂ 和 H₂O，说明加热后内界组成改变。`

- `CHK5_SEM_EXP_20_3_03_018`
  - `explanation` before: `canonical 方程式显示进入 Cr(Ⅲ) 内界的是 NO₃⁻，SCN⁻ 属于后续 Co(Ⅱ) 配合物实验语境。`
  - `explanation` after: `教材方程式显示进入 Cr(Ⅲ) 内界的是 NO₃⁻，SCN⁻ 属于后续 Co(Ⅱ) 配合物实验语境。`

- `CHK5_SEM_EXP_20_3_03_020`
  - `explanation` before: `canonical 反应是 Cr(Ⅲ) 配合物的水合异构变化，不是生成金属铬。`
  - `explanation` after: `教材资料 反应是 Cr(Ⅲ) 配合物的水合异构变化，不是生成金属铬。`

- `CHK5_SEM_EXP_20_3_03_021`
  - `explanation` before: `canonical 要求加热 Cr(NO₃)₃ 溶液并观察颜色变化；方程式显示内界由六水合形式转为五水一硝酸根形式。`
  - `explanation` after: `教材资料 要求加热 Cr(NO₃)₃ 溶液并观察颜色变化；方程式显示内界由六水合形式转为五水一硝酸根形式。`

- `CHK5_SEM_EXP_20_3_03_022`
  - `explanation` before: `canonical 方程式没有金属铬生成；本实验结论应围绕 Cr(Ⅲ) 配合物水合异构和颜色变化。`
  - `explanation` after: `教材方程式没有金属铬生成；本实验结论应围绕 Cr(Ⅲ) 配合物水合异构和颜色变化。`

- `CHK5_SEM_EXP_20_3_03_024`
  - `explanation` before: `canonical 明确要求观察加热前后溶液颜色的变化；答案是短中文词，适合手机端输入。`
  - `explanation` after: `教材资料 明确要求观察加热前后溶液颜色的变化；答案是短中文词，适合手机端输入。`

- `CHK5_SEM_EXP_20_3_03_026`
  - `stem` before: `下列哪一项最准确概括 canonical 方程式的方向信息？`
  - `stem` after: `下列哪一项最准确概括 教材方程式的方向信息？`

- `CHK5_SEM_EXP_20_3_03_028`
  - `explanation` before: `canonical 明确要求观察加热前后溶液颜色的变化；只写操作而无颜色比较，不能支撑水合异构现象观察。`
  - `explanation` after: `教材资料 明确要求观察加热前后溶液颜色的变化；只写操作而无颜色比较，不能支撑水合异构现象观察。`

- `CHK5_SEM_EXP_20_3_03_029`
  - `explanation` before: `canonical 方程式从 [Cr(H₂O)₆](NO₃)₃ 变为 [Cr(H₂O)₅NO₃](NO₃)₂，说明一个 NO₃⁻ 进入内界且水配体减少一个。`
  - `explanation` after: `教材方程式从 [Cr(H₂O)₆](NO₃)₃ 变为 [Cr(H₂O)₅NO₃](NO₃)₂，说明一个 NO₃⁻ 进入内界且水配体减少一个。`

- `CHK5_SEM_EXP_20_3_03_030`
  - `explanation` before: `canonical 小节标题和方程式都围绕 Cr(Ⅲ) 配合物，[Cr(H₂O)₆](NO₃)₃ 与 [Cr(H₂O)₅NO₃](NO₃)₂ 都不是金属铬单质。`
  - `explanation` after: `教材小节标题和方程式都围绕 Cr(Ⅲ) 配合物，[Cr(H₂O)₆](NO₃)₃ 与 [Cr(H₂O)₅NO₃](NO₃)₂ 都不是金属铬单质。`

### 20-3-04

- `CHK5_SEM_EXP_20_3_04_001`
  - `explanation` before: `canonical 规定向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`
  - `explanation` after: `教材资料 规定向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`

- `CHK5_SEM_EXP_20_3_04_002`
  - `explanation` before: `canonical 要求把蓝紫色溶液分至三支试管，其中两支分别加入蒸馏水和丙酮，另一支保留对照。`
  - `explanation` after: `教材资料 要求把蓝紫色溶液分至三支试管，其中两支分别加入蒸馏水和丙酮，另一支保留对照。`

- `CHK5_SEM_EXP_20_3_04_003`
  - `explanation` before: `canonical 方程式显示加水与硫氰配合物相互转化时可形成 [Co(H₂O)₆]²⁺；表 20.10 也支持该水合钴(Ⅱ)配合物为粉红色。`
  - `explanation` after: `教材方程式显示加水与硫氰配合物相互转化时可形成 [Co(H₂O)₆]²⁺；表 20.10 也支持该水合钴(Ⅱ)配合物为粉红色。`

- `CHK5_SEM_EXP_20_3_04_004`
  - `explanation` before: `canonical 方程式把丙酮标在硫氰合钴(Ⅱ)络阴离子方向；表 20.10 也支持钴(Ⅱ)硫氰配合物呈蓝色。`
  - `explanation` after: `教材方程式把丙酮标在硫氰合钴(Ⅱ)络阴离子方向；表 20.10 也支持钴(Ⅱ)硫氰配合物呈蓝色。`

- `CHK5_SEM_EXP_20_3_04_006`
  - `explanation` before: `KSCN 提供 SCN⁻，canonical 方程式中的钴(Ⅱ)-硫氰络阴离子正是由 SCN⁻ 配位形成。`
  - `explanation` after: `KSCN 提供 SCN⁻，教材方程式中的钴(Ⅱ)-硫氰络阴离子正是由 SCN⁻ 配位形成。`

- `CHK5_SEM_EXP_20_3_04_007`
  - `explanation` before: `canonical 要求把溶液分为三支试管，其中一支原溶液用于对照，便于比较水和丙酮处理后的颜色差异。`
  - `explanation` after: `教材资料 要求把溶液分为三支试管，其中一支原溶液用于对照，便于比较水和丙酮处理后的颜色差异。`

- `CHK5_SEM_EXP_20_3_04_009`
  - `explanation` before: `canonical 方程式中的硫氰钴络阴离子含四个 SCN⁻ 配体；题目用中文计数避免公式输入。`
  - `explanation` after: `教材方程式中的硫氰钴络阴离子含四个 SCN⁻ 配体；题目用中文计数避免公式输入。`

- `CHK5_SEM_EXP_20_3_04_011`
  - `explanation` before: `canonical 明确要求在两支试管中分别加入蒸馏水和丙酮，对比三支试管颜色差异。`
  - `explanation` after: `教材资料 明确要求在两支试管中分别加入蒸馏水和丙酮，对比三支试管颜色差异。`

- `CHK5_SEM_EXP_20_3_04_012`
  - `explanation` before: `canonical 使用 KSCN 饱和溶液，并在方程式中出现 SCN⁻，说明它是硫氰配体来源。`
  - `explanation` after: `教材资料 使用 KSCN 饱和溶液，并在方程式中出现 SCN⁻，说明它是硫氰配体来源。`

- `CHK5_SEM_EXP_20_3_04_013`
  - `explanation` before: `canonical 方程式显示硫氰合钴(Ⅱ)络阴离子与水可转化为 [Co(H₂O)₆]²⁺。`
  - `explanation` after: `教材方程式显示硫氰合钴(Ⅱ)络阴离子与水可转化为 [Co(H₂O)₆]²⁺。`

- `CHK5_SEM_EXP_20_3_04_014`
  - `explanation` before: `canonical 方程式将丙酮标在硫氰合钴(Ⅱ)络阴离子方向，表 20.10 也支持钴(Ⅱ)硫氰配合物为蓝色。`
  - `explanation` after: `教材方程式将丙酮标在硫氰合钴(Ⅱ)络阴离子方向，表 20.10 也支持钴(Ⅱ)硫氰配合物为蓝色。`

- `CHK5_SEM_EXP_20_3_04_018`
  - `explanation` before: `canonical 方程式和实验设计共同说明：水推动形成 [Co(H₂O)₆]²⁺ 一侧，丙酮推动蓝色硫氰钴配合物一侧。`
  - `explanation` after: `教材方程式和实验设计共同说明：水推动形成 [Co(H₂O)₆]²⁺ 一侧，丙酮推动蓝色硫氰钴配合物一侧。`

- `CHK5_SEM_EXP_20_3_04_019`
  - `explanation` before: `canonical 初始操作正是向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`
  - `explanation` after: `教材资料 初始操作正是向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`

- `CHK5_SEM_EXP_20_3_04_020`
  - `explanation` before: `canonical 方程式显示硫氰钴配合物与水合钴(Ⅱ)配合物之间存在可逆配体交换，丙酮和水条件影响方向。`
  - `explanation` after: `教材方程式显示硫氰钴配合物与水合钴(Ⅱ)配合物之间存在可逆配体交换，丙酮和水条件影响方向。`

- `CHK5_SEM_EXP_20_3_04_021`
  - `explanation` before: `canonical 明确把蓝紫色溶液分至三支试管，其中两支分别加水和丙酮，剩余一支用于对照。`
  - `explanation` after: `教材资料 明确把蓝紫色溶液分至三支试管，其中两支分别加水和丙酮，剩余一支用于对照。`

- `CHK5_SEM_EXP_20_3_04_023`
  - `explanation` before: `canonical 方程式把丙酮标在硫氰钴配合物方向；表 20.10 也支持钴(Ⅱ)硫氰配合物呈蓝色。`
  - `explanation` after: `教材方程式把丙酮标在硫氰钴配合物方向；表 20.10 也支持钴(Ⅱ)硫氰配合物呈蓝色。`

- `CHK5_SEM_EXP_20_3_04_024`
  - `options[1].text` before: `用 canonical 定位加水处理，再用表 20.10 确认水合钴(Ⅱ)配合物为粉红色`
  - `options[1].text` after: `用 教材资料 定位加水处理，再用表 20.10 确认水合钴(Ⅱ)配合物为粉红色`
  - `explanation` before: `canonical 说明加水使体系转向 [Co(H₂O)₆]²⁺；表 20.10 明确该水合钴(Ⅱ)配合物呈粉红色。`
  - `explanation` after: `教材资料 说明加水使体系转向 [Co(H₂O)₆]²⁺；表 20.10 明确该水合钴(Ⅱ)配合物呈粉红色。`

- `CHK5_SEM_EXP_20_3_04_026`
  - `explanation` before: `canonical 的设计是三支试管对比；完整记录应把原溶液、加水、加丙酮三个条件下的颜色分开。`
  - `explanation` after: `教材资料 的设计是三支试管对比；完整记录应把原溶液、加水、加丙酮三个条件下的颜色分开。`

- `CHK5_SEM_EXP_20_3_04_027`
  - `explanation` before: `[Co(H₂O)₆]²⁺ 是 canonical 方程式中的水合钴(Ⅱ)配合物，式中右下角六表示六个水配体。`
  - `explanation` after: `[Co(H₂O)₆]²⁺ 是 教材方程式中的水合钴(Ⅱ)配合物，式中右下角六表示六个水配体。`

- `CHK5_SEM_EXP_20_3_04_028`
  - `options[3].text` before: `无法判断，因为 canonical 没有给出金属元素`
  - `options[3].text` after: `无法判断，因为 教材资料 没有给出金属元素`
  - `explanation` before: `canonical 明确使用 CoCl₂ 和 KSCN 生成钴(Ⅱ)配合物；表 20.10 中 Fe(Ⅲ)-硫氰配合物血红色是另一个金属体系，不能套用。`
  - `explanation` after: `教材资料 明确使用 CoCl₂ 和 KSCN 生成钴(Ⅱ)配合物；表 20.10 中 Fe(Ⅲ)-硫氰配合物血红色是另一个金属体系，不能套用。`

- `CHK5_SEM_EXP_20_3_04_030`
  - `explanation` before: `canonical 的目的在于比较三支试管的颜色差异；只记录加丙酮一支会丢失原溶液对照和加水条件。`
  - `explanation` after: `教材资料 的目的在于比较三支试管的颜色差异；只记录加丙酮一支会丢失原溶液对照和加水条件。`

### 20-3-05

- `CHK5_SEM_EXP_20_3_05_001`
  - `explanation` before: `canonical 规定分别向多种金属盐溶液中滴加 6 mol·L⁻¹ NH₃·H₂O 溶液。`
  - `explanation` after: `教材资料 规定分别向多种金属盐溶液中滴加 6 mol·L⁻¹ NH₃·H₂O 溶液。`

- `CHK5_SEM_EXP_20_3_05_002`
  - `explanation` before: `canonical 明确使用 6 mol·L⁻¹ NH₃·H₂O 溶液。`
  - `explanation` after: `教材资料 明确使用 6 mol·L⁻¹ NH₃·H₂O 溶液。`

- `CHK5_SEM_EXP_20_3_05_003`
  - `explanation` before: `canonical 在滴加氨水并观察后继续追问静置一段时间有什么变化，因此要记录后续颜色或沉淀变化。`
  - `explanation` after: `教材资料 在滴加氨水并观察后继续追问静置一段时间有什么变化，因此要记录后续颜色或沉淀变化。`

- `CHK5_SEM_EXP_20_3_05_004`
  - `explanation` before: `canonical 规定静置后继续向各溶液中滴加 2 mol·L⁻¹ NaOH 溶液。`
  - `explanation` after: `教材资料 规定静置后继续向各溶液中滴加 2 mol·L⁻¹ NaOH 溶液。`

- `CHK5_SEM_EXP_20_3_05_005`
  - `explanation` before: `canonical 氨合物实验对象包括 FeCl₃、CoCl₂、NiSO₄ 等金属盐溶液。`
  - `explanation` after: `教材资料 氨合物实验对象包括 FeCl₃、CoCl₂、NiSO₄ 等金属盐溶液。`

- `CHK5_SEM_EXP_20_3_05_006`
  - `explanation` before: `theory 明确 Fe²⁺ 和 Fe³⁺ 的氨合物在水溶液中不能稳定存在，并给出水解生成氢氧化亚铁或氢氧化铁的反应。`
  - `explanation` after: `相关化学原理 明确 Fe²⁺ 和 Fe³⁺ 的氨合物在水溶液中不能稳定存在，并给出水解生成氢氧化亚铁或氢氧化铁的反应。`

- `CHK5_SEM_EXP_20_3_05_007`
  - `explanation` before: `theory 说明钴盐加过量氨水生成 Co(Ⅱ) 氨合物，并在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`
  - `explanation` after: `相关化学原理 说明钴盐加过量氨水生成 Co(Ⅱ) 氨合物，并在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`

- `CHK5_SEM_EXP_20_3_05_008`
  - `explanation` before: `theory 说明镍(Ⅱ)盐加入氨水先生成氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物。`
  - `explanation` after: `相关化学原理 说明镍(Ⅱ)盐加入氨水先生成氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物。`

- `CHK5_SEM_EXP_20_3_05_009`
  - `explanation` before: `canonical 通过继续加 NaOH 比较形成氨合物的能力；若配合物较稳定，自由金属离子浓度低，氢氧化物沉淀倾向会减弱。`
  - `explanation` after: `教材资料 通过继续加 NaOH 比较形成氨合物的能力；若配合物较稳定，自由金属离子浓度低，氢氧化物沉淀倾向会减弱。`

- `CHK5_SEM_EXP_20_3_05_010`
  - `explanation` before: `canonical 最后明确要求总结这些金属离子形成氨合物的能力。`
  - `explanation` after: `教材资料 最后明确要求总结这些金属离子形成氨合物的能力。`

- `CHK5_SEM_EXP_20_3_05_011`
  - `explanation` before: `canonical 明确使用 6 mol·L⁻¹ NH₃·H₂O 处理六种金属盐溶液。`
  - `explanation` after: `教材资料 明确使用 6 mol·L⁻¹ NH₃·H₂O 处理六种金属盐溶液。`

- `CHK5_SEM_EXP_20_3_05_012`
  - `explanation` before: `canonical 把静置和继续滴加 NaOH 放在总结形成氨合物能力之前，说明这些后续现象用于比较判断。`
  - `explanation` after: `教材资料 把静置和继续滴加 NaOH 放在总结形成氨合物能力之前，说明这些后续现象用于比较判断。`

- `CHK5_SEM_EXP_20_3_05_013`
  - `explanation` before: `theory 明确 Fe²⁺、Fe³⁺ 的氨合物可由无水盐与氨气得到，但在水溶液中不可能存在，并会水解生成氢氧化物。`
  - `explanation` after: `相关化学原理 明确 Fe²⁺、Fe³⁺ 的氨合物可由无水盐与氨气得到，但在水溶液中不可能存在，并会水解生成氢氧化物。`

- `CHK5_SEM_EXP_20_3_05_014`
  - `explanation` before: `theory 明确 Co(Ⅱ) 氨合物在空气中可缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`
  - `explanation` after: `相关化学原理 明确 Co(Ⅱ) 氨合物在空气中可缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`

- `CHK5_SEM_EXP_20_3_05_015`
  - `explanation` before: `canonical 金属盐列表中包括 NiSO₄。`
  - `explanation` after: `教材金属盐列表中包括 NiSO₄。`

- `CHK5_SEM_EXP_20_3_05_017`
  - `explanation` before: `canonical 要求观察金属盐溶液加氨水、静置和加 NaOH 后的化学现象，不是钥匙遮光轮廓。`
  - `explanation` after: `教材资料 要求观察金属盐溶液加氨水、静置和加 NaOH 后的化学现象，不是钥匙遮光轮廓。`

- `CHK5_SEM_EXP_20_3_05_018`
  - `explanation` before: `canonical 要求在静置后继续加 NaOH 并观察现象，用来辅助比较金属离子形成氨合物的能力。`
  - `explanation` after: `教材资料 要求在静置后继续加 NaOH 并观察现象，用来辅助比较金属离子形成氨合物的能力。`

- `CHK5_SEM_EXP_20_3_05_019`
  - `explanation` before: `canonical 金属盐列表中同时包括 CoCl₂ 和 NiSO₄。`
  - `explanation` after: `教材金属盐列表中同时包括 CoCl₂ 和 NiSO₄。`

- `CHK5_SEM_EXP_20_3_05_020`
  - `explanation` before: `canonical 最终要求总结这些金属离子形成氨合物的能力，属于配合物形成能力比较。`
  - `explanation` after: `教材资料 最终要求总结这些金属离子形成氨合物的能力，属于配合物形成能力比较。`

- `CHK5_SEM_EXP_20_3_05_021`
  - `explanation` before: `theory 说明 Fe²⁺、Fe³⁺ 氨合物在水中不能稳定存在，而 Co(Ⅱ)、Ni(Ⅱ) 在过量氨水中可形成相应氨合物。`
  - `explanation` after: `相关化学原理 说明 Fe²⁺、Fe³⁺ 氨合物在水中不能稳定存在，而 Co(Ⅱ)、Ni(Ⅱ) 在过量氨水中可形成相应氨合物。`

- `CHK5_SEM_EXP_20_3_05_022`
  - `stem` before: `关于钴盐加入氨水后的变化，哪项有 theory 支撑？`
  - `stem` after: `关于钴盐加入氨水后的变化，哪项有 相关化学原理 支撑？`
  - `explanation` before: `theory 明确钴盐加少量氨水先生成氢氧化钴，过量氨水使沉淀溶解生成土黄色 Co(Ⅱ) 氨合物，并可在空气中氧化。`
  - `explanation` after: `相关化学原理 明确钴盐加少量氨水先生成氢氧化钴，过量氨水使沉淀溶解生成土黄色 Co(Ⅱ) 氨合物，并可在空气中氧化。`

- `CHK5_SEM_EXP_20_3_05_023`
  - `explanation` before: `canonical 在滴加氨水后要求静置并询问有什么变化；答案是短中文词，适合手机端输入。`
  - `explanation` after: `教材资料 在滴加氨水后要求静置并询问有什么变化；答案是短中文词，适合手机端输入。`

- `CHK5_SEM_EXP_20_3_05_024`
  - `options[3].text` before: `NiSO₄ 不在 canonical 实验对象中`
  - `options[3].text` after: `NiSO₄ 不在 教材资料 实验对象中`
  - `explanation` before: `theory 说明镍(Ⅱ)盐加氨水先生成绿色氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物；canonical 也列出 NiSO₄。`
  - `explanation` after: `相关化学原理 说明镍(Ⅱ)盐加氨水先生成绿色氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物；教材资料 也列出 NiSO₄。`

- `CHK5_SEM_EXP_20_3_05_025`
  - `explanation` before: `canonical 把加 NaOH 作为后续观察步骤并要求总结形成氨合物能力；是否继续沉淀可帮助判断金属离子是否被氨配位稳定。`
  - `explanation` after: `教材资料 把加 NaOH 作为后续观察步骤并要求总结形成氨合物能力；是否继续沉淀可帮助判断金属离子是否被氨配位稳定。`

- `CHK5_SEM_EXP_20_3_05_026`
  - `explanation` before: `theory 说明铁氨合物在水中不稳定，可水解生成氢氧化亚铁或氢氧化铁；答案是短中文词，避免公式输入。`
  - `explanation` after: `相关化学原理 说明铁氨合物在水中不稳定，可水解生成氢氧化亚铁或氢氧化铁；答案是短中文词，避免公式输入。`

- `CHK5_SEM_EXP_20_3_05_027`
  - `explanation` before: `theory 说明 Co(Ⅱ) 氨合物在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物，而镍氨配合物比较稳定、空气中不会被氧化。`
  - `explanation` after: `相关化学原理 说明 Co(Ⅱ) 氨合物在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物，而镍氨配合物比较稳定、空气中不会被氧化。`

- `CHK5_SEM_EXP_20_3_05_028`
  - `explanation` before: `canonical 要求总结金属离子形成氨合物的能力，Ni²⁺ 与过量氨水形成镍氨配合物正体现这一点。`
  - `explanation` after: `教材资料 要求总结金属离子形成氨合物的能力，Ni²⁺ 与过量氨水形成镍氨配合物正体现这一点。`

- `CHK5_SEM_EXP_20_3_05_030`
  - `explanation` before: `canonical 最终要求总结这些金属离子形成氨合物的能力；答案为短中文词。`
  - `explanation` after: `教材资料 最终要求总结这些金属离子形成氨合物的能力；答案为短中文词。`

### 20-3-06

- `CHK5_SEM_EXP_20_3_06_001`
  - `explanation` before: `canonical 给出 KI、CCl₄ 和 FeCl₃ 的对照体系；theory 明确 Fe³⁺ 能把 I⁻ 氧化为 I₂，CCl₄ 层用于观察碘。`
  - `explanation` after: `教材资料 给出 KI、CCl₄ 和 FeCl₃ 的对照体系；相关化学原理 明确 Fe³⁺ 能把 I⁻ 氧化为 I₂，CCl₄ 层用于观察碘。`

- `CHK5_SEM_EXP_20_3_06_002`
  - `explanation` before: `canonical 要求比较先加 NaF 再加 FeCl₃ 的现象；table 支持 F⁻ 可与 Fe³⁺ 形成配合物。`
  - `explanation` after: `教材资料 要求比较先加 NaF 再加 FeCl₃ 的现象；table 支持 F⁻ 可与 Fe³⁺ 形成配合物。`

- `CHK5_SEM_EXP_20_3_06_003`
  - `explanation` before: `F⁻ 配合 Fe³⁺ 会降低游离 Fe³⁺ 的氧化干扰；canonical 要求比较先加 NaF 时现象的不同。`
  - `explanation` after: `F⁻ 配合 Fe³⁺ 会降低游离 Fe³⁺ 的氧化干扰；教材资料 要求比较先加 NaF 时现象的不同。`

- `CHK5_SEM_EXP_20_3_06_004`
  - `explanation` before: `canonical 把 KI 与 CCl₄ 混合后再加 FeCl₃；结合 Fe³⁺ 氧化 I⁻ 生成 I₂，可知 CCl₄ 用于有机层显色观察。`
  - `explanation` after: `教材资料 把 KI 与 CCl₄ 混合后再加 FeCl₃；结合 Fe³⁺ 氧化 I⁻ 生成 I₂，可知 CCl₄ 用于有机层显色观察。`

- `CHK5_SEM_EXP_20_3_06_005`
  - `explanation` before: `canonical 要求比较有 EDTA 与无 EDTA 时 Fe(Ⅱ) 溶液和 AgNO₃ 的反应；思考题把该比较指向利用配合物性质回收银。`
  - `explanation` after: `教材资料 要求比较有 EDTA 与无 EDTA 时 Fe(Ⅱ) 溶液和 AgNO₃ 的反应；思考题把该比较指向利用配合物性质回收银。`

- `CHK5_SEM_EXP_20_3_06_007`
  - `explanation` before: `canonical 小节标题即为“配合物的形成对氧化还原性的影响”，两个对比体系都服务于该结论。`
  - `explanation` after: `教材小节标题即为“配合物的形成对氧化还原性的影响”，两个对比体系都服务于该结论。`

- `CHK5_SEM_EXP_20_3_06_008`
  - `explanation` before: `canonical 依次安排 KI/CCl₄/FeCl₃ 与 Fe(Ⅱ)/AgNO₃/EDTA 两组对比。`
  - `explanation` after: `教材资料 依次安排 KI/CCl₄/FeCl₃ 与 Fe(Ⅱ)/AgNO₃/EDTA 两组对比。`

- `CHK5_SEM_EXP_20_3_06_011`
  - `explanation` before: `canonical 给出该体系；theory 说明 Fe³⁺ 可氧化 I⁻ 为 I₂。`
  - `explanation` after: `教材资料 给出该体系；相关化学原理 说明 Fe³⁺ 可氧化 I⁻ 为 I₂。`

- `CHK5_SEM_EXP_20_3_06_012`
  - `explanation` before: `canonical 要求比较先加 NaF 的差异；table 支持 F⁻ 与 Fe³⁺ 配合。`
  - `explanation` after: `教材资料 要求比较先加 NaF 的差异；table 支持 F⁻ 与 Fe³⁺ 配合。`

- `CHK5_SEM_EXP_20_3_06_014`
  - `explanation` before: `canonical 要求比较有无 EDTA 下 Fe(Ⅱ) 与 AgNO₃ 的反应；思考题将该现象联系到用配合物性质回收银。`
  - `explanation` after: `教材资料 要求比较有无 EDTA 下 Fe(Ⅱ) 与 AgNO₃ 的反应；思考题将该现象联系到用配合物性质回收银。`

- `CHK5_SEM_EXP_20_3_06_017`
  - `explanation` before: `canonical 明确 Fe(Ⅱ) 溶液与 AgNO₃ 溶液反应，AgNO₃ 提供 Ag⁺。`
  - `explanation` after: `教材资料 明确 Fe(Ⅱ) 溶液与 AgNO₃ 溶液反应，AgNO₃ 提供 Ag⁺。`

- `CHK5_SEM_EXP_20_3_06_020`
  - `explanation` before: `canonical 小节标题和两组对照均指向该主题。`
  - `explanation` after: `教材小节标题和两组对照均指向该主题。`

- `CHK5_SEM_EXP_20_3_06_021`
  - `explanation` before: `theory 明确 Fe³⁺ 可以氧化 I⁻ 生成 I₂；canonical 用 CCl₄ 层观察该变化。`
  - `explanation` after: `相关化学原理 明确 Fe³⁺ 可以氧化 I⁻ 生成 I₂；教材资料 用 CCl₄ 层观察该变化。`

- `CHK5_SEM_EXP_20_3_06_022`
  - `explanation` before: `canonical 要求先加少量 NaF 后再加 FeCl₃ 并比较现象；table 支持 F⁻ 可配合 Fe³⁺。`
  - `explanation` after: `教材资料 要求先加少量 NaF 后再加 FeCl₃ 并比较现象；table 支持 F⁻ 可配合 Fe³⁺。`

- `CHK5_SEM_EXP_20_3_06_023`
  - `explanation` before: `canonical 把 CCl₄ 放在 KI/FeCl₃ 观察体系中；其作用是有机层萃取碘，方便比较颜色。`
  - `explanation` after: `教材资料 把 CCl₄ 放在 KI/FeCl₃ 观察体系中；其作用是有机层萃取碘，方便比较颜色。`

- `CHK5_SEM_EXP_20_3_06_024`
  - `explanation` before: `canonical 明确比较 Fe(Ⅱ) 溶液在有无 EDTA 下与 AgNO₃ 溶液的反应。`
  - `explanation` after: `教材资料 明确比较 Fe(Ⅱ) 溶液在有无 EDTA 下与 AgNO₃ 溶液的反应。`

- `CHK5_SEM_EXP_20_3_06_028`
  - `explanation` before: `canonical 小节标题即“配合物的形成对氧化还原性的影响”。`
  - `explanation` after: `教材小节标题即“配合物的形成对氧化还原性的影响”。`

### 20-3-07

- `CHK5_SEM_EXP_20_3_07_001`
  - `explanation` before: `canonical 明确在 Cr₂(SO₄)₃ 溶液中加入少量 Na₂C₂O₄ 固体。`
  - `explanation` after: `教材资料 明确在 Cr₂(SO₄)₃ 溶液中加入少量 Na₂C₂O₄ 固体。`

- `CHK5_SEM_EXP_20_3_07_002`
  - `explanation` before: `canonical 要求在加入 Na₂C₂O₄ 后逐滴加入 2 mol·L⁻¹ NaOH，观察有无沉淀生成。`
  - `explanation` after: `教材资料 要求在加入 Na₂C₂O₄ 后逐滴加入 2 mol·L⁻¹ NaOH，观察有无沉淀生成。`

- `CHK5_SEM_EXP_20_3_07_003`
  - `explanation` before: `theory 与表格均说明 Fe³⁺ 与硫氰根形成血红色配合物。`
  - `explanation` after: `相关化学原理 与表格均说明 Fe³⁺ 与硫氰根形成血红色配合物。`

- `CHK5_SEM_EXP_20_3_07_004`
  - `explanation` before: `canonical 把 FeCl₃ + KSCN 显色后再加 Na₂C₂O₄ 放在“配合物稳定性与配体的关系”小节中。`
  - `explanation` after: `教材资料 把 FeCl₃ + KSCN 显色后再加 Na₂C₂O₄ 放在“配合物稳定性与配体的关系”小节中。`

- `CHK5_SEM_EXP_20_3_07_005`
  - `explanation` before: `canonical 明确 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`
  - `explanation` after: `教材资料 明确 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`

- `CHK5_SEM_EXP_20_3_07_006`
  - `explanation` before: `canonical 所在小节比较配合物稳定性与配体的关系；乙二胺是该步骤后加入的配体。`
  - `explanation` after: `教材资料 所在小节比较配合物稳定性与配体的关系；乙二胺是该步骤后加入的配体。`

- `CHK5_SEM_EXP_20_3_07_008`
  - `explanation` before: `theory 说明硫氰根与 Fe³⁺ 可形成血红色配合物。`
  - `explanation` after: `相关化学原理 说明硫氰根与 Fe³⁺ 可形成血红色配合物。`

- `CHK5_SEM_EXP_20_3_07_010`
  - `explanation` before: `A、B、C 都属于 canonical 的配体稳定性实验；D 是后续金属离子鉴定实验，不属于本 packet。`
  - `explanation` after: `A、B、C 都属于 教材资料 的配体稳定性实验；D 是后续金属离子鉴定实验，不属于本实验。`

- `CHK5_SEM_EXP_20_3_07_011`
  - `explanation` before: `canonical 明确在 NiSO₄ 加过量氨水后逐滴加入乙二胺溶液继续观察。`
  - `explanation` after: `教材资料 明确在 NiSO₄ 加过量氨水后逐滴加入乙二胺溶液继续观察。`

- `CHK5_SEM_EXP_20_3_07_014`
  - `explanation` before: `canonical 要求 FeCl₃ 加 KSCN 后再加 Na₂C₂O₄ 并观察溶液颜色变化。`
  - `explanation` after: `教材资料 要求 FeCl₃ 加 KSCN 后再加 Na₂C₂O₄ 并观察溶液颜色变化。`

- `CHK5_SEM_EXP_20_3_07_015`
  - `explanation` before: `canonical 明确该操作顺序。`
  - `explanation` after: `教材资料 明确该操作顺序。`

- `CHK5_SEM_EXP_20_3_07_016`
  - `explanation` before: `canonical 把乙二胺作为 NiSO₄ 过量氨水后的追加试剂，服务于“配合物稳定性与配体的关系”。`
  - `explanation` after: `教材资料 把乙二胺作为 NiSO₄ 过量氨水后的追加试剂，服务于“配合物稳定性与配体的关系”。`

- `CHK5_SEM_EXP_20_3_07_017`
  - `explanation` before: `canonical 三个子步骤分别改变配体或后加试剂，并观察沉淀或颜色变化。`
  - `explanation` after: `教材资料 三个子步骤分别改变配体或后加试剂，并观察沉淀或颜色变化。`

- `CHK5_SEM_EXP_20_3_07_020`
  - `explanation` before: `canonical 本 packet 的小节主题是配合物稳定性与配体的关系，而不是金属离子水解作用。`
  - `explanation` after: `教材资料 本实验 的小节主题是配合物稳定性与配体的关系，而不是金属离子水解作用。`

- `CHK5_SEM_EXP_20_3_07_022`
  - `explanation` before: `theory 明确 Fe³⁺ 与硫氰根生成血红色配合物。`
  - `explanation` after: `相关化学原理 明确 Fe³⁺ 与硫氰根生成血红色配合物。`

- `CHK5_SEM_EXP_20_3_07_023`
  - `explanation` before: `canonical 明确在 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`
  - `explanation` after: `教材资料 明确在 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`

- `CHK5_SEM_EXP_20_3_07_024`
  - `explanation` before: `canonical 明确该步骤是逐滴加入 NaOH，观察有无沉淀生成。`
  - `explanation` after: `教材资料 明确该步骤是逐滴加入 NaOH，观察有无沉淀生成。`

- `CHK5_SEM_EXP_20_3_07_025`
  - `explanation` before: `KSCN 提供硫氰根，theory 说明硫氰根可与 Fe³⁺ 形成血红色配合物。`
  - `explanation` after: `KSCN 提供硫氰根，相关化学原理 说明硫氰根可与 Fe³⁺ 形成血红色配合物。`

- `CHK5_SEM_EXP_20_3_07_027`
  - `stem` before: `NiSO₄ 加过量氨水后，canonical 要求再逐滴加入____溶液。`
  - `stem` after: `NiSO₄ 加过量氨水后，教材资料 要求再逐滴加入____溶液。`
  - `explanation` before: `canonical 明确后续逐滴加入 1% 乙二胺溶液，再观察现象。`
  - `explanation` after: `教材资料 明确后续逐滴加入 1% 乙二胺溶液，再观察现象。`

- `CHK5_SEM_EXP_20_3_07_029`
  - `explanation` before: `canonical 的镍体系从 NiSO₄ 溶液开始，NiSO₄ 提供 Ni²⁺。`
  - `explanation` after: `教材资料 的镍体系从 NiSO₄ 溶液开始，NiSO₄ 提供 Ni²⁺。`

- `CHK5_SEM_EXP_20_3_07_030`
  - `explanation` before: `canonical 明确加入少量 Na₂C₂O₄ 后观察溶液颜色变化。`
  - `explanation` after: `教材资料 明确加入少量 Na₂C₂O₄ 后观察溶液颜色变化。`

### 20-3-08

- `CHK5_SEM_EXP_20_3_08_001`
  - `explanation` before: `canonical 明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
  - `explanation` after: `教材资料 明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`

- `CHK5_SEM_EXP_20_3_08_002`
  - `explanation` before: `theory 明确硫氰根离子与 Fe³⁺ 可生成血红色配合物，可用于鉴定 Fe³⁺。`
  - `explanation` after: `相关化学原理 明确硫氰根离子与 Fe³⁺ 可生成血红色配合物，可用于鉴定 Fe³⁺。`

- `CHK5_SEM_EXP_20_3_08_004`
  - `explanation` before: `theory 明确 Fe²⁺ 与铁氰化物体系生成滕氏蓝的蓝色沉淀，是鉴定 Fe²⁺ 的灵敏反应。`
  - `explanation` after: `相关化学原理 明确 Fe²⁺ 与铁氰化物体系生成滕氏蓝的蓝色沉淀，是鉴定 Fe²⁺ 的灵敏反应。`

- `CHK5_SEM_EXP_20_3_08_006`
  - `explanation` before: `canonical 明确分别进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
  - `explanation` after: `教材资料 明确分别进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`

- `CHK5_SEM_EXP_20_3_08_011`
  - `explanation` before: `canonical 明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
  - `explanation` after: `教材资料 明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`

- `CHK5_SEM_EXP_20_3_08_013`
  - `explanation` before: `theory 明确该配合物为血红色，可用于 Fe³⁺ 鉴定。`
  - `explanation` after: `相关化学原理 明确该配合物为血红色，可用于 Fe³⁺ 鉴定。`

- `CHK5_SEM_EXP_20_3_08_017`
  - `explanation` before: `canonical 要求鉴定 Fe(Ⅱ) 和 Fe(Ⅲ)，因此记录必须体现价态和对应阳性现象。`
  - `explanation` after: `教材资料 要求鉴定 Fe(Ⅱ) 和 Fe(Ⅲ)，因此记录必须体现价态和对应阳性现象。`

- `CHK5_SEM_EXP_20_3_08_021`
  - `explanation` before: `canonical 明确进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
  - `explanation` after: `教材资料 明确进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`

- `CHK5_SEM_EXP_20_3_08_024`
  - `explanation` before: `theory 明确 Fe²⁺ 的铁氰化物鉴定反应生成滕氏蓝的蓝色沉淀。`
  - `explanation` after: `相关化学原理 明确 Fe²⁺ 的铁氰化物鉴定反应生成滕氏蓝的蓝色沉淀。`

- `CHK5_SEM_EXP_20_3_08_027`
  - `explanation` before: `canonical 要求分别鉴定铁(Ⅱ)和铁(Ⅲ)，supporting theory 也给出不同阳性反应。`
  - `explanation` after: `教材资料 要求分别鉴定铁(Ⅱ)和铁(Ⅲ)，相关化学原理 也给出不同阳性反应。`

### 20-3-09

- `CHK5_SEM_EXP_20_3_09_002`
  - `explanation` before: `canonical 步骤写明加入戊醇或丙酮后，再滴加饱和 KSCN 溶液。`
  - `explanation` after: `实验步骤写明加入戊醇或丙酮后，再滴加饱和 KSCN 溶液。`

- `CHK5_SEM_EXP_20_3_09_011`
  - `explanation` before: `这正是 canonical 给出的钴(Ⅱ)鉴定操作。`
  - `explanation` after: `这正是 教材资料 给出的钴(Ⅱ)鉴定操作。`

- `CHK5_SEM_EXP_20_3_09_015`
  - `explanation` before: `canonical 小节标题和操作均为钴(Ⅱ)的鉴定；镍(Ⅱ)有另一套丁二酮肟鉴定操作。`
  - `explanation` after: `教材小节标题和操作均为钴(Ⅱ)的鉴定；镍(Ⅱ)有另一套丁二酮肟鉴定操作。`

- `CHK5_SEM_EXP_20_3_09_018`
  - `explanation` before: `canonical 小节标题即为配合物应用中的金属离子鉴定，钴(Ⅱ)鉴定是其中一项。`
  - `explanation` after: `教材小节标题即为配合物应用中的金属离子鉴定，钴(Ⅱ)鉴定是其中一项。`

- `CHK5_SEM_EXP_20_3_09_022`
  - `explanation` before: `canonical 步骤明确写出戊醇或丙酮。`
  - `explanation` after: `实验步骤明确写出戊醇或丙酮。`

- `CHK5_SEM_EXP_20_3_09_028`
  - `explanation` before: `canonical 步骤把戊醇或丙酮放在滴加饱和 KSCN 之前；理论上有机溶剂可提高硫氰合钴蓝色显色的可观察性。`
  - `explanation` after: `实验步骤把戊醇或丙酮放在滴加饱和 KSCN 之前；理论上有机溶剂可提高硫氰合钴蓝色显色的可观察性。`

### 20-3-10

- `CHK5_SEM_EXP_20_3_10_001`
  - `explanation` before: `NiSO₄ 溶液提供 Ni²⁺，canonical 步骤要求先用氨水调至弱碱性。`
  - `explanation` after: `NiSO₄ 溶液提供 Ni²⁺，实验步骤要求先用氨水调至弱碱性。`

- `CHK5_SEM_EXP_20_3_10_002`
  - `explanation` before: `canonical 步骤写明加入氨水至呈弱碱性。`
  - `explanation` after: `实验步骤写明加入氨水至呈弱碱性。`

- `CHK5_SEM_EXP_20_3_10_004`
  - `explanation` before: `canonical 步骤写明加入 1 滴 1% 丁二酮肟溶液。`
  - `explanation` after: `实验步骤写明加入 1 滴 1% 丁二酮肟溶液。`

- `CHK5_SEM_EXP_20_3_10_007`
  - `explanation` before: `canonical 文字说明 H₂dmg 表示丁二酮肟。`
  - `explanation` after: `教材资料 文字说明 H₂dmg 表示丁二酮肟。`

- `CHK5_SEM_EXP_20_3_10_009`
  - `explanation` before: `canonical 反应式显示 NH₃ 与酸性氢结合形成 NH₄⁺。`
  - `explanation` after: `教材反应式显示 NH₃ 与酸性氢结合形成 NH₄⁺。`

- `CHK5_SEM_EXP_20_3_10_011`
  - `explanation` before: `canonical 步骤明确要求先用氨水调至弱碱性，再加入丁二酮肟。`
  - `explanation` after: `实验步骤明确要求先用氨水调至弱碱性，再加入丁二酮肟。`

- `CHK5_SEM_EXP_20_3_10_013`
  - `explanation` before: `canonical 文字说明 H₂dmg 表示丁二酮肟。`
  - `explanation` after: `教材资料 文字说明 H₂dmg 表示丁二酮肟。`

- `CHK5_SEM_EXP_20_3_10_015`
  - `explanation` before: `canonical 步骤要求加入氨水至弱碱性后再加入丁二酮肟。`
  - `explanation` after: `实验步骤要求加入氨水至弱碱性后再加入丁二酮肟。`

- `CHK5_SEM_EXP_20_3_10_024`
  - `explanation` before: `canonical 步骤要求加入 1 滴 1% 丁二酮肟溶液。`
  - `explanation` after: `实验步骤要求加入 1 滴 1% 丁二酮肟溶液。`

- `CHK5_SEM_EXP_20_3_10_027`
  - `explanation` before: `canonical 文字说明 H₂dmg 表示丁二酮肟。`
  - `explanation` after: `教材资料 文字说明 H₂dmg 表示丁二酮肟。`

- `CHK5_SEM_EXP_20_3_10_028`
  - `explanation` before: `canonical 反应式说明 Ni²⁺、丁二酮肟和氨参与形成丁二酮肟镍沉淀。`
  - `explanation` after: `教材反应式说明 Ni²⁺、丁二酮肟和氨参与形成丁二酮肟镍沉淀。`

### 20-3-11

- `CHK5_SEM_EXP_20_3_11_001`
  - `explanation` before: `canonical 步骤要求先加入过量 6 mol·L⁻¹ NaOH 溶液。`
  - `explanation` after: `实验步骤要求先加入过量 6 mol·L⁻¹ NaOH 溶液。`

- `CHK5_SEM_EXP_20_3_11_002`
  - `explanation` before: `canonical 步骤指定随后加入 3% H₂O₂ 溶液。`
  - `explanation` after: `实验步骤指定随后加入 3% H₂O₂ 溶液。`

- `CHK5_SEM_EXP_20_3_11_004`
  - `explanation` before: `canonical 步骤指定用稀 H₂SO₄ 酸化。`
  - `explanation` after: `实验步骤指定用稀 H₂SO₄ 酸化。`

- `CHK5_SEM_EXP_20_3_11_005`
  - `explanation` before: `canonical 步骤要求加入少量乙醚或戊醇。`
  - `explanation` after: `实验步骤要求加入少量乙醚或戊醇。`

- `CHK5_SEM_EXP_20_3_11_011`
  - `explanation` before: `canonical 步骤直接列出 Cr₂(SO₄)₃ 溶液。`
  - `explanation` after: `实验步骤直接列出 Cr₂(SO₄)₃ 溶液。`

- `CHK5_SEM_EXP_20_3_11_012`
  - `explanation` before: `canonical 步骤明确给出这一顺序。`
  - `explanation` after: `实验步骤明确给出这一顺序。`

- `CHK5_SEM_EXP_20_3_11_014`
  - `explanation` before: `canonical 步骤直接给出用稀 H₂SO₄ 酸化。`
  - `explanation` after: `实验步骤直接给出用稀 H₂SO₄ 酸化。`

- `CHK5_SEM_EXP_20_3_11_026`
  - `explanation` before: `canonical 步骤写明加入少量乙醚或戊醇。`
  - `explanation` after: `实验步骤写明加入少量乙醚或戊醇。`

### 20-3-12

- `CHK5_SEM_EXP_20_3_12_001`
  - `explanation` before: `canonical 步骤要求先在 TiOSO₄ 溶液中滴加 3% H₂O₂ 溶液。`
  - `explanation` after: `实验步骤要求先在 TiOSO₄ 溶液中滴加 3% H₂O₂ 溶液。`

- `CHK5_SEM_EXP_20_3_12_004`
  - `explanation` before: `canonical 步骤要求再加入少量 6 mol·L⁻¹ NH₃·H₂O。`
  - `explanation` after: `实验步骤要求再加入少量 6 mol·L⁻¹ NH₃·H₂O。`

- `CHK5_SEM_EXP_20_3_12_005`
  - `explanation` before: `canonical 反应式标明再加入少量 NH₃·H₂O 后生成黄色沉淀。`
  - `explanation` after: `教材反应式标明再加入少量 NH₃·H₂O 后生成黄色沉淀。`

- `CHK5_SEM_EXP_20_3_12_014`
  - `explanation` before: `canonical 小节明确列为钛(Ⅳ)的鉴定。`
  - `explanation` after: `教材小节明确列为钛(Ⅳ)的鉴定。`

### 20-3-13

- `CHK5_SEM_EXP_20_3_13_029`
  - `explanation` before: `教材要求先用 H₂SO₄ 酸化 NH₄VO₃，再加入 H₂O₂；跳过酸化不符合 canonical 流程。`
  - `explanation` after: `教材要求先用 H₂SO₄ 酸化 NH₄VO₃，再加入 H₂O₂；跳过酸化不符合 教材资料 流程。`

## Final Remaining Hits

| Category | Initial hits | Remaining hits |
|---|---:|---:|
| `internal_trace` | `275` | `0` |
| `ascii_digit_formula` | `0` | `0` |
| `ascii_charge_ion` | `29` | `0` |
| `caret_latex_markdown` | `0` | `0` |

Note: ASCII Roman valence markers such as `(III)` / `(IV)` were counted under `ascii_charge_ion` because the task grouped ion, charge, and valence normalization together.

## Invariant Confirmation

- `question_id`: unchanged.
- `primary_point_keys` / `secondary_point_keys`: unchanged.
- `source_audit.canonical_chunk_ids` / `source_audit.supporting_theory_chunk_ids`: unchanged.
- Evidence ids in package metadata and source audits: unchanged.
- File names and release final JSON: unchanged by this polish pass.

## Validation Summary

- Student-visible internal review/rebuild traces: `0`.
- Student-visible ASCII digit-subscript formulas: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax: `0`.
- JSON parse: passed for all 17 rebuilt packages.
- Each packet question count: passed, all 17 rebuilt packages contain `30` questions.
- Single-choice answer/options/option_links: passed.
- RAG evidence id existence: passed; all cited evidence ids were found in `E:\chemistry-rag\data\rag_ready\chunks`.

## Final Integrity Validation Run

- Validation command scope: all 17 `chunk_5` rebuilt JSON files plus RAG JSONL id lookup under `E:\chemistry-rag\data\rag_ready\chunks`.
- Total questions: `510`.
- Type totals: `321` single choice, `154` true/false, `35` fill blank.
- Unique cited evidence ids checked: `57`; missing ids: `0`.
- Validation errors: `0`.

## Readability Follow-Up Fix Log

- Purpose: second pass after manual spot-check to remove awkward spacing left by term replacement and to rephrase remaining student-visible “option diagnostic” wording.
- Fields changed in this follow-up: `239`.
- `20-2-08`: `CHK5_SEM_EXP_20_2_08_003`, `CHK5_SEM_EXP_20_2_08_005`, `CHK5_SEM_EXP_20_2_08_006`, `CHK5_SEM_EXP_20_2_08_008`, `CHK5_SEM_EXP_20_2_08_009`, `CHK5_SEM_EXP_20_2_08_011`, `CHK5_SEM_EXP_20_2_08_012`, `CHK5_SEM_EXP_20_2_08_014`, `CHK5_SEM_EXP_20_2_08_015`, `CHK5_SEM_EXP_20_2_08_016`, `CHK5_SEM_EXP_20_2_08_018`, `CHK5_SEM_EXP_20_2_08_019`, `CHK5_SEM_EXP_20_2_08_020`, `CHK5_SEM_EXP_20_2_08_022`, `CHK5_SEM_EXP_20_2_08_025`, `CHK5_SEM_EXP_20_2_08_027`
- `20-2-09`: `CHK5_SEM_EXP_20_2_09_003`, `CHK5_SEM_EXP_20_2_09_004`, `CHK5_SEM_EXP_20_2_09_005`, `CHK5_SEM_EXP_20_2_09_006`, `CHK5_SEM_EXP_20_2_09_007`, `CHK5_SEM_EXP_20_2_09_008`, `CHK5_SEM_EXP_20_2_09_009`, `CHK5_SEM_EXP_20_2_09_010`, `CHK5_SEM_EXP_20_2_09_011`, `CHK5_SEM_EXP_20_2_09_012`, `CHK5_SEM_EXP_20_2_09_013`, `CHK5_SEM_EXP_20_2_09_014`, `CHK5_SEM_EXP_20_2_09_016`, `CHK5_SEM_EXP_20_2_09_018`, `CHK5_SEM_EXP_20_2_09_019`, `CHK5_SEM_EXP_20_2_09_020`, `CHK5_SEM_EXP_20_2_09_021`, `CHK5_SEM_EXP_20_2_09_024`, `CHK5_SEM_EXP_20_2_09_025`, `CHK5_SEM_EXP_20_2_09_026`, `CHK5_SEM_EXP_20_2_09_028`, `CHK5_SEM_EXP_20_2_09_029`
- `20-2-10`: `CHK5_SEM_EXP_20_2_10_001`, `CHK5_SEM_EXP_20_2_10_003`, `CHK5_SEM_EXP_20_2_10_004`, `CHK5_SEM_EXP_20_2_10_005`, `CHK5_SEM_EXP_20_2_10_006`, `CHK5_SEM_EXP_20_2_10_007`, `CHK5_SEM_EXP_20_2_10_009`, `CHK5_SEM_EXP_20_2_10_011`, `CHK5_SEM_EXP_20_2_10_012`, `CHK5_SEM_EXP_20_2_10_013`, `CHK5_SEM_EXP_20_2_10_014`, `CHK5_SEM_EXP_20_2_10_015`, `CHK5_SEM_EXP_20_2_10_016`, `CHK5_SEM_EXP_20_2_10_018`, `CHK5_SEM_EXP_20_2_10_019`, `CHK5_SEM_EXP_20_2_10_021`, `CHK5_SEM_EXP_20_2_10_022`, `CHK5_SEM_EXP_20_2_10_023`, `CHK5_SEM_EXP_20_2_10_024`, `CHK5_SEM_EXP_20_2_10_025`, `CHK5_SEM_EXP_20_2_10_026`, `CHK5_SEM_EXP_20_2_10_027`, `CHK5_SEM_EXP_20_2_10_030`
- `20-3-01`: `CHK5_SEM_EXP_20_3_01_002`, `CHK5_SEM_EXP_20_3_01_008`, `CHK5_SEM_EXP_20_3_01_010`, `CHK5_SEM_EXP_20_3_01_011`, `CHK5_SEM_EXP_20_3_01_015`, `CHK5_SEM_EXP_20_3_01_018`, `CHK5_SEM_EXP_20_3_01_020`, `CHK5_SEM_EXP_20_3_01_021`, `CHK5_SEM_EXP_20_3_01_022`, `CHK5_SEM_EXP_20_3_01_025`, `CHK5_SEM_EXP_20_3_01_026`, `CHK5_SEM_EXP_20_3_01_027`
- `20-3-02`: `CHK5_SEM_EXP_20_3_02_002`, `CHK5_SEM_EXP_20_3_02_003`, `CHK5_SEM_EXP_20_3_02_004`, `CHK5_SEM_EXP_20_3_02_007`, `CHK5_SEM_EXP_20_3_02_010`, `CHK5_SEM_EXP_20_3_02_011`, `CHK5_SEM_EXP_20_3_02_012`, `CHK5_SEM_EXP_20_3_02_014`, `CHK5_SEM_EXP_20_3_02_015`, `CHK5_SEM_EXP_20_3_02_017`, `CHK5_SEM_EXP_20_3_02_018`, `CHK5_SEM_EXP_20_3_02_021`, `CHK5_SEM_EXP_20_3_02_022`, `CHK5_SEM_EXP_20_3_02_024`, `CHK5_SEM_EXP_20_3_02_026`, `CHK5_SEM_EXP_20_3_02_030`
- `20-3-03`: `CHK5_SEM_EXP_20_3_03_002`, `CHK5_SEM_EXP_20_3_03_003`, `CHK5_SEM_EXP_20_3_03_004`, `CHK5_SEM_EXP_20_3_03_012`, `CHK5_SEM_EXP_20_3_03_013`, `CHK5_SEM_EXP_20_3_03_014`, `CHK5_SEM_EXP_20_3_03_020`, `CHK5_SEM_EXP_20_3_03_021`, `CHK5_SEM_EXP_20_3_03_024`, `CHK5_SEM_EXP_20_3_03_028`
- `20-3-04`: `CHK5_SEM_EXP_20_3_04_001`, `CHK5_SEM_EXP_20_3_04_002`, `CHK5_SEM_EXP_20_3_04_007`, `CHK5_SEM_EXP_20_3_04_011`, `CHK5_SEM_EXP_20_3_04_012`, `CHK5_SEM_EXP_20_3_04_019`, `CHK5_SEM_EXP_20_3_04_021`, `CHK5_SEM_EXP_20_3_04_024`, `CHK5_SEM_EXP_20_3_04_026`, `CHK5_SEM_EXP_20_3_04_028`, `CHK5_SEM_EXP_20_3_04_030`
- `20-3-05`: `CHK5_SEM_EXP_20_3_05_001`, `CHK5_SEM_EXP_20_3_05_002`, `CHK5_SEM_EXP_20_3_05_003`, `CHK5_SEM_EXP_20_3_05_004`, `CHK5_SEM_EXP_20_3_05_005`, `CHK5_SEM_EXP_20_3_05_006`, `CHK5_SEM_EXP_20_3_05_007`, `CHK5_SEM_EXP_20_3_05_008`, `CHK5_SEM_EXP_20_3_05_009`, `CHK5_SEM_EXP_20_3_05_010`, `CHK5_SEM_EXP_20_3_05_011`, `CHK5_SEM_EXP_20_3_05_012`, `CHK5_SEM_EXP_20_3_05_013`, `CHK5_SEM_EXP_20_3_05_014`, `CHK5_SEM_EXP_20_3_05_017`, `CHK5_SEM_EXP_20_3_05_018`, `CHK5_SEM_EXP_20_3_05_020`, `CHK5_SEM_EXP_20_3_05_021`, `CHK5_SEM_EXP_20_3_05_022`, `CHK5_SEM_EXP_20_3_05_023`, `CHK5_SEM_EXP_20_3_05_024`, `CHK5_SEM_EXP_20_3_05_025`, `CHK5_SEM_EXP_20_3_05_026`, `CHK5_SEM_EXP_20_3_05_027`, `CHK5_SEM_EXP_20_3_05_028`, `CHK5_SEM_EXP_20_3_05_030`
- `20-3-06`: `CHK5_SEM_EXP_20_3_06_001`, `CHK5_SEM_EXP_20_3_06_002`, `CHK5_SEM_EXP_20_3_06_003`, `CHK5_SEM_EXP_20_3_06_004`, `CHK5_SEM_EXP_20_3_06_005`, `CHK5_SEM_EXP_20_3_06_008`, `CHK5_SEM_EXP_20_3_06_011`, `CHK5_SEM_EXP_20_3_06_012`, `CHK5_SEM_EXP_20_3_06_014`, `CHK5_SEM_EXP_20_3_06_017`, `CHK5_SEM_EXP_20_3_06_021`, `CHK5_SEM_EXP_20_3_06_022`, `CHK5_SEM_EXP_20_3_06_023`, `CHK5_SEM_EXP_20_3_06_024`
- `20-3-07`: `CHK5_SEM_EXP_20_3_07_001`, `CHK5_SEM_EXP_20_3_07_002`, `CHK5_SEM_EXP_20_3_07_003`, `CHK5_SEM_EXP_20_3_07_004`, `CHK5_SEM_EXP_20_3_07_005`, `CHK5_SEM_EXP_20_3_07_006`, `CHK5_SEM_EXP_20_3_07_008`, `CHK5_SEM_EXP_20_3_07_010`, `CHK5_SEM_EXP_20_3_07_011`, `CHK5_SEM_EXP_20_3_07_014`, `CHK5_SEM_EXP_20_3_07_015`, `CHK5_SEM_EXP_20_3_07_016`, `CHK5_SEM_EXP_20_3_07_017`, `CHK5_SEM_EXP_20_3_07_020`, `CHK5_SEM_EXP_20_3_07_022`, `CHK5_SEM_EXP_20_3_07_023`, `CHK5_SEM_EXP_20_3_07_024`, `CHK5_SEM_EXP_20_3_07_025`, `CHK5_SEM_EXP_20_3_07_027`, `CHK5_SEM_EXP_20_3_07_029`, `CHK5_SEM_EXP_20_3_07_030`
- `20-3-08`: `CHK5_SEM_EXP_20_3_08_001`, `CHK5_SEM_EXP_20_3_08_002`, `CHK5_SEM_EXP_20_3_08_004`, `CHK5_SEM_EXP_20_3_08_006`, `CHK5_SEM_EXP_20_3_08_011`, `CHK5_SEM_EXP_20_3_08_013`, `CHK5_SEM_EXP_20_3_08_017`, `CHK5_SEM_EXP_20_3_08_021`, `CHK5_SEM_EXP_20_3_08_024`, `CHK5_SEM_EXP_20_3_08_027`
- `20-3-09`: `CHK5_SEM_EXP_20_3_09_011`
- `20-3-10`: `CHK5_SEM_EXP_20_3_10_007`, `CHK5_SEM_EXP_20_3_10_013`, `CHK5_SEM_EXP_20_3_10_027`
- `20-3-13`: `CHK5_SEM_EXP_20_3_13_029`

### Follow-Up 20-2-08

- `CHK5_SEM_EXP_20_2_08_003` `stem` before: `本实验 的核心考点应归入哪类实验任务？`
- `CHK5_SEM_EXP_20_2_08_003` `stem` after: `本实验的核心考点应归入哪类实验任务？`
- `CHK5_SEM_EXP_20_2_08_005` `stem` before: `下列哪项属于本实验 中不应被当作“铬(Ⅲ)盐水解”直接证据的相邻实验内容？`
- `CHK5_SEM_EXP_20_2_08_005` `stem` after: `下列哪项属于本实验中不应被当作“铬(Ⅲ)盐水解”直接证据的相邻实验内容？`
- `CHK5_SEM_EXP_20_2_08_006` `stem` before: `与《20-2-08 铬(Ⅲ)盐的水解》相比，氢氧化物酸碱性实验 更适合支撑哪类题目？`
- `CHK5_SEM_EXP_20_2_08_006` `stem` after: `与《20-2-08 铬(Ⅲ)盐的水解》相比，氢氧化物酸碱性实验更适合支撑哪类题目？`
- `CHK5_SEM_EXP_20_2_08_006` `explanation` before: `氢氧化物酸碱性实验 的标题是“氢氧化物的酸碱性”，内容是多种金属盐溶液滴加 NaOH 后观察并检验沉淀酸碱性；它只能作为相邻背景，不是本实验 的主操作证据。`
- `CHK5_SEM_EXP_20_2_08_006` `explanation` after: `氢氧化物酸碱性实验的标题是“氢氧化物的酸碱性”，内容是多种金属盐溶液滴加 NaOH 后观察并检验沉淀酸碱性；它只能作为相邻背景，不是本实验的主操作证据。`
- `CHK5_SEM_EXP_20_2_08_008` `explanation` before: `实验 教材资料 只明确给出 Cr₂(SO₄)₃ + Na₂CO₃ 并观察现象；因此 B 的证据闭合。精确颜色、铬酸根颜色或 KSCN 鉴定都超出本点位。`
- `CHK5_SEM_EXP_20_2_08_008` `explanation` after: `实验步骤只明确给出 Cr₂(SO₄)₃ + Na₂CO₃ 并观察现象；因此 B 的判断完整。精确颜色、铬酸根颜色或 KSCN 鉴定都超出本点位。`
- `CHK5_SEM_EXP_20_2_08_009` `stem` before: `关于 实验内容，本实验 的题目通常应如何围绕？`
- `CHK5_SEM_EXP_20_2_08_009` `stem` after: `本实验题目通常应围绕哪一项操作展开？`
- `CHK5_SEM_EXP_20_2_08_009` `options[0].text` before: `只围绕 本实验的 Cr₂(SO₄)₃ 与 Na₂CO₃ 观察点，因为题目均围绕 Cr₂(SO₄)₃ + Na₂CO₃`
- `CHK5_SEM_EXP_20_2_08_009` `options[0].text` after: `只围绕本实验的 Cr₂(SO₄)₃ 与 Na₂CO₃ 观察点，因为题目均围绕 Cr₂(SO₄)₃ + Na₂CO₃`
- `CHK5_SEM_EXP_20_2_08_009` `explanation` before: `原实验资料 只有一个视频点位：Cr₂(SO₄)₃ + Na₂CO₃。相邻文本中的 FeCl₃ 和 TiOSO₄ 只能用于排除混淆，不能扩展为本题的 额外实验点。`
- `CHK5_SEM_EXP_20_2_08_009` `explanation` after: `本实验只有一个视频点位：Cr₂(SO₄)₃ + Na₂CO₃。相邻文本中的 FeCl₃ 和 TiOSO₄ 只能用于排除混淆，不能扩展为本题内容。`
- `CHK5_SEM_EXP_20_2_08_011` `stem` before: `若需要判断“Cr³⁺ 确实有水解倾向”，最合适的 相关化学原理依据是哪一项？`
- `CHK5_SEM_EXP_20_2_08_011` `stem` after: `若需要判断“Cr³⁺ 确实有水解倾向”，最合适的相关化学原理依据是哪一项？`
- `CHK5_SEM_EXP_20_2_08_011` `explanation` before: `Cr³⁺ 水解表格记录 是附录中 Cr³⁺ 水解的表格记录。过氧化氢氧化还原、离子颜色或 NaOH 酸碱性实验都不能直接证明 Cr³⁺ 水解倾向。`
- `CHK5_SEM_EXP_20_2_08_011` `explanation` after: `Cr³⁺ 水解表格记录是附录中 Cr³⁺ 水解的表格记录。过氧化氢氧化还原、离子颜色或 NaOH 酸碱性实验都不能直接证明 Cr³⁺ 水解倾向。`
- `CHK5_SEM_EXP_20_2_08_012` `options[0].text` before: `Cr(OH)₃ 难溶化合物记录 中 Cr(OH)₃ 的难溶化合物记录`
- `CHK5_SEM_EXP_20_2_08_012` `options[0].text` after: `Cr(OH)₃ 难溶化合物记录中 Cr(OH)₃ 的难溶化合物记录`
- `CHK5_SEM_EXP_20_2_08_012` `options[2].text` before: `金属离子水解实验步骤 中 TiOSO₄ 的水解步骤`
- `CHK5_SEM_EXP_20_2_08_012` `options[2].text` after: `金属离子水解实验步骤中 TiOSO₄ 的水解步骤`
- `CHK5_SEM_EXP_20_2_08_012` `options[3].text` before: `氢氧化物酸碱性实验 中“加热可溶于稀碱的溶液”`
- `CHK5_SEM_EXP_20_2_08_012` `options[3].text` after: `氢氧化物酸碱性实验中“加热可溶于稀碱的溶液”`
- `CHK5_SEM_EXP_20_2_08_014` `stem` before: `判断：仅凭 金属离子水解实验步骤，可以断言该步骤的具体沉淀颜色。`
- `CHK5_SEM_EXP_20_2_08_014` `stem` after: `判断：仅凭金属离子水解实验步骤，可以断言该步骤的具体沉淀颜色。`
- `CHK5_SEM_EXP_20_2_08_015` `explanation` before: `判断正确。教材资料中同一小节列出铁(Ⅲ)、铬(Ⅲ)、钛(Ⅳ)三种盐的水解步骤；本实验 只取中间的铬(Ⅲ)盐水解点位。`
- `CHK5_SEM_EXP_20_2_08_015` `explanation` after: `判断正确。教材资料中同一小节列出铁(Ⅲ)、铬(Ⅲ)、钛(Ⅳ)三种盐的水解步骤；本实验只取中间的铬(Ⅲ)盐水解点位。`
- `CHK5_SEM_EXP_20_2_08_016` `stem` before: `判断：把 NaOH 酸碱性实验中的操作直接当成本实验 的 Na₂CO₃ 水解操作，是证据错配。`
- `CHK5_SEM_EXP_20_2_08_016` `stem` after: `判断：把 NaOH 酸碱性实验中的操作直接当成本实验的 Na₂CO₃ 水解操作，是证据错配。`
- `CHK5_SEM_EXP_20_2_08_016` `explanation` before: `判断正确。氢氧化物酸碱性实验 是 NaOH 和沉淀酸碱性测试；本实验 的主操作来自 金属离子水解实验步骤 中 Cr₂(SO₄)₃ 加 Na₂CO₃ 的水解观察。`
- `CHK5_SEM_EXP_20_2_08_016` `explanation` after: `判断正确。氢氧化物酸碱性实验是 NaOH 和沉淀酸碱性测试；本实验的主操作来自金属离子水解实验步骤中 Cr₂(SO₄)₃ 加 Na₂CO₃ 的水解观察。`
- `CHK5_SEM_EXP_20_2_08_018` `stem` before: `判断：本实验 中没有跨多个视频点位的判断需求。`
- `CHK5_SEM_EXP_20_2_08_018` `stem` after: `判断：本实验中没有跨多个视频点位的判断需求。`
- `CHK5_SEM_EXP_20_2_08_018` `explanation` before: `判断正确。原实验资料 只有一个视频点位 本实验的 Cr₂(SO₄)₃ 与 Na₂CO₃ 观察点，最多引用相邻 教材内容作排除项，不应机械加入 额外实验点。`
- `CHK5_SEM_EXP_20_2_08_018` `explanation` after: `判断正确。本实验只有一个视频点位：Cr₂(SO₄)₃ + Na₂CO₃，最多引用相邻教材内容作排除项，不应机械加入额外实验点。`
- `CHK5_SEM_EXP_20_2_08_019` `stem` before: `以下哪种说法最不适合直接发布为本实验 的准确结论题？`
- `CHK5_SEM_EXP_20_2_08_019` `stem` after: `以下哪种说法最不适合作为本实验的准确结论？`
- `CHK5_SEM_EXP_20_2_08_020` `explanation` before: `教材资料 对本点位给出的试剂组合是 Cr₂(SO₄)₃ 和 Na₂CO₃。KSCN 血红色反应不在该步骤中，不能作为本实验结论。`
- `CHK5_SEM_EXP_20_2_08_020` `explanation` after: `教材资料对本点位给出的试剂组合是 Cr₂(SO₄)₃ 和 Na₂CO₃。KSCN 血红色反应不在该步骤中，不能作为本实验结论。`
- `CHK5_SEM_EXP_20_2_08_022` `stem` before: `哪项最能说明“CrO₄²⁻ 黄色”不应作为本实验 的正确答案？`
- `CHK5_SEM_EXP_20_2_08_022` `stem` after: `哪项最能说明“CrO₄²⁻ 黄色”不属于本实验的正确结论？`
- `CHK5_SEM_EXP_20_2_08_022` `explanation` before: `即使其他章节讨论 CrO₄²⁻ 颜色，它也不等于本实验的 Cr₂(SO₄)₃ + Na₂CO₃ 水解观察；本实验 的正确证据应回到该操作体系。`
- `CHK5_SEM_EXP_20_2_08_022` `explanation` after: `即使其他章节讨论 CrO₄²⁻ 颜色，它也不等于本实验的 Cr₂(SO₄)₃ + Na₂CO₃ 水解观察；本实验的判断依据应回到该操作体系。`
- `CHK5_SEM_EXP_20_2_08_025` `stem` before: `下列哪项解释最符合“为什么不能只靠原实验资料 继承的 相关化学原理依据”？`
- `CHK5_SEM_EXP_20_2_08_025` `stem` after: `为什么不能把其他章节的离子颜色或氧化还原资料直接当成本实验依据？`
- `CHK5_SEM_EXP_20_2_08_025` `options[0].text` before: `因为 相关化学原理依据 只要存在于 教材资料，就一定能支撑任意题目`
- `CHK5_SEM_EXP_20_2_08_025` `options[0].text` after: `只要教材中出现某条资料，就一定能支撑任意实验判断`
- `CHK5_SEM_EXP_20_2_08_025` `options[1].text` before: `因为必须读 教材内容，确认该 相关化学原理 是否真的支撑最终题干的判断`
- `CHK5_SEM_EXP_20_2_08_025` `options[1].text` after: `必须确认相关化学原理是否真的支撑题干中的具体判断`
- `CHK5_SEM_EXP_20_2_08_025` `options[2].text` before: `因为所有题目都只能引用 教材资料，不能引用 相关化学原理`
- `CHK5_SEM_EXP_20_2_08_025` `options[2].text` after: `所有题目都只能依据实验步骤，不能依据相关化学原理`
- `CHK5_SEM_EXP_20_2_08_025` `options[3].text` before: `因为 选项反馈 可以替代 教材依据`
- `CHK5_SEM_EXP_20_2_08_025` `options[3].text` after: `选项反馈可以替代教材依据核对`
- `CHK5_SEM_EXP_20_2_08_025` `explanation` before: `原实验资料 中继承了离子颜色和过氧化氢氧化还原等 相关化学原理依据，但这些并不自动支撑铬(Ⅲ)盐水解题。题目只在 Cr³⁺ 水解或 Cr(OH)₃ 难溶判断处使用匹配 相关化学原理。`
- `CHK5_SEM_EXP_20_2_08_025` `explanation` after: `其他章节中的离子颜色和过氧化氢氧化还原资料，并不自动支撑铬(Ⅲ)盐水解题；只有涉及 Cr³⁺ 水解或 Cr(OH)₃ 难溶判断时，才需要匹配的相关化学原理。`
- `CHK5_SEM_EXP_20_2_08_027` `stem` before: `关于选项诊断，下列哪条 选项反馈 写法最符合本题语义？`
- `CHK5_SEM_EXP_20_2_08_027` `stem` after: `下列哪条选项反馈最能说明错误选项的问题？`
- `CHK5_SEM_EXP_20_2_08_027` `explanation` before: `高质量 选项反馈 必须对具体选项说明错配来源。TiOSO₄ 是相邻钛(Ⅳ)盐水解，诊断应写明它与本铬(Ⅲ)盐水解点位的关系。`
- `CHK5_SEM_EXP_20_2_08_027` `explanation` after: `清晰的选项反馈应当说明具体错配来源。TiOSO₄ 是相邻钛(Ⅳ)盐水解，反馈应写明它与本铬(Ⅲ)盐水解点位的关系。`

### Follow-Up 20-2-09

- `CHK5_SEM_EXP_20_2_09_003` `stem` before: `如果题目问 TiOSO₄ 水解的产物判断，哪项说法有 相关化学原理 证据支撑？`
- `CHK5_SEM_EXP_20_2_09_003` `stem` after: `如果题目问 TiOSO₄ 水解的产物判断，哪项说法有相关化学原理证据支撑？`
- `CHK5_SEM_EXP_20_2_09_003` `explanation` before: `相关化学原理 明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，并进一步煅烧得到 TiO₂；其他选项不属于该水解体系。`
- `CHK5_SEM_EXP_20_2_09_003` `explanation` after: `相关化学原理明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，并进一步煅烧得到 TiO₂；其他选项不属于该水解体系。`
- `CHK5_SEM_EXP_20_2_09_004` `explanation` before: `实验步骤要求加入适量蒸馏水，相关化学原理 进一步说明稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，因此 B 的判断有证据闭合。`
- `CHK5_SEM_EXP_20_2_09_004` `explanation` after: `实验步骤要求加入适量蒸馏水，相关化学原理进一步说明稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃，因此 B 的判断有判断完整。`
- `CHK5_SEM_EXP_20_2_09_005` `stem` before: `关于“加热煮沸”的作用，哪项最符合本实验与 相关化学原理 的结合？`
- `CHK5_SEM_EXP_20_2_09_005` `stem` after: `关于“加热煮沸”的作用，哪项最符合本实验与相关化学原理的结合？`
- `CHK5_SEM_EXP_20_2_09_005` `explanation` before: `教材资料 要求加热煮沸并观察现象；相关化学原理 明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃。C 才把操作和目的连起来。`
- `CHK5_SEM_EXP_20_2_09_005` `explanation` after: `教材步骤要求加热煮沸并观察现象；相关化学原理明确写到稀释、加热使 TiOSO₄ 水解得到 H₂TiO₃。C 才把操作和目的连起来。`
- `CHK5_SEM_EXP_20_2_09_006` `stem` before: `下列哪项是本实验 的相邻实验干扰项，而不是钛(Ⅳ)盐水解？`
- `CHK5_SEM_EXP_20_2_09_006` `stem` after: `下列哪项是本实验的相邻实验干扰项，而不是钛(Ⅳ)盐水解？`
- `CHK5_SEM_EXP_20_2_09_007` `explanation` before: `本实验 的语义是 TiOSO₄ 稀释后加热煮沸并观察水解，而不是孤立记忆 TiOSO₄ 名称。`
- `CHK5_SEM_EXP_20_2_09_007` `explanation` after: `本实验的语义是 TiOSO₄ 稀释后加热煮沸并观察水解，而不是孤立记忆 TiOSO₄ 名称。`
- `CHK5_SEM_EXP_20_2_09_008` `options[1].text` before: `引用实验步骤判断 TiOSO₄ 加水、煮沸、观察现象；涉及 H₂TiO₃ 时另引 相关化学原理`
- `CHK5_SEM_EXP_20_2_09_008` `options[1].text` after: `引用实验步骤判断 TiOSO₄ 加水、煮沸、观察现象；涉及 H₂TiO₃ 时另引相关化学原理`
- `CHK5_SEM_EXP_20_2_09_008` `options[3].text` before: `只看 实验 中 继承依据，不读 教材内容`
- `CHK5_SEM_EXP_20_2_09_008` `options[3].text` after: `只看 实验 中继承依据，不读教材内容`
- `CHK5_SEM_EXP_20_2_09_008` `explanation` before: `教材资料 支撑操作步骤；产物 H₂TiO₃ 的判断需要 TiOSO₄ 水解产物资料 和 TiO₂ 转化资料。B 明确区分这两类证据。`
- `CHK5_SEM_EXP_20_2_09_008` `explanation` after: `教材资料支撑操作步骤；产物 H₂TiO₃ 的判断需要TiOSO₄ 水解产物资料和TiO₂ 转化资料。B 明确区分这两类证据。`
- `CHK5_SEM_EXP_20_2_09_009` `options[0].text` before: `教材资料 只要求观察现象；若写白色沉淀或 H₂TiO₃，应另有 相关化学原理 支撑`
- `CHK5_SEM_EXP_20_2_09_009` `options[0].text` after: `教材步骤只要求观察现象；若写白色沉淀或 H₂TiO₃，应另有相关化学原理支撑`
- `CHK5_SEM_EXP_20_2_09_009` `options[1].text` before: `教材资料 已逐字写明“红色沉淀”`
- `CHK5_SEM_EXP_20_2_09_009` `options[1].text` after: `教材资料已逐字写明“红色沉淀”`
- `CHK5_SEM_EXP_20_2_09_009` `options[2].text` before: `教材资料 已逐字写明“CCl₄ 层变紫”`
- `CHK5_SEM_EXP_20_2_09_009` `options[2].text` after: `教材资料已逐字写明“CCl₄ 层变紫”`
- `CHK5_SEM_EXP_20_2_09_009` `options[3].text` before: `教材资料 已逐字写明“金属钠熔成小球”`
- `CHK5_SEM_EXP_20_2_09_009` `options[3].text` after: `教材资料已逐字写明“金属钠熔成小球”`
- `CHK5_SEM_EXP_20_2_09_009` `explanation` before: `实验步骤只写观察现象，没有直接给出具体颜色。白色水解产物或 H₂TiO₃ 需要 相关化学原理；B、C、D 都是无证据或错实验语境。`
- `CHK5_SEM_EXP_20_2_09_009` `explanation` after: `实验步骤只写观察现象，没有直接给出具体颜色。白色水解产物或 H₂TiO₃ 需要相关化学原理；B、C、D 都是无证据或错实验语境。`
- `CHK5_SEM_EXP_20_2_09_010` `explanation` before: `A、B、C 直接来自 教材资料 的钛(Ⅳ)盐水解步骤；D 是钴离子鉴定或配合物显色语境，不属于本实验。`
- `CHK5_SEM_EXP_20_2_09_010` `explanation` after: `A、B、C 直接来自教材资料的钛(Ⅳ)盐水解步骤；D 是钴离子鉴定或配合物显色语境，不属于本实验。`
- `CHK5_SEM_EXP_20_2_09_011` `stem` before: `关于 实验内容，本实验 的题目应如何围绕？`
- `CHK5_SEM_EXP_20_2_09_011` `stem` after: `本实验题目应围绕哪一项操作？`
- `CHK5_SEM_EXP_20_2_09_011` `options[0].text` before: `只围绕 本实验的 TiOSO₄ 稀释煮沸观察点，因为题目围绕 TiOSO₄ 稀释后加热煮沸`
- `CHK5_SEM_EXP_20_2_09_011` `options[0].text` after: `只围绕本实验的 TiOSO₄ 稀释煮沸观察点，因为题目围绕 TiOSO₄ 稀释后加热煮沸`
- `CHK5_SEM_EXP_20_2_09_011` `explanation` before: `原实验资料 只有一个视频点位：TiOSO₄ 稀释后加热煮沸。铁(Ⅲ)和铬(Ⅲ)步骤只能作为相邻干扰项，不是真实 额外实验点。`
- `CHK5_SEM_EXP_20_2_09_011` `explanation` after: `本实验只有一个视频点位：TiOSO₄ 稀释后加热煮沸。铁(Ⅲ)和铬(Ⅲ)步骤只能作为相邻干扰项，不是真实的额外实验点。`
- `CHK5_SEM_EXP_20_2_09_012` `explanation` before: `判断正确。这句话概括了 教材资料 钛(Ⅳ)盐水解步骤。`
- `CHK5_SEM_EXP_20_2_09_012` `explanation` after: `判断正确。这句话概括了教材资料钛(Ⅳ)盐水解步骤。`
- `CHK5_SEM_EXP_20_2_09_013` `stem` before: `判断：TiOSO₄ 水解得到 H₂TiO₃ 的判断需要 相关化学原理，而不是只靠实验步骤中的“观察现象”。`
- `CHK5_SEM_EXP_20_2_09_013` `stem` after: `判断：TiOSO₄ 水解得到 H₂TiO₃ 的判断需要相关化学原理，而不是只靠实验步骤中的“观察现象”。`
- `CHK5_SEM_EXP_20_2_09_013` `explanation` before: `判断正确。教材资料 只写观察现象；TiOSO₄ 水解产物资料 和 TiO₂ 转化资料 才明确给出 TiOSO₄ 水解得到 H₂TiO₃。`
- `CHK5_SEM_EXP_20_2_09_013` `explanation` after: `判断正确。教材步骤只写观察现象；TiOSO₄ 水解产物资料和TiO₂ 转化资料才明确给出 TiOSO₄ 水解得到 H₂TiO₃。`
- `CHK5_SEM_EXP_20_2_09_014` `explanation` before: `判断错误。教材资料 明确要求加入适量蒸馏水，相关化学原理 也说明稀释、加热使 TiOSO₄ 水解。`
- `CHK5_SEM_EXP_20_2_09_014` `explanation` after: `判断错误。教材资料明确要求加入适量蒸馏水，相关化学原理也说明稀释、加热使 TiOSO₄ 水解。`
- `CHK5_SEM_EXP_20_2_09_016` `stem` before: `判断：同一 教材小节还列出铁(Ⅲ)盐和铬(Ⅲ)盐水解，但它们只能作相邻背景，不能替代钛(Ⅳ)盐点位。`
- `CHK5_SEM_EXP_20_2_09_016` `stem` after: `判断：同一教材小节还列出铁(Ⅲ)盐和铬(Ⅲ)盐水解，但它们只能作相邻背景，不能替代钛(Ⅳ)盐点位。`
- `CHK5_SEM_EXP_20_2_09_016` `explanation` before: `判断正确。同一小节中 Fe、Cr、Ti 三个水解步骤并列；本实验 只围绕 TiOSO₄ 稀释煮沸点位。`
- `CHK5_SEM_EXP_20_2_09_016` `explanation` after: `判断正确。同一小节中 Fe、Cr、Ti 三个水解步骤并列；本实验只围绕 TiOSO₄ 稀释煮沸点位。`
- `CHK5_SEM_EXP_20_2_09_018` `stem` before: `以下哪条 选项反馈 诊断最符合本实验 的语义？`
- `CHK5_SEM_EXP_20_2_09_018` `stem` after: `以下哪条选项反馈最符合本实验语义？`
- `CHK5_SEM_EXP_20_2_09_018` `explanation` before: `高质量 选项反馈 要说明具体错配来源。A 指出了 FeCl₃ 是相邻水解步骤，不是本 TiOSO₄ 点位；B 是模板话，C、D 是事实错误。`
- `CHK5_SEM_EXP_20_2_09_018` `explanation` after: `清晰的选项反馈要说明具体错配来源。A 指出了 FeCl₃ 是相邻水解步骤，不是本 TiOSO₄ 点位；B 是模板话，C、D 是事实错误。`
- `CHK5_SEM_EXP_20_2_09_019` `options[0].text` before: `只用 金属离子水解实验步骤`
- `CHK5_SEM_EXP_20_2_09_019` `options[0].text` after: `只用金属离子水解实验步骤`
- `CHK5_SEM_EXP_20_2_09_019` `options[1].text` before: `金属离子水解实验步骤 加 TiOSO₄ 水解产物资料 和 TiO₂ 转化资料`
- `CHK5_SEM_EXP_20_2_09_019` `options[1].text` after: `金属离子水解实验步骤加TiOSO₄ 水解产物资料和TiO₂ 转化资料`
- `CHK5_SEM_EXP_20_2_09_019` `options[2].text` before: `钛(Ⅳ)过氧化氢鉴定资料 单独作为水解产物证据`
- `CHK5_SEM_EXP_20_2_09_019` `options[2].text` after: `钛(Ⅳ)过氧化氢鉴定资料单独作为水解产物证据`
- `CHK5_SEM_EXP_20_2_09_019` `options[3].text` before: `任意存在于 教材资料 的钛相关 依据 都可`
- `CHK5_SEM_EXP_20_2_09_019` `options[3].text` after: `任意存在于教材资料的钛相关 依据 都可`
- `CHK5_SEM_EXP_20_2_09_019` `explanation` before: `教材资料 支撑实验操作，'01156' 和 '01157' 支撑 TiOSO₄ 水解得到 H₂TiO₃ 的产物判断。只用 教材资料 不足以证明产物，任意钛相关 依据 也不等于语义支持。`
- `CHK5_SEM_EXP_20_2_09_019` `explanation` after: `教材资料支撑实验操作，'01156' 和 '01157' 支撑 TiOSO₄ 水解得到 H₂TiO₃ 的产物判断。只用教材资料不足以证明产物，任意钛相关 依据 也不等于语义支持。`
- `CHK5_SEM_EXP_20_2_09_020` `stem` before: `下列哪项最能说明 钛(Ⅳ)过氧化氢鉴定资料 不适合作为本实验 的主要水解产物证据？`
- `CHK5_SEM_EXP_20_2_09_020` `stem` after: `下列哪项最能说明钛(Ⅳ)过氧化氢鉴定资料不适合作为本实验的主要水解产物证据？`
- `CHK5_SEM_EXP_20_2_09_020` `options[1].text` before: `它不是 教材资料中的真实 依据`
- `CHK5_SEM_EXP_20_2_09_020` `options[1].text` after: `它不是教材资料中的真实 依据`
- `CHK5_SEM_EXP_20_2_09_021` `explanation` before: `教材资料 明确给出本实验试剂和操作为 TiOSO₄ 加水、煮沸、观察。CoCl₂ 与 KSCN 不属于该步骤。`
- `CHK5_SEM_EXP_20_2_09_021` `explanation` after: `教材资料明确给出本实验试剂和操作为 TiOSO₄ 加水、煮沸、观察。CoCl₂ 与 KSCN 不属于该步骤。`
- `CHK5_SEM_EXP_20_2_09_024` `options[0].text` before: `教材资料 只写观察现象；白色 H₂TiO₃ 或水合 TiO₂ 判断要依赖 相关化学原理`
- `CHK5_SEM_EXP_20_2_09_024` `options[0].text` after: `教材步骤只写观察现象；白色 H₂TiO₃ 或水合 TiO₂ 判断要依赖相关化学原理`
- `CHK5_SEM_EXP_20_2_09_024` `options[1].text` before: `教材资料 已经逐字写明白色 H₂TiO₃`
- `CHK5_SEM_EXP_20_2_09_024` `options[1].text` after: `教材资料已经逐字写明白色 H₂TiO₃`
- `CHK5_SEM_EXP_20_2_09_024` `explanation` before: `教材资料 没有写具体颜色或产物；相关化学原理 支撑 TiOSO₄ 水解得到 H₂TiO₃，因而沉淀/产物题必须标明 相关化学原理 依赖。`
- `CHK5_SEM_EXP_20_2_09_024` `explanation` after: `教材步骤没有写具体颜色或产物；相关化学原理支撑 TiOSO₄ 水解得到 H₂TiO₃，因而沉淀/产物题必须标明相关化学原理依赖。`
- `CHK5_SEM_EXP_20_2_09_025` `explanation` before: `教材资料 要求加入适量蒸馏水，相关化学原理 也写到稀释、加热使 TiOSO₄ 水解。答案“稀释”短且确定。`
- `CHK5_SEM_EXP_20_2_09_025` `explanation` after: `教材步骤要求加入适量蒸馏水，相关化学原理也写到稀释、加热使 TiOSO₄ 水解。答案“稀释”短且确定。`
- `CHK5_SEM_EXP_20_2_09_026` `explanation` before: `B 完整复述了 教材资料 中钛(Ⅳ)盐水解的顺序；A 和 C 是同小节相邻 Fe/Cr 步骤，D 是无关鉴定操作。`
- `CHK5_SEM_EXP_20_2_09_026` `explanation` after: `B 完整复述了教材资料中钛(Ⅳ)盐水解的顺序；A 和 C 是同小节相邻 Fe/Cr 步骤，D 是无关鉴定操作。`
- `CHK5_SEM_EXP_20_2_09_028` `options[0].text` before: `教材资料 还要求加入适量蒸馏水、加热煮沸并观察现象`
- `CHK5_SEM_EXP_20_2_09_028` `options[0].text` after: `教材资料还要求加入适量蒸馏水、加热煮沸并观察现象`
- `CHK5_SEM_EXP_20_2_09_029` `stem` before: `如果题目要求学生选出本实验的 教材资料 教材依据，哪项最合适？`
- `CHK5_SEM_EXP_20_2_09_029` `stem` after: `如果题目要求学生选出本实验的教材资料教材依据，哪项最合适？`
- `CHK5_SEM_EXP_20_2_09_029` `explanation` before: `金属离子水解实验步骤 是实验教材中金属离子水解作用的 教材实验步骤，直接包含 TiOSO₄ 加水、煮沸、观察现象的步骤。其他 依据 可作特定 相关化学原理 背景，但不是本实验步骤主证据。`
- `CHK5_SEM_EXP_20_2_09_029` `explanation` after: `金属离子水解实验步骤是实验教材中金属离子水解作用的教材实验步骤，直接包含 TiOSO₄ 加水、煮沸、观察现象的步骤。其他 依据 可作特定相关化学原理背景，但不是本实验步骤的主要依据。`

### Follow-Up 20-2-10

- `CHK5_SEM_EXP_20_2_10_001` `explanation` before: `教材资料 小设计实验的任务就是把含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离并检出；其他选项属于不同离子组。`
- `CHK5_SEM_EXP_20_2_10_001` `explanation` after: `教材资料小设计实验的任务就是把含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离并检出；其他选项属于不同离子组。`
- `CHK5_SEM_EXP_20_2_10_003` `explanation` before: `相关化学原理 明确说明 Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似；这个性质可与锰(Ⅱ)氢氧化物的处理差异结合，用于设计分离。`
- `CHK5_SEM_EXP_20_2_10_003` `explanation` after: `相关化学原理明确说明 Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似；这个性质可与锰(Ⅱ)氢氧化物的处理差异结合，用于设计分离。`
- `CHK5_SEM_EXP_20_2_10_004` `explanation` before: `前置铬氧化还原实验和 相关化学原理 都指向碱性过氧化氢可把铬(Ⅲ)氧化为 CrO₄²⁻；颜色 相关化学原理 说明 CrO₄²⁻ 呈黄色。`
- `CHK5_SEM_EXP_20_2_10_004` `explanation` after: `前置铬氧化还原实验和相关化学原理都指向碱性过氧化氢可把铬(Ⅲ)氧化为 CrO₄²⁻；颜色相关化学原理说明 CrO₄²⁻ 呈黄色。`
- `CHK5_SEM_EXP_20_2_10_005` `explanation` before: `相关化学原理 的铬(Ⅲ)/铝(Ⅲ)分离示意说明，NH₃/H₂O₂ 条件下 Al 生成 Al(OH)₃ 沉淀，而铬(Ⅲ)被氧化为 CrO₄²⁻ 留在溶液中。`
- `CHK5_SEM_EXP_20_2_10_005` `explanation` after: `相关化学原理的铬(Ⅲ)/铝(Ⅲ)分离示意说明，NH₃/H₂O₂ 条件下 Al 生成 Al(OH)₃ 沉淀，而铬(Ⅲ)被氧化为 CrO₄²⁻ 留在溶液中。`
- `CHK5_SEM_EXP_20_2_10_006` `explanation` before: `锰(Ⅱ) 相关化学原理 说明，强氧化剂可把 Mn²⁺ 氧化为 MnO₄⁻，且 MnO₄⁻ 呈紫色，现象明显，可用于鉴定 Mn²⁺。`
- `CHK5_SEM_EXP_20_2_10_006` `explanation` after: `锰(Ⅱ)相关化学原理说明，强氧化剂可把 Mn²⁺ 氧化为 MnO₄⁻，且 MnO₄⁻ 呈紫色，现象明显，可用于鉴定 Mn²⁺。`
- `CHK5_SEM_EXP_20_2_10_007` `explanation` before: `教材资料 要求“分离检出”，因此设计方案不只写分离操作，还要给出每种目标离子的检出依据或确认现象。`
- `CHK5_SEM_EXP_20_2_10_007` `explanation` after: `教材步骤要求“分离检出”，因此设计方案不只写分离操作，还要给出每种目标离子的检出依据或确认现象。`
- `CHK5_SEM_EXP_20_2_10_009` `explanation` before: `教材资料 任务的关键词是“分离检出”三种离子，因此合格题目应考查分步分离与分别检出，而不是套用无关铁显色或只处理其中一种离子。`
- `CHK5_SEM_EXP_20_2_10_009` `explanation` after: `教材资料任务的关键词是“分离检出”三种离子，因此合格题目应考查分步分离与分别检出，而不是套用无关铁显色或只处理其中一种离子。`
- `CHK5_SEM_EXP_20_2_10_011` `explanation` before: `教材资料 明确给出小设计实验的目标混合溶液含 Cr³⁺、Al³⁺、Mn²⁺。`
- `CHK5_SEM_EXP_20_2_10_011` `explanation` after: `教材资料明确给出小设计实验的目标混合溶液含 Cr³⁺、Al³⁺、Mn²⁺。`
- `CHK5_SEM_EXP_20_2_10_012` `explanation` before: `相关化学原理 对铬(Ⅲ)/铝(Ⅲ)分离的说明正是：Al(OH)₃ 沉淀，铬(Ⅲ)被氧化为 CrO₄²⁻；这可支撑本小设计实验中的 Cr/Al 分离环节。`
- `CHK5_SEM_EXP_20_2_10_012` `explanation` after: `相关化学原理对铬(Ⅲ)/铝(Ⅲ)分离的说明正是：Al(OH)₃ 沉淀，铬(Ⅲ)被氧化为 CrO₄²⁻；这可支撑本小设计实验中的 Cr/Al 分离环节。`
- `CHK5_SEM_EXP_20_2_10_013` `explanation` before: `相关化学原理 给出碱性过氧化氢将铬(Ⅲ)羟基配合物氧化为 CrO₄²⁻ 的反应证据，因此该判断正确。`
- `CHK5_SEM_EXP_20_2_10_013` `explanation` after: `相关化学原理给出碱性过氧化氢将铬(Ⅲ)羟基配合物氧化为 CrO₄²⁻ 的反应证据，因此该判断正确。`
- `CHK5_SEM_EXP_20_2_10_014` `stem` before: `分离 Cr³⁺ 与 Al³⁺ 时，只加氨水、不加入 H₂O₂，就足以体现 相关化学原理 中的推荐分离思路。`
- `CHK5_SEM_EXP_20_2_10_014` `stem` after: `分离 Cr³⁺ 与 Al³⁺ 时，只加氨水、不加入 H₂O₂，就足以体现相关化学原理中的推荐分离思路。`
- `CHK5_SEM_EXP_20_2_10_014` `explanation` before: `相关化学原理 明确说 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，先把铬(Ⅲ)氧化。`
- `CHK5_SEM_EXP_20_2_10_014` `explanation` after: `相关化学原理明确说 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，先把铬(Ⅲ)氧化。`
- `CHK5_SEM_EXP_20_2_10_015` `explanation` before: `锰(Ⅱ) 相关化学原理 明确指出，把 Mn²⁺ 氧化成 MnO₄⁻ 且因紫色现象明显，可用于鉴定 Mn²⁺。`
- `CHK5_SEM_EXP_20_2_10_015` `explanation` after: `锰(Ⅱ)相关化学原理明确指出，把 Mn²⁺ 氧化成 MnO₄⁻ 且因紫色现象明显，可用于鉴定 Mn²⁺。`
- `CHK5_SEM_EXP_20_2_10_016` `explanation` before: `教材资料 指定的是 Cr³⁺、Al³⁺、Mn²⁺，不是 Ag⁺、Pb²⁺、Zn²⁺、Cu²⁺。`
- `CHK5_SEM_EXP_20_2_10_016` `explanation` after: `教材资料指定的是 Cr³⁺、Al³⁺、Mn²⁺，不是 Ag⁺、Pb²⁺、Zn²⁺、Cu²⁺。`
- `CHK5_SEM_EXP_20_2_10_018` `explanation` before: `教材资料 要求分离检出。方案只列试剂不能证明每种目标离子已被分别确认，因此不完整。`
- `CHK5_SEM_EXP_20_2_10_018` `explanation` after: `教材步骤要求分离检出。方案只列试剂不能证明每种目标离子已被分别确认，因此不完整。`
- `CHK5_SEM_EXP_20_2_10_019` `explanation` before: `前置实验要求滴加 NaOH 并检验沉淀酸碱性；相关化学原理 也支持 Cr(OH)₃、Al(OH)₃、Mn(OH)₂ 等性质差异可服务于分离设计。`
- `CHK5_SEM_EXP_20_2_10_019` `explanation` after: `前置实验要求滴加 NaOH 并检验沉淀酸碱性；相关化学原理也支持 Cr(OH)₃、Al(OH)₃、Mn(OH)₂ 等性质差异可服务于分离设计。`
- `CHK5_SEM_EXP_20_2_10_021` `options[3].text` before: `无法判断，因为 教材资料 没有给出目标离子`
- `CHK5_SEM_EXP_20_2_10_021` `options[3].text` after: `无法判断，因为教材资料没有给出目标离子`
- `CHK5_SEM_EXP_20_2_10_021` `explanation` before: `教材资料 已明确目标离子为 Cr³⁺、Al³⁺、Mn²⁺。Fe³⁺-KSCN 显色是错误语境，不能替代三种目标离子的分离检出。`
- `CHK5_SEM_EXP_20_2_10_021` `explanation` after: `教材资料已明确目标离子为 Cr³⁺、Al³⁺、Mn²⁺。Fe³⁺-KSCN 显色是错误语境，不能替代三种目标离子的分离检出。`
- `CHK5_SEM_EXP_20_2_10_022` `stem` before: `关于 Mn²⁺ 在碱性分离步骤中的表现，哪项说法有 相关化学原理 支撑？`
- `CHK5_SEM_EXP_20_2_10_022` `stem` after: `关于 Mn²⁺ 在碱性分离步骤中的表现，哪项说法有相关化学原理支撑？`
- `CHK5_SEM_EXP_20_2_10_022` `explanation` before: `锰(Ⅱ) 相关化学原理 说明 Mn²⁺ 与 OH⁻ 先生成 Mn(OH)₂ 沉淀，放置后可被氧化为棕色沉淀；这可作为分离和后续检出的线索。`
- `CHK5_SEM_EXP_20_2_10_022` `explanation` after: `锰(Ⅱ)相关化学原理说明 Mn²⁺ 与 OH⁻ 先生成 Mn(OH)₂ 沉淀，放置后可被氧化为棕色沉淀；这可作为分离和后续检出的线索。`
- `CHK5_SEM_EXP_20_2_10_023` `explanation` before: `相关化学原理 明确写到 Al(OH)₃ 呈酸碱两性，Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似。答案是短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_2_10_023` `explanation` after: `相关化学原理明确写到 Al(OH)₃ 呈酸碱两性，Cr(OH)₃ 也具有两性并与 Al(OH)₃ 相似。答案是短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_2_10_024` `options[1].text` before: `用小设计任务定位目标，再用碱性 H₂O₂ 氧化铬(Ⅲ)的 相关化学原理 解释转化`
- `CHK5_SEM_EXP_20_2_10_024` `options[1].text` after: `用小设计任务定位目标，再用碱性 H₂O₂ 氧化铬(Ⅲ)的相关化学原理解释转化`
- `CHK5_SEM_EXP_20_2_10_024` `explanation` before: `小设计任务只规定要分离检出 Cr³⁺、Al³⁺、Mn²⁺；铬(Ⅲ)到 CrO₄²⁻ 的转化需要前置铬氧化还原实验和 相关化学原理 才能证据闭合。`
- `CHK5_SEM_EXP_20_2_10_024` `explanation` after: `小设计任务只规定要分离检出 Cr³⁺、Al³⁺、Mn²⁺；铬(Ⅲ)到 CrO₄²⁻ 的转化需要前置铬氧化还原实验和相关化学原理才能判断完整。`
- `CHK5_SEM_EXP_20_2_10_025` `options[0].text` before: `因为 教材资料 不允许使用任何碱`
- `CHK5_SEM_EXP_20_2_10_025` `options[0].text` after: `因为教材资料不允许使用任何碱`
- `CHK5_SEM_EXP_20_2_10_025` `options[1].text` before: `因为 相关化学原理 指出 Cr³⁺ 与 Al³⁺ 分离需结合 H₂O₂ 氧化铬(Ⅲ)，而不是只靠氨水`
- `CHK5_SEM_EXP_20_2_10_025` `options[1].text` after: `因为相关化学原理指出 Cr³⁺ 与 Al³⁺ 分离需结合 H₂O₂ 氧化铬(Ⅲ)，而不是只靠氨水`
- `CHK5_SEM_EXP_20_2_10_025` `explanation` before: `相关化学原理 明确说明 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，将铬(Ⅲ)氧化后实现分离。`
- `CHK5_SEM_EXP_20_2_10_025` `explanation` after: `相关化学原理明确说明 Cr³⁺ 和 Al³⁺ 不采用只加氨水的方法，而是在加氨水的同时加入 H₂O₂，将铬(Ⅲ)氧化后实现分离。`
- `CHK5_SEM_EXP_20_2_10_026` `explanation` before: `相关化学原理 指出 Mn²⁺ 可被强氧化剂氧化为 MnO₄⁻，且紫色现象明显，因此可作为 Mn²⁺ 的确认检出思路。`
- `CHK5_SEM_EXP_20_2_10_026` `explanation` after: `相关化学原理指出 Mn²⁺ 可被强氧化剂氧化为 MnO₄⁻，且紫色现象明显，因此可作为 Mn²⁺ 的确认检出思路。`
- `CHK5_SEM_EXP_20_2_10_027` `explanation` before: `教材资料 的要求不是单纯分离，而是分离检出；答案为短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_2_10_027` `explanation` after: `教材资料的要求不是单纯分离，而是分离检出；答案为短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_2_10_030` `explanation` before: `因为 教材资料 要求“分离检出”，方案必须既有分离顺序，也有能确认目标离子的检出依据或证据。`
- `CHK5_SEM_EXP_20_2_10_030` `explanation` after: `因为教材步骤要求“分离检出”，方案必须既有分离顺序，也有能确认目标离子的检出依据或证据。`

### Follow-Up 20-3-01

- `CHK5_SEM_EXP_20_3_01_002` `explanation` before: `教材资料 明确把水合阳离子和阴离子分成两组列出；分栏记录能避免把 CrO₄²⁻、MnO₄⁻ 等阴离子颜色误当作水合阳离子颜色。`
- `CHK5_SEM_EXP_20_3_01_002` `explanation` after: `教材资料明确把水合阳离子和阴离子分成两组列出；分栏记录能避免把 CrO₄²⁻、MnO₄⁻ 等阴离子颜色误当作水合阳离子颜色。`
- `CHK5_SEM_EXP_20_3_01_008` `explanation` before: `教材资料 实验内容把 [Ti(H₂O)₆]³⁺ 列在水合阳离子观察对象中；本题只考查原文可直接支撑的对象归属和价态。`
- `CHK5_SEM_EXP_20_3_01_008` `explanation` after: `教材资料实验内容把 [Ti(H₂O)₆]³⁺ 列在水合阳离子观察对象中；本题只考查原文可直接支撑的对象归属和价态。`
- `CHK5_SEM_EXP_20_3_01_010` `explanation` before: `D 中三项都在 教材资料 水合阳离子列表中；其他选项混入了阴离子。`
- `CHK5_SEM_EXP_20_3_01_010` `explanation` after: `D 中三项都在教材资料水合阳离子列表中；其他选项混入了阴离子。`
- `CHK5_SEM_EXP_20_3_01_011` `explanation` before: `教材资料 水合阳离子列表中确有 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺。`
- `CHK5_SEM_EXP_20_3_01_011` `explanation` after: `教材资料水合阳离子列表中确有 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺。`
- `CHK5_SEM_EXP_20_3_01_015` `explanation` before: `教材资料 表 20.5 对 Fe²⁺ 水合离子的颜色记录为浅蓝色；因此不沿用这种说法的浅绿色说法。`
- `CHK5_SEM_EXP_20_3_01_015` `explanation` after: `教材资料表 20.5 对 Fe²⁺ 水合离子的颜色记录为浅蓝色；因此不沿用这种说法的浅绿色说法。`
- `CHK5_SEM_EXP_20_3_01_018` `explanation` before: `教材资料 水合阳离子列表中同时列出 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺，二者均带三价正电荷。`
- `CHK5_SEM_EXP_20_3_01_018` `explanation` after: `教材资料水合阳离子列表中同时列出 [Ti(H₂O)₆]³⁺ 和 [Cr(H₂O)₆]³⁺，二者均带三价正电荷。`
- `CHK5_SEM_EXP_20_3_01_020` `explanation` before: `教材资料 水合阳离子列表中包括 [Ni(H₂O)₆]²⁺ 和 [Co(H₂O)₆]²⁺，二者均带二价正电荷。`
- `CHK5_SEM_EXP_20_3_01_020` `explanation` after: `教材资料水合阳离子列表中包括 [Ni(H₂O)₆]²⁺ 和 [Co(H₂O)₆]²⁺，二者均带二价正电荷。`
- `CHK5_SEM_EXP_20_3_01_021` `stem` before: `关于过渡金属水合离子颜色，哪项表述最符合 相关化学原理？`
- `CHK5_SEM_EXP_20_3_01_021` `stem` after: `关于过渡金属水合离子颜色，哪项表述最符合相关化学原理？`
- `CHK5_SEM_EXP_20_3_01_021` `explanation` before: `相关化学原理 说明许多过渡金属水合离子或配离子的颜色与 d 轨道分裂和 d-d 跃迁有关，并且具体颜色随离子与氧化态而变。`
- `CHK5_SEM_EXP_20_3_01_021` `explanation` after: `相关化学原理说明许多过渡金属水合离子或配离子的颜色与 d 轨道分裂和 d-d 跃迁有关，并且具体颜色随离子与氧化态而变。`
- `CHK5_SEM_EXP_20_3_01_022` `explanation` before: `教材资料 把 CrO₄²⁻、MnO₄⁻ 等列为阴离子；相关化学原理 也说明 CrO₄²⁻ 为黄色、MnO₄⁻ 为紫色，不能把它们当作水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_022` `explanation` after: `教材资料把 CrO₄²⁻、MnO₄⁻ 等列为阴离子；相关化学原理也说明 CrO₄²⁻ 为黄色、MnO₄⁻ 为紫色，不能把它们当作水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_025` `explanation` before: `教材资料 列出 [Fe(H₂O)₆]²⁺，但具体颜色要按表 20.5：Fe²⁺ 水合离子为浅蓝色。`
- `CHK5_SEM_EXP_20_3_01_025` `explanation` after: `教材内容列出 [Fe(H₂O)₆]²⁺，但具体颜色要按表 20.5：Fe²⁺ 水合离子为浅蓝色。`
- `CHK5_SEM_EXP_20_3_01_026` `explanation` before: `教材资料 证明 [Ni(H₂O)₆]²⁺ 属于观察对象；表 20.5 和镍配合物表支持其颜色为绿色。`
- `CHK5_SEM_EXP_20_3_01_026` `explanation` after: `教材资料证明 [Ni(H₂O)₆]²⁺ 属于观察对象；表 20.5 和镍配合物表支持其颜色为绿色。`
- `CHK5_SEM_EXP_20_3_01_027` `explanation` before: `相关化学原理 说明过渡金属水合离子和配离子颜色与具体离子、氧化态等有关；不能把所有 d 区水合阳离子记成同一种颜色。`
- `CHK5_SEM_EXP_20_3_01_027` `explanation` after: `相关化学原理说明过渡金属水合离子和配离子颜色与具体离子、氧化态等有关；不能把所有 d 区水合阳离子记成同一种颜色。`

### Follow-Up 20-3-02

- `CHK5_SEM_EXP_20_3_02_002` `explanation` before: `相关化学原理 明确说明 CrO₄²⁻ 呈黄色；粉红色属于 Co²⁺ 水合离子语境，紫色容易与 MnO₄⁻ 混淆。`
- `CHK5_SEM_EXP_20_3_02_002` `explanation` after: `相关化学原理明确说明 CrO₄²⁻ 呈黄色；粉红色属于 Co²⁺ 水合离子语境，紫色容易与 MnO₄⁻ 混淆。`
- `CHK5_SEM_EXP_20_3_02_003` `explanation` before: `相关化学原理 明确说明 MnO₄⁻ 呈紫色；黄色更容易对应 CrO₄²⁻。`
- `CHK5_SEM_EXP_20_3_02_003` `explanation` after: `相关化学原理明确说明 MnO₄⁻ 呈紫色；黄色更容易对应 CrO₄²⁻。`
- `CHK5_SEM_EXP_20_3_02_004` `explanation` before: `教材阴离子列表同时列出 CrO₄²⁻ 和 Cr₂O₇²⁻；相关化学原理 还说明二者可随条件相互转化，因此应区分为相关但不同的含铬含氧阴离子。`
- `CHK5_SEM_EXP_20_3_02_004` `explanation` after: `教材阴离子列表同时列出 CrO₄²⁻ 和 Cr₂O₇²⁻；相关化学原理还说明二者可随条件相互转化，因此应区分为相关但不同的含铬含氧阴离子。`
- `CHK5_SEM_EXP_20_3_02_007` `explanation` before: `相关化学原理 指出一些高氧化态过渡金属含氧酸根阴离子虽然无 d 电子也能显色，原因是 O²⁻ 到金属中心的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_007` `explanation` after: `相关化学原理指出一些高氧化态过渡金属含氧酸根阴离子虽然无 d 电子也能显色，原因是 O²⁻ 到金属中心的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_010` `explanation` before: `[Ni(H₂O)₆]²⁺ 属于上一组水合阳离子颜色对象，不属于本实验 的阴离子颜色重点。`
- `CHK5_SEM_EXP_20_3_02_010` `explanation` after: `[Ni(H₂O)₆]²⁺ 属于上一组水合阳离子颜色对象，不属于本实验的阴离子颜色重点。`
- `CHK5_SEM_EXP_20_3_02_011` `explanation` before: `相关化学原理 给出的对应关系相反：CrO₄²⁻ 为黄色，MnO₄⁻ 为紫色。`
- `CHK5_SEM_EXP_20_3_02_011` `explanation` after: `相关化学原理给出的对应关系相反：CrO₄²⁻ 为黄色，MnO₄⁻ 为紫色。`
- `CHK5_SEM_EXP_20_3_02_012` `explanation` before: `教材资料 列出的是 Cr、Mn、Mo、W、V 的含氧阴离子；相关化学原理 还明确 CrO₄²⁻ 与 MnO₄⁻ 是有色的。`
- `CHK5_SEM_EXP_20_3_02_012` `explanation` after: `教材内容列出的是 Cr、Mn、Mo、W、V 的含氧阴离子；相关化学原理还明确 CrO₄²⁻ 与 MnO₄⁻ 是有色的。`
- `CHK5_SEM_EXP_20_3_02_014` `explanation` before: `本实验 的核心是区分 CrO₄²⁻、Cr₂O₇²⁻、MnO₄²⁻、MnO₄⁻ 等具体阴离子；记录时应把具体离子式和颜色配对。`
- `CHK5_SEM_EXP_20_3_02_014` `explanation` after: `本实验的核心是区分 CrO₄²⁻、Cr₂O₇²⁻、MnO₄²⁻、MnO₄⁻ 等具体阴离子；记录时应把具体离子式和颜色配对。`
- `CHK5_SEM_EXP_20_3_02_015` `stem` before: `下列哪一项颜色对应关系可以由 相关化学原理 直接支撑？`
- `CHK5_SEM_EXP_20_3_02_015` `stem` after: `下列哪一项颜色对应关系可以由相关化学原理直接支撑？`
- `CHK5_SEM_EXP_20_3_02_015` `explanation` before: `相关化学原理 原文直接给出 CrO₄²⁻ 呈黄色、MnO₄⁻ 呈紫色，并把显色解释为荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_015` `explanation` after: `相关化学原理原文直接给出 CrO₄²⁻ 呈黄色、MnO₄⁻ 呈紫色，并把显色解释为荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_017` `explanation` before: `教材资料 在水合阳离子之后另列了阴离子观察对象，本实验 正是阴离子颜色。`
- `CHK5_SEM_EXP_20_3_02_017` `explanation` after: `教材资料在水合阳离子之后另列了阴离子观察对象，本实验正是阴离子颜色。`
- `CHK5_SEM_EXP_20_3_02_018` `explanation` before: `相关化学原理 明确把 CrO₄²⁻、MnO₄⁻ 等含氧阴离子的颜色解释为 O²⁻ 到金属中心的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_018` `explanation` after: `相关化学原理明确把 CrO₄²⁻、MnO₄⁻ 等含氧阴离子的颜色解释为 O²⁻ 到金属中心的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_021` `options[1].text` before: `先确认它们在 教材资料 列表中，再依据实际观察或更精确颜色证据记录`
- `CHK5_SEM_EXP_20_3_02_021` `options[1].text` after: `先确认它们在教材资料列表中，再依据实际观察或更精确颜色证据记录`
- `CHK5_SEM_EXP_20_3_02_021` `explanation` before: `教材资料 能证明这些离子属于观察对象，但本轮直接 相关化学原理 颜色证据只明确给出 CrO₄²⁻ 黄色和 MnO₄⁻ 紫色；其他阴离子的具体颜色不能随意套用。`
- `CHK5_SEM_EXP_20_3_02_021` `explanation` after: `教材内容能证明这些离子属于观察对象，但本轮直接相关化学原理颜色证据只明确给出 CrO₄²⁻ 黄色和 MnO₄⁻ 紫色；其他阴离子的具体颜色不能随意套用。`
- `CHK5_SEM_EXP_20_3_02_022` `options[1].text` before: `错误；相关化学原理 只明确 MnO₄⁻ 为紫色，CrO₄²⁻ 为黄色，不能一概而论`
- `CHK5_SEM_EXP_20_3_02_022` `options[1].text` after: `错误；相关化学原理只明确 MnO₄⁻ 为紫色，CrO₄²⁻ 为黄色，不能一概而论`
- `CHK5_SEM_EXP_20_3_02_022` `options[3].text` before: `无法判断，因为 教材资料 没有列任何阴离子`
- `CHK5_SEM_EXP_20_3_02_022` `options[3].text` after: `无法判断，因为教材资料没有列任何阴离子`
- `CHK5_SEM_EXP_20_3_02_022` `explanation` before: `相关化学原理 明确 CrO₄²⁻ 黄色、MnO₄⁻ 紫色；因此不能把所有含氧阴离子统一记为紫色。`
- `CHK5_SEM_EXP_20_3_02_022` `explanation` after: `相关化学原理明确 CrO₄²⁻ 黄色、MnO₄⁻ 紫色；因此不能把所有含氧阴离子统一记为紫色。`
- `CHK5_SEM_EXP_20_3_02_024` `stem` before: `关于 CrO₄²⁻ 的黄色和 MnO₄⁻ 的紫色，哪项解释最贴近 相关化学原理？`
- `CHK5_SEM_EXP_20_3_02_024` `stem` after: `关于 CrO₄²⁻ 的黄色和 MnO₄⁻ 的紫色，哪项解释最贴近相关化学原理？`
- `CHK5_SEM_EXP_20_3_02_024` `explanation` before: `相关化学原理 把 CrO₄²⁻ 和 MnO₄⁻ 这类含氧阴离子的颜色归因于 O²⁻ 到金属中心的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_024` `explanation` after: `相关化学原理把 CrO₄²⁻ 和 MnO₄⁻ 这类含氧阴离子的颜色归因于 O²⁻ 到金属中心的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_026` `explanation` before: `[Co(H₂O)₆]²⁺ 是水合阳离子，不属于本实验 阴离子列表；不能用它的颜色替代含氧阴离子的颜色。`
- `CHK5_SEM_EXP_20_3_02_026` `explanation` after: `[Co(H₂O)₆]²⁺ 是水合阳离子，不属于本实验阴离子列表；不能用它的颜色替代含氧阴离子的颜色。`
- `CHK5_SEM_EXP_20_3_02_030` `explanation` before: `Cr₂O₇²⁻ 是 教材资料 列出的阴离子，右上角 ²⁻ 表示二负电荷。`
- `CHK5_SEM_EXP_20_3_02_030` `explanation` after: `Cr₂O₇²⁻ 是教材内容列出的阴离子，右上角 ²⁻ 表示二负电荷。`

### Follow-Up 20-3-03

- `CHK5_SEM_EXP_20_3_03_002` `explanation` before: `教材资料 要求取少量 Cr(NO₃)₃ 溶液加热，观察加热前后颜色变化。`
- `CHK5_SEM_EXP_20_3_03_002` `explanation` after: `教材步骤要求取少量 Cr(NO₃)₃ 溶液加热，观察加热前后颜色变化。`
- `CHK5_SEM_EXP_20_3_03_003` `explanation` before: `教材资料 指定操作是加热少量 Cr(NO₃)₃ 溶液，并观察加热前后颜色变化。`
- `CHK5_SEM_EXP_20_3_03_003` `explanation` after: `教材资料指定操作是加热少量 Cr(NO₃)₃ 溶液，并观察加热前后颜色变化。`
- `CHK5_SEM_EXP_20_3_03_004` `explanation` before: `教材资料 明确要求观察加热前后溶液颜色的变化。`
- `CHK5_SEM_EXP_20_3_03_004` `explanation` after: `教材资料明确要求观察加热前后溶液颜色的变化。`
- `CHK5_SEM_EXP_20_3_03_012` `explanation` before: `教材资料 指定起始溶液为 Cr(NO₃)₃ 溶液，不是 Cr₂(SO₄)₃ 加 Na₂CO₃。`
- `CHK5_SEM_EXP_20_3_03_012` `explanation` after: `教材资料指定起始溶液为 Cr(NO₃)₃ 溶液，不是 Cr₂(SO₄)₃ 加 Na₂CO₃。`
- `CHK5_SEM_EXP_20_3_03_013` `explanation` before: `教材资料 明确写到取 Cr(NO₃)₃ 溶液进行加热。`
- `CHK5_SEM_EXP_20_3_03_013` `explanation` after: `教材资料明确写到取 Cr(NO₃)₃ 溶液进行加热。`
- `CHK5_SEM_EXP_20_3_03_014` `explanation` before: `教材资料 要求观察的是加热前后溶液颜色变化，不是质量变化。`
- `CHK5_SEM_EXP_20_3_03_014` `explanation` after: `教材步骤要求观察的是加热前后溶液颜色变化，不是质量变化。`
- `CHK5_SEM_EXP_20_3_03_020` `explanation` before: `教材资料 反应是 Cr(Ⅲ) 配合物的水合异构变化，不是生成金属铬。`
- `CHK5_SEM_EXP_20_3_03_020` `explanation` after: `教材资料反应是 Cr(Ⅲ) 配合物的水合异构变化，不是生成金属铬。`
- `CHK5_SEM_EXP_20_3_03_021` `explanation` before: `教材资料 要求加热 Cr(NO₃)₃ 溶液并观察颜色变化；方程式显示内界由六水合形式转为五水一硝酸根形式。`
- `CHK5_SEM_EXP_20_3_03_021` `explanation` after: `教材步骤要求加热 Cr(NO₃)₃ 溶液并观察颜色变化；方程式显示内界由六水合形式转为五水一硝酸根形式。`
- `CHK5_SEM_EXP_20_3_03_024` `explanation` before: `教材资料 明确要求观察加热前后溶液颜色的变化；答案是短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_3_03_024` `explanation` after: `教材资料明确要求观察加热前后溶液颜色的变化；答案是短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_3_03_028` `explanation` before: `教材资料 明确要求观察加热前后溶液颜色的变化；只写操作而无颜色比较，不能支撑水合异构现象观察。`
- `CHK5_SEM_EXP_20_3_03_028` `explanation` after: `教材资料明确要求观察加热前后溶液颜色的变化；只写操作而无颜色比较，不能支撑水合异构现象观察。`

### Follow-Up 20-3-04

- `CHK5_SEM_EXP_20_3_04_001` `explanation` before: `教材资料 规定向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`
- `CHK5_SEM_EXP_20_3_04_001` `explanation` after: `教材资料规定向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`
- `CHK5_SEM_EXP_20_3_04_002` `explanation` before: `教材资料 要求把蓝紫色溶液分至三支试管，其中两支分别加入蒸馏水和丙酮，另一支保留对照。`
- `CHK5_SEM_EXP_20_3_04_002` `explanation` after: `教材步骤要求把蓝紫色溶液分至三支试管，其中两支分别加入蒸馏水和丙酮，另一支保留对照。`
- `CHK5_SEM_EXP_20_3_04_007` `explanation` before: `教材资料 要求把溶液分为三支试管，其中一支原溶液用于对照，便于比较水和丙酮处理后的颜色差异。`
- `CHK5_SEM_EXP_20_3_04_007` `explanation` after: `教材步骤要求把溶液分为三支试管，其中一支原溶液用于对照，便于比较水和丙酮处理后的颜色差异。`
- `CHK5_SEM_EXP_20_3_04_011` `explanation` before: `教材资料 明确要求在两支试管中分别加入蒸馏水和丙酮，对比三支试管颜色差异。`
- `CHK5_SEM_EXP_20_3_04_011` `explanation` after: `教材资料明确要求在两支试管中分别加入蒸馏水和丙酮，对比三支试管颜色差异。`
- `CHK5_SEM_EXP_20_3_04_012` `explanation` before: `教材资料 使用 KSCN 饱和溶液，并在方程式中出现 SCN⁻，说明它是硫氰配体来源。`
- `CHK5_SEM_EXP_20_3_04_012` `explanation` after: `教材资料使用 KSCN 饱和溶液，并在方程式中出现 SCN⁻，说明它是硫氰配体来源。`
- `CHK5_SEM_EXP_20_3_04_019` `explanation` before: `教材资料 初始操作正是向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`
- `CHK5_SEM_EXP_20_3_04_019` `explanation` after: `教材资料初始操作正是向 KSCN 饱和溶液滴加 CoCl₂ 溶液至呈蓝紫色。`
- `CHK5_SEM_EXP_20_3_04_021` `explanation` before: `教材资料 明确把蓝紫色溶液分至三支试管，其中两支分别加水和丙酮，剩余一支用于对照。`
- `CHK5_SEM_EXP_20_3_04_021` `explanation` after: `教材资料明确把蓝紫色溶液分至三支试管，其中两支分别加水和丙酮，剩余一支用于对照。`
- `CHK5_SEM_EXP_20_3_04_024` `options[1].text` before: `用 教材资料 定位加水处理，再用表 20.10 确认水合钴(Ⅱ)配合物为粉红色`
- `CHK5_SEM_EXP_20_3_04_024` `options[1].text` after: `用教材资料定位加水处理，再用表 20.10 确认水合钴(Ⅱ)配合物为粉红色`
- `CHK5_SEM_EXP_20_3_04_024` `explanation` before: `教材资料 说明加水使体系转向 [Co(H₂O)₆]²⁺；表 20.10 明确该水合钴(Ⅱ)配合物呈粉红色。`
- `CHK5_SEM_EXP_20_3_04_024` `explanation` after: `教材资料说明加水使体系转向 [Co(H₂O)₆]²⁺；表 20.10 明确该水合钴(Ⅱ)配合物呈粉红色。`
- `CHK5_SEM_EXP_20_3_04_026` `explanation` before: `教材资料 的设计是三支试管对比；完整记录应把原溶液、加水、加丙酮三个条件下的颜色分开。`
- `CHK5_SEM_EXP_20_3_04_026` `explanation` after: `教材资料的设计是三支试管对比；完整记录应把原溶液、加水、加丙酮三个条件下的颜色分开。`
- `CHK5_SEM_EXP_20_3_04_028` `options[3].text` before: `无法判断，因为 教材资料 没有给出金属元素`
- `CHK5_SEM_EXP_20_3_04_028` `options[3].text` after: `无法判断，因为教材资料没有给出金属元素`
- `CHK5_SEM_EXP_20_3_04_028` `explanation` before: `教材资料 明确使用 CoCl₂ 和 KSCN 生成钴(Ⅱ)配合物；表 20.10 中 Fe(Ⅲ)-硫氰配合物血红色是另一个金属体系，不能套用。`
- `CHK5_SEM_EXP_20_3_04_028` `explanation` after: `教材资料明确使用 CoCl₂ 和 KSCN 生成钴(Ⅱ)配合物；表 20.10 中 Fe(Ⅲ)-硫氰配合物血红色是另一个金属体系，不能套用。`
- `CHK5_SEM_EXP_20_3_04_030` `explanation` before: `教材资料 的目的在于比较三支试管的颜色差异；只记录加丙酮一支会丢失原溶液对照和加水条件。`
- `CHK5_SEM_EXP_20_3_04_030` `explanation` after: `教材资料的目的在于比较三支试管的颜色差异；只记录加丙酮一支会丢失原溶液对照和加水条件。`

### Follow-Up 20-3-05

- `CHK5_SEM_EXP_20_3_05_001` `explanation` before: `教材资料 规定分别向多种金属盐溶液中滴加 6 mol·L⁻¹ NH₃·H₂O 溶液。`
- `CHK5_SEM_EXP_20_3_05_001` `explanation` after: `教材资料规定分别向多种金属盐溶液中滴加 6 mol·L⁻¹ NH₃·H₂O 溶液。`
- `CHK5_SEM_EXP_20_3_05_002` `explanation` before: `教材资料 明确使用 6 mol·L⁻¹ NH₃·H₂O 溶液。`
- `CHK5_SEM_EXP_20_3_05_002` `explanation` after: `教材资料明确使用 6 mol·L⁻¹ NH₃·H₂O 溶液。`
- `CHK5_SEM_EXP_20_3_05_003` `explanation` before: `教材资料 在滴加氨水并观察后继续追问静置一段时间有什么变化，因此要记录后续颜色或沉淀变化。`
- `CHK5_SEM_EXP_20_3_05_003` `explanation` after: `教材资料在滴加氨水并观察后继续追问静置一段时间有什么变化，因此要记录后续颜色或沉淀变化。`
- `CHK5_SEM_EXP_20_3_05_004` `explanation` before: `教材资料 规定静置后继续向各溶液中滴加 2 mol·L⁻¹ NaOH 溶液。`
- `CHK5_SEM_EXP_20_3_05_004` `explanation` after: `教材资料规定静置后继续向各溶液中滴加 2 mol·L⁻¹ NaOH 溶液。`
- `CHK5_SEM_EXP_20_3_05_005` `explanation` before: `教材资料 氨合物实验对象包括 FeCl₃、CoCl₂、NiSO₄ 等金属盐溶液。`
- `CHK5_SEM_EXP_20_3_05_005` `explanation` after: `教材资料氨合物实验对象包括 FeCl₃、CoCl₂、NiSO₄ 等金属盐溶液。`
- `CHK5_SEM_EXP_20_3_05_006` `explanation` before: `相关化学原理 明确 Fe²⁺ 和 Fe³⁺ 的氨合物在水溶液中不能稳定存在，并给出水解生成氢氧化亚铁或氢氧化铁的反应。`
- `CHK5_SEM_EXP_20_3_05_006` `explanation` after: `相关化学原理明确 Fe²⁺ 和 Fe³⁺ 的氨合物在水溶液中不能稳定存在，并给出水解生成氢氧化亚铁或氢氧化铁的反应。`
- `CHK5_SEM_EXP_20_3_05_007` `explanation` before: `相关化学原理 说明钴盐加过量氨水生成 Co(Ⅱ) 氨合物，并在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`
- `CHK5_SEM_EXP_20_3_05_007` `explanation` after: `相关化学原理说明钴盐加过量氨水生成 Co(Ⅱ) 氨合物，并在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`
- `CHK5_SEM_EXP_20_3_05_008` `explanation` before: `相关化学原理 说明镍(Ⅱ)盐加入氨水先生成氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物。`
- `CHK5_SEM_EXP_20_3_05_008` `explanation` after: `相关化学原理说明镍(Ⅱ)盐加入氨水先生成氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物。`
- `CHK5_SEM_EXP_20_3_05_009` `explanation` before: `教材资料 通过继续加 NaOH 比较形成氨合物的能力；若配合物较稳定，自由金属离子浓度低，氢氧化物沉淀倾向会减弱。`
- `CHK5_SEM_EXP_20_3_05_009` `explanation` after: `教材资料通过继续加 NaOH 比较形成氨合物的能力；若配合物较稳定，自由金属离子浓度低，氢氧化物沉淀倾向会减弱。`
- `CHK5_SEM_EXP_20_3_05_010` `explanation` before: `教材资料 最后明确要求总结这些金属离子形成氨合物的能力。`
- `CHK5_SEM_EXP_20_3_05_010` `explanation` after: `教材资料最后明确要求总结这些金属离子形成氨合物的能力。`
- `CHK5_SEM_EXP_20_3_05_011` `explanation` before: `教材资料 明确使用 6 mol·L⁻¹ NH₃·H₂O 处理六种金属盐溶液。`
- `CHK5_SEM_EXP_20_3_05_011` `explanation` after: `教材资料明确使用 6 mol·L⁻¹ NH₃·H₂O 处理六种金属盐溶液。`
- `CHK5_SEM_EXP_20_3_05_012` `explanation` before: `教材资料 把静置和继续滴加 NaOH 放在总结形成氨合物能力之前，说明这些后续现象用于比较判断。`
- `CHK5_SEM_EXP_20_3_05_012` `explanation` after: `教材资料把静置和继续滴加 NaOH 放在总结形成氨合物能力之前，说明这些后续现象用于比较判断。`
- `CHK5_SEM_EXP_20_3_05_013` `explanation` before: `相关化学原理 明确 Fe²⁺、Fe³⁺ 的氨合物可由无水盐与氨气得到，但在水溶液中不可能存在，并会水解生成氢氧化物。`
- `CHK5_SEM_EXP_20_3_05_013` `explanation` after: `相关化学原理明确 Fe²⁺、Fe³⁺ 的氨合物可由无水盐与氨气得到，但在水溶液中不可能存在，并会水解生成氢氧化物。`
- `CHK5_SEM_EXP_20_3_05_014` `explanation` before: `相关化学原理 明确 Co(Ⅱ) 氨合物在空气中可缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`
- `CHK5_SEM_EXP_20_3_05_014` `explanation` after: `相关化学原理明确 Co(Ⅱ) 氨合物在空气中可缓慢氧化为更稳定的 Co(Ⅲ) 氨合物。`
- `CHK5_SEM_EXP_20_3_05_017` `explanation` before: `教材资料 要求观察金属盐溶液加氨水、静置和加 NaOH 后的化学现象，不是钥匙遮光轮廓。`
- `CHK5_SEM_EXP_20_3_05_017` `explanation` after: `教材步骤要求观察金属盐溶液加氨水、静置和加 NaOH 后的化学现象，不是钥匙遮光轮廓。`
- `CHK5_SEM_EXP_20_3_05_018` `explanation` before: `教材资料 要求在静置后继续加 NaOH 并观察现象，用来辅助比较金属离子形成氨合物的能力。`
- `CHK5_SEM_EXP_20_3_05_018` `explanation` after: `教材步骤要求在静置后继续加 NaOH 并观察现象，用来辅助比较金属离子形成氨合物的能力。`
- `CHK5_SEM_EXP_20_3_05_020` `explanation` before: `教材资料 最终要求总结这些金属离子形成氨合物的能力，属于配合物形成能力比较。`
- `CHK5_SEM_EXP_20_3_05_020` `explanation` after: `教材资料最终要求总结这些金属离子形成氨合物的能力，属于配合物形成能力比较。`
- `CHK5_SEM_EXP_20_3_05_021` `explanation` before: `相关化学原理 说明 Fe²⁺、Fe³⁺ 氨合物在水中不能稳定存在，而 Co(Ⅱ)、Ni(Ⅱ) 在过量氨水中可形成相应氨合物。`
- `CHK5_SEM_EXP_20_3_05_021` `explanation` after: `相关化学原理说明 Fe²⁺、Fe³⁺ 氨合物在水中不能稳定存在，而 Co(Ⅱ)、Ni(Ⅱ) 在过量氨水中可形成相应氨合物。`
- `CHK5_SEM_EXP_20_3_05_022` `stem` before: `关于钴盐加入氨水后的变化，哪项有 相关化学原理 支撑？`
- `CHK5_SEM_EXP_20_3_05_022` `stem` after: `关于钴盐加入氨水后的变化，哪项有相关化学原理支撑？`
- `CHK5_SEM_EXP_20_3_05_022` `explanation` before: `相关化学原理 明确钴盐加少量氨水先生成氢氧化钴，过量氨水使沉淀溶解生成土黄色 Co(Ⅱ) 氨合物，并可在空气中氧化。`
- `CHK5_SEM_EXP_20_3_05_022` `explanation` after: `相关化学原理明确钴盐加少量氨水先生成氢氧化钴，过量氨水使沉淀溶解生成土黄色 Co(Ⅱ) 氨合物，并可在空气中氧化。`
- `CHK5_SEM_EXP_20_3_05_023` `explanation` before: `教材资料 在滴加氨水后要求静置并询问有什么变化；答案是短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_3_05_023` `explanation` after: `教材资料在滴加氨水后要求静置并询问有什么变化；答案是短中文词，适合手机端输入。`
- `CHK5_SEM_EXP_20_3_05_024` `options[3].text` before: `NiSO₄ 不在 教材资料 实验对象中`
- `CHK5_SEM_EXP_20_3_05_024` `options[3].text` after: `NiSO₄ 不在教材资料实验对象中`
- `CHK5_SEM_EXP_20_3_05_024` `explanation` before: `相关化学原理 说明镍(Ⅱ)盐加氨水先生成绿色氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物；教材资料 也列出 NiSO₄。`
- `CHK5_SEM_EXP_20_3_05_024` `explanation` after: `相关化学原理说明镍(Ⅱ)盐加氨水先生成绿色氢氧化镍，氨水过量则沉淀溶解，得到蓝色镍氨配合物；教材资料也列出 NiSO₄。`
- `CHK5_SEM_EXP_20_3_05_025` `explanation` before: `教材资料 把加 NaOH 作为后续观察步骤并要求总结形成氨合物能力；是否继续沉淀可帮助判断金属离子是否被氨配位稳定。`
- `CHK5_SEM_EXP_20_3_05_025` `explanation` after: `教材资料把加 NaOH 作为后续观察步骤并要求总结形成氨合物能力；是否继续沉淀可帮助判断金属离子是否被氨配位稳定。`
- `CHK5_SEM_EXP_20_3_05_026` `explanation` before: `相关化学原理 说明铁氨合物在水中不稳定，可水解生成氢氧化亚铁或氢氧化铁；答案是短中文词，避免公式输入。`
- `CHK5_SEM_EXP_20_3_05_026` `explanation` after: `相关化学原理说明铁氨合物在水中不稳定，可水解生成氢氧化亚铁或氢氧化铁；答案是短中文词，避免公式输入。`
- `CHK5_SEM_EXP_20_3_05_027` `explanation` before: `相关化学原理 说明 Co(Ⅱ) 氨合物在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物，而镍氨配合物比较稳定、空气中不会被氧化。`
- `CHK5_SEM_EXP_20_3_05_027` `explanation` after: `相关化学原理说明 Co(Ⅱ) 氨合物在空气中缓慢氧化为更稳定的 Co(Ⅲ) 氨合物，而镍氨配合物比较稳定、空气中不会被氧化。`
- `CHK5_SEM_EXP_20_3_05_028` `explanation` before: `教材资料 要求总结金属离子形成氨合物的能力，Ni²⁺ 与过量氨水形成镍氨配合物正体现这一点。`
- `CHK5_SEM_EXP_20_3_05_028` `explanation` after: `教材步骤要求总结金属离子形成氨合物的能力，Ni²⁺ 与过量氨水形成镍氨配合物正体现这一点。`
- `CHK5_SEM_EXP_20_3_05_030` `explanation` before: `教材资料 最终要求总结这些金属离子形成氨合物的能力；答案为短中文词。`
- `CHK5_SEM_EXP_20_3_05_030` `explanation` after: `教材资料最终要求总结这些金属离子形成氨合物的能力；答案为短中文词。`

### Follow-Up 20-3-06

- `CHK5_SEM_EXP_20_3_06_001` `explanation` before: `教材资料 给出 KI、CCl₄ 和 FeCl₃ 的对照体系；相关化学原理 明确 Fe³⁺ 能把 I⁻ 氧化为 I₂，CCl₄ 层用于观察碘。`
- `CHK5_SEM_EXP_20_3_06_001` `explanation` after: `教材资料给出 KI、CCl₄ 和 FeCl₃ 的对照体系；相关化学原理明确 Fe³⁺ 能把 I⁻ 氧化为 I₂，CCl₄ 层用于观察碘。`
- `CHK5_SEM_EXP_20_3_06_002` `explanation` before: `教材资料 要求比较先加 NaF 再加 FeCl₃ 的现象；table 支持 F⁻ 可与 Fe³⁺ 形成配合物。`
- `CHK5_SEM_EXP_20_3_06_002` `explanation` after: `教材步骤要求比较先加 NaF 再加 FeCl₃ 的现象；表格资料支持 F⁻ 可与 Fe³⁺ 形成配合物。`
- `CHK5_SEM_EXP_20_3_06_003` `explanation` before: `F⁻ 配合 Fe³⁺ 会降低游离 Fe³⁺ 的氧化干扰；教材资料 要求比较先加 NaF 时现象的不同。`
- `CHK5_SEM_EXP_20_3_06_003` `explanation` after: `F⁻ 配合 Fe³⁺ 会降低游离 Fe³⁺ 的氧化干扰；教材步骤要求比较先加 NaF 时现象的不同。`
- `CHK5_SEM_EXP_20_3_06_004` `explanation` before: `教材资料 把 KI 与 CCl₄ 混合后再加 FeCl₃；结合 Fe³⁺ 氧化 I⁻ 生成 I₂，可知 CCl₄ 用于有机层显色观察。`
- `CHK5_SEM_EXP_20_3_06_004` `explanation` after: `教材资料把 KI 与 CCl₄ 混合后再加 FeCl₃；结合 Fe³⁺ 氧化 I⁻ 生成 I₂，可知 CCl₄ 用于有机层显色观察。`
- `CHK5_SEM_EXP_20_3_06_005` `explanation` before: `教材资料 要求比较有 EDTA 与无 EDTA 时 Fe(Ⅱ) 溶液和 AgNO₃ 的反应；思考题把该比较指向利用配合物性质回收银。`
- `CHK5_SEM_EXP_20_3_06_005` `explanation` after: `教材步骤要求比较有 EDTA 与无 EDTA 时 Fe(Ⅱ) 溶液和 AgNO₃ 的反应；思考题把该比较指向利用配合物性质回收银。`
- `CHK5_SEM_EXP_20_3_06_008` `explanation` before: `教材资料 依次安排 KI/CCl₄/FeCl₃ 与 Fe(Ⅱ)/AgNO₃/EDTA 两组对比。`
- `CHK5_SEM_EXP_20_3_06_008` `explanation` after: `教材资料依次安排 KI/CCl₄/FeCl₃ 与 Fe(Ⅱ)/AgNO₃/EDTA 两组对比。`
- `CHK5_SEM_EXP_20_3_06_011` `explanation` before: `教材资料 给出该体系；相关化学原理 说明 Fe³⁺ 可氧化 I⁻ 为 I₂。`
- `CHK5_SEM_EXP_20_3_06_011` `explanation` after: `教材资料给出该体系；相关化学原理说明 Fe³⁺ 可氧化 I⁻ 为 I₂。`
- `CHK5_SEM_EXP_20_3_06_012` `explanation` before: `教材资料 要求比较先加 NaF 的差异；table 支持 F⁻ 与 Fe³⁺ 配合。`
- `CHK5_SEM_EXP_20_3_06_012` `explanation` after: `教材步骤要求比较先加 NaF 的差异；表格资料支持 F⁻ 与 Fe³⁺ 配合。`
- `CHK5_SEM_EXP_20_3_06_014` `explanation` before: `教材资料 要求比较有无 EDTA 下 Fe(Ⅱ) 与 AgNO₃ 的反应；思考题将该现象联系到用配合物性质回收银。`
- `CHK5_SEM_EXP_20_3_06_014` `explanation` after: `教材步骤要求比较有无 EDTA 下 Fe(Ⅱ) 与 AgNO₃ 的反应；思考题将该现象联系到用配合物性质回收银。`
- `CHK5_SEM_EXP_20_3_06_017` `explanation` before: `教材资料 明确 Fe(Ⅱ) 溶液与 AgNO₃ 溶液反应，AgNO₃ 提供 Ag⁺。`
- `CHK5_SEM_EXP_20_3_06_017` `explanation` after: `教材资料明确 Fe(Ⅱ) 溶液与 AgNO₃ 溶液反应，AgNO₃ 提供 Ag⁺。`
- `CHK5_SEM_EXP_20_3_06_021` `explanation` before: `相关化学原理 明确 Fe³⁺ 可以氧化 I⁻ 生成 I₂；教材资料 用 CCl₄ 层观察该变化。`
- `CHK5_SEM_EXP_20_3_06_021` `explanation` after: `相关化学原理明确 Fe³⁺ 可以氧化 I⁻ 生成 I₂；教材资料用 CCl₄ 层观察该变化。`
- `CHK5_SEM_EXP_20_3_06_022` `explanation` before: `教材资料 要求先加少量 NaF 后再加 FeCl₃ 并比较现象；table 支持 F⁻ 可配合 Fe³⁺。`
- `CHK5_SEM_EXP_20_3_06_022` `explanation` after: `教材步骤要求先加少量 NaF 后再加 FeCl₃ 并比较现象；表格资料支持 F⁻ 可配合 Fe³⁺。`
- `CHK5_SEM_EXP_20_3_06_023` `explanation` before: `教材资料 把 CCl₄ 放在 KI/FeCl₃ 观察体系中；其作用是有机层萃取碘，方便比较颜色。`
- `CHK5_SEM_EXP_20_3_06_023` `explanation` after: `教材资料把 CCl₄ 放在 KI/FeCl₃ 观察体系中；其作用是有机层萃取碘，方便比较颜色。`
- `CHK5_SEM_EXP_20_3_06_024` `explanation` before: `教材资料 明确比较 Fe(Ⅱ) 溶液在有无 EDTA 下与 AgNO₃ 溶液的反应。`
- `CHK5_SEM_EXP_20_3_06_024` `explanation` after: `教材资料明确比较 Fe(Ⅱ) 溶液在有无 EDTA 下与 AgNO₃ 溶液的反应。`

### Follow-Up 20-3-07

- `CHK5_SEM_EXP_20_3_07_001` `explanation` before: `教材资料 明确在 Cr₂(SO₄)₃ 溶液中加入少量 Na₂C₂O₄ 固体。`
- `CHK5_SEM_EXP_20_3_07_001` `explanation` after: `教材资料明确在 Cr₂(SO₄)₃ 溶液中加入少量 Na₂C₂O₄ 固体。`
- `CHK5_SEM_EXP_20_3_07_002` `explanation` before: `教材资料 要求在加入 Na₂C₂O₄ 后逐滴加入 2 mol·L⁻¹ NaOH，观察有无沉淀生成。`
- `CHK5_SEM_EXP_20_3_07_002` `explanation` after: `教材步骤要求在加入 Na₂C₂O₄ 后逐滴加入 2 mol·L⁻¹ NaOH，观察有无沉淀生成。`
- `CHK5_SEM_EXP_20_3_07_003` `explanation` before: `相关化学原理 与表格均说明 Fe³⁺ 与硫氰根形成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_003` `explanation` after: `相关化学原理与表格均说明 Fe³⁺ 与硫氰根形成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_004` `explanation` before: `教材资料 把 FeCl₃ + KSCN 显色后再加 Na₂C₂O₄ 放在“配合物稳定性与配体的关系”小节中。`
- `CHK5_SEM_EXP_20_3_07_004` `explanation` after: `教材资料把 FeCl₃ + KSCN 显色后再加 Na₂C₂O₄ 放在“配合物稳定性与配体的关系”小节中。`
- `CHK5_SEM_EXP_20_3_07_005` `explanation` before: `教材资料 明确 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`
- `CHK5_SEM_EXP_20_3_07_005` `explanation` after: `教材资料明确 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`
- `CHK5_SEM_EXP_20_3_07_006` `explanation` before: `教材资料 所在小节比较配合物稳定性与配体的关系；乙二胺是该步骤后加入的配体。`
- `CHK5_SEM_EXP_20_3_07_006` `explanation` after: `教材资料所在小节比较配合物稳定性与配体的关系；乙二胺是该步骤后加入的配体。`
- `CHK5_SEM_EXP_20_3_07_008` `explanation` before: `相关化学原理 说明硫氰根与 Fe³⁺ 可形成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_008` `explanation` after: `相关化学原理说明硫氰根与 Fe³⁺ 可形成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_010` `explanation` before: `A、B、C 都属于 教材资料 的配体稳定性实验；D 是后续金属离子鉴定实验，不属于本实验。`
- `CHK5_SEM_EXP_20_3_07_010` `explanation` after: `A、B、C 都属于教材资料的配体稳定性实验；D 是后续金属离子鉴定实验，不属于本实验。`
- `CHK5_SEM_EXP_20_3_07_011` `explanation` before: `教材资料 明确在 NiSO₄ 加过量氨水后逐滴加入乙二胺溶液继续观察。`
- `CHK5_SEM_EXP_20_3_07_011` `explanation` after: `教材资料明确在 NiSO₄ 加过量氨水后逐滴加入乙二胺溶液继续观察。`
- `CHK5_SEM_EXP_20_3_07_014` `explanation` before: `教材资料 要求 FeCl₃ 加 KSCN 后再加 Na₂C₂O₄ 并观察溶液颜色变化。`
- `CHK5_SEM_EXP_20_3_07_014` `explanation` after: `教材步骤要求 FeCl₃ 加 KSCN 后再加 Na₂C₂O₄ 并观察溶液颜色变化。`
- `CHK5_SEM_EXP_20_3_07_015` `explanation` before: `教材资料 明确该操作顺序。`
- `CHK5_SEM_EXP_20_3_07_015` `explanation` after: `教材资料明确该操作顺序。`
- `CHK5_SEM_EXP_20_3_07_016` `explanation` before: `教材资料 把乙二胺作为 NiSO₄ 过量氨水后的追加试剂，服务于“配合物稳定性与配体的关系”。`
- `CHK5_SEM_EXP_20_3_07_016` `explanation` after: `教材资料把乙二胺作为 NiSO₄ 过量氨水后的追加试剂，服务于“配合物稳定性与配体的关系”。`
- `CHK5_SEM_EXP_20_3_07_017` `explanation` before: `教材资料 三个子步骤分别改变配体或后加试剂，并观察沉淀或颜色变化。`
- `CHK5_SEM_EXP_20_3_07_017` `explanation` after: `教材资料三个子步骤分别改变配体或后加试剂，并观察沉淀或颜色变化。`
- `CHK5_SEM_EXP_20_3_07_020` `explanation` before: `教材资料 本实验 的小节主题是配合物稳定性与配体的关系，而不是金属离子水解作用。`
- `CHK5_SEM_EXP_20_3_07_020` `explanation` after: `教材中本实验的小节主题是配合物稳定性与配体的关系，而不是金属离子水解作用。`
- `CHK5_SEM_EXP_20_3_07_022` `explanation` before: `相关化学原理 明确 Fe³⁺ 与硫氰根生成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_022` `explanation` after: `相关化学原理明确 Fe³⁺ 与硫氰根生成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_023` `explanation` before: `教材资料 明确在 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`
- `CHK5_SEM_EXP_20_3_07_023` `explanation` after: `教材资料明确在 NiSO₄ 加过量 NH₃·H₂O 后逐滴加入 1% 乙二胺溶液。`
- `CHK5_SEM_EXP_20_3_07_024` `explanation` before: `教材资料 明确该步骤是逐滴加入 NaOH，观察有无沉淀生成。`
- `CHK5_SEM_EXP_20_3_07_024` `explanation` after: `教材资料明确该步骤是逐滴加入 NaOH，观察有无沉淀生成。`
- `CHK5_SEM_EXP_20_3_07_025` `explanation` before: `KSCN 提供硫氰根，相关化学原理 说明硫氰根可与 Fe³⁺ 形成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_025` `explanation` after: `KSCN 提供硫氰根，相关化学原理说明硫氰根可与 Fe³⁺ 形成血红色配合物。`
- `CHK5_SEM_EXP_20_3_07_027` `stem` before: `NiSO₄ 加过量氨水后，教材资料 要求再逐滴加入____溶液。`
- `CHK5_SEM_EXP_20_3_07_027` `stem` after: `NiSO₄ 加过量氨水后，教材步骤要求再逐滴加入____溶液。`
- `CHK5_SEM_EXP_20_3_07_027` `explanation` before: `教材资料 明确后续逐滴加入 1% 乙二胺溶液，再观察现象。`
- `CHK5_SEM_EXP_20_3_07_027` `explanation` after: `教材资料明确后续逐滴加入 1% 乙二胺溶液，再观察现象。`
- `CHK5_SEM_EXP_20_3_07_029` `explanation` before: `教材资料 的镍体系从 NiSO₄ 溶液开始，NiSO₄ 提供 Ni²⁺。`
- `CHK5_SEM_EXP_20_3_07_029` `explanation` after: `教材资料的镍体系从 NiSO₄ 溶液开始，NiSO₄ 提供 Ni²⁺。`
- `CHK5_SEM_EXP_20_3_07_030` `explanation` before: `教材资料 明确加入少量 Na₂C₂O₄ 后观察溶液颜色变化。`
- `CHK5_SEM_EXP_20_3_07_030` `explanation` after: `教材资料明确加入少量 Na₂C₂O₄ 后观察溶液颜色变化。`

### Follow-Up 20-3-08

- `CHK5_SEM_EXP_20_3_08_001` `explanation` before: `教材资料 明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_001` `explanation` after: `教材资料明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_002` `explanation` before: `相关化学原理 明确硫氰根离子与 Fe³⁺ 可生成血红色配合物，可用于鉴定 Fe³⁺。`
- `CHK5_SEM_EXP_20_3_08_002` `explanation` after: `相关化学原理明确硫氰根离子与 Fe³⁺ 可生成血红色配合物，可用于鉴定 Fe³⁺。`
- `CHK5_SEM_EXP_20_3_08_004` `explanation` before: `相关化学原理 明确 Fe²⁺ 与铁氰化物体系生成滕氏蓝的蓝色沉淀，是鉴定 Fe²⁺ 的灵敏反应。`
- `CHK5_SEM_EXP_20_3_08_004` `explanation` after: `相关化学原理明确 Fe²⁺ 与铁氰化物体系生成滕氏蓝的蓝色沉淀，是鉴定 Fe²⁺ 的灵敏反应。`
- `CHK5_SEM_EXP_20_3_08_006` `explanation` before: `教材资料 明确分别进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_006` `explanation` after: `教材资料明确分别进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_011` `explanation` before: `教材资料 明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_011` `explanation` after: `教材资料明确要求进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_013` `explanation` before: `相关化学原理 明确该配合物为血红色，可用于 Fe³⁺ 鉴定。`
- `CHK5_SEM_EXP_20_3_08_013` `explanation` after: `相关化学原理明确该配合物为血红色，可用于 Fe³⁺ 鉴定。`
- `CHK5_SEM_EXP_20_3_08_017` `explanation` before: `教材资料 要求鉴定 Fe(Ⅱ) 和 Fe(Ⅲ)，因此记录必须体现价态和对应阳性现象。`
- `CHK5_SEM_EXP_20_3_08_017` `explanation` after: `教材步骤要求鉴定 Fe(Ⅱ) 和 Fe(Ⅲ)，因此记录必须体现价态和对应阳性现象。`
- `CHK5_SEM_EXP_20_3_08_021` `explanation` before: `教材资料 明确进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_021` `explanation` after: `教材资料明确进行铁(Ⅱ)和铁(Ⅲ)的鉴定。`
- `CHK5_SEM_EXP_20_3_08_024` `explanation` before: `相关化学原理 明确 Fe²⁺ 的铁氰化物鉴定反应生成滕氏蓝的蓝色沉淀。`
- `CHK5_SEM_EXP_20_3_08_024` `explanation` after: `相关化学原理明确 Fe²⁺ 的铁氰化物鉴定反应生成滕氏蓝的蓝色沉淀。`
- `CHK5_SEM_EXP_20_3_08_027` `explanation` before: `教材资料 要求分别鉴定铁(Ⅱ)和铁(Ⅲ)，相关化学原理 也给出不同阳性反应。`
- `CHK5_SEM_EXP_20_3_08_027` `explanation` after: `教材步骤要求分别鉴定铁(Ⅱ)和铁(Ⅲ)，相关化学原理也给出不同阳性反应。`

### Follow-Up 20-3-09

- `CHK5_SEM_EXP_20_3_09_011` `explanation` before: `这正是 教材资料 给出的钴(Ⅱ)鉴定操作。`
- `CHK5_SEM_EXP_20_3_09_011` `explanation` after: `这正是教材资料给出的钴(Ⅱ)鉴定操作。`

### Follow-Up 20-3-10

- `CHK5_SEM_EXP_20_3_10_007` `explanation` before: `教材资料 文字说明 H₂dmg 表示丁二酮肟。`
- `CHK5_SEM_EXP_20_3_10_007` `explanation` after: `教材资料文字说明 H₂dmg 表示丁二酮肟。`
- `CHK5_SEM_EXP_20_3_10_013` `explanation` before: `教材资料 文字说明 H₂dmg 表示丁二酮肟。`
- `CHK5_SEM_EXP_20_3_10_013` `explanation` after: `教材资料文字说明 H₂dmg 表示丁二酮肟。`
- `CHK5_SEM_EXP_20_3_10_027` `explanation` before: `教材资料 文字说明 H₂dmg 表示丁二酮肟。`
- `CHK5_SEM_EXP_20_3_10_027` `explanation` after: `教材资料文字说明 H₂dmg 表示丁二酮肟。`

### Follow-Up 20-3-13

- `CHK5_SEM_EXP_20_3_13_029` `explanation` before: `教材要求先用 H₂SO₄ 酸化 NH₄VO₃，再加入 H₂O₂；跳过酸化不符合 教材资料 流程。`
- `CHK5_SEM_EXP_20_3_13_029` `explanation` after: `教材要求先用 H₂SO₄ 酸化 NH₄VO₃，再加入 H₂O₂；跳过酸化不符合教材资料流程。`


## Final Validation After Readability Follow-Up

- Student-visible internal review/rebuild traces: `0`.
- Student-visible ASCII digit-subscript formulas: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax: `0`.
- JSON parse: passed.
- Total questions: `510`; each packet question count: `30`.
- Type totals: `321` single choice, `154` true/false, `35` fill blank.
- RAG evidence ids checked: `57`; missing: `0`.
- Validation errors: `0`.
