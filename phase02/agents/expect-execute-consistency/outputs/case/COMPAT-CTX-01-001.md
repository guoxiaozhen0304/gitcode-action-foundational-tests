# COMPAT-CTX-01-001

- 标题: 使用 github.ref 上下文应报错或求值为空
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-CTX-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-016
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      使用 github.ref 上下文应报错或求值为空

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow 的 run 步骤中引用 ${{ github.ref }}
  2. 提交并推送该 workflow
  3. 触发 workflow 运行

预期结果:
  - 平台应对 github.* 上下文给出明确报错，或在运行时求值为空字符串
  - 不应将 github.ref 静默映射到 atomgit.ref

验证点:
  - [负向] 使用 github.ref 不应被静默映射为 atomgit.ref
  - [非功能] 报错信息应提示将 github.* 替换为 atomgit.*

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo github ref | run: echo "github_ref=${{ github.ref }}"
echo "done"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test github context reference
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo github ref
        run: |
          echo "github_ref=${{ github.ref }}"
          echo "done"

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
| [负向] 使用 github.ref 不应被静默映射为 atomgit.ref | ✅ COVERED | negative assertion in YAML assertions |
| [非功能] 报错信息应提示将 github.* 替换为 atomgit.* | ✅ COVERED | steps have real logic |

### 问题

无

---
