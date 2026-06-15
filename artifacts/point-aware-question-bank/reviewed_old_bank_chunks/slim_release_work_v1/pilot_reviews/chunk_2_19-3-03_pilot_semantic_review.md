# Pilot Semantic Review: chunk_2 / 19-3-03

This pilot is exploratory. It does not modify the release JSON.

## Work Unit

- Packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_2\19-3-03.json`
- Experiment: `19-3-03 SO₃²⁻ 的检出`
- Questions: `30`
- Video points:
  - `candidate-1-26a8e36e`: 设计方法除去 SO₄²⁻ 干扰
  - `candidate-2-795f5a0b`: 验证样品中 SO₃²⁻ 的存在

## Evidence Procedure Used

1. Parse the packet with Python JSON, not PowerShell `ConvertFrom-Json`.
2. Force UTF-8 command output with `PYTHONIOENCODING=utf-8`.
3. Treat inherited `canonical_chunk_ids` and `supporting_theory_chunk_ids` as untrusted candidate locators.
4. Read the actual RAG source chunks from `E:\chemistry-rag\data\rag_ready`.
5. Compare each stem/options/answer/explanation against the RAG text.
6. Separate three outcomes:
   - evidence supported and non-duplicative
   - evidence supported but duplicate/low-depth
   - evidence weak, wrong ids, or needs rewrite

## RAG Evidence Read

Direct experiment chunks:

| Chunk ID | JSONL | Line | Evidence role |
| --- | --- | ---: | --- |
| `expchunk_00223_91cb040d8f` | `textbook_experiment_chunks_v1.jsonl` | 236 | 预习：复习 SO₃²⁻、SO₄²⁻ 等性质；涉及 H₂S/SO₂ 的安全措施 |
| `expchunk_00224_166bfb5a4a` | `textbook_experiment_chunks_v1.jsonl` | 237 | 安全：SO₂ 有刺激性和毒害性，相关反应需减少逸出并在通风橱内进行 |
| `expchunk_00228_5e99fe31b9` | `textbook_experiment_chunks_v1.jsonl` | 241 | SO₂ 制备；SO₂ 还原性/氧化性/漂白作用操作；SO₃²⁻ 检出要求预先除去 SO₄²⁻ 干扰，并设计分离步骤、验证样品、写示意图和方程式 |

Supporting theory checked:

| Chunk ID | JSONL | Line | Use |
| --- | --- | ---: | --- |
| `textbook_prose_00340_77f9d61c94` | `textbook_inorganic_lower_chunks_v1.jsonl` | 591 | SO₂ 可表现还原性/氧化还原背景，但不直接说明 KMnO₄ 褪色 |
| `textbook_prose_00363_d345af4100` | `textbook_inorganic_lower_chunks_v1.jsonl` | 614 | 亚硫酸及其盐氧化还原背景；不能单独支撑“酸化放出 SO₂” |
| `textbook_prose_00344_07bf4af806` | `textbook_inorganic_lower_chunks_v1.jsonl` | 595 | SO₂ 与有机色素形成无色有机物，可作漂白剂 |
| `textbook_prose_01251_89ce24842f` | `textbook_inorganic_lower_chunks_v1.jsonl` | 1909 | KMnO₄ 水溶液呈紫红色 |
| `textbook_prose_01253_29e4ee4b73` | `textbook_inorganic_lower_chunks_v1.jsonl` | 1908 | 酸性介质中 MnO₄⁻ 氧化 SO₃²⁻ 的反应 |
| `textbook_prose_00341_44241a0b9e` | `textbook_inorganic_lower_chunks_v1.jsonl` | 592 | SO₂ 与 H₂S 反应生成 S，可支撑 SO₂ 氧化性相关题 |

Important evidence finding: old ids exist, but several are semantically incomplete. In particular, the current theory ids do not directly support all KMnO₄ color-change and bleaching questions. Correct handling is to replace/augment theory ids, not to mark them passed just because ids resolve.

## Package-Level Findings

- The package is not release-ready as-is.
- There is a large duplicate cluster:
  - SO₄²⁻ 干扰/removal: Q001, Q002, Q003, Q008, Q011, Q018, Q021, Q022, Q023, Q027, Q029
  - KMnO₄ 褪色/SO₂ 还原性: Q005, Q009, Q013, Q015, Q019, Q025
  - 品红褪色/SO₂ 漂白性: Q006, Q016, Q017, Q020, Q026
  - SO₂ 安全/通风橱: Q007, Q010, Q012
- Several items use old or generic review language in explanations. This is metadata/content hygiene, not a source-evidence proof.
- The “酸化 SO₃²⁻ 放出 SO₂” questions need stronger explicit RAG support. Current direct experiment text asks to verify SO₃²⁻ and write equations, but does not itself state that exact acidification route.
- Fill blanks Q025/Q026 are mobile-acceptable short answers, but low-depth; Q030 is a formula/name fill blank and should be rewritten to deterministic single choice.

## Per-Question Pilot Decision

| ID | Pilot decision | Evidence result | Point/action |
| --- | --- | --- | --- |
| Q001 | Keep with metadata fix | Directly supported by `expchunk_00228` | Primary should be point 1 only; remove point 2 unless explanation explicitly includes verification step |
| Q002 | Rewrite | Supported but duplicate of Q001 | Replace with a sequence/output question from `expchunk_00228` |
| Q003 | Rewrite | Supported but too shallow/duplicate | Replace with a question about “预先除去” plus reason, or merge with Q001 |
| Q004 | Rewrite | Current acidification route needs stronger evidence | Rewrite to “教材要求完成哪两项任务：设计分离步骤并验证样品含 SO₃²⁻” |
| Q005 | Keep with theory-id repair | Needs `00340` plus `01251` and/or `01253`; old theory ids incomplete | Keep only if explanation states theory dependency |
| Q006 | Keep with theory-id repair | `expchunk_00228` gives operation; `00344` supports漂白 | Add `textbook_prose_00344_07bf4af806` |
| Q007 | Keep | Directly supported by `expchunk_00224` and `expchunk_00228` | Low depth but useful safety item |
| Q008 | Rewrite | Supported but duplicate | Ask about required deliverable: separation schematic and equations |
| Q009 | Rewrite | Duplicate of Q005 | Replace with SO₂ 氧化性: SO₂ 通入饱和 H₂S 水溶液，use `00341` |
| Q010 | Rewrite | Duplicate safety | Replace with SO₂ preparation setup: Na₂SO₃ in flask, conc. H₂SO₄ in separatory funnel |
| Q011 | Keep low-quality | Directly supported but very easy true/false | Acceptable only if quota needs a simple checkpoint |
| Q012 | Rewrite | Duplicate of Q007/Q010 | Replace with slow addition/heating sequence in SO₂ preparation |
| Q013 | Rewrite | Duplicate of Q005 | Replace with MnO₄⁻/SO₃²⁻ acidic reaction evidence using `01253` |
| Q014 | Rewrite | KSCN distractor is outside this experiment and too artificial | Rewrite as true/false: textbook asks for separation process schematic and equations |
| Q015 | Rewrite | Duplicate and too terse | Rewrite to reaction-level support from `01253`, not just color |
| Q016 | Rewrite | False statement is deterministic but too artificial | Rewrite to SO₂ 与有机色素形成无色物质, evidence `00344` |
| Q017 | Rewrite | Duplicate of Q006 | Replace with SO₂ 氧化性/H₂S water item, evidence `expchunk_00228` + `00341` |
| Q018 | Keep low-quality | Directly supported by `expchunk_00228` | Multi-point binding is semantically real, but item is very simple |
| Q019 | Rewrite | Duplicate of Q005/Q013 | Replace with KMnO₄ medium-dependent products from `01253` |
| Q020 | Rewrite | Duplicate of Q006/Q017 | Replace with why 品红 is used to observe漂白作用, evidence `00344` |
| Q021 | Rewrite | Supported but formula-choice blank is low-depth duplicate | Replace with “which statement matches the interference logic” |
| Q022 | Rewrite | Supported but duplicate | Replace with target/interferent role mapping |
| Q023 | Rewrite | Supported but duplicate | Replace with required written output: schematic + equations |
| Q024 | Rewrite | Acidification-to-SO₂ needs explicit support | Rewrite to direct textbook requirement rather than formula blank |
| Q025 | Rewrite or keep low-quality | Mobile answer is short, but asks only a color; theory ids need repair | Prefer single-choice or replace with reaction reasoning |
| Q026 | Rewrite or keep low-quality | Mobile answer is short, but asks only one observed effect; needs `00344` | Prefer single-choice with reason |
| Q027 | Rewrite | Duplicate of Q002 | Replace with point-1/point-2 relation question |
| Q028 | Rewrite | Duplicate of Q024 and theory weak | Replace with deterministic direct-text question |
| Q029 | Rewrite | Duplicate of Q002/Q027 | Replace with safety or preparation detail |
| Q030 | Rewrite | Formula/name fill blank; mobile and evidence risk | Convert to single choice or avoid unsupported acidification route |

Pilot count:

- Keep/minor metadata fix: `4` (Q001, Q005, Q006, Q007)
- Keep but quality low: `2` (Q011, Q018)
- Rewrite: `24`
- Reject: `0` for now, because most failures can become better deterministic questions using the same evidence surface

## Example Rewrite Targets

These are not applied; they show the desired repair style.

1. Replace a duplicate SO₄²⁻ item:
   - Stem: `教材在 SO₃²⁻ 的检出部分要求完成哪一组任务？`
   - Correct: `预先除去 SO₄²⁻ 干扰，设计分离步骤，验证样品中含 SO₃²⁻，并写出分离过程示意图和有关反应方程式`
   - Evidence: `expchunk_00228_5e99fe31b9`
   - Points: point 1 + point 2

2. Replace a duplicate safety item:
   - Stem: `按教材的 SO₂ 制备操作，蒸馏瓶和分液漏斗中分别应放入什么？`
   - Correct: `蒸馏瓶中放 Na₂SO₃ 固体，分液漏斗中装浓硫酸`
   - Evidence: `expchunk_00228_5e99fe31b9`
   - Points: point 2

3. Replace an unsupported acidification fill blank:
   - Stem: `关于 SO₃²⁻ 的检出，下列哪项最符合教材原文？`
   - Correct: `含 SO₃²⁻ 的溶液中少量 SO₄²⁻ 会干扰检出，因此需预先除去 SO₄²⁻`
   - Evidence: `expchunk_00228_5e99fe31b9`
   - Points: point 1

4. Replace a duplicate KMnO₄ color-only item:
   - Stem: `若用酸性 KMnO₄ 相关性质解释 SO₃²⁻ 的还原性，哪一组证据最贴合？`
   - Correct: `KMnO₄ 水溶液呈紫红色，酸性介质中 MnO₄⁻ 可氧化 SO₃²⁻ 为 SO₄²⁻`
   - Evidence: `textbook_prose_01251_89ce24842f`, `textbook_prose_01253_29e4ee4b73`
   - Points: point 2
   - Note: Mark as supporting-theory dependent.

5. Replace a duplicate品红 item:
   - Stem: `SO₂ 通入品红溶液用于观察哪类性质？`
   - Correct: `漂白作用；SO₂ 可与一些有机色素分子结合形成无色有机物`
   - Evidence: `expchunk_00228_5e99fe31b9`, `textbook_prose_00344_07bf4af806`
   - Points: point 2
   - Note: Mark as supporting-theory dependent.

## Lessons for the Distributed Spec

The small-package approach is feasible, but the spec must enforce these gates:

- Do not trust inherited chunk ids. They are candidates only.
- Every old id must be compared against actual RAG text.
- If an id exists but supports only a nearby idea, record `id_present_but_semantically_insufficient`.
- Search adjacent/parent RAG chunks when direct ids are incomplete.
- Distinguish canonical experiment evidence from supporting theory.
- Duplicate clusters must be repaired, not merely logged.
- Low-depth color/reagent/formula/name recall must be rewritten when possible.
- Formula/name fill blanks should generally become single choice unless the answer is a short ordinary Chinese word.
- A completed package should output a per-question decision table and a patchable list of proposed question rewrites.
