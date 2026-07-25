# COMPAT-MASK-01-001

- 标题: 直接 echo secrets 值应在日志中被脱敏
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

# 用例归档

用例 ID:   COMPAT-MASK-01-001
维度标签:   [compatibility, security]
维度:      兼容性
优先级:    P0
溯源意图:  INTENT-COMPAT-033
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      直接 echo secrets 值应在日志中被脱敏

前置条件:
  - 仓库配置了 secret TEST_SECRET，值为已知字符串（如 my-secret-value-123）

操作步骤:
  1. 创建一个 workflow_dispatch 触发的 workflow
  2. 在 step 中执行 `echo "${{ secrets.TEST_SECRET }}"`
  3. 手动触发该 workflow
  4. 查看运行日志中该 step 的输出

预期结果:
  - 日志中 secrets.TEST_SECRET 的值应被替换为 `***`
  - 不应出现 my-secret-value-123 的明文

验证点:
  - [负向] 日志中不含 TEST_SECRET 的原始明文值
  - [正向] 日志中出现 `***` 替代 secret 值

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | echo secret directly | run: echo "Secret value: ${{ secrets.TEST_SECRET }}"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  mask-test:
    name: Test secret masking direct echo
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: echo secret directly
        run: |
          echo "Secret value: ${{ secrets.TEST_SECRET }}"

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
| [负向] 日志中不含 TEST_SECRET 的原始明文值 | ✅ COVERED | negative assertion in YAML assertions |
| [正向] 日志中出现 `***` 替代 secret 值 | ✅ COVERED | steps have real logic |

### 问题

无

---
