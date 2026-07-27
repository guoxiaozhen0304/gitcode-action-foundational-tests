# COMPAT-PR-01-003
- **标题**: PR types 配置后匹配类型不触发与 GitHub 行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**PR types 配置后匹配类型不触发与 GitHub 行为差异**
- 触发事件: `pull_request` (types: open, reopen, update)
- 规格引用: INTENT-COMPAT-NEW-003
通过标准：
1. PR 更新后应有对应 workflow 运行
2. 差异应被记录
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo trigger info | `echo "event_name=${{ atomgit.event_name }}"` 后 `echo "done"` | — | event_name 和 done |
## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 假阴性判定由 LLM 判定 |
| 2 | run_status equals success (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | 修复后行为由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
