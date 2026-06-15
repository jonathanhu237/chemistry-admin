# Final Question Bank Quality Spotcheck - After Spec Closeout Manual Resample

Date: 2026-06-15

Scope:

- `chunk_1_release_final_v1.json`
- `chunk_2_release_final_v1.json`
- `chunk_3_release_final_v1.json`
- `chunk_4_release_final_v1.json`
- `chunk_5_release_final_v1.json`

This is a post-spec-closeout quality spotcheck. It does not replace the required full manual semantic rereview in `full-question-bank-semantic-release-repair`.

## Spec Closeout State

The OpenSpec change `full-question-bank-semantic-release-repair` is structurally valid, but implementation is not complete.

- Schema: `spec-driven`
- Current task progress: 14 / 141 complete
- Remaining tasks: 127
- Strict validation: passed
- Archive decision: do not archive
- Release decision from spec: chunks 1-5 are still blocked until every active question receives manual semantic rereview and the final gates are zero-blocker.

## Read-Only Inventory Snapshot

Script usage in this section was limited to parsing, locating candidates, and counting risk classes. No script-generated wording, decisions, point bindings, explanations, or repairs were used.

Active question count:

- chunk 1: 443
- chunk 2: 450
- chunk 3: 450
- chunk 4: 450
- chunk 5: 510
- total: 2303

Mechanical risk signals found:

| Chunk | Active | Visible ASCII formula hits | ASCII option-link hits | Mobile-risk fill blanks | Multi-point items |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 443 | 40 | 20 | 3 | 204 |
| 2 | 450 | 0 | 0 | 8 | 140 |
| 3 | 450 | 0 | 0 | 7 | 174 |
| 4 | 450 | 0 | 4 | 14 | 221 |
| 5 | 510 | 0 | 0 | 0 | 113 |

Important: zero mechanical hits does not mean semantic approval. The manual sample below found release blockers even in records with clean parse and `publish_status: publishable`.

## Manual Sample Results

Manual sample size: 11 active questions across all five chunks.

Strict release-bar result: 0 / 11 fully pass.

Some sampled questions are answerable by students, but they still fail the release bar because final metadata, option diagnostics, point binding, explanation specificity, or mobile determinism is not publish-ready.

### `CHUNK1_19_1_01_Q001`

- Experiment: `19-1-01 氯、溴、碘的置换次序`
- Effective type: single choice
- Point keys: primary `candidate-1-034a8366`; secondary none
- Bound point: `氯水 + KBr 溶液 + CCl₄`
- Manual verdict: not release-ready
- Reason: the displayed question, answer, and option diagnostics are mostly coherent, but `source_audit.reviewer_note` is contaminated with the later `KClO₃` oxidation experiment. This breaks final traceability and proves prior patching/review metadata was not cleanly scoped.

### `CHUNK1_19_1_07_Q021`

- Experiment: `19-1-07 氯含氧酸盐的氧化性`
- Effective type: fill blank
- Point keys: primary `candidate-1-02621b6d`, `candidate-2-1046fab6`; secondary `candidate-4-391ca911`
- Bound points: `NaClO + KI-淀粉溶液`; `KClO₃ + KI-淀粉溶液`; `对不反应体系再加入 H₂SO₄ 酸化，比较氧化能力`
- Manual verdict: not release-ready
- Reason: asks for `KI-淀粉` / `KI-淀粉溶液`, which is fragile for mobile short-answer input and low-depth reagent recall. The secondary acidification point is not actually needed by the stem. Explanation only says the material lists the reagent, so it does not meet the concrete evidence standard.

### `CHUNK1_19_1_07_Q028`

- Experiment: `19-1-07 氯含氧酸盐的氧化性`
- Effective type: single choice
- Point keys: primary `candidate-2-1046fab6`, `candidate-4-391ca911`; secondary none
- Bound points: `KClO₃ + KI-淀粉溶液`; `对不反应体系再加入 H₂SO₄ 酸化，比较氧化能力`
- Manual verdict: not release-ready
- Reason: visible student-facing text still contains `KClO3` and `K+` instead of Unicode chemistry notation. Explanation is generic: `本题答案由对应实验的操作、现象或结论直接支持。` Correct-option diagnostic still says `需要结合点位...point_key 指向首个直接证据点`, which is review-process wording rather than student-quality option semantics.

### `EXP_19_3_03_SEMANTIC_FINAL_001`

- Experiment: `19-3-03 SO₃²⁻ 的检出`
- Effective type: single choice
- Point keys: primary `candidate-1-26a8e36e`, `candidate-2-795f5a0b`; secondary none
- Bound points: `设计方法除去 SO₄²⁻ 干扰`; `验证样品中 SO₃²⁻ 的存在`
- Manual verdict: not release-ready
- Reason: the core answer is likely supported, but option diagnostics are still formulaic and repeat the stem instead of explaining each option concretely. The stem mainly asks why `SO₄²⁻` is removed, so the second primary point is broader than needed unless logged as detection-chain context.

### `EXP_19_3_03_SEMANTIC_FINAL_030`

