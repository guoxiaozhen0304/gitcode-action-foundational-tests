# COMPAT-VARS-01-004
- **标题**: vars 与 env 同名时的优先级差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证同名变量时env优先级高于vars——$MY_VAR返回env_value，而${{ vars.MY_VAR }}返回var_value。

## 做了什么
setup配置 `variables: {MY_VAR: var_value}`，workflow顶层 `env: {MY_VAR: env_value}`，step输出 `echo "shell_var=$MY_VAR"` + `echo "expr_var=${{ vars.MY_VAR }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive llm | "shell_var应返回env_value(env优先级高于vars)" | COVERED | $MY_VAR为env环境变量(GENUINE R1)；${{ vars.MY_VAR }}为GENUINE上下文表达式 |
| 2 | run_logs | positive llm | "expr_var应返回var_value" | COVERED | ${{ vars.MY_VAR }}为GENUINE(R1)，直接引用vars上下文不受env影响 |
