# COMPAT-VARS-01-004
- **标题**: vars 与 env 同名时的优先级差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode vars 与 env 同名时，env 优先级高于 vars（与 GitHub 行为一致）。
## 做了什么
同时定义 `env.MY_VAR=env_value` 和 `${{ vars.MY_VAR }}`，输出 `$MY_VAR` 和表达式值。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | llm_assisted 判断shell_var=env_value | LLM_DEPENDENT | eval=llm_assisted，需人工确认 env 优先级 |
| 2 | run_logs | positive | llm_assisted 判断expr_var=var_value | LLM_DEPENDENT | eval=llm_assisted，需人工确认 vars 仍可访问 |
