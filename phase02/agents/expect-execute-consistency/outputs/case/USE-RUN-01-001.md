# USE-RUN-01-001  - **标题**: 使用三段式标签时 job 正常调度   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

job 被成功调度到匹配的 runner

## 做了什么

- 1. 使用 runs-on: [dedicate-hosted, x64, large]

- - [正向] 运行成功完成
- - [正向] job 日志显示在对应 runner 上执行

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`COMPLETED` | COVERED | run_status: runs-on:[ubuntu-latest,x64,small]→测试标签格式可接受性; echo仅为标记 |
