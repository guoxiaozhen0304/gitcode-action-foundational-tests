# REL-MEM-01-020

- 标题: Runner 内存边界——small runner 分配 7.5 GB 应成功
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Runner 内存边界——small runner 分配 7.5 GB 应成功

- [正向] job 状态=success
- [负向] 不应在 7 GB 时 OOM

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | allocate 7.5GB | python3 -c "a=bytearray(7680*1024*1024); print(len(a))" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | success |

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
| [负向] 不应在 7 GB 时 OOM | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job 状态=success: assertions present but all steps trivial
- [负向] 不应在 7 GB 时 OOM: single dispatch cannot prove negative

---
