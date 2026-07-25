# REL-FAIR-01-044

- 标题: 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- 维度: 稳定性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

标题: 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度

- [正向] 启动时延差≤60 秒
- [负向] 不应出现 workflow X 全部完成后 workflow Y 才开始

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 30 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| nonfunctional | startup_time_diff_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 启动时延差≤60 秒 | NOT COVERED | no real steps, no assertions |
| [负向] 不应出现 workflow X 全部完成后 workflow Y 才开始 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 启动时延差≤60 秒: no real steps, no assertions
- [负向] 不应出现 workflow X 全部完成后 workflow Y 才开始: single dispatch cannot prove negative

---
