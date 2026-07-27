# COMPAT-PR-01-002
- **标题**: pull_request types 命名差异 - GitHub 风格 types 应报错
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request types 命名差异 - GitHub 风格 types 应报错**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-011
通过标准：
1. 平台应对不支持的 GitHub 风格 types 给出明确的校验错误
2. 错误信息应提示正确的 GitCode types 名称
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo PR event | `echo "PR_EVENT_TYPE=${{ atomgit.event.action }}"` 后 `echo "PR_TYPES_OK"` | — | PR_EVENT_TYPE=<action>, PR_TYPES_OK |
## 3. 触发与运行环境
| 触发事件 | pull_request (types: opened, closed, reopened — GitHub style) |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | negative | — | ✅ GENUINE | GitHub 风格 types (opened/closed/reopened) 不应被静默接受，若平台拒绝则 run_status 不为 success |
| 2 | error_message eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 错误信息质量由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过；断言1 为 GENUINE
---
