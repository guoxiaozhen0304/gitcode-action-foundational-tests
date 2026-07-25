# COMPAT-EXPR-01-004

- 标题: contains 表达式大小写敏感边界
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-004
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-006
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      contains 表达式大小写敏感边界

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow，在 step 中使用 contains 表达式分别检查大小写不同的字符串
  2. 例如检查 contains('Hello World', 'world') 与 contains('Hello World', 'World')
  3. 手动触发并观察输出结果

预期结果:
  - contains 表达式按平台实际实现返回 true 或 false
  - 验证大小写敏感行为与 GitHub Actions 是否一致

验证点:
  - [正向] 大小写匹配时返回 true
  - [正向] 大小写不匹配时返回 false（若平台为大小写敏感）
  - [负向] 结果不应与预期语义矛盾

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | test lowercase match | run: echo "lowercase match: ${{ contains('Hello World', 'world') }}" | 是 |
| 3 | test exact case match | run: echo "exact case match: ${{ contains('Hello World', 'World') }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-contains-case:
    name: Test contains case sensitivity
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: test lowercase match
        run: "echo \"lowercase match: ${{ contains('Hello World', 'world') }}\""
      - name: test exact case match
        run: "echo \"exact case match: ${{ contains('Hello World', 'World') }}\""

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
| [正向] 大小写匹配时返回 true | ✅ COVERED | steps have real logic |
| [正向] 大小写不匹配时返回 false（若平台为大小写敏感） | ✅ COVERED | steps have real logic |
| [负向] 结果不应与预期语义矛盾 | ❌ UNVERIFIABLE | single dispatch cannot prove negation |

### 问题

- [负向] 结果不应与预期语义矛盾: UNVERIFIABLE - single dispatch cannot prove negation

---
