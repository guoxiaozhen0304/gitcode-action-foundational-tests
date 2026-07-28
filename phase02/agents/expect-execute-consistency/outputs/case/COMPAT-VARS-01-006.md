# COMPAT-VARS-01-006
- **标题**: vars 在 Action 中的可用性差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode vars 在 Action 的 with 参数中是否正常求值，与 GitHub 行为一致。
## 做了什么
在 checkout Action 的 with.ref 参数中引用 `${{ vars.ACTION_VAR }}`，触发 workflow。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | llm_assisted 判断Action的with参数正确接收值 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_logs | negative | llm_assisted 判断vars不应被静默视为空字符串 | LLM_DEPENDENT | eval=llm_assisted |
