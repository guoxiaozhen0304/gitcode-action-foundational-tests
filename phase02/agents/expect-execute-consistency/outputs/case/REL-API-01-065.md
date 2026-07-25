# REL-API-01-065

- 标题: API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据
- 维度: 稳定性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据

- [正向] 200 占比=100%
- [负向] 不应出现 429/503/500
- [非功能] P95≤2s

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 30 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | http_200_ratio | 100% |
| negative | http_error_codes |  |
| nonfunctional | response_time_p95_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 200 占比=100% | WEAK | assertions present but all steps trivial |
| [负向] 不应出现 429/503/500 | COVERED | negative assertion present |
| [非功能] P95≤2s | WEAK | assertions present but all steps trivial |

### 问题

- [正向] 200 占比=100%: assertions present but all steps trivial
- [非功能] P95≤2s: assertions present but all steps trivial

---
