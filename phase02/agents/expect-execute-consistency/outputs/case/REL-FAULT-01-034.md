# REL-FAULT-01-034
- **标题**: 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**cache 服务 503 时应优雅降级为 cache miss 不阻断 job**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-034
通过标准：
1. cache step 标记为 miss 或跳过
2. 后续 step 正常执行
3. job 不应整体 failure

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | restore cache step | `uses: cache` path=node_modules | - | cache action 输出（含 cache miss） |
| 2 | subsequent step | `echo subsequent step executed` | - | 确认后续执行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | cache service 503 at step 1 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | - | ✅ GENUINE | cache 服务 503 时平台优雅降级，后续步骤不受影响 |
| 2 | run_logs contains "cache miss" | positive | - | ✅ GENUINE | cache action 内部输出 "cache miss" |
---
