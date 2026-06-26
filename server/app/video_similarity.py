from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from threatexchange.extensions.vpdq.vpdq import VPDQSignal


def _float_env(name: str, default: float) -> float:
    value = os.getenv(name, "").strip()
    if not value:
        return default
    try:
        return float(value)
    except ValueError:
        return default


def _signature(input_path: Path, output_path: Path, seconds_per_hash: float | None = None) -> None:
    if seconds_per_hash is None:
        seconds_per_hash = _float_env(
            "VIDEO_DUPLICATE_DEFAULT_INTERVAL_SECONDS",
            _float_env("VIDEO_VPDQ_SECONDS_PER_HASH", 3.0),
        )
    signal = VPDQSignal.hash_from_file(input_path, seconds_per_hash=seconds_per_hash)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(signal, encoding="utf-8")


def _compare(current_path: Path, candidate_path: Path) -> None:
    current = current_path.read_text(encoding="utf-8")
    candidate = candidate_path.read_text(encoding="utf-8")
    try:
        comparison = VPDQSignal.compare_hash(current, candidate, 0.0, 0.0)
        info = comparison.distance
        query_percent = float(getattr(info, "query_match_percent", 0.0))
        compared_percent = float(getattr(info, "compared_match_percent", 0.0))
    except ZeroDivisionError:
        query_percent = 0.0
        compared_percent = 0.0
    score = min(query_percent, compared_percent) / 100.0
    print(f"{score:.6f}")
    print(
        json.dumps(
            {
                "algorithm": "vpdq",
                "query_match_percent": query_percent,
                "compared_match_percent": compared_percent,
                "score": score,
            },
            ensure_ascii=False,
        ),
        file=sys.stderr,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Video duplicate-detection helpers backed by Meta vPDQ.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    signature_parser = subparsers.add_parser("vpdq-signature")
    signature_parser.add_argument("input", type=Path)
    signature_parser.add_argument("output", type=Path)
    signature_parser.add_argument("seconds_per_hash", type=float, nargs="?")

    compare_parser = subparsers.add_parser("vpdq-compare")
    compare_parser.add_argument("current", type=Path)
    compare_parser.add_argument("candidate", type=Path)

    args = parser.parse_args(argv)
    if args.command == "vpdq-signature":
        _signature(args.input, args.output, args.seconds_per_hash)
        return 0
    if args.command == "vpdq-compare":
        _compare(args.current, args.candidate)
        return 0
    parser.error("Unsupported command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
