# COMP-STAGES-01-003

- 标题: post.run_always true 时 workflow 失败仍执行 post
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-STAGES-01-003
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-007
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      post.run_always true 时 workflow 失败仍执行 post

前置条件:
  - workflow 定义 post 阶段且 run_always: true

操作步骤:
  1. 触发 workflow 使主流程 job 失败
  2. 观察 post 阶段是否仍执行

预期结果:
  - 主 workflow 失败
  - post 阶段仍被执行

验证点:
  - [正向] post 阶段步骤日志存在
  - [正向] post 阶段步骤输出出现在运行详情页

清理:      none
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Force failure (main) | exit 1  | GENUINE |
| 2 | Post cleanup (post) | echo "post executed"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| post 阶段步骤日志存在 | 覆盖 | deliberate failure step exists |
| post 阶段步骤输出出现在运行详情页 | 覆盖 | deliberate failure step exists |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | failure | CONSISTENT | deliberate failure step exists |
| 2 | post_logs | positive | post executed | VACUOUS | step Post cleanup only echoes 'post executed', no real logic |

### 问题

- 断言 `[positive] post_logs` → VACUOUS: step Post cleanup only echoes 'post executed', no real logic

---
