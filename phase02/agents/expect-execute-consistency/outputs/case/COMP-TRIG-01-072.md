# COMP-TRIG-01-072
- **标题**: push 事件关键字段与过滤验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: REF=refs/ | COVERED | step echo REF=\${{ atomgit.event.ref }} |
| 2 | run_logs | positive | must_contain: BEFORE= | COVERED | step echo BEFORE=\${{ atomgit.event.before }} |
| 3 | run_logs | positive | must_contain: push_ok | COVERED | step echo push_ok |
