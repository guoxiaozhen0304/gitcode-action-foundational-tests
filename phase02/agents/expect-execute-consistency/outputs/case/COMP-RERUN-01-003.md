# COMP-RERUN-01-003
- **标题**: 超过 6 小时的运行不可 rerun
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**超过 6 小时的运行不可 rerun**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-009
通过标准：
1. 超 6h 的运行的 rerun 不应成功（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo | `echo "run"` | - | run |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_result | negative | equals: rerun_of_6h_plus_run | ✅ GENUINE | 平台 rerun 时效限制由 harness 验证——超过 6 小时的运行的 rerun 不应成功 |
---
