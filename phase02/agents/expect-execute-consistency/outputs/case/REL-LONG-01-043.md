# REL-LONG-01-043

- 标题: 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常

- [正向] job 状态=success
- [正向] 心跳日志间隔≤60 秒
- [负向] 不应在 350 分钟前被终止

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | heartbeat run | for i in $(seq 1 350); do   echo heartbeat $i   sleep 60 done | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | success |
| nonfunctional | heartbeat_interval_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job 状态=success | COVERED | 1 real steps, assertions present |
| [正向] 心跳日志间隔≤60 秒 | COVERED | 1 real steps, assertions present |
| [负向] 不应在 350 分钟前被终止 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应在 350 分钟前被终止: single dispatch cannot prove negative

---
