# COMPAT-CONCUR-01-003
- **标题**: concurrency preemption enable 行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**系统接受或拒绝 preemption 配置时应给出明确提示**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-005
通过标准：
1. 系统接受或拒绝 preemption 配置时给出明确提示
2. 不通过 preemption 配置被静默忽略
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Sleep and echo | `sleep 30; echo "done"` | — | done |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message 明确提示 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_status 不静默忽略 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
