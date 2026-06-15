# chunk_4 student-facing de-meta polish report

## Scope

- Chunk: `chunk_4`
- Packets: `20-1-02`, `20-1-03`, `20-1-04`, `20-1-05`, `20-1-06`, `20-1-07`, `20-1-08`, `20-1-09`, `20-2-01`, `20-2-02`, `20-2-03`, `20-2-04`, `20-2-05`, `20-2-06`, `20-2-07`
- Rebuilt JSON directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_4`
- Report path: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_4\chunk_4_student_facing_demeta_polish_report.md`
- Evidence sources:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Release JSON policy: this pass did not edit any `chunk_X_release_final_v1.json`. The recorded SHA-256 for `chunk_4_release_final_v1.json` remained `3CC7F9DEDEB4F6E191A3CD9478CA14F2E16BB81E21006634AEB211EE15369812` before and after this pass.

## Summary

- Total questions scanned: 450
- Meta/display-risk questions semantically reviewed: 101
- Actually modified questions: 72
- Retained after review with reasons: 29
- Answer changes: 0
- Point key changes: 0
- New supporting theory dependencies introduced: 0
- Existing supporting-theory flags were left unchanged. In the repair log below, `Supporting theory` means the final question already has `source_audit.supporting_theory_required = true`.
- Internal metadata retained: `source_audit`, evidence locators, packet metadata, and reviewer notes may still contain internal terms because they are not student-facing answer content. Student-facing fields and `option_links[].diagnostic_note` were cleaned.

## Modified Question IDs

`REV_CH4_EXP_20_1_02_Q001`, `REV_CH4_EXP_20_1_02_Q003`, `REV_CH4_EXP_20_1_02_Q004`, `REV_CH4_EXP_20_1_02_Q008`, `REV_CH4_EXP_20_1_02_Q009`, `REV_CH4_EXP_20_1_02_Q018`, `REV_CH4_EXP_20_1_02_Q023`, `REV_CH4_EXP_20_1_02_Q024`, `REV_CH4_EXP_20_1_02_Q025`, `REV_CH4_EXP_20_1_02_Q026`, `REV_CH4_EXP_20_1_02_Q028`, `REV_CH4_EXP_20_1_02_Q029`, `REV_CH4_EXP_20_1_03_Q016`, `REV_CH4_EXP_20_1_03_Q021`, `REV_CH4_EXP_20_1_03_Q030`, `REV_CH4_EXP_20_1_04_Q006`, `REV_CH4_EXP_20_1_04_Q014`, `REV_CH4_EXP_20_1_04_Q018`, `REV_CH4_EXP_20_1_04_Q019`, `REV_CH4_EXP_20_1_04_Q021`, `REV_CH4_EXP_20_1_04_Q025`, `REV_CH4_EXP_20_1_04_Q030`, `REV_CH4_EXP_20_1_05_Q003`, `REV_CH4_EXP_20_1_05_Q007`, `REV_CH4_EXP_20_1_05_Q009`, `REV_CH4_EXP_20_1_05_Q012`, `REV_CH4_EXP_20_1_05_Q013`, `REV_CH4_EXP_20_1_05_Q015`, `REV_CH4_EXP_20_1_05_Q020`, `REV_CH4_EXP_20_1_05_Q023`, `REV_CH4_EXP_20_1_05_Q030`, `REV_CH4_EXP_20_1_06_Q010`, `REV_CH4_EXP_20_1_06_Q013`, `REV_CH4_EXP_20_1_06_Q017`, `REV_CH4_EXP_20_1_06_Q021`, `REV_CH4_EXP_20_1_06_Q024`, `REV_CH4_EXP_20_1_06_Q025`, `REV_CH4_EXP_20_1_07_Q018`, `REV_CH4_EXP_20_1_07_Q019`, `REV_CH4_EXP_20_1_07_Q021`, `REV_CH4_EXP_20_1_07_Q024`, `REV_CH4_EXP_20_1_08_Q011`, `REV_CH4_EXP_20_1_08_Q017`, `REV_CH4_EXP_20_1_08_Q028`, `REV_CH4_EXP_20_1_08_Q030`, `REV_CH4_EXP_20_1_09_Q001`, `REV_CH4_EXP_20_1_09_Q002`, `REV_CH4_EXP_20_1_09_Q003`, `REV_CH4_EXP_20_1_09_Q004`, `REV_CH4_EXP_20_1_09_Q005`, `REV_CH4_EXP_20_1_09_Q007`, `REV_CH4_EXP_20_1_09_Q009`, `REV_CH4_EXP_20_1_09_Q010`, `REV_CH4_EXP_20_1_09_Q011`, `REV_CH4_EXP_20_1_09_Q012`, `REV_CH4_EXP_20_1_09_Q013`, `REV_CH4_EXP_20_1_09_Q014`, `REV_CH4_EXP_20_1_09_Q018`, `REV_CH4_EXP_20_1_09_Q020`, `REV_CH4_EXP_20_1_09_Q023`, `REV_CH4_EXP_20_1_09_Q024`, `REV_CH4_EXP_20_1_09_Q025`, `REV_CH4_EXP_20_1_09_Q026`, `REV_CH4_EXP_20_2_01_Q022`, `REV_CH4_EXP_20_2_02_Q004`, `REV_CH4_EXP_20_2_03_Q007`, `REV_CH4_EXP_20_2_03_Q018`, `REV_CH4_EXP_20_2_04_Q008`, `REV_CH4_EXP_20_2_04_Q009`, `REV_CH4_EXP_20_2_04_Q010`, `REV_CH4_EXP_20_2_04_Q016`, `REV_CH4_EXP_20_2_04_Q019`

