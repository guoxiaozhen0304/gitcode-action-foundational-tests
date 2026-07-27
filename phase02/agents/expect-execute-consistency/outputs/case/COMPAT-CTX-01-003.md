# COMPAT-CTX-01-003
- **标题**: github 上下文嵌套属性访问应报错而非返回空
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**嵌套属性访问不导致 workflow 崩溃，返回值与 GitHub 行为一致**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-016
通过标准：
1. 嵌套属性访问不导致 workflow 崩溃
2. 返回值与 GitHub 行为一致
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Access nested github property | `echo "pr_number=${{ github.event.pull_request.number }}"` | — | pr_number=（空或报错） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=success | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_logs 与 GitHub 一致 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
