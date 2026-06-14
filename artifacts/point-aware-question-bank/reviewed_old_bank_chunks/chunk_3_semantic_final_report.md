# chunk_3 semantic_final_v1 逐题语义终审报告

## 总览

- 总题数：450

- keep：411

- rewrite：39

- reject：0

- 输出文件：`E:/chemistry-admin/artifacts/point-aware-question-bank/reviewed_old_bank_chunks/chunk_3_semantic_final_v1.json`

- 生成时间：2026-06-14T12:27:32.926763+00:00


## 终审说明

本轮已按题逐题语义终审：逐题读取 original_question 的题干、选项、答案、解析；检查已有 proposed_question；对照本实验 formal video_points；核对 canonical 实验教材原文；当题目判断涉及现象、产物、颜色、价态、两性、氧化还原强弱等教材步骤之外的化学结论时，已在 source_audit 中标注 supporting theory 依赖。脚本只用于把人工终审决定表落盘、统计和校验，不用于批量替代语义判断。


## 修改过的题目列表

- 19-6-02: Q001（point binding revised; option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（option_links rewritten; source_audit refreshed）；Q004（option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（option_links rewritten; source_audit refreshed）；Q011（point binding revised; source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（source_audit refreshed）；Q014（source_audit refreshed）；Q015（source_audit refreshed）；Q016（source_audit refreshed）；Q017（source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（source_audit refreshed）；Q021（point binding revised; source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（source_audit refreshed）；Q024（source_audit refreshed）；Q025（source_audit refreshed）；Q026（source_audit refreshed）；Q027（source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（source_audit refreshed）；Q030（source_audit refreshed）
- 19-6-03: Q001（option_links rewritten; source_audit refreshed）；Q002（option_links rewritten; source_audit refreshed）；Q003（option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（point binding revised; option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（source_audit refreshed）；Q014（source_audit refreshed）；Q015（source_audit refreshed）；Q016（source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（source_audit refreshed）；Q021（source_audit refreshed）；Q022（source_audit refreshed）；Q023（source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（source_audit refreshed）；Q027（source_audit refreshed）；Q028（source_audit refreshed）；Q029（source_audit refreshed）；Q030（source_audit refreshed）
- 19-6-04: Q001（option_links rewritten; source_audit refreshed）；Q002（option_links rewritten; source_audit refreshed）；Q003（option_links rewritten; source_audit refreshed）；Q004（option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（source_audit refreshed）；Q013（source_audit refreshed）；Q014（source_audit refreshed）；Q015（source_audit refreshed）；Q016（source_audit refreshed）；Q017（source_audit refreshed）；Q018（source_audit refreshed）；Q019（source_audit refreshed）；Q020（source_audit refreshed）；Q021（source_audit refreshed）；Q022（source_audit refreshed）；Q023（source_audit refreshed）；Q024（source_audit refreshed）；Q025（source_audit refreshed）；Q026（source_audit refreshed）；Q027（source_audit refreshed）；Q028（source_audit refreshed）；Q029（source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 19-8-01: Q001（option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（point binding revised; source_audit refreshed）；Q014（decision/rewrite: direct_concentration_recall; point binding revised; source_audit refreshed）；Q015（source_audit refreshed）；Q016（source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（source_audit refreshed）；Q019（source_audit refreshed）；Q020（point binding revised; source_audit refreshed）；Q021（source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（source_audit refreshed）；Q030（point binding revised; option_links rewritten; source_audit refreshed）
- 19-8-02: Q001（option_links rewritten; source_audit refreshed）；Q002（option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（point binding revised; option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（point binding revised; source_audit refreshed）；Q012（source_audit refreshed）；Q013（point binding revised; source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（point binding revised; source_audit refreshed）；Q020（decision/rewrite: meta_or_off_target_statement; point binding revised; source_audit refreshed）；Q021（source_audit refreshed）；Q022（source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（source_audit refreshed）；Q027（source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（point binding revised; source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 19-8-03: Q001（point binding revised; option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（point binding revised; source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（point binding revised; source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（decision/rewrite: ambiguous_wrong_polarity; point binding revised; source_audit refreshed）；Q021（point binding revised; source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（source_audit refreshed）；Q030（decision/rewrite: mobile_fill_blank_too_complex_and_corrupt_v1; option_links rewritten; source_audit refreshed）
- 19-8-04: Q001（option_links rewritten; source_audit refreshed）；Q002（option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（point binding revised; source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（source_audit refreshed）；Q017（source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（point binding revised; source_audit refreshed）；Q021（source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（source_audit refreshed）；Q024（decision/rewrite: direct_concentration_recall; point binding revised; option_links rewritten; source_audit refreshed）；Q025（source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（source_audit refreshed）；Q029（point binding revised; source_audit refreshed）；Q030（source_audit refreshed）
- 19-8-05: Q001（point binding revised; option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（point binding revised; option_links rewritten; source_audit refreshed）；Q010（option_links rewritten; source_audit refreshed）；Q011（point binding revised; source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（point binding revised; source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（source_audit refreshed）；Q019（point binding revised; source_audit refreshed）；Q020（source_audit refreshed）；Q021（point binding revised; source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（point binding revised; source_audit refreshed）；Q030（source_audit refreshed）
- 19-8-06: Q001（point binding revised; option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（option_links rewritten; source_audit refreshed）；Q004（option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（source_audit refreshed）；Q016（point binding revised; source_audit refreshed）；Q017（source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（point binding revised; source_audit refreshed）；Q021（source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（source_audit refreshed）；Q024（source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（source_audit refreshed）；Q029（source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 19-8-07: Q001（option_links rewritten; source_audit refreshed）；Q002（option_links rewritten; source_audit refreshed）；Q003（option_links rewritten; source_audit refreshed）；Q004（option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（source_audit refreshed）；Q016（source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（source_audit refreshed）；Q019（source_audit refreshed）；Q020（source_audit refreshed）；Q021（point binding revised; source_audit refreshed）；Q022（source_audit refreshed）；Q023（source_audit refreshed）；Q024（source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（source_audit refreshed）；Q028（source_audit refreshed）；Q029（point binding revised; source_audit refreshed）；Q030（source_audit refreshed）
- 19-8-08: Q001（point binding revised; option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（point binding revised; option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（point binding revised; source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（point binding revised; source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（point binding revised; source_audit refreshed）；Q017（point binding revised; source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（decision/rewrite: ambiguous_true_false_polarity; point binding revised; source_audit refreshed）；Q020（point binding revised; source_audit refreshed）；Q021（point binding revised; option_links rewritten; source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（point binding revised; source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 19-8-09: Q001（option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（point binding revised; source_audit refreshed）；Q017（source_audit refreshed）；Q018（source_audit refreshed）；Q019（point binding revised; source_audit refreshed）；Q020（source_audit refreshed）；Q021（source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（source_audit refreshed）；Q025（point binding revised; source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（point binding revised; source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 19-8-10: Q001（point binding revised; option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（option_links rewritten; source_audit refreshed）；Q007（point binding revised; option_links rewritten; source_audit refreshed）；Q008（point binding revised; option_links rewritten; source_audit refreshed）；Q009（option_links rewritten; source_audit refreshed）；Q010（point binding revised; option_links rewritten; source_audit refreshed）；Q011（point binding revised; source_audit refreshed）；Q012（source_audit refreshed）；Q013（source_audit refreshed）；Q014（source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（point binding revised; source_audit refreshed）；Q017（source_audit refreshed）；Q018（source_audit refreshed）；Q019（source_audit refreshed）；Q020（point binding revised; source_audit refreshed）；Q021（point binding revised; source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（source_audit refreshed）；Q024（source_audit refreshed）；Q025（source_audit refreshed）；Q026（source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（source_audit refreshed）；Q029（source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 19-8-11: Q001（option_links rewritten; source_audit refreshed）；Q002（point binding revised; option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（option_links rewritten; source_audit refreshed）；Q006（option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（option_links rewritten; source_audit refreshed）；Q009（point binding revised; option_links rewritten; source_audit refreshed）；Q010（decision/rewrite: outside_formal_video_point_scope; point binding revised; option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（point binding revised; source_audit refreshed）；Q013（point binding revised; source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（source_audit refreshed）；Q016（source_audit refreshed）；Q017（source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（source_audit refreshed）；Q021（source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（source_audit refreshed）；Q030（point binding revised; source_audit refreshed）
- 20-1-01: Q001（option_links rewritten; source_audit refreshed）；Q002（option_links rewritten; source_audit refreshed）；Q003（point binding revised; option_links rewritten; source_audit refreshed）；Q004（point binding revised; option_links rewritten; source_audit refreshed）；Q005（point binding revised; option_links rewritten; source_audit refreshed）；Q006（point binding revised; option_links rewritten; source_audit refreshed）；Q007（option_links rewritten; source_audit refreshed）；Q008（option_links rewritten; source_audit refreshed）；Q009（point binding revised; option_links rewritten; source_audit refreshed）；Q010（decision/rewrite: meta_item_not_student_chemistry; point binding revised; option_links rewritten; source_audit refreshed）；Q011（source_audit refreshed）；Q012（source_audit refreshed）；Q013（source_audit refreshed）；Q014（point binding revised; source_audit refreshed）；Q015（point binding revised; source_audit refreshed）；Q016（source_audit refreshed）；Q017（source_audit refreshed）；Q018（point binding revised; source_audit refreshed）；Q019（source_audit refreshed）；Q020（source_audit refreshed）；Q021（source_audit refreshed）；Q022（point binding revised; source_audit refreshed）；Q023（point binding revised; source_audit refreshed）；Q024（point binding revised; source_audit refreshed）；Q025（source_audit refreshed）；Q026（point binding revised; source_audit refreshed）；Q027（point binding revised; source_audit refreshed）；Q028（point binding revised; source_audit refreshed）；Q029（source_audit refreshed）；Q030（point binding revised; source_audit refreshed）


