# COMPAT-VARS-01-005
- **标题**: vars 在条件表达式 if 中的可用性差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode vars 在 if 条件表达式中是否正常求值与 GitHub 一致。
## 做了什么
step 的 if 条件使用 `${{ vars.ENABLE_FEATURE == 'true' }}`，触发 workflow 观察条件步骤是否执行。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | llm_assisted 判断条件步骤执行输出feature_enabled | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_logs | negative | llm_assisted 判断vars不应被静默视为空字符串 | LLM_DEPENDENT | eval=llm_assisted |
