# Chunk 1-5 Quality Gate Summary

Date: 2026-06-15

## Scope

- Rebuilt package root: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages`
- Chunks checked: `chunk_1` to `chunk_5`
- RAG id sources checked:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- This audit did not modify `chunk_X_release_final_v1.json`.

## Verdict

Current rebuilt packages are structurally valid and substantially better than the previous reviewed/release files, but they are **not ready for direct import as-is**.

The remaining problems are last-mile publish blockers and quality-edge issues, not a need to restart the whole reconstruction:

- Student-visible raw evidence ids remain in `chunk_5`.
- `chunk_3` still uses ASCII Roman valence notation such as `Sn(II)`, `Pb(IV)`, `As(III)` in many student-visible fields.
- `chunk_4` and `chunk_5` contain visible spacing/process-style wording such as `本实验 的`, `教材资料`, `视频点位`, and raw evidence framing.
- `chunk_3` has duplicate point-key bindings where the same point appears in both primary and secondary point lists.
- There are exact duplicate generic stems across experiments, mostly broad “learning goal / conclusion / evidence scope” items.
- `option_links[].diagnostic_note` still contains process terms in chunk 4/5; this matters because option links are stored in metadata and selected option links are copied into attempt metadata.

## Structural Validation

| chunk | packets | questions | single_choice | true_false | fill_blank |
|---|---:|---:|---:|---:|---:|
| chunk_1 | 15 | 450 | 283 | 128 | 39 |
| chunk_2 | 15 | 450 | 287 | 103 | 60 |
| chunk_3 | 15 | 450 | 231 | 120 | 99 |
| chunk_4 | 15 | 450 | 300 | 90 | 60 |
| chunk_5 | 17 | 510 | 321 | 154 | 35 |
| total | 77 | 2310 | 1422 | 595 | 293 |

Passed:

- JSON parse: pass for all 77 rebuilt packages.
- Packet size: every packet has 30 questions.
- Single-choice answer/options/option_links: pass.
- RAG evidence ids: all referenced ids exist in the RAG JSONL sources.
- `evidence_sufficient`: all published rows are true.
- Source-diff check: rebuilt stems and explanations are not copied verbatim from the slim source packets.
- Visible ASCII digit formulas and ASCII charge/ion notation: no broad residual class found in normal student-visible fields.

## Blocking Findings

### 1. Student-visible raw evidence ids

`chunk_5` has raw evidence ids in student-visible explanations:

- `20-2-09 / CHK5_SEM_EXP_20_2_09_019`: explanation includes `` `01156` `` and `` `01157` ``.
- `20-2-09 / CHK5_SEM_EXP_20_2_09_020`: explanation includes `` `01179` ``.

These should be rewritten as normal student-facing source descriptions, not id references.

### 2. ASCII Roman valence notation

Student-visible fields still contain 166 hits in `chunk_3`, for example:

- `Sn(II)`
- `Fe(III)`
- `Fe(II)`
- `Pb(IV)`
- `As(III)`, `Sb(III)`, `Bi(III)`

Under the current polish rule, these should become direct-display Unicode or Chinese-valence wording, e.g. `Sn(Ⅱ)`, `Fe(Ⅲ)`, `Pb(Ⅳ)`, or “二价锡 / 四价铅” where more readable.

### 3. Visible wording artifacts

Student-visible spacing/process-style artifacts were found:

- `chunk_3`: 5 hits, e.g. `教材材料 表明...`
- `chunk_4`: 58 hits, e.g. `本实验 的`, `本实验 覆盖`, `实验步骤 实验步骤本身`
- `chunk_5`: 16 hits, e.g. `哪组 教材依据`, `任意钛相关 依据 都可`

Representative examples:

- `chunk_4 / 20-1-03 / REV_CH4_EXP_20_1_03_Q015`: explanation has `本实验 覆盖...本实验的 实验观察点 和 实验文本范围内`.
- `chunk_4 / 20-2-05 / REV_CH4_EXP_20_2_05_Q020`: stem has `本实验 的实验主线`.
- `chunk_5 / 20-2-09 / CHK5_SEM_EXP_20_2_09_019`: stem/options/explanation use `教材依据`, raw ids, and `语义支持`.

These are not chemistry errors, but they are publish-quality blockers.

### 4. Duplicate point-key bindings

`chunk_3` has 62 questions where the same point key appears in both `primary_point_keys` and `secondary_point_keys`.

Example:

- `chunk_3 / 19-8-06 / REBUILT_CH3_19_8_06_Q013` has `candidate-4-5f9c97e0` in both primary and secondary lists.

This should be normalized before import so reporting and coverage analytics do not double-count the same point.

### 5. Exact duplicate generic stems

There are 18 exact duplicate stems across rebuilt packages. Examples:

- `下列哪一项属于本实验相关内容，而不是串入其他实验的干扰项？`
- `下列哪一项最需要理论说明，而不是只靠实验操作原文？`
- `本实验最简洁的结论是哪一项？`
- `本实验最合理的学习目标是哪一项？`

These are usually not evidence failures, but they are low-depth/generic phrasing. They should be rewritten with experiment-specific wording before final publication.

## Sample Quality Notes

Good signs:

- `chunk_2 / 19-3-06 / REBUILT_CH2_19_3_06_Q014` is evidence-backed and deterministic: it asks for the product of `S₂O₈²⁻` reduction and cites supporting theory.
- `chunk_1` samples checked after polish are clean in visible formula/evidence wording.
- Many `chunk_2` and `chunk_3` questions now test operation-to-evidence reasoning rather than only reagent names.

Quality risks:

- `chunk_2` still has generic scope/conclusion stems that repeat across neighboring packets.
- `chunk_3` has good chemistry intent but is not polished to the symbol/point-key standard.
- `chunk_4` has many wording artifacts from generation/polish, especially extra spaces around Chinese terms.
- `chunk_5` has the strongest remaining evidence-process leakage into student-visible text.

## Import Readiness

Do not import the current files directly as the default published bank.

Recommended gate:

1. Run a last-mile polish on chunks 2-5:
   - remove student-visible raw ids/backticks;
   - Unicode or Chinese-normalize Roman valence notation;
   - clean Chinese spacing artifacts;
   - rewrite generic duplicate stems with experiment-specific wording;
   - deduplicate primary/secondary point-key lists.
2. Clean or strip `option_links[].diagnostic_note` before import, or make a deliberate import transform that excludes diagnostic notes from student/attempt-facing metadata.
3. Rerun the same quality gate:
   - JSON/structure/evidence validation;
   - visible chemical-symbol scan;
   - process/raw-id scan;
   - duplicate stem scan;
   - point-key duplicate scan.

Expected effort: this is a polish/normalization pass, not a full semantic rebuild.

