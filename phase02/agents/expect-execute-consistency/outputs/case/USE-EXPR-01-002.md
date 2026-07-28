# USE-EXPR-01-002  - **标题**: 调用未知函数时报错应提示函数名错误与修正方向   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

报错指出未知函数，并建议检查函数名拼写

## 做了什么

- 1. 在 if 条件中使用 ${{ unknownFunc() }}

- - [负向] 不应静默通过
- - [非功能] 报错中是否包含 unknownFunc 或未知函数字样

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: if: ${{ unknownFunc() }}真实表达式求值→应失败 |
| 2 | error_message | positive | must_contain=`unknownFunc` | COVERED | error_message+must_contain: 错误信息从平台日志获取 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错文案质量需LLM评估 |