## rewrite 题目与原因

- 19-6-02 Q017：wrong_safety_polarity；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-6-03 Q017：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-6-03 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-6-03 Q020：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-6-04 Q018：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-6-04 Q020：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-01 Q002：direct_concentration_recall；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-01 Q014：direct_concentration_recall
- 19-8-01 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-01 Q030：direct_concentration_recall；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-02 Q020：meta_or_off_target_statement
- 19-8-03 Q020：ambiguous_wrong_polarity
- 19-8-03 Q030：mobile_fill_blank_too_complex_and_corrupt_v1
- 19-8-04 Q018：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-04 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-04 Q020：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-04 Q024：direct_concentration_recall
- 19-8-05 Q018：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-05 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-06 Q017：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-06 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-08 Q019：ambiguous_true_false_polarity
- 19-8-08 Q021：mobile_fill_blank_too_complex；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-09 Q017：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-09 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-09 Q020：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-10 Q018：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-10 Q019：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-11 Q006：outside_formal_video_point_scope；rewritten_with_replacement
- 19-8-11 Q007：outside_formal_video_point_scope；rewritten_with_replacement
- 19-8-11 Q010：outside_formal_video_point_scope
- 19-8-11 Q015：outside_formal_video_point_scope；rewritten_with_replacement
- 19-8-11 Q017：confusing_double_negative；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-11 Q019：confusing_double_negative；outside_formal_video_point_scope；rewritten_with_replacement
- 19-8-11 Q020：confusing_double_negative；outside_formal_video_point_scope；rewritten_with_replacement
- 19-8-11 Q026：outside_formal_video_point_scope；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-11 Q027：outside_formal_video_point_scope；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 19-8-11 Q028：outside_formal_video_point_scope；rewritten_with_replacement；theory_dependent_for_outcome_or_property
- 20-1-01 Q010：meta_item_not_student_chemistry


