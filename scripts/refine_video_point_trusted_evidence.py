from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


WEAK_EXPERIMENT_SECTION_MARKERS = ("实验目的", "实验预习", "安全知识", "思考题", "注释")
GOOD_EXPERIMENT_TYPES = {"property_test", "reaction", "reagent", "waste_disposal"}
WEAK_THEORY_TYPES = {"table_context", "table_record"}
COMMON_FORMULA_TERMS = {"H", "H2O", "OH"}
LOW_SIGNAL_FORMULA_TERMS = {"CCL4", "H2SO4", "HNO3", "HCL", "AGNO3"}
FORMULA_ALIASES = {
    "KI": {"I2"},
    "KBR": {"BR", "BR2"},
    "NANO2": {"HNO2", "NO2"},
    "KSCN": {"SCN", "NCS"},
    "KMNO4": {"MNO4"},
    "KCLO3": {"CLO3", "CL2"},
    "NA2SO3": {"SO3", "SO32"},
    "NA2O2": {"H2O2", "O2"},
    "BAO22H2O": {"BAO2", "O3"},
    "SO32": {"H2SO3", "SO3"},
    "SO42": {"SO4"},
    "PB3O4": {"PBO2", "PB"},
}
FORMULA_PREVIEW_NEEDLES = {
    "KI": ["KI", "I2", "I^-", "I}^{-}"],
    "KBR": ["KBr", "Br2", "Br^-", "Br}^{-}"],
    "NANO2": ["NaNO_2", "NaNO2", "HNO_2", "HNO2", "NO_2"],
    "NA2O2": ["Na_2O_2", "Na2O2", "H_2O_2", "H2O2"],
    "BAO22H2O": ["BaO_2", "BaO2", "O_3", "O3", "臭氧"],
    "KSCN": ["KSCN", "SCN", "NCS"],
    "KCLO3": ["KClO_3", "KClO3", "ClO_3", "Cl2"],
    "NA2SO3": ["Na_2SO_3", "Na2SO3", "SO_3", "SO3"],
    "KMNO4": ["KMnO_4", "KMNO4", "MnO_4"],
    "SO2": ["SO_2", "SO2"],
    "SO32": ["SO_3", "SO3"],
    "SO42": ["SO_4", "SO4"],
    "PB3O4": ["Pb_3O_4", "Pb3O4", "铅丹"],
    "COCL2": ["CoCl_2", "CoCl2"],
}
GENERIC_CHINESE_TERMS = {
    "实验",
    "性质",
    "观察",
    "变化",
    "生成",
    "反应",
    "溶液",
    "加入",
    "比较",
    "验证",
    "检出",
    "设计",
    "方法",
    "现象",
    "制备",
    "作用",
    "溶液",
    "气体",
}
THEORY_PRINCIPLE_TERMS = {
    "氧化性",
    "还原性",
    "氧化还原",
    "标准电极电势",
    "电势",
    "酸性",
    "碱性",
    "沉淀",
    "溶解度",
    "配合物",
    "络合物",
    "配位",
    "颜色",
    "显色",
    "水解",
    "分解",
    "歧化",
    "平衡",
    "稳定常数",
    "键能",
    "极化",
    "检验",
    "鉴定",
    "萃取",
    "漂白",
    "褪色",
    "恢复",
    "感光",
}
WEAK_THEORY_SECTION_MARKERS = (
    "用途与生物学作用",
    "简介",
)
HARD_WEAK_THEORY_SECTION_MARKERS = ("本章学习要求",)


def _json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def _chunk_text(item: dict[str, Any]) -> str:
    return " ".join(str(item.get("markdown") or item.get("text") or "").split())


def _is_weak_experiment_candidate(item: dict[str, Any]) -> bool:
    section = str(item.get("section_title") or "")
    content_type = str(item.get("content_type") or "")
    if any(marker in section for marker in WEAK_EXPERIMENT_SECTION_MARKERS):
        return True
    if content_type in {"experiment_protocol", "safety_note", "teaching_question_seed"}:
        return True
    return False


def _is_good_experiment_candidate(item: dict[str, Any]) -> bool:
    if _is_weak_experiment_candidate(item):
        return False
    content_type = str(item.get("content_type") or "")
    return content_type in GOOD_EXPERIMENT_TYPES


def _is_good_theory_candidate(item: dict[str, Any]) -> bool:
    content_type = str(item.get("content_type") or "")
    if content_type in WEAK_THEORY_TYPES:
        return False
    if content_type == "figure":
        return False
    section = str(item.get("section_title") or "")
    if any(marker in section for marker in HARD_WEAK_THEORY_SECTION_MARKERS):
        return False
    text = _chunk_text(item)
    if not text:
        return False
    return True


