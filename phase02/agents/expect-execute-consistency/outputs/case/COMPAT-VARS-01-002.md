# COMPAT-VARS-01-002
- **标题**: vars 上下文若不支持应报错而非静默为空
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode vars 上下文不支持时在解析或运行时给出明确报错，而非将 `vars.UNKNOWN_VAR` 静默求值为空字符串。
## 做了什么
在 workflow 中输出 `${{ vars.UNKNOWN_VAR }}`，观察运行结果。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | llm_assisted 判断不应静默求值为空 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | error_message | nonfunctional | llm_assisted 判断报错说明vars不可用 | LLM_DEPENDENT | type=nonfunctional，文档化建议任务 |
