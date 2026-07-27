# COMPAT-CACHE-01-001
- **标题**: cache 行为等价性——缓存命中场景
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**第二次运行时 cache 步骤识别到已有缓存并命中，直接恢复缓存目录内容**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-025
通过标准：
1. 第二次运行日志中出现缓存命中标识
2. 缓存目录内容正确恢复
3. 不应因 key 匹配而实际未恢复内容
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | restore cache | `uses: cache with: key: ...${{ atomgit.run_id }}` | — | 缓存恢复 |
| 2 | verify cache state | `if [ -f ... ] echo CACHE_HIT else CACHE_MISS; mkdir; echo marker` | — | CACHE_HIT 或 CACHE_MISS |
| 3 | save cache | `uses: cache with: key` | if: ${{ always() }} | 缓存保存 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs CACHE_HIT | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_logs 持久化失败/key 冲突 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
