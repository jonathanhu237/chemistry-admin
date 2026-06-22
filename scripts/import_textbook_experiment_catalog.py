#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.domains.experiment_points.textbook_import import import_textbook_experiment_catalog


def main() -> None:
    parser = argparse.ArgumentParser(description="Import textbook experiment hierarchy and point descriptions.")
    parser.add_argument("--catalog", required=True, help="Path to 实验目录_整理版.md")
    parser.add_argument("--descriptions", help="Path to 元素性质实验点位描述汇总.md")
    parser.add_argument("--apply", action="store_true", help="Apply changes. Omit for dry-run.")
    parser.add_argument("--user-id", help="Optional app user UUID for created_by/updated_by metadata.")
    args = parser.parse_args()

    report = import_textbook_experiment_catalog(
        catalog_path=Path(args.catalog),
        description_path=Path(args.descriptions) if args.descriptions else None,
        dry_run=not args.apply,
        user_id=args.user_id,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
