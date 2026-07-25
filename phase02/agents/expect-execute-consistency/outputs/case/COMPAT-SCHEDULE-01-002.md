# COMPAT-SCHEDULE-01-002

- 标题: schedule 不支持 timezone 字段差异
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: schedule 不支持 timezone 字段差异

- [负向] 不应因 timezone 字段导致不可预期的行为
- [正向] 错误信息应明确指出 timezone 字段不支持或文档说明忽略策略

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo schedule | echo "SCHEDULE_TIMEZONE_OK" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status | success |
| nonfunctional | error_message |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | schedule |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "schedule" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 不应因 timezone 字段导致不可预期的行为 | COVERED | negative assertion present |
| [正向] 错误信息应明确指出 timezone 字段不支持或文档说明忽略策略 | NOT COVERED | no real steps, no assertions |

### 问题

- [正向] 错误信息应明确指出 timezone 字段不支持或文档说明忽略策略: no real steps, no assertions

---
