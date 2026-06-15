# Final Question Bank Quality Spotcheck - 2026-06-15

## Scope

Files checked:

- `chunk_1_release_final_v1.json`
- `chunk_2_release_final_v1.json`
- `chunk_3_release_final_v1.json`
- `chunk_4_release_final_v1.json`
- `chunk_5_release_final_v1.json`

This spotcheck used scripts only for JSON parsing, inventory, statistics, and locating evidence. The quality judgments below are manual semantic judgments from reading the effective question, bound points, option links/source audit, and canonical experiment evidence.

## Structural Checks

| Chunk | Active questions | Missing effective explanations | Option-link text mismatches | ASCII formula candidate hits |
|---|---:|---:|---:|---:|
| chunk 1 | 443 | 45 | 0 | 302 |
| chunk 2 | 450 | 0 | 0 | 7 |
| chunk 3 | 450 | 0 | 0 | 3 |
| chunk 4 | 450 | 0 | 0 | 5 |
| chunk 5 | 510 | 0 | 0 | 0 |

Notes:

- ASCII formula hits are candidate hits in effective displayed fields and visible option-link/export fields; they still require manual confirmation before editing.
- Manual inspection confirmed several hits are real release issues, not just false positives.
- Per-question manual rereview logs do not cover all 2,303 active questions, so the full-bank semantic-release standard is not satisfied.

## Manual Sample

| Chunk | Question | Points checked | Manual judgment |
|---|---|---|---|
| 1 | `CHUNK1_19_2_02_Q002` | `candidate-1-452aecdc` Na₂O₂ + 水; `candidate-2-ca62174d` 冰水冷却 | Answer D is supported by the canonical procedure and cooling purpose, but the effective explanation is `None`. Release blocker. |
| 1 | `CHUNK1_19_1_01_Q010` | `candidate-1-034a8366` 氯水 + KBr 溶液 + CCl₄ | Chemistry is supported, but final displayed text still has ASCII `Cl2`, `Br2`, `CCl4` in stem/options/option links. Release blocker until normalized. |
| 2 | `EXP_19_3_03_SEMANTIC_FINAL_001` | `candidate-1-26a8e36e` 设计方法除去 SO₄²⁻ 干扰; `candidate-2-795f5a0b` 验证样品中 SO₃²⁻ 的存在 | Good. The canonical selected-experiment text states SO₄²⁻ interferes with SO₃²⁻ detection and should be removed first. Deterministic and point-aware. |
| 2 | `EXP_19_4_06_SEMANTIC_FINAL_001` | Six nitric-acid oxidation points from 浓硝酸 + 硫粉 through Zn/NH₃ or NH₄⁺ verification | Source-supported, but low-depth list recognition. Also has ASCII `NaClO` in a distractor/export-visible field. Needs polish before a strict release. |
| 3 | `OLD_CHUNK3_EXP_19_6_02_Q001` | `candidate-1-a3329021` 镁条除去氧化膜后点燃; `candidate-2-ea144d3d` 观察镁燃烧及生成物 | Good. The effective question connects operation and observation, not a bare reagent/product recall. |
| 3 | `OLD_CHUNK3_EXP_19_8_07_Q007` | `candidate-2-e9c3de06` PbO₂ + H₂SO₄ + MnSO₄，水浴加热 | Not release-ready. Explanation contains review-process wording (“原题未提供解析；审查时...”), option links assign the same point key to distractors, and option D keeps ASCII `NaClO`. |
| 4 | `REV_CH4_EXP_20_1_02_Q001` | Five NH₃·H₂O complex-formation points plus precipitation/dissolution observation | Source-supported but quality low. It mostly asks for the reagent name `NH₃·H₂O`; primary points are overbroad and option diagnostics include generic template language. Should be rewritten or at least narrowed. |
| 4 | `REV_CH4_EXP_20_2_02_Q012` | Co(II)/Ni(II) precipitates treated with H₂O₂ and bromine water | Effective stem/answer are supported. Metadata/export quality is not clean: option-link text fields are missing, diagnostic note is English and contains ASCII `H2O2`. Needs cleanup if option links are exported or reviewed downstream. |
| 5 | `CHK5_SEM_EXP_20_2_08_001` | `candidate-1-376fa2cd` Cr₂(SO₄)₃ + Na₂CO₃ | Acceptable but low-depth. It tests the correct reagent/context and excludes unrelated experiments; deterministic, but not very diagnostic. |
| 5 | `CHK5_SEM_EXP_20_3_14_029` | `candidate-1-de6f1130` Fe³⁺/Co²⁺/Ni²⁺ design experiment | Good conceptually. It correctly tests interference-aware design. The judgment depends on supporting theory about Fe³⁺/SCN⁻ strong color interference with Co²⁺ identification and should keep that theory dependency explicit. |

## Decision

Do not import/publish the five chunks as a final release set yet.

The current final files contain confirmed blockers:

- chunk 1 still has missing explanations.
- chunk 1 and some later chunks still contain displayed/export-visible ASCII chemistry formulas.
- At least one chunk 3 sampled item still contains review-process wording in the effective explanation.
- Some option-link diagnostics and point bindings are still template-like or overbroad.
- The full per-question manual semantic rereview required by the active OpenSpec change is not complete.

## Recommended Next Action

Resume manual semantic repair from `19-2-02`, then complete the full task list or explicitly create a narrower acceptance standard. Under the current strict standard, the set is not yet release-grade.