def _score(item: dict[str, Any], key: str, default: float = 0.0) -> float:
    value = item.get(key)
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _chinese_terms(value: str) -> list[str]:
    terms: list[str] = []
    for term in re.findall(r"[\u4e00-\u9fff]{2,}", value or ""):
        if term in GENERIC_CHINESE_TERMS:
            continue
        if len(term) >= 4:
            if term not in GENERIC_CHINESE_TERMS and term not in terms:
                terms.append(term)
            for size in (3, 2):
                for index in range(0, len(term) - size + 1):
                    part = term[index : index + size]
                    if part not in GENERIC_CHINESE_TERMS and part not in terms:
                        terms.append(part)
            continue
        if term not in terms:
            terms.append(term)
    return terms


def _affinity(item: dict[str, Any], record: dict[str, Any]) -> int:
    haystack = f"{item.get('section_title') or ''} {_chunk_text(item)[:1000]}"
    terms = _chinese_terms(str(record.get("experiment_title") or "")) + _chinese_terms(str(record.get("point_title") or ""))
    return sum(1 for term in terms if term and term in haystack)


def _point_affinity(item: dict[str, Any], record: dict[str, Any]) -> int:
    haystack = f"{item.get('section_title') or ''} {_chunk_text(item)[:1000]}"
    return sum(1 for term in _chinese_terms(str(record.get("point_title") or "")) if term and term in haystack)


def _has_canonical_link(item: dict[str, Any]) -> bool:
    return "canonical_experiment_link" in (item.get("candidate_sources") or [])


