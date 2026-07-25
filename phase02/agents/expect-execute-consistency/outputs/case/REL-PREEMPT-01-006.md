# REL-PREEMPT-01-006

- 标题: preemption events 越界值——配置 11 个应被拒绝
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: preemption events 越界值——配置 11 个应被拒绝

- [正向] 明确报错
- [负向] 不应静默截断

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo step | echo test | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | yaml_validation | rejected |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 明确报错 | WEAK | assertions present but all steps trivial |
| [负向] 不应静默截断 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 明确报错: assertions present but all steps trivial
- [负向] 不应静默截断: single dispatch cannot prove negative

---
