# USE-RUN-01-002

- 标题: 使用单标签 ubuntu-latest 时报错应给出三段式格式指引
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-RUN-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-006
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      使用单标签 ubuntu-latest 时报错应给出三段式格式指引

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 job 中写 runs-on: [ubuntu-latest]

预期结果:
  系统在校验或调度阶段报错，给出三段式标签格式示例或可用标签列表

验证点:
  - [负向] 不应无限 queued 且无提示
  - [非功能] 报错中应包含三段式或 default 等关键词

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | step (bad-runner) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应无限 queued 且无提示 | 覆盖 | negative status assertion |
| 报错中应包含三段式或 default 等关键词 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含 runs-on 或 runner 标签相关说明，并给出至少一个 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含 runs-on 或 runner 标签相关说明，并给出至少一个正确示例 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
