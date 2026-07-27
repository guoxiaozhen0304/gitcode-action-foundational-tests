# COMPAT-ACTIONDEV-01-001
- **标题**: action.yml 元数据校验与 GitHub 差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**GitCode 对 action.yml 的校验规则可能与 GitHub 不同，不支持的字段应不导致 workflow 失败**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-010
通过标准：
1. 不支持的 action.yml 字段不导致 workflow 失败
2. 系统给出明确提示说明不支持的字段
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout action repo | `uses: checkout` | — | 检出 action 仓库 |
| 2 | Use local action | `uses: ./.github/actions/my-action` | — | 加载本地 action |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status 不因不支持字段失败 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 明确提示 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
