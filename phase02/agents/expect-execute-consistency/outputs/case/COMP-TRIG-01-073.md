# COMP-TRIG-01-073
- **标题**: pull_request 事件关键字段与 types 验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: PR_NUM= | COVERED | step echo PR_NUM=\${{ atomgit.event.pull_request.number }} |
| 2 | run_logs | positive | must_contain: pr_ok | COVERED | step echo pr_ok |
| 3 | run_logs | positive | must_contain: type_in_filter | COVERED | step case 语句匹配 open|update|reopen 时 echo type_in_filter |
| 4 | run_logs | negative | must_not_contain: type_out_of_filter | COVERED | step 仅非匹配路径写此值；PR types 限制确保不出现 |
