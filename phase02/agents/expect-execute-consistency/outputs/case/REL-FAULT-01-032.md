# REL-FAULT-01-032

- 标题: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误

- [正向] upload-artifact step 状态=failure
- [正向] 日志含网络错误
- [负向] 不应无限挂起超过 120 秒

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | generate artifact file | dd if=/dev/urandom of=artifact.bin bs=1M count=10 | - |
| 2 | upload artifact step | uses: upload-artifact | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | step_status | failure |
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
| [正向] upload-artifact step 状态=failure | COVERED | 1 real steps, assertions present |
| [正向] 日志含网络错误 | COVERED | 1 real steps, assertions present |
| [负向] 不应无限挂起超过 120 秒 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应无限挂起超过 120 秒: single dispatch cannot prove negative

---
