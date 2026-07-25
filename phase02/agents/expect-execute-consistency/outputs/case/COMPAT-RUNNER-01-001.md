# COMPAT-RUNNER-01-001

- 标题: runner.os 在 Linux Runner 上应返回 Linux
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: runner.os 在 Linux Runner 上应返回 Linux

- [正向] 日志中 runner.os 的值为 Linux
- [负向] 不应返回小写的 linux

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo runner os | echo "runner_os=${{ runner.os }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
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
| [正向] 日志中 runner.os 的值为 Linux | COVERED | 1 real steps, assertions present |
| [负向] 不应返回小写的 linux | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应返回小写的 linux: single dispatch cannot prove negative

---
