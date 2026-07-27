# SEC-PRTGT-01-001

- **标题**: pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-SEC-002

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="DEPLOY_TOKEN"
2. type=positive, target=run_status, equals=blocked_or_pending

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Checkout PR head | `checkout` |  | ✅ GENUINE |
| 2 | Attempt secret access | `echo "secret is ${{ secrets.DEPLOY_TOKEN }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

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

| 触发事件 | `pull_request_target` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 DEPLOY_TOKEN，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_status | positive | equals=blocked_or_pending | ✅ GENUINE | 状态断言 blocked_or_pending 可被步骤行为验证 |

---