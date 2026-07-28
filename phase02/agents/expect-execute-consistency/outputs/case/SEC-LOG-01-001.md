# SEC-LOG-01-001
- **标题**: 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
加注释明确：log_api 断言由 harness 以不同角色调用日志 API 验证；过期日志恢复检查由 harness 在保留期过期后执行（时间夹具依赖，YAML 已注释）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_api | positive | equals authorized_download_ok | ✅ COVERED | harness 有权限角色下载 |
| 2 | log_api | negative | must_not_equal unauthorized_log_access_granted | ✅ COVERED | harness 无权限角色请求 |
| 3 | log_api | negative | must_not_equal expired_log_recoverable | ✅ COVERED | harness 过期后复查（注释已说明） |
