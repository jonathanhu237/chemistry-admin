## 1. Legacy App Foundation

- [x] 1.1 Decide whether `web-student-old` and `web-teacher-old` are separate packages or separate build entrypoints, and document the chosen structure in the repository.
- [x] 1.2 Create the old student frontend shell with its own routing, root layout, app identity, package/build scripts, and API base behavior.
- [x] 1.3 Create the old teacher frontend shell with its own routing, root layout, app identity, package/build scripts, and API base behavior.
- [x] 1.4 Share only safe domain clients, types, and API helpers from current frontends; avoid importing current Atom/RAG UI shells into old apps.
- [x] 1.5 Add old-product route guards so stale or manually entered old URLs for excluded routes redirect to a safe old route or controlled not-found page.

## 2. SYSU Red Brand And Legacy Visual Baseline

- [x] 2.1 Select official SYSU SVG assets from `E:\迅雷下载\sysu-logo-main` for old login, header, sidebar, favicon/app mark, and optional reverse-header use.
- [x] 2.2 Copy selected SVG assets into repository-managed old-app public asset directories without leaving runtime or build references to the local download path.
- [x] 2.3 Define old frontend brand tokens with SYSU red `#740003` as the canonical primary color and separate old neutral/accent tokens.
- [x] 2.4 Build old student and old teacher base layouts using traditional card/list/table language rather than current green H5/Atom visual language.
- [x] 2.5 Add a visual or DOM-level check that old primary navigation, active states, and primary buttons do not use current green Atom/RAG theme tokens.

## 3. Legacy Student Product

- [x] 3.1 Implement old student root navigation without Atom, AI assistant, chat, artifact, contextual assistant, or Atom model-card entries.
- [x] 3.2 Make the old student authenticated home route open directly to the experiment video feed.
- [x] 3.3 Remove the current home recommendation topic rail/category strip from the old student video feed.
- [x] 3.4 Render old video feed cards or rows with stable traditional thumbnail/player geometry, readable titles, and concise experiment metadata.
- [x] 3.5 Implement old point/video detail playback with native browser controls or a simple traditional video surface.
- [x] 3.6 Ensure old point/video detail does not import or mount the current custom player, ArtPlayer point player, or Atom-oriented action surface.
- [x] 3.7 Preserve protected media authorization by using shared backend media URLs and access rules.
- [x] 3.8 Replace old student assessment/report copy with BKT, mastery, weak point, mistake review, and learning suggestion language.
- [x] 3.9 Ensure old student assessment and recommendation flows continue to use shared pretest/posttest, grading, mastery, and recommendation APIs.

## 4. Legacy Teacher Product

- [x] 4.1 Implement old teacher navigation around experiment navigation, video/resources, AI question generation, teacher review, question bank, assessments, classes, and learning scores.
- [x] 4.2 Exclude learning assistant, intelligent monitoring, AI/RAG/ES diagnostics, provider credentials, guardrails, and platform governance from old teacher navigation.
- [x] 4.3 Implement old AI question generation entry points using `AI出题` wording and selected experiment/point/chapter context.
- [x] 4.4 Preserve teacher review controls for accepting, rejecting, or requesting revision before generated questions become student-facing.
- [x] 4.5 Render source grounding as `教材依据`, `实验资料依据`, or `出题依据` without visible RAG/chunk/provider labels.
- [x] 4.6 Render old question bank browsing by experiment, video point, question type, status, answer, explanation, and review state where available.
- [x] 4.7 Render old class and student learning-score pages from shared analytics, assessment, and mastery records.
- [x] 4.8 Ensure old teacher learning-score pages explain the feedback loop through BKT mastery and experiment learning progress.

## 5. Shared Data And Backend Integration

- [x] 5.1 Verify old student and old teacher products read the same catalog, video, question bank, assessment, mastery, and analytics records as current products.
- [x] 5.2 Confirm no old-only seed ids, old-only question ids, old-only mastery tables, or old-only analytics imports are introduced.
- [x] 5.3 Wrap backend diagnostic/provider/retrieval error messages in old-product copy before rendering them in old frontends.
- [x] 5.4 Keep current products able to use Atom/RAG/monitoring routes and settings after old products are added.

## 6. Deployment

- [x] 6.1 Add `web-student-old` and `web-teacher-old` frontend service definitions using the existing frontend Dockerfile pattern or documented equivalent.
- [x] 6.2 Assign default browser port `15176` to `web-student-old` and default browser port `15177` to `web-teacher-old`.
- [x] 6.3 Configure old frontend services to serve deep SPA routes from their own `index.html`.
- [x] 6.4 Configure old frontend services to proxy browser-facing `/api/*` to the shared backend.
- [x] 6.5 Update Compose smoke or service documentation so old services can be started for legacy demos without making them mandatory for current-only development.

## 7. Forbidden-Term And Route Regression Tests

- [x] 7.1 Add old student rendered UI tests or snapshots proving Atom/AI assistant navigation, routes, contextual actions, and report branding are absent.
- [x] 7.2 Add old teacher rendered UI tests proving learning assistant, intelligent monitoring, and diagnostic navigation are absent.
- [x] 7.3 Add old-profile string scans for forbidden visible terms including Atom, RAG, Agent, chunk, embedding, rerank, Qwen, BGE, OpenAI, ES diagnostics, intelligent monitoring, and learning assistant.
- [x] 7.4 Add allowlist coverage for permitted old terms including AI出题, BKT, 掌握度, 个性化推荐, 智能组卷, 学情分数, 教材依据, and 出题依据.
- [x] 7.5 Add tests for stale old assistant/monitoring URLs redirecting to safe old routes or controlled not-found states.

## 8. Student Verification

- [x] 8.1 Verify old student home renders the feed first without a recommendation topic rail on common mobile widths.
- [x] 8.2 Verify old student video detail uses native/simple video playback and does not mount the current custom player.
- [x] 8.3 Verify old student assessment submission updates or reads shared mastery evidence and renders BKT-centered report copy.
- [x] 8.4 Verify old student video, assessment, and report pages do not expose raw backend diagnostic or provider wording during controlled failures.

## 9. Teacher Verification

- [x] 9.1 Verify old teacher AI question generation produces reviewable drafts and requires teacher confirmation before publication.
- [x] 9.2 Verify old teacher question-bank evidence copy hides RAG/chunk/provider terminology while preserving source usefulness.
- [x] 9.3 Verify old teacher learning-score pages read shared analytics and mastery records after student attempts.
- [x] 9.4 Verify current `web-teacher` intelligent monitoring remains available and unaffected.

## 10. Final Validation

- [x] 10.1 Run typecheck/build checks for old student and old teacher frontends.
- [x] 10.2 Run focused old student and old teacher route/render tests.
- [x] 10.3 Run current student/teacher smoke tests that guard against regressions in current products.
- [x] 10.4 Run Compose or documented service smoke for the old frontend services.
- [x] 10.5 Run `openspec validate add-bkt-legacy-competition-profile --strict`.

Note: current `apps/web-student` typecheck and e2e Vitest passed. Current `apps/web-teacher` typecheck and focused route/monitoring Vitest passed, confirming the current monitoring surface remains available outside `web-teacher-old`.
