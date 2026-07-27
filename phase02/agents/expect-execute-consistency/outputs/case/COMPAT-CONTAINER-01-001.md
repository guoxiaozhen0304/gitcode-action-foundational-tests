# COMPAT-CONTAINER-01-001
- **标题**: container 字段不被支持时应明确报错而非静默忽略
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**系统拒绝 container 字段的 workflow，报错应明确指出 container 字段不被支持**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-001
通过标准：
1. 不通过无指引报错
2. 不通过静默忽略
3. 报错含 container 关键字
4. 报错指向正确行号
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
| 1 | validation_error 无指引报错 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_status 不静默忽略 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | error_message 含 container 关键字 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
