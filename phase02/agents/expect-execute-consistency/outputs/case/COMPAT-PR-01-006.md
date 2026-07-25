# COMPAT-PR-01-006

- 标题: PR 目标分支过滤行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: PR 目标分支过滤行为差异

- [正向] 目标分支为 main 的 PR 应触发 workflow
- [负向] 目标分支为 develop 的 PR 不应触发 workflow

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo trigger info | echo "event_name=${{ atomgit.event_name }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
| negative | run_status |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | pull_request |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "pull_request" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 目标分支为 main 的 PR 应触发 workflow | COVERED | 1 real steps, assertions present |
| [负向] 目标分支为 develop 的 PR 不应触发 workflow | COVERED | negative assertion present |

### 问题

无重大问题。

---
