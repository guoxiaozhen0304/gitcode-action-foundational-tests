# COMPAT-CONCUR-01-003

- 标题: concurrency preemption enable 行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-CONCUR-01-003
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-005
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      concurrency preemption enable 行为差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，配置 `concurrency.preemption.enable: true`
  2. 触发该 workflow 的多个并发运行
  3. 观察超上限时的抢占行为

预期结果:
  - GitHub 行为：cancel-in-progress 为 true 时，新运行取消旧运行
  - GitCode 行为：preemption 配置可能不被识别或行为不同
  - 应明确记录差异

验证点:
  - [正向] 系统接受或拒绝 preemption 配置时应给出明确提示
  - [负向] 不通过 preemption 配置被静默忽略

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Sleep and echo (test-preemption) | sleep 30 echo "done"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 系统接受或拒绝 preemption 配置时应给出明确提示 | 覆盖 | LLM/nonfunctional assertion: 系统接受或拒绝 preemption 配置时应给出明确提示 |
| 不通过 preemption 配置被静默忽略 | 覆盖 | LLM/nonfunctional assertion: preemption 配置不应被静默忽略 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | positive | 系统接受或拒绝 preemption 配置时应给出明确提示 | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统接受或拒绝 preemption 配置时应给出明确提示 |
| 2 | run_status | negative | preemption 配置不应被静默忽略 | LLM_DEPENDENT | LLM/nonfunctional assertion: preemption 配置不应被静默忽略 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
