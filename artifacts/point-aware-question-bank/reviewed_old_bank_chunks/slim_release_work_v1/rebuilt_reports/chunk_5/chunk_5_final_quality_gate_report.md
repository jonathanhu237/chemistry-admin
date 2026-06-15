# chunk_5 Final Quality Gate Report

## Scope

- Rebuilt package directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5`.
- Reports directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_5`.
- Full-chunk scan covered all 17 rebuilt packages, not only prompt examples.
- Student-visible fields checked: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- Diagnostic fields checked: `option_links[].diagnostic_note`.
- RAG source check for known raw-id items: `textbook_prose_01156_e3d54318a3`, `textbook_prose_01157_702c31a997`, and `textbook_prose_01179_863cead3f0` were read from `textbook_inorganic_lower_chunks_v1.jsonl`; `expchunk_00319_b995aa9123` and `expchunk_00322_6c10a1661c` were read from `textbook_experiment_chunks_v1.jsonl`.

## Counts

- Total questions in chunk_5: `510`.
- Modified question count: `95`.
- Modified packet count: `8`.
- Raw id/backtick visible hits fixed: `2`; remaining `0`.
- Visible spacing/review-wording hits fixed: `16`; remaining `0`.
- Visible internal process-word hits fixed: `0`; remaining `0`.
- Diagnostic-note internal process hits fixed: `126`; remaining `0`.
- Visible fields changed by explicit reviewed replacements: `21`.
- Diagnostic-note fields changed: `150`.

## Modified Question IDs

- `20-2-08`: `CHK5_SEM_EXP_20_2_08_001`, `CHK5_SEM_EXP_20_2_08_002`, `CHK5_SEM_EXP_20_2_08_003`, `CHK5_SEM_EXP_20_2_08_004`, `CHK5_SEM_EXP_20_2_08_005`, `CHK5_SEM_EXP_20_2_08_006`, `CHK5_SEM_EXP_20_2_08_007`, `CHK5_SEM_EXP_20_2_08_008`, `CHK5_SEM_EXP_20_2_08_009`, `CHK5_SEM_EXP_20_2_08_010`, `CHK5_SEM_EXP_20_2_08_011`, `CHK5_SEM_EXP_20_2_08_012`, `CHK5_SEM_EXP_20_2_08_013`, `CHK5_SEM_EXP_20_2_08_014`, `CHK5_SEM_EXP_20_2_08_020`, `CHK5_SEM_EXP_20_2_08_021`, `CHK5_SEM_EXP_20_2_08_022`, `CHK5_SEM_EXP_20_2_08_025`, `CHK5_SEM_EXP_20_2_08_029`
- `20-2-09`: `CHK5_SEM_EXP_20_2_09_001`, `CHK5_SEM_EXP_20_2_09_002`, `CHK5_SEM_EXP_20_2_09_003`, `CHK5_SEM_EXP_20_2_09_004`, `CHK5_SEM_EXP_20_2_09_005`, `CHK5_SEM_EXP_20_2_09_006`, `CHK5_SEM_EXP_20_2_09_007`, `CHK5_SEM_EXP_20_2_09_008`, `CHK5_SEM_EXP_20_2_09_009`, `CHK5_SEM_EXP_20_2_09_011`, `CHK5_SEM_EXP_20_2_09_019`, `CHK5_SEM_EXP_20_2_09_020`, `CHK5_SEM_EXP_20_2_09_021`, `CHK5_SEM_EXP_20_2_09_024`, `CHK5_SEM_EXP_20_2_09_026`, `CHK5_SEM_EXP_20_2_09_028`, `CHK5_SEM_EXP_20_2_09_029`
- `20-2-10`: `CHK5_SEM_EXP_20_2_10_001`, `CHK5_SEM_EXP_20_2_10_004`, `CHK5_SEM_EXP_20_2_10_005`, `CHK5_SEM_EXP_20_2_10_008`, `CHK5_SEM_EXP_20_2_10_021`, `CHK5_SEM_EXP_20_2_10_022`, `CHK5_SEM_EXP_20_2_10_024`, `CHK5_SEM_EXP_20_2_10_025`
- `20-3-01`: `CHK5_SEM_EXP_20_3_01_001`, `CHK5_SEM_EXP_20_3_01_002`, `CHK5_SEM_EXP_20_3_01_007`, `CHK5_SEM_EXP_20_3_01_008`, `CHK5_SEM_EXP_20_3_01_009`, `CHK5_SEM_EXP_20_3_01_010`, `CHK5_SEM_EXP_20_3_01_021`, `CHK5_SEM_EXP_20_3_01_022`, `CHK5_SEM_EXP_20_3_01_025`, `CHK5_SEM_EXP_20_3_01_027`, `CHK5_SEM_EXP_20_3_01_028`
- `20-3-02`: `CHK5_SEM_EXP_20_3_02_001`, `CHK5_SEM_EXP_20_3_02_002`, `CHK5_SEM_EXP_20_3_02_003`, `CHK5_SEM_EXP_20_3_02_005`, `CHK5_SEM_EXP_20_3_02_006`, `CHK5_SEM_EXP_20_3_02_007`, `CHK5_SEM_EXP_20_3_02_009`, `CHK5_SEM_EXP_20_3_02_010`, `CHK5_SEM_EXP_20_3_02_015`, `CHK5_SEM_EXP_20_3_02_021`, `CHK5_SEM_EXP_20_3_02_022`, `CHK5_SEM_EXP_20_3_02_023`, `CHK5_SEM_EXP_20_3_02_024`, `CHK5_SEM_EXP_20_3_02_025`, `CHK5_SEM_EXP_20_3_02_026`, `CHK5_SEM_EXP_20_3_02_027`, `CHK5_SEM_EXP_20_3_02_028`
- `20-3-03`: `CHK5_SEM_EXP_20_3_03_001`, `CHK5_SEM_EXP_20_3_03_002`, `CHK5_SEM_EXP_20_3_03_003`, `CHK5_SEM_EXP_20_3_03_021`, `CHK5_SEM_EXP_20_3_03_022`, `CHK5_SEM_EXP_20_3_03_026`, `CHK5_SEM_EXP_20_3_03_028`, `CHK5_SEM_EXP_20_3_03_030`
- `20-3-04`: `CHK5_SEM_EXP_20_3_04_001`, `CHK5_SEM_EXP_20_3_04_002`, `CHK5_SEM_EXP_20_3_04_021`, `CHK5_SEM_EXP_20_3_04_022`, `CHK5_SEM_EXP_20_3_04_023`, `CHK5_SEM_EXP_20_3_04_027`, `CHK5_SEM_EXP_20_3_04_028`
- `20-3-05`: `CHK5_SEM_EXP_20_3_05_002`, `CHK5_SEM_EXP_20_3_05_004`, `CHK5_SEM_EXP_20_3_05_005`, `CHK5_SEM_EXP_20_3_05_006`, `CHK5_SEM_EXP_20_3_05_010`, `CHK5_SEM_EXP_20_3_05_022`, `CHK5_SEM_EXP_20_3_05_024`, `CHK5_SEM_EXP_20_3_05_027`

## Answer And Point-Key Changes

- Answer values changed: `0`.
- `question_id` changed: `0`.
- `primary_point_keys` / `secondary_point_keys` changed: `0`.
- `source_audit` evidence ids changed: `0`.
- `option_links` labels / point keys / roles changed: `0`; only `diagnostic_note` wording was changed.
- Release final JSON modified by this pass: `false`; mtime unchanged.

## Field Change Log

### 20-2-08

