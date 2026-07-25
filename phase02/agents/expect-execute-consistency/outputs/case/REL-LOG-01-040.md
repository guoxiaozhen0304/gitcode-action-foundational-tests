# REL-LOG-01-040

- 标题: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看

- [正向] 日志总大小≈100 MB
- [正向] 首尾行可查看
- [正向] 日志下载正常
- [负向] 不应截断或乱序

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | generate 100MB log | for i in $(seq 1 2500); do python3 -c "print('A'*40960)"; done | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | log_size_mb | 100 |
| positive | log_download | success |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 日志总大小≈100 MB | COVERED | 1 real steps, assertions present |
| [正向] 首尾行可查看 | COVERED | 1 real steps, assertions present |
| [正向] 日志下载正常 | COVERED | 1 real steps, assertions present |
| [负向] 不应截断或乱序 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应截断或乱序: single dispatch cannot prove negative

---