def _normal_formula(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", value.upper())


def _direct_terms(item: dict[str, Any]) -> set[str]:
    return {
        normal
        for term in item.get("direct_match_terms") or []
        if (normal := _normal_formula(str(term))) and normal not in COMMON_FORMULA_TERMS
    }


def _formula_terms(record: dict[str, Any]) -> set[str]:
    terms: set[str] = set()
    for term in record.get("evidence_terms") or []:
        normal = _normal_formula(str(term))
        if normal and normal not in COMMON_FORMULA_TERMS and re.search(r"[A-Z]", normal):
            terms.add(normal)
    return terms


def _signal_formula_terms(record: dict[str, Any]) -> set[str]:
    return {term for term in _formula_terms(record) if term not in LOW_SIGNAL_FORMULA_TERMS}


def _formula_match_count(item: dict[str, Any], record: dict[str, Any]) -> int:
    wanted = _signal_formula_terms(record)
    if not wanted:
        return 0
    direct = _direct_terms(item)
    matched = set(wanted & direct)
    if len(matched) == len(wanted):
        return len(matched)

    normal_text = _normal_formula(f"{item.get('section_title') or ''} {_chunk_text(item)}")
    for term in wanted - matched:
        aliases = FORMULA_ALIASES.get(term, set())
        if term in normal_text or any(alias in normal_text for alias in aliases):
            matched.add(term)
    return len(matched)


def _fit_sort_key(item: dict[str, Any], record: dict[str, Any]) -> tuple[int, int, int, float, float]:
    return (
        _formula_match_count(item, record),
        len(_direct_terms(item)),
        _point_affinity(item, record),
        _score(item, "evidence_score"),
        _score(item, "rerank_score"),
    )


def _required_formula_matches(record: dict[str, Any]) -> int:
    formulas = _signal_formula_terms(record)
    if not formulas:
        return 0
    return min(2, len(formulas))


def _has_enough_formula_coverage(item: dict[str, Any], record: dict[str, Any]) -> bool:
    required = _required_formula_matches(record)
    return required == 0 or _formula_match_count(item, record) >= required


def _principle_hit_count(item: dict[str, Any]) -> int:
    haystack = f"{item.get('section_title') or ''} {_chunk_text(item)[:1600]}"
    return sum(1 for term in THEORY_PRINCIPLE_TERMS if term in haystack)


def _weak_theory_penalty(item: dict[str, Any]) -> float:
    section = str(item.get("section_title") or "")
    penalty = 0.0
    if any(marker in section for marker in WEAK_THEORY_SECTION_MARKERS):
        penalty += 2.0
    content_type = str(item.get("content_type") or "")
    if content_type in {"definition", "procedure", "property", "comparison"}:
        penalty += 0.25
    if content_type in WEAK_THEORY_TYPES:
        penalty += 1.0
    return penalty


def _is_halogen_displacement_point(record: dict[str, Any]) -> bool:
    title = f"{record.get('experiment_title') or ''} {record.get('point_title') or ''}"
    formulas = _formula_terms(record)
    has_halide_solution = bool({"KI", "KBR"} & formulas)
    return has_halide_solution and any(term in title for term in ("氯水", "溴水", "置换", "先后顺序"))


def _halogen_displacement_adjustment(item: dict[str, Any], record: dict[str, Any]) -> float:
    if not _is_halogen_displacement_point(record):
        return 0.0
    text = f"{item.get('section_title') or ''} {_chunk_text(item)[:1600]}"
    score = 0.0
    if "卤素与化合物的反应" in text:
        score += 2.0
    if any(term in text for term in ("卤离子的还原性顺序", "氧化性不如氯和溴", "非金属性的顺序", "标准电极电势")):
        score += 5.0
    if "含氧酸" in text or "卤素氧化水" in text or "用途与生物学作用" in text:
        score -= 3.0
    if "四氯化碳" in text and not any(term in text for term in ("卤离子", "氧化性", "还原性")):
        score -= 2.0
    return score


def _theory_semantic_score(item: dict[str, Any], record: dict[str, Any]) -> float:
    point_hits = _point_affinity(item, record)
    all_affinity = _affinity(item, record)
    formula_hits = _formula_match_count(item, record)
    principle_hits = _principle_hit_count(item)
    direct_hits = len(_direct_terms(item) - LOW_SIGNAL_FORMULA_TERMS)
    score = (
        point_hits * 2.4
        + max(0, all_affinity - point_hits) * 0.9
        + formula_hits * 1.5
        + min(principle_hits, 3) * 0.8
        + direct_hits * 0.4
        + _score(item, "rerank_score") * 0.6
    )
    if _signal_formula_terms(record) and formula_hits == 0:
        score -= 1.4
    if point_hits == 0 and principle_hits == 0:
        score -= 1.2
    return score + _halogen_displacement_adjustment(item, record) - _weak_theory_penalty(item)


def _focused_preview(item: dict[str, Any], record: dict[str, Any]) -> str:
    text = _chunk_text(item)
    if not text:
        return ""
    needles: list[str] = []
    needles.extend(_chinese_terms(str(record.get("point_title") or "")))
    for term in sorted(_formula_terms(record) | _direct_terms(item)):
        needles.append(term)
        needles.extend(FORMULA_PREVIEW_NEEDLES.get(term, []))

    text_upper = text.upper()
    for needle in sorted({value for value in needles if len(value) >= 2}, key=len, reverse=True):
        position = text.find(needle)
        if position < 0:
            position = text_upper.find(needle.upper())
        if position >= 0:
            start = max(0, position - 140)
            end = min(len(text), position + 320)
            prefix = "..." if start > 0 else ""
            suffix = "..." if end < len(text) else ""
            return f"{prefix}{text[start:end]}{suffix}"
    return text[:420]


def _brief(item: dict[str, Any], reason: str, confidence: str, record: dict[str, Any] | None = None) -> dict[str, Any]:
    formula_terms = sorted(_formula_terms(record)) if record is not None else []
    return {
        "chunk_id": item.get("chunk_id"),
        "reason": reason,
        "confidence": confidence,
        "point_affinity": _affinity(item, record) if record is not None else None,
        "point_title_affinity": _point_affinity(item, record) if record is not None else None,
        "theory_semantic_score": round(_theory_semantic_score(item, record), 4) if record is not None else None,
        "principle_hit_count": _principle_hit_count(item),
        "formula_terms": formula_terms,
        "signal_formula_terms": sorted(_signal_formula_terms(record)) if record is not None else [],
        "formula_match_count": _formula_match_count(item, record) if record is not None else None,
        "rank": item.get("rank"),
        "candidate_sources": item.get("candidate_sources"),
        "rerank_score": item.get("rerank_score"),
        "evidence_score": item.get("evidence_score"),
        "direct_evidence": item.get("direct_evidence"),
        "direct_match_terms": item.get("direct_match_terms"),
        "content_type": item.get("content_type"),
        "page_number": item.get("page_number"),
        "section_title": item.get("section_title"),
        "focused_preview": _focused_preview(item, record) if record is not None else None,
        "text_preview": _chunk_text(item)[:420],
    }


def _append_unique(
    target: list[dict[str, Any]],
    item: dict[str, Any],
    *,
    reason: str,
    confidence: str,
    limit: int,
    record: dict[str, Any] | None = None,
) -> None:
    if len(target) >= limit:
        return
    chunk_id = item.get("chunk_id")
    if not chunk_id or any(existing.get("chunk_id") == chunk_id for existing in target):
        return
    target.append(_brief(item, reason, confidence, record))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _build_raw_index(raw_rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, list[dict[str, Any]]]]:
    index: dict[tuple[str, str], dict[str, list[dict[str, Any]]]] = defaultdict(lambda: {"experiment": [], "theory": []})
    for row in raw_rows:
        key = (str(row.get("experiment_id")), str(row.get("point_key")))
        pool = str(row.get("pool"))
        if pool in {"experiment", "theory"}:
            index[key][pool].append(row)
    for pools in index.values():
        for rows in pools.values():
            rows.sort(key=lambda item: int(item.get("rank") or 999999))
    return index


