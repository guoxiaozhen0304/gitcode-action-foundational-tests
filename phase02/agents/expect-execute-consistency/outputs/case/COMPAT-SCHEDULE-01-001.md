# COMPAT-SCHEDULE-01-001

- 标题: schedule cron 按 UTC 时间触发
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: schedule cron 按 UTC 时间触发

- [正向] schedule 事件能正常触发 workflow
- [非功能] 触发时间应与 UTC 解释一致

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo schedule time | echo "SCHEDULE_TRIGGER_OK" echo "Current UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
| positive | run_event | schedule |
| nonfunctional | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | schedule |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "schedule" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] schedule 事件能正常触发 workflow | COVERED | 1 real steps, assertions present |
| [非功能] 触发时间应与 UTC 解释一致 | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
