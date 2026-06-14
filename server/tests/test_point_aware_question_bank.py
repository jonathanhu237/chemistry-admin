from __future__ import annotations

import json

from scripts.point_aware_question_bank import prepare_import_rows
from server.app.experiment_admin import _attempt_diagnostic_metadata


def test_prepare_import_rows_preserves_point_metadata(tmp_path):
    inventory_path = tmp_path / "inventory.json"
    artifact_path = tmp_path / "bank.json"
    inventory_path.write_text(
        json.dumps(
            {
                "experiments": [
                    {
                        "experiment_id": "EXP_TEST",
                        "code": "T-1",
                        "title": "测试实验",
                        "chapter_bindings": [{"chapter_id": "CH13"}],
                        "video_points": [
                            {
                                "point_key": "point-1",
                                "point_title": "观察颜色变化",
                                "source": "formal_experiment.video_candidates",
                            }
                        ],
                        "canonical_chunk_ids": ["chunk-1"],
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    artifact_path.write_text(
        json.dumps(
            {
                "metadata": {"artifact_type": "point_aware_question_bank", "version": "test-v1"},
                "experiments": [
                    {
                        "experiment_id": "EXP_TEST",
                        "experiment_code": "T-1",
                        "experiment_title": "测试实验",
                        "video_points": [{"point_key": "point-1", "point_title": "观察颜色变化"}],
                        "questions": [
                            {
                                "question_id": "Q1",
                                "question_type": "single_choice",
                                "stem": "下列哪一项符合观察点位？",
                                "options": [
                                    {"label": "A", "text": "观察颜色变化"},
                                    {"label": "B", "text": "记录仪器编号"},
                                ],
                                "answer": {"value": "A"},
                                "explanation": "该点位要求观察颜色变化。",
                                "difficulty": "basic",
                                "review_decision": "keep",
                                "quality_flags": ["reviewed"],
                                "primary_point_keys": ["point-1"],
                                "coverage_tags": ["phenomenon_observation"],
                                "option_links": [
                                    {"label": "A", "point_key": "point-1", "role": "correct_evidence"},
                                    {"label": "B", "point_key": None, "role": "unrelated_distractor"},
                                ],
                                "source_audit": {
                                    "canonical_chunk_ids": ["chunk-1"],
                                    "supporting_theory_chunk_ids": [],
                                    "evidence_sufficient": True,
                                    "reviewer_note": "人工审查通过。",
                                },
                            }
                        ],
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    rows, validation_report, prepare_report = prepare_import_rows(artifact_path, inventory_path)

    assert validation_report["valid"] is True
    assert prepare_report["prepared_question_count"] == 1
    assert rows[0]["metadata"]["primary_point_keys"] == ["point-1"]
    assert rows[0]["metadata"]["primary_points"] == [{"point_key": "point-1", "point_title": "观察颜色变化"}]
    assert rows[0]["related_chapter_ids"] == ["CH13"]
    assert rows[0]["source_chunk_ids"] == ["chunk-1"]


def test_attempt_diagnostic_metadata_captures_selected_option_link():
    question = {
        "question_type": "single_choice",
        "metadata": {
            "point_aware_question_bank": True,
            "primary_point_keys": ["point-1"],
            "primary_points": [{"point_key": "point-1", "point_title": "观察颜色变化"}],
            "coverage_tags": ["phenomenon_observation"],
            "option_links": [
                {"label": "A", "point_key": "point-1", "role": "correct_evidence"},
                {"label": "B", "point_key": None, "role": "unrelated_distractor"},
            ],
        },
    }

    metadata = _attempt_diagnostic_metadata(question, "B", False)

    assert metadata["point_aware_question_bank"] is True
    assert metadata["primary_point_keys"] == ["point-1"]
    assert metadata["selected_option_label"] == "B"
    assert metadata["diagnostic_role"] == "unrelated_distractor"
