# SEC-ENV-01-001

- **标题**: 环境级 secret 必须经审批后才能被 workflow 访问
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**环境级 secret 必须经审批后才能被 workflow 访问**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-027

通过标准：
1. type=positive, target=run_status, equals=success_after_approval
2. type=negative, target=run_logs, must_not_contain_secret="PROD_TOKEN"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use env secret | `echo "secret length is ${#PROD_TOKEN}"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  env-secret-approved:
    name: Access env secret after approval
    runs-on: [ubuntu-latest, x64, small]
    environment: production
    steps:
      - name: Use env secret
        run: |
          echo "secret length is ${#PROD_TOKEN}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-env-secrets` |
| Secrets | `['PROD_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success_after_approval | ✅ GENUINE | 状态断言 success_after_approval 可被步骤行为验证 |
| 2 | run_logs | negative | !secret=PROD_TOKEN | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 PROD_TOKEN |

### 问题

**断言 2 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 PROD_TOKEN

---