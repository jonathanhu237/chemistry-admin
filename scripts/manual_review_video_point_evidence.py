from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BASE_RUN = Path("artifacts/video-point-default-evidence/gpu-rerank-direct-v2-20260616T1140Z")
RAW_PATH = BASE_RUN / "raw_candidates.jsonl"
TRUSTED_PATH = BASE_RUN / "trusted" / "point_trusted_evidence.jsonl"
OUTPUT_DIR = Path(os.environ.get("MANUAL_REVIEW_OUTPUT_DIR", str(BASE_RUN / "manual-reviewed-fast-20260616T2055Z")))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def point_id(row: dict[str, Any]) -> str:
    return f"{row['experiment_id']}::{row['point_key']}"


def short_text(value: str | None, limit: int = 360) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def candidate_brief(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "chunk_id": item.get("chunk_id"),
        "pool": item.get("pool"),
        "rank": item.get("rank"),
        "selected_default": item.get("selected_default"),
        "content_type": item.get("content_type"),
        "section_title": item.get("section_title"),
        "rerank_score": item.get("rerank_score"),
        "evidence_score": item.get("evidence_score"),
        "direct_evidence": item.get("direct_evidence"),
        "direct_match_terms": item.get("direct_match_terms") or [],
        "text": short_text(item.get("text") or item.get("markdown"), 520),
    }


def trusted_item_brief(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "chunk_id": item.get("chunk_id"),
        "confidence": item.get("confidence"),
        "content_type": item.get("content_type"),
        "section_title": item.get("section_title"),
        "rerank_score": item.get("rerank_score"),
        "evidence_score": item.get("evidence_score"),
        "theory_semantic_score": item.get("theory_semantic_score"),
        "principle_hit_count": item.get("principle_hit_count"),
        "direct_match_terms": item.get("direct_match_terms") or [],
        "text": short_text(item.get("focused_preview") or item.get("text_preview"), 520),
    }


def load_raw_index() -> dict[str, dict[str, list[dict[str, Any]]]]:
    index: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: {"experiment": [], "theory": []})
    with RAW_PATH.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            item = json.loads(line)
            pool = str(item.get("pool") or "")
            if pool not in {"experiment", "theory"}:
                continue
            key = f"{item['experiment_id']}::{item['point_key']}"
            index[key][pool].append(item)
    for pools in index.values():
        for pool in ("experiment", "theory"):
            pools[pool].sort(
                key=lambda item: (
                    bool(item.get("selected_default")),
                    float(item.get("evidence_score") or 0),
                    float(item.get("rerank_score") or 0),
                ),
                reverse=True,
            )
    return index


def init_output() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    trusted_rows = read_jsonl(TRUSTED_PATH)
    fingerprint = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "mode": "manual-reviewed-fast",
        "objective": "逐点去伪存真，输出轻量最终 point evidence chunk ids。",
        "input_files": {
            "raw_candidates": {
                "path": str(RAW_PATH),
                "sha256": sha256_file(RAW_PATH),
                "bytes": RAW_PATH.stat().st_size,
            },
            "trusted": {
                "path": str(TRUSTED_PATH),
                "sha256": sha256_file(TRUSTED_PATH),
                "bytes": TRUSTED_PATH.stat().st_size,
            },
        },
        "point_count": len(trusted_rows),
        "trusted_status_counts": Counter(row.get("review_status") for row in trusted_rows),
        "note": "Final manual_reviewed=true is written only through review decisions, not by this init step.",
    }
    (OUTPUT_DIR / "input_fingerprint.json").write_text(
        json.dumps(fingerprint, ensure_ascii=False, indent=2, default=dict) + "\n",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "decisions").mkdir(exist_ok=True)
    (OUTPUT_DIR / "review_packets").mkdir(exist_ok=True)


def build_packet(args: argparse.Namespace) -> Path:
    trusted_rows = read_jsonl(TRUSTED_PATH)
    raw_index = load_raw_index()
    rows = trusted_rows
    if args.codes:
        wanted = set(args.codes.split(","))
        rows = [row for row in rows if row.get("experiment_code") in wanted]
    if args.offset:
        rows = rows[args.offset :]
    if args.limit:
        rows = rows[: args.limit]

    packet = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "count": len(rows),
        "points": [],
    }
    lines: list[str] = [
        "# Manual Review Packet",
        "",
        f"- count: {len(rows)}",
        "- Keep chunks that support operation, phenomenon, reaction, principle, equation, or necessary background.",
        "- Delete chunks that are only wording/auxiliary-reagent matches.",
        "",
    ]
    for index, row in enumerate(rows, 1):
        key = point_id(row)
        raw = raw_index.get(key, {"experiment": [], "theory": []})
        point = {
            "experiment_id": row.get("experiment_id"),
            "experiment_code": row.get("experiment_code"),
            "point_key": row.get("point_key"),
            "point_title": row.get("point_title"),
            "trusted_experiment_chunk_ids": row.get("trusted_experiment_chunk_ids") or [],
            "trusted_theory_chunk_ids": row.get("trusted_theory_chunk_ids") or [],
            "trusted_experiment_evidence": [trusted_item_brief(item) for item in row.get("experiment_evidence") or []],
            "trusted_theory_evidence": [trusted_item_brief(item) for item in row.get("theory_evidence") or []],
            "raw_experiment_top": [candidate_brief(item) for item in raw["experiment"][: args.raw_top]],
            "raw_theory_top": [candidate_brief(item) for item in raw["theory"][: args.raw_top]],
        }
        packet["points"].append(point)
        lines.extend(
            [
                f"## {index}. {point['experiment_code']} / {point['point_title']}",
                "",
                f"- point_key: `{point['point_key']}`",
                f"- current experiment: `{', '.join(point['trusted_experiment_chunk_ids'])}`",
                f"- current theory: `{', '.join(point['trusted_theory_chunk_ids'])}`",
                "",
                "### Current Experiment Evidence",
            ]
        )
        for item in point["trusted_experiment_evidence"]:
            lines.append(
                f"- `{item['chunk_id']}` {item.get('confidence')} {item.get('content_type')} "
                f"score={item.get('evidence_score')} section={item.get('section_title')}\n"
                f"  {item.get('text')}"
            )
        lines.append("")
        lines.append("### Current Theory Evidence")
        for item in point["trusted_theory_evidence"]:
            lines.append(
                f"- `{item['chunk_id']}` {item.get('confidence')} {item.get('content_type')} "
                f"semantic={item.get('theory_semantic_score')} section={item.get('section_title')}\n"
                f"  {item.get('text')}"
            )
        lines.append("")
        lines.append("### Raw Experiment Top")
        for item in point["raw_experiment_top"]:
            lines.append(
                f"- `{item['chunk_id']}` rank={item.get('rank')} selected={item.get('selected_default')} "
                f"type={item.get('content_type')} score={item.get('evidence_score')} matches={item.get('direct_match_terms')} "
                f"section={item.get('section_title')}\n  {item.get('text')}"
            )
        lines.append("")
        lines.append("### Raw Theory Top")
        for item in point["raw_theory_top"]:
            lines.append(
                f"- `{item['chunk_id']}` rank={item.get('rank')} selected={item.get('selected_default')} "
                f"type={item.get('content_type')} score={item.get('evidence_score')} matches={item.get('direct_match_terms')} "
                f"section={item.get('section_title')}\n  {item.get('text')}"
            )
        lines.append("")

    suffix = args.name or datetime.now().strftime("%Y%m%dT%H%M%S")
    json_path = OUTPUT_DIR / "review_packets" / f"{suffix}.json"
    md_path = OUTPUT_DIR / "review_packets" / f"{suffix}.md"
    json_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return md_path


