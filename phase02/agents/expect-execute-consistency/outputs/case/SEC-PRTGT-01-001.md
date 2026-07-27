# SEC-PRTGT-01-001

- 标题: pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-PRTGT-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-002
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 在 base 分支 workflow 中使用 pull_request_target 触发
  2. 显式 checkout fork PR 的 head sha 并执行脚本
  3. 观察 secrets 是否可被该脚本访问

预期结果:
  - 系统应阻止或限制在 pull_request_target 中直接执行未经审核的 fork PR 代码
  - secrets 不应被不可信代码直接读取

验证点:
  - [负向] 运行日志中不应出现 DEPLOY_TOKEN 明文
  - [正向] 若存在审批机制，未审批状态下 job 应处于挂起或拒绝态

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Checkout PR head | uses: checkout (ref: ${{ atomgit.event.pull_request.head.sha }}) | 是 |
| 2 | Attempt secret access | run: echo "secret is ${{ secrets.DEPLOY_TOKEN }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches: [main]
jobs:
  risky-checkout:
    name: Risky checkout test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Checkout PR head
        uses: checkout
        with:
          ref: ${{ atomgit.event.pull_request.head.sha }}
      - name: Attempt secret access
        run: |
          echo "secret is ${{ secrets.DEPLOY_TOKEN }}"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request_target |
| as | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 运行日志中不应出现 DEPLOY_TOKEN 明文 | ✅ COVERED | 步骤1 使用 `uses: checkout` + `${{ atomgit.event.pull_request.head.sha }}` 真实 checkout fork PR 代码，步骤2 通过 `${{ secrets.DEPLOY_TOKEN }}` 真实访问 secret；断言 `must_not_contain_secret` 验证 secret 值不泄露 |
| [正向] 若存在审批机制，未审批状态下 job 应处于挂起或拒绝态 | ✅ COVERED | 步骤真实构建 pull_request_target 下 checkout 不可信代码的危险场景，断言 `run_status equals blocked_or_pending` 检验平台是否对此场景实施审批/拒绝控制 |

### 问题

无。两个验证点均被步骤真实覆盖。

## 5. 评级理由

步骤使用 `uses: checkout` action 和 `${{ secrets.DEPLOY_TOKEN }}` 真实构建 pull_request_target 下的高危场景，断言直接观测 secret 泄露和 job 状态。所有验证点均 COVERED。
