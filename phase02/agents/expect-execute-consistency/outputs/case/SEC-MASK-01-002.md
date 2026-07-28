# SEC-MASK-01-002
- **标题**: Secret 值在 step summary 和错误堆栈中必须被脱敏   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
step summary和错误堆栈中API_KEY原值必须被脱敏替换为***。
## 做了什么
YAML workflow中step将secret写入$ATOMGIT_STEP_SUMMARY后intentionally fail(exit 1)产生错误堆栈。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | step_summary | negative | must_not_contain_secret "API_KEY" | COVERED | step summary为可访问的workflow产物 |
| 2 | error_stack | negative | must_not_contain_secret "API_KEY" | COVERED | 错误堆栈为可观测的job输出 |