- `CHK5_SEM_EXP_20_2_08_001` `option_links[0].diagnostic_note` (`A`) before: `A 同时包含 Cr₂(SO₄)₃、Na₂CO₃ 和观察现象，三者合起来才是本 packet 的视频点位。`
- `CHK5_SEM_EXP_20_2_08_001` `option_links[0].diagnostic_note` (`A`) after: `A 同时包含 Cr₂(SO₄)₃、Na₂CO₃ 和观察现象，三者合起来才是本实验的视频点位。`
- `CHK5_SEM_EXP_20_2_08_001` `option_links[1].diagnostic_note` (`B`) before: `B 对应同一 RAG chunk 中的钛(IV)盐水解，不是铬(III)盐水解。`
- `CHK5_SEM_EXP_20_2_08_001` `option_links[1].diagnostic_note` (`B`) after: `B 对应教材同一小节中的钛(Ⅳ)盐水解，不是铬(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_08_001` `option_links[2].diagnostic_note` (`C`) before: `C 对应同一 RAG chunk 中的铁(III)盐水解，试剂和操作都换了。`
- `CHK5_SEM_EXP_20_2_08_001` `option_links[2].diagnostic_note` (`C`) after: `C 对应教材同一小节中的铁(Ⅲ)盐水解，试剂和操作都换了。`
- `CHK5_SEM_EXP_20_2_08_002` `option_links[2].diagnostic_note` (`C`) before: `C 把观察结果与实验对象割裂，不能证明对应铬(III)盐水解。`
- `CHK5_SEM_EXP_20_2_08_002` `option_links[2].diagnostic_note` (`C`) after: `C 把观察结果与实验对象割裂，不能证明对应铬(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_08_002` `option_links[3].diagnostic_note` (`D`) before: `D 把相邻的铁(III)盐水解混入本点位。`
- `CHK5_SEM_EXP_20_2_08_002` `option_links[3].diagnostic_note` (`D`) after: `D 把相邻的铁(Ⅲ)盐水解混入本点位。`
- `CHK5_SEM_EXP_20_2_08_003` `option_links[0].diagnostic_note` (`A`) before: `硝酸盐热分解与本 RAG 步骤无关。`
- `CHK5_SEM_EXP_20_2_08_003` `option_links[0].diagnostic_note` (`A`) after: `硝酸盐热分解与本实验步骤无关。`
- `CHK5_SEM_EXP_20_2_08_003` `option_links[2].diagnostic_note` (`C`) before: `C 与 RAG 小节标题和 Cr(III)盐水解步骤一致。`
- `CHK5_SEM_EXP_20_2_08_003` `option_links[2].diagnostic_note` (`C`) after: `C 与教材小节标题和 Cr(Ⅲ)盐水解步骤一致。`
- `CHK5_SEM_EXP_20_2_08_004` `option_links[1].diagnostic_note` (`B`) before: `B 正确区分 canonical 操作证据与产物判断所需 theory。`
- `CHK5_SEM_EXP_20_2_08_004` `option_links[1].diagnostic_note` (`B`) after: `B 正确区分实验操作依据与产物判断所需相关化学原理。`
- `CHK5_SEM_EXP_20_2_08_004` `option_links[2].diagnostic_note` (`C`) before: `C 是钛(IV)盐水解，不支持铬(III)盐产物判断。`
- `CHK5_SEM_EXP_20_2_08_004` `option_links[2].diagnostic_note` (`C`) after: `C 是钛(Ⅳ)盐水解，不支持铬(Ⅲ)盐产物判断。`
- `CHK5_SEM_EXP_20_2_08_004` `option_links[3].diagnostic_note` (`D`) before: `D 是铁离子鉴定语境，与铬(III)水解沉淀无关。`
- `CHK5_SEM_EXP_20_2_08_004` `option_links[3].diagnostic_note` (`D`) after: `D 是铁离子鉴定语境，与铬(Ⅲ)水解沉淀无关。`
- `CHK5_SEM_EXP_20_2_08_005` `explanation` before: `教材同一小节 中列出了铁、铬、钛三种盐的水解步骤；TiOSO₄ 稀释煮沸是钛(Ⅳ)盐水解，不能替代铬(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_08_005` `explanation` after: `教材同一小节中列出了铁、铬、钛三种盐的水解步骤；TiOSO₄ 稀释煮沸是钛(Ⅳ)盐水解，不能替代铬(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_08_005` `option_links[1].diagnostic_note` (`B`) before: `B 是相邻钛(IV)盐水解内容，不应作为本题直接证据。`
- `CHK5_SEM_EXP_20_2_08_005` `option_links[1].diagnostic_note` (`B`) after: `B 是相邻钛(Ⅳ)盐水解内容，不应作为本题直接证据。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[0].diagnostic_note` (`A`) before: `A 应由 expchunk_00322 支撑，而不是 expchunk_00319。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[0].diagnostic_note` (`A`) after: `A 应由金属离子水解步骤支撑，而不是氢氧化物酸碱性实验。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[1].diagnostic_note` (`B`) before: `B 准确概括 expchunk_00319 的 NaOH 酸碱性测试范围。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[1].diagnostic_note` (`B`) after: `B 准确概括氢氧化物酸碱性实验的 NaOH 酸碱性测试范围。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[2].diagnostic_note` (`C`) before: `C 是 expchunk_00322 中钛(IV)盐水解步骤。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[2].diagnostic_note` (`C`) after: `C 是金属离子水解步骤中钛(Ⅳ)盐水解步骤。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[3].diagnostic_note` (`D`) before: `D 不在这两个 canonical chunk 的本点位范围内。`
- `CHK5_SEM_EXP_20_2_08_006` `option_links[3].diagnostic_note` (`D`) after: `D 不在这两段教材内容对应的本实验范围内。`
- `CHK5_SEM_EXP_20_2_08_007` `option_links[1].diagnostic_note` (`B`) before: `同 chunk 的其他水解步骤不能被这道题自动覆盖。`
- `CHK5_SEM_EXP_20_2_08_007` `option_links[1].diagnostic_note` (`B`) after: `同一小节的其他水解步骤不能被这道题自动覆盖。`
- `CHK5_SEM_EXP_20_2_08_007` `option_links[2].diagnostic_note` (`C`) before: `盐名题不能证明沉淀溶解度，需要额外 theory。`
- `CHK5_SEM_EXP_20_2_08_007` `option_links[2].diagnostic_note` (`C`) after: `盐名题不能证明沉淀溶解度，需要额外相关化学原理。`
- `CHK5_SEM_EXP_20_2_08_008` `option_links[3].diagnostic_note` (`D`) before: `D 把铁离子鉴定误绑定到铬(III)水解。`
- `CHK5_SEM_EXP_20_2_08_008` `option_links[3].diagnostic_note` (`D`) after: `D 把铁离子鉴定误绑定到铬(Ⅲ)水解。`
- `CHK5_SEM_EXP_20_2_08_009` `option_links[0].diagnostic_note` (`A`) before: `A 与源 packet 的唯一视频点位一致。`
- `CHK5_SEM_EXP_20_2_08_009` `option_links[0].diagnostic_note` (`A`) after: `A 与本实验的唯一视频点位一致。`
- `CHK5_SEM_EXP_20_2_08_009` `option_links[1].diagnostic_note` (`B`) before: `B 把同 RAG chunk 的相邻步骤误认为视频点位。`
- `CHK5_SEM_EXP_20_2_08_009` `option_links[1].diagnostic_note` (`B`) after: `B 把教材同一小节的相邻步骤误认为本实验视频点位。`
- `CHK5_SEM_EXP_20_2_08_010` `explanation` before: `本 实验步骤的措辞是“观察现象”，没有在该步骤给出血红色、有机层深蓝色或铬酸根黄色等具体结果。如果问题涉及具体颜色，需要另找匹配证据。`
- `CHK5_SEM_EXP_20_2_08_010` `explanation` after: `本实验步骤的措辞是“观察现象”，没有在该步骤给出血红色、有机层深蓝色或铬酸根黄色等具体结果。如果问题涉及具体颜色，需要另找匹配证据。`
- `CHK5_SEM_EXP_20_2_08_010` `option_links[0].diagnostic_note` (`A`) before: `A 精确反映 RAG 步骤只要求观察。`
- `CHK5_SEM_EXP_20_2_08_010` `option_links[0].diagnostic_note` (`A`) after: `A 精确反映教材步骤只要求观察。`
- `CHK5_SEM_EXP_20_2_08_011` `option_links[0].diagnostic_note` (`A`) before: `A 是 Cr³⁺ 水解的直接 theory locator。`
- `CHK5_SEM_EXP_20_2_08_011` `option_links[0].diagnostic_note` (`A`) after: `A 是 Cr³⁺ 水解的直接相关化学原理依据。`
- `CHK5_SEM_EXP_20_2_08_012` `options[1].text` before: `d-d 跃迁与颜色解释资料 中 d-d 跃迁与颜色解释`
- `CHK5_SEM_EXP_20_2_08_012` `options[1].text` after: `d-d 跃迁与颜色解释资料`
- `CHK5_SEM_EXP_20_2_08_012` `option_links[2].diagnostic_note` (`C`) before: `C 是钛(IV)盐水解，不支撑 Cr(OH)₃。`
- `CHK5_SEM_EXP_20_2_08_012` `option_links[2].diagnostic_note` (`C`) after: `C 是钛(Ⅳ)盐水解，不支撑 Cr(OH)₃。`
- `CHK5_SEM_EXP_20_2_08_013` `explanation` before: `判断正确。这句话与 实验步骤和视频点位标题完全一致。`
- `CHK5_SEM_EXP_20_2_08_013` `explanation` after: `判断正确。这句话与实验步骤和视频点位标题完全一致。`
- `CHK5_SEM_EXP_20_2_08_014` `explanation` before: `判断错误。该 实验步骤只写“观察现象”，未给出具体颜色；涉及颜色或沉淀成分时需要额外匹配证据。`
- `CHK5_SEM_EXP_20_2_08_014` `explanation` after: `判断错误。该实验步骤只写“观察现象”，未给出具体颜色；涉及颜色或沉淀成分时需要额外匹配证据。`
- `CHK5_SEM_EXP_20_2_08_020` `option_links[3].diagnostic_note` (`D`) before: `RAG 已明确写出 Cr₂(SO₄)₃ 和 Na₂CO₃。`
- `CHK5_SEM_EXP_20_2_08_020` `option_links[3].diagnostic_note` (`D`) after: `教材步骤已明确写出 Cr₂(SO₄)₃ 和 Na₂CO₃。`
- `CHK5_SEM_EXP_20_2_08_021` `option_links[2].diagnostic_note` (`C`) before: `C 是钛(IV)盐水解。`
- `CHK5_SEM_EXP_20_2_08_021` `option_links[2].diagnostic_note` (`C`) after: `C 是钛(Ⅳ)盐水解。`
- `CHK5_SEM_EXP_20_2_08_021` `option_links[3].diagnostic_note` (`D`) before: `D 是铁(III)盐水解。`
- `CHK5_SEM_EXP_20_2_08_021` `option_links[3].diagnostic_note` (`D`) after: `D 是铁(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_08_022` `option_links[2].diagnostic_note` (`C`) before: `RAG 没有支持 Na₂CO₃ 将 Cr(III) 自动氧化为 CrO₄²⁻。`
- `CHK5_SEM_EXP_20_2_08_022` `option_links[2].diagnostic_note` (`C`) after: `教材内容不支持 Na₂CO₃ 将 Cr(Ⅲ) 自动氧化为 CrO₄²⁻。`
- `CHK5_SEM_EXP_20_2_08_025` `option_links[0].diagnostic_note` (`A`) before: `id 存在不等于语义支持。`
- `CHK5_SEM_EXP_20_2_08_025` `option_links[0].diagnostic_note` (`A`) after: `资料存在不等于能支撑该判断。`
- `CHK5_SEM_EXP_20_2_08_025` `option_links[2].diagnostic_note` (`C`) before: `必要理论判断可以引用 theory，但必须匹配。`
- `CHK5_SEM_EXP_20_2_08_025` `option_links[2].diagnostic_note` (`C`) after: `必要理论判断可以引用相关化学原理，但必须匹配。`
- `CHK5_SEM_EXP_20_2_08_025` `option_links[3].diagnostic_note` (`D`) before: `option_links 解释选项，不能替代证据源。`
- `CHK5_SEM_EXP_20_2_08_025` `option_links[3].diagnostic_note` (`D`) after: `选项反馈用于解释选项，不能替代教材依据。`
- `CHK5_SEM_EXP_20_2_08_029` `option_links[1].diagnostic_note` (`B`) before: `TiOSO₄ 是钛(IV)盐，不是 Cr₂(SO₄)₃。`
- `CHK5_SEM_EXP_20_2_08_029` `option_links[1].diagnostic_note` (`B`) after: `TiOSO₄ 是钛(Ⅳ)盐，不是 Cr₂(SO₄)₃。`
- `CHK5_SEM_EXP_20_2_08_029` `option_links[3].diagnostic_note` (`D`) before: `RAG 步骤明确出现 Cr₂(SO₄)₃。`
- `CHK5_SEM_EXP_20_2_08_029` `option_links[3].diagnostic_note` (`D`) after: `教材步骤明确出现 Cr₂(SO₄)₃。`

