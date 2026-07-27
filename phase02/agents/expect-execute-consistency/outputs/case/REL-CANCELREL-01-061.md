# REL-CANCELREL-01-061
- **标题**: 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**queued/running/post 各阶段取消状态正确过渡**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-061
通过标准：
1. 各阶段取消终态稳定
2. 取消到终态≤60s
3. queued 取消后不应错标

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep main step | `sleep 60` | - | 运行中 |
| 2 | cleanup always step | `echo cleanup executed` | `if: ${{ always() }}` | cleanup 标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cancel_queued_status = canceled | positive | - | ✅ GENUINE | sleep 是真实命令；cleanup 含 `if: ${{ always() }}`；harness 分阶段取消 |
| 2 | cancel_running_status = canceled | positive | - | ✅ GENUINE | running 阶段取消 |
| 3 | cancel_post_main_status = success | positive | - | ✅ GENUINE | post 阶段取消后主结论不变 |
| 4 | cancel_stabilization_seconds le 60 | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
---
