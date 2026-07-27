# REL-CANCEL-01-028
- **标题**: 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**手动取消运行中的 workflow 时 always() cleanup step 仍应执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-028
通过标准：
1. 非 always step 被终止
2. cleanup step 日志存在且 completed
3. workflow 状态=cancelled

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep main step | `sleep 60` | - | 耗时步骤，供取消操作窗口 |
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
| 1 | cleanup_step_status = success | positive | - | ✅ GENUINE | sleep 提供取消窗口；cleanup 步骤含 `if: ${{ always() }}` 表达式，真实测试取消后 always 语义 |
| 2 | run_status = canceled | positive | - | ✅ GENUINE | harness 在 sleep 期间取消，workflow 真实进入 canceled 状态 |
---
