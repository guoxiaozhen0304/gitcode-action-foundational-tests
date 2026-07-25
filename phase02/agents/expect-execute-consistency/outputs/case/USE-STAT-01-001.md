# USE-STAT-01-001

- 标题: 使用 always() 带括号时若被接受则正常执行
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-STAT-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-004
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      使用 always() 带括号时若被接受则正常执行

前置条件:
  - workflow 文件合法

操作步骤:
  1. 在 step 中使用 if: ${{ always() }}

预期结果:
  该 step 无论上游成败均执行

验证点:
  - [正向] step 日志出现执行记录
  - [正向] 运行成功完成

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | force fail (test-always) | exit 1  | GENUINE |
| 2 | cleanup with always (test-always) | echo "cleanup executed"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| step 日志出现执行记录 | 覆盖 | produced by step 'cleanup with always': uses ${{ }} expression |
| 运行成功完成 | 覆盖 | produced by step 'cleanup with always': uses ${{ }} expression |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | cleanup executed | CONSISTENT | produced by step 'cleanup with always': uses ${{ }} expression |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
