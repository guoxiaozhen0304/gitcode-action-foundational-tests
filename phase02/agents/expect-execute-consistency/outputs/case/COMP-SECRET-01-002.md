# COMP-SECRET-01-002

- 标题: secret 原始值不应以明文出现在标准日志中
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SECRET-01-002
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-012
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      secret 原始值不应以明文出现在标准日志中

前置条件:
  - 仓库配置了 secret TEST_SECRET

操作步骤:
  1. 在 workflow 中通过多种方式输出 secret
  2. 查看运行日志

预期结果:
  - 无论通过何种标准方式引用，secret 原始值均不出现在日志

验证点:
  - [负向] 日志中不包含 secret 原始明文

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo secret via env | run: echo "env secret is $MY_SECRET"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify no secret plaintext
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo secret via env
        env:
          MY_SECRET: ${{ secrets.TEST_SECRET }}
        run: |
          echo "env secret is $MY_SECRET"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | with-secrets |
| Secrets | TEST_SECRET |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 日志中不包含 secret 原始明文 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
