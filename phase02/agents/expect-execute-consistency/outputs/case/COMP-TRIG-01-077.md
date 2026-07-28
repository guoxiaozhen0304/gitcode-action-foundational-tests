# COMP-TRIG-01-077
- **标题**: pull_request_comment 事件关键字段与过滤验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: PR_NUM= | COVERED | step echo PR_NUM=\${{ atomgit.event.pull_request.number }} |
| 2 | run_logs | positive | must_contain: pr_comment_ok | COVERED | step echo pr_comment_ok |
