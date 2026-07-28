# COMPAT-EXPR-01-012

- **标题**: fromJSON() 函数缺失时的降级行为   - **维度**: 兼容性   - **评级**: 部分不符

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | fromjson-result=1 | VACUOUS | must_not_contain 'fromjson-result=1' but no step produces this string |
| 2 | error_message | nonfunctional |  | COVERED |  |

