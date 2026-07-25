# REL-MATRIXFAIR-01-056

- 标题: 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证

- [正向] 20 实例全部完成
- [非功能] 最大/最小 queued 延迟比≤3
- [负向] 无实例被无限饿死

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | matrix step | echo version=${{ matrix.version }} | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | completed_jobs_count | 20 |
| nonfunctional | queued_delay_ratio |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 20 实例全部完成 | COVERED | 1 real steps, assertions present |
| [非功能] 最大/最小 queued 延迟比≤3 | COVERED | 1 real steps, assertions present |
| [负向] 无实例被无限饿死 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 无实例被无限饿死: single dispatch cannot prove negative

---
