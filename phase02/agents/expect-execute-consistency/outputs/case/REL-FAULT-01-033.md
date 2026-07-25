# REL-FAULT-01-033

- 标题: 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满

- [正向] job 状态=failure
- [正向] 日志含磁盘满错误

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | prefill disk | fallocate -l 49.5G prefill.bin || dd if=/dev/zero of=prefill.bin bs=1M count=50688 | - |
| 2 | write additional 2GB | dd if=/dev/zero of=extra.bin bs=1M count=2048 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | failure |
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
| [正向] job 状态=failure | WEAK | assertions present but all steps trivial |
| [正向] 日志含磁盘满错误 | WEAK | assertions present but all steps trivial |

### 问题

- [正向] job 状态=failure: assertions present but all steps trivial
- [正向] 日志含磁盘满错误: assertions present but all steps trivial

---
