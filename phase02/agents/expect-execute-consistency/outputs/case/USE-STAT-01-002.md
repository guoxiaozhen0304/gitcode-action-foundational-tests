# USE-STAT-01-002

- 标题: 使用 success() 带括号时报错应提示 GitCode 括号差异
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-STAT-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-004
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      使用 success() 带括号时报错应提示 GitCode 括号差异

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 step 中使用 if: ${{ success() }}

预期结果:
  YAML 校验或表达式求值报错，提示 GitCode 状态函数不带括号

验证点:
  - [负向] 不应静默通过校验
  - [非功能] 报错中应包含括号差异提示

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | step with brackets (bad-stat) | echo "hello"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应静默通过校验 | 覆盖 | negative status assertion |
| 报错中应包含括号差异提示 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含 success 或 状态函数关键词，并明示 GitCode 状 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含 success 或 状态函数关键词，并明示 GitCode 状态函数不带括号 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
