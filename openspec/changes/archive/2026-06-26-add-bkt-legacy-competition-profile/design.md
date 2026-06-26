## Context

The current product has evolved into a modern multi-frontend chemistry learning platform with student H5, teacher console, platform admin console, Atom student assistant, RAG-backed question generation, retrieval diagnostics, intelligent monitoring, video discovery, smart assessment, and class analytics. That is appropriate for the higher-level competition narrative, but it is too visibly AI-agent/RAG-centered for the lower-level competition story now being planned.

The legacy competition profile must present a different product: an inorganic chemistry experiment teaching system centered on experiment knowledge units, BKT knowledge tracing, personalized experiment-video recommendation, smart assessment composition, AI-assisted question-bank construction, teacher review, and teacher learning-score feedback. Reviewers should not reasonably infer that the legacy UI is the same application with a feature switch. At the same time, the legacy profile must not fork the seed data, database, backend, mastery model, question bank, media pipeline, or analytics records.

Relevant current state:

- `docker-compose.yml` already deploys independent frontend services with a generic frontend Dockerfile pattern, so adding old frontend services is feasible without making the backend serve SPA bundles again.
- Current `web-student` already owns the student home video feed, video-library search, point detail playback, Atom assistant routes, assessment routes, and report surfaces.
- Current `web-teacher` owns experiment catalog, question bank, videos, classes, analytics, learning assistant, intelligent monitoring, settings, and student preview routes.
- Backend mastery/BKT behavior already exists around experiment mastery updates, point mastery, assessment attempts, and smart assessment draw probability.
- The available SYSU brand asset directory contains red, green, gold, black, and reverse/white variants for school badge, school name, horizontal/vertical lockups, and campus line/canvas graphics.

## Goals / Non-Goals

**Goals:**

- Create a formal OpenSpec contract for a legacy lower-level competition profile.
- Add two old frontend products, `web-student-old` and `web-teacher-old`, that share the current backend and database.
- Make the old products visually and narratively distinct from the current green Atom/RAG product.
- Center the old product around BKT, experiment-video recommendation, smart assessment, AI question generation, teacher review, and learning-score feedback.
- Remove Atom/RAG/Agent/intelligent-monitoring exposure from old visible UI while preserving supported backend workflows where they are needed behind the scenes.
- Use SYSU red as the old product's canonical brand color and official SYSU SVG assets as the old product's brand material.
- Avoid seed/database splits that could reintroduce the previous seed-mixing risk.

**Non-Goals:**

- Do not delete or degrade the current `web-student`, `web-teacher`, or `web-admin` products.
- Do not create a second database, second seed corpus, or old-only question bank.
- Do not rewrite the BKT model in this change.
- Do not remove RAG, Atom, intelligent monitoring, or diagnostics from the current modern product.
- Do not expose the local `E:\迅雷下载\sysu-logo-main` directory as a runtime or build dependency.
- Do not introduce new LLM/provider features for the old competition profile beyond the existing AI question-generation and teacher-review loop.

## Decisions

### Decision: Add separate old frontend products instead of one global feature flag

Create old student and teacher products as separate frontend apps or separate build entrypoints with their own routing, navigation, theme tokens, brand assets, and tests.

Alternatives considered:

- **Single runtime feature flag in current apps.** This would keep code smaller initially, but the old profile needs different navigation, product copy, theme, video player treatment, and forbidden terminology checks across many surfaces. A runtime flag would likely turn the current apps into conditional spaghetti and make it easier for Atom/RAG UI to leak.
- **Restore a historical branch.** The available historical frontend is not a clean match: earlier student versions already contained AI routes, and older admin assets do not map directly to current student/teacher data contracts. Historical code can inspire layout tone, but it should not become the implementation source of truth.

### Decision: Share backend, database, seed data, and BKT logic

The old frontends must call the same backend and API proxy contract as current frontends. They should consume the same published catalog, video resources, assessment sessions, question bank, mastery state, and class analytics.

This avoids the largest data risk: old/new seed divergence. The old product is a presentation/profile layer over the same core learning engine, not a parallel data universe.

### Decision: Deploy old frontends as Compose services on sequential ports

The old products should be available through Docker Compose as `web-student-old` and `web-teacher-old`, using the existing frontend image pattern where practical. Their default browser ports are fixed as:

- `web-student-old`: `15176`
- `web-teacher-old`: `15177`

These ports intentionally continue after the current frontend port range and keep old demos reachable without changing the current `web-student`, `web-teacher`, or `web-admin` ports.

