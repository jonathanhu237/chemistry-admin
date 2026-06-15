# chunk_1 student-facing de-meta polish report

## Scope

- Chunk: `chunk_1`
- Packets: `19-1-01, 19-1-02, 19-1-03, 19-1-04, 19-1-05, 19-1-06, 19-1-07, 19-1-08, 19-2-01, 19-2-02, 19-2-03, 19-2-04, 19-2-05, 19-3-01, 19-3-02`
- Rebuilt JSON directory: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_1`
- Report path: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_reports\chunk_1\chunk_1_student_facing_demeta_polish_report.md`
- Release JSON policy: no `chunk_X_release_final_v1.json` was edited. This pass only touched rebuilt JSON files under `rebuilt_packages\chunk_1`.

## Summary

- Total questions scanned: 450
- Meta/display-risk questions found: 65
  - Student-visible review/annotation language: 56
  - Extra display risks found during the same pass: 2 (`Ba(OH)2`; ASCII `-1` / `+7` valence)
- Legitimate experiment-design wording retained after semantic review: 7
- Actually modified questions: 58
- Student-visible risk hits retained without modification: 7
- Internal metadata retained with explanation: point keys, source ids, `option_links`, and `source_audit` may still contain internal identifiers or reviewer language because they are not student-facing answer content.

## Modified Question IDs

`CHUNK1_19_1_01_Q003`, `CHUNK1_19_1_01_Q004`, `CHUNK1_19_1_01_Q005`, `CHUNK1_19_1_01_Q008`, `CHUNK1_19_1_01_Q009`, `CHUNK1_19_1_01_Q011`, `CHUNK1_19_1_01_Q012`, `CHUNK1_19_1_01_Q018`, `CHUNK1_19_1_01_Q021`, `CHUNK1_19_1_01_Q022`, `CHUNK1_19_1_01_Q025`, `CHUNK1_19_1_01_Q027`, `CHUNK1_19_1_04_Q024`, `CHUNK1_19_1_04_Q030`, `CHUNK1_19_2_01_Q027`, `CHUNK1_19_2_04_Q001`, `CHUNK1_19_2_04_Q008`, `CHUNK1_19_2_04_Q009`, `CHUNK1_19_2_04_Q011`, `CHUNK1_19_2_04_Q016`, `CHUNK1_19_2_04_Q018`, `CHUNK1_19_2_05_Q001`, `CHUNK1_19_2_05_Q006`, `CHUNK1_19_2_05_Q007`, `CHUNK1_19_2_05_Q008`, `CHUNK1_19_2_05_Q009`, `CHUNK1_19_2_05_Q011`, `CHUNK1_19_2_05_Q012`, `CHUNK1_19_2_05_Q014`, `CHUNK1_19_2_05_Q016`, `CHUNK1_19_2_05_Q017`, `CHUNK1_19_2_05_Q018`, `CHUNK1_19_2_05_Q019`, `CHUNK1_19_2_05_Q020`, `CHUNK1_19_2_05_Q021`, `CHUNK1_19_2_05_Q023`, `CHUNK1_19_2_05_Q026`, `CHUNK1_19_2_05_Q027`, `CHUNK1_19_2_05_Q030`, `CHUNK1_19_3_02_Q001`, `CHUNK1_19_3_02_Q002`, `CHUNK1_19_3_02_Q003`, `CHUNK1_19_3_02_Q004`, `CHUNK1_19_3_02_Q006`, `CHUNK1_19_3_02_Q007`, `CHUNK1_19_3_02_Q008`, `CHUNK1_19_3_02_Q011`, `CHUNK1_19_3_02_Q012`, `CHUNK1_19_3_02_Q013`, `CHUNK1_19_3_02_Q014`, `CHUNK1_19_3_02_Q016`, `CHUNK1_19_3_02_Q019`, `CHUNK1_19_3_02_Q022`, `CHUNK1_19_3_02_Q023`, `CHUNK1_19_3_02_Q024`, `CHUNK1_19_3_02_Q025`, `CHUNK1_19_3_02_Q029`, `CHUNK1_19_3_02_Q030`

## Per-question Repair Log

