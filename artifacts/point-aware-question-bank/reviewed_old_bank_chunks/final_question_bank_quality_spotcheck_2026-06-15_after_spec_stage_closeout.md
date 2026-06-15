# Final Question Bank Quality Spotcheck - 2026-06-15 After Spec Stage Closeout

## Scope

- Files checked:
  - `chunk_1_release_final_v1.json`
  - `chunk_2_release_final_v1.json`
  - `chunk_3_release_final_v1.json`
  - `chunk_4_release_final_v1.json`
  - `chunk_5_release_final_v1.json`
- OpenSpec change: `full-question-bank-semantic-release-repair`
- OpenSpec status after closeout update: valid, `11 / 115` tasks complete.
- Release publishable item count by file:
  - chunk 1: 443 publishable items, 7 excluded reject items
  - chunk 2: 450 publishable items
  - chunk 3: 450 publishable items
  - chunk 4: 450 publishable items
  - chunk 5: 510 publishable items
  - total publishable items: 2,303

## Conclusion

Chunks 1-5 are not ready for direct import or publication.

The latest stage closeout is correct: the OpenSpec change must stay open. The already rereviewed batches can reach release quality, but the unrepaired portions still contain release blockers. This spotcheck confirms that the remaining issues are not isolated metadata noise; they appear in active publishable questions and include visible/template option diagnostics, ASCII chemistry aliases, mobile-hostile formula fill blanks, low-depth retained items, and questionable point-link semantics.

Scripts were used only for inventory counts and locating examples. The pass/fail judgments below come from manually reading the sampled effective questions, their options/answers/explanations, bound video points, and canonical experiment text.

## Inventory Gate Snapshot

Approximate read-only scan over active publishable items:

| Chunk | Publishable | Missing Explanation | Template Diagnostics | ASCII Formula Hits | Fill Blanks | Fill Blanks With ASCII Formula Alias |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 443 | 0 | 99 | 51 | 68 | 0 |
| 2 | 450 | 0 | 37 | 4 | 64 | 4 |
| 3 | 450 | 0 | 215 | 6 | 133 | 1 |
| 4 | 450 | 0 | 313 | 11 | 126 | 6 |
| 5 | 510 | 0 | 331 | 2 | 35 | 0 |
| Total | 2,303 | 0 | 995 | 74 | 426 | 11 |

Interpretation: explanation completeness is currently good, but option-link language and formula/mobile quality are still not release-clean.

## Manual Samples

