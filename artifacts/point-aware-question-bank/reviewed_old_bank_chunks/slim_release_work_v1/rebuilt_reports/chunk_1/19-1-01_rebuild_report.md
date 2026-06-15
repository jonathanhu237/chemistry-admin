# Rebuild Report: 19-1-01 氯、溴、碘的置换次序

## Packet

- Packet id / experiment code: `19-1-01`
- Experiment title: 氯、溴、碘的置换次序
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_1\19-1-01.json`
- Output JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_1\19-1-01_rebuilt_v1.json`
- Statement: this packet was manually rebuilt question by question; it is not a script-bulk-generated package.
- Release JSON edit status: no `chunk_X_release_final_v1.json` file was modified.

## Counts

- Total questions: 30
- Type counts: single_choice = 19, true_false = 9, fill_blank = 2
- Keep / rewrite / reject: 11 / 19 / 0

## Actual Rewrite List

Rewritten question ids:

- `CHUNK1_19_1_01_Q003`
- `CHUNK1_19_1_01_Q006`
- `CHUNK1_19_1_01_Q007`
- `CHUNK1_19_1_01_Q008`
- `CHUNK1_19_1_01_Q009`
- `CHUNK1_19_1_01_Q010`
- `CHUNK1_19_1_01_Q017`
- `CHUNK1_19_1_01_Q018`
- `CHUNK1_19_1_01_Q019`
- `CHUNK1_19_1_01_Q020`
- `CHUNK1_19_1_01_Q021`
- `CHUNK1_19_1_01_Q022`
- `CHUNK1_19_1_01_Q023`
- `CHUNK1_19_1_01_Q024`
- `CHUNK1_19_1_01_Q025`
- `CHUNK1_19_1_01_Q026`
- `CHUNK1_19_1_01_Q027`
- `CHUNK1_19_1_01_Q028`
- `CHUNK1_19_1_01_Q029`

Note: `CHUNK1_19_1_01_Q020` was changed from a broad true/false item about K⁺ into a phone-safe short fill blank asking for the experiment output concept `氧化性`.

## Keep Rationale

Kept question ids:

- `CHUNK1_19_1_01_Q001`: retained as the direct Cl₂/Br₂ operation-evidence item; wording was tightened to foreground the operation chain and CCl₄ role.
- `CHUNK1_19_1_01_Q002`: retained as the CCl₄ role question; supporting theory is now explicit.
- `CHUNK1_19_1_01_Q004`: retained as the Br₂/I₂ point-boundary item; options were cleaned to avoid ambiguity.
- `CHUNK1_19_1_01_Q005`: retained as the complete order item; multi-point binding is justified by the full order requirement.
- `CHUNK1_19_1_01_Q011`: retained as a deterministic true/false item for candidate-1.
- `CHUNK1_19_1_01_Q012`: retained as a deterministic true/false item for candidate-3.
- `CHUNK1_19_1_01_Q013`: retained to rule out the common misconception that CCl₄ is the oxidant.
- `CHUNK1_19_1_01_Q014`: retained as the general displacement principle behind all three points.
- `CHUNK1_19_1_01_Q015`: retained to catch reversed halogen-order reasoning.
- `CHUNK1_19_1_01_Q016`: retained because it directly matches the canonical experiment purpose.
- `CHUNK1_19_1_01_Q030`: retained as a phone-safe fill blank; answer is short ordinary Chinese.

## Keep But Quality-Edge

- `CHUNK1_19_1_01_Q011`: basic direct recall, kept because it is the clean single-point foundation for Cl₂ > Br₂.
- `CHUNK1_19_1_01_Q012`: basic direct recall, kept because it is the clean single-point foundation for Br₂ > I₂.
- `CHUNK1_19_1_01_Q016`: low cognitive load, kept because it anchors the experiment purpose from canonical RAG.
- `CHUNK1_19_1_01_Q030`: simple observation-word blank, kept because it is mobile-safe and checks the non-oxidant role of CCl₄.

## Evidence Insufficient

0

No question is marked publishable with `evidence_sufficient = false`.

## Multi-Point Questions

