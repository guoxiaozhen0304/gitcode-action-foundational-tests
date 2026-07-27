# SEC-CACHE-01-002
- **标题**: 主仓 cache restore 对 fork cache miss
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**主仓读取与 fork PR 相同的 cache key 时返回 miss**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-018
通过标准：
1. cache_restore 不命中 fork cache
2. 日志显示 cache_miss
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Restore cache | `uses: cache` with path=./node_modules, key=test-cache-key | — | cache restore 结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-cache |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore 不命中 fork cache | negative | must_not_hit "fork_cache_key" | ❌ MISSING_SOURCE | target=cache_restore 为平台接口，非 run_logs/run_status，workflow 无对应输出 |
| 2 | 日志显示 cache_miss | positive | run_logs equals "cache_miss" | ✅ GENUINE | uses: cache 是真实 action，其输出依赖平台缓存隔离行为；$NEVER_VACUOUS |
### 问题
断言 1 MISSING_SOURCE：target 为外部缓存接口而非 run_logs。
---
