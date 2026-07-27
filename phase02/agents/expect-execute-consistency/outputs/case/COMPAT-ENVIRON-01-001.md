# COMPAT-ENVIRON-01-001
- **标题**: 含 environment 字段的 job 应被报错或警告
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**平台应在解析或保存阶段给出明确报错或警告，不应被静默接受**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-023
通过标准：
1. 不应被静默接受
2. 报错信息应提示 environment 字段不支持及替代方案
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo hello | `echo "hello"` | — | hello（若解析通过） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message 明确报错或警告 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
