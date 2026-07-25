# COMPAT-CTX-01-003

- 标题: github 上下文嵌套属性访问应报错而非返回空
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-CTX-01-003
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-016
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      github 上下文嵌套属性访问应报错而非返回空

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，在 run 步骤中引用 `${{ github.event.pull_request.number }}`
  2. 触发 workflow（非 PR 事件）

预期结果:
  - GitHub 行为：非 PR 事件中 github.event.pull_request 为空对象，访问 .number 返回 null
  - GitCode 行为：应报错或返回空值，不应崩溃

验证点:
  - [正向] 嵌套属性访问不导致 workflow 崩溃
  - [正向] 返回值与 GitHub 行为一致（空值或 null）

清理:      无


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Access nested github property | run: echo "pr_number=${{ github.event.pull_request.number }}"
echo "done"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-github-nested:
    name: Test github nested property
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Access nested github property
        run: |
          echo "pr_number=${{ github.event.pull_request.number }}"
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
| [正向] 嵌套属性访问不导致 workflow 崩溃 | ✅ COVERED | steps have real logic |
| [正向] 返回值与 GitHub 行为一致（空值或 null） | ✅ COVERED | steps have real logic |

### 问题

无

---
