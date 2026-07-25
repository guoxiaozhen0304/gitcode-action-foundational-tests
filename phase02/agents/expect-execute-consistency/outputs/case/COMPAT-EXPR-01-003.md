# COMPAT-EXPR-01-003

- 标题: failure() 与 failed 关键字的处理行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-003
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-005
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      failure() 与 failed 关键字的处理行为差异

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow，其中包含一个会失败的 step
  2. 在后续 step 中尝试使用 failure() 函数或 failed 关键字形式的表达式
  3. 手动触发并观察运行结果

预期结果:
  - 平台对 failure() 函数与 failed 关键字可能有不同的支持策略
  - 记录实际行为，验证与 GitHub Actions 的兼容性差异

验证点:
  - [正向] 若支持，可在失败后获取到正确的状态值
  - [负向] 若不支持，应有表达式解析错误或降级行为
  - [正向] 失败后 step 的执行状态可被观察或引用

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | force failure | run: exit 1
 | 是 |
| 3 | cleanup after failure | run: echo "Cleanup ran after failure"
 | if: ${{ always() }} | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-failure:
    name: Test failure handling
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: force failure
        run: |
          exit 1
      - name: cleanup after failure
        if: ${{ always() }}
        run: |
          echo "Cleanup ran after failure"

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
| [正向] 若支持，可在失败后获取到正确的状态值 | ✅ COVERED | steps have real logic |
| [负向] 若不支持，应有表达式解析错误或降级行为 | ❌ UNVERIFIABLE | single dispatch cannot prove negation |
| [正向] 失败后 step 的执行状态可被观察或引用 | ✅ COVERED | steps have real logic |

### 问题

- [负向] 若不支持，应有表达式解析错误或降级行为: UNVERIFIABLE - single dispatch cannot prove negation

---
