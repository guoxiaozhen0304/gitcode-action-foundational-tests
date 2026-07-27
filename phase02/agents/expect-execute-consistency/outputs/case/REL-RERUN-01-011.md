# REL-RERUN-01-011
- **标题**: rerun 边界值——单条运行连续重新运行 3 次应全部成功
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**rerun 边界值——单条运行连续重新运行 3 次应全部成功**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-011
通过标准：
1. 运行编号递增
2. 每次 rerun 状态 = success

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 5` | — | 持有 runner 5 秒 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_count = 3 | positive | — | ✅ GENUINE | 由 harness 执行 3 次 rerun 操作，`sleep 5` 真实命令使每次 run 有真实执行 |
| 2 | run_status = completed(success) | positive | — | ✅ GENUINE | `sleep 5` 真实运行，job 无失败路径 |
---
