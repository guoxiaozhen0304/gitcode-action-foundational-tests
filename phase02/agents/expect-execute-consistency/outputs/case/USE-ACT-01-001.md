# USE-ACT-01-001
- **标题**: 使用裸插件名 checkout 时正常拉取官方 Action
- **维度**: usability
- **评级**: 断言一致

## 想测什么
`uses: checkout` 短名可正常拉取并执行官方 Action。

## 做了什么
step uses:checkout，step2 `ls -la` 确认 checkout 成功。断言检查 run_status。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals:COMPLETED | COVERED | 平台 run_status 为 GENUINE 来源；step uses checkout + ls 验证 |
