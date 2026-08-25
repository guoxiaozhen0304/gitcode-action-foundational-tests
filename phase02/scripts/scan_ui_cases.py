#!/usr/bin/env python3
"""Scan all 24 UI cases and summarize their requirements."""
import os, yaml

dir_path = r"D:\gxz\gitcode-action-foundational-tests\phase01\runs\2026-08-25-01\cases\yaml"
files = sorted([f for f in os.listdir(dir_path) if f.startswith("UI-") and f.endswith(".yaml")])

for fname in files:
    fpath = os.path.join(dir_path, fname)
    with open(fpath, encoding="utf-8") as f:
        case = yaml.safe_load(f)
    ui = case.get("ui", {})
    url = ui.get("url", "")
    actions = ui.get("actions", [])
    assertions = case.get("assertions", [])
    action_types = [a["type"] for a in actions]
    assertion_targets = [a["target"] for a in assertions]
    print(f"{fname}: {url[:60]}... | actions={action_types} | asserts={assertion_targets}")
