# COMPAT-ISOLATE-01-001

- **标题**: Runner 环境隔离——跨 job 文件隔离   - **维度**: 兼容性   - **评级**: 断言一致

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive |  | COVERED |  |
| 2 | run_logs | positive |  | COVERED |  |
| 3 | run_logs | negative | ISOLATION_BROKEN_WORKSPACE | COVERED |  |
| 4 | run_logs | negative | ISOLATION_BROKEN_TMP | COVERED |  |

