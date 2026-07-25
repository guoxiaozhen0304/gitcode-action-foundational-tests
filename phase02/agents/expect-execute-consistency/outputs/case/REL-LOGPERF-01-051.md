# REL-LOGPERF-01-051

- 标题: 日志加载性能——50MB 日志下载与查看耗时
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 日志加载性能——50MB 日志下载与查看耗时

- [正向] 下载≤30s
- [正向] 大小/行数 100% 一致
- [负向] 不应 UI 卡死

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | generate 50MB log | for i in $(seq 1 50000); do echo LOG_LINE_${{i}} $(date +%s%N); done | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| nonfunctional | download_time_seconds |  |
| positive | log_integrity | 100% |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 下载≤30s | COVERED | 1 real steps, assertions present |
| [正向] 大小/行数 100% 一致 | COVERED | 1 real steps, assertions present |
| [负向] 不应 UI 卡死 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应 UI 卡死: single dispatch cannot prove negative

---
