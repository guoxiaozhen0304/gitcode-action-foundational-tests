#!/usr/bin/env python3
"""Assertion-Step Consistency Analyzer — Phase 02.

Reads text specs + YAML workflows, analyzes whether workflow steps
genuinely produce the outputs that assertions expect, and generates:
  - Per-case analysis files (outputs/case/<ID>.md)
  - Summary report (outputs/consistency-report.md)
  - accessable/ with 断言一致 YAMLs
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
TEXT_DIR = Path("/home/chenqi252/code/gitcode-ci/workspace-gitcode-action/gitcode-action-foundational-tests/phase01/runs/2026-07-27-01/cases/text")
YAML_DIR = Path("/home/chenqi252/code/gitcode-ci/workspace-gitcode-action/gitcode-action-foundational-tests/phase01/runs/2026-07-27-01/cases/yaml")
CASE_OUT = ROOT / "outputs" / "case"
ACCESS_OUT = ROOT / "outputs" / "accessable"
REPORT_OUT = ROOT / "outputs" / "consistency-report.md"

CASE_OUT.mkdir(parents=True, exist_ok=True)
ACCESS_OUT.mkdir(parents=True, exist_ok=True)

# ── Real commands that indicate GENUINE steps ──────────────────────
REAL_COMMANDS = [
    r'\bcurl\b', r'\bpip\b', r'\bnpm\b', r'\bpython\b', r'\bpy\b',
    r'\bmake\b', r'\bgrep\b', r'\bdiff\b', r'\bcat\b', r'\bdocker\b',
    r'\bgit\b', r'\bwget\b', r'\bunzip\b', r'\btar\b', r'\bsystemctl\b',
    r'\bservice\b', r'\bnode\b', r'\bapt-get\b', r'\byum\b', r'\bgo\b',
    r'\brustc\b', r'\bcargo\b', r'\bgcc\b', r'\bg\+\+', r'\bcmake\b',
    r'\bperl\b', r'\bruby\b', r'\bbash\b', r'\bsh\b', r'\bsudo\b',
    r'\bchmod\b', r'\bchown\b', r'\bmkdir\b', r'\bcp\b', r'\bmv\b',
    r'\brm\b', r'\bkill\b', r'\bpkill\b', r'\btrue\b', r'\bfalse\b',
    r'\bexit\b', r'\breturn\b', r'\bsource\b', r'\btest\b',
    r'\b\[\[', r'\b\$\(', r'\b`', r'\b\bexport\b', r'\bif\b', r'\bfi\b',
    r'\bfor\b', r'\bwhile\b', r'\bcase\b', r'\bawk\b', r'\bsed\b',
    r'\bsort\b', r'\buniq\b', r'\bwc\b', r'\bxargs\b', r'\bssh\b',
    r'\bscp\b', r'\brsync\b', r'\benv\b', r'\bwhich\b',
]

# Patterns for "this step has real behavior"
EXPR_PAT = re.compile(r'\$\{\{.*?\}\}')
VAR_PAT = re.compile(r'\$[A-Za-z_][A-Za-z0-9_]*')  # $VARIABLE
ECHO_ONLY_PAT = re.compile(r'^\s*(echo|printf|print)\s+', re.MULTILINE)

# Dimension mapping
DIM_CN = {
    "completeness": "完备性",
    "compatibility": "兼容性",
    "reliability": "可靠性",
    "security": "安全性",
    "usability": "易用性",
}


def parse_text_spec(path: Path) -> dict:
    """Parse text .md spec file."""
    text = path.read_text()
    
    info = {"id": path.stem}
    
    m = re.search(r'标题:\s*(.+)', text)
    info["title"] = m.group(1).strip() if m else ""
    
    m = re.search(r'维度:\s*(.+)', text)
    info["dim_raw"] = m.group(1).strip() if m else ""
    
    m = re.search(r'优先级:\s*(.+)', text)
    info["priority"] = m.group(1).strip() if m else ""
    
    m = re.search(r'溯源意图:\s*(.+)', text)
    info["intent_ref"] = m.group(1).strip() if m else ""
    
    # Extract 验证点
    verification_points = []
    vp_section = re.search(r'验证点:\s*\n((?:\s+-.+\n?)+)', text)
    if vp_section:
        for line in vp_section.group(1).strip().split("\n"):
            line = line.strip().lstrip("- ")
            tag = ""
            desc = line
            if line.startswith("[正向]"):
                tag = "positive"
                desc = line[4:].strip()
            elif line.startswith("[负向]"):
                tag = "negative"
                desc = line[4:].strip()
            elif line.startswith("[非功能]"):
                tag = "nonfunctional"
                desc = line[4:].strip()
            elif line.startswith("[正向/记录]"):
                tag = "positive_record"
                desc = line[7:].strip()
            else:
                tag = "unknown"
            verification_points.append({"tag": tag, "desc": desc})
    info["verification_points"] = verification_points
    
    # Extract 触发事件 from text
    m = re.search(r'触发事件:\s*(.+)', text)
    info["trigger_text"] = m.group(1).strip() if m else ""
    
    return info


def parse_case_yaml(path: Path) -> dict:
    """Parse case YAML file."""
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError:
        data = {}
    
    if not data:
        return {}
    
    dim = data.get("dimension", "")
    dim_cn = DIM_CN.get(dim, dim)
    
    trigger = data.get("trigger", {})
    
    # Extract workflow steps
    steps = []
    workflow_str = data.get("workflow", "")
    has_yaml_error = False
    
    if workflow_str:
        try:
            wf = yaml.safe_load(workflow_str)
        except yaml.YAMLError:
            wf = None
            has_yaml_error = True
        
        if wf and isinstance(wf, dict):
            jobs = wf.get("jobs", {})
            if isinstance(jobs, dict):
                for job_name, job in jobs.items():
                    if isinstance(job, dict):
                        for step in job.get("steps", []):
                            if not isinstance(step, dict):
                                continue
                            step_info = {
                                "name": step.get("name", step.get("id", "")),
                                "run": step.get("run", ""),
                                "uses": step.get("uses", ""),
                                "if_expr": step.get("if", ""),
                                "env": step.get("env", {}),
                                "with": step.get("with", {}),
                                "continue_on_error": step.get("continue-on-error", False),
                            }
                            steps.append(step_info)
    
    assertions_raw = data.get("assertions", [])
    assertions = []
    for a in assertions_raw:
        if not isinstance(a, dict):
            continue
        assertions.append({
            "type": a.get("type", ""),
            "target": a.get("target", ""),
            "equals": a.get("equals", ""),
            "must_contain": a.get("must_contain", ""),
            "contains": a.get("contains", ""),
            "must_not_contain_secret": a.get("must_not_contain_secret", ""),
            "eval": a.get("eval", ""),
            "rubric": a.get("rubric", ""),
        })
    
    setup = data.get("setup", {})
    
    return {
        "id": data.get("id", path.stem),
        "dim": dim_cn,
        "dim_raw": dim,
        "priority": data.get("priority", ""),
        "title": data.get("title", ""),
        "intent_ref": data.get("intent_ref", ""),
        "trigger": trigger,
        "steps": steps,
        "assertions": assertions,
        "has_yaml_error": has_yaml_error,
        "workflow_raw": workflow_str,
        "setup": setup,
        "fault_injection": data.get("fault_injection"),
    }


def is_echo_only(command: str) -> bool:
    """Check if a command is purely echo/printf/print with no dynamic content."""
    lines = [l.strip() for l in command.strip().split("\n") if l.strip() and not l.strip().startswith("#")]
    
    has_real_cmd = False
    has_expr = bool(EXPR_PAT.search(command))
    has_var = bool(re.search(r'(?<!\$)\$[A-Za-z_]', command))  # $VAR (not $$)
    
    for line in lines:
        for cmd in REAL_COMMANDS:
            if re.search(cmd, line):
                has_real_cmd = True
                break
        if has_real_cmd:
            break
    
    # Even if just echo, ${{ }} makes it GENUINE
    if has_expr:
        return False
    
    # echo $VARIABLE is GENUINE (using env context)
    # But we need to be more careful - echo "text $HOME" is genuine
    if has_var and has_real_cmd:
        return False
    
    if has_real_cmd:
        return False
    
    # Check if all lines are echo/printf/print
    for line in lines:
        if not re.match(r'^(echo|printf|print)\s', line):
            return False
    
    return True


def analyze_step(step: dict) -> str:
    """Analyze a step and return VACUOUS or GENUINE."""
    # Rule 6: uses: action → GENUINE
    if step.get("uses"):
        return "GENUINE"
    
    # if: condition → GENUINE
    if step.get("if_expr"):
        return "GENUINE"
    
    # continue-on-error → GENUINE (deliberate failure path)
    if step.get("continue_on_error"):
        return "GENUINE"
    
    run_cmd = step.get("run", "")
    if not run_cmd:
        return "GENUINE"  # no run = uses action, already caught above
    
    # Check for ${{ }} in run command
    if EXPR_PAT.search(run_cmd):
        return "GENUINE"
    
    if is_echo_only(run_cmd):
        return "VACUOUS"
    
    return "GENUINE"


def find_expected_string_in_steps(expect_str: str, steps: list[dict]) -> bool:
    """Check if any step produces the expected string."""
    for step in steps:
        run_cmd = step.get("run", "")
        if expect_str in run_cmd:
            return True
        if step.get("uses"):
            name = step.get("name", "")
            if expect_str in name:
                return True
    return False


def find_secret_usage(secret_name: str, steps: list[dict]) -> bool:
    """Check if any step references secrets.<name>."""
    pattern = re.compile(r'secrets\.' + re.escape(secret_name))
    for step in steps:
        run_cmd = step.get("run", "")
        if pattern.search(run_cmd):
            return True
    return False


def analyze_assertion(assertion: dict, steps: list[dict], has_yaml_error: bool, dim: str, trigger_event: str) -> dict:
    """Analyze a single assertion against steps. Returns verdict + explanation."""
    a_type = assertion.get("type", "")
    target = assertion.get("target", "")
    equals = assertion.get("equals", "")
    must_contain = assertion.get("must_contain", "")
    contains = assertion.get("contains", "")
    secret = assertion.get("must_not_contain_secret", "")
    eval_method = assertion.get("eval", "")
    rubric = assertion.get("rubric", "")
    
    # Rule 5: nonfunctional / LLM assisted → LLM_DEPENDENT
    if a_type == "nonfunctional" or eval_method == "llm_assisted":
        return {"verdict": "LLM_DEPENDENT", "reason": "非功能性/LLM 辅助断言，跳过步骤追溯分析"}
    
    # Rule 3: run_event must match trigger
    if target == "run_event":
        if equals == trigger_event:
            return {"verdict": "GENUINE", "reason": f"事件断言与 trigger.event={trigger_event} 一致"}
        else:
            return {"verdict": "INVALID", "reason": f"事件断言期望 {equals} 但 trigger.event={trigger_event}"}
    
    # Security: must_not_contain_secret (check BEFORE run_logs/run_status, since these can overlap)
    if secret:
        used = find_secret_usage(secret, steps)
        if used:
            return {"verdict": "GENUINE", "reason": f"步骤使用 {secret}，secret 脱敏断言有验证对象（故意暴露测试）"}
        else:
            return {"verdict": "UNEXERCISED", "reason": f"断言 secret 不泄露但无步骤使用 {secret}"}
    
    # Platform validation case
    if has_yaml_error and target == "run_status" and equals == "COMPLETED":
        return {"verdict": "COVERED", "reason": "平台验证型用例：YAML 含语法错误，batch_validate.py 可验证平台拒绝"}
    
    # run_status assertions
    if target == "run_status":
        all_trivial = all(analyze_step(s) == "VACUOUS" for s in steps) if steps else True
        
        if equals == "success":
            if all_trivial:
                return {"verdict": "STATUS_GUARANTEED", "reason": "所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功"}
            else:
                return {"verdict": "GENUINE", "reason": "存在真实可执行步骤，有行为观测价值"}
        elif equals in ("failure", "COMPLETED"):
            # Check for failure paths
            has_failure_path = False
            for s in steps:
                cmd = s.get("run", "")
                if "exit 1" in cmd or "exit 2" in cmd or "false" in cmd.split("\n"):
                    has_failure_path = True
                if s.get("continue_on_error"):
                    has_failure_path = True
            if has_failure_path or has_yaml_error:
                return {"verdict": "GENUINE", "reason": "存在故意失败步骤或 continue-on-error"}
            else:
                return {"verdict": "IMPOSSIBLE", "reason": "期望 !=success 但无步骤可能失败"}
        elif equals == "completed_or_blocked":
            return {"verdict": "GENUINE", "reason": "检查步骤是否能完成或被平台阻止 — 有实际观测价值"}
        else:
            return {"verdict": "GENUINE", "reason": f"状态断言 {equals} 可被步骤行为验证"}
    
    # run_logs assertions
    if target == "run_logs":
        expect_str = must_contain or contains
        if not expect_str or not isinstance(expect_str, str):
            return {"verdict": "GENUINE", "reason": "日志断言无特定字符串匹配要求"}
        
        # build expected string set (can be comma-separated or multi-value)
        expected_strings = [s.strip().strip('"') for s in re.split(r'[,;]', expect_str) if s.strip()]
        
        results = []
        for es in expected_strings:
            found_in_step = find_expected_string_in_steps(es, steps)
            if found_in_step:
                # Check if the step that produces it is VACUOUS or GENUINE
                producing_steps = []
                for s in steps:
                    if es in s.get("run", "") or es in s.get("name", ""):
                        producing_steps.append(s)
                
                all_vacuous = all(analyze_step(s) == "VACUOUS" for s in producing_steps) if producing_steps else True
                if all_vacuous:
                    results.append(f"{es}: VACUOUS (步骤仅 echo，未执行功能)")
                else:
                    results.append(f"{es}: GENUINE")
            else:
                # Check if `uses:` action internal output could produce it
                uses_produces = False
                for s in steps:
                    if s.get("uses") and (es in s.get("name", "") or es in s.get("with", {}).get("path", "")):
                        uses_produces = True
                        break
                    # Any uses: action could produce the expected string internally
                    if s.get("uses"):
                        uses_produces = True
                        break
                if uses_produces:
                    results.append(f"{es}: GENUINE (uses action 内部输出)")
                else:
                    results.append(f"{es}: MISSING_SOURCE (无步骤产出此字符串)")
        
        # Aggregate
        verdicts = []
        for r in results:
            if "GENUINE" in r:
                verdicts.append("GENUINE")
            elif "VACUOUS" in r:
                verdicts.append("VACUOUS")
            else:
                verdicts.append("MISSING_SOURCE")
        
        if not verdicts:
            return {"verdict": "GENUINE", "reason": "无明确匹配字符串"}
        
        # Worst verdict
        if "MISSING_SOURCE" in verdicts and "VACUOUS" not in verdicts and "GENUINE" not in verdicts:
            final = "MISSING_SOURCE"
        elif "MISSING_SOURCE" in verdicts or "VACUOUS" in verdicts:
            final = "MIXED" if "GENUINE" in verdicts else ("VACUOUS" if "VACUOUS" in verdicts else "MISSING_SOURCE")
        else:
            final = "GENUINE"
        
        reason = "; ".join(results[:3])
        return {"verdict": final, "reason": reason}
    
    # step_summary / error_stack assertions
    if target in ("step_summary", "error_stack"):
        return {"verdict": "GENUINE", "reason": f"步骤有 {target} 输出，断言可观测"}
    
    # Other targets: cache_step, stage_order, job_parallelism, env_naming, etc.
    if target in ("cache_step", "stage_order", "job_parallelism", "env_naming",
                  "job_status", "error_message"):
        return {"verdict": "GENUINE", "reason": f"平台级断言 {target} — 由 harness 在运行时观测"}
    
    # Default: if assertion has any condition that steps can satisfy
    if equals or must_contain or contains or secret:
        return {"verdict": "GENUINE", "reason": "断言有条件可被步骤验证"}
    
    return {"verdict": "GENUINE", "reason": "通用断言匹配"}


def rate_case(assertion_results: list[dict]) -> str:
    """Rate case based on assertion verdicts. Only 3 ratings per CLAUDE.md."""
    verdicts = [a["verdict"] for a in assertion_results]
    
    # LLM_DEPENDENT assertions are skipped (can't be statically analyzed)
    real_verdicts = [v for v in verdicts if v != "LLM_DEPENDENT"]
    
    if not real_verdicts:
        return "部分不符"  # all LLM_DEPENDENT — can't confirm coverage
    
    all_genuine = all(v in ("GENUINE", "COVERED") for v in real_verdicts)
    if all_genuine:
        return "断言一致"
    
    all_bad = all(v not in ("GENUINE", "COVERED") for v in real_verdicts)
    if all_bad:
        return "完全不符"
    
    return "部分不符"


def generate_case_report(info: dict, yaml_info: dict, assertion_results: list[dict], rating: str) -> str:
    """Generate per-case markdown."""
    lines = []
    
    cid = info["id"]
    title = info.get("title", yaml_info.get("title", ""))
    dim = yaml_info.get("dim", info.get("dim_raw", ""))
    priority = yaml_info.get("priority", info.get("priority", ""))
    intent_ref = yaml_info.get("intent_ref", info.get("intent_ref", ""))
    trigger = yaml_info.get("trigger", {})
    trigger_event = trigger.get("event", "?")
    steps = yaml_info.get("steps", [])
    workflow_raw = yaml_info.get("workflow_raw", "")
    has_yaml_error = yaml_info.get("has_yaml_error", False)
    
    # Header
    lines.append(f"# {cid}")
    lines.append("")
    lines.append(f"- **标题**: {title}")
    lines.append(f"- **维度**: {dim}")
    lines.append(f"- **优先级**: {priority}")
    lines.append(f"- **评级**: {rating}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # 1. 想测什么
    lines.append("## 1. 想测什么")
    lines.append("")
    lines.append(f"本用例验证：**{title}**")
    lines.append("")
    lines.append(f"- 触发事件: `{trigger_event}`")
    lines.append(f"- 规格引用: {intent_ref}")
    lines.append("")
    lines.append("通过标准：")
    for i, a in enumerate(yaml_info.get("assertions", []), 1):
        desc = f"type={a['type']}, target={a['target']}"
        if a.get("equals"):
            desc += f", equals={a['equals']}"
        if a.get("must_contain"):
            desc += f", must_contain=\"{a['must_contain']}\""
        if a.get("contains") and isinstance(a.get("contains"), str):
            desc += f", contains=\"{a['contains']}\""
        elif a.get("contains") is not None and not isinstance(a.get("contains"), str):
            desc += f", contains={a['contains']}"
        if a.get("must_not_contain_secret"):
            desc += f", must_not_contain_secret=\"{a['must_not_contain_secret']}\""
        if a.get("eval"):
            desc += f", eval={a['eval']}"
        lines.append(f"{i}. {desc}")
    lines.append("")
    
    # 2. 做了什么
    lines.append("## 2. 做了什么")
    lines.append("")
    lines.append("workflow 中每个步骤的实际行为：")
    lines.append("")
    lines.append("| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |")
    lines.append("|---|--------|-----------|------|------|")
    for i, s in enumerate(steps, 1):
        name = s.get("name", str(i))
        cmd = s.get("run", "") or s.get("uses", "")
        # Truncate for display
        cmd_short = cmd.strip().replace("\n", " ")[:80]
        if_cond = s.get("if_expr", "-")
        quality = analyze_step(s)
        q_icon = "✅" if quality == "GENUINE" else "❌"
        lines.append(f"| {i} | {name[:25]} | `{cmd_short}` | {if_cond[:25]} | {q_icon} {quality} |")
    lines.append("")
    
    if workflow_raw:
        lines.append("<details>")
        lines.append("<summary>完整 workflow YAML</summary>")
        lines.append("")
        lines.append("```yaml")
        lines.append(workflow_raw.strip())
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    
    # 3. 触发与运行环境
    lines.append("## 3. 触发与运行环境")
    lines.append("")
    lines.append(f"| 触发事件 | `{trigger_event}` |")
    as_identity = trigger.get("as", "maintainer")
    lines.append(f"| 触发身份 | `{as_identity}` |")
    
    setup = yaml_info.get("setup", {})
    repo = setup.get("repo_fixture", "default")
    secrets_list = setup.get("secrets", [])
    lines.append(f"| Repo 环境 | `{repo}` |")
    lines.append(f"| Secrets | `{secrets_list}` |")
    
    fault = yaml_info.get("fault_injection", None)
    if fault:
        lines.append(f"| 故障注入 | `{fault}` |")
    else:
        lines.append(f"| 故障注入 | 无 |")
    lines.append("")
    
    # 4. 能否达成目标
    lines.append("## 4. 能否达成目标")
    lines.append("")
    lines.append("逐条断言对比步骤实际输出：")
    lines.append("")
    lines.append("| # | 目标 | 类型 | 条件 | 判定 | 说明 |")
    lines.append("|---|------|------|------|------|------|")
    
    assertions = yaml_info.get("assertions", [])
    for i, (a, ar) in enumerate(zip(assertions, assertion_results), 1):
        target = a.get("target", "?")
        a_type = a.get("type", "?")
        condition = ""
        if a.get("equals"):
            condition = f"equals={a['equals']}"
        elif a.get("must_contain"):
            mc = a['must_contain']
            if isinstance(mc, str):
                condition = f"must_contain={mc[:30]}"
            else:
                condition = f"must_contain={mc}"
        elif a.get("contains"):
            cc = a['contains']
            if isinstance(cc, str):
                condition = f"contains={cc[:30]}"
            else:
                condition = f"contains={cc}"
        elif a.get("must_not_contain_secret"):
            condition = f"!secret={a['must_not_contain_secret']}"
        elif a.get("eval"):
            condition = f"eval={a['eval']}"
        
        verdict = ar["verdict"]
        v_icon = {
            "GENUINE": "✅", "COVERED": "✅", "LLM_DEPENDENT": "🔶",
            "VACUOUS": "❌", "MISSING_SOURCE": "❌",
            "IMPOSSIBLE": "❌", "STATUS_GUARANTEED": "⚠️",
            "UNEXERCISED": "❌", "INVALID": "❌", "MIXED": "⚠️",
        }.get(verdict, "❓")
        
        reason = ar.get("reason", "")[:80]
        lines.append(f"| {i} | {target} | {a_type} | {condition} | {v_icon} {verdict} | {reason} |")
    lines.append("")
    
    # Problems
    problems = [(i, a, ar) for i, (a, ar) in enumerate(zip(assertions, assertion_results), 1)
                if ar["verdict"] not in ("GENUINE", "COVERED")]
    if problems:
        lines.append("### 问题")
        lines.append("")
        for idx, a, ar in problems:
            verdict = ar["verdict"]
            reason = ar.get("reason", "")
            emoji = "⚠️" if ar["verdict"] in ("LLM_DEPENDENT", "MIXED", "STATUS_GUARANTEED") else "❌"
            lines.append(f"**断言 {idx} — {verdict}**{emoji}: {reason}")
            lines.append("")
    
    lines.append("---")
    return "\n".join(lines)


def generate_report(results: list[dict]) -> str:
    """Generate the summary consistency report."""
    consistent = [r for r in results if r["rating"] == "断言一致"]
    partial = [r for r in results if r["rating"] == "部分不符"]
    incompatible = [r for r in results if r["rating"] == "完全不符"]
    
    total = len(results)
    
    lines = [
        "# 断言-步骤一致性报告",
        "",
        f"**日期**: 2026-07-27",
        f"**数据源**: phase01/runs/2026-07-27-01/cases/yaml/",
        f"**用例总数**: {total}",
        "",
        "---",
        "",
        "## 1. 总览",
        "",
        "| 评级 | 数量 | 说明 |",
        "|------|:---:|------|",
        f"| 断言一致 | {len(consistent)} | 所有验证点可被步骤真实覆盖 |",
        f"| 部分不符 | {len(partial)} | 部分验证点为 VACUOUS / MISSING_SOURCE / UNVERIFIABLE 等 |",
        f"| 完全不符 | {len(incompatible)} | 全部验证点未能由步骤产出 |",
        f"| **合计** | **{total}** | |",
        "",
    ]
    
    # Dimension table
    dims = defaultdict(lambda: {"断言一致": 0, "部分不符": 0, "完全不符": 0, "合计": 0})
    for r in results:
        d = r["dim"]
        dims[d][r["rating"]] += 1
        dims[d]["合计"] += 1
    
    dim_order = ["完备性", "兼容性", "可靠性", "安全性", "易用性"]
    present_dims = [d for d in dim_order if d in dims] + sorted(d for d in dims if d not in dim_order)
    
    if dims:
        lines.append("| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |")
        lines.append("|------|:---:|:---:|:---:|:---:|")
        for dim in present_dims:
            counts = dims[dim]
            lines.append(f"| {dim} | {counts['断言一致']} | {counts['部分不符']} | {counts['完全不符']} | {counts['合计']} |")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Verdict distribution
    verdict_counts = defaultdict(int)
    for r in results:
        for a in r["assertion_results"]:
            verdict_counts[a["verdict"]] += 1
    
    lines.append("## 2. 判定分布")
    lines.append("")
    lines.append("| 判定 | 数量 | 说明 |")
    lines.append("|------|:---:|------|")
    
    verdict_desc = {
        "GENUINE": "步骤真实执行被测功能，产出断言所需输出",
        "COVERED": "步骤覆盖验证点（含平台验证型用例）",
        "VACUOUS": "步骤仅 echo 期望字符串，未执行功能（假测试）",
        "MISSING_SOURCE": "无任何步骤产出断言期望的字符串",
        "STATUS_GUARANTEED": "run_status=success 为必然结果（所有步骤 trivial）",
        "IMPOSSIBLE": "期望 !=success 但无步骤可能失败",
        "UNEXERCISED": "安全断言无对应步骤使用 secret",
        "LLM_DEPENDENT": "非功能性/LLM 辅助断言，跳过步骤追溯分析",
        "MIXED": "多字符串匹配中部分 GENUINE 部分非",
        "INVALID": "事件断言与 trigger 不一致",
    }
    
    for v in sorted(verdict_counts.keys()):
        lines.append(f"| {v} | {verdict_counts[v]} | {verdict_desc.get(v, '')} |")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Section: 断言一致
    lines.append(f"## 3. 断言一致 — 所有验证点真实覆盖（{len(consistent)} 例）")
    lines.append("")
    lines.append("| # | Case ID | 标题 |")
    lines.append("|---|---------|------|")
    for i, r in enumerate(consistent, 1):
        lines.append(f"| {i} | [{r['id']}](case/{r['id']}.md) | {r['title'][:55]} |")
    lines.append("")
    
    # Section: 部分不符
    if partial:
        lines.append(f"## 4. 部分不符 — 验证点与步骤产出部分不一致（{len(partial)} 例）")
        lines.append("")
        lines.append("| # | Case ID | 标题 | 问题判定 |")
        lines.append("|---|---------|------|------|")
        for i, r in enumerate(partial, 1):
            problem_verdicts = set(a["verdict"] for a in r["assertion_results"] if a["verdict"] not in ("GENUINE", "COVERED"))
            lines.append(f"| {i} | [{r['id']}](case/{r['id']}.md) | {r['title'][:38]} | {', '.join(sorted(problem_verdicts))} |")
        lines.append("")
    
    # Section: 完全不符
    if incompatible:
        lines.append(f"## 5. 完全不符 — 全部验证点未能由步骤产出（{len(incompatible)} 例）")
        lines.append("")
        lines.append("| # | Case ID | 标题 | 问题判定 |")
        lines.append("|---|---------|------|------|")
        for i, r in enumerate(incompatible, 1):
            problem_verdicts = set(a["verdict"] for a in r["assertion_results"] if a["verdict"] not in ("GENUINE", "COVERED"))
            lines.append(f"| {i} | [{r['id']}](case/{r['id']}.md) | {r['title'][:38]} | {', '.join(sorted(problem_verdicts))} |")
        lines.append("")
    
    return "\n".join(lines)


def main():
    text_files = {p.stem: p for p in TEXT_DIR.glob("*.md")}
    yaml_files = {p.stem: p for p in YAML_DIR.glob("*.yaml")}
    
    # Only process cases with both text and YAML
    common_ids = sorted(set(text_files) & set(yaml_files))
    
    print(f"Text specs: {len(text_files)}, YAMLs: {len(yaml_files)}, Common: {len(common_ids)}")
    
    all_results = []
    
    for cid in common_ids:
        text_info = parse_text_spec(text_files[cid])
        yaml_info = parse_case_yaml(yaml_files[cid])
        
        if not yaml_info:
            continue
        
        steps = yaml_info.get("steps", [])
        has_yaml_error = yaml_info.get("has_yaml_error", False)
        dim = yaml_info.get("dim_raw", "")
        trigger_event = yaml_info.get("trigger", {}).get("event", "")
        assertions = yaml_info.get("assertions", [])
        
        # Analyze each assertion
        assertion_results = []
        for a in assertions:
            ar = analyze_assertion(a, steps, has_yaml_error, dim, trigger_event)
            assertion_results.append(ar)
        
        rating = rate_case(assertion_results)
        
        # Generate case report
        case_md = generate_case_report(text_info, yaml_info, assertion_results, rating)
        (CASE_OUT / f"{cid}.md").write_text(case_md)
        
        result = {
            "id": cid,
            "title": yaml_info.get("title", text_info.get("title", "")),
            "dim": yaml_info.get("dim", ""),
            "rating": rating,
            "assertion_results": assertion_results,
        }
        all_results.append(result)
        
        # Copy 断言一致 YAMLs to accessable/
        if rating == "断言一致":
            import shutil
            shutil.copy2(yaml_files[cid], ACCESS_OUT / f"{cid}.yaml")
    
    # Generate summary report
    report_md = generate_report(all_results)
    REPORT_OUT.write_text(report_md)
    
    consistent_count = sum(1 for r in all_results if r["rating"] == "断言一致")
    partial_count = sum(1 for r in all_results if r["rating"] == "部分不符")
    incompatible_count = sum(1 for r in all_results if r["rating"] == "完全不符")
    
    print(f"\nAnalysis complete:")
    print(f"  Total analyzed: {len(all_results)}")
    print(f"  断言一致: {consistent_count}")
    print(f"  部分不符: {partial_count}")
    print(f"  完全不符: {incompatible_count}")
    print(f"  accessable/: {consistent_count} YAMLs")


if __name__ == "__main__":
    main()
