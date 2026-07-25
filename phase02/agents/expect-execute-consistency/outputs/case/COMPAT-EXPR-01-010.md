# COMPAT-EXPR-01-010

- 标题: loose equality null 与空字符串及零的等价性差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-010
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-009
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    COMPAT-EXPR-01-009
标题:      loose equality null 与空字符串及零的等价性差异

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow 中使用 eq 表达式比较 null 与空字符串、null 与数字零
  2. 提交并触发 workflow
  3. 观察求值结果是否与 GitHub Actions 一致

预期结果:
  - null 与空字符串、null 与 0 的比较行为应与 GitHub Actions 一致
  - 若存在差异，应明确记录 null 的强制转换规则

验证点:
  - [正向] 表达式求值不报错
  - [非功能] null 比较结果应与 GitHub Actions 行为一致

清理:      fixture
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Compare null and empty string (test-null-eq) | if ${{ null == '' }}; then   echo "NULL_EQ_EMPTY=true" else   echo "NULL_EQ_EMPTY=false" fi  | GENUINE |
| 2 | Compare null and number zero (test-null-eq) | if ${{ null == 0 }}; then   echo "NULL_EQ_ZERO=true" else   echo "NULL_EQ_ZERO=false" fi  | GENUINE |
| 3 | Compare null and false (test-null-eq) | if ${{ null == false }}; then   echo "NULL_EQ_FALSE=true" else   echo "NULL_EQ_FALSE=false" fi  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 表达式求值不报错 | 覆盖 | real command in step 'Compare null and empty string' contains string |
| null 比较结果应与 GitHub Actions 行为一致 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | NULL_EQ_EMPTY= | CONSISTENT | real command in step 'Compare null and empty string' contains string |
| 2 | run_logs | positive | NULL_EQ_ZERO= | CONSISTENT | real command in step 'Compare null and number zero' contains string |
| 3 | run_logs | nonfunctional | null 的 loose equality 比较结果应与 GitHub Acti | LLM_DEPENDENT | LLM/nonfunctional assertion: null 的 loose equality 比较结果应与 GitHub Actions 一致；null |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
