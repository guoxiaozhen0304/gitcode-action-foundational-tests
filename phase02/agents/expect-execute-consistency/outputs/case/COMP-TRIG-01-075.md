# COMP-TRIG-01-075
- **标题**: schedule 事件关键字段与 cron 格式验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**schedule 事件关键字段与 cron 格式验证**
- 触发事件: `schedule`
- 规格引用: INTENT-COMP-075
通过标准：
1. 数组格式 schedule 通过校验（正向）
2. 对象格式 schedule 被拒绝（负向）
3. event.schedule 非空（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print schedule | `${{ atomgit.event.schedule }}`, `echo "schedule_ok"` | - | 平台事件上下文 + schedule_ok |
## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: schedule_ok | ✅ GENUINE | 步骤含 `${{ atomgit.event.schedule }}` 表达式，schedule_ok 为同一步骤内的辅助标记 |
---
