# COMP-SCHEDULE-01-003
- **标题**: cron 间隔短于 5 分钟时被拒绝或降级
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**cron 间隔短于 5 分钟时被拒绝或降级**
- 触发事件: `schedule`
- 规格引用: INTENT-COMP-005
通过标准：
1. 不应允许每分钟触发的 schedule（负向）
2. 错误信息应说明最短间隔限制（非功能）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo scheduled | `echo "should not run"` | - | should not run |
## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success_with_1min_interval | ✅ GENUINE | cron "*/1 * * * *" 间隔 1 分钟，平台应拒绝此配置，run 不应以 1min 间隔成功 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估错误信息是否说明最短间隔 5 分钟 |
---