| question_id | Before problem | Student-facing repair direction | Answer changed | Point keys changed | Supporting theory |
|---|---|---|---|---|---|
| CHUNK1_19_1_01_Q003 | Used visible "point" wording for one operation. | Reworded as one group of replacement operations and its direct conclusion. | No | No | Yes |
| CHUNK1_19_1_01_Q004 | Used visible "point" wording for Br₂/KI operation. | Reworded as a concrete replacement operation supporting Br₂ > I₂. | No | No | Yes |
| CHUNK1_19_1_01_Q005 | "Three points" appeared in the stem. | Reworded as three groups of replacement operations. | No | No | Yes |
| CHUNK1_19_1_01_Q008 | Asked for "minimum points". | Reworded as minimum operation/evidence combination for full order. | No | No | Yes |
| CHUNK1_19_1_01_Q009 | "Two points" and "point gap" appeared in stem/explanation. | Reworded as two operation groups and the missing Br₂/I₂ comparison. | No | No | Yes |
| CHUNK1_19_1_01_Q011 | Explanation used "point". | Reworded as the corresponding operation group. | No | No | Yes |
| CHUNK1_19_1_01_Q012 | Explanation used "point". | Reworded as the corresponding operation group and direct evidence. | No | No | Yes |
| CHUNK1_19_1_01_Q018 | Stem/explanation used "one point". | Reworded as one operation group and the missing direct comparison. | No | No | Yes |
| CHUNK1_19_1_01_Q021 | Options exposed `candidate-*` ids and explanation used "point". | Removed raw ids; options are now operation groups only. | No | No | Yes |
| CHUNK1_19_1_01_Q022 | Stem said "if the stem wants to prove" and "evidence point". | Reworded as proving Br₂ oxidizing ability over I₂ by operation/observation. | No | No | Yes |
| CHUNK1_19_1_01_Q025 | Stem/option used "points" and "this point". | Reworded as completing three replacement operations and recording the conclusion. | No | No | Yes |
| CHUNK1_19_1_01_Q027 | Internal binding-review question about why a question should bind multiple points. | Rebuilt as a chemistry operation-combination question for deriving Cl₂ > Br₂ > I₂. | No | Yes | Yes |
| CHUNK1_19_1_04_Q024 | Explanation used "this point". | Reworded as the KI-starch paper test operation. | No | No | No |
| CHUNK1_19_1_04_Q030 | Explanation used "this point". | Reworded as this test operation and its blue-color interpretation. | No | No | No |
| CHUNK1_19_2_01_Q027 | Option D had `Ba(OH)2`; stem was close to salt-name recall. | Reworded as identifying the insoluble barium salt product in ozone preparation; fixed `Ba(OH)₂`. | No | No | No |
| CHUNK1_19_2_04_Q001 | Explanation used "this point". | Reworded as H₂O₂ showing oxidizing property in the reaction. | No | No | Yes |
| CHUNK1_19_2_04_Q008 | Explanation used "this point". | Reworded as PbS oxidation showing H₂O₂ oxidizing property. | No | No | Yes |
| CHUNK1_19_2_04_Q009 | Stem used "this point". | Reworded as the acidified KMnO₄ reaction. | No | No | Yes |
| CHUNK1_19_2_04_Q011 | Explanation used "oxidizing point". | Reworded as the acidic H₂O₂/KI reaction system. | No | No | Yes |
| CHUNK1_19_2_04_Q016 | Explanation used "point purpose". | Reworded as the purpose of the comparative AgNO₃ experiments. | No | No | Yes |
| CHUNK1_19_2_04_Q018 | Stem/explanation used "oxidizing point" and "different points". | Reworded as different experimental sections/reaction systems. | No | No | Yes |
| CHUNK1_19_2_05_Q001 | Stem used "two points". | Reworded as two experimental phenomena showing dual redox behavior. | No | No | Yes |
| CHUNK1_19_2_05_Q006 | Stem/explanation used "two points". | Reworded as PbS whitening and KMnO₄ fading experiments. | No | No | Yes |
| CHUNK1_19_2_05_Q007 | Explanation used "this point". | Reworded as the operation using black PbS whitening. | No | No | Yes |
| CHUNK1_19_2_05_Q008 | Explanation used "reducing point". | Reworded as the typical phenomenon showing H₂O₂ reducing property. | No | No | Yes |
| CHUNK1_19_2_05_Q009 | Stem/explanation used "point". | Reworded as which phenomenon shows oxidizing property. | No | No | Yes |
| CHUNK1_19_2_05_Q011 | Visible ASCII valence `-1`; explanation said "two experiment points". | Changed to `−1` and reworded as two experimental groups. | No | No | Yes |
| CHUNK1_19_2_05_Q012 | Stem used "point". | Reworded as which phenomenon shows reducing property. | No | No | Yes |
| CHUNK1_19_2_05_Q014 | Stem used "reducing point". | Reworded as the acidified KMnO₄ reducing-property experiment. | No | No | No |
| CHUNK1_19_2_05_Q016 | Explanation used "point". | Reworded as acidified KMnO₄ reaction evidence. | No | No | Yes |
| CHUNK1_19_2_05_Q017 | Explanation used "reducing point". | Reworded as the core phenomenon showing reducing property. | No | No | Yes |
| CHUNK1_19_2_05_Q018 | Stem used "identification point". | Reworded as H₂O₂ identification experiment phenomenon. | No | No | Yes |
| CHUNK1_19_2_05_Q019 | Explanation used "PbS point". | Reworded as the PbS reaction. | No | No | Yes |
| CHUNK1_19_2_05_Q020 | Explanation used "PbS-related point". | Reworded as PbS-related experiment. | No | No | Yes |
| CHUNK1_19_2_05_Q021 | Explanation used "PbS point" and "KMnO₄ point". | Reworded as PbS reaction and acidified KMnO₄ reaction. | No | No | Yes |
| CHUNK1_19_2_05_Q023 | Explanation used "KMnO₄ point". | Reworded as acidified KMnO₄ reaction. | No | No | Yes |
| CHUNK1_19_2_05_Q026 | Explanation used "KMnO₄ point". | Reworded as acidified KMnO₄ reaction. | No | No | Yes |
| CHUNK1_19_2_05_Q027 | Explanation used "two experiment points"; options had ASCII valence `-1` / `+7`. | Reworded as two operations and changed valence display to `−1` / "正七价". | No | No | Yes |
| CHUNK1_19_2_05_Q030 | Stem/explanation used "two points". | Reworded as two experimental phenomena/reactions. | No | No | Yes |
| CHUNK1_19_3_02_Q001 | Explanation used "reducing point". | Reworded as acidified KMnO₄ used to observe reducing property. | No | No | Yes |
| CHUNK1_19_3_02_Q002 | Explanation used "oxidizing point". | Reworded as H₂S system used to observe oxidizing property. | No | No | Yes |
| CHUNK1_19_3_02_Q003 | Explanation used "reducing point". | Reworded as the acidified KMnO₄ reaction system. | No | No | Yes |
| CHUNK1_19_3_02_Q004 | Explanation used "oxidizing point". | Reworded as the H₂S oxidation observation. | No | No | Yes |
| CHUNK1_19_3_02_Q006 | Explanation used "bleaching point". | Reworded as the fuchsin solution system for bleaching observation. | No | No | Yes |
| CHUNK1_19_3_02_Q007 | Explanation used "reducing point". | Reworded as acidified KMnO₄ reducing-property experiment. | No | No | Yes |
| CHUNK1_19_3_02_Q008 | Explanation used "oxidizing point". | Reworded as the H₂S system observing SO₂ oxidizing property. | No | No | Yes |
| CHUNK1_19_3_02_Q011 | Explanation used "reducing point". | Reworded as acidified KMnO₄ used to observe SO₂ reducing property. | No | No | Yes |
| CHUNK1_19_3_02_Q012 | Explanation referred to "the stem says". | Reworded as "the judgment says". | No | No | Yes |
| CHUNK1_19_3_02_Q013 | Explanation used "oxidizing point". | Reworded as H₂S system observing SO₂ oxidizing property. | No | No | Yes |
| CHUNK1_19_3_02_Q014 | Explanation used "bleaching point". | Reworded as fuchsin solution used to observe bleaching. | No | No | Yes |
| CHUNK1_19_3_02_Q016 | Explanation used "reducing/oxidizing points". | Reworded as reducing/oxidizing reaction systems. | No | No | Yes |
| CHUNK1_19_3_02_Q019 | Explanation used "oxidizing point". | Reworded as H₂S system support for SO₂ oxidizing property. | No | No | Yes |
| CHUNK1_19_3_02_Q022 | Explanation used "reducing point". | Reworded as acidified KMnO₄ system used to observe SO₂ reducing property. | No | No | Yes |
| CHUNK1_19_3_02_Q023 | Stem used "H₂S point". | Reworded as H₂S system. | No | No | Yes |
| CHUNK1_19_3_02_Q024 | Explanation used "reducing point". | Reworded as acidified KMnO₄ system used to observe SO₂ reducing property. | No | No | Yes |
| CHUNK1_19_3_02_Q025 | Explanation used "oxidizing point". | Reworded as H₂S system used to observe SO₂ oxidizing property. | No | No | Yes |
| CHUNK1_19_3_02_Q029 | Explanation used "reducing point". | Reworded as acidified KMnO₄ system used to observe SO₂ reducing property. | No | No | Yes |
| CHUNK1_19_3_02_Q030 | Explanation used "extension point". | Reworded as extension experimental step for fuchsin bleaching. | No | No | Yes |

