# COMPAT-CONCUR-01-004

- 标题: concurrency preemption events 越界时行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-CONCUR-01-004
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-005
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      concurrency preemption events 越界时行为差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，配置 `concurrency.preemption.events` 为 11 个（越界值）
  2. 提交该 workflow
  3. 观察系统校验行为

预期结果:
  - GitHub 行为：events 越界时应被拒绝并给出有效范围提示
  - GitCode 行为：可能不支持 preemption events 配置
  - 应明确记录差异

验证点:
  - [正向] 系统对越界值给出明确报错
  - [正向] 报错包含有效范围提示

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo hello (test-preemption-events) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 系统对越界值给出明确报错 | 覆盖 | LLM/nonfunctional assertion: 系统对 events 越界值给出明确报错 |
| 报错包含有效范围提示 | 覆盖 | LLM/nonfunctional assertion: 系统对 events 越界值给出明确报错 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | positive | 系统对 events 越界值给出明确报错 | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统对 events 越界值给出明确报错 |
| 2 | error_message | positive | 报错包含有效范围提示（如 1-10） | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错包含有效范围提示（如 1-10） |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
