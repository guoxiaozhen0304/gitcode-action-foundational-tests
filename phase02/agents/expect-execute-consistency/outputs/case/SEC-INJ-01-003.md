# SEC-INJ-01-003

- 标题: 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   SEC-INJ-01-003
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-011
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入

前置条件:
  - 存在一条包含 shell 元字符的评论

操作步骤:
  1. 提交一个由 issue_comment 触发的 workflow，在 run 中引用评论 body
  2. 提交一条含 shell 元字符的评论触发 workflow

预期结果:
  - 评论 body 中的 shell 元字符不应被解释为命令执行
  - 即使评论被编辑，重新触发时仍应维持安全过滤

验证点:
  - [负向] 含 shell 元字符的评论内容绝不应被解释为命令执行
  - [非功能] 即使评论被编辑，重新触发时仍应维持安全过滤

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Inline comment body | run: echo "Comment is ${{ atomgit.event.comment.body }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  comment-inj:
    name: Test comment injection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Inline comment body
        run: |
          echo "Comment is ${{ atomgit.event.comment.body }}"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | issue_comment |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 含 shell 元字符的评论内容绝不应被解释为命令执行 | ✅ COVERED | 步骤通过 `${{ atomgit.event.comment.body }}` 将评论内容内联到 shell 脚本中，真实测试平台表达式求值是否防止注入；断言 `must_not_contain injected_command_executed` 直接观测注入哨兵 |
| [非功能] 即使评论被编辑，重新触发时仍应维持安全过滤 | ❌ MISSING | workflow 仅响应 `types: [created]`，无步骤验证编辑后重新触发仍维持安全过滤 |

### 问题

- **断言 2 — MISSING**: 规格要求验证"即使评论被编辑，重新触发时仍应维持安全过滤"，但 workflow 仅监听 `created` 事件类型，缺少 `edited` 类型及对应的验证步骤。

## 5. 评级理由

一个验证点 COVERED（`${{ }}` 表达式真实测试注入行为），一个 MISSING（缺少评论编辑重触发的验证步骤）。判定为部分不符。
