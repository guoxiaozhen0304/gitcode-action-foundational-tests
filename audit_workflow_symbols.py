#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
审查所有基线用例的 workflow 字段，查找 steps 中的异常/额外符号
"""
import os, sys, glob, yaml

CASES_DIR = os.path.join(os.path.dirname(__file__), "phase01", "runs", "2026-07-23-01", "cases", "yaml")

# 异常字符检查集
# 制表符、零宽字符、非标准空格、控制字符（除标准换行/回车外）
def find_anomalies(text, context=""):
    issues = []
    for lineno, line in enumerate(text.splitlines(), 1):
        # 1. 制表符
        if '\t' in line:
            issues.append((lineno, "制表符(tab)", line.strip()))
        # 2. 零宽字符
        for ch in ['​', '‌', '‍', '⁠', '﻿']:
            if ch in line:
                issues.append((lineno, f"零宽字符(U+{ord(ch):04X})", line.strip()))
        # 3. 非标准空格（除普通空格 U+0020 外）
        for ch in line:
            if ch.isspace() and ch not in (' ', '\n', '\r'):
                issues.append((lineno, f"非标准空白(U+{ord(ch):04X})", line.strip()))
        # 4. 控制字符
        for ch in line:
            if ord(ch) < 32 and ch not in ('\n', '\r', '\t'):
                issues.append((lineno, f"控制字符(U+{ord(ch):04X})", line.strip()))
        # 5. 全角符号（ASCII 范围内的常见符号的全角变体）
        fullwidth_punct = set('＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝')
        for ch in line:
            if ch in fullwidth_punct:
                issues.append((lineno, f"全角符号({ch})", line.strip()))
    return issues


def analyze_workflow_steps(doc, path):
    cid = doc.get("id", os.path.basename(path))
    wf_text = doc.get("workflow") or ""
    if not isinstance(wf_text, str):
        return []

    findings = []

    # 对 workflow 整体做异常字符扫描
    anomalies = find_anomalies(wf_text, "workflow")
    if anomalies:
        findings.append({"scope": "workflow整体", "anomalies": anomalies})

    # 尝试解析 workflow 字符串为 YAML，定位 steps
    try:
        wf_doc = yaml.safe_load(wf_text)
    except yaml.YAMLError:
        wf_doc = None

    if isinstance(wf_doc, dict):
        jobs = wf_doc.get("jobs", {})
        if isinstance(jobs, dict):
            for job_name, job_def in jobs.items():
                if not isinstance(job_def, dict):
                    continue
                steps = job_def.get("steps", [])
                if isinstance(steps, list):
                    for step_idx, step in enumerate(steps):
                        if not isinstance(step, dict):
                            continue
                        step_str = yaml.safe_dump(step, allow_unicode=True)
                        step_anomalies = find_anomalies(step_str, f"step[{step_idx}]")
                        if step_anomalies:
                            findings.append({
                                "scope": f"job={job_name} step[{step_idx}]",
                                "step_name": step.get("name", ""),
                                "anomalies": step_anomalies
                            })

    return findings


def main():
    files = sorted(glob.glob(os.path.join(CASES_DIR, "*.yaml")) + glob.glob(os.path.join(CASES_DIR, "*.yml")))
    total = 0
    cases_with_issues = 0
    report = []

    for f in files:
        total += 1
        try:
            doc = yaml.safe_load(open(f, encoding="utf-8"))
        except yaml.YAMLError as e:
            report.append((os.path.basename(f), [{"scope": "YAML解析失败", "error": str(e)}]))
            cases_with_issues += 1
            continue
        if not isinstance(doc, dict):
            continue
        findings = analyze_workflow_steps(doc, f)
        if findings:
            cases_with_issues += 1
            report.append((doc.get("id", os.path.basename(f)), findings))

    # 输出报告
    print(f"=== 基线用例 workflow steps 异常符号审查报告 ===")
    print(f"扫描用例: {total}")
    print(f"异常用例: {cases_with_issues}")
    print()

    for cid, findings in report:
        print(f"\n{cid}:")
        for finding in findings:
            scope = finding.get("scope", "")
            if "error" in finding:
                print(f"  [YAML解析失败] {finding['error']}")
                continue
            step_name = finding.get("step_name", "")
            if step_name:
                print(f"  [{scope}] name='{step_name}'")
            else:
                print(f"  [{scope}]")
            for lineno, desc, content in finding["anomalies"]:
                print(f"    行{lineno}: {desc}")
                print(f"      内容: {repr(content[:120])}")

    print(f"\n[SUMMARY] total={total} with_issues={cases_with_issues}")


if __name__ == "__main__":
    main()
