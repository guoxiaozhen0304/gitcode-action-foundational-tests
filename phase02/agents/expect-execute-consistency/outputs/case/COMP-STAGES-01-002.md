# COMP-STAGES-01-002

- 标题: fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-STAGES-01-002
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-007
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job

前置条件:
  - workflow 定义含 fail_fast: true 的 stage
  - stage 内至少两个 jobs

操作步骤:
  1. 触发 workflow，使 stage 内一个 job 失败
  2. 观察同 stage 其他 job 的行为

预期结果:
  - 失败的 job 导致同 stage 其他 job 被取消或跳过
  - 后续 stages 被跳过

验证点:
  - [正向] 同 stage 其余 job 被终止
  - [负向] 后续 stage 不应执行

清理:      none
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Force failure (fail-job) | exit 1  | GENUINE |
| 2 | Echo skipped (should-skip) | echo "should not execute"  | VACUOUS |
| 3 | Echo deploy (deploy) | echo "should not execute"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 同 stage 其余 job 被终止 | 覆盖 | status assertion: skipped_for_should_skip |
| 后续 stage 不应执行 | 覆盖 | real logic exists for negative verification |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | skipped_for_should_skip | CONSISTENT | status assertion: skipped_for_should_skip |
| 2 | stage_execution | negative | deploy_stage_executed | CONSISTENT | real logic exists for negative verification |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
