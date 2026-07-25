# REL-PROJLIMIT-01-068

- 标题: 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队

- [正向] completed_count = 201
- [正向] failed_count = 0
- [正向] queued_count ≥ 1（超出 200 上限部分应排队）
- [正向] lost_count = 0
- [负向] 不应出现触发后无对应 run 记录（丢失）
- [负向] 不应因并发超限而直接返回 429/500 导致触发失败

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | quick step | echo "run_id=${{ atomgit.run_id }}" sleep 5 | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | completed_count | 201 |
| positive | failed_count | 0 |
| positive | queued_count |  |
| nonfunctional | total_duration_seconds |  |
| nonfunctional | lost_count | 0 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] completed_count = 201 | COVERED | 1 real steps, assertions present |
| [正向] failed_count = 0 | COVERED | 1 real steps, assertions present |
| [正向] queued_count ≥ 1（超出 200 上限部分应排队） | COVERED | 1 real steps, assertions present |
| [正向] lost_count = 0 | COVERED | 1 real steps, assertions present |
| [负向] 不应出现触发后无对应 run 记录（丢失） | UNVERIFIABLE | single dispatch cannot prove negative |
| [负向] 不应因并发超限而直接返回 429/500 导致触发失败 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应出现触发后无对应 run 记录（丢失）: single dispatch cannot prove negative
- [负向] 不应因并发超限而直接返回 429/500 导致触发失败: single dispatch cannot prove negative

---
