# SEC-LOG-01-001
- **标题**: 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
有权限成员可查看下载日志，无权限角色请求返回403/404，过期日志不可恢复。
## 做了什么
YAML workflow仅包含echo步骤产生日志。所有断言target log_api，依赖harness以不同角色调用日志API验证权限。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | log_api | positive | equals "authorized_download_ok" | COVERED | 有权限下载可观测，依赖harness角色切换 |
| 2 | log_api | negative | must_not_equal "unauthorized_log_access_granted" | COVERED | 无权限角色请求结果可观测 |
| 3 | log_api | negative | must_not_equal "expired_log_recoverable" | UNVERIFIABLE | 过期日志恢复判定依赖平台保留期策略，非workflow步骤可验证 |
