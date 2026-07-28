# COMPAT-VARS-01-001
- **标题**: vars 上下文若支持应正确返回值
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ vars.TEST_VAR }}` 在vars上下文可用时返回配置值hello_vars。

## 做了什么
workflow_dispatch触发，setup中配置 `variables: {TEST_VAR: hello_vars}`，step输出 `echo "test_var=${{ vars.TEST_VAR }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success | workflow成功 | COVERED | run_status平台可观测 |
| 2 | run_logs | positive llm | "test_var应包含hello_vars" | COVERED | ${{ vars.TEST_VAR }}为GENUINE(R1上下文表达式)；GGI |
