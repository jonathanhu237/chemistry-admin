# Rebuild Report: chunk_5 / 20-2-10

## Packet

- Packet id / experiment code: `20-2-10`
- Experiment title: 小设计实验
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-2-10.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-2-10_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `8`
- Rewrite: `22`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_2_10_002`, `CHK5_SEM_EXP_20_2_10_003`, `CHK5_SEM_EXP_20_2_10_005`, `CHK5_SEM_EXP_20_2_10_006`, `CHK5_SEM_EXP_20_2_10_008`, `CHK5_SEM_EXP_20_2_10_009`, `CHK5_SEM_EXP_20_2_10_012`, `CHK5_SEM_EXP_20_2_10_013`, `CHK5_SEM_EXP_20_2_10_014`, `CHK5_SEM_EXP_20_2_10_015`, `CHK5_SEM_EXP_20_2_10_016`, `CHK5_SEM_EXP_20_2_10_017`, `CHK5_SEM_EXP_20_2_10_019`, `CHK5_SEM_EXP_20_2_10_020`, `CHK5_SEM_EXP_20_2_10_021`, `CHK5_SEM_EXP_20_2_10_022`, `CHK5_SEM_EXP_20_2_10_024`, `CHK5_SEM_EXP_20_2_10_025`, `CHK5_SEM_EXP_20_2_10_026`, `CHK5_SEM_EXP_20_2_10_027`, `CHK5_SEM_EXP_20_2_10_028`, `CHK5_SEM_EXP_20_2_10_029`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_2_10_001`: kept because it directly identifies the canonical target ion group.
- `CHK5_SEM_EXP_20_2_10_004`: kept because Cr(III) to CrO₄²⁻ under alkaline H₂O₂ is well-supported and central to a Cr detection route.
- `CHK5_SEM_EXP_20_2_10_007`: kept because “确认检出” is a necessary design requirement, not a mere naming recall.
- `CHK5_SEM_EXP_20_2_10_010`: kept because it checks design completeness: separation order plus detection evidence.
- `CHK5_SEM_EXP_20_2_10_011`: kept as a direct true/false check of the canonical target ions.
- `CHK5_SEM_EXP_20_2_10_018`: kept because it flags an incomplete scheme and is machine-deterministic.
- `CHK5_SEM_EXP_20_2_10_023`: kept because the visible answer `两性` is short, deterministic, and theory-supported.
- `CHK5_SEM_EXP_20_2_10_030`: kept because the visible answers `检出依据` / `检出证据` are phone-safe and central to “分离检出”.

## Evidence Insufficient

- None.

## Multi-Point Questions

- None. The packet has one video point, `candidate-1-121e9e71` (`含 Cr³⁺、Al³⁺、Mn²⁺ 的混合溶液分离检出`). Earlier property experiments and theory chunks are used only as evidence for designing the separation route, not as separate video point bindings.

## Fill-Blank Mobile Risk

| question_id | visible answer | hidden aliases | risk | action |
|---|---|---|---|---|
| `CHK5_SEM_EXP_20_2_10_023` | `两性` | `酸碱两性` | low | kept |
| `CHK5_SEM_EXP_20_2_10_027` | `检出`, `确认检出` | `验证检出` | low | rewritten |
| `CHK5_SEM_EXP_20_2_10_028` | `氧化还原`, `氧化还原性质` | none | low | rewritten |
| `CHK5_SEM_EXP_20_2_10_030` | `检出依据`, `检出证据` | `确认依据` | low | kept |

No visible fill-blank answer requires typing Cr(OH)₃, Al(OH)₃, Mn(OH)₂, H₂O₂, CrO₄²⁻, MnO₄⁻, or any other formula.

## RAG Evidence IDs Used

- Canonical design task: `expchunk_00323_56549b57c0`
- Preceding hydroxide property experiment: `expchunk_00319_b995aa9123`
- Preceding chromium redox property experiment: `expchunk_00321_53b9414bde`
- Aluminum amphoterism: `textbook_prose_00835_0d3c423061`
- Chromium hydroxide amphoterism and equilibrium: `textbook_prose_01208_f648cd206f`, `textbook_prose_01209_56d80e2580`
- Cr/Al separation under NH₃/H₂O₂ and Cr(III) oxidation: `textbook_prose_01211_3fe6c336b5`, `textbook_prose_01212_9b1152bdeb`, `textbook_prose_01213_dedb851b08`
- Mn(II) hydroxide and Mn²⁺ detection by oxidation to permanganate: `textbook_prose_01239_7b36e4736b`, `textbook_prose_01240_f358ee9f2c`, `textbook_prose_01241_99049758ad`
- Color support for CrO₄²⁻ and MnO₄⁻: `textbook_prose_01119_8478df1f7f`

Rejected or excluded locator ids from the source packet:

- `textbook_prose_00037_a7dbd4c099`, `textbook_prose_00039_cb1a979cf8`: halogen/iron redox context, not this separation design.
- `textbook_prose_01297_b761f39d9a`: iron cyanide complex context, not Cr/Al/Mn separation.
- `textbook_prose_01340_c4d5e485b6`: palladium/platinum complex context, not this packet.
- `expchunk_00325_d498507596`: related thought questions, useful for boundary awareness but not used as primary evidence for release questions.

## Duplicate Resolution

The source packet repeated a generic “which statement is correct” stem across several items and often reused broad theory locator lists. The rebuilt packet separates the design task into target-ion scope, NaOH/hydroxide logic, Cr/Al separation under NH₃/H₂O₂, CrO₄²⁻ and MnO₄⁻ color evidence, Mn²⁺ hydroxide behavior, scheme completeness, and mobile-safe fill blanks.

## Validation Notes

- JSON parse: passed.
- Question ids: unique.
- Single-choice answers: aligned with option labels.
- Option links: every single-choice option has one concrete semantic diagnostic.
- Evidence ids: passed.
- Visible ASCII digit formulas: passed.
- Release JSON direct edit: no `chunk_5_release_final_v1.json` was edited for this packet.
## Publish Blocker Polish Validation

- Student-visible scan scope: `stem`, `options[].text`, `explanation`, and fill-blank visible accepted answers.
- `option_links[].diagnostic_note`: internal diagnostic metadata used for option-level analytics after submission; not included in the student-visible text scan.
- Modified visible fields in this packet: `30`.
- Modified question_id list: `CHK5_SEM_EXP_20_2_10_001`, `CHK5_SEM_EXP_20_2_10_003`, `CHK5_SEM_EXP_20_2_10_004`, `CHK5_SEM_EXP_20_2_10_005`, `CHK5_SEM_EXP_20_2_10_006`, `CHK5_SEM_EXP_20_2_10_007`, `CHK5_SEM_EXP_20_2_10_009`, `CHK5_SEM_EXP_20_2_10_011`, `CHK5_SEM_EXP_20_2_10_012`, `CHK5_SEM_EXP_20_2_10_013`, `CHK5_SEM_EXP_20_2_10_014`, `CHK5_SEM_EXP_20_2_10_015`, `CHK5_SEM_EXP_20_2_10_016`, `CHK5_SEM_EXP_20_2_10_018`, `CHK5_SEM_EXP_20_2_10_019`, `CHK5_SEM_EXP_20_2_10_021`, `CHK5_SEM_EXP_20_2_10_022`, `CHK5_SEM_EXP_20_2_10_023`, `CHK5_SEM_EXP_20_2_10_024`, `CHK5_SEM_EXP_20_2_10_025`, `CHK5_SEM_EXP_20_2_10_026`, `CHK5_SEM_EXP_20_2_10_027`, `CHK5_SEM_EXP_20_2_10_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