### 20-2-09

- `CHK5_SEM_EXP_20_2_09_001` `option_links[1].diagnostic_note` (`B`) before: `B 完整覆盖 canonical 步骤和视频点位。`
- `CHK5_SEM_EXP_20_2_09_001` `option_links[1].diagnostic_note` (`B`) after: `B 完整覆盖教材步骤和视频点位。`
- `CHK5_SEM_EXP_20_2_09_001` `option_links[2].diagnostic_note` (`C`) before: `C 是同一小节的铁(III)盐水解，不是钛(IV)盐水解。`
- `CHK5_SEM_EXP_20_2_09_001` `option_links[2].diagnostic_note` (`C`) after: `C 是同一小节的铁(Ⅲ)盐水解，不是钛(Ⅳ)盐水解。`
- `CHK5_SEM_EXP_20_2_09_001` `option_links[3].diagnostic_note` (`D`) before: `D 是同一小节的铬(III)盐水解，不是本 packet。`
- `CHK5_SEM_EXP_20_2_09_001` `option_links[3].diagnostic_note` (`D`) after: `D 是同一小节的铬(Ⅲ)盐水解，不是本实验。`
- `CHK5_SEM_EXP_20_2_09_002` `option_links[3].diagnostic_note` (`D`) before: `D 是 canonical 中加水后的下一步。`
- `CHK5_SEM_EXP_20_2_09_002` `option_links[3].diagnostic_note` (`D`) after: `D 是教材步骤中加水后的下一步。`
- `CHK5_SEM_EXP_20_2_09_003` `option_links[0].diagnostic_note` (`A`) before: `A 与 TiOSO₄ 水解 theory chunks 直接对应。`
- `CHK5_SEM_EXP_20_2_09_003` `option_links[0].diagnostic_note` (`A`) after: `A 与 TiOSO₄ 水解相关化学原理直接对应。`
- `CHK5_SEM_EXP_20_2_09_004` `option_links[0].diagnostic_note` (`A`) before: `A 与 theory 中“稀释、加热使 TiOSO₄ 水解”相反。`
- `CHK5_SEM_EXP_20_2_09_004` `option_links[0].diagnostic_note` (`A`) after: `A 与相关化学原理中“稀释、加热使 TiOSO₄ 水解”相反。`
- `CHK5_SEM_EXP_20_2_09_004` `option_links[1].diagnostic_note` (`B`) before: `B 同时符合 canonical 操作和 theory 解释。`
- `CHK5_SEM_EXP_20_2_09_004` `option_links[1].diagnostic_note` (`B`) after: `B 同时符合实验步骤和相关化学原理解释。`
- `CHK5_SEM_EXP_20_2_09_005` `option_links[1].diagnostic_note` (`B`) before: `canonical 和 theory 都没有氯气生成。`
- `CHK5_SEM_EXP_20_2_09_005` `option_links[1].diagnostic_note` (`B`) after: `实验步骤和相关化学原理都没有氯气生成。`
- `CHK5_SEM_EXP_20_2_09_005` `option_links[2].diagnostic_note` (`C`) before: `C 由加热步骤和 TiOSO₄ 水解 theory 共同支撑。`
- `CHK5_SEM_EXP_20_2_09_005` `option_links[2].diagnostic_note` (`C`) after: `C 由加热步骤和 TiOSO₄ 水解相关化学原理共同支撑。`
- `CHK5_SEM_EXP_20_2_09_005` `option_links[3].diagnostic_note` (`D`) before: `theory 指向水解生成固体 H₂TiO₃，而不是溶解所有产物。`
- `CHK5_SEM_EXP_20_2_09_005` `option_links[3].diagnostic_note` (`D`) after: `相关化学原理指向水解生成固体 H₂TiO₃，而不是溶解所有产物。`
- `CHK5_SEM_EXP_20_2_09_006` `option_links[0].diagnostic_note` (`A`) before: `A 是 Ti(IV)盐水解的起始操作。`
- `CHK5_SEM_EXP_20_2_09_006` `option_links[0].diagnostic_note` (`A`) after: `A 是 Ti(Ⅳ)盐水解的起始操作。`
- `CHK5_SEM_EXP_20_2_09_006` `option_links[3].diagnostic_note` (`D`) before: `D 属于铬(III)盐水解，不应绑定本点位。`
- `CHK5_SEM_EXP_20_2_09_006` `option_links[3].diagnostic_note` (`D`) after: `D 属于铬(Ⅲ)盐水解，不应绑定本点位。`
- `CHK5_SEM_EXP_20_2_09_007` `option_links[2].diagnostic_note` (`C`) before: `生成 H₂TiO₃ 需要 theory 证据，不是试剂名自动证明。`
- `CHK5_SEM_EXP_20_2_09_007` `option_links[2].diagnostic_note` (`C`) after: `生成 H₂TiO₃ 需要相关化学原理支撑，不是试剂名自动证明。`
- `CHK5_SEM_EXP_20_2_09_008` `stem` before: `哪项题目设计最符合 依据明确 原则？`
- `CHK5_SEM_EXP_20_2_09_008` `stem` after: `哪项题目设计最能做到证据明确？`
- `CHK5_SEM_EXP_20_2_09_008` `options[3].text` before: `只看 实验 中继承依据，不读教材内容`
- `CHK5_SEM_EXP_20_2_09_008` `options[3].text` after: `只看原有资料线索，不核对教材内容`
- `CHK5_SEM_EXP_20_2_09_008` `explanation` before: `教材资料支撑操作步骤；产物 H₂TiO₃ 的判断需要TiOSO₄ 水解产物资料和TiO₂ 转化资料。B 明确区分这两类证据。`
- `CHK5_SEM_EXP_20_2_09_008` `explanation` after: `实验步骤支撑操作过程；TiOSO₄ 水解产物资料和 TiO₂ 转化资料支撑 H₂TiO₃ 的产物判断。B 明确区分这两类证据。`
- `CHK5_SEM_EXP_20_2_09_008` `option_links[0].diagnostic_note` (`A`) before: `A 用 canonical 操作证据承载产物方程判断，证据不足。`
- `CHK5_SEM_EXP_20_2_09_008` `option_links[0].diagnostic_note` (`A`) after: `A 只用实验操作依据承载产物方程判断，证据不足。`
- `CHK5_SEM_EXP_20_2_09_008` `option_links[1].diagnostic_note` (`B`) before: `B 正确区分 canonical 和 theory 的职责。`
- `CHK5_SEM_EXP_20_2_09_008` `option_links[1].diagnostic_note` (`B`) after: `B 正确区分实验步骤和相关化学原理的作用边界。`
- `CHK5_SEM_EXP_20_2_09_008` `option_links[3].diagnostic_note` (`D`) before: `inherited id 只是 locator，必须读 RAG 原文。`
- `CHK5_SEM_EXP_20_2_09_008` `option_links[3].diagnostic_note` (`D`) after: `D 只看原有材料而不核对教材原文，容易把不相关材料当作依据。`
- `CHK5_SEM_EXP_20_2_09_009` `option_links[0].diagnostic_note` (`A`) before: `A 控制了 canonical 与 theory 的边界。`
- `CHK5_SEM_EXP_20_2_09_009` `option_links[0].diagnostic_note` (`A`) after: `A 控制了实验步骤和相关化学原理的边界。`
- `CHK5_SEM_EXP_20_2_09_009` `option_links[1].diagnostic_note` (`B`) before: `canonical 没有写红色沉淀。`
- `CHK5_SEM_EXP_20_2_09_009` `option_links[1].diagnostic_note` (`B`) after: `教材步骤没有写红色沉淀。`
- `CHK5_SEM_EXP_20_2_09_011` `option_links[0].diagnostic_note` (`A`) before: `A 与源 packet 的唯一视频点位一致。`
- `CHK5_SEM_EXP_20_2_09_011` `option_links[0].diagnostic_note` (`A`) after: `A 与本实验的唯一视频点位一致。`
- `CHK5_SEM_EXP_20_2_09_011` `option_links[1].diagnostic_note` (`B`) before: `B 把同 RAG chunk 的相邻步骤误绑定为本点位。`
- `CHK5_SEM_EXP_20_2_09_011` `option_links[1].diagnostic_note` (`B`) after: `B 把教材同一小节的相邻步骤误认为本实验点位。`
- `CHK5_SEM_EXP_20_2_09_019` `stem` before: `若需要证明“TiOSO₄ 稀释、加热后水解得到 H₂TiO₃”，应优先使用哪组 教材依据？`
- `CHK5_SEM_EXP_20_2_09_019` `stem` after: `若需要证明“TiOSO₄ 稀释、加热后水解得到 H₂TiO₃”，应优先使用哪组材料支持？`
- `CHK5_SEM_EXP_20_2_09_019` `options[1].text` before: `金属离子水解实验步骤加TiOSO₄ 水解产物资料和TiO₂ 转化资料`
- `CHK5_SEM_EXP_20_2_09_019` `options[1].text` after: `金属离子水解实验步骤，以及 TiOSO₄ 水解产物资料和 TiO₂ 转化资料`
- `CHK5_SEM_EXP_20_2_09_019` `options[3].text` before: `任意存在于教材资料的钛相关 依据 都可`
- `CHK5_SEM_EXP_20_2_09_019` `options[3].text` after: `任意存在于教材资料的钛相关内容都可`
- `CHK5_SEM_EXP_20_2_09_019` `explanation` before: `教材资料支撑实验操作，'01156' 和 '01157' 支撑 TiOSO₄ 水解得到 H₂TiO₃ 的产物判断。只用教材资料不足以证明产物，任意钛相关 依据 也不等于语义支持。`
- `CHK5_SEM_EXP_20_2_09_019` `explanation` after: `实验步骤能支撑操作过程；TiOSO₄ 水解产物资料和 TiO₂ 转化资料能支撑 TiOSO₄ 水解得到 H₂TiO₃ 的产物判断。只用实验步骤不足以证明产物，任意钛相关内容也不等于能支撑该判断。`
- `CHK5_SEM_EXP_20_2_09_019` `option_links[0].diagnostic_note` (`A`) before: `canonical 只写操作和观察，不直接给出 H₂TiO₃。`
- `CHK5_SEM_EXP_20_2_09_019` `option_links[0].diagnostic_note` (`A`) after: `教材步骤只写操作和观察，不直接给出 H₂TiO₃。`
- `CHK5_SEM_EXP_20_2_09_019` `option_links[1].diagnostic_note` (`B`) before: `B 同时覆盖操作证据和产物 theory。`
- `CHK5_SEM_EXP_20_2_09_019` `option_links[1].diagnostic_note` (`B`) after: `B 同时覆盖操作依据和产物相关化学原理。`
- `CHK5_SEM_EXP_20_2_09_019` `option_links[3].diagnostic_note` (`D`) before: `RAG id 存在不等于语义匹配。`
- `CHK5_SEM_EXP_20_2_09_019` `option_links[3].diagnostic_note` (`D`) after: `资料出现不等于能支撑该判断。`
- `CHK5_SEM_EXP_20_2_09_020` `options[1].text` before: `它不是教材资料中的真实 依据`
- `CHK5_SEM_EXP_20_2_09_020` `options[1].text` after: `它不是本实验水解产物判断的直接依据`
- `CHK5_SEM_EXP_20_2_09_020` `explanation` before: `'01179' 与过氧化氢显色有关，可用于钛或过氧化氢比色分析，不是本 TiOSO₄ 稀释煮沸水解的主证据。`
- `CHK5_SEM_EXP_20_2_09_020` `explanation` after: `该资料讨论 TiO²⁺ 与 H₂O₂ 的显色反应，可用于钛或过氧化氢比色分析，不是本 TiOSO₄ 稀释煮沸水解的主证据。`
- `CHK5_SEM_EXP_20_2_09_020` `option_links[1].diagnostic_note` (`B`) before: `01179 是真实 RAG id，但不适合本判断。`
- `CHK5_SEM_EXP_20_2_09_020` `option_links[1].diagnostic_note` (`B`) after: `该资料确实存在，但不适合支撑本判断。`
- `CHK5_SEM_EXP_20_2_09_020` `option_links[2].diagnostic_note` (`C`) before: `FeCl₃ 水解来自 canonical 相邻步骤。`
- `CHK5_SEM_EXP_20_2_09_020` `option_links[2].diagnostic_note` (`C`) after: `FeCl₃ 水解来自教材步骤相邻步骤。`
- `CHK5_SEM_EXP_20_2_09_020` `option_links[3].diagnostic_note` (`D`) before: `Cr₂(SO₄)₃ 与 Na₂CO₃ 是铬(III)盐水解。`
- `CHK5_SEM_EXP_20_2_09_020` `option_links[3].diagnostic_note` (`D`) after: `Cr₂(SO₄)₃ 与 Na₂CO₃ 是铬(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_09_021` `option_links[3].diagnostic_note` (`D`) before: `canonical 已给出 TiOSO₄、蒸馏水、加热煮沸。`
- `CHK5_SEM_EXP_20_2_09_021` `option_links[3].diagnostic_note` (`D`) after: `教材步骤已给出 TiOSO₄、蒸馏水、加热煮沸。`
- `CHK5_SEM_EXP_20_2_09_024` `option_links[0].diagnostic_note` (`A`) before: `A 正确控制了 canonical 和 theory 的分工。`
- `CHK5_SEM_EXP_20_2_09_024` `option_links[0].diagnostic_note` (`A`) after: `A 正确控制了实验步骤和相关化学原理的分工。`
- `CHK5_SEM_EXP_20_2_09_024` `option_links[1].diagnostic_note` (`B`) before: `canonical 没有逐字写白色 H₂TiO₃。`
- `CHK5_SEM_EXP_20_2_09_024` `option_links[1].diagnostic_note` (`B`) after: `教材步骤没有逐字写白色 H₂TiO₃。`
- `CHK5_SEM_EXP_20_2_09_024` `option_links[3].diagnostic_note` (`D`) before: `沉淀题可发布，但需匹配 theory 并保证确定性。`
- `CHK5_SEM_EXP_20_2_09_024` `option_links[3].diagnostic_note` (`D`) after: `沉淀题可发布，但需匹配相关化学原理并保证确定性。`
- `CHK5_SEM_EXP_20_2_09_026` `option_links[0].diagnostic_note` (`A`) before: `A 对应 Fe(III)盐水解。`
- `CHK5_SEM_EXP_20_2_09_026` `option_links[0].diagnostic_note` (`A`) after: `A 对应 Fe(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_09_026` `option_links[2].diagnostic_note` (`C`) before: `C 混入 Cr(III)盐水解。`
- `CHK5_SEM_EXP_20_2_09_026` `option_links[2].diagnostic_note` (`C`) after: `C 混入 Cr(Ⅲ)盐水解。`
- `CHK5_SEM_EXP_20_2_09_028` `option_links[0].diagnostic_note` (`A`) before: `A 列出 canonical 里除取样外的关键步骤。`
- `CHK5_SEM_EXP_20_2_09_028` `option_links[0].diagnostic_note` (`A`) after: `A 列出教材步骤里除取样外的关键步骤。`
- `CHK5_SEM_EXP_20_2_09_028` `option_links[1].diagnostic_note` (`B`) before: `canonical 明确要求加入蒸馏水。`
- `CHK5_SEM_EXP_20_2_09_028` `option_links[1].diagnostic_note` (`B`) after: `教材步骤明确要求加入蒸馏水。`
- `CHK5_SEM_EXP_20_2_09_028` `option_links[3].diagnostic_note` (`D`) before: `canonical 明确要求观察现象。`
- `CHK5_SEM_EXP_20_2_09_028` `option_links[3].diagnostic_note` (`D`) after: `教材步骤明确要求观察现象。`
- `CHK5_SEM_EXP_20_2_09_029` `stem` before: `如果题目要求学生选出本实验的教材资料教材依据，哪项最合适？`
- `CHK5_SEM_EXP_20_2_09_029` `stem` after: `如果题目要求学生选出能直接支撑本实验步骤的教材内容，哪项最合适？`
- `CHK5_SEM_EXP_20_2_09_029` `explanation` before: `金属离子水解实验步骤是实验教材中金属离子水解作用的教材实验步骤，直接包含 TiOSO₄ 加水、煮沸、观察现象的步骤。其他 依据 可作特定相关化学原理背景，但不是本实验步骤的主要依据。`
- `CHK5_SEM_EXP_20_2_09_029` `explanation` after: `金属离子水解实验步骤直接包含 TiOSO₄ 加水、煮沸、观察现象。其他资料可作特定相关化学原理背景，但不是本实验步骤的主要依据。`
- `CHK5_SEM_EXP_20_2_09_029` `option_links[3].diagnostic_note` (`D`) before: `附录记录不能替代 canonical 实验步骤。`
- `CHK5_SEM_EXP_20_2_09_029` `option_links[3].diagnostic_note` (`D`) after: `附录记录不能替代教材实验步骤。`

