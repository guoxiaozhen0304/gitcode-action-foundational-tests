# REL-DISK-01-018

- 标题: Runner 磁盘边界——small runner 写入 49 GB 应成功
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Runner 磁盘边界——small runner 写入 49 GB 应成功

- [正向] job 状态=success
- [负向] 不应在 49 GB 时报磁盘满

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | write 49GB file | fallocate -l 49G testfile || dd if=/dev/zero of=testfile bs=1M count=50176 | - |
| 2 | verify disk space | df -h . test -f testfile | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | job_status | success |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] job 状态=success | WEAK | assertions present but all steps trivial |
| [负向] 不应在 49 GB 时报磁盘满 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] job 状态=success: assertions present but all steps trivial
- [负向] 不应在 49 GB 时报磁盘满: single dispatch cannot prove negative

---
