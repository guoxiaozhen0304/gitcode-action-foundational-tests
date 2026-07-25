# COMPAT-PR-01-003

- 标题: PR types 配置后匹配类型不触发与 GitHub 行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: PR types 配置后匹配类型不触发与 GitHub 行为差异

- [负向] 不通过假阴性（PR 更新后没有对应 workflow 运行）
- [正向] 若平台已修复，PR 更新后应触发 workflow 运行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo trigger info | echo "event_name=${{ atomgit.event_name }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status |  |
| positive | run_status | success |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | pull_request |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "pull_request" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 不通过假阴性（PR 更新后没有对应 workflow 运行） | COVERED | negative assertion present |
| [正向] 若平台已修复，PR 更新后应触发 workflow 运行 | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
