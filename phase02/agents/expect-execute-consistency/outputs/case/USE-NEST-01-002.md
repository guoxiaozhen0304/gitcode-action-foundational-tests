# USE-NEST-01-002  - **标题**: workflow_call 嵌套 2 层时应正常执行   - **维度**: usability   - **评级**: 断言一致

## 想测什么

运行成功完成，无嵌套层数报错；日志包含最内层步骤输出 level2 executed

## 做了什么

- 1. 主 workflow 以 job 级 uses 调用 reusable-level1.yml
- 2. reusable-level1.yml 再以 job 级 uses 调用 reusable-level2.yml
- 3. 触发主 workflow 并观察运行状态与日志

- - [正向] 运行成功完成（run 状态 COMPLETED）
- - [正向] 日志包含 level2 executed（嵌套链路真正执行到最内层）
- - [负向] 不应报嵌套超限错误

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`COMPLETED` | COVERED | run_status: uses:嵌套2层→应正常执行; 包含job-uses→GENUINE |
| 2 | run_logs | positive | contains=`level2 executed` | COVERED | run_logs+contains: 'level2 executed'由被调用workflow真实echo→GENUINE |
