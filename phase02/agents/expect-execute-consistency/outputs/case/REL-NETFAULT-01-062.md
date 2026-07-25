# REL-NETFAULT-01-062

- 标题: 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时
- 维度: 稳定性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时

- [正向] 可达地址成功
- [负向] 不可达地址不应 hang>60s
- [非功能] 失败归因清晰

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | curl unreachable addresses | curl --connect-timeout 10 --max-time 120 -v http://192.0.2.1/ || true curl --connect-timeout 10 --ma | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | reachable_status | success |
| positive | unreachable_timeout_seconds |  |
| positive | failure_attribution | clear |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 可达地址成功 | COVERED | 1 real steps, assertions present |
| [负向] 不可达地址不应 hang>60s | UNVERIFIABLE | single dispatch cannot prove negative |
| [非功能] 失败归因清晰 | COVERED | 1 real steps, assertions present |

### 问题

- [负向] 不可达地址不应 hang>60s: single dispatch cannot prove negative

---
