# USE-CTX-01-001

- 标题: 使用 atomgit 上下文时表达式正常求值
- 维度: 易用性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-CTX-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-002
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      使用 atomgit 上下文时表达式正常求值

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 workflow 的 run 步骤中引用 ${{ atomgit.ref }}

预期结果:
  表达式正确求值为当前分支引用

验证点:
  - [正向] 日志中输出当前分支引用值
  - [正向] 运行成功完成

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo atomgit ref (test-ctx) | echo "ref=${{ atomgit.ref }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 日志中输出当前分支引用值 | 空洞 | no step produces 'ref=refs/heads/' |
| 运行成功完成 | 空洞 | no step produces 'ref=refs/heads/' |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | ref=refs/heads/ | MISSING_SOURCE | no step produces 'ref=refs/heads/' |

### 问题

- 验证点 `日志中输出当前分支引用值` → 空洞: no step produces 'ref=refs/heads/'

- 验证点 `运行成功完成` → 空洞: no step produces 'ref=refs/heads/'

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'ref=refs/heads/'

---
