# SEC-PRTGT-01-002

- **标题**: pull_request_target 无审批不执行 fork PR 代码
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_target 无审批不执行 fork PR 代码**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-SEC-002

通过标准：
1. type=negative, target=run_status
2. type=positive, target=run_status, equals=pending_or_blocked

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Checkout PR head | `checkout` |  | ✅ GENUINE |
| 2 | Run build | `echo "Building PR code"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

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

| 触发事件 | `pull_request_target` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative |  | ✅ GENUINE | 状态断言  可被步骤行为验证 |
| 2 | run_status | positive | equals=pending_or_blocked | ✅ GENUINE | 状态断言 pending_or_blocked 可被步骤行为验证 |

---