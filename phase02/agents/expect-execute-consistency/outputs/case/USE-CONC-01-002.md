# USE-CONC-01-002

- 标题: concurrency.max 配置 -1 时报错应提示有效范围
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-CONC-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-027
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      concurrency.max 配置 -1 时报错应提示有效范围

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 workflow 中配置 concurrency: max: -1

预期结果:
  YAML 校验报错，明确说明 max 取值范围应为 1-5

验证点:
  - [负向] 不应静默截断
  - [非功能] 报错中是否包含有效范围说明

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | step (bad) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应静默截断 | 覆盖 | negative status assertion |
| 报错中是否包含有效范围说明 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含有效范围 1-5 或 1 到 5 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含有效范围 1-5 或 1 到 5 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
