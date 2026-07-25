# COMPAT-PR-01-002

- 标题: pull_request types 命名差异 - GitHub 风格 types 应报错
- 维度: 兼容性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: pull_request types 命名差异 - GitHub 风格 types 应报错

- [负向] GitHub 风格 types 不应被静默接受
- [正向] 错误信息应明确指出类型名称不兼容并给出正确写法

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo PR event | echo "PR_EVENT_TYPE=${{ atomgit.event.action }}" echo "PR_TYPES_OK" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status | success |
| nonfunctional | error_message |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | pull_request |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "pull_request" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] GitHub 风格 types 不应被静默接受 | COVERED | negative assertion present |
| [正向] 错误信息应明确指出类型名称不兼容并给出正确写法 | WEAK | 1 real steps but no assertions |

### 问题

- [正向] 错误信息应明确指出类型名称不兼容并给出正确写法: 1 real steps but no assertions

---
