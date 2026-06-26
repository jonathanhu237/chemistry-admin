## Why

The project needs a lower-level competition presentation that foregrounds inorganic chemistry experiment teaching, BKT knowledge tracing, personalized video recommendation, and intelligent assessment composition while hiding the newer RAG/Agent/Atom product line. The current student and teacher frontends are visibly modern and AI-agent-centric, so a simple feature switch or color tweak would still look like the same application and weaken the intended competition narrative.

## What Changes

- Add a legacy competition profile made of two additional frontend products: `web-student-old` and `web-teacher-old`.
- Add Docker Compose deployment for the old frontend products, with default browser ports `15176` for `web-student-old` and `15177` for `web-teacher-old`.
- Keep the legacy frontends on the same backend, database, seed data, BKT/mastery logic, question bank, video resources, and analytics data as the current product.
- Reframe the visible legacy product narrative around: experiment knowledge-graph navigation, AI-assisted question-bank construction, BKT knowledge tracing, personalized video recommendation, and smart assessment composition.
- Make the legacy student frontend feel like an older experiment-learning product:
  - no Atom assistant route, tab, contextual action, AI chat, Atom model card, or assistant-branded report explanation;
  - default home is the experiment video feed;
  - no recommendation category rail on the home video feed;
  - no current custom/self-drawn player; use native browser video controls or a simple traditional video surface;
  - traditional card/list visual language using SYSU red branding.
- Make the legacy teacher frontend feel like an older BKT teaching-management product:
  - no learning assistant or intelligent monitoring navigation;
  - no visible RAG, Agent, retrieval, embedding, rerank, chunk, model-provider, or guardrail terminology;
  - preserve AI question generation, teacher review, question bank, student assessment, and teacher learning-score review.
- Use official SYSU assets from `E:\迅雷下载\sysu-logo-main` as implementation source material, copied into the old frontend apps during implementation so builds do not depend on the local download directory.
- Require the old visible UI to be visually distinct enough that a reviewer should not reasonably infer it is the same application skin as the current green Atom/RAG product.

## Capabilities

### New Capabilities

- `bkt-legacy-competition-profile`: Defines the legacy competition product profile, its allowed narrative, separate frontend products, SYSU-red visual baseline, BKT-centered workflows, and forbidden RAG/Agent/Atom exposure.

### Modified Capabilities

- `split-frontend-deployment`: Add legacy student and teacher frontend services to the deployable service topology while preserving shared backend/API proxy behavior.
- `web-console-product-boundaries`: Clarify that legacy frontends are separate competition products sharing core data rather than replacements for current `web-student` and `web-teacher`.
- `student-h5-video-discovery`: Define legacy student home/video discovery differences: feed-first default, no topic rail, and simple/native playback.
- `student-h5-ai-assistant`: Define that the legacy student profile excludes Atom/AI assistant routes, navigation, contextual actions, and assistant-branded UI.
- `student-h5-assessment-flow`: Preserve BKT/mastery-driven assessment and reporting in the legacy student profile while removing Atom/RAG-branded explanation surfaces.
- `experiment-question-bank-management`: Preserve AI-assisted question generation and teacher confirmation in the legacy teacher profile while hiding RAG/Agent implementation terminology.
- `teacher-intelligent-monitoring-console`: Define that the legacy teacher profile excludes intelligent monitoring navigation and diagnostic surfaces.
- `class-learning-analytics`: Preserve teacher review of student learning scores/mastery in the legacy profile as part of the BKT feedback loop.

## Impact

- Adds implementation work under new legacy frontend packages or entrypoints such as `apps/web-student-old` and `apps/web-teacher-old`.
- Affects Docker Compose and frontend image build configuration by adding `web-student-old` and `web-teacher-old` services.
- Affects frontend routing, navigation, copy, theming, assets, and visible feature gating for old products only.
- Affects acceptance tests through old-profile visual/string checks that ensure forbidden RAG/Agent/Atom terminology is not visible.
- Does not require a new database, a seed split, a BKT rewrite, or removal of the current modern student/teacher frontends.