## Retained Student-visible Hits

These 7 hits used "设计" in the ordinary chemistry-experiment sense, not in question-bank design, item review, point binding, evidence scope, option feedback, or machine-grading language.

| question_id | Field | Retained text summary | Reason retained |
|---|---|---|---|
| CHUNK1_19_1_02_Q007 | stem | Same reagent added to chlorine/bromine/iodine water. | Valid experimental comparison design. |
| CHUNK1_19_1_03_Q023 | stem | KBr amount exceeds KI amount but I⁻ is still oxidized first. | Valid control-design reasoning about amount versus reducing ability. |
| CHUNK1_19_1_06_Q011 | explanation | Neutral/acidic KClO₃ and Na₂SO₃ comparison plus product test. | Valid textbook experimental design for medium effect. |
| CHUNK1_19_1_07_Q003 | stem | Follow the designed next step after weak neutral-condition phenomenon. | Valid procedural design in the experiment. |
| CHUNK1_19_1_08_Q016 | stem | Key-shielding design controls a variable. | Valid variable-control design. |
| CHUNK1_19_1_08_Q022 | stem | AgCl on filter paper with key exposure observation design. | Valid observation-layout design. |
| CHUNK1_19_2_04_Q004 | stem | AgNO₃/NaOH brown precipitate followed by H₂O₂. | Valid contrast design for Ag system behavior. |

