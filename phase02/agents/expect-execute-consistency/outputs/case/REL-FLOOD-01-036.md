# REL-FLOOD-01-036
- **标题**: 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**10 个并发 push 应全部创建 run**
- 触发事件: `push`
- 规格引用: INTENT-REL-036
通过标准：
1. 10 个运行均被创建
2. 每个运行有独立 RUN_ID
3. 10 个运行全部 completed

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 5` | - | 保持 job 运行一段时间 |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count = 10 | positive | - | ✅ GENUINE | sleep 是真实命令；harness 并发 push 10 次 + 数 run |
| 2 | run_status = completed(success) | positive | - | ✅ GENUINE | 所有 run 应通过真实 sleep + exit 0 完成 |
---
