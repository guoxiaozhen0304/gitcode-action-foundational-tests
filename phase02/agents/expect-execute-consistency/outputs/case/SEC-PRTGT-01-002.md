# SEC-PRTGT-01-002

- 标题: pull_request_target 无审批不执行 fork PR 代码
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-PRTGT-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-002
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    SEC-PRTGT-01-001
标题:      pull_request_target 无审批不执行 fork PR 代码

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 在 base 分支 workflow 中使用 pull_request_target 触发
  2. 显式 checkout fork PR 的 head sha
  3. 在无审批状态下触发 workflow

预期结果:
  - 未审批状态下 job 应处于挂起或拒绝态
  - 不应直接执行 fork PR 的代码

验证点:
  - [负向] 绝不应在无审批情况下，让 pull_request_target 的 job 直接执行 fork PR 的构建脚本
  - [正向] 若存在审批机制，未审批状态下 job 应处于挂起或拒绝态

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Checkout PR head | uses: checkout, ref: ${{ atomgit.event.pull_request.head.sha }} | 是 |
| 2 | Run build | run: echo "Building PR code" | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches: [main]
jobs:
  unapproved-checkout:
    name: Unapproved checkout test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Checkout PR head
        uses: checkout
        with:
          ref: ${{ atomgit.event.pull_request.head.sha }}
      - name: Run build
        run: |
          echo "Building PR code"
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
| [负向] 未审批时不应让 job 直接执行 fork PR 代码 | ✅ COVERED | 断言 target=run_status must_not_equal success_without_approval，harness 可直接观测运行状态；checkout 步骤使用了 ${{ }} 表达式和 uses: action，属真实操作 |
| [正向] 未审批状态下 job 应处于挂起或拒绝态 | ✅ COVERED | 断言 target=run_status equals pending_or_blocked，harness 可观测平台是否阻止执行 |

### 问题

无。

## 5. 评级理由

两个断言均为 run_status 类型，harness 可直接观测 workflow 运行状态（被平台阻止或成功执行）。checkout 步骤包含 ${{ }} 表达式和 uses: action，为真实步骤。步骤能产生断言所需的可观测行为。