def load_decisions() -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    for path in sorted((OUTPUT_DIR / "decisions").glob("*.jsonl")):
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row = json.loads(line)
                key = f"{row['experiment_id']}::{row['point_key']}"
                decisions[key] = row
    return decisions


def build_final() -> None:
    trusted_rows = read_jsonl(TRUSTED_PATH)
    decisions = load_decisions()
    final_rows: list[dict[str, Any]] = []
    missing: list[str] = []
    for source in trusted_rows:
        key = point_id(source)
        decision = decisions.get(key)
        if not decision:
            missing.append(key)
            continue
        row = {
            "experiment_id": source["experiment_id"],
            "experiment_code": source["experiment_code"],
            "point_key": source["point_key"],
            "point_title": source["point_title"],
            "experiment_chunk_ids": decision.get("experiment_chunk_ids") or [],
            "theory_chunk_ids": decision.get("theory_chunk_ids") or [],
            "manual_reviewed": bool(decision.get("manual_reviewed")),
            "review_grade": decision.get("review_grade"),
        }
        final_rows.append(row)

    errors: list[str] = []
    if missing:
        errors.append(f"missing decisions: {len(missing)}")
    seen = Counter(row["point_key"] for row in final_rows)
    duplicates = [key for key, count in seen.items() if count > 1]
    if duplicates:
        errors.append(f"duplicate point_key: {duplicates[:5]}")
    if any(not row["experiment_chunk_ids"] for row in final_rows):
        errors.append("some rows have no experiment_chunk_ids")
    if any(not row["theory_chunk_ids"] for row in final_rows):
        errors.append("some rows have no theory_chunk_ids")
    if any(row["manual_reviewed"] is not True for row in final_rows):
        errors.append("some rows are not manual_reviewed=true")
    invalid_grade = [
        row["point_key"]
        for row in final_rows
        if row["review_grade"] not in {"pass", "usable", "weak_but_best_available"}
    ]
    if invalid_grade:
        errors.append(f"invalid review_grade: {invalid_grade[:5]}")

    write_jsonl(OUTPUT_DIR / "manual_reviewed_point_evidence.jsonl", final_rows)
    summary = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "row_count": len(final_rows),
        "missing_decision_count": len(missing),
        "grade_counts": Counter(row.get("review_grade") for row in final_rows),
        "experiment_chunk_count_distribution": Counter(len(row["experiment_chunk_ids"]) for row in final_rows),
        "theory_chunk_count_distribution": Counter(len(row["theory_chunk_ids"]) for row in final_rows),
        "errors": errors,
    }
    (OUTPUT_DIR / "manifest.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, default=dict) + "\n",
        encoding="utf-8",
    )
    (OUTPUT_DIR / "summary.md").write_text(
        "\n".join(
            [
                "# Manual Reviewed Point Evidence",
                "",
                f"- rows: {summary['row_count']}",
                f"- missing decisions: {summary['missing_decision_count']}",
                f"- grades: {dict(summary['grade_counts'])}",
                f"- experiment chunk counts: {dict(summary['experiment_chunk_count_distribution'])}",
                f"- theory chunk counts: {dict(summary['theory_chunk_count_distribution'])}",
                f"- errors: {errors or 'none'}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    if errors:
        raise SystemExit("; ".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    packet = sub.add_parser("packet")
    packet.add_argument("--codes", help="Comma-separated experiment_code values.")
    packet.add_argument("--limit", type=int)
    packet.add_argument("--offset", type=int, default=0)
    packet.add_argument("--raw-top", type=int, default=5)
    packet.add_argument("--name")
    sub.add_parser("build-final")
    args = parser.parse_args()
    if args.command == "init":
        init_output()
    elif args.command == "packet":
        print(build_packet(args))
    elif args.command == "build-final":
        build_final()


if __name__ == "__main__":
    main()
