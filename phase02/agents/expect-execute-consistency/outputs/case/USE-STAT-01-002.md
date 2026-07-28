# USE-STAT-01-002  - **标题**: 使用 success() 带括号时报错应提示 GitCode 括号差异   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

YAML 校验或表达式求值报错，提示 GitCode 状态函数不带括号

## 做了什么

- 1. 在 step 中使用 if: ${{ success() }}

- - [负向] 不应静默通过校验
- - [非功能] 报错中应包含括号差异提示

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: if:${{ success() }}→平台拒绝括号写法; 状态可观察 |
| 2 | error_message | positive | must_contain=`success` | COVERED | error_message+must_contain: 错误信息可验证 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 括号差异提示质量需LLM评估 |
