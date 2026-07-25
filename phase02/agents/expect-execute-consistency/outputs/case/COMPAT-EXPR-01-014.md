# COMPAT-EXPR-01-014

- 标题: always() 带括号与不带括号的兼容性差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-014
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-004
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      always() 带括号与不带括号的兼容性差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，if 条件分别使用 `${{ always() }}` 和 `${{ always }}`
  2. 触发 workflow

预期结果:
  - GitHub 行为：always() 和 always 都可用
  - GitCode 行为：可能仅支持带括号形式
  - 应明确记录差异

验证点:
  - [正向] 若支持无括号形式，应正常求值
  - [正向] 若不支持，应给出明确的语法错误提示

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Step with parens (test-always-paren) | echo "with_parens"  | GENUINE |
| 2 | Step without parens (test-always-paren) | echo "without_parens"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 若支持无括号形式，应正常求值 | 覆盖 | LLM/nonfunctional assertion: 若支持无括号形式，应正常求值并执行 |
| 若不支持，应给出明确的语法错误提示 | 覆盖 | LLM/nonfunctional assertion: 若支持无括号形式，应正常求值并执行 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 若支持无括号形式，应正常求值并执行 | LLM_DEPENDENT | LLM/nonfunctional assertion: 若支持无括号形式，应正常求值并执行 |
| 2 | error_message | positive | 若不支持无括号形式，应给出明确的语法错误提示 | LLM_DEPENDENT | LLM/nonfunctional assertion: 若不支持无括号形式，应给出明确的语法错误提示 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