| Sample | Point Binding | Manual Judgment |
| --- | --- | --- |
| `CHUNK1_19_1_01_Q010` | `candidate-1-034a8366` / 氯水 + KBr 溶液 + CCl₄ | Pass. The rewritten effective question asks which point proves Cl₂ > Br₂. The canonical experiment and video point support the answer. Options and diagnostics are chemistry-specific, and formula display is Unicode-clean. |
| `CHUNK1_19_1_02_Q001` | `candidate-1-656364cb` / 卤素水分别与 Na₂S₂O₃ 反应 | Fail. The question itself is source-supported, but the correct option diagnostic still says it “直接落在点位” and “能回答题干要求”. This is template/review wording, not a final student-quality option explanation. |
| `EXP_19_3_03_SEMANTIC_FINAL_001` | `candidate-1-26a8e36e`, `candidate-2-795f5a0b` / 除去 SO₄²⁻ 干扰并验证 SO₃²⁻ | Needs repair. The rewrite improves a shallow title-object recall into a reason question, and the canonical text supports SO₄²⁻ interference. However, diagnostics remain formulaic and should be reauthored to explain each distractor by actual chemistry. |
| `EXP_19_3_03_SEMANTIC_FINAL_030` | `candidate-2-795f5a0b` / 验证 SO₃²⁻ 存在 | Fail. Fill blank asks for released gas and accepts `SO2`, `SO₂`, and `二氧化硫`. The canonical point supports SO₂, but visible/mobile answer handling is not release-clean unless ASCII is explicitly hidden as grading tolerance and the displayed answer is Unicode or Chinese. The explanation is also generic. |
| `OLD_CHUNK3_EXP_19_8_01_Q001` | `candidate-1-356d797d` / Pb(NO₃)₂ + NaOH | Fail. Source supports NaOH, but the item is low-depth reagent recall. The correct option diagnostic is still “该选项直接对应本题考查的实验操作、现象或结论”, and distractor option links point to the current point despite being adjacent/other-experiment distractors. |
| `OLD_CHUNK3_EXP_19_6_02_Q024` | `candidate-2-ea144d3d` / 镁燃烧及生成物 | Needs repair/logging. The fill blank asks for MgO as product. This is machine-deterministic but formula input on mobile should either be rewritten to single choice or logged as an explicitly retained short formula answer. |
| `REV_CH4_EXP_20_1_02_Q001` | `candidate-1-5b3e91cf` through `candidate-5-2962277d`, secondary `candidate-6-e34dc5e9` | Fail. Canonical text supports NH₃·H₂O as reagent across several metal salts, but the item is mostly reagent-name recall and option diagnostics are still generic template text. Multi-point binding is broad but not explained at option level. |
| `REV_CH4_EXP_20_1_02_Q022` | `candidate-1-5b3e91cf` / CuSO₄ + NH₃·H₂O | Fail. Fill blank asks for 硫酸铜 and accepts `CuSO4` plus `CuSO₄`. This is a visible/mobile formula alias risk, and the explanation “对应的实验操作或现象内容是……” is generic. |
| `CHK5_SEM_EXP_20_2_08_001` | `candidate-1-376fa2cd` / Cr₂(SO₄)₃ + Na₂CO₃ | Needs repair. The rewritten effective question is source-supported, but option diagnostics still include template phrases. Since this chunk has many similar diagnostics, it cannot be considered publish-clean. |
| `CHK5_SEM_EXP_20_2_08_026` | `candidate-1-376fa2cd` / Cr₂(SO₄)₃ + Na₂CO₃ | Fail / low-depth. Fill blank answer is “观察” in “操作后应重点____现象”. Although source text says to observe phenomena, this is too shallow for release unless rewritten to the actual phenomenon/conclusion. |

## Evidence Notes

- `19-1-01`: canonical experiment describes KBr/KI/CCl₄ systems with chlorine water or bromine water, observing the CCl₄ layer to infer Cl₂ > Br₂ > I₂. This supports the clean rewritten Q010.
- `19-3-03`: canonical material supports the SO₃²⁻ test and the need to avoid SO₄²⁻ interference. Some sampled questions are source-supported but still fail final wording/mobile gates.
- `19-8-01`: canonical text says Pb(NO₃)₂ solution is treated with 2 mol/L NaOH, then the precipitate is tested with HNO₃ and NaOH. Reagent-recall questions are supported but low-depth.
- `20-1-02`: canonical text says CuSO₄, AgNO₃, ZnSO₄, CdSO₄, and HgCl₂ solutions are treated with NH₃·H₂O, then precipitate generation/dissolution and stability are observed. The source supports the chemistry, but sampled option diagnostics and fill blanks are not release-clean.
- `20-2-08`: canonical text supports the point “向 Cr₂(SO₄)₃ 溶液中滴加 Na₂CO₃ 溶液，观察现象”, but sampled items still carry template diagnostics or shallow blanks.

## Release Blockers Confirmed

- Visible template option diagnostics remain across all five chunks.
- ASCII formula aliases remain in active publishable fill blanks without per-question retained-risk logging.
- Several fill blanks are still mobile-hostile or too shallow for short-answer entry.
- Some retained low-depth items have no concrete prerequisite/operation/safety reason in the manual log.
- Some option links have semantically weak point binding, especially distractors linked to the current point rather than null or a truly relevant adjacent point.
- Mechanical parse and missing-explanation gates are not enough to prove release quality.

## Action Required Before Import

Continue `full-question-bank-semantic-release-repair` in order:

1. Finish chunk 1 remaining manual batches starting at `19-1-02`.
2. Reauthor visible option-link diagnostics for every active single-choice item.
3. Resolve or log every formula-heavy/mobile-risk fill blank.
4. Normalize displayed chemistry formulas while keeping ASCII only as hidden deterministic grading synonyms when justified.
5. Recheck every retained low-depth item against operation, observation, safety, or prerequisite value.
6. Produce the final all-chunk QA report only after every active publishable item appears exactly once in the manual rereview logs.
