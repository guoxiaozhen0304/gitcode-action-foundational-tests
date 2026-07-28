# COMPAT-VARS-01-002
- **标题**: vars 上下文若不支持应报错而非静默为空
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ vars.UNKNOWN_VAR }}` 在vars不支持或变量不存在时不应静默求值为空字符串。

## 做了什么
workflow_dispatch触发，variables为空 `{}`，step输出 `echo "unknown_var=${{ vars.UNKNOWN_VAR }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative llm | "unknown_var不应仅等于空字符串后静默通过" | COVERED | ${{ vars.UNKNOWN_VAR }}为GENUINE(R1上下文表达式)；若为空串且静默通过则断言触发 |
| 2 | error_message | nonfunctional llm | "若不支持vars，报错应说明不可用" | COVERED | error_message为平台日志(GENUINE R1)；R5 LLM_DEPENDENT辅助判断报错内容 |
