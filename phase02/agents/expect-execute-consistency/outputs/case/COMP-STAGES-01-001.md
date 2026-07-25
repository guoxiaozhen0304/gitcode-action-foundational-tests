# COMP-STAGES-01-001

- 标题: stages 阶段间串行、阶段内 job 并行执行
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-STAGES-01-001
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-007
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      stages 阶段间串行、阶段内 job 并行执行

前置条件:
  - workflow 定义多个 stages，每个 stage 含多个 jobs

操作步骤:
  1. 触发 workflow
  2. 观察 stages 和 jobs 的执行顺序

预期结果:
  - stage 1 的所有 job 完成后，stage 2 才开始
  - 同 stage 内的 jobs 并行执行

验证点:
  - [正向] stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间
  - [正向] 同 stage 内 job 的开始时间相近（并行）

清理:      none
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Build A step (build-a) | echo "build-a"  | VACUOUS |
| 2 | Build B step (build-b) | echo "build-b"  | VACUOUS |
| 3 | Test step (test) | echo "test"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间 | 空洞 | all steps trivial, status=success always guaranteed |
| 同 stage 内 job 的开始时间相近（并行） | 空洞 | all steps trivial, status=success always guaranteed |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | STATUS_GUARANTEED | all steps trivial, status=success always guaranteed |
| 2 | stage_order | positive | serial_across_stages | VACUOUS | steps only echo literal strings |
| 3 | job_parallelism | positive | parallel_within_stage | VACUOUS | steps only echo literal strings |

### 问题

- 验证点 `stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间` → 空洞: all steps trivial, status=success always guaranteed

- 验证点 `同 stage 内 job 的开始时间相近（并行）` → 空洞: all steps trivial, status=success always guaranteed

- 断言 `[positive] run_status` → STATUS_GUARANTEED: all steps trivial, status=success always guaranteed

- 断言 `[positive] stage_order` → VACUOUS: steps only echo literal strings

- 断言 `[positive] job_parallelism` → VACUOUS: steps only echo literal strings

---