### 20-2-10

- `CHK5_SEM_EXP_20_2_10_001` `explanation` before: `教材资料小设计实验的任务就是把含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离并检出；其他选项属于不同离子组。`
- `CHK5_SEM_EXP_20_2_10_001` `explanation` after: `教材中的小设计实验要求把含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离并检出；其他选项属于不同离子组。`
- `CHK5_SEM_EXP_20_2_10_001` `option_links[0].diagnostic_note` (`A`) before: `A 逐项对应 canonical 的三种目标离子。`
- `CHK5_SEM_EXP_20_2_10_001` `option_links[0].diagnostic_note` (`A`) after: `A 逐项对应教材步骤的三种目标离子。`
- `CHK5_SEM_EXP_20_2_10_001` `option_links[3].diagnostic_note` (`D`) before: `D 是阴离子组，不是本 packet 的混合阳离子。`
- `CHK5_SEM_EXP_20_2_10_001` `option_links[3].diagnostic_note` (`D`) after: `D 是阴离子组，不是本实验的混合阳离子。`
- `CHK5_SEM_EXP_20_2_10_004` `option_links[0].diagnostic_note` (`A`) before: `MnO₄⁻ 用于锰的检出语境，不是 Cr(III) 的产物。`
- `CHK5_SEM_EXP_20_2_10_004` `option_links[0].diagnostic_note` (`A`) after: `MnO₄⁻ 用于锰的检出语境，不是 Cr(Ⅲ) 的产物。`
- `CHK5_SEM_EXP_20_2_10_004` `option_links[3].diagnostic_note` (`D`) before: `D 符合 Cr(III) 在碱性 H₂O₂ 中氧化为铬酸根的 evidence。`
- `CHK5_SEM_EXP_20_2_10_004` `option_links[3].diagnostic_note` (`D`) after: `D 符合 Cr(Ⅲ) 在碱性 H₂O₂ 中氧化为铬酸根的 evidence。`
- `CHK5_SEM_EXP_20_2_10_005` `option_links[0].diagnostic_note` (`A`) before: `A 对应 Al(III) 在 NH₃/H₂O₂ 条件下形成沉淀的分离路径。`
- `CHK5_SEM_EXP_20_2_10_005` `option_links[0].diagnostic_note` (`A`) after: `A 对应 Al(Ⅲ) 在 NH₃/H₂O₂ 条件下形成沉淀的分离路径。`
- `CHK5_SEM_EXP_20_2_10_005` `option_links[2].diagnostic_note` (`C`) before: `RAG 未支持该条件下 Al(III) 变成金属铝。`
- `CHK5_SEM_EXP_20_2_10_005` `option_links[2].diagnostic_note` (`C`) after: `教材内容未支持该条件下 Al(Ⅲ) 变成金属铝。`
- `CHK5_SEM_EXP_20_2_10_008` `option_links[3].diagnostic_note` (`D`) before: `D 对应 Cr(III) 氧化转化与 Al(III) 沉淀分离的性质差异。`
- `CHK5_SEM_EXP_20_2_10_008` `option_links[3].diagnostic_note` (`D`) after: `D 对应 Cr(Ⅲ) 氧化转化与 Al(Ⅲ) 沉淀分离的性质差异。`
- `CHK5_SEM_EXP_20_2_10_021` `option_links[3].diagnostic_note` (`D`) before: `canonical 已给出三种目标离子。`
- `CHK5_SEM_EXP_20_2_10_021` `option_links[3].diagnostic_note` (`D`) after: `教材步骤已给出三种目标离子。`
- `CHK5_SEM_EXP_20_2_10_022` `option_links[0].diagnostic_note` (`A`) before: `theory 明确支持 Mn²⁺ 与 OH⁻ 生成沉淀。`
- `CHK5_SEM_EXP_20_2_10_022` `option_links[0].diagnostic_note` (`A`) after: `相关化学原理明确支持 Mn²⁺ 与 OH⁻ 生成沉淀。`
- `CHK5_SEM_EXP_20_2_10_022` `option_links[1].diagnostic_note` (`B`) before: `B 符合 Mn(II) 氢氧化物与氧化后续变化。`
- `CHK5_SEM_EXP_20_2_10_022` `option_links[1].diagnostic_note` (`B`) after: `B 符合 Mn(Ⅱ) 氢氧化物与氧化后续变化。`
- `CHK5_SEM_EXP_20_2_10_024` `option_links[1].diagnostic_note` (`B`) before: `B 同时包含目标定位和转化 theory。`
- `CHK5_SEM_EXP_20_2_10_024` `option_links[1].diagnostic_note` (`B`) after: `B 同时包含目标定位和转化相关化学原理。`
- `CHK5_SEM_EXP_20_2_10_024` `option_links[2].diagnostic_note` (`C`) before: `铂配合物顺反异构与本 packet 无关。`
- `CHK5_SEM_EXP_20_2_10_024` `option_links[2].diagnostic_note` (`C`) after: `铂配合物顺反异构与本实验无关。`
- `CHK5_SEM_EXP_20_2_10_025` `option_links[0].diagnostic_note` (`A`) before: `canonical 没有限制不能用碱，前置实验还使用 NaOH。`
- `CHK5_SEM_EXP_20_2_10_025` `option_links[0].diagnostic_note` (`A`) after: `教材步骤没有限制不能用碱，前置实验还使用 NaOH。`
- `CHK5_SEM_EXP_20_2_10_025` `option_links[2].diagnostic_note` (`C`) before: `KSCN 不是 Al(III) 检出依据。`
- `CHK5_SEM_EXP_20_2_10_025` `option_links[2].diagnostic_note` (`C`) after: `KSCN 不是 Al(Ⅲ) 检出依据。`

