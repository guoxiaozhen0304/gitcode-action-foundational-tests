#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, re, glob, yaml, json

CASES_DIR = os.path.join(os.path.dirname(__file__), "phase01", "runs", "2026-07-23-01", "cases", "yaml")

REQUIRED_TOP = ["id", "dimensions", "dimension", "priority", "title", "intent_ref", "setup", "trigger", "assertions", "teardown"]
ALLOWED_TOP = set(REQUIRED_TOP + ["workflow", "fault_injection"])
ID_RE = re.compile(r"^(COMP|COMPAT|REL|SEC|USE)-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2}-\d{3}(-V\d+)?$")
INTENT_RE = re.compile(r"^INTENT-(COMP|COMPAT|REL|SEC|USE|ACT)-\d+$")
DIMS = {"completeness", "compatibility", "reliability", "security", "usability"}
TRIGGER_EVENTS = {"push", "pr", "pull_request", "fork_pr", "pull_request_target", "pull_request_comment", "manual", "schedule", "tag", "workflow_dispatch", "issue_comment"}
TRIGGER_AS = {"maintainer", "untrusted_contributor"}
ASSERT_TYPES = {"positive", "negative", "nonfunctional"}
FAULT_AT = {"pre_job", "mid_job", "post_job"}
FAULT_ACTION = {"kill_runner", "network_partition", "disk_full", "cpu_saturate", "concurrent_flood"}
TEARDOWN_RESET = {"fixture", "full_instance", "none"}