## 仍保留但质量偏低的题目列表及理由

- 19-6-02 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q006：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q010：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q011：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q012：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q013：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q014：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q015：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q016：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q018：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q019：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q020：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-02 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-02 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q002：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-03 Q006：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-03 Q009：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-03 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-03 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-6-04 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-6-04 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-01 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-01 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-02 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q002：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q003：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q005：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q008：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q009：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q011：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q012：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q013：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q014：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q015：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q016：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q017：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q018：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q019：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-03 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-03 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q008：safety item is only indirectly tied to the formal point; kept because it is operationally relevant and deterministic.
- 19-8-04 Q016：safety item is indirectly supported rather than a discrete video action.
- 19-8-04 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q028：fill blank asks waste handling rather than a visible step; retained with indirect safety rationale.
- 19-8-04 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-04 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-05 Q002：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-05 Q003：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-05 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-05 Q020：safety item spans the whole heavy-metal set and is weakly point-specific.
- 19-8-05 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-05 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-06 Q005：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-06 Q006：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-06 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-06 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-07 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-07 Q005：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-07 Q006：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-07 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-07 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q002：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q003：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q005：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q011：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q012：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q013：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q014：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q015：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q016：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q017：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q018：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q020：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-08 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-08 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q003：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-09 Q006：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-09 Q008：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-09 Q009：safety item is canonical/theory safety support rather than a direct point observation.
- 19-8-09 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q027：fill blank safety action is indirectly supported and simple.
- 19-8-09 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-09 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-10 Q002：FeCl3/KSCN check appears in canonical redox text but the formal point title names the HgCl2/SnCl2 branch; bound to Sn(II) reducing point with note.
- 19-8-10 Q003：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-10 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q022：same point-scope mismatch as the KSCN single-choice item; retained because canonical supports it.
- 19-8-10 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-10 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-11 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-11 Q003：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-11 Q016：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 19-8-11 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-11 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-11 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-11 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-11 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 19-8-11 Q029：mentions the broader textbook small-design task, while formal video points focus on Pb3O4 analysis.
- 19-8-11 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q001：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 20-1-01 Q004：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 20-1-01 Q005：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 20-1-01 Q009：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 20-1-01 Q011：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 20-1-01 Q019：basic direct recall of reagent/object/color/procedure; retained only because it is point-bound and machine-deterministic.
- 20-1-01 Q021：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q022：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q023：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q024：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q025：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q026：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q027：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q028：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q029：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.
- 20-1-01 Q030：short fill blank mainly recalls a reagent, ion, formula, color, or one-word property; deterministic but low discrimination.


