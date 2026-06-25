from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.domains.catalog_tree.catalog_seed import load_catalog_seed
from server.app.domains.platform.settings import _textbook_rag_runtime_status, effective_textbook_rag_settings


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Catalog-node evidence generation stub. It verifies that external textbook RAG work targets "
            "leaf catalog nodes by catalog node id or seed key, not legacy experiment_id + point_key."
        )
    )
    parser.add_argument("--skip-rag-health", action="store_true")
    parser.add_argument("--plan-only", action="store_true", help="Print the catalog-node generation plan and exit 0.")
    args = parser.parse_args()

    textbook_settings = effective_textbook_rag_settings()
    nodes = load_catalog_seed()
    points = [node for node in nodes if node.get("node_kind") == "point"]
    plan = {
        "mode": "catalog_node_evidence_generation_stub",
        "point_count": len(points),
        "identity_contract": ["catalog_node_id", "catalog_seed_key"],
        "query_context": "point title plus full catalog path",
        "legacy_identity_rejected": ["experiment_id", "point_key"],
        "source_boundary": "external_textbook_rag",
        "textbook_rag_index": textbook_settings.get("index_name"),
        "sample_points": [
            {
                "catalog_seed_key": point["seed_key"],
                "catalog_path": point["path_titles"],
                "query": " / ".join(point["path_titles"]),
            }
            for point in points[:5]
        ],
    }
    if not args.skip_rag_health:
        runtime = _textbook_rag_runtime_status(textbook_settings, rag_enabled=True)
        plan["textbook_rag_runtime"] = runtime
        if runtime.get("status") != "healthy":
            raise SystemExit(str(runtime.get("message") or "External textbook RAG is not ready."))
    sys.stdout.buffer.write((json.dumps(plan, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    if not args.plan_only:
        raise SystemExit(
            "Catalog-node evidence generation is not implemented in this change. "
            "Run the external textbook RAG evidence refresh job that writes catalog_node_id or catalog_seed_key bindings."
        )


if __name__ == "__main__":
    main()
