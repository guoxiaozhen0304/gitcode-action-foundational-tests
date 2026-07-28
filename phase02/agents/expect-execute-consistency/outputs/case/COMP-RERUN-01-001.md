# COMP-RERUN-01-001
- **标题**: rerun 后 atomgit.sha 保持原始值 run_number 递增   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | rerun_context | positive | sha_unchanged: True | COVERED | workflow echo ATOMGIT_SHA 等环境变量供 harness 对比 |
| 2 | rerun_context | positive | run_number_increased: True | COVERED | 同上；R1: echo \$var 为 GENUINE |
