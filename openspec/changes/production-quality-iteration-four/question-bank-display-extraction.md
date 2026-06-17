# Question Bank Display Extraction

Date: 2026-06-17

## Scope

The first fourth-pass implementation slice extracted pure display and formatting helpers from `apps/admin-web/src/features/question-bank/QuestionBanksPage.tsx` into `apps/admin-web/src/features/question-bank/questionBankDisplay.tsx`.

Moved helper ownership includes:

- question type and coverage tag labels
- answer/source-reference formatting
- question point extraction and point-title helpers
- candidate payload display helpers
- candidate validation error selection
- evidence/status/review display tags and text
- question workbench runtime gate display state
- removal of previously unreferenced draft display helpers from the page module

## Behavior Boundary

This was a mechanical extraction. It intentionally did not change:

- route paths
- query keys
- API endpoints
- mutation payloads
- selected experiment/question state
- AI workbench session flow
- question bank visible workflows
- protected question-bank data

## Size Impact

Before extraction:

- `QuestionBanksPage.tsx`: 1345 lines, 59.5 KB

After extraction:

- `QuestionBanksPage.tsx`: 1111 lines, 51.3 KB
- `questionBankDisplay.tsx`: 235 lines, 7.9 KB

The page remains large, but the moved code is now owned as a feature-local display helper module and can be tested or reused without entering the page state machine.
