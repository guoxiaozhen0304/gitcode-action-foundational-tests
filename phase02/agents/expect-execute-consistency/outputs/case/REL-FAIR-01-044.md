# REL-FAIR-01-044
- **标题**: 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**并发资源公平性——2 workflow 各 3 jobs 公平调度**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-044
通过标准：
1. 启动时延差≤60s
2. 不应出现独占

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 30` | - | 占用 runner |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | startup_time_diff_seconds le 60 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量对比 |
---
