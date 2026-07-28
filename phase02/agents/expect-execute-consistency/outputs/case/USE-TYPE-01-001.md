# USE-TYPE-01-001  - **标题**: 使用 GitCode types 命名时正常触发   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

PR 事件正常触发 workflow

## 做了什么

- 1. 配置 on: pull_request: types: [open, update, reopen]

- - [正向] PR 创建或更新时触发运行
- - [正向] 运行成功或至少进入执行态

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`COMPLETED` | COVERED | run_status: ${{ atomgit.event_name }}表达式→GENUINE; types:[open,update,reopen]可被dispatch验证 |
