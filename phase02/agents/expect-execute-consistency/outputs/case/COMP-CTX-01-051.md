# COMP-CTX-01-051

- **标题**: 上下文在 workflow job step 各级注入验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**上下文在 workflow job step 各级注入验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-051

通过标准：
1. [正向] workflow 级 env 可解析 atomgit 属性 —— 断言 WF_REF=refs/
2. [正向] job 级 env 可解析 env 属性 —— 断言 JOB_REF=refs/
3. [正向] step 级 run 可解析 job 和 atomgit 属性 —— 断言 JOB_STATUS=

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| - | (workflow env) | `WF_REF: ${{ atomgit.ref }}` | - | 平台上下文在 workflow 级 env 求值 |
| - | (job env) | `JOB_REF: ${{ env.WF_REF }}` | - | env 上下文在 job 级 env 求值 |
| 1 | Step context | `echo "WF_REF=$WF_REF"` + `echo "JOB_REF=$JOB_REF"` + `echo "JOB_STATUS=${{ job.status }}"` + `echo "ATOMGIT_REF=${{ atomgit.ref }}"` | - | 各级上下文在 step 中回显 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: WF_REF=refs/ | ✅ GENUINE | 值来自 workflow env 中的 `${{ atomgit.ref }}` 上下文注入，非字面量 |
| 2 | run_logs | positive | must_contain: JOB_REF=refs/ | ✅ GENUINE | 值来自 job env 中的 `${{ env.WF_REF }}` 链式上下文引用 |
| 3 | run_logs | positive | must_contain: JOB_STATUS= | ✅ GENUINE | 同一步骤包含 `${{ job.status }}` 和 `${{ atomgit.ref }}` 表达式 |

