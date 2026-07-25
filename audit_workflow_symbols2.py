#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
审查所有基线用例 workflow steps 中的可疑/额外符号模式
"""
import os, glob, yaml

CASES_DIR = os.path.join(os.path.dirname(__file__), "phase01", "runs", "2026-07-23-01", "cases", "yaml")


def audit():
    files = sorted(glob.glob(os.path.join(CASES_DIR, "*.yaml")))
    total = 0
    cases_with_issues = 0

    for f in files:
        total += 1
        try:
            doc = yaml.safe_load(open(f, encoding="utf-8"))
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        cid = doc.get("id", os.path.basename(f))
        wf = doc.get("workflow") or ""
        if not isinstance(wf, str):
            continue

        issues = []
        for lineno, line in enumerate(wf.splitlines(), 1):
            # 模式1: $ATOMGIT_ 品牌前缀变量（在 run 步骤中可能应为 GITHUB_）
            if "$ATOMGIT_" in line:
                issues.append(("ATOMGIT_var_in_run", lineno, line.strip()))
            # 模式2: 双美元符号
            if "$$" in line:
                issues.append(("double_dollar", lineno, line.strip()))
            # 模式3: 反引号命令替换（deprecated，现代 shell 用 $()）
            if "`" in line:
                issues.append(("backtick_substitution", lineno, line.strip()))
            # 模式4: run 中裸露的 $ 变量引用（可能触发 bad substitution）
            # 排除 ${{ }} 表达式和 $() 命令替换
            stripped = line.strip()
            if "$" in stripped and "${{" not in stripped and "$()" not in stripped:
                # 进一步检查是否有 $VARNAME 模式
                import re
                if re.search(r"\$[A-Z_]+", stripped):
                    issues.append(("bare_dollar_var", lineno, line.strip()))
            # 模式5: 三重重定向 >>> / <<<
            if ">>>" in line or "<<<" in line:
                issues.append(("triple_redirect", lineno, line.strip()))
            # 模式6: 非 ASCII 可打印字符（中文/日文/韩文等常见字符除外）
            for ch in line:
                o = ord(ch)
                if o > 127:
                    # 允许 CJK、常见全角标点
                    if not (0x4E00 <= o <= 0x9FFF or 0x3000 <= o <= 0x303F or 0xFF00 <= o <= 0xFFEF or 0x2000 <= o <= 0x206F):
                        issues.append((f"uncommon_unicode(U+{o:04X})", lineno, line.strip()))
                        break
            # 模式7: 控制字符
            for ch in line:
                o = ord(ch)
                if o < 32 and ch not in ("\n", "\r", "\t"):
                    issues.append((f"control_char(U+{o:04X})", lineno, line.strip()))
                    break

        if issues:
            cases_with_issues += 1
            print(f"\n{cid}:")
            for t, l, c in issues[:8]:
                print(f"  [{t}] line{l}: {c[:120]}")

    print(f"\n[SUMMARY] total={total} with_issues={cases_with_issues}")


if __name__ == "__main__":
    audit()
