# COMP-JOB-01-067

- **标题**: job 可选字段 env if timeout-minutes needs 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**job 可选字段 env if timeout-minutes needs 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-066

通过标准：
1. [正向] job env 在 step 中可访问 —— 断言 JOB_VAR=job_value
2. [正向] needs 依赖 job 先执行 —— 断言 prepare_done
3. [正向] timeout-minutes 字段被接受 —— 断言 optional_ok

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 (prepare) | Prepare | `echo "prepare_done"` | - | 字面量 |
| 2 (verify) | Check fields | `echo "JOB_VAR=$JOB_VAR"` + `echo "optional_ok"` | (job 级) if: ${{ true }}, needs: prepare, timeout-minutes: 30 | env 块定义值和 echo 字面量 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: prepare_done | ❌ VACUOUS | prepare job 仅 echo 字面量，无 if:、无 ${{ }}、无 uses:、无 real commands |
| 2 | run_logs | positive | must_contain: JOB_VAR=job_value | ❌ VACUOUS | 值来自 `env:` 块定义的字面量 job_value，步骤仅回显该预定义值 |
| 3 | run_logs | positive | must_contain: optional_ok | ❌ VACUOUS | 仅 echo 字面量 |

### 问题

**全部断言 VACUOUS**: prepare job 仅 echo 字面量。verify job 虽有 `needs: prepare`、`if: ${{ true }}`、`timeout-minutes: 30` 等 job 级字段配置，但步骤本身仅 echo 预定义的环境变量值和字面量字符串。env 值 "job_value" 是硬编码在 YAML 中的，步骤不做任何验证。needs 依赖和 timeout-minutes 的效果由 harness 在外部验证，step 内无自检逻辑。

