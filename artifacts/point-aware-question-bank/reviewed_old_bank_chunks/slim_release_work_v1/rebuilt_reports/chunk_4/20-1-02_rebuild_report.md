# Rebuild Report: chunk_4 / 20-1-02 氨合物

## Packet

- Packet id: `20-1-02`
- Experiment code: `20-1-02`
- Experiment title: `氨合物`
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_4\20-1-02.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_4\20-1-02_rebuilt_v1.json`
- Statement: this packet was manually rebuilt question by question; it is not a script-generated batch normalization.
- 明确声明：本 packet 已逐题语义重构，不是脚本批量生成。

## Counts

- Total questions: `30`
- Type counts: `20 single_choice`, `6 true_false`, `4 fill_blank`
- Keep: `5`
- Rewrite: `25`
- Reject: `0`

## Rewrite List

Rewritten question ids:

- `REV_CH4_EXP_20_1_02_Q002`
- `REV_CH4_EXP_20_1_02_Q003`
- `REV_CH4_EXP_20_1_02_Q004`
- `REV_CH4_EXP_20_1_02_Q005`
- `REV_CH4_EXP_20_1_02_Q006`
- `REV_CH4_EXP_20_1_02_Q007`
- `REV_CH4_EXP_20_1_02_Q010`
- `REV_CH4_EXP_20_1_02_Q012`
- `REV_CH4_EXP_20_1_02_Q013`
- `REV_CH4_EXP_20_1_02_Q014`
- `REV_CH4_EXP_20_1_02_Q015`
- `REV_CH4_EXP_20_1_02_Q016`
- `REV_CH4_EXP_20_1_02_Q017`
- `REV_CH4_EXP_20_1_02_Q018`
- `REV_CH4_EXP_20_1_02_Q019`
- `REV_CH4_EXP_20_1_02_Q020`
- `REV_CH4_EXP_20_1_02_Q022`
- `REV_CH4_EXP_20_1_02_Q023`
- `REV_CH4_EXP_20_1_02_Q024`
- `REV_CH4_EXP_20_1_02_Q025`
- `REV_CH4_EXP_20_1_02_Q026`
- `REV_CH4_EXP_20_1_02_Q027`
- `REV_CH4_EXP_20_1_02_Q028`
- `REV_CH4_EXP_20_1_02_Q029`
- `REV_CH4_EXP_20_1_02_Q030`

Main rewrite reasons:

- The source packet repeated low-depth salt-name and formula fill blanks for CuSO₄, AgNO₃, ZnSO₄, CdSO₄, and HgCl₂.
- Several source true/false questions were answerable by guessing from an obviously wrong reagent or color.
- Broad inherited multi-point bindings were narrowed or redesigned so multi-point questions truly ask across multiple operations or point titles.
- Formula/name fill blanks were replaced by single-choice or short ordinary Chinese fill blanks.
- Supporting theory was narrowed to the two theory ids that directly support NH₃ coordination and copper ammine color.

## Kept But Quality-Edge Questions

- `REV_CH4_EXP_20_1_02_Q001`: kept because it already asks for the full CuSO₄ observation chain rather than a reagent name; it truly binds CuSO₄ and common precipitate-generation/dissolution points.
- `REV_CH4_EXP_20_1_02_Q008`: kept with tightened theory evidence because copper ammine deep-blue color is a valid theory-supported phenomenon; it is edge only because canonical experiment text alone does not state the color.
- `REV_CH4_EXP_20_1_02_Q009`: kept because acid/base/heat is directly stated in canonical evidence; it is basic recall but still tests a required post-dissolution stability condition.
- `REV_CH4_EXP_20_1_02_Q011`: kept because the CuSO₄ inner/outer-sphere design purpose is directly stated by the canonical experiment text and has a specific point.
- `REV_CH4_EXP_20_1_02_Q021`: kept because the fill answer `热` is short, ordinary Chinese, deterministic, and directly supported by the canonical stability-test sentence.

## Evidence Insufficient

- None.

No question is marked publishable with `evidence_sufficient=false`.

## Multi-Point Questions

- `REV_CH4_EXP_20_1_02_Q001`: uses `candidate-1-5b3e91cf` for the CuSO₄ system and `candidate-6-e34dc5e9` for the common precipitate-generation/dissolution observation chain.
- `REV_CH4_EXP_20_1_02_Q002`: uses the five metal salt point keys plus `candidate-6-e34dc5e9` because the stem asks for the purpose of comparing all five salts under the same NH₃·H₂O observation task.
- `REV_CH4_EXP_20_1_02_Q003`: uses the five salt point keys and the common operation/observation point because the stem asks for the common first operation across all five systems.
- `REV_CH4_EXP_20_1_02_Q004`: uses `candidate-6-e34dc5e9` plus the five salt systems because the missing judgement applies to the shared observation chain after initial precipitate formation.
- `REV_CH4_EXP_20_1_02_Q005`: uses ZnSO₄ and CdSO₄ point keys because the stem asks for the zinc/cadmium comparison entry point.
- `REV_CH4_EXP_20_1_02_Q006`: uses AgNO₃ and HgCl₂ point keys because the stem asks for the silver/mercury comparison entry point.
- `REV_CH4_EXP_20_1_02_Q010`: uses `candidate-6-e34dc5e9` and `candidate-7-bff176fd` because the stem asks for procedure order from dissolution to stability testing.
- `REV_CH4_EXP_20_1_02_Q013`: uses all five metal salt point keys because it checks the full scope of the parallel NH₃·H₂O observation set.
- `REV_CH4_EXP_20_1_02_Q014`: uses `candidate-6-e34dc5e9` and `candidate-7-bff176fd` because the object of stability testing depends on the previous dissolution step.
- `REV_CH4_EXP_20_1_02_Q025`: uses ZnSO₄ and CdSO₄ point keys because the stem asks for the paired zinc/cadmium inclusion.
- `REV_CH4_EXP_20_1_02_Q027`: uses dissolution and stability points because the question asks the object of stability testing.
- `REV_CH4_EXP_20_1_02_Q028`: uses CuSO₄ and common observation points because the stem explicitly asks about both.
- `REV_CH4_EXP_20_1_02_Q029`: uses all five metal salt points plus the common observation point because the stem asks which task truly justifies broad multi-point binding.

## Fill-Blank Mobile Risk

| question_id | accepted answer | risk | reason |
|---|---|---|---|
| `REV_CH4_EXP_20_1_02_Q019` | `沉淀` | low | Short ordinary Chinese answer; no formula or alias required. |
| `REV_CH4_EXP_20_1_02_Q020` | `溶解` | low | Short ordinary Chinese answer; deterministic normalized exact match. |
| `REV_CH4_EXP_20_1_02_Q021` | `热` | low | Single Chinese character; directly supported by canonical text. |
| `REV_CH4_EXP_20_1_02_Q022` | `外界` | low | Short concept word; no chemical formula input. |

Formula-bearing source fill blanks for CuSO₄, AgNO₃, ZnSO₄, CdSO₄, and HgCl₂ were rewritten to single choice.

## RAG Evidence Used

- `expchunk_00309_5610e5bc6f`: primary canonical experiment text for five salts with NH₃·H₂O, precipitate generation/dissolution, stability against acid/base/heat, and CuSO₄ inner/outer design.
- `expchunk_00314_c493a6ddc5`: canonical thought-question seed for comparing zinc/cadmium, zinc/copper, silver/mercury and broader ds-element complex-forming ability.
- `textbook_prose_00473_d672f2b358`: supporting theory for NH₃ coordination and Ag/Cu ammine complex formation.
- `textbook_prose_01050_e04444dc5f`: supporting theory for deep-blue [Cu(NH₃)₄]²⁺.

Rejected inherited/not-used evidence:

- `expchunk_00310_822a1490b4` was not used for final question support because it mainly covers a later copper(II) complex operation rather than the 20-1-02氨合物 point set.
- `textbook_prose_01034_1fe1dd3d56` was not used because it concerns Cu₂O/Cu(I) ammonia behavior and is not the precise support for most final stems.

## Validation

- JSON parse: pass.
- Question count: `30`.
- Unique question ids: pass.
- Single-choice answers align with options: pass.
- Single-choice option_links count equals options count: pass.
- All cited evidence ids found in RAG JSONL: pass.
- No `evidence_sufficient=false` publishable questions: pass.
- No visible ASCII digit formula hits found in final stems/options/explanations: pass.
- No formula-like fill-blank visible answers: pass.

## Publish Blocker Polish Validation

- Scope: student-visible JSON fields (`stem`, `options[].text`, `explanation`, and fill-blank `answer.accepted_answers`) in `20-1-02` rebuilt package.
- Internal/process wording: pass; remaining hits in student-visible fields = `0`.
- ASCII digit formula display: pass; remaining hits in student-visible fields = `0`.
- ASCII charge / ASCII valence display: pass; remaining hits in student-visible fields = `0`.
- caret / LaTeX / Markdown chemistry display: pass; remaining hits in student-visible fields = `0`.
- `option_links[].diagnostic_note`: treated as internal option diagnostic metadata, not included in the student-visible field scan.
- Release final JSON: not edited by this polish pass.
- Structural validation after polish: JSON parse pass; question count remains `30`; single-choice answers/options/option_links pass; cited RAG evidence ids are present.