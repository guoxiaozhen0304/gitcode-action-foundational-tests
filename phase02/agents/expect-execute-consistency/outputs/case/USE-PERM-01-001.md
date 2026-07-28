# USE-PERM-01-001  - **标题**: 使用 GitCode 权限域命名时正常生效   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

权限声明被正确解析，运行成功

## 做了什么

- 1. 在 workflow 中使用 permissions: repository: read

- - [正向] 运行成功完成
- - [正向] 权限声明未导致校验失败

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`COMPLETED` | COVERED | run_status: uses:checkout→真实action→GENUINE; 测试permissions:repository解析 |
