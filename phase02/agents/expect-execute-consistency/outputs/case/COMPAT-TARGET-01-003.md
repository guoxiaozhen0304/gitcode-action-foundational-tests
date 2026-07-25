# COMPAT-TARGET-01-003

- 标题: pull_request_target 默认 types 与 GitHub 差异
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: pull_request_target 默认 types 与 GitHub 差异

- [正向] 默认 types 下 PR open 应触发 workflow
- [正向] 默认 types 下 PR synchronize 应触发 workflow

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo trigger info | echo "event_name=${{ atomgit.event_name }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status |  |
| positive | run_status |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | pull_request_target |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "pull_request_target" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 默认 types 下 PR open 应触发 workflow | COVERED | 1 real steps, assertions present |
| [正向] 默认 types 下 PR synchronize 应触发 workflow | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
