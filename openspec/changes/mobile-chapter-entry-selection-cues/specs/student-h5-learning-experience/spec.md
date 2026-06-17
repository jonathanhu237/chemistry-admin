## ADDED Requirements

### Requirement: Periodic-table entry distinguishes selection from recommendation
The student H5 periodic-table entry SHALL distinguish area selection, recommended guidance, and chapter navigation entry semantics.

#### Scenario: Recommended chapter is shown as guidance
- **WHEN** the periodic-table entry has a recommended profile
- **THEN** the matching chapter entry MUST show a recommendation label
- **AND** it MUST NOT render as a selected, active, or current chapter before the student opens it

#### Scenario: Student changes selected area
- **WHEN** the student taps an area control or an element cell from a different area
- **THEN** the chapter list MUST filter to that selected area
- **AND** the selected area MUST be visually distinguishable from other areas
- **AND** the recommended area cue MUST remain recommendation guidance rather than forcing the selected area back after the student's tap

#### Scenario: Student opens a chapter entry
- **WHEN** the student taps a chapter entry card
- **THEN** the H5 app MUST navigate into that family or chapter learning page
- **AND** the entry card itself MUST be treated as a navigation row rather than a persistent selected item on the entry page
