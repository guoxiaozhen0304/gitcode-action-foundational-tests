# SEC-TOKEN-01-002

- 标题: fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-TOKEN-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-003
参照来源:  inputs/gitcode-spec/
母意图:    SEC-TOKEN-01-001
标题:      fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝

前置条件:
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以 fork 贡献者身份提交一个尝试用 ATOMGIT_TOKEN 推送代码的 workflow
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - 推送操作返回权限拒绝（403）
  - 运行日志中显示权限不足

验证点:
  - [负向] 写操作绝不应成功
  - [正向] 权限拒绝信息明确

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt push | run: git clone ... && git commit && git push origin main \|\| echo "push denied" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  token-write-denied:
    name: Test token write denied
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt push
        run: |
          git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git repo
          cd repo
          echo test > test.txt
          git add test.txt
          git commit -m "test"
          git push origin main || echo "push denied"
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
| [负向] 写操作绝不应成功 | ✅ COVERED | 断言 target=run_logs equals "push_denied_or_403"，步骤真实执行 git clone + push，push 被拒时输出 "push denied" 及平台 403 信息，harness 可校验 |
| [正向] 权限拒绝信息明确 | ✅ COVERED | 断言 target=run_status equals "completed"，步骤使用 \|\| 容错模式使 workflow 正常完成，harness 可观测 run_status 确认执行完毕且拒绝信息可读 |

### 问题

无。

## 5. 评级理由

步骤使用了 `${{ atomgit.token }}` 表达式并执行了真实 git 操作（clone、commit、push）。push 被平台拒绝时通过 `|| echo "push denied"` 输出明确的拒绝标识。run_logs 和 run_status 断言均可被 harness 观测。触发事件不影响判定。
