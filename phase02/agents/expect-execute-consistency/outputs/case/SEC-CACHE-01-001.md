# SEC-CACHE-01-001
- **标题**: fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**主仓 workflow 不能命中 fork PR 写入的 cache 键**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-018
通过标准：
1. cache_restore 不命中 fork_cache_key
2. run_status 为 completed
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write cache | `uses: cache` with path=./node_modules, key=test-cache-key | — | cache 写入 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-cache |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore 不命中 fork cache | negative | must_not_hit "fork_cache_key" | ❌ MISSING_SOURCE | target=cache_restore 是平台缓存接口，workflow 步骤仅写入 cache，无 restore 操作；无法验证 restore 行为 |
| 2 | run_status completed | positive | run_status equals "completed" | ⚠️ STATUS_GUARANTEED | 步骤仅 uses: cache（无 if/${{ }}），cache 写入成功则状态必然 success |
### 问题
断言 1 MISSING_SOURCE：target 为 cache_restore（读取操作），但 workflow 仅执行写入。断言 2 价值有限。
---