### 20-3-01

- `CHK5_SEM_EXP_20_3_01_001` `option_links[2].diagnostic_note` (`C`) before: `C 是 canonical 明列的水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_001` `option_links[2].diagnostic_note` (`C`) after: `C 是教材步骤明列的水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_002` `option_links[1].diagnostic_note` (`B`) before: `B 符合 canonical 的两类对象分组。`
- `CHK5_SEM_EXP_20_3_01_002` `option_links[1].diagnostic_note` (`B`) after: `B 符合教材步骤的两类对象分组。`
- `CHK5_SEM_EXP_20_3_01_002` `option_links[2].diagnostic_note` (`C`) before: `C 漏掉本 packet 的水合阳离子观察对象。`
- `CHK5_SEM_EXP_20_3_01_002` `option_links[2].diagnostic_note` (`C`) after: `C 漏掉本实验的水合阳离子观察对象。`
- `CHK5_SEM_EXP_20_3_01_007` `option_links[0].diagnostic_note` (`A`) before: `A 与 Cr(III) 水合络合物颜色证据一致。`
- `CHK5_SEM_EXP_20_3_01_007` `option_links[0].diagnostic_note` (`A`) after: `A 与 Cr(Ⅲ) 水合络合物颜色证据一致。`
- `CHK5_SEM_EXP_20_3_01_008` `option_links[1].diagnostic_note` (`B`) before: `B 由 canonical 水合阳离子列表直接支撑。`
- `CHK5_SEM_EXP_20_3_01_008` `option_links[1].diagnostic_note` (`B`) after: `B 由教材列出的水合阳离子列表直接支撑。`
- `CHK5_SEM_EXP_20_3_01_009` `option_links[2].diagnostic_note` (`C`) before: `C 概括 canonical 实验目的。`
- `CHK5_SEM_EXP_20_3_01_009` `option_links[2].diagnostic_note` (`C`) after: `C 概括教材步骤实验目的。`
- `CHK5_SEM_EXP_20_3_01_010` `option_links[3].diagnostic_note` (`D`) before: `D 三项均为 canonical 水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_010` `option_links[3].diagnostic_note` (`D`) after: `D 三项均为教材列出的水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_021` `option_links[0].diagnostic_note` (`A`) before: `A 与 colored transition-metal ion theory 相反。`
- `CHK5_SEM_EXP_20_3_01_021` `option_links[0].diagnostic_note` (`A`) after: `A 与过渡金属离子显色原理相反。`
- `CHK5_SEM_EXP_20_3_01_021` `option_links[1].diagnostic_note` (`B`) before: `B 概括 theory 的显色原因。`
- `CHK5_SEM_EXP_20_3_01_021` `option_links[1].diagnostic_note` (`B`) after: `B 概括相关化学原理的显色原因。`
- `CHK5_SEM_EXP_20_3_01_021` `option_links[3].diagnostic_note` (`D`) before: `D 与不同氧化态颜色可不同的 theory 不符。`
- `CHK5_SEM_EXP_20_3_01_021` `option_links[3].diagnostic_note` (`D`) after: `D 与不同氧化态颜色可不同的相关化学原理不符。`
- `CHK5_SEM_EXP_20_3_01_022` `option_links[1].diagnostic_note` (`B`) before: `B 符合 canonical 分组和 theory 颜色边界。`
- `CHK5_SEM_EXP_20_3_01_022` `option_links[1].diagnostic_note` (`B`) after: `B 符合教材步骤分组和相关化学原理颜色边界。`
- `CHK5_SEM_EXP_20_3_01_025` `option_links[1].diagnostic_note` (`B`) before: `B 忽略 canonical 已列出 Fe 水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_025` `option_links[1].diagnostic_note` (`B`) after: `B 忽略教材步骤已列出 Fe 水合阳离子。`
- `CHK5_SEM_EXP_20_3_01_027` `option_links[2].diagnostic_note` (`C`) before: `C 符合 canonical 的阴离子分组。`
- `CHK5_SEM_EXP_20_3_01_027` `option_links[2].diagnostic_note` (`C`) after: `C 符合教材步骤的阴离子分组。`
- `CHK5_SEM_EXP_20_3_01_028` `option_links[0].diagnostic_note` (`A`) before: `A 与 canonical 列表相反。`
- `CHK5_SEM_EXP_20_3_01_028` `option_links[0].diagnostic_note` (`A`) after: `A 与教材列表相反。`
- `CHK5_SEM_EXP_20_3_01_028` `option_links[1].diagnostic_note` (`B`) before: `B 由 canonical 原文直接支撑。`
- `CHK5_SEM_EXP_20_3_01_028` `option_links[1].diagnostic_note` (`B`) after: `B 由教材原文直接支撑。`

