# SEC-BASE-01-001

- **标题**: pull_request_target 使用 base 分支的 workflow 版本
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_target 使用 base 分支的 workflow 版本**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-SEC-035

通过标准：
1. type=positive, target=run_logs, equals=base_branch_workflow_executed
2. type=negative, target=run_logs

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo from base | `echo "Executing base branch workflow"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches: [main]
jobs:
  base-version:
    name: Verify base workflow version
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo from base
        run: |
          echo "Executing base branch workflow"
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
| 1 | run_logs | positive | equals=base_branch_workflow_executed | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---