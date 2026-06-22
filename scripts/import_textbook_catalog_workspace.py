#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.domains.catalog_tree.markdown_import import import_textbook_catalog_workspace
from server.app.infrastructure.database import apply_migrations


def main() -> None:
    parser = argparse.ArgumentParser(description="Import textbook markdown into the catalog-tree workspace tables.")
    parser.add_argument("--catalog", required=True, help="Path to 实验目录_整理版.md")
    parser.add_argument("--descriptions", required=True, help="Path to 元素性质实验点位描述汇总.md")
    parser.add_argument("--apply", action="store_true", help="Apply changes. Omit for dry-run.")
    parser.add_argument("--skip-migrations", action="store_true")
    parser.add_argument("--no-reset", action="store_true", help="Do not clear catalog/question derived data before import.")
    parser.add_argument("--draft", action="store_true", help="Import nodes and point content as draft instead of published.")
    parser.add_argument("--user-id", help="Optional app user UUID for created_by/updated_by metadata.")
    args = parser.parse_args()

    if args.apply and not args.skip_migrations:
        apply_migrations()

    report = import_textbook_catalog_workspace(
        catalog_path=Path(args.catalog),
        description_path=Path(args.descriptions),
        dry_run=not args.apply,
        reset=not args.no_reset,
        publish=not args.draft,
        user_id=args.user_id,
    )
    sys.stdout.buffer.write((json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n").encode("utf-8"))
    if not report.get("ok"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