## evidence insufficient 的题目列表

- 无


## 多点位题目列表

- 19-6-03: Q003: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做”；Q005: 镁条与冷水反应 / 镁条与热水反应；Q007: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做”；Q009: 镁条与冷水反应 / 镁条与热水反应；Q010: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做” / 镁条与冷水反应 / 镁条与热水反应 / 金属钙与水反应；Q013: 镁条与冷水反应 / 镁条与热水反应；Q016: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做”；Q017: 镁条与冷水反应 / 镁条与热水反应；Q018: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做” / 镁条与冷水反应 / 镁条与热水反应 / 金属钙与水反应；Q019: 金属钠与水反应 / 金属钙与水反应；Q020: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做” / 镁条与冷水反应 / 镁条与热水反应 / 金属钙与水反应；Q025: 镁条与冷水反应 / 镁条与热水反应；Q026: 镁条与冷水反应 / 镁条与热水反应；Q030: 金属钠与水反应 / 原文列出金属钾与水反应，但试剂处标注“不采购，不做” / 镁条与冷水反应 / 镁条与热水反应 / 金属钙与水反应
- 19-6-04: Q001: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q002: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q009: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q010: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q011: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q015: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q016: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q017: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q018: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q020: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q021: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q022: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q029: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应；Q030: Li⁺ 焰色反应 / Na⁺ 焰色反应 / K⁺ 焰色反应，需透过钴玻璃观察 / Ca²⁺ 焰色反应 / Sr²⁺ 焰色反应 / Ba²⁺ 焰色反应
- 19-8-01: Q002: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q003: Pb(NO₃)₂ + NaOH / Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q004: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q008: Pb(NO₃)₂ + NaOH / Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q012: Pb(NO₃)₂ + NaOH / Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q013: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q014: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q016: Pb(NO₃)₂ + NaOH / Pb(OH)₂ + NaOH；Q020: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q023: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH；Q024: Pb(NO₃)₂ + NaOH / Pb(OH)₂ + NaOH；Q030: Pb(OH)₂ + HNO₃ / Pb(OH)₂ + NaOH
- 19-8-02: Q005: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q006: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q008: Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q009: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q010: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q015: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q017: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q018: Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q019: Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q020: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q025: Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH；Q028: SnCl₂ + NaOH / Sn(OH)₂ + HCl / Sn(OH)₂ + NaOH
- 19-8-03: Q005: Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q006: Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q007: Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q008: SbCl₃ + NaOH / Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q010: SbCl₃ + NaOH / Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q015: Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q016: Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q017: Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q018: SbCl₃ + NaOH / Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q025: Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q026: Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q027: Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH；Q028: SbCl₃ + NaOH / Sb(OH)₃ + HCl / Sb(OH)₃ + 2 mol/L NaOH / Sb(OH)₃ + 6 mol/L NaOH
- 19-8-04: Q005: Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q006: Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q007: Bi(NO₃)₃ + NaOH / Bi(OH)₃ + HCl / Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q010: Bi(NO₃)₃ + NaOH / Bi(OH)₃ + HCl / Bi(OH)₃ + 40% NaOH；Q013: Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q014: Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q015: Bi(NO₃)₃ + NaOH / Bi(OH)₃ + HCl / Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q024: Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q027: Bi(NO₃)₃ + NaOH / Bi(OH)₃ + HCl / Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH；Q029: Bi(OH)₃ + 6 mol/L NaOH / Bi(OH)₃ + 40% NaOH
- 19-8-05: Q010: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性 / SbCl₃ 制备 Sb(OH)₃，并测试酸碱性 / Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性；Q015: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性；Q016: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性 / SbCl₃ 制备 Sb(OH)₃，并测试酸碱性 / Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性；Q018: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性 / SbCl₃ 制备 Sb(OH)₃，并测试酸碱性 / Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性；Q019: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性；Q020: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性 / SbCl₃ 制备 Sb(OH)₃，并测试酸碱性 / Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性；Q030: SnCl₂ 制备 Sn(OH)₂，并测试酸碱性 / Pb(NO₃)₂ 制备 Pb(OH)₂，并测试酸碱性 / SbCl₃ 制备 Sb(OH)₃，并测试酸碱性 / Bi(NO₃)₃ 制备 Bi(OH)₃，并测试酸碱性
- 19-8-06: Q009: SnCl₂ + FeCl₃ / 比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性；Q010: SnCl₂ + FeCl₃ / SnCl₂ + HgCl₂ / 比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性；Q017: SnCl₂ + FeCl₃ / 比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性；Q019: SnCl₂ + FeCl₃ / 用 KSCN 检验 Fe³⁺ 是否仍存在；Q020: SnCl₂ + FeCl₃ / SnCl₂ + HgCl₂ / 比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性；Q028: SnCl₂ + FeCl₃ / 比较 Sn(II) 与 Fe(II)、Sn(II) 与 Hg(I) 的还原性
- 19-8-07: Q001: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q002: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q003: PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q004: PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q005: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q009: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q010: PbO₂ + 浓 HCl / PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q011: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q013: PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q016: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q017: PbO₂ + 浓 HCl / PbO₂ + H₂SO₄ + MnSO₄，水浴加热；Q018: PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q021: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q022: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q023: PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q024: PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性；Q028: PbO₂ + 浓 HCl / 比较 Pb(IV) 与 Cl₂、Pb(IV) 与 MnO₄⁻ 的氧化性
- 19-8-08: Q001: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水 / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q003: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水；Q004: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水；Q005: 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q010: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水 / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q011: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水 / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q013: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水；Q014: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水；Q015: 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q020: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水 / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q021: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水 / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q023: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水；Q024: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水；Q025: 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水；Q030: 碱性 KMnO₄ 体系中分别加入 AsCl₃、SbCl₃、BiCl₃ / 银氨溶液中分别加入 Na₃AsO₃、Na₃SbO₃、Bi(NO₃)₃ / AsCl₃、SbCl₃ 溶液调至弱酸性后滴加碘水 / Bi(NO₃)₃ + NaOH 生成沉淀后加入氯水
- 19-8-09: Q001: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q007: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q009: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q010: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q011: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q013: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q017: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q018: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q020: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q021: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q024: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应；Q027: Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别酸化后加入 KI 和 CCl₄ / Na[As(OH)₆]、K[Sb(OH)₆]、NaBiO₃ 分别与酸性 MnSO₄ 体系反应
- 19-8-10: Q010: Sn(II) 的还原性：HgCl₂ + SnCl₂ / Pb(IV) 的氧化性：PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / Bi(III) 的还原性和 Bi(V) 的氧化性：Bi(NO₃)₃ + NaOH + 氯水，水浴加热；沉淀再加浓 HCl 并鉴别气体产物；Q020: Sn(II) 的还原性：HgCl₂ + SnCl₂ / Pb(IV) 的氧化性：PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / Bi(III) 的还原性和 Bi(V) 的氧化性：Bi(NO₃)₃ + NaOH + 氯水，水浴加热；沉淀再加浓 HCl 并鉴别气体产物；Q030: Sn(II) 的还原性：HgCl₂ + SnCl₂ / Pb(IV) 的氧化性：PbO₂ + H₂SO₄ + MnSO₄，水浴加热 / Bi(III) 的还原性和 Bi(V) 的氧化性：Bi(NO₃)₃ + NaOH + 氯水，水浴加热；沉淀再加浓 HCl 并鉴别气体产物
- 19-8-11: Q006: 设计分析铅丹 Pb₃O₄ 组成的实验方法 / Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺；Q007: 设计分析铅丹 Pb₃O₄ 组成的实验方法 / Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺；Q009: Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺；Q010: 设计分析铅丹 Pb₃O₄ 组成的实验方法 / Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺；Q015: 设计分析铅丹 Pb₃O₄ 组成的实验方法 / Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺；Q019: 设计分析铅丹 Pb₃O₄ 组成的实验方法 / Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺；Q020: 设计分析铅丹 Pb₃O₄ 组成的实验方法 / Pb₃O₄ + HNO₃，微热 / 吸取清液，用稀 H₂SO₄ 检查 Pb²⁺
- 20-1-01: Q001: CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q002: CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q003: 比较沉淀颜色、形态 / CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q004: ZnSO₄ + NaOH / 检验沉淀酸碱性；Q005: CuSO₄ + NaOH / 比较沉淀颜色、形态；Q006: AgNO₃ + NaOH / 比较沉淀颜色、形态；Q007: 检验沉淀酸碱性 / 检验沉淀热稳定性；Q008: CuSO₄ + NaOH / ZnSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q009: CdSO₄ + NaOH / ZnSO₄ + NaOH / 检验沉淀酸碱性；Q010: 检验沉淀酸碱性 / 检验沉淀热稳定性；Q011: CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q012: 检验沉淀酸碱性 / 检验沉淀热稳定性；Q013: 检验沉淀酸碱性 / 检验沉淀热稳定性；Q014: CuSO₄ + NaOH / 比较沉淀颜色、形态；Q015: ZnSO₄ + NaOH / 检验沉淀酸碱性；Q016: CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q018: AgNO₃ + NaOH / 比较沉淀颜色、形态；Q021: CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH；Q022: CuSO₄ + NaOH / 比较沉淀颜色、形态；Q023: ZnSO₄ + NaOH / 检验沉淀酸碱性；Q026: 检验沉淀酸碱性 / 检验沉淀热稳定性；Q030: CuSO₄ + NaOH / AgNO₃ + NaOH / ZnSO₄ + NaOH / CdSO₄ + NaOH / Hg(NO₃)₂ + NaOH / 比较沉淀颜色、形态 / 检验沉淀酸碱性 / 检验沉淀热稳定性