## Per-question Repair Log

| question_id | Before problem | Student-facing repair direction | Answer changed | Point keys changed | Supporting theory |
|---|---|---|---|---|---|
| REV_CH4_EXP_20_1_02_Q001 | `diagnostic_note` used internal packet wording. | Reworded as the ammonia-complex observation, not package status. | No | No | No |
| REV_CH4_EXP_20_1_02_Q003 | Diagnostics mixed formula/meta shorthand. | Reworded distractor feedback as natural copper-ammonia observation errors. | No | No | No |
| REV_CH4_EXP_20_1_02_Q004 | Diagnostic said `本小包`. | Reworded as the current experiment scope. | No | No | No |
| REV_CH4_EXP_20_1_02_Q008 | Diagnostic exposed `点位`. | Reworded as the sulfuric copper and ammonia operation. | No | No | Yes |
| REV_CH4_EXP_20_1_02_Q009 | Diagnostic exposed stability `点位`. | Reworded as acid, base, and heat stability tests. | No | No | No |
| REV_CH4_EXP_20_1_02_Q018 | Option said the stability test only `考查` light and magnetism. | Reworded as a false claim about involving light and magnetism. | No | No | Yes |
| REV_CH4_EXP_20_1_02_Q023 | Stem/explanation discussed rewriting as choice and mobile input. | Rebuilt wording around the concrete ammonia precipitate behavior. | No | No | No |
| REV_CH4_EXP_20_1_02_Q024 | Diagnostics exposed `点位`. | Reworded as directly observed ammonia reaction outcomes. | No | No | No |
| REV_CH4_EXP_20_1_02_Q025 | Stem used `题目要考查`; option used formula-only distractors. | Reworded as ammonia observation; distractors use Chinese compound names. | No | No | No |
| REV_CH4_EXP_20_1_02_Q026 | Explanation discussed original fill blank and input risk. | Reworded as evidence from the five metal-salt comparison. | No | No | No |
| REV_CH4_EXP_20_1_02_Q028 | Stem/explanation used `考查` and `题干` perspective. | Reworded as simultaneous experimental judgment and observation coverage. | No | No | No |
| REV_CH4_EXP_20_1_02_Q029 | Stem asked which `考查` needed broad comparison. | Reworded as which experimental task needs the five-salt comparison. | No | No | No |
| REV_CH4_EXP_20_1_03_Q016 | Stem began from `某题只问`. | Reworded as explaining the AgI ammonia comparison without item-language framing. | No | No | Yes |
| REV_CH4_EXP_20_1_03_Q021 | Explanation said the judgment `考查` object confusion. | Reworded as distinguishing the silver-halide and copper-complex operations. | No | No | Yes |
| REV_CH4_EXP_20_1_03_Q030 | Explanation exposed mobile and machine-grading rationale. | Reworded as direct evidence from the KBr addition step. | No | No | No |
| REV_CH4_EXP_20_1_04_Q006 | Diagnostic said `本题重点`. | Reworded as the key chemistry of the redox reaction. | No | No | Yes |
| REV_CH4_EXP_20_1_04_Q014 | Stem used `题目要求`. | Reworded as deciding whether CuI is hard to dissolve from the operation. | No | No | Yes |
| REV_CH4_EXP_20_1_04_Q018 | Stem/option/explanation used item-design and `考查` language. | Reworded as verifying CuI and iodine by connected observations. | No | No | Yes |
| REV_CH4_EXP_20_1_04_Q019 | Stem/explanation exposed mobile and machine-grading concerns. | Reworded as a chemistry-object judgment about iodine formation. | No | No | Yes |
| REV_CH4_EXP_20_1_04_Q021 | Explanation contained abnormal spacing. | Normalized to natural Chinese about CuI formation. | No | No | No |
| REV_CH4_EXP_20_1_04_Q025 | Stem used `考查内容`. | Reworded as whether CuCl and Cu2O formation belong to the same experiment content. | No | No | No |
| REV_CH4_EXP_20_1_04_Q030 | Explanation exposed mobile wording. | Reworded as iodine being the product indicated by the reaction. | No | No | Yes |
| REV_CH4_EXP_20_1_05_Q003 | Diagnostic exposed adjacent packet number. | Reworded as the neighboring copper-iodide experiment. | No | No | Yes |
| REV_CH4_EXP_20_1_05_Q007 | Explanation said the item used Chinese to avoid formula memory. | Reworded as direct evidence from the CuCl2 solid step. | No | No | No |
| REV_CH4_EXP_20_1_05_Q009 | Diagnostic exposed `点位`. | Reworded as the complete CuCl formation and property-test sequence. | No | No | Yes |
| REV_CH4_EXP_20_1_05_Q012 | Stem used `最适合考查`. | Reworded as the operation matching the CuCl concentrated-ammonia experiment. | No | No | No |
| REV_CH4_EXP_20_1_05_Q013 | Stem used `最适合考查`. | Reworded as the operation matching the CuCl concentrated-HCl experiment. | No | No | No |
| REV_CH4_EXP_20_1_05_Q015 | Option text contained abnormal Chinese spacing. | Removed the extra space in the experimental-step wording. | No | No | Yes |
| REV_CH4_EXP_20_1_05_Q020 | Diagnostic exposed `点位`. | Reworded as the observed CuCl property experiment. | No | No | No |
| REV_CH4_EXP_20_1_05_Q023 | Explanation contained abnormal Chinese spacing. | Removed the extra space in the experimental-step wording. | No | No | No |
| REV_CH4_EXP_20_1_05_Q030 | Explanation exposed deterministic-grading wording. | Reworded as sodium sulfite causing Cu(II) to Cu(I) reduction, so the blank is "还原剂". | No | No | Yes |
| REV_CH4_EXP_20_1_06_Q010 | Diagnostic exposed `点位`. | Reworded as the continuous copper-sugar experiment mainline. | No | No | Yes |
| REV_CH4_EXP_20_1_06_Q013 | Explanation contained abnormal Chinese spacing. | Normalized the experiment-step wording. | No | No | No |
| REV_CH4_EXP_20_1_06_Q017 | Diagnostic exposed `点位`. | Reworded as the relevant experimental section. | No | No | Yes |
| REV_CH4_EXP_20_1_06_Q021 | Explanation exposed mobile/publish wording. | Reworded as the reaction mixture turning blue. | No | No | Yes |
| REV_CH4_EXP_20_1_06_Q024 | Explanation referred to `填空答案`. | Reworded as direct evidence from the glucose step. | No | No | Yes |
| REV_CH4_EXP_20_1_06_Q025 | Explanation exposed mobile wording. | Reworded as the use of water-bath heating. | No | No | No |
| REV_CH4_EXP_20_1_07_Q018 | Diagnostic referred to a previous small packet. | Reworded as the previous copper-compound experiment. | No | No | No |
| REV_CH4_EXP_20_1_07_Q019 | Explanation said the item was changed into a structure question. | Reworded as understanding Hg(I) from its dimeric structure. | No | No | Yes |
| REV_CH4_EXP_20_1_07_Q021 | Explanation said the item only accepted Chinese reagent names. | Reworded as direct evidence from the mercury nitrate step. | No | No | No |
| REV_CH4_EXP_20_1_07_Q024 | Explanation exposed publish-question wording. | Reworded as the experimental step requiring mercury addition. | No | No | Yes |
| REV_CH4_EXP_20_1_08_Q011 | Explanation contained abnormal Chinese spacing. | Removed the extra space before the experimental step phrase. | No | No | No |
| REV_CH4_EXP_20_1_08_Q017 | Diagnostic said `不是本题核心`. | Reworded as not being the experiment's comparison target. | No | No | Yes |
| REV_CH4_EXP_20_1_08_Q028 | Explanation said not to simplify `本题`. | Reworded as a chemistry warning not to stop at red precipitate recall. | No | No | Yes |
| REV_CH4_EXP_20_1_08_Q030 | Explanation exposed publish-question wording. | Reworded as the use of the previous Hg(I) solution. | No | No | No |
| REV_CH4_EXP_20_1_09_Q001 | Stem/diagnostic used small-design-item framing. | Reworded as the target cation group for the separation experiment. | No | No | No |
| REV_CH4_EXP_20_1_09_Q002 | Stem/diagnostics used design-item framing. | Reworded as the first experimental constraint in the separation task. | No | No | No |
| REV_CH4_EXP_20_1_09_Q003 | Explanation used `设计题` phrasing. | Reworded as what a valid separation-detection scheme must state. | No | No | No |
| REV_CH4_EXP_20_1_09_Q004 | Stem used `设计题`. | Reworded as the chemistry requirement for a separation-detection scheme. | No | No | No |
| REV_CH4_EXP_20_1_09_Q005 | Explanation/diagnostic mentioned machine certainty and scoring. | Reworded as direct experimental evidence for a detection basis. | No | No | No |
| REV_CH4_EXP_20_1_09_Q007 | Explanation used small-design-item wording. | Reworded as the experimental requirement for silver recovery. | No | No | Yes |
| REV_CH4_EXP_20_1_09_Q009 | Diagnostic used internal point-language. | Reworded as the stable silver-thiosulfate structure that must be handled. | No | No | Yes |
| REV_CH4_EXP_20_1_09_Q010 | Stem/diagnostic used `作答`. | Reworded as the scheme focus shared by the two design tasks. | No | No | No |
| REV_CH4_EXP_20_1_09_Q011 | Explanation had abnormal spacing. | Removed the extra space before the experimental-design requirement. | No | No | No |
| REV_CH4_EXP_20_1_09_Q012 | Stem/options used `分离检出题` and fixed-recall-item wording. | Reworded as an experimental task and design-task classification. | No | No | No |
| REV_CH4_EXP_20_1_09_Q013 | Stem/explanation used scoring/item framing. | Reworded as whether the design scheme completes the assigned goal. | No | No | No |
| REV_CH4_EXP_20_1_09_Q014 | Diagnostic used design-item wording. | Reworded as an open but evidence-checkable experimental scheme. | No | No | No |
| REV_CH4_EXP_20_1_09_Q018 | Diagnostic said a distractor did not belong to `该题`. | Reworded as not belonging to separation-detection design. | No | No | No |
| REV_CH4_EXP_20_1_09_Q020 | Explanation began `本题出自`. | Reworded as the small design experiment belonging to ds-block compound properties. | No | No | No |
| REV_CH4_EXP_20_1_09_Q023 | Explanation used `分离检出题`. | Reworded as the separation-detection scheme. | No | No | No |
| REV_CH4_EXP_20_1_09_Q024 | Stem/explanation used small-design-item and `考查点` phrasing. | Reworded as direct judgment from design goals and detection evidence. | No | No | No |
| REV_CH4_EXP_20_1_09_Q025 | Stem/diagnostic used item and answer-structure language. | Reworded as the most reasonable experimental scheme structure. | No | No | No |
| REV_CH4_EXP_20_1_09_Q026 | Explanation/diagnostic used `本题` and abnormal spacing. | Reworded as directly judgeable chemical facts from the experiment text. | No | No | No |
| REV_CH4_EXP_20_2_01_Q022 | Diagnostic said `本题考查目的`. | Reworded as the acid-base test purpose. | No | No | Yes |
| REV_CH4_EXP_20_2_02_Q004 | Diagnostic said `本题体系`. | Reworded as the ferrous precipitate standing-observation system. | No | No | Yes |
| REV_CH4_EXP_20_2_03_Q007 | Diagnostic said `本题所需`. | Reworded as suitability for this oxidizing-gas test. | No | No | Yes |
| REV_CH4_EXP_20_2_03_Q018 | Diagnostic said `本题问`. | Reworded as the reaction showing chloride oxidation ability. | No | No | Yes |
| REV_CH4_EXP_20_2_04_Q008 | Explanation contained abnormal Chinese spacing. | Removed the extra space in the experiment-step section phrase. | No | No | No |
| REV_CH4_EXP_20_2_04_Q009 | Option used `只考查`. | Reworded as only comparing filtration speed. | No | No | Yes |
| REV_CH4_EXP_20_2_04_Q010 | Explanation contained abnormal Chinese spacing. | Removed the extra space in the manganese-compound experiment phrase. | No | No | No |
| REV_CH4_EXP_20_2_04_Q016 | Explanation contained abnormal Chinese spacing. | Removed the extra space after `实验小节`. | No | No | No |
| REV_CH4_EXP_20_2_04_Q019 | Stem used `用于考查`. | Reworded as comparing Mn(VII) oxidizing ability in different media. | No | No | No |

