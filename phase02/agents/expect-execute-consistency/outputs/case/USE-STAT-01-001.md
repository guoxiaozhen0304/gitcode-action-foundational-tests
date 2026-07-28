# USE-STAT-01-001  - **标题**: 使用 always() 带括号时若被接受则正常执行   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

该 step 无论上游成败均执行

## 做了什么

- 1. 在 step 中使用 if: ${{ always() }}

- - [正向] step 日志出现执行记录
- - [正向] 运行成功完成

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=`cleanup executed` | COVERED | run_logs+contains: exit 1→真实失败; if:${{ always() }}→表达式求值→cleanup步骤执行→GENUINE |
