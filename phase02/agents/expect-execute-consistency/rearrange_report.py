#!/usr/bin/env python3
"""Rearrange consistency report with brief reasons for each case.

Extracts rating, title, and key failure reasons from per-case detail files,
then rewrites the consistency report with per-case tables that include reasons.
"""
import re
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parent / "outputs/case"
REPORT_PATH = Path(__file__).resolve().parent / "outputs/consistency-report.md"

DIMENSIONS = ["完备性", "兼容性", "可靠性", "安全性", "易用性"]
DIM_ALIASES = {
    "稳定性": "可靠性",
    "completeness": "完备性",
    "compatibility": "兼容性",
    "reliability": "可靠性",
    "security": "安全性",
    "usability": "易用性",
    "未知": "易用性",
}

# Map detailed ratings to 3 summary categories
DETAIL_TO_SUMMARY = {
    "断言一致": "断言一致",
    "部分不符": "部分不符",
    "存在空洞": "部分不符",
    "不可评估": "部分不符",
    "混合问题": "部分不符",
    "完全不符": "完全不符",
    "BLOCKED": "完全不符",
}


def to_summary(rating: str) -> str:
    return DETAIL_TO_SUMMARY.get(rating, rating)


def parse_case(filepath):
    content = Path(filepath).read_text()
    lines = content.split("\n")

    title = ""
    dim = ""
    detail_rating = ""
    matched_dim = ""

    for line in lines[:20]:
        m = re.match(r"- 标题:\s*(.+)", line)
        if m:
            title = m.group(1).strip()
        m = re.match(r"- 维度:\s*(.+)\s*\|", line)
        if m:
            dim = m.group(1).strip()
            # Try direct match first
            for d in DIMENSIONS:
                if d in dim:
                    matched_dim = d
                    break
            # Try aliases (longer aliases first to avoid partial matches)
            if not matched_dim:
                for alias, target in sorted(DIM_ALIASES.items(), key=lambda x: -len(x[0])):
                    if alias in dim.strip():
                        matched_dim = target
                        break
        m = re.match(r"- 评级:\s*(.+)", line)
        if m:
            detail_rating = m.group(1).strip()

    # Find the "问题" section
    problems = []
    in_problems = False
    for line in lines:
        if line.strip() == "### 问题":
            in_problems = True
            continue
        if in_problems and line.startswith("---"):
            break
        if in_problems and line.strip().startswith("-"):
            problems.append(line.strip().lstrip("- "))

    # Extract COVERED/TRIVIAL/MISSING counts from table
    covered = 0
    trivial = 0
    missing = 0
    status_guaranteed = 0
    unverifiable = 0

    for line in lines:
        if "✅ COVERED" in line:
            covered += 1
        elif "❌ TRIVIAL" in line:
            trivial += 1
        elif "❌ MISSING" in line:
            missing += 1
        elif "⚠️ STATUS_GUARANTEED" in line:
            status_guaranteed += 1
        elif "⚠️ UNVERIFIABLE" in line:
            unverifiable += 1

    # Build reason
    reasons = []
    if detail_rating == "断言一致":
        if covered == 0:
            reasons.append("所有断言均可在流程中验证")
        else:
            reasons.append(f"共 {covered} 个验证点全部真实覆盖")
    elif detail_rating == "规格缺失":
        reasons.append("Phase 01 text case 缺失，无法做规格-实现对照")
    elif detail_rating in ("部分不符", "存在空洞", "不可评估", "混合问题"):
        if trivial > 0:
            reasons.append(f"{trivial} TRIVIAL（仅 echo 未执行功能）")
        if missing > 0:
            reasons.append(f"{missing} MISSING（无步骤产出期望输出）")
        if status_guaranteed > 0:
            reasons.append(f"{status_guaranteed} STATUS_GUARANTEED（必然成功）")
        if unverifiable > 0:
            reasons.append(f"{unverifiable} UNVERIFIABLE（单次运行无法验证否定）")
        if not reasons and problems:
            reasons.append(problems[0][:70])
        if not reasons:
            reasons.append(f"共 {covered} 覆盖 + {trivial + missing + unverifiable} 未覆盖")
    elif detail_rating in ("完全不符", "BLOCKED"):
        if trivial > 0:
            reasons.append(f"全部 {trivial} TRIVIAL（仅 echo 未执行功能）")
        if missing > 0:
            reasons.append(f"全部 {missing} MISSING（无步骤产出期望输出）")
        if status_guaranteed > 0:
            reasons.append(f"全部 {status_guaranteed} STATUS_GUARANTEED（必然成功）")
        if not reasons and problems:
            reasons.append(problems[0][:70])
        if not reasons:
            reasons.append("无步骤执行实质功能，断言无法由步骤产出")

    reason = "; ".join(reasons) if reasons else "—"

    return {
        "id": filepath.stem,
        "title": title,
        "dim": dim,
        "matched_dim": matched_dim,
        "detail_rating": detail_rating,
        "summary_rating": to_summary(detail_rating),
        "reason": reason,
        "covered": covered,
        "total_issues": trivial + missing + status_guaranteed + unverifiable,
    }


