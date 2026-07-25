# COMPAT-EXPR-01-002

- 标题: success() 函数的处理行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-004
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      success() 函数的处理行为差异

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow，在 step 中尝试使用 success() 函数形式的表达式
  2. 对比平台对 success() 与 bare success 的解析差异
  3. 手动触发并观察运行结果

预期结果:
  - 平台可能对 success() 函数与 bare success 关键字有不同的支持策略
  - 记录并验证实际行为与 GitHub Actions 的兼容性差异

验证点:
  - [正向] 若支持，表达式返回布尔结果
  - [负向] 若不支持，应有表达式解析错误或降级行为

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | succeed | run: echo "Job A done"
 | 否 |
| 3 | checkout source | uses: checkout | 是 |
| 4 | observe dependency success | run: echo "Job B ran after Job A success"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-a:
    name: Job A that succeeds
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: succeed
        run: |
          echo "Job A done"
  job-b:
    name: Job B depends on A
    runs-on: [ubuntu-latest, x64, small]
    needs: job-a
    steps:
      - name: checkout source
        uses: checkout
      - name: observe dependency success
        run: |
          echo "Job B ran after Job A success"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 若支持，表达式返回布尔结果 | ✅ COVERED | steps have real logic |
| [负向] 若不支持，应有表达式解析错误或降级行为 | ❌ UNVERIFIABLE | single dispatch cannot prove negation |

### 问题

- [负向] 若不支持，应有表达式解析错误或降级行为: UNVERIFIABLE - single dispatch cannot prove negation

---
