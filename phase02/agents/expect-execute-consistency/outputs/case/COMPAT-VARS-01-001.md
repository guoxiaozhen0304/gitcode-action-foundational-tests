# COMPAT-VARS-01-001
- **标题**: vars 上下文若支持应正确返回值
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode vars 上下文如果支持，`vars.TEST_VAR` 应正确返回配置值。
## 做了什么
在 workflow 中输出 `${{ vars.TEST_VAR }}`，触发后检查日志。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=success | COVERED | 标准运行状态检查 |
| 2 | run_logs | positive | llm_assisted 判断test_var=hello_vars | LLM_DEPENDENT | eval=llm_assisted，需人工确认值 |
