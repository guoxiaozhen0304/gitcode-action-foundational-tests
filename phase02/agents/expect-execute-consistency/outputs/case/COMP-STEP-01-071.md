# COMP-STEP-01-071
- **标题**: step 执行控制 shell working-directory continue-on-error timeout-minutes 验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: success | COVERED | continue-on-error 使 exit 1 不阻止 job |
| 2 | run_logs | positive | must_contain: bash_ok | COVERED | bash shell step echo bash_ok |
| 3 | run_logs | positive | must_contain: sh_ok | COVERED | sh shell step echo sh_ok |
| 4 | run_logs | positive | must_contain: PWD_NOW=/tmp | COVERED | working-directory: /tmp 下 echo PWD_NOW=\$(pwd) |
| 5 | run_logs | positive | must_contain: before_fail | COVERED | continue-on-error step echo before_fail |
| 6 | run_logs | positive | must_contain: continue_ok | COVERED | step echo continue_ok（失败后继续执行） |
