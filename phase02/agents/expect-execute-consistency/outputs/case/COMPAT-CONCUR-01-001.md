# COMPAT-CONCUR-01-001

- 标题: concurrency cancel-in-progress false 时应排队而非报错
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
# 用例归档

用例 ID:   COMPAT-CONCUR-01-001
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-034
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      concurrency cancel-in-progress false 时应排队而非报错

前置条件:
  - 仓库已启用 workflow
  - 同一 concurrency group 当前无运行中实例或可通过快速触发制造冲突

操作步骤:
  1. 创建一个 workflow_dispatch 触发的 workflow
  2. 配置 workflow 级 `concurrency` 块，指定 group 名称和 `cancel-in-progress: false`
  3. 在 job 中加入一个长时间运行的 step（如 sleep 60）
  4. 快速连续触发两次该 workflow
  5. 观察第二次触发的行为

预期结果:
  - 第二次触发不应直接报错失败
  - 第二次触发应进入排队（pending/queued）状态，等待第一次完成后执行
  - 这与 GitHub Actions 的排队语义一致

验证点:
  - [负向] 第二次触发不应被标记为失败或取消
  - [正向] 第二次触发的状态为 queued / pending
  - [正向] 第一次完成后第二次正常开始执行

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | checkout source (concurrency-test) | checkout | GENUINE |
| 2 | long running step (concurrency-test) | echo "Starting long job" sleep 60 echo "Job done"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 第二次触发不应被标记为失败或取消 | 覆盖 | LLM/nonfunctional assertion: 第二次触发不应被标记为失败 |
| 第二次触发的状态为 queued / pending | 覆盖 | LLM/nonfunctional assertion: 第二次触发的状态为 queued / pending，等待第一次完成后执行 |
| 第一次完成后第二次正常开始执行 | 覆盖 | LLM/nonfunctional assertion: 第二次触发的状态为 queued / pending，等待第一次完成后执行 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | failure | LLM_DEPENDENT | LLM/nonfunctional assertion: 第二次触发不应被标记为失败 |
| 2 | run_status | positive | 第二次触发的状态为 queued / pending，等待第一次完成后执行 | LLM_DEPENDENT | LLM/nonfunctional assertion: 第二次触发的状态为 queued / pending，等待第一次完成后执行 |
| 3 | run_logs | positive | 第一次完成后第二次正常开始执行并输出 Job done | LLM_DEPENDENT | LLM/nonfunctional assertion: 第一次完成后第二次正常开始执行并输出 Job done |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