### Decision: Treat BKT as the visible old-product core

The old product should explicitly present the teaching loop as:

```
AI出题 -> 教师审核 -> 题库
题库 -> 学生测评 -> BKT掌握度
BKT掌握度 -> 推荐视频 / 智能组卷
学习与再测 -> 掌握度更新 -> 教师查看学情分数
```

Visible copy should use terms such as `BKT知识追踪`, `掌握度`, `学情分数`, `个性化推荐`, `智能组卷`, `实验知识导航`, and `AI出题`. It must not use RAG/Agent implementation vocabulary.

### Decision: Use official SYSU red branding for old products only

The old products should define a legacy brand token set with SYSU red as the canonical primary color. The red extracted from the provided official SVGs is approximately `#740003` from `rgb(45.489502%, 0%, 1.176453%)`.

Implementation should copy selected official SVG files into old frontend asset directories, with likely candidates:

- horizontal school badge/name lockup for login and teacher headers;
- standalone badge for sidebar, app icon, or login mark;
- reverse/white variants for red headers if a red background is used;
- optional campus line/canvas graphics as subdued old-product decorative material.

The current green product theme must not be changed by this work.

### Decision: Native/simple video playback in legacy student

The old student point/video detail surface should use native browser controls or a simple traditional media block. It must not use the current self-drawn/custom player chrome, ArtPlayer-based point player, or Atom-oriented video action surface.

This is intentionally a product signal: old should feel like a traditional teaching system, not the new immersive H5 learning product.

### Decision: Visibility gate for forbidden implementation terms

Old visible UI should pass a string/content gate for forbidden terms. Examples include: `Atom`, `RAG`, `Agent`, `chunk`, `embedding`, `rerank`, `Qwen`, `OpenAI`, `BGE`, `ES诊断`, `智能监控`, `学习助手`, and provider/model/debug vocabulary. The gate applies to rendered UI copy, navigation labels, empty states, toasts, table headers, panel titles, and visible diagnostic disclosures in the old frontends.

Allowed terms include `AI出题`, `智能组卷`, `BKT`, `掌握度`, `个性化推荐`, and teacher-facing source/evidence wording that does not disclose retrieval internals.

### Decision: Old teacher removes diagnostic routes but keeps teacher feedback loop

The old teacher frontend should keep enough surfaces for:

- AI-assisted objective question generation;
- teacher preview/review/publish or reject;
- question bank browsing by experiment/video point;
- class/student learning-score review;
- assessment and mastery reporting;
- resource/video/catalog management when needed for the demo.

It should remove learning assistant, intelligent monitoring, AI/RAG/ES diagnostics, provider configuration, and visible retrieval internals from old navigation and old routes.

### Decision: Old visual language should be structurally different, not just red

The old products should use traditional first-level pages, card/table modules, red-accent headers, school identity, and compact admin-style layouts. They should avoid the modern green paper-grid H5 aesthetic, Atom pictogram, floating modern assistant shells, recommendation topic rails, and highly polished immersive player chrome.

The intended visual contrast:

```
Current product:  green / modern H5 / Atom / RAG / immersive detail pages
Legacy product:  SYSU red / traditional teaching platform / BKT / cards + tables
```

## Risks / Trade-offs

- **Risk: Old and current products drift in behavior because UI code is copied.** -> Keep old products thin around shared API clients and shared domain types where practical; test shared API assumptions through both old and current frontends.
- **Risk: RAG/Agent terms leak through reused components, error strings, or metadata labels.** -> Add old-profile string scans and route/navigation tests; wrap raw backend errors with old-product copy.
- **Risk: SYSU assets are referenced from the user's local download path.** -> Copy only selected assets into repository-managed old-app public assets during implementation; document their source.
- **Risk: Old visual distinction becomes only a color swap.** -> Add acceptance scenarios for layout/navigation/player differences, not just token values.
- **Risk: New old containers increase build time and Compose surface area.** -> Reuse the existing frontend Dockerfile pattern and keep old apps scoped; allow old containers to be optional when running only the modern product.
- **Risk: Hiding diagnostics makes operational troubleshooting harder during old demos.** -> Keep current teacher/admin diagnostics in modern products; old products should fail with controlled student/teacher-facing errors and operators can troubleshoot through the current products.
- **Risk: AI question generation still uses RAG internally, creating copy tension.** -> Old teacher UI should say `教材依据`, `实验资料依据`, or `出题依据` rather than `RAG evidence`, `chunk`, or provider labels.
