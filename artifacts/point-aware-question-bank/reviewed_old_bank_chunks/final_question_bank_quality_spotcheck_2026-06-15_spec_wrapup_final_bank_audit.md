# Spec Wrap-Up Final Bank Audit

Date: 2026-06-15

Scope:
- Release files checked: `chunk_1_release_final_v1.json` through `chunk_5_release_final_v1.json`.
- OpenSpec change checked: `full-question-bank-semantic-release-repair`.
- This audit did not edit release JSONs. It used scripts only for inventory, navigation, and parse/risk counts; sample pass/fail judgments below are manual semantic judgments from reading the effective question, answer, explanation, point binding, video point titles, and canonical/supporting evidence where needed.

## OpenSpec Wrap-Up Status

- `openspec validate full-question-bank-semantic-release-repair --strict`: pass.
- Apply progress: 18 / 160 tasks complete; 142 tasks remain.
- Last completed work: current-release audit seed failures and conditional samples were repaired/rechecked under tasks 2.45 and 2.46.
- Not complete: the change cannot be archived and chunks 1-5 cannot be declared import-ready because full per-experiment rereview is still pending. The next pending contiguous batch remains task 3.8, `19-1-08` (27 active questions).

## Inventory Signals

Read-only script inventory over active non-reject records:

| Chunk | Active non-reject | Missing explanations | Visible ASCII formula records | Formula/mobile-risk fill blanks | Multi-point records |
|---|---:|---:|---:|---:|---:|
| chunk 1 | 443 | 0 | 38 | 0 | 205 |
| chunk 2 | 450 | 0 | 5 | 5 | 140 |
| chunk 3 | 450 | 0 | 0 | 0 | 174 |
| chunk 4 | 450 | 0 | 3 | 3 | 221 |
| chunk 5 | 510 | 0 | 0 | 0 | 113 |

Important caveat: schema differences remain real. Chunk 5 uses `reviewed_questions`; chunk 3 uses `question_id`; chunk 4 uses `review_item_id`. A single-field validator can miss records. One manually sampled chunk 5 item still contains template option-link diagnostics even though an earlier quick aggregate scan missed it.

## Manual Sample Results

| Verdict | Count |
|---|---:|
| Pass | 6 |
| Conditional pass / low quality retained | 1 |
| Fail / not import-ready as written | 7 |
| Total sampled | 14 |

## Sample Details

### Pass

1. `CHUNK1_19_1_01_Q025`, chunk 1, `19-1-01`
   - Points: primary `candidate-1-034a8366`, `candidate-2-1e180c68`, `candidate-3-9b8be606`.
   - Judgment: pass. The rewritten stem asks for the evidence chain proving Cl₂/Br₂/I₂ oxidation order. The three point binding is justified because the answer requires all three displacement/CCl₄ observations.

2. `OLD_CHUNK3_EXP_19_6_02_Q001`, chunk 3, `19-6-02`
   - Points: primary `candidate-1-a3329021`, `candidate-2-ea144d3d`.
   - Judgment: pass. The question asks for the operation chain "remove oxide film, ignite magnesium, observe combustion and product"; both points are genuinely used. Explanation and option diagnostics are concrete.

3. `REV_CH4_EXP_20_1_02_Q001`, chunk 4, `20-1-02`
   - Points: primary `candidate-1-5b3e91cf`, `candidate-6-e34dc5e9`.
   - Judgment: pass. The repaired question tests the continuous phenomenon in CuSO₄ + NH₃·H₂O: precipitate formation and dissolution in excess ammonia. Multi-point binding is justified.

4. `REV_CH4_EXP_20_1_02_Q021`, chunk 4, `20-1-02`
   - Points: primary `candidate-2-167c639f`, `candidate-6-e34dc5e9`.
   - Judgment: pass. The repaired question focuses on why AgNO₃ + NH₃·H₂O must be observed in excess ammonia. It avoids formula fill risk and has concrete option diagnostics.

5. `CHK5_SEM_EXP_20_2_08_001`, chunk 5, `20-2-08`
   - Points: primary `candidate-1-376fa2cd`.
   - Judgment: pass. The seed repair changed reagent-name recall into an operation-observation item: Cr₂(SO₄)₃ solution plus Na₂CO₃ solution and observation of hydrolysis behavior.

