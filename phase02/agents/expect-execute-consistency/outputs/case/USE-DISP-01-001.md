# USE-DISP-01-001

- 标题: workflow_dispatch 必填参数未提供时应给出明确校验错误
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-DISP-01-001
维度标签:   ['usability', 'completeness']
维度:      usability/completeness
优先级:    P1
溯源意图:  INTENT-USE-030
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      workflow_dispatch 必填参数未提供时应给出明确校验错误

前置条件:
  - workflow 配置了一个 required: true 且无 default 的 input

操作步骤:
  1. 手动触发 workflow 但不提供该必填参数

预期结果:
  系统拒绝触发并提示缺少必填参数

验证点:
  - [负向] 不应在缺少必填参数时触发运行
  - [非功能] 报错中是否指出具体缺少的字段名

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo env (test-required) | echo "env=${{ inputs.environment }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应在缺少必填参数时触发运行 | 覆盖 | negative status assertion |
| 报错中是否指出具体缺少的字段名 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须指出缺少必填参数 environment 或等效字段名 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须指出缺少必填参数 environment 或等效字段名 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
