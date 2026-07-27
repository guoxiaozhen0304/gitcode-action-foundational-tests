# COMP-ENVCTX-01-050

- **标题**: env 优先级链 step 大于 job 大于 workflow
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**env 优先级链 step 大于 job 大于 workflow**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-050

通过标准：
1. [正向] 最终输出值为 step 级定义的值 —— 断言 MY_VAR=step_value
2. [正向] 无 job 级 env 时继承 workflow 级 —— 断言 JOB_VAR=job_value

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| - | (workflow env) | `MY_VAR: workflow_value` | - | workflow 级环境变量 |
| - | (job env) | `MY_VAR: job_value` | - | job 级环境变量（覆盖 workflow 级） |
| 1 | Step override | `echo "MY_VAR=$MY_VAR"` | - (step env: MY_VAR: step_value) | 平台 env 优先级链解析结果 |
| 2 | Job inherit | `echo "JOB_VAR=$MY_VAR"` | - | 继承 job 级 env 值 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: MY_VAR=step_value | ✅ GENUINE | 值来自 step 级 `env:` 块定义，验证平台 env 优先级链 step > job > workflow |
| 2 | run_logs | positive | must_contain: JOB_VAR=job_value | ✅ GENUINE | 值来自 job 级 `env:` 块定义（无 step 覆盖），验证 job 级 env 对 step 可见 |

