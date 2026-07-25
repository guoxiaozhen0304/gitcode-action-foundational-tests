#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
校验所有 Phase 01 用例 YAML 是否符合 executable-case.schema.yaml
"""
import os, sys, re, glob, yaml

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "phase01", "schema")
CASES_DIR = os.path.join(os.path.dirname(__file__), "phase01", "runs", "2026-07-23-01", "cases", "yaml")

# Schema 规则（从 executable-case.schema.yaml 提取）
REQUIRED_TOP = ["id", "dimensions", "dimension", "priority", "title", "intent_ref", "setup", "trigger", "assertions", "teardown"]
ALLOWED_TOP = set(REQUIRED_TOP + ["workflow", "fault_injection"])
ID_RE = re.compile(r"^(COMP|COMPAT|REL|SEC|USE)-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2}-\d{3}(-V\d+)?$")
INTENT_RE = re.compile(r"^INTENT-(COMP|COMPAT|REL|SEC|USE|ACT)-\d+$")
DIMS = {"completeness", "compatibility", "reliability", "security", "usability"}
PRIORITIES = {"P0", "P1", "P2"}
TRIGGER_EVENTS = {"push", "pr", "pull_request", "fork_pr", "pull_request_target", "pull_request_comment", "manual", "schedule", "tag", "workflow_dispatch", "issue_comment"}
TRIGGER_AS = {"maintainer", "untrusted_contributor"}
ASSERT_TYPES = {"positive", "negative", "nonfunctional"}
FAULT_AT = {"pre_job", "mid_job", "post_job"}
FAULT_ACTION = {"kill_runner", "network_partition", "disk_full", "cpu_saturate", "concurrent_flood"}
TEARDOWN_RESET = {"fixture", "full_instance", "none"}


def validate(doc, path):
    errors = []
    cid = doc.get("id", os.path.basename(path))

    # 1. 顶层 required
    for field in REQUIRED_TOP:
        if field not in doc:
            errors.append(f"[{cid}] 缺失必填字段: {field}")

    # 2. additionalProperties: false
    for key in doc:
        if key not in ALLOWED_TOP:
            errors.append(f"[{cid}] 不允许的额外字段: {key}")

    # 3. id 格式
    if "id" in doc:
        if not ID_RE.match(doc["id"]):
            errors.append(f"[{cid}] id 格式不符: {doc['id']}")

    # 4. dimensions
    dims = doc.get("dimensions")
    if isinstance(dims, list):
        if len(dims) < 1:
            errors.append(f"[{cid}] dimensions 至少 1 项")
        for d in dims:
            if d not in DIMS:
                errors.append(f"[{cid}] dimensions 含非法值: {d}")
    elif dims is not None:
        errors.append(f"[{cid}] dimensions 应为数组")

    # 5. dimension
    dim = doc.get("dimension")
    if dim is not None and dim not in DIMS:
        errors.append(f"[{cid}] dimension 非法值: {dim}")

    # 6. dimensions 应包含 dimension
    if isinstance(dims, list) and dim is not None and dim not in dims:
        errors.append(f"[{cid}] dimension({dim}) 不在 dimensions{dims} 中")

    # 7. priority
    pri = doc.get("priority")
    if pri is not None and pri not in PRIORITIES:
        errors.append(f"[{cid}] priority 非法值: {pri}")

    # 8. title
    title = doc.get("title")
    if title is not None and (not isinstance(title, str) or len(title.strip()) == 0):
        errors.append(f"[{cid}] title 为空或非法")

    # 9. intent_ref
    intent = doc.get("intent_ref")
    if intent is not None and not INTENT_RE.match(intent):
        errors.append(f"[{cid}] intent_ref 格式不符: {intent}")

    # 10. setup
    setup = doc.get("setup")
    if isinstance(setup, dict):
        if "repo_fixture" not in setup:
            errors.append(f"[{cid}] setup 缺失 repo_fixture")
    elif setup is not None:
        errors.append(f"[{cid}] setup 应为对象")

    # 11. workflow 类型
    wf = doc.get("workflow")
    if wf is not None and not isinstance(wf, str):
        errors.append(f"[{cid}] workflow 应为 string 或 null")

    # 12. trigger
    trig = doc.get("trigger")
    if isinstance(trig, dict):
        if "event" not in trig:
            errors.append(f"[{cid}] trigger 缺失 event")
        else:
            if trig["event"] not in TRIGGER_EVENTS:
                errors.append(f"[{cid}] trigger.event 非法值: {trig['event']}")
        if "as" in trig and trig["as"] not in TRIGGER_AS:
            errors.append(f"[{cid}] trigger.as 非法值: {trig['as']}")
    elif trig is not None:
        errors.append(f"[{cid}] trigger 应为对象")

    # 13. fault_injection
    fi = doc.get("fault_injection")
    if isinstance(fi, dict):
        for f in ("at", "action", "recovery_expectation"):
            if f not in fi:
                errors.append(f"[{cid}] fault_injection 缺失 {f}")
        if "at" in fi and fi["at"] not in FAULT_AT:
            errors.append(f"[{cid}] fault_injection.at 非法值: {fi['at']}")
        if "action" in fi and fi["action"] not in FAULT_ACTION:
            errors.append(f"[{cid}] fault_injection.action 非法值: {fi['action']}")
    elif fi is not None:
        errors.append(f"[{cid}] fault_injection 应为 null 或对象")

    # 14. assertions
    asserts = doc.get("assertions")
    if isinstance(asserts, list):
        if len(asserts) < 1:
            errors.append(f"[{cid}] assertions 至少 1 条")
        for idx, a in enumerate(asserts):
            if not isinstance(a, dict):
                errors.append(f"[{cid}] assertions[{idx}] 应为对象")
                continue
            if "type" not in a:
                errors.append(f"[{cid}] assertions[{idx}] 缺失 type")
            elif a["type"] not in ASSERT_TYPES:
                errors.append(f"[{cid}] assertions[{idx}].type 非法值: {a['type']}")
            if "target" not in a:
                errors.append(f"[{cid}] assertions[{idx}] 缺失 target")
    elif asserts is not None:
        errors.append(f"[{cid}] assertions 应为数组")

    # 15. teardown
    td = doc.get("teardown")
    if isinstance(td, dict):
        if "reset" not in td:
            errors.append(f"[{cid}] teardown 缺失 reset")
        elif td["reset"] not in TEARDOWN_RESET:
            errors.append(f"[{cid}] teardown.reset 非法值: {td['reset']}")
    elif td is not None:
        errors.append(f"[{cid}] teardown 应为对象")

    # === 校验要点（review 规则）===
    # 1. 安全用例 assertions 中至少一条 type=negative
    if dim == "security":
        has_negative = False
        if isinstance(asserts, list):
            for a in asserts:
                if isinstance(a, dict) and a.get("type") == "negative":
                    has_negative = True
                    break
        if not has_negative:
            errors.append(f"[{cid}] dimension=security 但 assertions 中无 negative 断言（schema 要求至少 1 条）")

    # 2. 破坏性用例 teardown.reset 不得为 none
    # 这里保守判断：只要有 fault_injection 且非 null，就视为破坏性用例
    if isinstance(fi, dict) and td is not None and td.get("reset") == "none":
        errors.append(f"[{cid}] 含 fault_injection 但 teardown.reset=none（schema 要求不得为 none）")

    # 3. 主观判据必须标 eval=llm_assisted 并给 rubric
    if isinstance(asserts, list):
        for idx, a in enumerate(asserts):
            if not isinstance(a, dict):
                continue
            # 如果包含 eval 字段且不是 llm_assisted，或包含 rubric 但没有 eval=llm_assisted
            has_rubric = "rubric" in a and a["rubric"]
            eval_val = a.get("eval")
            if has_rubric and eval_val != "llm_assisted":
                errors.append(f"[{cid}] assertions[{idx}] 含 rubric 但 eval!='llm_assisted'（主观判据必须标 llm_assisted）")
            # 如果 eval=llm_assisted 但没有 rubric
            if eval_val == "llm_assisted" and not has_rubric:
                errors.append(f"[{cid}] assertions[{idx}] eval=llm_assisted 但缺少 rubric")

    return errors


def main():
    all_errors = []
    total = 0
    bad = 0
    files = sorted(glob.glob(os.path.join(CASES_DIR, "*.yaml")) + glob.glob(os.path.join(CASES_DIR, "*.yml")))

    for f in files:
        total += 1
        try:
            doc = yaml.safe_load(open(f, encoding="utf-8"))
        except yaml.YAMLError as e:
            all_errors.append(f"[{os.path.basename(f)}] YAML 解析失败: {e}")
            bad += 1
            continue
        if not isinstance(doc, dict):
            all_errors.append(f"[{os.path.basename(f)}] 根节点不是对象")
            bad += 1
            continue
        errs = validate(doc, f)
        if errs:
            all_errors.extend(errs)
            bad += 1

    # 输出报告
    print(f"=== 用例 Schema 校验报告 ===")
    print(f"总计用例: {total}")
    print(f"合规用例: {total - bad}")
    print(f"不合规用例: {bad}")
    print()

    if all_errors:
        # 按用例分组
        from collections import defaultdict
        grouped = defaultdict(list)
        for e in all_errors:
            m = re.match(r"\[([^\]]+)\] (.+)", e)
            if m:
                grouped[m.group(1)].append(m.group(2))
            else:
                grouped["UNKNOWN"].append(e)

        print("--- 不合规用例详情 ---")
        for cid in sorted(grouped.keys()):
            print(f"\n{cid}:")
            for msg in grouped[cid]:
                print(f"  - {msg}")
    else:
        print("所有用例均通过 schema 校验！")

    # 额外输出一行统计供调用方解析
    print(f"\n[SUMMARY] total={total} bad={bad}")


if __name__ == "__main__":
    main()