## Retained After Semantic Review

These 29 questions still contain `设计` or related wording in student-facing fields, but the term is used in the chemistry-experiment sense: designing a scheme, test-tube group, comparison, or separation route. They do not discuss question-bank review, point binding, evidence scope, scoring, mobile input, or machine grading.

| question_id | Retained wording summary | Reason retained |
|---|---|---|
| REV_CH4_EXP_20_1_02_Q006 | Inner/outer-sphere design and CCl4 extraction distractor. | Valid CuSO4 complex inner/outer-sphere experimental design. |
| REV_CH4_EXP_20_1_02_Q011 | Design experiment to determine CuSO4-ammonia complex inner/outer sphere. | Valid textbook experiment task. |
| REV_CH4_EXP_20_1_02_Q015 | Judgment about replacing the inner/outer-sphere design by CCl4 extraction. | Valid experiment-method comparison. |
| REV_CH4_EXP_20_1_02_Q022 | Fill blank for outer sphere in the design experiment. | Valid chemistry design target, not item-design metadata. |
| REV_CH4_EXP_20_1_03_Q001 | Design AgCl/AgBr/AgI test-tube group. | Valid experimental comparison design. |
| REV_CH4_EXP_20_1_05_Q002 | Role of sodium sulfite in the experiment design. | Valid reagent-function reasoning. |
| REV_CH4_EXP_20_1_05_Q010 | CuCl formation design is not simply chloride addition. | Valid explanation of experimental design logic. |
| REV_CH4_EXP_20_1_07_Q027 | Design uses the same NaCl reagent to compare Hg(II)/Hg(I). | Valid control-comparison design. |
| REV_CH4_EXP_20_1_09_Q006 | What to avoid in separation-detection design. | Valid open experimental-scheme requirement. |
| REV_CH4_EXP_20_1_09_Q008 | Silver recovery design final form. | Valid experimental design objective. |
| REV_CH4_EXP_20_1_09_Q015 | Waste fixer silver species and design background. | Valid chemistry design background. |
| REV_CH4_EXP_20_1_09_Q016 | True/false target ions in the small design experiment. | Valid experiment task statement. |
| REV_CH4_EXP_20_1_09_Q019 | Silver-thiosulfate complex in recovery design. | Valid chemical rationale for the design. |
| REV_CH4_EXP_20_1_09_Q022 | A reagent name alone cannot complete the design. | Valid requirement for scheme completeness. |
| REV_CH4_EXP_20_1_09_Q028 | Final AgNO3 form in recovery design. | Valid design target. |
| REV_CH4_EXP_20_1_09_Q029 | Thiosulfate complex is key background for recovery design. | Valid chemical background. |
| REV_CH4_EXP_20_1_09_Q030 | Fill blank for detection evidence in design. | Valid deterministic fill-blank about the scheme. |
| REV_CH4_EXP_20_2_02_Q017 | Fractional processing as an experiment-design idea. | Valid experimental planning concept. |
| REV_CH4_EXP_20_2_04_Q028 | Correct design for three-media permanganate/sulfite experiment. | Valid comparison-design question. |
| REV_CH4_EXP_20_2_05_Q001 | Chromium test-tube series design. | Valid redox-conversion experimental design. |
| REV_CH4_EXP_20_2_05_Q002 | Hydrogen peroxide in chromium conversion design. | Valid reagent selection in design. |
| REV_CH4_EXP_20_2_05_Q005 | Core design objective of chromium series. | Valid experimental design purpose. |
| REV_CH4_EXP_20_2_05_Q016 | Reagent group for chromium oxidation-state conversion design. | Valid reagent-combination design. |
| REV_CH4_EXP_20_2_05_Q017 | Tungsten reagent not belonging to chromium design. | Valid cross-experiment discrimination. |
| REV_CH4_EXP_20_2_05_Q019 | Design of the tungsten experiment. | Valid procedure-design judgment. |
| REV_CH4_EXP_20_2_05_Q020 | Chromium medium-related conversion design. | Valid module description. |
| REV_CH4_EXP_20_2_05_Q021 | Compare media in chromium conversion design. | Valid variable-comparison design. |
| REV_CH4_EXP_20_2_05_Q022 | Series test-tube design in different media. | Valid contrast-design requirement. |
| REV_CH4_EXP_20_2_05_Q028 | Hydrogen peroxide and sodium hydroxide in chromium design. | Valid reagent-use explanation. |

