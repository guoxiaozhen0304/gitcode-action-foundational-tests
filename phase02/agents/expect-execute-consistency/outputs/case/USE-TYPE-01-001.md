# USE-TYPE-01-001
- **标题**: 使用 GitCode types 命名时正常触发
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证在 pull_request 事件中使用 GitCode types 命名 [open, update, reopen] 时 workflow 可正常触发并执行。

## 做了什么
workflow 监听 `on: pull_request: types: [open, update, reopen]`，step echo `${{ atomgit.event_name }}`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功完成 | COVERED | 平台事件触发与调度行为 → GENUINE |
