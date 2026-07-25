# REL-MATRIX-01-026

- 标题: matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: matrix fail-fast=true——任意 job 实例失败应立即取消其余实例

- [正向] 失败 job 状态=failure
- [正向] 其余未完成 jobs 状态=cancelled
- [负向] 不应继续执行已失败的 matrix 其余实例

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | matrix step | echo version=${{ matrix.version }} | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | failure |
| positive | cancelled_jobs_count | 8 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 失败 job 状态=failure | COVERED | 1 real steps, assertions present |
| [正向] 其余未完成 jobs 状态=cancelled | COVERED | 1 real steps, assertions present |
| [负向] 不应继续执行已失败的 matrix 其余实例 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应继续执行已失败的 matrix 其余实例: single dispatch cannot prove negative

---
