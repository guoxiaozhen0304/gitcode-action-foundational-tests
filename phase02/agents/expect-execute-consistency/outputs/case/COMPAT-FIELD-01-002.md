# COMPAT-FIELD-01-002
- **标题**: 含 services 字段的 job 应被报错或警告
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**含 services 字段的 job 应被报错或警告**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-021
通过标准：
1. 平台应在解析或保存阶段给出明确报错或警告
2. 不应被静默接受且服务未启动
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
| 1 | error_message eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 由 LLM 判定报错信息是否明确提示 services 不支持 |
### 问题
唯一断言为 LLM_DEPENDENT
---
