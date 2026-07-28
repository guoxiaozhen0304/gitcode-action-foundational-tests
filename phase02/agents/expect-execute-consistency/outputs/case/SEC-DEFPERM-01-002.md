# SEC-DEFPERM-01-002
- **标题**: job 级覆盖后权限正确收窄
- **维度**: security
- **评级**: 断言一致

## 想测什么
顶层 repository: write，job 级覆盖为 read 后写操作被拒。

## 做了什么
workflow 顶层写权限，job 覆盖为 read 后尝试 POST 写 API；判 HTTP 码。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "WRITE_201" | COVERED | 对应"job 级收窄后写操作绝不应成功"；real curl→GENUINE |
| 2 | run_logs | positive | contains "WRITE_403" | COVERED | 对应"越权写被拒"；real curl→GENUINE |