### 20-3-02

- `CHK5_SEM_EXP_20_3_02_001` `option_links[0].diagnostic_note` (`A`) before: `A 是 canonical 明列阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[0].diagnostic_note` (`A`) after: `A 是教材步骤明列阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[1].diagnostic_note` (`B`) before: `B 属于水合阳离子，不是本 packet 阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[1].diagnostic_note` (`B`) after: `B 属于水合阳离子，不是本实验阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[2].diagnostic_note` (`C`) before: `C 不是 canonical 目标阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[2].diagnostic_note` (`C`) after: `C 不是教材步骤目标阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[3].diagnostic_note` (`D`) before: `D 不是 canonical 目标阴离子。`
- `CHK5_SEM_EXP_20_3_02_001` `option_links[3].diagnostic_note` (`D`) after: `D 不是教材步骤目标阴离子。`
- `CHK5_SEM_EXP_20_3_02_002` `option_links[1].diagnostic_note` (`B`) before: `B 是 theory 明确给出的 CrO₄²⁻ 颜色。`
- `CHK5_SEM_EXP_20_3_02_002` `option_links[1].diagnostic_note` (`B`) after: `B 是相关化学原理明确给出的 CrO₄²⁻ 颜色。`
- `CHK5_SEM_EXP_20_3_02_003` `option_links[1].diagnostic_note` (`B`) before: `B 不是 theory 给出的 MnO₄⁻ 颜色。`
- `CHK5_SEM_EXP_20_3_02_003` `option_links[1].diagnostic_note` (`B`) after: `B 不是相关化学原理给出的 MnO₄⁻ 颜色。`
- `CHK5_SEM_EXP_20_3_02_003` `option_links[2].diagnostic_note` (`C`) before: `C 是 theory 明确给出的 MnO₄⁻ 颜色。`
- `CHK5_SEM_EXP_20_3_02_003` `option_links[2].diagnostic_note` (`C`) after: `C 是相关化学原理明确给出的 MnO₄⁻ 颜色。`
- `CHK5_SEM_EXP_20_3_02_005` `option_links[0].diagnostic_note` (`A`) before: `A 与 canonical 同时列出二者相反。`
- `CHK5_SEM_EXP_20_3_02_005` `option_links[0].diagnostic_note` (`A`) after: `A 与教材步骤同时列出二者相反。`
- `CHK5_SEM_EXP_20_3_02_006` `explanation` before: `CrO₄²⁻、MnO₄⁻、VO₃⁻ 均在 教材阴离子列表中；A 是水合阳离子，C 和 D 不属于本实验阴离子颜色列表。`
- `CHK5_SEM_EXP_20_3_02_006` `explanation` after: `CrO₄²⁻、MnO₄⁻、VO₃⁻ 均在教材阴离子列表中；A 是水合阳离子，C 和 D 不属于本实验阴离子颜色列表。`
- `CHK5_SEM_EXP_20_3_02_006` `option_links[1].diagnostic_note` (`B`) before: `B 三项均为 canonical 阴离子。`
- `CHK5_SEM_EXP_20_3_02_006` `option_links[1].diagnostic_note` (`B`) after: `B 三项均为教材列出的阴离子。`
- `CHK5_SEM_EXP_20_3_02_007` `option_links[2].diagnostic_note` (`C`) before: `C 对应 theory 的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_007` `option_links[2].diagnostic_note` (`C`) after: `C 对应相关化学原理的荷移跃迁。`
- `CHK5_SEM_EXP_20_3_02_009` `option_links[0].diagnostic_note` (`A`) before: `A 符合 canonical 阴离子列表。`
- `CHK5_SEM_EXP_20_3_02_009` `option_links[0].diagnostic_note` (`A`) after: `A 符合教材列出的阴离子列表。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[0].diagnostic_note` (`A`) before: `A 属于本 packet 范围。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[0].diagnostic_note` (`A`) after: `A 属于本实验范围。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[1].diagnostic_note` (`B`) before: `B 属于水合阳离子颜色，不是本 packet 阴离子。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[1].diagnostic_note` (`B`) after: `B 属于水合阳离子颜色，不是本实验阴离子。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[2].diagnostic_note` (`C`) before: `C 属于本 packet 范围。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[2].diagnostic_note` (`C`) after: `C 属于本实验范围。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[3].diagnostic_note` (`D`) before: `D 属于本 packet 范围。`
- `CHK5_SEM_EXP_20_3_02_010` `option_links[3].diagnostic_note` (`D`) after: `D 属于本实验范围。`
- `CHK5_SEM_EXP_20_3_02_015` `option_links[1].diagnostic_note` (`B`) before: `B 是 theory 直接支撑的对应关系。`
- `CHK5_SEM_EXP_20_3_02_015` `option_links[1].diagnostic_note` (`B`) after: `B 是相关化学原理直接支撑的对应关系。`
- `CHK5_SEM_EXP_20_3_02_021` `option_links[1].diagnostic_note` (`B`) before: `B 区分 canonical 归属和颜色证据。`
- `CHK5_SEM_EXP_20_3_02_021` `option_links[1].diagnostic_note` (`B`) after: `B 区分教材步骤归属和颜色证据。`
- `CHK5_SEM_EXP_20_3_02_022` `option_links[3].diagnostic_note` (`D`) before: `D 与 canonical 已列阴离子相反。`
- `CHK5_SEM_EXP_20_3_02_022` `option_links[3].diagnostic_note` (`D`) after: `D 与教材步骤已列阴离子相反。`
- `CHK5_SEM_EXP_20_3_02_023` `explanation` before: `Cr₂O₇²⁻ 位于 教材阴离子列表；其余选项都是水合阳离子。`
- `CHK5_SEM_EXP_20_3_02_023` `explanation` after: `Cr₂O₇²⁻ 位于教材阴离子列表；其余选项都是水合阳离子。`
- `CHK5_SEM_EXP_20_3_02_023` `option_links[1].diagnostic_note` (`B`) before: `B 是 canonical 阴离子。`
- `CHK5_SEM_EXP_20_3_02_023` `option_links[1].diagnostic_note` (`B`) after: `B 是教材列出的阴离子。`
- `CHK5_SEM_EXP_20_3_02_024` `option_links[1].diagnostic_note` (`B`) before: `B 对应 theory 的荷移跃迁解释。`
- `CHK5_SEM_EXP_20_3_02_024` `option_links[1].diagnostic_note` (`B`) after: `B 对应相关化学原理的荷移跃迁解释。`
- `CHK5_SEM_EXP_20_3_02_024` `option_links[3].diagnostic_note` (`D`) before: `D 与 theory 明确的电子跃迁解释相反。`
- `CHK5_SEM_EXP_20_3_02_024` `option_links[3].diagnostic_note` (`D`) after: `D 与相关化学原理明确的电子跃迁解释相反。`
- `CHK5_SEM_EXP_20_3_02_025` `option_links[0].diagnostic_note` (`A`) before: `A 漏掉其他 canonical 阴离子。`
- `CHK5_SEM_EXP_20_3_02_025` `option_links[0].diagnostic_note` (`A`) after: `A 漏掉其他教材列出的阴离子。`
- `CHK5_SEM_EXP_20_3_02_025` `option_links[2].diagnostic_note` (`C`) before: `C 漏掉本 packet 阴离子。`
- `CHK5_SEM_EXP_20_3_02_025` `option_links[2].diagnostic_note` (`C`) after: `C 漏掉本实验阴离子。`
- `CHK5_SEM_EXP_20_3_02_026` `option_links[0].diagnostic_note` (`A`) before: `A 有 theory 支撑。`
- `CHK5_SEM_EXP_20_3_02_026` `option_links[0].diagnostic_note` (`A`) after: `A 有相关化学原理支撑。`
- `CHK5_SEM_EXP_20_3_02_026` `option_links[2].diagnostic_note` (`C`) before: `C 有 theory 支撑。`
- `CHK5_SEM_EXP_20_3_02_026` `option_links[2].diagnostic_note` (`C`) after: `C 有相关化学原理支撑。`
- `CHK5_SEM_EXP_20_3_02_026` `option_links[3].diagnostic_note` (`D`) before: `D 符合 canonical 阴离子列表。`
- `CHK5_SEM_EXP_20_3_02_026` `option_links[3].diagnostic_note` (`D`) after: `D 符合教材列出的阴离子列表。`
- `CHK5_SEM_EXP_20_3_02_027` `option_links[0].diagnostic_note` (`A`) before: `A 与 canonical 列表相反。`
- `CHK5_SEM_EXP_20_3_02_027` `option_links[0].diagnostic_note` (`A`) after: `A 与教材列表相反。`
- `CHK5_SEM_EXP_20_3_02_028` `option_links[0].diagnostic_note` (`A`) before: `A 与 canonical 相反。`
- `CHK5_SEM_EXP_20_3_02_028` `option_links[0].diagnostic_note` (`A`) after: `A 与教材步骤相反。`
- `CHK5_SEM_EXP_20_3_02_028` `option_links[1].diagnostic_note` (`B`) before: `B 由 canonical 直接支撑。`
- `CHK5_SEM_EXP_20_3_02_028` `option_links[1].diagnostic_note` (`B`) after: `B 由教材步骤直接支撑。`