- Experiment: `19-3-03 SO₃²⁻ 的检出`
- Effective type: fill blank
- Point keys: primary `candidate-2-795f5a0b`; secondary none
- Bound point: `验证样品中 SO₃²⁻ 的存在`
- Manual verdict: not release-ready
- Reason: fill blank accepts `SO2`, `SO₂`, and `二氧化硫`, mixing ASCII and Unicode formula aliases. This is a mobile-risk symbolic answer. Explanation is generic: `对应的实验操作或现象内容是“SO₂/二氧化硫”。`

### `OLD_CHUNK3_EXP_19_8_01_Q001`

- Experiment: `19-8-01 Pb(OH)₂ 的生成与性质`
- Effective type: single choice
- Point keys: primary `candidate-1-356d797d`; secondary none
- Bound point: `Pb(NO₃)₂ + NaOH`
- Manual verdict: not release-ready
- Reason: answer is source-supported, but the item is a shallow reagent-name recall. Correct option diagnostic remains the forbidden template: `该选项直接对应本题考查的实验操作、现象或结论。` Retention reason is not concrete enough for final release.

### `OLD_CHUNK3_EXP_19_8_02_Q026`

- Experiment: `19-8-02 Sn(OH)₂ 的生成与性质`
- Effective type: fill blank
- Point keys: primary `candidate-1-f427ce6a`; secondary none
- Bound point: `SnCl₂ + NaOH`
- Manual verdict: not release-ready
- Reason: fill blank expects `+2` / `正二价`, which is mobile-fragile and mostly formula/valence recall. The explanation says only `对应的实验操作或现象内容是“+2”`; the oxidation-state judgment depends on supporting theory, not just the canonical operation.

### `REV_CH4_EXP_20_1_02_Q001`

- Experiment: `20-1-02 氨合物`
- Effective type: single choice
- Point keys: primary `candidate-1-5b3e91cf`, `candidate-2-167c639f`, `candidate-3-ee066dec`, `candidate-4-968503d0`, `candidate-5-2962277d`; secondary `candidate-6-e34dc5e9`
- Bound points: five metal-salt + ammonia-water reactions and observation of precipitation / dissolution in excess ammonia
- Manual verdict: not release-ready
- Reason: the question asks only which reagent supplies `NH₃`; the point binding is over-broad. Option diagnostics for `NaCl` and `NH₃·H₂O` are still template-level. The item is low-depth reagent identification unless rewritten toward operation/phenomenon comparison.

### `REV_CH4_EXP_20_1_02_Q021`

- Experiment: `20-1-02 氨合物`
- Effective type: fill blank
- Point keys: primary `candidate-1-5b3e91cf`, `candidate-2-167c639f`, `candidate-3-ee066dec`, `candidate-4-968503d0`, `candidate-5-2962277d`; secondary `candidate-6-e34dc5e9`
- Bound points: same broad ammonia-complex set as Q001
- Manual verdict: not release-ready
- Reason: accepts `氨水`, `NH3·H2O`, and `NH₃·H₂O`, so it mixes a short Chinese answer with symbolic aliases. If retained, aliases must be hidden grading tolerance; as written it is mobile-risk and low-depth. Explanation is generic and point keys are over-broad for a single reagent-source blank.

### `CHK5_SEM_EXP_20_2_08_001`

- Experiment: `20-2-08 铬(III)盐的水解`
- Effective type: single choice
- Point keys: primary `candidate-1-376fa2cd`; secondary none
- Bound point: `Cr₂(SO₄)₃ + Na₂CO₃`
- Manual verdict: not release-ready
- Reason: generic stem asks `下列哪项判断与实验操作、现象或结论一致`. Correct answer still mainly identifies `Cr₂(SO₄)₃`, a low-depth reagent recall. Option diagnostics use forbidden template wording such as `该选项直接对应...` and `该选项混淆...`.

### `CHK5_SEM_EXP_20_3_14_026`

- Experiment: `20-3-14 小设计实验`
- Effective type: single choice
- Point keys: primary `candidate-1-de6f1130`; secondary none
- Bound point: `已知溶液中含 Fe³⁺、Co²⁺、Ni²⁺，设计方案分别检出三种离子`
- Manual verdict: not release-ready
- Reason: the answer about `Ni²⁺ 与丁二酮肟生成红色沉淀` is plausible and theory-supported, but the stem remains generic and option diagnostics remain template-level. The final version should ask directly about the role of positive phenomenon and interference control in the design, not ask a broad “which judgment matches” question.

## Release Decision

Chunks 1-5 cannot be imported or published as-is.

The strongest blockers are:

- There are still visible ASCII chemistry formula hits in active effective fields, especially chunk 1.
- There are still template option-link diagnostics in active publishable items.
- Several fill blanks remain unsafe for mobile deterministic input because they expect formulas, valence symbols, or mixed Chinese/symbolic aliases.
- Multi-point bindings are often inherited too broadly and not justified by the final stem.
- Some `publish_status: publishable` records still fail the stricter release bar.
- At least one chunk 1 record contains cross-experiment audit contamination, so the manual traceability layer is not trustworthy enough yet.

## Required Next Action

Continue the OpenSpec tasks in order. The next unfinished task remains `3.6 Manually rereview and repair 19-1-06`, but the post-closeout sample also confirms that previously marked batches and chunks 2-5 must not be trusted without the full manual rereview required by the spec.

Do not archive `full-question-bank-semantic-release-repair`.

