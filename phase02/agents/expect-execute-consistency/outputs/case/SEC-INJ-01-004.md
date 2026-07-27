# SEC-INJ-01-004

- 标题: 不可信 commit message 不可直接插进 run 脚本导致命令注入
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   SEC-INJ-01-004
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-012
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      不可信 commit message 不可直接插进 run 脚本导致命令注入

前置条件:
  - 存在一条 commit message 含反引号或分号的 push

操作步骤:
  1. 提交一个由 push 触发的 workflow，在 run 中引用 commit message
  2. 推送一条含 shell 元字符的 commit

预期结果:
  - commit message 中的 shell 元字符不应被解释为命令执行
  - 安全写法（中间环境变量）应正常生效

验证点:
  - [负向] 含反引号或分号的 commit message 绝不应被解释为命令执行
  - [非功能] 安全写法（中间环境变量）应正常生效

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Inline commit message | run: echo "Message is ${{ atomgit.event.commits[0].message }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  commit-inj:
    name: Test commit message injection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Inline commit message
        run: |
          echo "Message is ${{ atomgit.event.commits[0].message }}"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | push |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 含反引号或分号的 commit message 绝不应被解释为命令执行 | ✅ COVERED | 步骤通过 `${{ atomgit.event.commits[0].message }}` 将 commit message 内联到 shell 脚本中，真实测试平台表达式求值是否安全转义；断言 `must_not_contain injected_command_executed` 直接观测注入哨兵 |
| [非功能] 安全写法（中间环境变量）应正常生效 | ❌ MISSING | workflow 中无步骤将 commit message 先存入中间环境变量再引用，未展示安全对照写法 |

### 问题

- **断言 2 — MISSING**: 规格要求验证"安全写法（中间环境变量）应正常生效"，但 workflow 仅有一种写法（直接内联），缺少对应的安全对照步骤。

## 5. 评级理由

一个验证点 COVERED（`${{ }}` 表达式真实测试注入行为），一个 MISSING（缺少安全写法对照步骤）。判定为部分不符。
