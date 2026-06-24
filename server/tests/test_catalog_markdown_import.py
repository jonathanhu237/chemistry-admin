from __future__ import annotations

from pathlib import Path

from server.app.domains.catalog_tree.markdown_import import build_markdown_import_plan, parse_catalog_markdown, principle_import_from_text


def test_markdown_catalog_skips_placeholder_chapter(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.md"
    catalog.write_text(
        "\n".join(
            [
                "# 第 21 章 镧系和锕系元素",
                "",
                "## 一、暂无对应实验内容",
                "",
                "# 第 22 章 氢和稀有气体",
                "",
                "## 一、氢气的制备与性质",
                "",
                "- 氢气的制备",
            ]
        ),
        encoding="utf-8",
    )

    nodes = parse_catalog_markdown(catalog)

    assert [node.title for node in nodes] == ["氢气的制备与性质", "氢气的制备"]


def test_markdown_import_matches_titles_containing_slashes(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.md"
    descriptions = tmp_path / "descriptions.md"
    catalog.write_text(
        "\n".join(
            [
                "# 第 13 章 卤族元素",
                "",
                "## 二、卤素的氧化性",
                "",
                "- 氯水、溴水分别与H2S / Na2S反应",
                "  - 氯水 + H2S / Na2S",
            ]
        ),
        encoding="utf-8",
    )
    descriptions.write_text(
        "\n".join(
            [
                "# 元素性质实验点位描述汇总",
                "",
                "## 第 13 章 卤族元素",
                "",
                "### 二、卤素的氧化性",
                "",
                "#### 1. 氯水 + H2S / Na2S",
                "",
                "**目录路径：** 第 13 章 卤族元素 / 二、卤素的氧化性 / 氯水、溴水分别与H2S / Na2S反应 / 氯水 + H2S / Na2S",
                "",
                "实验原理：",
                "Cl₂ + H₂S → S↓ + 2HCl",
                "",
                "现象解释：",
                "产生硫浑浊。",
                "",
                "安全提示：",
                "通风橱内操作。",
            ]
        ),
        encoding="utf-8",
    )

    plan = build_markdown_import_plan(catalog_path=catalog, description_path=descriptions)

    assert plan["ok"] is True
    assert plan["counts"]["matched_content_records"] == 1
    assert plan["counts"]["equation_content_records"] == 1
    assert [node.title for node in plan["nodes"] if node.node_kind == "directory"] == [
        "卤素的氧化性",
        "氯水、溴水分别与H2S / Na2S反应",
    ]


def test_markdown_import_splits_sibling_duplicate_canonical_points(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.md"
    descriptions = tmp_path / "descriptions.md"
    catalog.write_text(
        "\n".join(
            [
                "# 第 13 章 卤族元素",
                "",
                "## 五、卤素含氧酸盐的氧化性",
                "",
                "- 次氯酸盐的氧化性",
                "  - NaClO + MnSO₄",
                "  - NaClO + MnSO₄",
            ]
        ),
        encoding="utf-8",
    )
    descriptions.write_text(
        "\n\n".join(
            [
                "# 元素性质实验点位描述汇总",
                "## 第 13 章 卤族元素",
                "### 五、卤素含氧酸盐的氧化性",
                "#### 1. NaClO + MnSO₄\n\n**目录路径：** 第 13 章 卤族元素 / 五、卤素含氧酸盐的氧化性 / 次氯酸盐的氧化性 / NaClO + MnSO₄\n\n实验原理：\nMn²⁺ + ClO⁻ + 2OH⁻ → MnO₂↓ + Cl⁻ + H₂O\n\n现象解释：\n生成沉淀。\n\n安全提示：\n避免接触。",
                "#### 2. NaClO + MnSO₄\n\n**目录路径：** 第 13 章 卤族元素 / 五、卤素含氧酸盐的氧化性 / 次氯酸盐的氧化性 / NaClO + MnSO₄\n\n实验原理：\nMn²⁺ + ClO⁻ + 2OH⁻ → MnO₂↓ + Cl⁻ + H₂O\n\n现象解释：\n生成沉淀。\n\n安全提示：\n避免接触。",
            ]
        ),
        encoding="utf-8",
    )

    plan = build_markdown_import_plan(catalog_path=catalog, description_path=descriptions)
    point_nodes = [node for node in plan["nodes"] if node.node_kind == "point"]

    assert plan["ok"] is True
    assert len({node.canonical_point_id for node in point_nodes}) == 2
    assert plan["duplicate_parent_canonical"] == []


def test_principle_import_extracts_reaction_with_annotation() -> None:
    principle = "BrO₃⁻在酸性条件下氧化Br⁻：BrO₃⁻ + 5Br⁻ + 6H⁺ → 3Br₂ + 3H₂O。"

    result = principle_import_from_text(principle)

    assert result.mode == "equation"
    assert result.reaction_rows == [
        {
            "raw_text": "BrO₃⁻ + 5Br⁻ + 6H⁺ → 3Br₂ + 3H₂O // BrO₃⁻在酸性条件下氧化Br⁻",
            "row_order": 1,
            "metadata": {"source": "markdown_principle_equation_extraction"},
        }
    ]