## Evidence Consistency Notes

- The modified questions were checked against their existing `primary_point_keys`, `secondary_point_keys`, `option_links`, `source_audit`, `video_points`, and `evidence_sources`.
- RAG ids used by the affected questions resolve in:
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_experiment_chunks_v1.jsonl`
  - `E:\chemistry-rag\data\rag_ready\chunks\textbook_inorganic_lower_chunks_v1.jsonl`
- Only `CHUNK1_19_1_01_Q027` changed point keys: its primary keys now match the two adjacent replacement operations used by the correct option.
- No answer values changed.

## Final Validation

- JSON parse: pass
- Rebuilt JSON file count: 15
- Total question count: 450
- Type counts: 283 single choice, 128 true/false, 39 fill blank
- Unique question ids: pass, 450 unique ids
- Single-choice answer/options/option_links: pass, 283/283 have valid answer label, 4 options, and 4 option_links
- Cited RAG ids: pass, 0 missing ids
- Student-visible raw id: pass, 0 hits
- Student-visible ASCII digit formula: pass, 0 hits
- Student-visible ASCII valence: pass, 0 hits
- Chinese abnormal spacing: pass, 0 hits
- Student-visible review language: pass, 0 hits for `题干/题目/出题/点位/点位绑定/本点位/视频点位/证据范围/教材依据/选项反馈/机器判分/移动端/RAG/canonical/packet/evidence-first/backticks`