## Evidence and Determinism Notes

- Every modified hit was reviewed with its `stem`, `options`, `answer`, `explanation`, `primary_point_keys`, `secondary_point_keys`, `option_links`, `source_audit`, `video_points`, and `evidence_sources`.
- No answer value was changed. Existing deterministic answer forms remain:
  - Single choice: `answer.value` is one of `A/B/C/D`.
  - True/false: `answer.value` is boolean.
  - Fill blank: `accepted_answers` is a finite list of accepted Chinese strings.
- No point keys were changed. Option-link labels were kept aligned to their question options; diagnostic notes were naturalized where they exposed internal review language.
- No new supporting theory dependency was introduced. Questions already requiring supporting theory still rely on the same `source_audit.supporting_theory_chunk_ids`.
- RAG id existence check: 37 unique cited evidence ids were found across the two evidence JSONL sources; missing ids: 0.

## Final Validation

- JSON parse: pass, 0 parse errors.
- Rebuilt JSON file count: pass, 15 files.
- Total question count: pass, 450 questions.
- Type counts: 300 single choice, 90 true/false, 60 fill blank.
- Single-choice answer/options/option_links: pass, 300/300 have 4 options, answer label in `A/B/C/D`, and matching `option_links` labels.
- True/false deterministic answers: pass, 90/90 boolean answers.
- Fill-blank deterministic answers: pass, 60/60 have non-empty `accepted_answers`.
- RAG id format and existence: pass, 37 unique ids, 0 missing from evidence sources.
- Student-visible raw id/backtick/internal locator/packet-like code: pass, 0 hits.
- Student-visible ASCII digit formula: pass, 0 hits.
- Student-visible ASCII valence: pass, 0 hits.
- Chinese abnormal spacing: pass, 0 hits.
- Student-facing review language: pass, 0 hits for `题库/审查/题干/题目/出题/点位/本点位/视频点位/证据范围/教材依据/选项反馈/机器判分/稳定判分/移动端/发布题/考查/本题/作答/评分/RAG/canonical/packet/evidence-first`.
