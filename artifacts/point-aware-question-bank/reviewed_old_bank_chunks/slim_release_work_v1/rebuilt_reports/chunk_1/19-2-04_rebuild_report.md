# 19-2-04 Rebuild Report

## Packet
- Chunk: chunk_1
- Experiment code: 19-2-04
- Experiment title: 过氧化氢的性质
- Source packet: `semantic_work_packets/chunk_1/19-2-04.json`
- Rebuilt package: `rebuilt_packages/chunk_1/19-2-04_rebuilt_v1.json`
- Release JSON edit policy: no `chunk_X_release_final_v1.json` file was modified.

## Counts
- Total questions: 30
- Keep: 17
- Rewrite: 13
- Reject: 0
- Question type counts: 17 single choice, 10 true/false, 3 fill blank

## Rewrite List
- CHUNK1_19_2_04_Q004: changed AgNO₃/NaOH item from product recall into the source-required comparison between alkaline and direct AgNO₃/H₂O₂ systems.
- CHUNK1_19_2_04_Q005: rebuilt medium-effect question to explicitly compare H₂O₂ roles in alkaline and acidified Mn systems.
- CHUNK1_19_2_04_Q006: rebuilt decomposition item as a source-specific operation group: heating, MnO₂, iron powder.
- CHUNK1_19_2_04_Q010: rebuilt overall-scope question to include weak acidity, redox behavior, and decomposition while separating it from the previous identification packet.
- CHUNK1_19_2_04_Q013: changed broad catalyst wording to source-grounded “decomposition observation” wording.
- CHUNK1_19_2_04_Q016: rewrote the Ag comparison true/false item to remove vague wording and match the canonical comparison.
- CHUNK1_19_2_04_Q017: rebuilt three-operation decomposition statement with explicit source-subsection binding.
- CHUNK1_19_2_04_Q018: rebuilt as a point-scope distinction between decomposition and acid KI oxidation.
- CHUNK1_19_2_04_Q019: simplified a reducing-property judgment into a direct, non-double-negative statement.
- CHUNK1_19_2_04_Q020: rebuilt as a scope-level misconception item.
- CHUNK1_19_2_04_Q024: replaced decomposition product recall with property classification.
- CHUNK1_19_2_04_Q026: kept Ag₂O only with explicit supporting theory; canonical alone says “棕色沉淀”.
- CHUNK1_19_2_04_Q028: rebuilt KI item to connect I₂ generation with observation clues.

## Keep But Edge
- CHUNK1_19_2_04_Q001, Q003, Q009, Q011, Q012, Q015, Q030: retained because they test the central dual redox roles of H₂O₂ and are supported by both experiment and theory.
- CHUNK1_19_2_04_Q002, Q008, Q014, Q022, Q029: retained because PbS black-to-white / PbSO₄ questions are strongly supported by theory and the experiment point.
- CHUNK1_19_2_04_Q007, Q025: retained though basic because they anchor the decomposition setup involving MnO₂.
- CHUNK1_19_2_04_Q021: retained as a direct I₂ product item with theory support.
- CHUNK1_19_2_04_Q023, Q027: retained as short Chinese fill blanks with stable deterministic answers.

## Evidence Insufficient
- None. All released questions have canonical evidence; product-level claims use supporting theory where canonical wording is only procedural.

## Multipoint Questions
- CHUNK1_19_2_04_Q004 and Q016: bind candidate-5 and candidate-6 because the question asks the comparison between AgNO₃/NaOH/H₂O₂ and direct AgNO₃/H₂O₂.
- CHUNK1_19_2_04_Q005, Q015, Q027, Q030: bind candidate-7, candidate-8, and candidate-9 because the answer depends on medium-controlled role changes.
- CHUNK1_19_2_04_Q006, Q017, Q024: bind candidate-10, candidate-11, and candidate-12 because all three are the decomposition-observation operations.
- CHUNK1_19_2_04_Q010 and Q020: bind multiple property points because they summarize the experiment-level scope.
- CHUNK1_19_2_04_Q018: binds candidate-10 and candidate-2 to distinguish decomposition from KI oxidation.

## Fill Blank Mobile Risk
- CHUNK1_19_2_04_Q023: answer “还原/还原剂”; low risk and no formula input.
- CHUNK1_19_2_04_Q027: answer “介质/溶液介质”; low risk.
- CHUNK1_19_2_04_Q030: answer “还原/还原性”; low risk.
- No fill blank requires students to type complex chemical formulas.

## RAG Evidence IDs
- `expchunk_00218_1a6196cddf` line 231: canonical H₂O₂ property experiments for weak acidity, KI oxidation, PbS oxidation, KMnO₄ reduction, and AgNO₃/NaOH setup.
- `expchunk_00219_5cb548b963` line 232: canonical Ag comparison, medium acid-base effect, heating/MnO₂/iron powder decomposition observations, and preservation prompt.
- `expchunk_00220_42e84103ab` line 233: thought questions on H₂O₂ as oxidant/reductant and Mn²⁺/MnO₂ medium conditions.
- `textbook_prose_00281_7e85498a41` line 510: H₂O₂ chemical properties include weak acidity, decomposition, and redox behavior.
- `textbook_prose_00291_440e726030` line 520: H₂O₂ has intermediate oxygen oxidation state and therefore both oxidizing and reducing properties.
- `textbook_prose_00292_940c386244` line 516: H₂O₂ oxidizes black PbS to white PbSO₄.
- `textbook_prose_00293_6e62d1272e` line 517: acidic H₂O₂ oxidizes I⁻ to I₂.
- `textbook_prose_00294_81753ec362` line 521: H₂O₂ shows reducing property with strong oxidizers.
- `textbook_prose_00295_e1465a9872` line 518: H₂O₂ reacts with acidic MnO₄⁻ and produces O₂.
- `textbook_prose_00298_1aa73dd09c` line 515: light or heavy metal ions promote H₂O₂ decomposition and inform storage.
- `textbook_prose_01057_8ebcc2ce77` line 1643: Ag⁺ with OH⁻ forms brown-black Ag₂O.

## Manual Reconstruction Statement
This packet was manually rebuilt question by question. The rebuilt JSON and this report were not generated by a batch script, and no release JSON was directly modified.


## Publish Blocker Polish Validation

- Scope: student-visible fields in this packet rebuilt JSON: stem, options[].text, explanation, fill_blank accepted_answers, and visible feedback-like fields if present.
- Fixed question_ids: Q004, Q006, Q026.
- Rules checked: internal process traces, ASCII digit-subscript formulas, ASCII charge/ion notation, caret/LaTeX/Markdown chemical notation, and visible process notes.
- Final remaining blockers in this packet: 0.
- Protected fields unchanged by this polish pass: question_id, point keys, option_links point keys, canonical/supporting evidence ids.
- Release JSON unchanged by this polish pass.
