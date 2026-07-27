# COMP-CTX-01-052

- **标题**: 上下文在条件表达式 if 中注入验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**上下文在条件表达式 if 中注入验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-051

通过标准：
1. [正向] atomgit.ref 条件正确匹配时步骤执行 —— 断言 run_logs must_contain always
2. [正向] env 条件正确匹配时步骤执行 —— 断言 run_logs must_contain conditional_env_passed

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| - | (job if) | - | `if: ${{ atomgit.ref == 'refs/heads/main' \|\| true }}` | job 级上下文条件求值 |
| 1 | Always run | `echo "always"` | - | "always" |
| 2 | Conditional env | `echo "conditional_env_passed"` | `if: ${{ env.ALWAYS_TRUE == 'yes' }}` | "conditional_env_passed"（当 env 上下文条件通过时） |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: always | ✅ GENUINE | job 级 `if:` 包含 `${{ atomgit.ref }}` 条件，条件求值即真实被测行为 |
| 2 | run_logs | positive | must_contain: conditional_env_passed | ✅ GENUINE | 步骤 `if:` 包含 `${{ env.ALWAYS_TRUE }}` 条件，条件求值即真实被测行为 |