### 20-3-03

- `CHK5_SEM_EXP_20_3_03_001` `option_links[2].diagnostic_note` (`C`) before: `C 对应 canonical 标题和试剂。`
- `CHK5_SEM_EXP_20_3_03_001` `option_links[2].diagnostic_note` (`C`) after: `C 对应教材步骤标题和试剂。`
- `CHK5_SEM_EXP_20_3_03_002` `option_links[3].diagnostic_note` (`D`) before: `D 是 canonical 指定溶液。`
- `CHK5_SEM_EXP_20_3_03_002` `option_links[3].diagnostic_note` (`D`) after: `D 是教材步骤指定溶液。`
- `CHK5_SEM_EXP_20_3_03_003` `option_links[0].diagnostic_note` (`A`) before: `A 是 canonical 操作。`
- `CHK5_SEM_EXP_20_3_03_003` `option_links[0].diagnostic_note` (`A`) after: `A 是教材步骤操作。`
- `CHK5_SEM_EXP_20_3_03_021` `option_links[0].diagnostic_note` (`A`) before: `A 漏掉 canonical 的颜色比较。`
- `CHK5_SEM_EXP_20_3_03_021` `option_links[0].diagnostic_note` (`A`) after: `A 漏掉教材步骤的颜色比较。`
- `CHK5_SEM_EXP_20_3_03_022` `option_links[1].diagnostic_note` (`B`) before: `B 是 canonical 操作目的。`
- `CHK5_SEM_EXP_20_3_03_022` `option_links[1].diagnostic_note` (`B`) after: `B 是教材步骤操作目的。`
- `CHK5_SEM_EXP_20_3_03_026` `stem` before: `下列哪一项最准确概括 教材方程式的方向信息？`
- `CHK5_SEM_EXP_20_3_03_026` `stem` after: `下列哪一项最准确概括教材方程式的方向信息？`
- `CHK5_SEM_EXP_20_3_03_028` `option_links[0].diagnostic_note` (`A`) before: `A 对应 canonical 的观察重点。`
- `CHK5_SEM_EXP_20_3_03_028` `option_links[0].diagnostic_note` (`A`) after: `A 对应教材步骤的观察重点。`
- `CHK5_SEM_EXP_20_3_03_030` `option_links[2].diagnostic_note` (`C`) before: `C 与 canonical 方程式不符。`
- `CHK5_SEM_EXP_20_3_03_030` `option_links[2].diagnostic_note` (`C`) after: `C 与教材步骤方程式不符。`

