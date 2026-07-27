# SEC-SUPPLY-01-003

- **标题**: 第三方 Action 来源应具备信任边界（typosquatting 限制）
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**第三方 Action 来源应具备信任边界（typosquatting 限制）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-015

通过标准：
1. type=negative, target=run_status
2. type=positive, target=run_logs, equals=action_not_found_or_unapproved

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use typo action | `checkout-action@v1` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  typo-test:
    name: Test typosquatting rejection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Use typo action
        uses: checkout-action@v1
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative |  | ✅ GENUINE | 状态断言  可被步骤行为验证 |
| 2 | run_logs | positive | equals=action_not_found_or_unapproved | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---