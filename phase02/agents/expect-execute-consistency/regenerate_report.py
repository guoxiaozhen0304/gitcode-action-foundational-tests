#!/usr/bin/env python3
"""Regenerate consistency-report.md from per-case .md files.

Only uses 断言一致 / 部分不符 / 完全不符 — no BLOCKED/TRIGGER_BLOCKED.
"""

import re
from pathlib import Path
from collections import Counter

CASE_DIR = Path(__file__).resolve().parent / "outputs" / "case"
YAML_DIR = Path("/home/chenqi252/code/gitcode-ci/workspace-gitcode-action/gitcode-action-foundational-tests/phase01/runs/2026-07-23-01/cases/yaml")
REPORT_PATH = Path(__file__).resolve().parent / "outputs" / "consistency-report.md"

YAML_IDS = {p.stem for p in YAML_DIR.glob("*.yaml")}

DIM_CNS = {
    "completeness": "完备性",
    "compatibility": "兼容性",
    "reliability": "可靠性",
    "security": "安全性",
    "usability": "易用性",
}


RATING_MAP = {
    "断言一致": "断言一致",
    "部分不符": "部分不符",
    "完全不符": "完全不符",
    "存在空洞": "部分不符",
    "混合问题": "部分不符",
}


def parse_case(fp: Path) -> dict | None:
    text = fp.read_text()

    m = re.search(r"评级:\s*(.+)", text)
    if not m:
        return None
    rating_raw = m.group(1).strip()
    rating = RATING_MAP.get(rating_raw, rating_raw)

    title = ""
    m = re.search(r"标题:\s*(.+)", text)
    if m:
        title = m.group(1).strip()

    dim = ""
    m = re.search(r"维度:\s*(.+?)\s*\|", text)
    if m:
        dim = m.group(1).strip()
        dim = DIM_CNS.get(dim, dim)

    reason = ""
    m = re.search(r"## 4\. 规格 vs 实现对照\s*?\n\|(.*?)(?:\n\n###|\n---|\n\n\n)", text, re.DOTALL)
    if m:
        table = "|" + m.group(1)
        reasons = []
        for row in table.strip().split("\n"):
            parts = row.split("|")
            # Table format: | 验证点 | 覆盖? | 说明 |
            if len(parts) >= 4 and "---" not in parts[2]:
                vp = parts[1].strip()
                verdict = parts[2].strip()
                note = parts[3].strip() if len(parts) > 3 else ""
                if verdict and verdict != "覆盖?":
                    reasons.append(f"{vp}: {verdict} — {note}")
        reason = "; ".join(reasons[:3])
    if not reason:
        r = re.search(r"## 5\. 评级理由\s*\n(.*?)(?:\n\n|\n---)", text, re.DOTALL)
        if r:
            reason = r.group(1).strip()[:120].replace("\n", " ")

    return {
        "id": fp.stem,
        "title": title,
        "dim": dim,
        "rating": rating,
        "reason": reason,
    }


def main():
    consistent = []
    partial = []
    incompatible = []
    spec_missing = []

    for f in sorted(CASE_DIR.glob("*.md")):
        if f.stem not in YAML_IDS:
            continue
        info = parse_case(f)
        if not info:
            continue

        r = info["rating"]
        if r == "断言一致":
            consistent.append(info)
        elif r == "部分不符":
            partial.append(info)
        elif r == "完全不符":
            incompatible.append(info)
        elif r == "规格缺失":
            spec_missing.append(info)
        else:
            incompatible.append(info)  # treat unknown as incompatible

    analyzable = len(consistent) + len(partial) + len(incompatible)
    total = analyzable + len(spec_missing)

    lines = [
        "# 断言-步骤一致性报告",
        "",
        f"**用例总数**: {analyzable}",
        "",
        "---",
        "",
        "## 1. 总览",
        "",
        "| 评级 | 数量 | 说明 |",
        "|------|:---:|------|",
        f"| 断言一致 | {len(consistent)} | 所有验证点可被步骤真实覆盖 |",
        f"| 部分不符 | {len(partial)} | 部分验证点为 TRIVIAL / MISSING / UNVERIFIABLE |",
        f"| 完全不符 | {len(incompatible)} | 全部验证点未能由步骤产出 |",
        "| 合计 | **" + str(analyzable) + "** | |",
        "",
    ]

    # Dimension table
    dims = {}
    for cases, rating in [(consistent, "断言一致"), (partial, "部分不符"), (incompatible, "完全不符")]:
        for c in cases:
            dims.setdefault(c["dim"], {"断言一致": 0, "部分不符": 0, "完全不符": 0, "合计": 0})
            dims[c["dim"]][rating] += 1
            dims[c["dim"]]["合计"] += 1

    if dims:
        lines.append("| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |")
        lines.append("|------|:---:|:---:|:---:|:---:|")
        for dim, counts in sorted(dims.items()):
            lines.append(f"| {dim} | {counts['断言一致']} | {counts['部分不符']} | {counts['完全不符']} | {counts['合计']} |")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Section: 断言一致
    lines.append(f"## 断言一致 — 所有验证点真实覆盖（{len(consistent)} 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 | 原因 |")
    lines.append("|---|---------|------|------|")
    for i, c in enumerate(consistent, 1):
        lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:42]} | {c['reason'][:70]} |")
    lines.append("")

    # Section: 部分不符
    lines.append(f"## 部分不符 — 验证点与步骤产出部分不一致（{len(partial)} 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 | 原因 |")
    lines.append("|---|---------|------|------|")
    for i, c in enumerate(partial, 1):
        lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:38]} | {c['reason'][:75]} |")
    lines.append("")

    # Section: 完全不符
    lines.append(f"## 完全不符 — 全部验证点未能由步骤产出（{len(incompatible)} 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 | 原因 |")
    lines.append("|---|---------|------|------|")
    for i, c in enumerate(incompatible, 1):
        lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:38]} | {c['reason'][:75]} |")
    lines.append("")

    # Spec missing
    if spec_missing:
        lines.append(f"## 规格缺失 — 无 Phase 01 文本用例（{len(spec_missing)} 例）")
        lines.append("")
        lines.append("以下用例缺少对应 Phase 01 文本规格，无法进行规格-实现对照分析：")
        lines.append("")
        lines.append("| # | Case ID | 标题 |")
        lines.append("|---|---------|------|")
        for i, c in enumerate(spec_missing, 1):
            lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:55]} |")
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines))
    print(f"Report written: {REPORT_PATH}")
    print(f"  断言一致: {len(consistent)} | 部分不符: {len(partial)} | 完全不符: {len(incompatible)} | 规格缺失: {len(spec_missing)}")


if __name__ == "__main__":
    main()
