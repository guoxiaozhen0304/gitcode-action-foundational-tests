# SEC-ENV-01-002

- **标题**: 环境级 secret 审批前 workflow 不可读取
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**环境级 secret 审批前 workflow 不可读取**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-027

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_status, equals=pending_or_failed

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Try use env secret | `if [ -z "$PROD_TOKEN" ]; then   echo "secret not accessible before approval" els` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  env-secret-denied:
    name: Access env secret before approval
    runs-on: [ubuntu-latest, x64, small]
    environment: production
    steps:
      - name: Try use env secret
        run: |
          if [ -z "$PROD_TOKEN" ]; then
            echo "secret not accessible before approval"
          else
            echo "secret accessible unexpectedly"
            exit 1
          fi
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_status | positive | equals=pending_or_failed | ✅ GENUINE | 状态断言 pending_or_failed 可被步骤行为验证 |

---