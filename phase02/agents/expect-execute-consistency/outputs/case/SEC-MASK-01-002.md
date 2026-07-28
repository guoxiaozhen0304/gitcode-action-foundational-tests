# SEC-MASK-01-002
- **标题**: Secret 值在 step summary 和错误堆栈中必须被脱敏
- **维度**: security
- **评级**: 断言一致

## 想测什么
写入 step summary 和故意失败产生堆栈时，secret 值均被脱敏。

## 做了什么
workflow 将 secret 写入 $ATOMGIT_STEP_SUMMARY，再故意 exit 1 产生错误堆栈。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_summary | negative | must_not_contain_secret "API_KEY" | COVERED | 对应"step summary 不含 API_KEY 原值"；platform→GENUINE |
| 2 | error_stack | negative | must_not_contain_secret "API_KEY" | COVERED | 对应"错误堆栈不含 API_KEY 原值"；platform→GENUINE |
