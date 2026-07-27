# COMPAT-ENVIRON-01-002
- **标题**: environment 字段绑定 secrets 的行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**environment 字段不被识别，环境 secrets 不可用，应明确报错或警告**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-023
通过标准：
1. 不通过 environment 字段被静默忽略
2. 系统对 environment 字段给出明确报错或警告
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo env secret | `echo "env_secret=${{ secrets.ENV_SECRET }}"` | — | env_secret=（若解析通过） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status 不静默忽略 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 明确报错或警告 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
