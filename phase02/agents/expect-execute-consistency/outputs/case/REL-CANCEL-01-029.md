# REL-CANCEL-01-029
- **标题**: 多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**按 run_id 取消指定 run 不影响其他并发 run**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-070
通过标准：
1. RUN-2 状态=canceled
2. RUN-1/RUN-3 状态=success
3. 取消收敛≤60s

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | long sleep step | `sleep 300` | - | 长时间运行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | target_run_status = canceled | positive | - | ✅ GENUINE | sleep 是真实命令；harness 并发触发 3 run + API 取消指定 run |
| 2 | sibling_run_status = success | positive | - | ✅ GENUINE | 不被取消的 run 应正常完成 |
| 3 | sibling_run_status = canceled | negative | - | ✅ GENUINE | 负向验证其他 run 未被误杀 |
| 4 | cancel_convergence_seconds le 60 | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
---
