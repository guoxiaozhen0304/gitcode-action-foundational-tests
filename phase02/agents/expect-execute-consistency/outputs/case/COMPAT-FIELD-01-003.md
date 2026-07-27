# COMPAT-FIELD-01-003
- **标题**: 未知顶层字段不应被静默忽略而应给出警告
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**未知顶层字段不应被静默忽略而应给出警告**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-021
通过标准：
1. 系统不应静默忽略未知字段
2. 应给出警告或错误
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo hello | `echo "hello"` | — | "hello" |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 由 LLM 判定是否静默忽略 |
| 2 | error_message eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 由 LLM 判定警告/错误是否有用 |
### 问题
全部断言均为 LLM_DEPENDENT
---
