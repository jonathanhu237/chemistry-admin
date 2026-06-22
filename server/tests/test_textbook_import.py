from __future__ import annotations

from pathlib import Path

import pytest

from server.app.domains.experiment_points.textbook_import import (
    normalize_import_text,
    parse_experiment_catalog_markdown,
    parse_point_description_markdown,
)


def test_catalog_parser_treats_leaf_bullets_as_points(tmp_path: Path) -> None:
    path = tmp_path / "catalog.md"
    path.write_text(
        """# 第 13 章 卤族元素

## 二、卤素的氧化性

- 氯、溴、碘的置换次序
  - 氯水 + KBr + CCl₄（点位）
  - 氯水 + KI + CCl₄（点位）
- 氯水对溴离子、碘离子混合溶液的氧化顺序
""",
        encoding="utf-8",
    )

    result = parse_experiment_catalog_markdown(path)

    assert len(result.experiments) == 1
    assert len(result.points) == 3
    assert result.points[0].title == "氯水 + KBr + CCl4"
    assert result.points[0].folder_path == ("氯、溴、碘的置换次序",)
    assert result.points[2].folder_path == ()


def test_description_parser_uses_heading_title_when_directory_path_contains_slashes(tmp_path: Path) -> None:
    path = tmp_path / "descriptions.md"
    path.write_text(
        """# 元素性质实验点位描述汇总

## 第 13 章 卤族元素

### 一、卤素单质在不同溶剂中的溶解性

#### 1. Cl2在水 /四氯化碳 / KI水溶液中的溶解性

**目录路径：** 第 13 章 卤族元素 / 一、卤素单质在不同溶剂中的溶解性 / Cl2在水 /四氯化碳 / KI水溶液中的溶解性

实验原理：
Cl2在不同溶剂中溶解形态不同。

现象解释：
CCl4层呈颜色变化。

安全提示：
CCl4有毒，废液回收。
""",
        encoding="utf-8",
    )

    descriptions = parse_point_description_markdown(path)

    assert len(descriptions) == 1
    assert descriptions[0].title == "Cl2在水 /四氯化碳 / KI水溶液中的溶解性"
    assert descriptions[0].principle.startswith("Cl2")
    assert descriptions[0].phenomenon.startswith("CCl4")
    assert descriptions[0].safety.startswith("CCl4")


def test_import_normalization_matches_subscripts_and_repeat_markers() -> None:
    assert normalize_import_text("氯水 + KBr + CCl₄（点位）") == normalize_import_text("4. 氯水 + KBr + CCl4")
    assert normalize_import_text("NaClO + MnSO₄（重复点位 2）") == normalize_import_text("NaClO + MnSO4")


def test_uploaded_textbook_files_parse_to_expected_counts_when_available() -> None:
    catalog_path = Path(
        "/Users/jonathanhu237/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/"
        "wxid_3w6u3qd3jbea22_ee4b/temp/drag/实验目录_整理版.md"
    )
    description_path = Path(
        "/Users/jonathanhu237/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/"
        "2E36BE3416094863C99F5D0E090653C3/Caches/Files/2026-06/"
        "3ceabce0ceaad9a4c7f02f879e67b542/元素性质实验点位描述汇总.md"
    )
    if not catalog_path.exists() or not description_path.exists():
        pytest.skip("Uploaded textbook Markdown files are not available in this environment")

    catalog = parse_experiment_catalog_markdown(catalog_path)
    descriptions = parse_point_description_markdown(description_path)
    catalog_keys = {
        (
            normalize_import_text(point.chapter),
            normalize_import_text(point.experiment),
            normalize_import_text(point.title),
            point.duplicate_ordinal,
        )
        for point in catalog.points
    }
    unmatched = [
        item
        for item in descriptions
        if (
            normalize_import_text(item.chapter),
            normalize_import_text(item.experiment),
            normalize_import_text(item.title),
            item.duplicate_ordinal,
        )
        not in catalog_keys
    ]

    assert len(catalog.experiments) == 55
    assert len(catalog.points) == 393
    assert len(descriptions) == 393
    assert unmatched == []
