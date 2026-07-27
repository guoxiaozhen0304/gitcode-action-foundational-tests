# SEC-INJ-01-001

- 标题: 不可信 PR 标题不可直接插进 run 脚本导致命令注入
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   SEC-INJ-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-009
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      不可信 PR 标题不可直接插进 run 脚本导致命令注入

前置条件:
  - 存在一个来自外部 fork 的 PR，其标题包含 shell 元字符

操作步骤:
  1. 提交一个 workflow，在 run 脚本中直接内联引用 PR 标题
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - PR 标题中的特殊字符不应被解释为 shell 命令执行
  - 表达式值应在脚本生成前完成求值并安全转义

验证点:
  - [负向] 含特殊字符的 PR 标题绝不应被解释为 shell 命令执行
  - [非功能] 安全写法（先存入中间环境变量再引用）应正常工作

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Inline PR title | run: echo "PR title is ${{ atomgit.event.pull_request.title }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  pr-title-inj:
    name: Test PR title injection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Inline PR title
        run: |
          echo "PR title is ${{ atomgit.event.pull_request.title }}"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 含特殊字符的 PR 标题绝不应被解释为 shell 命令执行 | ✅ COVERED | 步骤通过 `${{ atomgit.event.pull_request.title }}` 将 PR 标题内联到 shell 脚本中，真实测试平台表达式求值阶段是否安全转义；断言 `must_not_contain injected_command_executed` 直接观测注入哨兵是否出现 |
| [非功能] 安全写法（先存入中间环境变量再引用）应正常工作 | ❌ MISSING | workflow 中无步骤将 PR 标题先存入中间环境变量再引用，未展示安全写法 |

### 问题

- **断言 2 — MISSING**: 规格要求验证"安全写法（先存入中间环境变量再引用）应正常工作"，但 workflow 仅有一种写法（直接内联），缺少对应的安全对照步骤。

## 5. 评级理由

一个验证点 COVERED（`${{ }}` 表达式真实测试注入行为），一个 MISSING（缺少安全写法对照步骤）。判定为部分不符。
