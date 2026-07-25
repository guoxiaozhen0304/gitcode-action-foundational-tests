# REL-MATRIX-01-027

- 标题: matrix max-parallel=4——9 个组合应最多同时运行 4 个
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: matrix max-parallel=4——9 个组合应最多同时运行 4 个

- [正向] 峰值并发≤4
- [正向] 9 个 jobs 全部 completed(success)
- [负向] 不应超过 4 个同时运行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | matrix step | echo version=${{ matrix.version }} | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | max_concurrent_jobs |  |
| positive | run_status | completed(success) |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 峰值并发≤4 | COVERED | 1 real steps, assertions present |
| [正向] 9 个 jobs 全部 completed(success) | COVERED | 1 real steps, assertions present |
| [负向] 不应超过 4 个同时运行 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应超过 4 个同时运行: single dispatch cannot prove negative

---