6. `CHK5_SEM_EXP_20_3_01_002`, chunk 5, `20-3-01`
   - Points: primary `candidate-1-e0d18274`, `candidate-2-1d49d35b`, `candidate-3-99dd6b35`, `candidate-4-3926ad6c`, `candidate-5-a4376972`, `candidate-6-c0cbece1`.
   - Judgment: pass. The stem asks how to separate water-aquo cation color records from anion records; all six cation points are semantically involved.

### Conditional Pass

7. `EXP_19_3_03_SEMANTIC_FINAL_025`, chunk 2, `19-3-03`
   - Points: primary `candidate-2-795f5a0b`.
   - Judgment: conditional pass, low quality retained. The answer `紫` is mobile-safe and deterministic. Canonical SO₂/KMnO₄ observation plus supporting theory supports the color loss, but it remains a low-depth color anchor and should not be treated as a high-value reasoning item.

### Fail / Not Import-Ready

8. `CHUNK1_19_1_08_Q001`, chunk 1, `19-1-08`
   - Current points: primary `candidate-1-1e83fb7a`, `candidate-4-fb906ca4`.
   - Failure: low-depth reagent-source recall. Stem only asks which silver salt reagent is used; explanation is just "答案为：AgNO₃ 溶液". The point binding is overbroad because the key-outline point is not needed to answer the reagent question. Option diagnostics are still template-like.

9. `CHUNK1_19_1_08_Q015`, chunk 1, `19-1-08`
   - Current points: primary `candidate-1-1e83fb7a`.
   - Failure: true/false is too guessable and uses an absurd unrelated distractor ("flame color"). Explanation is tautological and does not teach the actual AgCl light/dark observation.

10. `EXP_19_3_03_SEMANTIC_FINAL_030`, chunk 2, `19-3-03`
    - Current points: primary `candidate-2-795f5a0b`.
    - Failure: formula/mobile-risk fill blank. Accepted answers include visible ASCII `SO2` alongside `SO₂`/Chinese alias semantics, and explanation is generic. This should be rewritten to deterministic single choice or explicitly separate hidden ASCII grading aliases from visible answer display.

11. `EXP_19_4_09_SEMANTIC_FINAL_021`, chunk 2, `19-4-09`
    - Current points: primary `candidate-2-a452c505`.
    - Failure: formula-heavy fill blank asks students to type `Fe(NO)SO4` / `Fe(NO)SO₄` style symbolic answer. This is not phone-friendly and the explanation is generic.

12. `OLD_CHUNK3_EXP_19_8_01_Q001`, chunk 3, `19-8-01`
    - Current points: primary `candidate-1-356d797d`.
    - Failure: reagent-name recall only. The correct option diagnostic is template language, and wrong options are all linked to the same point key even though they are unrelated/adjacent distractors. Needs rewrite into Pb(OH)₂ generation plus acid/base property comparison, or explicit low-depth retention justification.

13. `REV_CH4_EXP_20_1_02_Q022`, chunk 4, `20-1-02`
    - Current points: primary `candidate-1-5b3e91cf`.
    - Failure: formula/mobile-risk fill blank. It asks for "硫酸铜 / `CuSO4` / CuSO₄" as a blank answer, retains ASCII alias risk, and explanation says only "对应的实验操作或现象内容是...". The adjacent repaired Q001 shows the better pattern: ask about precipitate formation and dissolution.

14. `CHK5_SEM_EXP_20_3_14_026`, chunk 5, `20-3-14`
    - Current points: primary `candidate-1-de6f1130`.
    - Failure: still has generic shell stem ("哪项判断与实验操作、现象或结论一致") and template option-link diagnostics ("该选项直接对应...", "该选项混淆..."). The correct fact about Ni²⁺ and dimethylglyoxime is supported by canonical/supporting theory, but the final item is not polished enough for release.

## Release Decision

Current final bank quality is not sufficient for full import/publication. The repaired seed items are much better and several sampled repairs can enter after final validation, but the bank still contains unresolved classes required by the OpenSpec: low-depth recall, formula/mobile-risk fill blanks, overbroad point bindings, template diagnostics, and generic or tautological explanations.

No pure Unicode chemical equation or formula in the release JSON was edited during this audit. Any later formula normalization must remain semantic and student-facing only, not identifier-wide replacement.

Recommended next execution step: continue OpenSpec task 3.8 (`19-1-08`) first, because this spotcheck again found chunk 1 `19-1-08` failures, then proceed through remaining batches in order.