## 填空题手机端风险列表

以下条目保留了机器确定性判分；有符号/化学式答案的题目均尽量保留中文或短答案别名。v1 中不适合手机输入的长试剂组合已改写为单选。

- 19-6-02 Q026：symbolic aliases ['O₂']; phone-friendly alias retained: ['O₂']
- 19-6-03 Q021：symbolic aliases ['H₂']; phone-friendly alias retained: ['H₂', '氢气']
- 19-6-03 Q027：symbolic aliases ['Ca(OH)₂']; phone-friendly alias retained: ['Ca(OH)₂', '氢氧化钙']
- 19-6-03 Q029：symbolic aliases ['H₂']; phone-friendly alias retained: ['氢气', 'H₂']
- 19-8-01 Q021：symbolic aliases ['Pb(OH)₂']; phone-friendly alias retained: ['Pb(OH)₂', '氢氧化铅']
- 19-8-01 Q022：symbolic aliases ['Pb(NO₃)₂']; phone-friendly alias retained: ['Pb(NO₃)₂', '硝酸铅']
- 19-8-01 Q025：symbolic aliases ['HNO₃']; phone-friendly alias retained: ['HNO₃', '硝酸']
- 19-8-01 Q026：symbolic aliases ['Pb²⁺']; phone-friendly alias retained: ['Pb²⁺', '铅离子']
- 19-8-02 Q021：symbolic aliases ['SnCl₂']; phone-friendly alias retained: ['SnCl₂', '氯化亚锡']
- 19-8-02 Q022：symbolic aliases ['Sn(OH)₂']; phone-friendly alias retained: ['Sn(OH)₂']
- 19-8-03 Q021：symbolic aliases ['SbCl₃']; phone-friendly alias retained: ['SbCl₃']
- 19-8-03 Q023：symbolic aliases ['Sb(OH)₃']; phone-friendly alias retained: ['Sb(OH)₃']
- 19-8-04 Q025：symbolic aliases ['Bi³⁺', '铋(III)']; phone-friendly alias retained: ['Bi³⁺', '铋(III)']
- 19-8-04 Q026：symbolic aliases ['H₂O']; phone-friendly alias retained: ['水', 'H₂O']
- 19-8-04 Q030：symbolic aliases ['OH⁻']; phone-friendly alias retained: ['OH⁻', '氢氧根']
- 19-8-05 Q022：symbolic aliases ['Pb(NO₃)₂']; phone-friendly alias retained: ['Pb(NO₃)₂', '硝酸铅']
- 19-8-05 Q023：symbolic aliases ['SbCl₃']; phone-friendly alias retained: ['SbCl₃', '三氯化锑']
- 19-8-05 Q024：symbolic aliases ['Bi(NO₃)₃']; phone-friendly alias retained: ['Bi(NO₃)₃', '硝酸铋']
- 19-8-06 Q021：symbolic aliases ['SnCl₂']; phone-friendly alias retained: ['SnCl₂', '氯化亚锡']
- 19-8-06 Q023：symbolic aliases ['Fe²⁺']; phone-friendly alias retained: ['Fe²⁺', '亚铁离子']
- 19-8-06 Q024：symbolic aliases ['Sn(IV)', 'Sn⁴⁺']; phone-friendly alias retained: ['Sn(IV)', 'Sn⁴⁺']
- 19-8-06 Q025：symbolic aliases ['Hg₂Cl₂']; phone-friendly alias retained: ['Hg₂Cl₂', '氯化亚汞']
- 19-8-06 Q028：symbolic aliases ['Fe(II)', 'Fe²⁺']; phone-friendly alias retained: ['Fe(II)', 'Fe²⁺']
- 19-8-06 Q029：symbolic aliases ['Hg(II)']; phone-friendly alias retained: ['+2', '二价']
- 19-8-07 Q021：symbolic aliases ['PbO₂']; phone-friendly alias retained: ['PbO₂', '二氧化铅']
- 19-8-07 Q022：symbolic aliases ['Cl₂']; phone-friendly alias retained: ['Cl₂', '氯气']
- 19-8-07 Q023：symbolic aliases ['Mn²⁺', '锰(II)离子']; phone-friendly alias retained: ['Mn²⁺', '锰(II)离子']
- 19-8-07 Q024：symbolic aliases ['MnO₄⁻']; phone-friendly alias retained: ['MnO₄⁻', '高锰酸根']
- 19-8-07 Q025：symbolic aliases ['H₂SO₄']; phone-friendly alias retained: ['H₂SO₄', '硫酸']
- 19-8-07 Q028：symbolic aliases ['Cl⁻']; phone-friendly alias retained: ['Cl⁻', '氯离子']
- 19-8-08 Q022：symbolic aliases ['KMnO₄']; phone-friendly alias retained: ['KMnO₄']
- 19-8-08 Q023：symbolic aliases ['AsCl₃']; phone-friendly alias retained: ['AsCl₃']
- 19-8-08 Q024：symbolic aliases ['SbCl₃']; phone-friendly alias retained: ['SbCl₃']
- 19-8-08 Q025：symbolic aliases ['Bi(NO₃)₃']; phone-friendly alias retained: ['Bi(NO₃)₃']
- 19-8-08 Q027：symbolic aliases ['I₂']; phone-friendly alias retained: ['I₂']
- 19-8-09 Q022：symbolic aliases ['I₂']; phone-friendly alias retained: ['I₂', '碘']
- 19-8-09 Q023：symbolic aliases ['CCl₄']; phone-friendly alias retained: ['CCl₄', '四氯化碳']
- 19-8-09 Q024：symbolic aliases ['NaBiO₃']; phone-friendly alias retained: ['NaBiO₃', '铋酸钠']
- 19-8-09 Q025：symbolic aliases ['MnSO₄']; phone-friendly alias retained: ['MnSO₄', '硫酸锰']
- 19-8-09 Q026：symbolic aliases ['I⁻']; phone-friendly alias retained: ['I⁻', '碘离子']
- 19-8-09 Q028：symbolic aliases ['MnO₄⁻']; phone-friendly alias retained: ['MnO₄⁻', '高锰酸根']
- 19-8-10 Q021：symbolic aliases ['SnCl₂']; phone-friendly alias retained: ['SnCl₂', '氯化亚锡']
- 19-8-10 Q023：symbolic aliases ['PbO₂']; phone-friendly alias retained: ['PbO₂', '二氧化铅']
- 19-8-10 Q024：symbolic aliases ['Cl₂']; phone-friendly alias retained: ['Cl₂', '氯气']
- 19-8-10 Q025：symbolic aliases ['MnO₄⁻']; phone-friendly alias retained: ['MnO₄⁻', '高锰酸根']
- 19-8-10 Q027：symbolic aliases ['I₂']; phone-friendly alias retained: ['I₂', '碘']
- 19-8-10 Q029：symbolic aliases ['HNO₃']; phone-friendly alias retained: ['HNO₃', '硝酸']
- 19-8-11 Q021：symbolic aliases ['Pb₃O₄']; phone-friendly alias retained: ['Pb₃O₄', '四氧化三铅']
- 19-8-11 Q022：symbolic aliases ['HNO₃']; phone-friendly alias retained: ['HNO₃', '硝酸']
- 19-8-11 Q023：symbolic aliases ['H₂SO₄']; phone-friendly alias retained: ['H₂SO₄', '硫酸']
- 19-8-11 Q024：symbolic aliases ['PbSO₄']; phone-friendly alias retained: ['PbSO₄', '硫酸铅']
- 19-8-11 Q025：symbolic aliases ['Pb(IV)', 'Pb⁴⁺']; phone-friendly alias retained: ['Pb(IV)', 'Pb⁴⁺']
- 19-8-11 Q026：symbolic aliases ['Pb²⁺']; phone-friendly alias retained: ['Pb²⁺', 'Pb2+']
- 19-8-11 Q027：symbolic aliases ['Pb²⁺']; phone-friendly alias retained: ['Pb²⁺', 'Pb2+']
- 19-8-11 Q028：symbolic aliases ['Pb²⁺']; phone-friendly alias retained: ['Pb²⁺', 'Pb2+']
- 19-8-11 Q030：symbolic aliases ['SO₄²⁻']; phone-friendly alias retained: ['SO₄²⁻', '硫酸根']
- 20-1-01 Q023：symbolic aliases ['Zn(OH)₂']; phone-friendly alias retained: ['Zn(OH)₂', '氢氧化锌']
- 20-1-01 Q024：symbolic aliases ['Ag₂O']; phone-friendly alias retained: ['Ag₂O']
- 20-1-01 Q027：symbolic aliases ['Cd(OH)₂']; phone-friendly alias retained: ['Cd(OH)₂', '氢氧化镉']


