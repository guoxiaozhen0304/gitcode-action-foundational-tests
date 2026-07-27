# REL-CONC-01-001
- **标题**: concurrency.max=5 时同时触发 5 个运行应全部进入执行态
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**concurrency.max=5 时 5 个运行全部进入执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-001
通过标准：
1. 5 个运行状态均为 completed(success)
2. queued→in_progress ≤60s

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 10` | concurrency max=5 exceed-action=QUEUE | 短暂运行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = completed(success) | positive | - | ✅ GENUINE | sleep 是真实命令；concurrency max=5 是真实平台功能 |
| 2 | queued_to_running_latency le 60s | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
---
