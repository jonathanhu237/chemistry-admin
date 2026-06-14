# Reviewed Old Bank Merged Artifact Report

## Result

- Merged artifact: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\reviewed_old_bank_merged_v1.json`
- Source reviewed items: `2310`
- Effective questions: `2310`
- Experiments: `77` / `77`
- Original review decisions: keep `1888`, rewrite `416`, reject `6`
- Proposed replacements used: `422`
- Reject-original replacements used: `6`
- Effective question types: single_choice `899`, true_false `744`, fill_blank `667`

## Validation

- Merge errors: `0`
- Artifact validator valid: `True`
- Artifact validator errors: `0`
- Artifact validator warnings: `0`
- Import dry-run prepared questions: `2310`
- Import dry-run skipped: `{}`
- Import dry-run point usage count: `286`

## Import Semantics

- `keep` old questions are flattened into importable point-aware questions.
- `rewrite` old questions use their `proposed_question` as the importable effective question.
- `reject` old originals are not imported; when a source-grounded `proposed_question` exists, that replacement is imported and the original reject decision is preserved in `review_lineage`.
- The five chunk artifacts remain the detailed audit source for old-question text.