## supporting theory 依赖说明

以下题目的“实验步骤/观察任务”由 canonical 实验原文支撑，但答案中的现象、颜色、产物、价态、酸碱性、氧化性/还原性等判断依赖 supporting theory；对应题目的 source_audit.supporting_theory_chunk_ids 已填入。

- 19-6-02: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-6-03: Q001、Q002、Q004、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q024、Q025、Q026、Q027、Q028、Q029
- 19-6-04: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-01: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-02: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-03: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-04: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-05: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-06: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-07: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-08: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-09: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-10: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030
- 19-8-11: Q004、Q005、Q008、Q014、Q016、Q017、Q018、Q024、Q025、Q026、Q027、Q028、Q030
- 20-1-01: Q001、Q002、Q003、Q004、Q005、Q006、Q007、Q008、Q009、Q010、Q011、Q012、Q013、Q014、Q015、Q016、Q017、Q018、Q019、Q020、Q021、Q022、Q023、Q024、Q025、Q026、Q027、Q028、Q029、Q030


## option_links 终审说明

- 单选题 option_links 已重写为逐选项说明：154 题。

- 正确选项标为 correct_evidence；错误选项按相邻实验、相邻点位、误概念或无关干扰分别标注，并在 diagnostic_note 中说明具体错因。


## 逐题语义终审确认

确认：chunk_3 的 450 道题已经逐题逐字完成语义终审；本终审稿未直接沿用 reviewed_v1 的结论，已修正发现的模板化点位绑定、模板化 option_links、编码损坏 proposed_question、元测试题和不适合手机端的填空题。
