# Rebuild Report: chunk_5 / 20-3-02

## Packet

- Packet id / experiment code: `20-3-02`
- Experiment title: 阴离子颜色
- Source packet: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets\chunk_5\20-3-02.json`
- Rebuilt JSON: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\rebuilt_packages\chunk_5\20-3-02_rebuilt_v1.json`
- Declaration: this packet has been manually reconstructed question by question. It is not a script-generated metadata normalization or batch copy of the source packet.

## Counts

- Total questions: `30`
- Keep: `16`
- Rewrite: `14`
- Reject: `0`

## Actual Rewrites

`CHK5_SEM_EXP_20_3_02_004`, `CHK5_SEM_EXP_20_3_02_005`, `CHK5_SEM_EXP_20_3_02_014`, `CHK5_SEM_EXP_20_3_02_015`, `CHK5_SEM_EXP_20_3_02_021`, `CHK5_SEM_EXP_20_3_02_022`, `CHK5_SEM_EXP_20_3_02_023`, `CHK5_SEM_EXP_20_3_02_024`, `CHK5_SEM_EXP_20_3_02_025`, `CHK5_SEM_EXP_20_3_02_026`, `CHK5_SEM_EXP_20_3_02_027`, `CHK5_SEM_EXP_20_3_02_028`, `CHK5_SEM_EXP_20_3_02_029`, `CHK5_SEM_EXP_20_3_02_030`

## Kept But Quality-Edge Items

- `CHK5_SEM_EXP_20_3_02_001`: kept because CrO₄²⁻ is explicitly listed as an anion observation object.
- `CHK5_SEM_EXP_20_3_02_002`: kept because CrO₄²⁻ yellow is directly supported by theory.
- `CHK5_SEM_EXP_20_3_02_003`: kept because MnO₄⁻ purple is directly supported by theory.
- `CHK5_SEM_EXP_20_3_02_006`: kept because the listed group is fully canonical.
- `CHK5_SEM_EXP_20_3_02_007`: kept because charge-transfer transition is directly supported by theory.
- `CHK5_SEM_EXP_20_3_02_008`: kept because MoO₄²⁻ and WO₄²⁻ are canonical list items.
- `CHK5_SEM_EXP_20_3_02_009`: kept because VO₃⁻ is a canonical anion observation object.
- `CHK5_SEM_EXP_20_3_02_010`: kept as a scope-exclusion question separating anion colors from water hydrated cation colors.
- `CHK5_SEM_EXP_20_3_02_011`: kept because the swapped CrO₄²⁻ / MnO₄⁻ color statement is clearly false.
- `CHK5_SEM_EXP_20_3_02_012`: kept because the canonical list is not simple halides and not all colorless.
- `CHK5_SEM_EXP_20_3_02_013`: kept because MoO₄²⁻ and WO₄²⁻ are listed observation objects.
- `CHK5_SEM_EXP_20_3_02_016`: kept because it directly states the Mo/W canonical inclusion.
- `CHK5_SEM_EXP_20_3_02_017`: kept because the packet does observe anions, not only water hydrated cations.
- `CHK5_SEM_EXP_20_3_02_018`: kept because the charge-transfer statement is supported by theory.
- `CHK5_SEM_EXP_20_3_02_019`: kept because Cl⁻ is not in the canonical target list.
- `CHK5_SEM_EXP_20_3_02_020`: kept because VO₃⁻ is explicitly listed.

## Evidence Insufficient

- None in the rebuilt packet.
- Exact colors were asserted only for CrO₄²⁻ and MnO₄⁻ because those two are directly supported by `textbook_prose_01119_8478df1f7f`.
- Cr₂O₇²⁻, MnO₄²⁻, MoO₄²⁻, WO₄²⁻, and VO₃⁻ are used for canonical membership, charge/formula discrimination, and recording-method questions rather than unsupported exact color claims.

## Multi-Point Questions

- `CHK5_SEM_EXP_20_3_02_006`, `014`, `017`, `021`, and `025` deliberately bind multiple point keys because they test list-level scope or recording method.
- Single-ion color, membership, or formula-reading questions bind only to the relevant ion point.

