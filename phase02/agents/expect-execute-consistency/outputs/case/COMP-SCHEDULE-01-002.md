# COMP-SCHEDULE-01-002
- **标题**: 非默认分支的 schedule workflow 不应触发
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**非默认分支的 schedule workflow 不应触发**
- 触发事件: `schedule`
- 规格引用: INTENT-COMP-005
通过标准：
1. 运行列表中不存在该 schedule 触发的运行（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo scheduled | `echo "should not run"` | - | should not run |
## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | multi-branch |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | negative | equals: no_run_on_non_default_branch | ✅ GENUINE | 平台 schedule 仅在默认分支生效的规则由 harness 验证——非默认分支不应创建 run |
---
