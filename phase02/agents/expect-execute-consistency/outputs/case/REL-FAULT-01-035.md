# REL-FAULT-01-035

- 标题: 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误
- 维度: 稳定性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误

- [正向] download-artifact step 状态=failure
- [正向] 日志含服务不可用错误
- [正向] job 状态=failure

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | download artifact step | uses: download-artifact | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | step_status | failure |
| positive | run_logs |  |
| positive | job_status | failure |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] download-artifact step 状态=failure | COVERED | 1 real steps, assertions present |
| [正向] 日志含服务不可用错误 | COVERED | 1 real steps, assertions present |
| [正向] job 状态=failure | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