- `CHUNK1_19_1_01_Q002`: CCl₄ role applies across all three video points.
- `CHUNK1_19_1_01_Q005`: asks for the complete Cl₂ > Br₂ > I₂ order, requiring combined point evidence.
- `CHUNK1_19_1_01_Q006`: asks for the full canonical reagent set across the three point systems.
- `CHUNK1_19_1_01_Q007`: asks why CCl₄ alone is insufficient across all point systems.
- `CHUNK1_19_1_01_Q008`: asks for the minimal two-point evidence set to infer the full order.
- `CHUNK1_19_1_01_Q009`: compares the two chlorine-water points and identifies the missing Br₂/I₂ point.
- `CHUNK1_19_1_01_Q010`: asks packet point-boundary across all three listed points.
- `CHUNK1_19_1_01_Q013`: CCl₄ role misconception spans all three point systems.
- `CHUNK1_19_1_01_Q014`: states the shared displacement principle for all three point systems.
- `CHUNK1_19_1_01_Q015`: reversed iodine/bromine reasoning is judged against the order supported by point 1 and point 3.
- `CHUNK1_19_1_01_Q016`: experiment purpose is the combined outcome of the three points.
- `CHUNK1_19_1_01_Q017`: evidence-record completeness applies to all CCl₄ observation points.
- `CHUNK1_19_1_01_Q019`: invalid evidence claim contrasts CCl₄-only observation with all three real point systems.
- `CHUNK1_19_1_01_Q020`: experiment-output concept depends on all three point systems.
- `CHUNK1_19_1_01_Q023`: supporting-theory decision applies to CCl₄ color reasoning across the point systems.
- `CHUNK1_19_1_01_Q024`: “保密信” application depends on the combined displacement-order idea.
- `CHUNK1_19_1_01_Q025`: asks for final experiment-record output across all points.
- `CHUNK1_19_1_01_Q026`: distinguishes this packet's three points from adjacent experiment content.
- `CHUNK1_19_1_01_Q027`: directly tests when multi-point binding is justified.
- `CHUNK1_19_1_01_Q028`: asks for canonical + theory evidence combination for CCl₄ color reasoning.
- `CHUNK1_19_1_01_Q030`: CCl₄ observation role spans all three point systems.

## Fill-Blank Mobile Risk

| question_id | visible answer(s) | hidden aliases | risk |
|---|---|---|---|
| `CHUNK1_19_1_01_Q020` | 氧化性 | none | low; ordinary Chinese word |
| `CHUNK1_19_1_01_Q030` | 颜色 / 颜色变化 | none | low; ordinary Chinese phrase |

No visible fill blank requires a formula, ion, equation, valence, or multi-alias symbol answer.

## RAG Evidence IDs Used

Canonical experiment evidence:

- `expchunk_00193_497eb97bd6`
- `expchunk_00199_8240477bff`

Supporting theory evidence:

- `textbook_prose_00028_a4c7b7c9ae`
- `textbook_prose_00030_522edfaa72`

## Rejected Or Replaced Old Evidence IDs

0

Inherited locators were treated as candidates only. The final package uses only RAG JSONL ids verified in the required files.

## Duplicate Resolution

The old low-depth cluster around “被氧化的离子 / 生成的单质 / 最弱的是谁 / 哪组试剂证明 Cl₂ > Br₂” was split into:

- direct single-point evidence questions (`Q001`, `Q004`, `Q011`, `Q012`);
- point-boundary questions (`Q003`, `Q009`, `Q010`, `Q021`, `Q022`);
- evidence-combination questions (`Q008`, `Q025`, `Q028`);
- invalid-evidence and adjacent-experiment boundary questions (`Q007`, `Q019`, `Q026`);
- multi-point binding and experiment-output questions (`Q020`, `Q027`, `Q030`);
- application/output reasoning (`Q024`).

## Validation

- JSON parse: pass
- Question count: pass, 30
- `question_id` uniqueness: pass
- Single-choice answer labels exist in options: pass
- Single-choice option_links count equals options count: pass
- Cited evidence ids found in RAG JSONL: pass
- Missing explanations: 0
- Visible ASCII digit formulas: 0
- Visible formula-like fill answers: 0
- Evidence-insufficient publishable questions: 0


## Publish Blocker Polish Validation

- Scope: student-visible fields in this packet rebuilt JSON: stem, options[].text, explanation, fill_blank accepted_answers, and visible feedback-like fields if present.
- Fixed question_ids: Q002, Q006, Q010, Q016, Q021, Q023, Q025, Q026, Q028.
- Rules checked: internal process traces, ASCII digit-subscript formulas, ASCII charge/ion notation, caret/LaTeX/Markdown chemical notation, and visible process notes.
- Final remaining blockers in this packet: 0.
- Protected fields unchanged by this polish pass: question_id, point keys, option_links point keys, canonical/supporting evidence ids.
- Release JSON unchanged by this polish pass.