def validate(doc, path):
    errors = []
    cid = doc.get("id", os.path.basename(path))

    for field in REQUIRED_TOP:
        if field not in doc:
            errors.append({"rule": "required_field", "field": field, "msg": f"缺失必填字段: {field}"})

    for key in doc:
        if key not in ALLOWED_TOP:
            errors.append({"rule": "additionalProperties", "field": key, "msg": f"不允许的额外字段: {key}"})

    if "id" in doc and not ID_RE.match(doc["id"]):
        errors.append({"rule": "id_format", "field": "id", "msg": f"id 格式不符: {doc['id']}"})

    dims = doc.get("dimensions")
    if isinstance(dims, list):
        if len(dims) < 1:
            errors.append({"rule": "minItems", "field": "dimensions", "msg": "dimensions 至少 1 项"})
        for d in dims:
            if d not in DIMS:
                errors.append({"rule": "enum", "field": "dimensions", "msg": f"dimensions 含非法值: {d}"})
    elif dims is not None:
        errors.append({"rule": "type", "field": "dimensions", "msg": "dimensions 应为数组"})

    dim = doc.get("dimension")
    if dim is not None and dim not in DIMS:
        errors.append({"rule": "enum", "field": "dimension", "msg": f"dimension 非法值: {dim}"})
    if isinstance(dims, list) and dim is not None and dim not in dims:
        errors.append({"rule": "consistency", "field": "dimension", "msg": f"dimension({dim}) 不在 dimensions{dims} 中"})

    pri = doc.get("priority")
    if pri is not None and pri not in {"P0", "P1", "P2"}:
        errors.append({"rule": "enum", "field": "priority", "msg": f"priority 非法值: {pri}"})

    title = doc.get("title")
    if title is not None and (not isinstance(title, str) or len(title.strip()) == 0):
        errors.append({"rule": "minLength", "field": "title", "msg": "title 为空或非法"})

    intent = doc.get("intent_ref")
    if intent is not None and not INTENT_RE.match(intent):
        errors.append({"rule": "intent_ref_format", "field": "intent_ref", "msg": f"intent_ref 格式不符: {intent}"})

    setup = doc.get("setup")
    if isinstance(setup, dict):
        if "repo_fixture" not in setup:
            errors.append({"rule": "required_field", "field": "setup.repo_fixture", "msg": "setup 缺失 repo_fixture"})
    elif setup is not None:
        errors.append({"rule": "type", "field": "setup", "msg": "setup 应为对象"})

    wf = doc.get("workflow")
    if wf is not None and not isinstance(wf, str):
        errors.append({"rule": "type", "field": "workflow", "msg": "workflow 应为 string 或 null"})

    trig = doc.get("trigger")
    if isinstance(trig, dict):
        if "event" not in trig:
            errors.append({"rule": "required_field", "field": "trigger.event", "msg": "trigger 缺失 event"})
        elif trig["event"] not in TRIGGER_EVENTS:
            errors.append({"rule": "enum", "field": "trigger.event", "msg": f"trigger.event 非法值: {trig['event']}"})
        if "as" in trig and trig["as"] not in TRIGGER_AS:
            errors.append({"rule": "enum", "field": "trigger.as", "msg": f"trigger.as 非法值: {trig['as']}"})
    elif trig is not None:
        errors.append({"rule": "type", "field": "trigger", "msg": "trigger 应为对象"})

    fi = doc.get("fault_injection")
    if isinstance(fi, dict):
        for f in ("at", "action", "recovery_expectation"):
            if f not in fi:
                errors.append({"rule": "required_field", "field": f"fault_injection.{f}", "msg": f"fault_injection 缺失 {f}"})
        if "at" in fi and fi["at"] not in FAULT_AT:
            errors.append({"rule": "enum", "field": "fault_injection.at", "msg": f"fault_injection.at 非法值: {fi['at']}"})
        if "action" in fi and fi["action"] not in FAULT_ACTION:
            errors.append({"rule": "enum", "field": "fault_injection.action", "msg": f"fault_injection.action 非法值: {fi['action']}"})
    elif fi is not None:
        errors.append({"rule": "type", "field": "fault_injection", "msg": "fault_injection 应为 null 或对象"})

    asserts = doc.get("assertions")
    if isinstance(asserts, list):
        if len(asserts) < 1:
            errors.append({"rule": "minItems", "field": "assertions", "msg": "assertions 至少 1 条"})
        for idx, a in enumerate(asserts):
            if not isinstance(a, dict):
                errors.append({"rule": "type", "field": f"assertions[{idx}]", "msg": "assertions 项应为对象"})
                continue
            if "type" not in a:
                errors.append({"rule": "required_field", "field": f"assertions[{idx}].type", "msg": f"assertions[{idx}] 缺失 type"})
            elif a["type"] not in ASSERT_TYPES:
                errors.append({"rule": "enum", "field": f"assertions[{idx}].type", "msg": f"assertions[{idx}].type 非法值: {a['type']}"})
            if "target" not in a:
                errors.append({"rule": "required_field", "field": f"assertions[{idx}].target", "msg": f"assertions[{idx}] 缺失 target"})
    elif asserts is not None:
        errors.append({"rule": "type", "field": "assertions", "msg": "assertions 应为数组"})

    td = doc.get("teardown")
    if isinstance(td, dict):
        if "reset" not in td:
            errors.append({"rule": "required_field", "field": "teardown.reset", "msg": "teardown 缺失 reset"})
        elif td["reset"] not in TEARDOWN_RESET:
            errors.append({"rule": "enum", "field": "teardown.reset", "msg": f"teardown.reset 非法值: {td['reset']}"})
    elif td is not None:
        errors.append({"rule": "type", "field": "teardown", "msg": "teardown 应为对象"})

    # === review 规则 ===
    if dim == "security":
        has_negative = False
        if isinstance(asserts, list):
            for a in asserts:
                if isinstance(a, dict) and a.get("type") == "negative":
                    has_negative = True
                    break
        if not has_negative:
            errors.append({"rule": "security_negative", "field": "assertions", "msg": "dimension=security 但 assertions 中无 negative 断言（schema 要求至少 1 条）"})

    if isinstance(fi, dict) and td is not None and td.get("reset") == "none":
        errors.append({"rule": "destructive_teardown", "field": "teardown.reset", "msg": "含 fault_injection 但 teardown.reset=none（schema 要求不得为 none）"})

    if isinstance(asserts, list):
        for idx, a in enumerate(asserts):
            if not isinstance(a, dict):
                continue
            has_rubric = "rubric" in a and a["rubric"]
            eval_val = a.get("eval")
            if has_rubric and eval_val != "llm_assisted":
                errors.append({"rule": "rubric_eval", "field": f"assertions[{idx}]", "msg": f"含 rubric 但 eval!='llm_assisted'（主观判据必须标 llm_assisted）"})
            if eval_val == "llm_assisted" and not has_rubric:
                errors.append({"rule": "llm_assisted_rubric", "field": f"assertions[{idx}]", "msg": "eval=llm_assisted 但缺少 rubric"})

    return errors


def main():
    results = []
    total = 0
    bad = 0
    files = sorted(glob.glob(os.path.join(CASES_DIR, "*.yaml")) + glob.glob(os.path.join(CASES_DIR, "*.yml")))

    for f in files:
        total += 1
        cid = os.path.basename(f)
        try:
            doc = yaml.safe_load(open(f, encoding="utf-8"))
        except yaml.YAMLError as e:
            results.append({"case_id": cid, "errors": [{"rule": "yaml_parse", "msg": str(e)}]})
            bad += 1
            continue
        if not isinstance(doc, dict):
            results.append({"case_id": cid, "errors": [{"rule": "root_type", "msg": "根节点不是对象"}]})
            bad += 1
            continue
        errs = validate(doc, f)
        if errs:
            results.append({"case_id": doc.get("id", cid), "errors": errs})
            bad += 1

    out_path = os.path.join(os.path.dirname(__file__), "schema_validation_report.json")
    json.dump({"total": total, "bad": bad, "good": total - bad, "details": results}, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Report written to {out_path}")
    print(f"total={total} bad={bad} good={total-bad}")


if __name__ == "__main__":
    main()
