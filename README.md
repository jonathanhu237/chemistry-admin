# SYSU Chemistry Platform Console

This repository contains the standalone admin-management application and the student H5 login shell for the SYSU chemistry experiment learning platform.

It includes:

- React + Ant Design admin frontend in `apps/admin-web`
- React student H5 login frontend in `apps/student-web`
- FastAPI admin backend in `server`
- database migrations in `server/migrations`
- admin bootstrap/import scripts in `scripts`
- seed data for the formal experiment catalog and reviewed curriculum data for admin setup

It intentionally excludes:

- WeChat/student mini-program source
- generated student app JSON bundles
- legacy courseware-derived demo chunks, guessed links, and generated placeholder question seeds
- raw PDF extraction inputs
- intermediate extraction output
- uploaded media files
- local logs, caches, dependency folders, and build output

## Local Development

Install backend dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install frontend dependencies:

```powershell
Set-Location apps/admin-web
npm install
Set-Location ../student-web
npm install
```

Run the admin backend:

```powershell
python -m uvicorn server.app.admin_main:app --host 127.0.0.1 --port 8000 --reload
```

Run the admin frontend:

```powershell
Set-Location apps/admin-web
npm run dev
```

Run the student H5 frontend:

```powershell
Set-Location apps/student-web
npm run dev
```

The student H5 runs at `http://127.0.0.1:5173/` and the admin frontend runs at `http://127.0.0.1:5174/admin/login`. Both proxy `/api` to the backend.

## Production-Style Local Run

Build the frontend first:

```powershell
Set-Location apps/admin-web
npm run build
Set-Location ../student-web
npm run build
```

Then run the backend with the built student H5 mounted at `/` and the built admin frontend mounted at `/admin`:

```powershell
python -m uvicorn server.app.admin_main:app --host 0.0.0.0 --port 8000
```

For Docker Compose, copy `.env.example` to `.env`, adjust secrets and database settings, then run:

```powershell
docker compose up --build
```

## Bootstrap

Apply migrations:

```powershell
python scripts/apply_migrations.py
```

Create or update an admin user:

```powershell
python scripts/bootstrap_admin.py --username admin
```

Import formal admin data and canonical evidence when needed:

```powershell
python scripts/seed_formal_experiments.py
python scripts/publish_reviewed_curriculum.py
python scripts/import_canonical_evidence.py
python scripts/import_experiment_question_bank.py --skip-migrations
python scripts/verify_canonical_evidence.py
```

## Validation

Validate backend import:

```powershell
python -c "import server.app.admin_main as m; print(m.app.title)"
```

Validate the frontend:

```powershell
Set-Location apps/admin-web
npm run typecheck
npm run build
Set-Location ../student-web
npm run typecheck
npm run build
```

Validate OpenSpec:

```powershell
openspec validate extract-admin-management-repo --strict
```

## GitHub Publishing

After the local repository has been created and committed, add the GitHub remote and push:

```powershell
git remote add origin <github-repo-url>
git push -u origin main
```
