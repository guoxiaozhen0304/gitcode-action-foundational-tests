# COMP-UNKNOWN-01-003
- **标题**: 未声明 select 的 stage 与 job 默认被执行   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
验证未声明 select 字段的 job 默认执行，不因缺省 select 而被跳过。
## 做了什么
workflow_dispatch 触发单个 job，step 中 echo `NO_SELECT_JOB_RAN` 作为标记，同时 echo `RUN_ID=${{ atomgit.run_id }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success | GENUINE→COVERED | 无可失败步骤，正常运行即成功 |
| 2 | run_logs | positive | must_contain: NO_SELECT_JOB_RAN | GENUINE→COVERED | 步骤中有 `${{ atomgit.run_id }}` 引用，按 R6 视为 GENUINE；标记词由步骤 echo 产生 |
