# REL-RERUN-01-013

- 标题: rerun 6 小时年龄限制——超期运行不可重新运行
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-RERUN-01-013
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-013
参照来源:  inputs/gitcode-spec/running-pipelines/view-job-logs.md; inputs/gitcode-spec/running-pipelines/view-run-results.md
母意图:    —
标题:      rerun 6 小时年龄限制——超期运行不可重新运行

前置条件:
  - 存在一条完成时间超过 6 小时的运行记录

操作步骤:
  1. 6 小时 1 分钟后尝试 rerun

预期结果:
  - rerun 请求被拒绝
  - 错误信息含 6 小时或已过期

验证点:
  - [正向] rerun 被拒绝
  - [负向] 不应创建新运行

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | sleep step (test) | sleep 5  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| rerun 被拒绝 | 覆盖 | real step logic exists |
| 不应创建新运行 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_request | positive | rejected | CONSISTENT | real step logic exists |

### 问题

- 验证点 `不应创建新运行` → 未覆盖: 缺少负向断言

---
