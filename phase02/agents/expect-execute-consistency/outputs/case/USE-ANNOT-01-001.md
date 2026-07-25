# USE-ANNOT-01-001

- 标题: workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-ANNOT-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-021
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文

前置条件:
  - workflow 在 GitCode Runner 上执行

操作步骤:
  1. 在 run 步骤中输出 ::error:: 和 ::warning:: 命令

预期结果:
  日志中保留原始命令文本，不静默吞掉

验证点:
  - [正向] 日志中包含 ::error:: 原始文本
  - [正向] 日志中包含 ::warning:: 原始文本

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | emit error and warning (annot-test) | echo "::error file=src/main.js,line=10::Missing semicolon" echo "::warning file=src/util.js,line=5:: | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 日志中包含 ::error:: 原始文本 | 覆盖 | produced by step 'emit error and warning': executes real command |
| 日志中包含 ::warning:: 原始文本 | 覆盖 | produced by step 'emit error and warning': executes real command |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | ::error file=src/main.js,line=10::Missing semicolo | CONSISTENT | produced by step 'emit error and warning': executes real command |
| 2 | run_logs | positive | ::warning file=src/util.js,line=5::Deprecated func | CONSISTENT | produced by step 'emit error and warning': executes real command |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
