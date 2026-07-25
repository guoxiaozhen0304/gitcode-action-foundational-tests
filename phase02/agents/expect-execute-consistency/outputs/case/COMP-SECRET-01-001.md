# COMP-SECRET-01-001

- 标题: echo secret 在日志中被脱敏为 ***
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SECRET-01-001
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-012
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      echo secret 在日志中被脱敏为 ***

前置条件:
  - 仓库配置了 secret TEST_SECRET

操作步骤:
  1. 在 workflow 中执行 echo ${{ secrets.TEST_SECRET }}
  2. 查看运行日志

预期结果:
  - 日志中 secret 值显示为 ***

验证点:
  - [正向] 日志中包含 *** 而非真实 secret 值

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo secret | run: echo "secret is ${{ secrets.TEST_SECRET }}"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify secret masking
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo secret
        run: |
          echo "secret is ${{ secrets.TEST_SECRET }}"

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
| [正向] 日志中包含 *** 而非真实 secret 值 | ✅ COVERED | steps have real logic |

### 问题

无

---
