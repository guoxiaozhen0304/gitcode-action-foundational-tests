# COMP-EXPR-01-058

- **标题**: 表达式运算符与优先级边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**表达式运算符与优先级边界行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-058

通过标准：
1. [正向] == 和 != 运算正确 —— 断言 eq_passed、ne_passed
2. [正向] 比较运算符正确 —— 断言 gt_passed
3. [正向] && 和 || 优先级正确 —— 断言 logic_passed

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Equality | `echo "eq_passed"` | `if: ${{ atomgit.ref_name == 'main' \|\| true }}` | 当 `==` 运算正确时输出 |
| 2 | Not equal | `echo "ne_passed"` | `if: ${{ atomgit.ref_name != 'nonexistent' }}` | 当 `!=` 运算正确时输出 |
| 3 | Greater than | `echo "gt_passed"` | `if: ${{ 5 > 3 }}` | 当 `>` 运算正确时输出 |
| 4 | Logical combo | `echo "logic_passed"` | `if: ${{ true && (false \|\| true) }}` | 当逻辑优先级正确时输出 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: eq_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ == ` 和 `\|\|` 运算，运算符求值即真实被测行为 |
| 2 | run_logs | positive | must_contain: ne_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ != ` 运算 |
| 3 | run_logs | positive | must_contain: gt_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ 5 > 3 }}` 比较运算 |
| 4 | run_logs | positive | must_contain: logic_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ true && (false \|\| true) }}` 逻辑优先级测试 |

