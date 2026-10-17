#!/usr/bin/env python3
"""Repository invariant validators for ai-news-daily.

ROUTINE.md / CLAUDE.md で規定したスキーマ・必須セクションを CI から検証する。
GitHub Actions の `.github/workflows/validate.yml` から呼ばれる。

Usage:
    python3 scripts/validate.py {sources,data,summaries,all}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Callable

import yaml

# ===== 共有スキーマ定数 (DRY: ここが正規の場所) =====
# ROUTINE.md の「カテゴリ別の優先度」「Step 6 出力フォーマット」「Step 6.5 構造化データ」
# と同期させる。ROUTINE.md を改訂したらここも更新する。

ALLOWED_CATEGORIES = frozenset({"vendor", "community", "papers_trending", "media", "media_jp"})
ALLOWED_PRIORITIES = frozenset({"high", "medium", "low"})
ALLOWED_ITEM_TYPES = frozenset({"new", "followup", "no-update"})

REQUIRED_SOURCE_FIELDS = ("name", "url", "category")
REQUIRED_ITEM_FIELDS = ("id", "type", "vendor", "section")

REQUIRED_MD_SECTIONS = (
    "## 🔥 今日のハイライト",
    "## 🏢 企業・モデル発表",
    "## 💻 技術コミュニティ",
    "## 📚 話題の研究論文",
    "## 📰 メディア記事",
    "## 📊 メタ情報",
)


# ===== 検証関数 (SRP: 1関数 = 1検証対象) =====


def validate_sources(path: Path) -> list[str]:
    """sources.yaml がスキーマを満たすか検証する。"""
    if not path.exists():
        return [f"{path}: file not found"]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"{path}: invalid YAML: {e}"]

    if not isinstance(data, dict) or "sources" not in data:
        return [f"{path}: top-level must be a mapping with 'sources' key"]
    sources = data["sources"]
    if not isinstance(sources, list):
        return [f"{path}: 'sources' must be a list"]

    errors: list[str] = []
    seen_names: set[str] = set()
    for i, src in enumerate(sources):
        prefix = f"{path} sources[{i}]"
        if not isinstance(src, dict):
            errors.append(f"{prefix}: not a mapping")
            continue
        for field in REQUIRED_SOURCE_FIELDS:
            if field not in src:
                errors.append(f"{prefix}: missing required field '{field}'")
        cat = src.get("category")
        if cat is not None and cat not in ALLOWED_CATEGORIES:
            errors.append(
                f"{prefix}: unknown category {cat!r} "
                f"(allowed: {sorted(ALLOWED_CATEGORIES)})"
            )
        pri = src.get("priority")
        if pri is not None and pri not in ALLOWED_PRIORITIES:
            errors.append(f"{prefix}: unknown priority {pri!r}")
        name = src.get("name")
        if name in seen_names:
            errors.append(f"{prefix}: duplicate name {name!r}")
        if name:
            seen_names.add(name)
    return errors


def validate_data(root: Path) -> list[str]:
    """docs/data/index.json および items/*.json の構造を検証する。"""
    if not root.exists():
        return []  # 初期セットアップ時はデータが無いことを許容
    errors = _validate_index(root / "index.json")
    items_dir = root / "items"
    if items_dir.exists():
        for path in sorted(items_dir.glob("*.json")):
            errors += _validate_items_file(path)
    return errors


def _validate_index(path: Path) -> list[str]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"{path}: invalid JSON: {e}"]
    if not isinstance(data, list):
        return [f"{path}: must be a flat array (ROUTINE.md Step 6.5 B)"]

    errors: list[str] = []
    for i, item in enumerate(data):
        prefix = f"{path}[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: not an object")
            continue
        for key in ("date", "id"):
            if key not in item:
                errors.append(f"{prefix}: missing '{key}'")
    return errors


def _validate_items_file(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"{path}: invalid JSON: {e}"]
    if not isinstance(data, dict):
        return [f"{path}: top-level must be an object"]

    errors: list[str] = []
    for key in ("date", "items"):
        if key not in data:
            errors.append(f"{path}: missing top-level '{key}'")

    items = data.get("items") or []
    if not isinstance(items, list):
        errors.append(f"{path}: 'items' must be a list")
        return errors

    for i, item in enumerate(items):
        prefix = f"{path} items[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: not an object")
            continue
        for field in REQUIRED_ITEM_FIELDS:
            if field not in item:
                errors.append(f"{prefix}: missing '{field}'")
        item_type = item.get("type")
        if item_type not in ALLOWED_ITEM_TYPES:
            errors.append(f"{prefix}: unknown type {item_type!r}")
        # 注: ROUTINE.md は url を required フィールドに含めていない。
        # community/papers セクションのダイジェスト等、単一の元記事 URL を持たない
        # 正当な item が実際に存在するため、url の有無は検証しない。
    return errors


def validate_summaries(root: Path) -> list[str]:
    """各 summary md が ROUTINE.md Step 6 の必須セクションを含むか検証する。"""
    if not root.exists():
        return []
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_MD_SECTIONS:
            if section not in text:
                errors.append(f"{path}: missing required section '{section}'")
    return errors


# ===== CLI エントリポイント =====

# 単一の正規ルックアップテーブル。新しいターゲットを足すならここを 1 行追加するだけ (ETC)。
Validator = Callable[[], list[str]]
TARGETS: dict[str, Validator] = {
    "sources": lambda: validate_sources(Path("sources.yaml")),
    "data": lambda: validate_data(Path("docs/data")),
    "summaries": lambda: validate_summaries(Path("summaries")),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        choices=[*TARGETS, "all"],
        help="検証対象 (all で全て)",
    )
    args = parser.parse_args()

    selected = list(TARGETS) if args.target == "all" else [args.target]

    # フェイルファスト的に途中で止めず、全ターゲットを実行して結果を集約する。
    # CI で「修正したら次の問題が出る」を一度のランで全部見せるための判断 (ETC)。
    all_errors: list[str] = []
    for name in selected:
        errors = TARGETS[name]()
        if errors:
            all_errors.extend(errors)
            print(f"✗ {name} ({len(errors)} error{'s' if len(errors) != 1 else ''})")
        else:
            print(f"✓ {name}")

    if all_errors:
        print("", file=sys.stderr)
        for err in all_errors:
            print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
