# REL-RERUN-01-011

- 标题: rerun 边界值——单条运行连续重新运行 3 次应全部成功
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: rerun 边界值——单条运行连续重新运行 3 次应全部成功

- [正向] 运行编号递增
- [正向] 每次 rerun 状态=success
- [负向] 不应复用旧运行记录

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 5 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | rerun_count | 3 |
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
| [正向] 运行编号递增 | WEAK | assertions present but all steps trivial |
| [正向] 每次 rerun 状态=success | WEAK | assertions present but all steps trivial |
| [负向] 不应复用旧运行记录 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 运行编号递增: assertions present but all steps trivial
- [正向] 每次 rerun 状态=success: assertions present but all steps trivial
- [负向] 不应复用旧运行记录: single dispatch cannot prove negative

---
