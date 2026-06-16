## 1. Migration Closure

- [x] 1.1 Confirm that the earlier fixed-mix enhanced-bank demo plan has been superseded by the reviewed point-aware default-bank migration.
- [x] 1.2 Remove the stale requirement for a separate `2` single-choice plus `1` true/false per point enhanced-bank artifact from this active change.
- [x] 1.3 Preserve the current production objective type contract: `single_choice`, `true_false`, and deterministic phone-friendly `fill_blank`.

## 2. Imported Bank Evidence

- [x] 2.1 Validate the rebuilt reviewed bank artifact before import.
- [x] 2.2 Import the reviewed point-aware bank as the published default bank, replacing the old default bank.
- [x] 2.3 Verify the imported bank keeps experiment ids, primary point keys, point titles, source refs, source audit metadata, option links, coverage tags, and deterministic answers.

## 3. Teacher And Analytics Surfaces

- [x] 3.1 Adapt question-bank browsing to formal experiment and experiment point navigation.
- [x] 3.2 Show point titles, evidence status, source references, accepted answers, and option diagnostic links in teacher question detail.
- [x] 3.3 Preserve point-aware weak-point analytics and readable student learning-path display.
- [x] 3.4 Configure the OpenAI-compatible AI provider for later point-aware AI suggestion workflows.

## 4. Validation And Archive Readiness

- [x] 4.1 Run frontend typecheck/build after the point-aware UI migration.
- [x] 4.2 Run backend or targeted validation for the imported bank and point-aware analytics paths.
- [x] 4.3 Run `openspec validate add-diagnostic-enhanced-point-bank --strict`.