### 20-3-04

- `CHK5_SEM_EXP_20_3_04_001` `option_links[0].diagnostic_note` (`A`) before: `A 是 canonical 指定的饱和溶液。`
- `CHK5_SEM_EXP_20_3_04_001` `option_links[0].diagnostic_note` (`A`) after: `A 是教材步骤指定的饱和溶液。`
- `CHK5_SEM_EXP_20_3_04_002` `option_links[1].diagnostic_note` (`B`) before: `B 对应 canonical 的两支处理。`
- `CHK5_SEM_EXP_20_3_04_002` `option_links[1].diagnostic_note` (`B`) after: `B 对应教材步骤的两支处理。`
- `CHK5_SEM_EXP_20_3_04_021` `option_links[1].diagnostic_note` (`B`) before: `B 符合 canonical 三试管设计。`
- `CHK5_SEM_EXP_20_3_04_021` `option_links[1].diagnostic_note` (`B`) after: `B 符合教材步骤三试管设计。`
- `CHK5_SEM_EXP_20_3_04_022` `option_links[2].diagnostic_note` (`C`) before: `C 不是 canonical 处理。`
- `CHK5_SEM_EXP_20_3_04_022` `option_links[2].diagnostic_note` (`C`) after: `C 不是教材步骤处理。`
- `CHK5_SEM_EXP_20_3_04_023` `option_links[3].diagnostic_note` (`D`) before: `D 不是 canonical 处理。`
- `CHK5_SEM_EXP_20_3_04_023` `option_links[3].diagnostic_note` (`D`) after: `D 不是教材步骤处理。`
- `CHK5_SEM_EXP_20_3_04_027` `explanation` before: `[Co(H₂O)₆]²⁺ 是 教材方程式中的水合钴(Ⅱ)配合物，式中右下角六表示六个水配体。`
- `CHK5_SEM_EXP_20_3_04_027` `explanation` after: `[Co(H₂O)₆]²⁺ 是教材方程式中的水合钴(Ⅱ)配合物，式中右下角六表示六个水配体。`
- `CHK5_SEM_EXP_20_3_04_028` `option_links[3].diagnostic_note` (`D`) before: `D 忽略 canonical 的 CoCl₂。`
- `CHK5_SEM_EXP_20_3_04_028` `option_links[3].diagnostic_note` (`D`) after: `D 忽略教材步骤的 CoCl₂。`

### 20-3-05

- `CHK5_SEM_EXP_20_3_05_002` `option_links[0].diagnostic_note` (`A`) before: `A 与 canonical 浓度不符。`
- `CHK5_SEM_EXP_20_3_05_002` `option_links[0].diagnostic_note` (`A`) after: `A 与教材步骤浓度不符。`
- `CHK5_SEM_EXP_20_3_05_002` `option_links[1].diagnostic_note` (`B`) before: `B 与 canonical 浓度不符。`
- `CHK5_SEM_EXP_20_3_05_002` `option_links[1].diagnostic_note` (`B`) after: `B 与教材步骤浓度不符。`
- `CHK5_SEM_EXP_20_3_05_002` `option_links[3].diagnostic_note` (`D`) before: `D 是 NH₃·H₂O 的 canonical 浓度。`
- `CHK5_SEM_EXP_20_3_05_002` `option_links[3].diagnostic_note` (`D`) after: `D 是 NH₃·H₂O 的教材步骤浓度。`
- `CHK5_SEM_EXP_20_3_05_004` `option_links[1].diagnostic_note` (`B`) before: `B 是 canonical 后续强碱。`
- `CHK5_SEM_EXP_20_3_05_004` `option_links[1].diagnostic_note` (`B`) after: `B 是教材步骤后续强碱。`
- `CHK5_SEM_EXP_20_3_05_005` `option_links[2].diagnostic_note` (`C`) before: `C 三项均在 canonical 对象中。`
- `CHK5_SEM_EXP_20_3_05_005` `option_links[2].diagnostic_note` (`C`) after: `C 三项均在教材步骤对象中。`
- `CHK5_SEM_EXP_20_3_05_006` `option_links[1].diagnostic_note` (`B`) before: `B 与水溶液中不稳定的 theory 相反。`
- `CHK5_SEM_EXP_20_3_05_006` `option_links[1].diagnostic_note` (`B`) after: `B 与水溶液中不稳定的相关化学原理相反。`
- `CHK5_SEM_EXP_20_3_05_010` `option_links[3].diagnostic_note` (`D`) before: `D 直接对应 canonical 总结要求。`
- `CHK5_SEM_EXP_20_3_05_010` `option_links[3].diagnostic_note` (`D`) after: `D 直接对应教材步骤总结要求。`
- `CHK5_SEM_EXP_20_3_05_022` `option_links[1].diagnostic_note` (`B`) before: `B 对应 theory 的钴盐氨水变化。`
- `CHK5_SEM_EXP_20_3_05_022` `option_links[1].diagnostic_note` (`B`) after: `B 对应相关化学原理的钴盐氨水变化。`
- `CHK5_SEM_EXP_20_3_05_024` `option_links[1].diagnostic_note` (`B`) before: `B 对应 Ni²⁺ 氨水 theory。`
- `CHK5_SEM_EXP_20_3_05_024` `option_links[1].diagnostic_note` (`B`) after: `B 对应 Ni²⁺ 氨水相关化学原理。`
- `CHK5_SEM_EXP_20_3_05_024` `option_links[3].diagnostic_note` (`D`) before: `D 与 canonical NiSO₄ 列表相反。`
- `CHK5_SEM_EXP_20_3_05_024` `option_links[3].diagnostic_note` (`D`) after: `D 与教材步骤 NiSO₄ 列表相反。`
- `CHK5_SEM_EXP_20_3_05_027` `option_links[3].diagnostic_note` (`D`) before: `D 与 canonical 静置观察要求相反。`
- `CHK5_SEM_EXP_20_3_05_027` `option_links[3].diagnostic_note` (`D`) after: `D 与教材步骤静置观察要求相反。`


## Final Validation

- JSON parse: `passed`.
- Total rebuilt package files: `17`.
- Total questions: `510`.
- Each packet question count: `30`.
- Type totals: `321` single_choice / `154` true_false / `35` fill_blank.
- Single-choice answer/options/option_links: `passed`.
- Fill-blank accepted answers: `passed`.
- RAG evidence ids checked: `57`; missing: `0`.
- Student-visible raw id/backtick hits: `0`.
- Student-visible internal process-word hits: `0`.
- Student-visible abnormal Chinese spacing hits: `0`.
- Diagnostic-note internal process-word hits: `0`.
- Diagnostic-note raw id/backtick hits: `0`.
- Student-visible ASCII digit-subscript formula hits: `0`.
- Student-visible ASCII charge/ion/ASCII valence hits: `0`.
- Student-visible caret / LaTeX / Markdown chemistry hits: `0`.
- Validation errors: `0`.

## Diagnostic Raw-ID Spot-Check Addendum

- Spot-check found two diagnostic notes with bare `01179`; both were rewritten to the student-facing description `钛(Ⅳ)过氧化氢鉴定资料`.
- `CHK5_SEM_EXP_20_2_09_019` `C` before: `01179 是 TiO²⁺ 与 H₂O₂ 显色，不是本水解产物主证据。`
- `CHK5_SEM_EXP_20_2_09_019` `C` after: `钛(Ⅳ)过氧化氢鉴定资料讨论 TiO²⁺ 与 H₂O₂ 显色，不是本水解产物主证据。`
- `CHK5_SEM_EXP_20_2_09_020` `A` before: `A 准确指出 01179 的显色语境和本水解产物判断不匹配。`
- `CHK5_SEM_EXP_20_2_09_020` `A` after: `A 准确指出钛(Ⅳ)过氧化氢鉴定资料的显色语境与本水解产物判断不匹配。`

## Final Validation After Diagnostic Raw-ID Addendum

- JSON parse: `passed`.
- Total questions: `510`.
- Each packet question count: `30`.
- Type totals: `321` single_choice / `154` true_false / `35` fill_blank.
- Single-choice answer/options/option_links: `passed`.
- RAG evidence ids checked: `57`; missing: `0`.
- visible_raw_id_backtick: `0`.
- visible_internal: `0`.
- visible_spacing: `0`.
- diagnostic_internal: `0`.
- diagnostic_raw_backtick: `0`.
- ascii_digit_formula: `0`.
- ascii_charge_ion: `0`.
- caret_latex_markdown: `0`.
- Validation errors: `0`.
