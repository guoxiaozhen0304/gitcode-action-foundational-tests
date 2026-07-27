# SEC-ORG-01-002

- **标题**: fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离）
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离）**

- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-039

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="ORG_SHARED_KEY"
2. type=positive, target=run_logs, equals=fork_pr_org_secret_isolated

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt to echo org secre | `echo "ORG_SECRET_VALUE: ${{ secrets.ORG_SHARED_KEY }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  org-secret-fork:
    name: Fork PR must not read org secret
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt to echo org secret
        run: |
          echo "ORG_SECRET_VALUE: ${{ secrets.ORG_SHARED_KEY }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `org-scoped-secret` |
| Secrets | `['ORG_SHARED_KEY']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=ORG_SHARED_KEY | ✅ GENUINE | 步骤使用 ORG_SHARED_KEY，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_logs | positive | equals=fork_pr_org_secret_isolated | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---