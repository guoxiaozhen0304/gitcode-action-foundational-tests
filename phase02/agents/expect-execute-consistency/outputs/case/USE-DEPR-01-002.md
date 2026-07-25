# USE-DEPR-01-002

- 标题: 使用 ::set-output 时应给出弃用警告与替代示例
- 维度: 易用性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-DEPR-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-010
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      使用 ::set-output 时应给出弃用警告与替代示例

前置条件:
  - workflow 在 GitCode Runner 上执行

操作步骤:
  1. 在 run 步骤中使用 echo ::set-output name=key::val

预期结果:
  日志中出现明确的弃用警告，包含替代命令示例

验证点:
  - [负向] 不应静默生效
  - [非功能] 日志警告中应包含 deprecated/废弃/ATOMGIT_OUTPUT 字样

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | use deprecated set-output (bad-depr) | echo "::set-output name=mykey::myvalue"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应静默生效 | 未覆盖 | 缺少负向断言 |
| 日志警告中应包含 deprecated/废弃/ATOMGIT_OUTPUT 字样 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | 报错/警告信息必须包含已废弃或 deprecated 字样，并给出至少一条完整的 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错/警告信息必须包含已废弃或 deprecated 字样，并给出至少一条完整的替代命令示例 |

### 问题

- 验证点 `不应静默生效` → 未覆盖: 缺少负向断言

---
