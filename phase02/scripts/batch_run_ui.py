#!/usr/bin/env python3
"""Batch run all 24 UI cases with dependency management."""
import os, sys, json, yaml, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ui_runner import UiConfig, _load_cookies, run_ui_case

COOKIE_PATH = "ui_cookie.json"
CASE_DIR = r"D:\gxz\gitcode-action-foundational-tests\phase01\runs\2026-08-25-01\cases\yaml"
OUT_DIR = "ui_run_results"

cfg = UiConfig(owner="weixin_55883847", repo="agent_gxz")
cookies = _load_cookies(COOKIE_PATH)

os.makedirs(OUT_DIR, exist_ok=True)

# List all UI cases
files = sorted([f for f in os.listdir(CASE_DIR) if f.startswith("UI-") and f.endswith(".yaml")])

results = []
for i, fname in enumerate(files, 1):
    fpath = os.path.join(CASE_DIR, fname)
    print(f"\n[{i}/{len(files)}] Running {fname}...")

    with open(fpath, encoding="utf-8") as f:
        case = yaml.safe_load(f)

    case_id = case.get("id", fname)
    url = case["ui"]["url"]
    actions = case["ui"].get("actions", [])
    assertions = case.get("assertions", [])

    result = run_ui_case(
        cfg=cfg,
        case_id=case_id,
        url=url,
        actions=actions,
        assertions=assertions,
        cookies=cookies,
        output_dir=OUT_DIR,
    )
    results.append(result)
    print(f"  → {result['status']} ({result['duration_seconds']}s)")

    # Brief pause between cases
    time.sleep(1)

# Summary
print("\n" + "="*60)
print("BATCH RUN SUMMARY")
print("="*60)
pass_count = sum(1 for r in results if r["status"] == "PASS")
fail_count = sum(1 for r in results if r["status"] == "FAIL")
env_count = sum(1 for r in results if r["status"] == "ENV_ERROR")
print(f"PASS: {pass_count}  FAIL: {fail_count}  ENV_ERROR: {env_count}")

for r in results:
    status_icon = "✅" if r["status"] == "PASS" else "❌"
    print(f"{status_icon} {r['case_id']:25s} {r['status']:10s} {r['duration_seconds']:5.1f}s")

# Save summary
summary_path = os.path.join(OUT_DIR, "summary.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nSummary saved: {summary_path}")
