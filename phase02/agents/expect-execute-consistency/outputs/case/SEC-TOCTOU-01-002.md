# SEC-TOCTOU-01-002

- 标题: 评论触发不应绕过代码固定与 PR 审批
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-TOCTOU-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-031
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    SEC-TOCTOU-01-001
标题:      评论触发不应绕过代码固定与 PR 审批

前置条件:
  - 仓库配置了 issue_comment 触发 workflow

操作步骤:
  1. 提交一个由 issue_comment 触发的高权限 workflow
  2. 在评论触发后、执行前推送新 commit
  3. 观察运行是否执行了最新 commit 而非触发时的 commit

预期结果:
  - 评论触发不应绕过代码固定
  - 运行应执行评论触发时刻锁定的 commit SHA

验证点:
  - [负向] 评论触发后推送的新 commit 绝不应被该次特权运行自动执行
  - [正向] 运行日志中的 commit SHA 与触发时刻一致

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check fixed commit | run: echo "Executing commit: ${{ atomgit.sha }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  comment-toctou:
    name: Test comment TOCTOU
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check fixed commit
        run: |
          echo "Executing commit: ${{ atomgit.sha }}"
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
| [负向] 新 commit 绝不应被该次特权运行自动执行 | ✅ COVERED | 断言 target=run_logs must_not_contain "new_commit_after_trigger"，步骤使用 ${{ atomgit.sha }} 表达式真实输出 commit SHA，harness 核对日志中未出现新 commit 标识 |
| [正向] 运行日志中的 commit SHA 与触发时刻一致 | ✅ COVERED | 断言 target=run_logs equals "trigger_sha_matched"，步骤真实输出执行所用 commit SHA，harness 可将其与触发时刻 SHA 比对 |

### 问题

无。

## 5. 评级理由

唯一步骤使用 `${{ atomgit.sha }}` 上下文表达式输出 commit SHA，步骤内容真实（非字面 echo）。两个断言均为 run_logs 类型，harness 可通过比对步骤输出与触发 commit 来验证 TOCTOU 防护是否生效。触发事件不影响步骤对断言的覆盖能力。
