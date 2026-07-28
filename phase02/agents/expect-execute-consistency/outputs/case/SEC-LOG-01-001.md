# SEC-LOG-01-001
- **标题**: 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复
- **维度**: security
- **评级**: 断言一致

## 想测什么
有权限成员可下载日志；无权限角色被拒；过期日志不可恢复。

## 做了什么
workflow 产生日志内容；harness 以不同角色调用 log_api 验证权限控制。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_api | positive | equals "authorized_download_ok" | COVERED | 对应"有权限成员可查看/下载日志"；harness→GENUINE |
| 2 | log_api | negative | must_not_equal "unauthorized_log_access_granted" | COVERED | 对应"无权限角色绝不应读取或下载日志"；harness→GENUINE |
| 3 | log_api | negative | must_not_equal "expired_log_recoverable" | COVERED | 对应"过期日志绝不应可恢复"；harness→GENUINE |
