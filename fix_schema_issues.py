#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复 schema 违规用例
"""
import os, re, glob, yaml

CASES_DIR = os.path.join(os.path.dirname(__file__), "phase01", "runs", "2026-07-23-01", "cases", "yaml")

# A1 类映射: KEEP-TC-xxx → INTENT-COMP-{功能编号}
KEEP_TC_MAP = {
    "KEEP-TC-017~057": "INTENT-COMP-047",
    "KEEP-TC-048~060": "INTENT-COMP-048",
    "KEEP-TC-566~570": "INTENT-COMP-049",
    "KEEP-TC-514~559": "INTENT-COMP-084",
    "KEEP-TC-475~512": "INTENT-COMP-085",
    "KEEP-TC-276~328": "INTENT-COMP-086",
    "KEEP-TC-331~333": "INTENT-COMP-087",
    "KEEP-TC-240~246": "INTENT-COMP-088",
    "KEEP-TC-086~124": "INTENT-COMP-051",
    "KEEP-TC-001~004": "INTENT-COMP-050",
    "KEEP-TC-180~182": "INTENT-COMP-054",
    "KEEP-TC-186": "INTENT-COMP-055",
    "KEEP-TC-187": "INTENT-COMP-056",
    "KEEP-TC-183~185": "INTENT-COMP-057",
    "KEEP-TC-160~175": "INTENT-COMP-058",
    "KEEP-TC-264~288": "INTENT-COMP-066",
    "KEEP-TC-276~278": "INTENT-COMP-067",
    "KEEP-TC-096~098": "INTENT-COMP-080",
    "KEEP-TC-431~433": "INTENT-COMP-081",
    "KEEP-TC-279~288": "INTENT-COMP-069",
    "KEEP-TC-197~222": "INTENT-COMP-059",
    "KEEP-TC-223~233": "INTENT-COMP-072",
    "KEEP-TC-061~083": "INTENT-COMP-073",
    "KEEP-TC-084~085": "INTENT-COMP-074",
    "KEEP-TC-237~430": "INTENT-COMP-075",
    "KEEP-TC-075~083": "INTENT-COMP-076",
    "KEEP-TC-469~470": "INTENT-COMP-077",
    "KEEP-TC-423": "INTENT-COMP-078",
    "KEEP-TC-234~560": "INTENT-COMP-079",
    "KEEP-TC-438~440": "INTENT-COMP-083",
    "KEEP-TC-366~401": "INTENT-COMP-061",
    "KEEP-TC-289~293": "INTENT-COMP-063",
}

# A2 类映射: INTENT-COMPAT-NEW-xxx → INTENT-COMPAT-xxx
NEW_SUFFIX_RE = re.compile(r"INTENT-COMPAT-NEW-(\d+)")


def fix_file(path):
    changes = []
    raw = open(path, encoding="utf-8").read()
    doc = yaml.safe_load(raw)
    cid = doc.get("id", os.path.basename(path))
    modified = False

    # --- C 类: fault_injection + teardown.reset=none → fixture ---
    fi = doc.get("fault_injection")
    td = doc.get("teardown")
    if isinstance(fi, dict) and isinstance(td, dict) and td.get("reset") == "none":
        raw = raw.replace("reset: none", "reset: fixture", 1)
        changes.append("C: teardown.reset none→fixture")
        modified = True

    # --- A1 类: KEEP-TC-xxx → INTENT-COMP-xxx ---
    intent = doc.get("intent_ref", "")
    if intent in KEEP_TC_MAP:
        new_intent = KEEP_TC_MAP[intent]
        raw = raw.replace(f"intent_ref: {intent}", f"intent_ref: {new_intent}", 1)
        changes.append(f"A1: intent_ref {intent}→{new_intent}")
        modified = True

    # --- A2 类: INTENT-COMPAT-NEW-xxx → INTENT-COMPAT-xxx ---
    m = NEW_SUFFIX_RE.match(intent)
    if m:
        new_intent = f"INTENT-COMPAT-{m.group(1)}"
        raw = raw.replace(f"intent_ref: {intent}", f"intent_ref: {new_intent}", 1)
        changes.append(f"A2: intent_ref {intent}→{new_intent}")
        modified = True

    # --- B 类: 含 rubric 但 eval != llm_assisted → 补 eval: llm_assisted ---
    asserts = doc.get("assertions", [])
    if isinstance(asserts, list):
        for idx, a in enumerate(asserts):
            if not isinstance(a, dict):
                continue
            has_rubric = "rubric" in a and a["rubric"]
            eval_val = a.get("eval")
            if has_rubric and eval_val != "llm_assisted":
                # 策略: 如果 rubric 存在，统一视为 llm_assisted
                old_text = None
                # 尝试多种 YAML 排版模式进行精确替换
                # 模式1: rubric 在行尾，eval 缺失
                # 模式2: 已有 eval 行但值不对
                patterns = [
                    # eval 行存在但值错误
                    (rf"(eval: {eval_val}\n)(\s+rubric:)", rf"eval: llm_assisted\n\2"),
                    # eval 缺失，在 rubric 前插入
                    (rf"(\n)(\s+rubric:)", rf"\1  eval: llm_assisted\n\2"),
                ]
                for pat_old, pat_new in patterns:
                    if re.search(pat_old, raw):
                        raw = re.sub(pat_old, pat_new, raw, count=1)
                        changes.append(f"B: assertions[{idx}] eval→llm_assisted")
                        modified = True
                        break
                else:
                    # fallback: 直接在 rubric 行前插入 eval: llm_assisted
                    rubric_line = None
                    lines = raw.splitlines()
                    for i, line in enumerate(lines):
                        stripped = line.lstrip()
                        if stripped.startswith("rubric:"):
                            indent = line[:len(line) - len(line.lstrip())]
                            lines.insert(i, f"{indent}eval: llm_assisted")
                            changes.append(f"B: assertions[{idx}] eval→llm_assisted (inserted)")
                            modified = True
                            raw = "\n".join(lines)
                            break

    if modified:
        open(path, "w", encoding="utf-8").write(raw)

    return cid, changes


def main():
    files = sorted(glob.glob(os.path.join(CASES_DIR, "*.yaml")) + glob.glob(os.path.join(CASES_DIR, "*.yml")))
    total_fixed = 0
    total_files = 0
    report = []

    for f in files:
        total_files += 1
        cid, changes = fix_file(f)
        if changes:
            total_fixed += 1
            report.append((cid, changes))

    print(f"=== Schema 批量修复报告 ===")
    print(f"扫描文件: {total_files}")
    print(f"修复文件: {total_fixed}")
    print()
    for cid, changes in report:
        print(f"{cid}:")
        for c in changes:
            print(f"  + {c}")
    print(f"\n[SUMMARY] scanned={total_files} fixed={total_fixed}")


if __name__ == "__main__":
    main()
