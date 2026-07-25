# COMPAT-PR-01-001

- 标题: pull_request types 命名差异 - GitCode 合法 types 应被接受
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: pull_request types 命名差异 - GitCode 合法 types 应被接受

- [正向] workflow 校验通过
- [正向] 指定 types 的 PR 事件能正常触发 workflow

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo PR event | echo "PR_EVENT_TYPE=${{ atomgit.event.action }}" echo "PR_TYPES_OK" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
| positive | run_logs | PR_TYPES_OK |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | pull_request |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "pull_request" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] workflow 校验通过 | COVERED | 1 real steps, assertions present |
| [正向] 指定 types 的 PR 事件能正常触发 workflow | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
