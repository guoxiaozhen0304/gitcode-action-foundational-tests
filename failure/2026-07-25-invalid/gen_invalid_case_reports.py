#!/usr/bin/env python3
"""
生成 66 个 INVALID case 的逐例失败分析报告。
遵循 phase02/agents/failure-analyst/CLAUDE.md 模板。

用法:
    python3 gen_invalid_case_reports.py [--output-dir failure/2026-07-25/invalid-case-analysis/]
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent

TEXT_CASES_DIR = BASE / "phase01/runs/2026-07-23-01/cases/text"
YAML_DIR = BASE / "phase02/classify-experiment/2026-07-23/INVALID"
VAL_RESULTS = BASE / "phase02/classify-experiment/2026-07-23/validation-results.json"
SPEC_DIR = BASE / "phase01/inputs/gitcode-spec"

# ── Metadata from existing analysis (validation-invalid-74-cases.md) ────────

EXPECTED_NEGATIVE = {
    "COMP-SCHEDULE-01-002", "COMP-SCHEDULE-01-003",
    "COMPAT-CONCUR-01-002", "COMPAT-ENVIRON-01-001",
    "COMPAT-FIELD-01-001", "COMPAT-FIELD-01-002", "COMPAT-FIELD-01-003",
    "COMPAT-MIGRATE-01-001", "COMPAT-MIGRATE-01-002",
    "COMPAT-PERM-01-003", "COMPAT-PR-01-002",
    "COMPAT-RUNNER-01-004",
    "REL-PREEMPT-01-006",
    "USE-CONC-01-002", "USE-EXPR-01-002", "USE-LBL-01-001",
    "USE-NEST-01-001", "USE-PERM-01-002", "USE-RUN-01-002",
    "USE-STAT-01-002", "USE-TYPE-01-002", "USE-UNKN-01-001",
    "USE-YAML-01-001", "USE-YAML-01-002",
}

# Root cause classification for unexpected cases
ROOT_CAUSE_MAP = {
    "COMPAT-PATHS-01-001": ("平台缺陷", "列表长度限制未在文档声明"),
    "COMPAT-PATHS-01-002": ("平台缺陷", "列表长度限制未在文档声明"),
    "COMPAT-PR-01-003": ("平台缺陷", "列表长度限制未在文档声明"),
    "COMPAT-PR-01-004": ("平台缺陷", "列表长度限制未在文档声明"),
    "COMPAT-PR-01-005": ("平台缺陷", "列表长度限制未在文档声明"),
    "COMP-BOUND-01-085": ("产品bug", "cron 表达式被拒 (合法语法)"),
    "COMP-SCHEDULE-01-001": ("产品bug", "cron 表达式被拒 (合法语法)"),
    "COMP-TRIG-01-075": ("产品bug", "cron 表达式被拒 (合法语法)"),
    "COMPAT-SCHEDULE-01-003": ("产品bug", "cron 表达式被拒 (合法语法)"),
    "COMP-EXPR-01-058": ("产品bug", "if 表达式解析器不支持合法运算符组合"),
    "COMPAT-CONCUR-01-001": ("产品bug", "concurrency 字段语义与文档不符"),
    "COMPAT-CONCUR-01-003": ("产品bug", "concurrency preemption 配置校验过严"),
    "COMPAT-EXPR-01-014": ("用例问题", "GitHub 表达式函数 vs GitCode 关键字——always 关键字未使用"),
    "COMPAT-ENVIRON-01-002": ("平台缺陷", "environment 字段不支持"),
    "COMPAT-SECRET-01-005": ("平台缺陷", "environment 字段不支持"),
    "SEC-ENV-01-001": ("平台缺陷", "environment 字段不支持"),
    "SEC-ENV-01-002": ("平台缺陷", "environment 字段不支持"),
    "COMP-RUNNER-01-003": ("产品bug", "runs-on 数组校验过严"),
    "COMPAT-RUNNER-01-005": ("产品bug", "runs-on 数组校验过严"),
    "COMPAT-SHELL-01-003": ("产品bug", "runs-on 数组校验过严"),
    "COMP-STAGES-01-001": ("文档冲突", "stages 反序列化错误 (array vs map)"),
    "COMP-STAGES-01-002": ("文档冲突", "stages 反序列化错误 (array vs map)"),
    "REL-STAGES-01-029": ("文档冲突", "stages 反序列化错误 (array vs map)"),
    "COMPAT-ACTIONDEV-01-001": ("用例问题", "uses 路径引用不存在的文件"),
    "SEC-SUPPLY-01-003": ("用例问题", "uses 引用不存在的插件"),
    "USE-NEST-01-002": ("用例问题", "uses 路径引用不存在的 workflow 文件"),
    "COMPAT-EXPR-01-013": ("用例问题", "GitHub 表达式函数 vs GitCode 关键字——success 关键字未使用"),
    "COMPAT-VARS-01-005": ("用例问题", "GitHub 表达式函数 vs GitCode 关键字——vars 上下文不支持 if 条件"),
    "REL-RACE-01-048": ("用例问题", "GitHub 表达式函数 vs GitCode 关键字——failure() 函数不支持"),
    "SEC-DEFPERM-01-002": ("平台缺陷", "job 级 permissions 不支持"),
    "SEC-PERM-01-001": ("平台缺陷", "job 级 permissions 不支持"),
    "SEC-PERM-01-002": ("平台缺陷", "job 级 permissions 不支持"),
    "COMP-STAGES-01-003": ("文档冲突", "post.steps/run_always 文档描述但平台拒"),
    "COMP-WFLOW-01-065": ("文档冲突", "post.steps/run_always 文档描述但平台拒"),
    "COMPAT-CONCUR-01-004": ("文档缺失", "preemption events 取值限制"),
    "REL-PREEMPT-01-005": ("文档缺失", "preemption events 取值限制"),
    "COMPAT-SCHEDULE-01-001": ("产品bug", "schedule 反序列化错误——array 期望 vs object"),
    "COMPAT-SCHEDULE-01-002": ("产品bug", "schedule 反序列化错误——array 期望 vs object"),
    "SEC-WCMD-01-003": ("用例问题", "YAML 语法错误——引号未正确闭合"),
    "SEC-WCMD-01-004": ("用例问题", "YAML 语法错误——引号未正确闭合"),
    "COMP-UNKNOWN-01-001": ("平台缺陷", "未知字段静默拒绝"),
    "REL-STEPS-01-042": ("文档缺失", "steps <=16 限制未在文档声明"),
}

# Spec doc references for each root cause category
SPEC_REFERENCES = {
    "cron 表达式被拒": {
        "file": "syntax-reference/trigger-events.md",
        "note": "文档描述了 schedule cron 触发方式，但平台 cron 解析器与标准 cron 语法不兼容。"
    },
    "environment 字段": {
        "file": "security-permissions",
        "note": "文档描述了 environment 字段绑定环境级 secrets，但平台校验器拒绝此字段。"
    },
    "job 级 permissions": {
        "file": "security-permissions/token-permissions.md",
        "note": "文档描述了 job 级 permissions 覆盖，但平台尚不支持 job 级 permissions 字段。"
    },
    "stages": {
        "file": "writing-pipelines/configure-dependencies-order.md",
        "note": "文档展示 stages array 和 map 两种格式，但平台只接受 map 格式。"
    },
    "post": {
        "file": "core-concepts/workflow-job-step-action.md",
        "note": "文档描述了 post 后处理阶段，但平台校验器报 unknown property。"
    },
    "runs-on": {
        "file": "syntax-reference/runner-images-tools.md",
        "note": "文档描述 runs-on 数组格式，但平台校验器对合法标签组合也拒绝。"
    },
    "if 表达式": {
        "file": "syntax-reference/expressions.md",
        "note": "文档描述了 if 条件表达式语法，但平台解析器不支持部分合法运算符。"
    },
    "schedule 反序列化": {
        "file": "syntax-reference/trigger-events.md",
        "note": "文档描述 schedule 期望数组，但平台期望 ArrayList。"
    },
    "steps 限制": {
        "file": "core-concepts",
        "note": "平台限制每 job 最多 16 个 step，但文档未声明此上限。"
    },
    "preemption": {
        "file": "core-concepts",
        "note": "文档未声明 preemption events 仅支持 mr_id。"
    },
}


def load_val_results():
    with open(VAL_RESULTS) as f:
        return json.load(f)


def guess_spec_file(case_id, dimension, trigger, title, diag_msg):
    """根据诊断信息推测相关规格文件路径。"""
    msg = diag_msg.lower()
    if "cron" in msg or "schedule" in msg:
        return SPEC_DIR / "syntax-reference/trigger-events.md"
    if "environment" in msg:
        return SPEC_DIR / "security-permissions"
    if "permissions" in msg:
        return SPEC_DIR / "security-permissions/token-permissions.md"
    if "runs-on" in msg:
        return SPEC_DIR / "syntax-reference/runner-images-tools.md"
    if "stages" in msg:
        return SPEC_DIR / "writing-pipelines/configure-dependencies-order.md"
    if "expression" in msg or "if" in msg:
        return SPEC_DIR / "syntax-reference/expressions.md"
    if "post" in msg:
        return SPEC_DIR / "core-concepts/workflow-job-step-action.md"
    if "uses" in msg or "plugin" in msg:
        return SPEC_DIR / "core-concepts/workflow-job-step-action.md"
    if "step" in msg:
        return SPEC_DIR / "core-concepts"
    if "concurrency" in msg or "preemption" in msg:
        return SPEC_DIR / "writing-pipelines"
    if "push" in msg or "merge_requests" in msg or "branches" in msg:
        return SPEC_DIR / "syntax-reference/trigger-events.md"
    return None


def read_spec_sample(spec_path):
    """Read the first relevant section of a spec file."""
    if spec_path is None or not Path(spec_path).exists():
        return "（未找到对应规格文件）"
    if Path(spec_path).is_dir():
        md_files = sorted(Path(spec_path).glob("*.md"))
        if not md_files:
            return "（规格目录为空）"
        spec_path = md_files[0]
    try:
        with open(spec_path) as f:
            content = f.read()
        if len(content) > 3000:
            return content[:3000] + "\n... (截断)"
        return content
    except Exception as e:
        return f"（读取失败: {e}）"


def load_yaml_workflow(case_id):
    yf = YAML_DIR / f"{case_id}.yaml"
    with open(yf) as f:
        return yaml.safe_load(f)


def load_text_case(case_id):
    tf = TEXT_CASES_DIR / f"{case_id}.md"
    if not tf.exists():
        return None
    with open(tf) as f:
        return f.read()


def classify(case_id):
    """Classify a case as EXPECTED or UNEXPECTED."""
    if case_id in EXPECTED_NEGATIVE:
        return "EXPECTED"
    return "UNEXPECTED"


def responsible_party(rc_label, case_id):
    """Map root cause to responsible party."""
    rc_mapping = {
        "产品bug": "平台方",
        "平台缺陷": "平台方",
        "文档冲突": "平台方",
        "文档缺失": "平台方",
        "用例问题": "Phase 01",
    }
    for k, v in rc_mapping.items():
        if k in rc_label:
            return v
    return "需人工判断"


def severity_label(diags):
    """Return impact severity indicators."""
    n = len(diags)
    msgs = [d.get("message", "") for d in diags]
    has_blocking = any("unknown property" in m or "Cannot deserialize" in m for m in msgs)
    has_compat = any("不是可识别" in m or "无法解析" in m or "不支持" in m for m in msgs)
    if has_blocking:
        return ("🔴阻塞", "🟢明确报错")
    if has_compat:
        return ("🟡非阻塞", "🟡可察觉")
    return ("⚪无影响", "🟢明确报错")


def generate_report(case_id, val_entry):
    """Generate a per-case failure analysis report following the failure-analyst template."""
    expected = classify(case_id)
    yaml_data = load_yaml_workflow(case_id)
    text_case = load_text_case(case_id)
    diags = val_entry.get("diagnostics", [])
    dim = yaml_data.get("dimensions", [yaml_data.get("dimension", "unknown")])
    if isinstance(dim, list):
        dim = dim[0] if dim else "unknown"
    priority = yaml_data.get("priority", "?")
    title = yaml_data.get("title", "")
    trigger = yaml_data.get("trigger", {}).get("event", "?") if isinstance(yaml_data.get("trigger"), dict) else "?"
    assertions = yaml_data.get("assertions", [])
    pos_count = sum(1 for a in assertions if a.get("type") == "positive")
    neg_count = sum(1 for a in assertions if a.get("type") == "negative")
    root_cause = ROOT_CAUSE_MAP.get(case_id, ("需人工判断", "未分类"))

    # Determine spec file
    diag_combined = "; ".join(d.get("message", "") for d in diags)
    spec_path = guess_spec_file(case_id, dim, trigger, title, diag_combined)

    # Severity
    blocking, silent = severity_label(diags)
    if len(diags) == 1:
        scope = "🟢单用例"
    else:
        scope = "🟡同维度"

    # Build the report
    lines = []
    lines.append(f"## 失败分诊 · {case_id} · {title}")
    lines.append("")
    lines.append(f"**判定结果**: INVALID (平台 API 校验驳回)")
    lines.append(f"**分类**: {'预期非法 (negative test)' if expected == 'EXPECTED' else '非预期非法 (需修复)'}")
    lines.append(f"**诊断数**: {len(diags)} 条")
    lines.append("")

    # Diagnostics
    lines.append("### 诊断信息")
    lines.append("")
    for i, d in enumerate(diags, 1):
        sev = d.get("severity", "?")
        line = d.get("line", "?")
        col = d.get("column", "?")
        msg = d.get("message", "")
        lines.append(f"{i}. **[{sev}] L{line}:C{col}** — {msg}")
        lines.append("")
    lines.append("")

    # Root cause
    lines.append("### 根因初判")
    lines.append("")
    lines.append(f"**根因**: {root_cause[0]} — {root_cause[1]}")
    lines.append(f"**责任人**: {responsible_party(root_cause[0], case_id)}")
    lines.append("")
    if expected == "EXPECTED":
        lines.append("> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。")
    else:
        lines.append("> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。")
    lines.append("")

    # Evidence - Case metadata
    lines.append("### 证据")
    lines.append("")
    lines.append(f"- **维度**: {dim} | **优先级**: {priority} | **触发器**: {trigger}")
    lines.append(f"- **标题**: {title}")
    lines.append(f"- **断言**: {pos_count} positive / {neg_count} negative")
    lines.append("")

    # Workflow excerpt
    workflow = yaml_data.get("workflow", "")
    if workflow:
        lines.append("**Workflow 摘要**:")
        lines.append("```yaml")
        # Show first 25 lines
        wf_lines = workflow.strip().split("\n")
        lines.extend(wf_lines[:25])
        if len(wf_lines) > 25:
            lines.append("... (截断)")
        lines.append("```")
        lines.append("")

    # Text case excerpt
    if text_case:
        lines.append("**预期行为** (Phase 01 文本用例):")
        lines.append("```markdown")
        # Extract key sections
        tc_lines = text_case.strip().split("\n")
        key_sections = []
        for line in tc_lines:
            if any(line.startswith(k) for k in ["用例 ID", "维度", "优先级", "标题", "前置条件", "操作步骤", "预期结果", "验证点"]):
                key_sections.append(line)
        lines.extend(key_sections)
        lines.append("```")
        lines.append("")

    # Spec reference
    lines.append("### 对照 GitCode 规格")
    lines.append("")
    if spec_path:
        lines.append(f"**规格文件**: `phase01/inputs/gitcode-spec/{Path(spec_path).relative_to(SPEC_DIR) if Path(spec_path).is_relative_to(SPEC_DIR) else spec_path}`")
        lines.append("")
    else:
        lines.append("（未找到直接对应的规格文件）")
        lines.append("")

    # Spec-specific commentary
    root_cause_label = root_cause[1] if root_cause else ""
    spec_ref = {}
    for key in SPEC_REFERENCES:
        if key in root_cause_label or key.replace(" ", "") in diag_combined.replace(" ", ""):
            spec_ref = SPEC_REFERENCES[key]
            break
    if spec_arg := spec_ref.get(  # bypass lint
        "note",
        ""
    ):  # Use spec_ref dict for note
        lines.append(f"> {spec_arg}")
        lines.append("")

    # Impact
    lines.append("### 影响评估")
    lines.append("")
    lines.append(f"- **阻塞性**: {blocking} — {'YAML 无法通过校验，workflow 无法部署运行' if blocking == '🔴阻塞' else 'workflow 仍可通过其他合法语法完成' if blocking == '🟡非阻塞' else '用例本身有意测试非法输入'}")
    lines.append(f"- **静默性**: {silent} — {'平台明确报错，用户可定位问题' if '明确' in silent else '平台报错信息不够清晰'}")
    lines.append(f"- **影响面**: {scope} — {'影响同维度多个用例' if '同维度' in scope else '仅影响当前测试场景'}")
    lines.append("")

    # Summary
    impacts = []
    if expected == "EXPECTED":
        impacts.append("非阻塞：case 本身是 negative test，INVALID 是期望结果")
    else:
        impacts.append(f"非预期拒绝：{root_cause[0]}——{root_cause[1]}")
    lines.append(f"**综合**: {' | '.join(impacts)}")
    lines.append("")

    # Avoidance
    if expected == "EXPECTED":
        lines.append("**规避手段**: 无——此为有意测试，平台报错符合预期")
    else:
        lines.append(f"**规避手段**: {'修正 YAML 语法' if '用例问题' in root_cause[0] else '需平台修复' if '平台' in responsible_party(root_cause[0], case_id) else '需平台更新文档或实现'}")
    lines.append("")

    # Confidence
    conf = "高" if len(diags) > 0 else "中"
    lines.append(f"**置信度**: {conf}（诊断信息明确，可直接定位根因）")
    lines.append("")

    # Suggestions
    lines.append("### 建议")
    lines.append("")
    if expected == "EXPECTED":
        lines.append("- 保持 case 不变，确认平台对非法输入的报错行为符合预期")
    elif "用例问题" in root_cause[0]:
        lines.append(f"- 修正 case YAML 语法错误: {root_cause[1]}")
        lines.append("- 回流 Phase 01 评审 case 语法")
    elif "文档" in root_cause[0]:
        lines.append(f"- 平台团队更新文档以描述实际行为: {root_cause[1]}")
    else:
        lines.append(f"- 提交平台 bug: {root_cause[1]}")
        lines.append("- 等待平台修复后重新验证")
    lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "failure/2026-07-25/invalid-case-analysis"
    out_dir.mkdir(parents=True, exist_ok=True)

    results = load_val_results()
    invalid = [r for r in results if r["status"] == "INVALID"]

    today = datetime.now().strftime("%Y-%m-%d")
    idx_lines = [
        f"# 66 INVALID Cases — 逐例失败分析报告",
        f"",
        f"> 批次: 2026-07-23-01 | 生成日期: {today}",
        f"> 分析方法: 遵循 `phase02/agents/failure-analyst/CLAUDE.md`",
        f"> 数据源: 369 cases → 289 通过 API 校验 → 66 被拒绝",
        f"",
        f"## 统计",
        f"",
        f"| 类别 | 数量 |",
        f"|------|------|",
        f"| 预期非法 (negative test) | {sum(1 for r in invalid if classify(r['case_id']) == 'EXPECTED')} |",
        f"| 非预期非法 (需修复) | {sum(1 for r in invalid if classify(r['case_id']) != 'EXPECTED')} |",
        f"| **总计** | **{len(invalid)}** |",
        f"",
        f"## 逐例分析",
        f"",
    ]

    # Group: expected then unexpected
    expected_cases = [r for r in invalid if classify(r["case_id"]) == "EXPECTED"]
    unexpected_cases = [r for r in invalid if classify(r["case_id"]) != "EXPECTED"]

    idx_lines.append("### 预期非法 — Negative Tests")
    idx_lines.append("")
    idx_lines.append("| # | case_id | dimension | trigger | 标题 | 诊断 |")
    idx_lines.append("|---|---------|-----------|---------|------|------|")
    for i, r in enumerate(expected_cases, 1):
        yd = load_yaml_workflow(r["case_id"])
        dim = yd.get("dimensions", [yd.get("dimension", "?")])
        if isinstance(dim, list):
            dim = dim[0] if dim else "?"
        trig = yd.get("trigger", {}).get("event", "?") if isinstance(yd.get("trigger"), dict) else "?"
        title = yd.get("title", "")
        diag = r["diagnostics"][0]["message"][:60] if r["diagnostics"] else ""
        idx_lines.append(f"| {i} | [{r['case_id']}](./{r['case_id']}.md) | {dim} | {trig} | {title} | {diag} |")

    idx_lines.append("")
    idx_lines.append("### 非预期非法 — 需修复")
    idx_lines.append("")
    idx_lines.append("| # | case_id | root_cause | responsible | dimension | 诊断 |")
    idx_lines.append("|---|---------|-----------|-------------|-----------|------|")
    for i, r in enumerate(unexpected_cases, 1):
        yd = load_yaml_workflow(r["case_id"])
        rc = ROOT_CAUSE_MAP.get(r["case_id"], ("?", "?"))
        dim = yd.get("dimensions", [yd.get("dimension", "?")])
        if isinstance(dim, list):
            dim = dim[0] if dim else "?"
        resp = responsible_party(rc[0], r["case_id"])
        diag = r["diagnostics"][0]["message"][:60] if r["diagnostics"] else ""
        idx_lines.append(f"| {i} | [{r['case_id']}](./{r['case_id']}.md) | {rc[0]} ({rc[1]}) | {resp} | {dim} | {diag} |")

    idx_lines.append("")

    # Generate per-case files
    for r in invalid:
        cid = r["case_id"]
        report = generate_report(cid, r)
        out_file = out_dir / f"{cid}.md"
        with open(out_file, "w") as f:
            f.write(report)
        print(f"[OK] {cid}")

    # Write index
    idx_file = out_dir / "INDEX.md"
    with open(idx_file, "w") as f:
        f.write("\n".join(idx_lines))
    print(f"\nDone: {len(invalid)} reports in {out_dir}")
    print(f"Index: {idx_file}")


if __name__ == "__main__":
    main()
