# COMP-TRIG-01-076
- **标题**: issue_comment 事件关键字段与 types 验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: COMMENT_ID= | COVERED | step echo COMMENT_ID=\${{ atomgit.event.comment.id }} |
| 2 | run_logs | positive | must_contain: issue_comment_ok | COVERED | step echo issue_comment_ok |
