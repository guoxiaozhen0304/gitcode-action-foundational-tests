# COMP-SECRET-01-003

- 标题: base64 编码后的 secret 是否仍被脱敏
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SECRET-01-003
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-012
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      base64 编码后的 secret 是否仍被脱敏

前置条件:
  - 仓库配置了 secret TEST_SECRET

操作步骤:
  1. 在 workflow 中对 secret 进行 base64 编码后输出
  2. 查看运行日志

预期结果:
  - 记录实际行为：编码后是否仍被脱敏

验证点:
  - [非功能] 记录 base64 编码输出是否被脱敏

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo base64 secret | run: echo "base64 secret is $(echo -n '${{ secrets.TEST_SECRET }}'   base64)"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify base64 masking
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo base64 secret
        run: |
          echo "base64 secret is $(echo -n '${{ secrets.TEST_SECRET }}' | base64)"

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
| [非功能] 记录 base64 编码输出是否被脱敏 | ✅ COVERED | steps have real logic |

### 问题

无

---
