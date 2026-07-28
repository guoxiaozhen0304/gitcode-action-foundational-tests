# COMPAT-WCMD-01-005
- **标题**: debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
确认 GitCode `::debug::` 命令在无门控配置时的默认可见性，与 GitHub 的 ACTIONS_STEP_DEBUG 门控对比。
## 做了什么
输出 `::debug::demo debug message`，观察在默认配置下该消息在日志中是否可见。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain=DEBUG_PROBE_DONE | COVERED | 工作流固定输出标志字符串 |
| 2 | run_logs | positive | llm_assisted 判断debug消息默认可见性确定 | LLM_DEPENDENT | eval=llm_assisted，需人工观察debug消息是否可见 |