## Fill-Blank Mobile Risk

- None. This rebuilt packet uses only single-choice and true/false items.
- Formula-reading items were converted to single-choice so students do not need to type formulas, charges, or element symbols.

## RAG Evidence IDs Used

- Canonical anion list: `expchunk_00330_3a60414cf4`
- General transition-metal color theory and high-oxidation oxyanion transition boundary: `textbook_prose_01118_9e2eabedd8`
- CrO₄²⁻ yellow, MnO₄⁻ purple, and charge-transfer explanation: `textbook_prose_01119_8478df1f7f`
- CrO₄²⁻ / Cr₂O₇²⁻ relationship and pH-dependent distinction: `textbook_prose_00789_e61f8704bd`

Rejected or excluded locator ids from the source packet:

- `textbook_prose_00293_6e62d1272e`: hydrogen peroxide oxidation context, not needed for the final anion color scope.
- `textbook_prose_00296_5f7afd3720`: useful for detecting Cr₂O₇²⁻ via blue peroxychromium, but outside the core color-recording questions in this packet.

## Duplicate Resolution

The source packet repeated a generic “which statement is correct” shell across many items. The rebuilt packet separates the concepts into canonical anion scope, CrO₄²⁻ / MnO₄⁻ direct color evidence, chromate/dichromate and manganate/permanganate formula distinctions, charge-transfer theory, evidence boundaries for Mo/W/V species, category separation from water hydrated cations, and phone-safe formula reading.

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
- Modified visible fields in this packet: `34`.
- Modified question_id list: `CHK5_SEM_EXP_20_3_02_001`, `CHK5_SEM_EXP_20_3_02_002`, `CHK5_SEM_EXP_20_3_02_003`, `CHK5_SEM_EXP_20_3_02_004`, `CHK5_SEM_EXP_20_3_02_005`, `CHK5_SEM_EXP_20_3_02_006`, `CHK5_SEM_EXP_20_3_02_007`, `CHK5_SEM_EXP_20_3_02_008`, `CHK5_SEM_EXP_20_3_02_009`, `CHK5_SEM_EXP_20_3_02_010`, `CHK5_SEM_EXP_20_3_02_011`, `CHK5_SEM_EXP_20_3_02_012`, `CHK5_SEM_EXP_20_3_02_013`, `CHK5_SEM_EXP_20_3_02_014`, `CHK5_SEM_EXP_20_3_02_015`, `CHK5_SEM_EXP_20_3_02_016`, `CHK5_SEM_EXP_20_3_02_017`, `CHK5_SEM_EXP_20_3_02_018`, `CHK5_SEM_EXP_20_3_02_019`, `CHK5_SEM_EXP_20_3_02_020`, `CHK5_SEM_EXP_20_3_02_021`, `CHK5_SEM_EXP_20_3_02_022`, `CHK5_SEM_EXP_20_3_02_023`, `CHK5_SEM_EXP_20_3_02_024`, `CHK5_SEM_EXP_20_3_02_025`, `CHK5_SEM_EXP_20_3_02_026`, `CHK5_SEM_EXP_20_3_02_027`, `CHK5_SEM_EXP_20_3_02_028`, `CHK5_SEM_EXP_20_3_02_030`.
- Student-visible internal review/rebuild traces remaining: `0`.
- Student-visible ASCII digit-subscript formulas remaining: `0`.
- Student-visible ASCII charge/ion/ASCII valence syntax remaining: `0`.
- Student-visible caret / LaTeX / Markdown chemistry syntax remaining: `0`.
- JSON parse and packet question count: passed; expected `30` questions.
- Single-choice answer/options/option_links shape: passed.
- `question_id`, `primary_point_keys`, `secondary_point_keys`, `source_audit` evidence ids, and `option_links` labels/point keys/roles: unchanged by this polish pass.
- Release JSON direct edit: no `chunk_X_release_final_v1.json` file was edited in this polish pass.
