# COMPAT-MASK-01-002

- 标题: 通过 env 注入 secret 后输出应在日志中被脱敏
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

# 用例归档

用例 ID:   COMPAT-MASK-01-002
维度标签:   [compatibility, security]
维度:      兼容性
优先级:    P0
溯源意图:  INTENT-COMPAT-033
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      通过 env 注入 secret 后输出应在日志中被脱敏

前置条件:
  - 仓库配置了 secret TEST_SECRET，值为已知字符串（如 my-secret-value-456）

操作步骤:
  1. 创建一个 workflow_dispatch 触发的 workflow
  2. 在 step 的 env 块中将 TEST_SECRET 注入为环境变量 MY_VAR
  3. 在 run 脚本中执行 `echo "$MY_VAR"`
  4. 手动触发该 workflow
  5. 查看运行日志中该 step 的输出

预期结果:
  - 日志中 MY_VAR 的值（即 secret 的值）应被替换为 `***`
  - 即使通过 env 间接引用，脱敏机制仍应生效
  - 不应出现 my-secret-value-456 的明文

验证点:
  - [负向] 日志中不含 TEST_SECRET 的原始明文值
  - [正向] 日志中出现 `***` 替代通过 env 注入的 secret 值
  - [正向] 环境变量在运行时可被正常读取（仅日志脱敏）

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | echo secret via env | run: echo "Env value: $MY_VAR"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  mask-env-test:
    name: Test secret masking via env
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: echo secret via env
        env:
          MY_VAR: ${{ secrets.TEST_SECRET }}
        run: |
          echo "Env value: $MY_VAR"

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
| [正向] 日志中出现 `***` 替代通过 env 注入的 secret 值 | ✅ COVERED | steps have real logic |
| [正向] 环境变量在运行时可被正常读取（仅日志脱敏） | ✅ COVERED | steps have real logic |

### 问题

无

---
