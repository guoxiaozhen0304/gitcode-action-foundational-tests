# REL-DISK-01-019

- 标题: Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满

- [正向] job 状态=failure
- [正向] 日志含磁盘满错误
- [负向] 不应静默卡死

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | write 51GB file | fallocate -l 51G testfile || dd if=/dev/zero of=testfile bs=1M count=52224 | - |
| 2 | check failure | echo expecting failure above | - |

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
| [负向] 不应静默卡死 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job 状态=failure: assertions present but all steps trivial
- [正向] 日志含磁盘满错误: assertions present but all steps trivial
- [负向] 不应静默卡死: single dispatch cannot prove negative

---
