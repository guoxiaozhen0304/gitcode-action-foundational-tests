# COMPAT-SCHEDULE-01-003

- 标题: schedule 在非默认分支不触发与 GitHub 差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: schedule 在非默认分支不触发与 GitHub 差异

- [负向] develop 分支的 schedule workflow 不应触发
- [正向] 默认分支的 schedule workflow 正常触发

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo branch | echo "branch=${{ atomgit.ref_name }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status |  |
| positive | run_status |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | schedule |
| 身份 | maintainer |
| 触发阻塞 | 是 (trigger event "schedule" requires platform scheduling) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] develop 分支的 schedule workflow 不应触发 | COVERED | negative assertion present |
| [正向] 默认分支的 schedule workflow 正常触发 | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
