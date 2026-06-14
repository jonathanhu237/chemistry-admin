## 1. Inventory And Schema

- [ ] 1.1 Confirm the current formal experiment point inventory count and expected full enhanced-bank size.
- [ ] 1.2 Define the enhanced diagnostic artifact schema for point-first `single_choice` and `true_false` items.
- [ ] 1.3 Add validation for per-point counts, allowed question types, source audit, point keys, and option-level diagnostic links.

## 2. Demo Generation

- [ ] 2.1 Select a representative demo point set from existing formal experiment video points.
- [ ] 2.2 Generate demo questions with exactly two single-choice and one true/false item per covered point.
- [ ] 2.3 Manually review demo questions against canonical experiment chunks and revise weak, unsupported, or non-diagnostic items.
- [ ] 2.4 Write the demo artifact and readable demo quality report.

## 3. Validation And Full Plan

- [ ] 3.1 Validate the demo artifact with the enhanced-bank validator.
- [ ] 3.2 Write the full-generation plan showing expected `2` single-choice plus `1` true/false per current experiment point.
- [ ] 3.3 Run `openspec validate add-diagnostic-enhanced-point-bank --strict`.