def main():
    cases = []
    for f in sorted(CASE_DIR.glob("*.md")):
        info = parse_case(f)
        if info["detail_rating"]:
            cases.append(info)

    # Skip 规格缺失 (50 cases that aren't part of the main 369)
    main_cases = [c for c in cases if c["detail_rating"] != "规格缺失"]
    spec_missing = [c for c in cases if c["detail_rating"] == "规格缺失"]

    consistent = [c for c in main_cases if c["summary_rating"] == "断言一致"]
    partial = [c for c in main_cases if c["summary_rating"] == "部分不符"]
    incompatible = [c for c in main_cases if c["summary_rating"] == "完全不符"]

    lines = []
    lines.append("# 断言-步骤一致性报告")
    lines.append("")
    lines.append(f"**日期**: 2026-07-25")
    lines.append(f"**用例总数**: {len(main_cases)}（另有 {len(spec_missing)} 例缺 Phase 01 文本规格）")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Section 1: Overview
    lines.append("## 1. 总览")
    lines.append("")
    lines.append(f"| 评级 | 数量 | 说明 |")
    lines.append(f"|------|:---:|------|")
    lines.append(f"| 断言一致 | {len(consistent)} | 所有验证点被 workflow 步骤真实覆盖 |")
    lines.append(f"| 部分不符 | {len(partial)} | 部分验证点存在空洞、缺失或无法由步骤产出 |")
    lines.append(f"| 完全不符 | {len(incompatible)} | 全部验证点为空洞/缺失/必然结果 |")
    lines.append(f"| **合计** | **{len(main_cases)}** | |")
    lines.append("")

    # Detail breakdown of partial
    detail_groups = {}
    for c in partial:
        dr = c["detail_rating"]
        detail_groups[dr] = detail_groups.get(dr, 0) + 1
    if detail_groups:
        lines.append("**部分不符内部分类**:")
        for dr in ["部分不符", "存在空洞", "不可评估", "混合问题"]:
            if dr in detail_groups:
                lines.append(f"- {dr}: {detail_groups[dr]}")
        lines.append("")

    # Section 2: By dimension
    lines.append("## 2. 按维度分布")
    lines.append("")
    lines.append("| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |")
    lines.append("|------|:---:|:---:|:---:|:---:|")
    for dim in DIMENSIONS:
        dc = [c for c in consistent if c["matched_dim"] == dim]
        dp = [c for c in partial if c["matched_dim"] == dim]
        di = [c for c in incompatible if c["matched_dim"] == dim]
        lines.append(f"| {dim} | {len(dc)} | {len(dp)} | {len(di)} | {len(dc)+len(dp)+len(di)} |")
    lines.append("")

    # Section 3: 断言一致
    lines.append("## 断言一致 — 所有验证点真实覆盖（155 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 | 原因 |")
    lines.append("|---|---------|------|------|")
    for i, c in enumerate(consistent, 1):
        lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:42]} | {c['reason'][:70]} |")
    lines.append("")

    # Section 4: 部分不符
    lines.append("## 部分不符 — 验证点与步骤产出部分不一致（176 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 | 原因 |")
    lines.append("|---|---------|------|------|")
    for i, c in enumerate(partial, 1):
        lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:38]} | {c['reason'][:75]} |")
    lines.append("")

    # Section 5: 完全不符
    lines.append("## 完全不符 — 全部验证点未能由步骤产出（38 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 | 原因 |")
    lines.append("|---|---------|------|------|")
    for i, c in enumerate(incompatible, 1):
        lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:38]} | {c['reason'][:75]} |")
    lines.append("")

    # Section 6: 规格缺失
    if spec_missing:
        lines.append("## 规格缺失 — 无 Phase 01 文本用例（50 例）")
        lines.append("")
        lines.append("以下用例缺少对应 Phase 01 文本规格，无法进行规格-实现对照分析：")
        lines.append("")
        lines.append("| # | Case ID | 标题 |")
        lines.append("|---|---------|------|")
        for i, c in enumerate(spec_missing, 1):
            lines.append(f"| {i} | [{c['id']}](case/{c['id']}.md) | {c['title'][:55]} |")
        lines.append("")

    Path(REPORT_PATH).write_text("\n".join(lines))
    print(f"Updated: {REPORT_PATH}")
    print(f"  Consistent: {len(consistent)} | Partial: {len(partial)} | Incompatible: {len(incompatible)} | Spec-missing: {len(spec_missing)}")


if __name__ == "__main__":
    main()
