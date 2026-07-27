# REL-CPU-01-022
- **标题**: Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**CPU 饱和时 job 应完成但耗时延长**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-022
通过标准：
1. job 状态=success
2. 总耗时 120±24 秒
3. 不应被强制终止

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | burn 4 CPU processes | `for i in 1 2 3 4; do python3 -c "..." & done; wait` | - | 4 个并行 CPU 密集型进程 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | - | ✅ GENUINE | python3 真实 CPU burn 进程 |
| 2 | job_duration_seconds ge 96 le 144 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
---
