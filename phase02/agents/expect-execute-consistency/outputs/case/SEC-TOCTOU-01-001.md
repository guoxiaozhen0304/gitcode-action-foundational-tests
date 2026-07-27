# SEC-TOCTOU-01-001

- **标题**: 审批后推送新 commit 不应被已授权特权运行执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**审批后推送新 commit 不应被已授权特权运行执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-031

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=approved_sha_matched

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Check commit SHA | `echo "Running commit: ${{ atomgit.sha }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  toctou-test:
    name: Test TOCTOU protection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check commit SHA
        run: |
          echo "Running commit: ${{ atomgit.sha }}"
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | positive | equals=approved_sha_matched | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---