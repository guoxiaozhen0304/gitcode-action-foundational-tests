# COMP-EXPR-01-054

- **标题**: 字符串函数 contains startsWith endsWith 边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**字符串函数 contains startsWith endsWith 边界行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-054

通过标准：
1. [正向] contains 匹配子串返回真 —— 断言 contains_passed
2. [正向] startsWith 匹配前缀返回真 —— 断言 startswith_passed
3. [正向] endsWith 匹配后缀返回真 —— 断言 endswith_passed

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Contains match | `echo "contains_passed"` | `if: ${{ contains(atomgit.ref_name, 'main') }}` | 仅当 contains 函数求值为真时输出 |
| 2 | StartsWith match | `echo "startswith_passed"` | `if: ${{ startsWith(atomgit.ref, 'refs/heads/') }}` | 仅当 startsWith 函数求值为真时输出 |
| 3 | EndsWith match | `echo "endswith_passed"` | `if: ${{ endsWith(atomgit.ref_name, 'ain') }}` | 仅当 endsWith 函数求值为真时输出 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: contains_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ contains(...) }}` 条件，条件求值即真实被测行为 |
| 2 | run_logs | positive | must_contain: startswith_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ startsWith(...) }}` 条件 |
| 3 | run_logs | positive | must_contain: endswith_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ endsWith(...) }}` 条件 |

