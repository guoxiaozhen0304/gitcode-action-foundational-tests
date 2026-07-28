# COMP-STAGES-01-003
- **标题**: post.run_always true 时 workflow 失败仍执行 post   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals: failure | COVERED | 主 job exit 1 |
| 2 | post_logs | positive | contains: post executed | COVERED | post step echo 'post executed'，run_always=true |
