# REL-MEM-01-021

- 标题: Runner 内存越界——small runner 分配 9 GB 应被 OOM kill
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Runner 内存越界——small runner 分配 9 GB 应被 OOM kill

- [正向] job 状态=failure
- [正向] 日志含 OOM 或 Killed
- [负向] 不应导致 Runner 宿主机崩溃

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | allocate 9GB | python3 -c "a=bytearray(9216*1024*1024); print(len(a))" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | failure |
| positive | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job 状态=failure | WEAK | assertions present but all steps trivial |
| [正向] 日志含 OOM 或 Killed | WEAK | assertions present but all steps trivial |
| [负向] 不应导致 Runner 宿主机崩溃 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job 状态=failure: assertions present but all steps trivial
- [正向] 日志含 OOM 或 Killed: assertions present but all steps trivial
- [负向] 不应导致 Runner 宿主机崩溃: single dispatch cannot prove negative

---