def _make_sibling_theory_pool(records: list[dict[str, Any]], raw_index: dict[tuple[str, str], dict[str, list[dict[str, Any]]]]) -> dict[str, list[dict[str, Any]]]:
    by_experiment: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for record in records:
        key = (record["experiment_id"], record["point_key"])
        for item in raw_index[key]["theory"]:
            chunk_id = str(item.get("chunk_id") or "")
            if not chunk_id or not item.get("selected_default") or not _is_good_theory_candidate(item):
                continue
            existing = by_experiment[record["experiment_id"]].get(chunk_id)
            if existing is None or _score(item, "evidence_score") > _score(existing, "evidence_score"):
                by_experiment[record["experiment_id"]][chunk_id] = item
    result: dict[str, list[dict[str, Any]]] = {}
    for experiment_id, items in by_experiment.items():
        result[experiment_id] = sorted(
            items.values(),
            key=lambda item: (_score(item, "evidence_score"), _score(item, "rerank_score")),
            reverse=True,
        )
    return result


def select_experiment_evidence(record: dict[str, Any], rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    notes: list[str] = []
    selected: list[dict[str, Any]] = []
    selected_defaults = sorted(
        [item for item in rows if item.get("selected_default") and _is_good_experiment_candidate(item)],
        key=lambda item: (_has_canonical_link(item), *_fit_sort_key(item, record)),
        reverse=True,
    )
    for item in selected_defaults:
        if _score(item, "evidence_score") < 0.25:
            continue
        if not item.get("direct_evidence") and _affinity(item, record) == 0:
            continue
        if selected and not _has_enough_formula_coverage(item, record):
            continue

        confidence = "high"
        if not item.get("direct_evidence") or not _has_enough_formula_coverage(item, record):
            confidence = "medium"
        if _required_formula_matches(record) <= 1 and _point_affinity(item, record) == 0:
            confidence = "medium"
            notes.append("experiment_single_term_match_requires_review")
        _append_unique(selected, item, reason="direct_gate_default_refined", confidence=confidence, limit=2, record=record)
    if not selected:
        canonical = sorted(
            [
                item
                for item in rows[:12]
                if _has_canonical_link(item)
                and _is_good_experiment_candidate(item)
                and _score(item, "rerank_score") >= 0.15
                and (_affinity(item, record) > 0 or _has_enough_formula_coverage(item, record))
            ],
            key=lambda item: _fit_sort_key(item, record),
            reverse=True,
        )
        for item in canonical[:1]:
            confidence = "high" if item.get("direct_evidence") and _has_enough_formula_coverage(item, record) else "medium"
            _append_unique(selected, item, reason="canonical_experiment_link_refined", confidence=confidence, limit=1, record=record)
            notes.append("experiment_default_added_from_canonical_link")
    if not selected:
        ranked = sorted(
            [
                item
                for item in rows[:10]
                if _is_good_experiment_candidate(item)
                and _score(item, "rerank_score") >= 0.35
                and (_affinity(item, record) > 0 or _has_enough_formula_coverage(item, record))
            ],
            key=lambda item: _fit_sort_key(item, record),
            reverse=True,
        )
        for item in ranked[:1]:
            _append_unique(selected, item, reason="codex_refined_top_experiment_candidate", confidence="medium", limit=1, record=record)
            notes.append("experiment_default_added_from_top_candidate")
            break
    if not selected:
        for item in rows[:12]:
            if not _is_weak_experiment_candidate(item) and _score(item, "rerank_score") >= 0.25:
                _append_unique(selected, item, reason="codex_low_confidence_experiment_fallback", confidence="low", limit=1, record=record)
                notes.append("experiment_low_confidence_fallback")
                break
    return selected, notes


def select_theory_evidence(
    record: dict[str, Any],
    rows: list[dict[str, Any]],
    sibling_pool: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    notes: list[str] = []
    selected: list[dict[str, Any]] = []
    candidates = sorted(
        [item for item in rows[:30] if _is_good_theory_candidate(item)],
        key=lambda item: (_theory_semantic_score(item, record), *_fit_sort_key(item, record)),
        reverse=True,
    )
    for item in candidates:
        semantic_score = _theory_semantic_score(item, record)
        if semantic_score < 1.6:
            continue
        if selected:
            first = selected[0]
            same_section = first.get("section_title") == item.get("section_title")
            if semantic_score < 2.2 and not same_section:
                continue
            if _required_formula_matches(record) > 1 and _formula_match_count(item, record) < _required_formula_matches(record) and not same_section:
                continue
            if _point_affinity(item, record) == 0 and not _has_enough_formula_coverage(item, record) and not same_section:
                continue
            if _point_affinity(item, record) == 0 and not same_section:
                current_best_formula_count = max(_formula_match_count(candidate, record) for candidate in candidates)
                if _formula_match_count(item, record) < current_best_formula_count:
                    continue
        confidence = "medium"
        if (
            semantic_score >= 3.2
            and (_point_affinity(item, record) > 0 or _has_enough_formula_coverage(item, record) or _principle_hit_count(item) >= 2)
            and _principle_hit_count(item) > 0
        ):
            confidence = "high"
        reason = "semantic_theory_refined"
        if item.get("selected_default"):
            reason = "semantic_default_theory_refined"
        _append_unique(selected, item, reason=reason, confidence=confidence, limit=1, record=record)
    if len(selected) < 1:
        current_ids = {str(item.get("chunk_id")) for item in rows[:30]}
        before = len(selected)
        for item in sibling_pool:
            if str(item.get("chunk_id")) not in current_ids and selected:
                continue
            if _theory_semantic_score(item, record) >= 2.4 and (
                _point_affinity(item, record) > 0 or _has_enough_formula_coverage(item, record) or _principle_hit_count(item) >= 2
            ):
                _append_unique(selected, item, reason="sibling_point_context_refined", confidence="medium", limit=1, record=record)
        if len(selected) > before:
            notes.append("theory_context_filled_from_sibling_points")
    if not selected:
        ranked = sorted(
            [
                item
                for item in rows[:12]
                if _is_good_theory_candidate(item)
                and _score(item, "rerank_score") >= 0.45
                and _theory_semantic_score(item, record) >= 1.0
            ],
            key=lambda item: (_theory_semantic_score(item, record), *_fit_sort_key(item, record)),
            reverse=True,
        )
        for item in ranked[:1]:
                _append_unique(selected, item, reason="codex_refined_top_theory_candidate", confidence="medium", limit=1, record=record)
                notes.append("theory_default_added_from_top_candidate")
                break
    if not selected:
        for item in rows[:15]:
            if _is_good_theory_candidate(item) and _score(item, "rerank_score") >= 0.35:
                _append_unique(selected, item, reason="codex_low_confidence_theory_fallback", confidence="low", limit=1, record=record)
                notes.append("theory_low_confidence_fallback")
                break
    if not selected:
        notes.append("theory_not_found_in_recalled_candidates")
    return selected, notes


def confidence_for(selected: list[dict[str, Any]]) -> str:
    if not selected:
        return "missing"
    if any(item.get("confidence") == "low" for item in selected):
        return "low"
    if all(item.get("confidence") == "high" for item in selected):
        return "high"
    return "medium"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a curated trusted evidence artifact from direct-v2 candidates.")
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    run_dir = args.run_dir
    output_dir = args.output_dir or run_dir / "trusted"
    output_dir.mkdir(parents=True, exist_ok=True)

    point_records = _load_jsonl(run_dir / "point_default_evidence.jsonl")
    raw_rows = _load_jsonl(run_dir / "raw_candidates.jsonl")
    raw_index = _build_raw_index(raw_rows)
    sibling_theory_pool = _make_sibling_theory_pool(point_records, raw_index)

    trusted_records: list[dict[str, Any]] = []
    for record in point_records:
        key = (record["experiment_id"], record["point_key"])
        pools = raw_index[key]
        experiment_evidence, experiment_notes = select_experiment_evidence(record, pools["experiment"])
        theory_evidence, theory_notes = select_theory_evidence(
            record,
            pools["theory"],
            sibling_theory_pool.get(record["experiment_id"], []),
        )
        review_notes = experiment_notes + theory_notes
        exp_confidence = confidence_for(experiment_evidence)
        theory_confidence = confidence_for(theory_evidence)
        if exp_confidence == "high" and theory_confidence == "high":
            review_status = "trusted"
        elif exp_confidence in {"high", "medium"} and theory_confidence in {"high", "medium", "low"}:
            review_status = "usable_with_review_note"
        else:
            review_status = "needs_manual_review"
        trusted_records.append(
            {
                "experiment_id": record["experiment_id"],
                "experiment_code": record.get("experiment_code"),
                "experiment_title": record.get("experiment_title"),
                "point_key": record["point_key"],
                "point_title": record["point_title"],
                "evidence_terms": record.get("evidence_terms") or [],
                "trusted_experiment_chunk_ids": [item["chunk_id"] for item in experiment_evidence],
                "trusted_theory_chunk_ids": [item["chunk_id"] for item in theory_evidence],
                "experiment_evidence": experiment_evidence,
                "theory_evidence": theory_evidence,
                "experiment_confidence": exp_confidence,
                "theory_confidence": theory_confidence,
                "review_status": review_status,
                "review_notes": review_notes,
                "source_run": run_dir.name,
            }
        )

    out_jsonl = output_dir / "point_trusted_evidence.jsonl"
    out_jsonl.write_text("\n".join(_json_dumps(record) for record in trusted_records) + "\n", encoding="utf-8")

    summary_counts: dict[str, int] = defaultdict(int)
    for record in trusted_records:
        summary_counts[f"status:{record['review_status']}"] += 1
        summary_counts[f"experiment:{record['experiment_confidence']}"] += 1
        summary_counts[f"theory:{record['theory_confidence']}"] += 1
        if not record["trusted_experiment_chunk_ids"]:
            summary_counts["missing_experiment"] += 1
        if not record["trusted_theory_chunk_ids"]:
            summary_counts["missing_theory"] += 1

    summary = {
        "artifact_mode": "trusted-refine-v1",
        "source_run": run_dir.name,
        "point_count": len(trusted_records),
        "counts": dict(sorted(summary_counts.items())),
        "output": str(out_jsonl),
        "status_semantics": {
            "trusted": "Both experiment and theory evidence are high-confidence direct support.",
            "usable_with_review_note": "The point has complete experiment/theory coverage, but at least one side is medium-confidence and should be treated as supporting evidence rather than canonical truth.",
            "needs_manual_review": "Evidence is missing or low-confidence.",
        },
        "write_boundary": "Read-only artifact generation. No question-bank rows, source chunks, metadata, or publish status are modified.",
    }
    (output_dir / "manifest.json").write_text(_json_dumps(summary) + "\n", encoding="utf-8")

    lines = [
        "# Trusted Evidence Refinement",
        "",
        "- Artifact mode: `trusted-refine-v1`",
        f"- Source run: `{run_dir.name}`",
        f"- Points: {len(trusted_records)}",
        "- Boundary: read-only artifact generation; no question-bank rows, metadata, answers, source chunks, or publish status are modified.",
        "",
        "## Status Semantics",
        "",
        "- `trusted`: experiment evidence and theory evidence are both high-confidence direct support.",
        "- `usable_with_review_note`: the point has experiment and theory coverage, but at least one side is medium-confidence and should be treated as supporting evidence rather than canonical truth.",
        "- `needs_manual_review`: evidence is missing or low-confidence.",
        "",
        "## Counts",
    ]
    for key, value in sorted(summary_counts.items()):
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Review Notes")
    for record in trusted_records:
        if record["review_status"] == "trusted" and not record["review_notes"]:
            continue
        lines.extend(
            [
                "",
                f"### {record['experiment_id']} / {record['point_key']}",
                f"- Point: {record['point_title']}",
                f"- Status: {record['review_status']}",
                f"- Experiment confidence: {record['experiment_confidence']}",
                f"- Theory confidence: {record['theory_confidence']}",
                f"- Experiment chunks: {', '.join(record['trusted_experiment_chunk_ids']) or '-'}",
                f"- Theory chunks: {', '.join(record['trusted_theory_chunk_ids']) or '-'}",
                f"- Notes: {', '.join(record['review_notes']) or '-'}",
            ]
        )
    (output_dir / "curation_notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(_json_dumps(summary))


if __name__ == "__main__":
    main()
