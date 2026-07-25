# REL-CPU-01-022

- 标题: Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长

- [正向] job 状态=success
- [非功能] 总耗时 120±24 秒
- [负向] 不应被系统强制终止

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | burn 4 CPU processes | for i in 1 2 3 4; do python3 -c "import time; end=time.time()+60; [x*x for x in range(10000)] while  | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | success |
| nonfunctional | job_duration_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job 状态=success | WEAK | assertions present but all steps trivial |
| [非功能] 总耗时 120±24 秒 | WEAK | assertions present but all steps trivial |
| [负向] 不应被系统强制终止 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job 状态=success: assertions present but all steps trivial
- [非功能] 总耗时 120±24 秒: assertions present but all steps trivial
- [负向] 不应被系统强制终止: single dispatch cannot prove negative

---
