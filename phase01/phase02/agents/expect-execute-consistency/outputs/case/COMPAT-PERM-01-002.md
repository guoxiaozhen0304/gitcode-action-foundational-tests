# COMPAT-PERM-01-002

- **标题**: 未声明 permissions 时 fork PR 写操作隔离   - **维度**: 兼容性   - **评级**: 完全不符

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative |  | UNVERIFIABLE | trigger event 'fork_pr' not in workflow on events ['workflow_dispatch'] |
| 2 | run_logs | negative |  | UNVERIFIABLE | trigger event 'fork_pr' not in workflow on events ['workflow_dispatch'] |

