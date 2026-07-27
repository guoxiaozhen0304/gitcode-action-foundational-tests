# COMPAT-CACHE-01-002
- **标题**: cache 行为等价性——fork PR 写隔离
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**fork PR 不应覆盖或污染主干分支的缓存条目，系统应为 fork 提供独立的缓存命名空间或阻止写入**
- 触发事件: `pr`
- 规格引用: INTENT-COMPAT-025
通过标准：
1. fork PR 不应成功覆盖主干缓存
2. 主干缓存保持完整未被污染
3. 系统提供明确的缓存隔离机制
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | restore cache | `uses: cache with: key: compat-cache-fork-test` | — | 缓存恢复 |
| 2 | attempt write from fork | `mkdir; echo "FORK_MARKER_..." > file; echo "FORK_WRITE_ATTEMPTED"` | — | FORK_WRITE_ATTEMPTED |
| 3 | save cache | `uses: cache with: key` | if: ${{ always() }} | 缓存保存 |
## 3. 触发与运行环境
| 触发事件 | pr |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-fork-pr |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs 不应覆盖主干缓存 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_logs 缓存隔离/拒绝写入标识 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_status=leaked_cache_to_fork | negative | — | ❌ IMPOSSIBLE | "leaked_cache_to_fork" 不是合法 run_status 值，断言恒为真，无法验证任何行为 |
### 问题
第三个断言（run_status=leaked_cache_to_fork, negative）使用了不存在的 run_status 值，导致断言无条件成立，无法验证缓存隔离是否生效。
---
