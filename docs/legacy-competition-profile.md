# Legacy Competition Profile

The lower-level competition profile is implemented as two separate frontend apps:

- `apps/web-student-old`: legacy student experiment-video learning frontend.
- `apps/web-teacher-old`: legacy teacher BKT teaching-management frontend.

The old apps share the same backend, database, catalog, video resources, question bank, assessment sessions, mastery records, and analytics records as the current products. They are not a seed fork and must not introduce old-only runtime ids.

The product narrative is intentionally different from the current green modern product. The old profile centers:

- experiment knowledge navigation;
- AI-assisted objective question creation;
- teacher review before publication;
- BKT mastery tracking;
- personalized experiment-video recommendation;
- smart assessment composition;
- teacher learning-score review.

The old visible UI uses SYSU red branding and official SYSU logo assets copied into each old app's `public/assets` directory. The source material is the local official asset package at `E:\迅雷下载\sysu-logo-main`, but builds must use repository-managed copies only.

Deployment adds optional Compose services:

- `web-student-old`, default endpoint `222.200.189.249:15176`;
- `web-teacher-old`, default endpoint `127.0.0.1:15177`.

Use `python scripts/deploy_compose_stack.py --include-legacy` or `python scripts/validate_compose_stack.py --include-legacy` when the old services should be part of a demo or smoke run. The default current-product Compose path remains valid without old services.

The existing `web-admin` endpoint remains local-only; do not move platform operations workflows into the old teacher product.
