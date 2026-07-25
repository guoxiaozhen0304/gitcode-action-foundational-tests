# REL-FLOOD-01-036

- 标题: 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失

- [正向] 10 个运行均被创建
- [正向] 每个运行有独立 RUN_ID
- [负向] 不应出现运行数<10 或状态混乱

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 5 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | created_runs_count | 10 |
| positive | run_status | completed(success) |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | push |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 10 个运行均被创建 | WEAK | assertions present but all steps trivial |
| [正向] 每个运行有独立 RUN_ID | WEAK | assertions present but all steps trivial |
| [负向] 不应出现运行数<10 或状态混乱 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 10 个运行均被创建: assertions present but all steps trivial
- [正向] 每个运行有独立 RUN_ID: assertions present but all steps trivial
- [负向] 不应出现运行数<10 或状态混乱: single dispatch cannot prove negative

---
