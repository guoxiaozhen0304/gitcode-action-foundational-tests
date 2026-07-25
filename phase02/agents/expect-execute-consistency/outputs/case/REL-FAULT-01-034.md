# REL-FAULT-01-034

- 标题: 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss

- [正向] cache step 标记为 miss 或跳过
- [正向] 后续 step 正常执行
- [负向] job 不应因 cache 服务不可用而整体 failure

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | restore cache step | uses: cache | Y |
| 2 | subsequent step | echo subsequent step executed | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | success |
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
| [正向] cache step 标记为 miss 或跳过 | COVERED | 1 real steps, assertions present |
| [正向] 后续 step 正常执行 | COVERED | 1 real steps, assertions present |
| [负向] job 不应因 cache 服务不可用而整体 failure | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] job 不应因 cache 服务不可用而整体 failure: single dispatch cannot prove negative

---
