# COMPAT-ENV-01-003

- 标题: GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ENV-01-003
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-017
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，在 run 步骤中输出 `$GITHUB_ENV` 和 `$ATOMGIT_ENV`
  2. 触发 workflow

预期结果:
  - GITHUB_ENV 不应存在或被设置为空/未定义
  - 不应将 GITHUB_ENV 静默映射为 ATOMGIT_ENV 的值

验证点:
  - [负向] GITHUB_ENV 不等于 ATOMGIT_ENV
  - [正向] GITHUB_ENV 为空或未定义

清理:      无


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Compare env vars | run: echo "GITHUB_ENV=$GITHUB_ENV"
echo "ATOMGIT_ENV=$ATOMGIT_ENV"
echo "done"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-github-env:
    name: Test GITHUB_ENV not mapped
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare env vars
        run: |
          echo "GITHUB_ENV=$GITHUB_ENV"
          echo "ATOMGIT_ENV=$ATOMGIT_ENV"
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
| [负向] GITHUB_ENV 不等于 ATOMGIT_ENV | ✅ COVERED | negative assertion in YAML assertions |
| [正向] GITHUB_ENV 为空或未定义 | ✅ COVERED | steps have real logic |

### 问题

无

---
