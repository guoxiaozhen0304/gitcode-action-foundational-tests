# COMP-SCHEDULE-01-001
- **标题**: 合法 cron 在默认分支按时触发
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**合法 cron 在默认分支按时触发**
- 触发事件: `schedule`
- 规格引用: INTENT-COMP-005
通过标准：
1. 运行记录存在且 event 为 schedule（正向）
2. 触发时间与 cron 预期 UTC 时间一致（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo scheduled | `echo "scheduled run"` | - | scheduled run |
## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 所有步骤仅 echo 字面量，无 if/uses/${{ }}/实质命令，run_status=success 为必然结果 |
| 2 | run_event | positive | equals: schedule | ✅ GENUINE | trigger.event 为 schedule，与断言一致 |
### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅 echo 字面量，无条件失败路径，运行永远成功，测试无区分能力。
---
