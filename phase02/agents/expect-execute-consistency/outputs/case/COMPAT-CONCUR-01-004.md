# COMPAT-CONCUR-01-004
- **标题**: concurrency preemption events 越界时行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**系统对 events 越界值（11）给出明确报错，包含有效范围提示**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-005
通过标准：
1. 系统对越界值给出明确报错
2. 报错包含有效范围提示
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo hello | `echo "hello"` | — | hello |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message events 越界报错 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 范围提示 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
