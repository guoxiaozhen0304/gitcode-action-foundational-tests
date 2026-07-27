# COMP-ISOLATION-01-002

- **标题**: 环境变量不跨 job 泄漏
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**环境变量不跨 job 泄漏**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-011

通过标准：
1. [负向] job 2 中环境变量值为空或未设置 —— 断言 must_not_contain "env leaked"

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 (job1) | Export env | `echo "ISOLATION_VAR=leak" >> "$ATOMGIT_ENV"` | - | 通过平台命令写入环境变量 |
| 2 (job2) | Verify env absent | `if [ -z "${ISOLATION_VAR:-}" ]; then echo "env not leaked as expected"; else echo "env leaked: $ISOLATION_VAR"; exit 1; fi` | - (needs: job1) | 验证跨 job 环境变量隔离 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | job2 有真实 bash `if/elif/exit 1` 逻辑，env 泄漏时 dirty exit |
| 2 | run_logs | negative | must_not_contain: env leaked | ✅ GENUINE | 若 env 泄漏则 job2 输出 "env leaked: ..." 并 exit 1；隔离正常则无此输出 |

