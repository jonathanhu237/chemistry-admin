## ADDED Requirements

### Requirement: Legacy student home opens as video feed
The legacy student frontend SHALL make the default authenticated home surface an experiment-video feed rather than an Atom assistant, category browser, or modern recommendation-topic page.

#### Scenario: Legacy student opens home
- **WHEN** an authenticated student opens the old student product home route
- **THEN** the first primary content surface MUST be the experiment video feed
- **AND** the feed MUST use published playable experiment point/video data from the shared backend
- **AND** the home page MUST NOT require the student to choose a category, topic, Atom prompt, or assistant mode before browsing videos

#### Scenario: Legacy student feed has no topic rail
- **WHEN** the old student home video feed renders
- **THEN** it MUST NOT show the current recommendation topic rail or category strip above the feed
- **AND** it MUST NOT show modern category buttons for recommendation topics, element families, phenomena, reagents, or knowledge chips as the default home chrome

### Requirement: Legacy student uses simple native video playback
The legacy student frontend SHALL use native browser video controls or a simple traditional video surface for point/video playback.

#### Scenario: Legacy student opens a video point
- **WHEN** a student opens a video point in `web-student-old`
- **THEN** the page MUST render a playable video using native browser controls or a simple traditional player surface
- **AND** it MUST NOT use the current custom/self-drawn player chrome, ArtPlayer-based point player, or Atom-oriented video action surface
- **AND** the page MUST still use protected student-visible media URLs authorized by the shared backend

#### Scenario: Legacy video media cannot autoplay or load
- **WHEN** native playback is unavailable, blocked, or fails
- **THEN** the old student page MUST show a controlled traditional error or poster state
- **AND** it MUST NOT surface RAG, Atom, media-pipeline, or diagnostic implementation wording to the student

### Requirement: Legacy video discovery uses traditional card/list UI
The legacy student video discovery surface SHALL use a traditional card or list style that is visually distinct from the current modern H5 feed.

#### Scenario: Legacy feed is rendered on mobile width
- **WHEN** the old student feed is rendered on common mobile widths
- **THEN** video cards or rows MUST keep stable thumbnail/player dimensions, readable titles, and concise experiment metadata
- **AND** the visual language MUST use SYSU-red legacy tokens rather than the current green topic-rail visual language
- **AND** visible feed actions MUST remain learning-oriented rather than Atom/chat-oriented
