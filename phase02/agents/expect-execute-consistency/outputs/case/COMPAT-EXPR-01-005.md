# COMPAT-EXPR-01-005

- 标题: contains 表达式空值与空字符串边界
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-006
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      contains 表达式空值与空字符串边界

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow，在 step 中使用 contains 表达式测试边界情况
  2. 包括 contains('', 'a')、contains('abc', '')、以及包含 null/未定义变量的场景
  3. 手动触发并观察输出结果

预期结果:
  - contains 表达式对空字符串和空值有确定性的返回值
  - 验证边界行为与 GitHub Actions 是否一致

验证点:
  - [正向] 空字符串包含任意非空子串返回 false
  - [正向] 任意字符串包含空子串返回 true（若与 GitHub 行为一致）
  - [负向] 空值场景不应导致表达式解析崩溃

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | test empty haystack | run: echo "empty haystack: ${{ contains('', 'a') }}" | 是 |
| 3 | test empty needle | run: echo "empty needle: ${{ contains('abc', '') }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-contains-empty:
    name: Test contains empty boundaries
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: test empty haystack
        run: "echo \"empty haystack: ${{ contains('', 'a') }}\""
      - name: test empty needle
        run: "echo \"empty needle: ${{ contains('abc', '') }}\""

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
| [正向] 空字符串包含任意非空子串返回 false | ✅ COVERED | steps have real logic |
| [正向] 任意字符串包含空子串返回 true（若与 GitHub 行为一致） | ✅ COVERED | steps have real logic |
| [负向] 空值场景不应导致表达式解析崩溃 | ❌ UNVERIFIABLE | single dispatch cannot prove negation |

### 问题

- [负向] 空值场景不应导致表达式解析崩溃: UNVERIFIABLE - single dispatch cannot prove negation

---
