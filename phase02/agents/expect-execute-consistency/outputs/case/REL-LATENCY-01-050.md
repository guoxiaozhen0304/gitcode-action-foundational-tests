# REL-LATENCY-01-050
- **标题**: 调度延迟基准——queued→running P50/P95 等待时间
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**queued→running 调度延迟基准**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-050
通过标准：
1. P95≤60s
2. P50≤30s

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 5` | - | 短暂运行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | p95_latency_seconds le 60 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
| 2 | p50_latency_seconds le 30 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
---
