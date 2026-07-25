# REL-FLOOD-01-037

- 标题: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃

- [正向] 50 个运行均被创建
- [正向] API/UI 无 5xx
- [非功能] 全部完成总时长合理
- [负向] 不应出现运行丢失或重复触发

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 5 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | created_runs_count | 50 |
| positive | api_status | 200 |
| negative | api_status | 500 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | push |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 50 个运行均被创建 | WEAK | assertions present but all steps trivial |
| [正向] API/UI 无 5xx | WEAK | assertions present but all steps trivial |
| [非功能] 全部完成总时长合理 | WEAK | assertions present but all steps trivial |
| [负向] 不应出现运行丢失或重复触发 | COVERED | negative assertion present |

### 问题

- [正向] 50 个运行均被创建: assertions present but all steps trivial
- [正向] API/UI 无 5xx: assertions present but all steps trivial
- [非功能] 全部完成总时长合理: assertions present but all steps trivial

---
