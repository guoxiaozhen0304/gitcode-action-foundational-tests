#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 YAML 格式破坏：eval: llm_assisted 缩进错误导致的解析失败
"""
import os, glob, yaml

CASES_DIR = os.path.join(os.path.dirname(__file__), "phase01", "runs", "2026-07-23-01", "cases", "yaml")

# 已知损坏的 10 个文件
BROKEN_FILES = [
    "COMPAT-COMM-01-001.yaml",
    "COMPAT-CTX-01-003.yaml",
    "COMPAT-OUTPUT-01-001.yaml",
    "COMPAT-PR-01-003.yaml",
    "COMPAT-PR-01-004.yaml",
    "COMPAT-PR-01-005.yaml",
    "COMPAT-PR-01-006.yaml",
    "COMPAT-WCMD-01-001.yaml",
    "COMPAT-WCMD-01-002.yaml",
    "COMPAT-WCMD-01-003.yaml",
]


def fix_yaml(path):
    raw = open(path, encoding="utf-8").read()
    lines = raw.splitlines()
    changes = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        # 模式A: 2空格缩进的 eval: llm_assisted，下一行是4空格的 rubric:
        # 修复：将 eval 改为与 rubric 相同的缩进
        if stripped == "eval: llm_assisted":
            indent = len(line) - len(line.lstrip())
            if indent == 2 and i + 1 < len(lines):
                next_line = lines[i + 1]
                next_stripped = next_line.lstrip()
                next_indent = len(next_line) - len(next_line.lstrip())
                if next_stripped.startswith("rubric:") and next_indent == 4:
                    # 检查上一行是否已经有同 assertion 内的 eval
                    prev_has_eval = False
                    if i - 1 >= 0:
                        prev_line = lines[i - 1]
                        prev_stripped = prev_line.lstrip()
                        prev_indent = len(prev_line) - len(prev_line.lstrip())
                        if prev_stripped == "eval: llm_assisted" and prev_indent == 4:
                            prev_has_eval = True

                    if prev_has_eval:
                        # 删除重复的 eval 行
                        del lines[i]
                        changes.append(f"deleted duplicate eval at line {i+1}")
                        continue
                    else:
                        # 修正缩进为4空格
                        lines[i] = "    eval: llm_assisted"
                        changes.append(f"fixed eval indent at line {i+1}")

        i += 1

    if changes:
        new_raw = "\n".join(lines)
        open(path, "w", encoding="utf-8").write(new_raw)
        # 验证 YAML 可解析
        try:
            yaml.safe_load(new_raw)
            changes.append("YAML valid")
        except yaml.YAMLError as e:
            changes.append(f"YAML still broken: {e}")

    return changes


def main():
    for fname in BROKEN_FILES:
        path = os.path.join(CASES_DIR, fname)
        changes = fix_yaml(path)
        if changes:
            print(f"{fname}: {changes}")
        else:
            print(f"{fname}: no changes needed")


if __name__ == "__main__":
    main()
