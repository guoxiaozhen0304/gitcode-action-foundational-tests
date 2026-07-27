# COMP-PR-01-001

- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 触发 pull_request 时不可读取项目 secrets**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-004

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="DEPLOY_TOKEN"
2. type=positive, target=run_status, equals=success_or_blocked

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt to read secret | `echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches:
      - main
jobs:
  verify:
    name: Verify fork PR secret isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt to read secret
        run: |
          echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 DEPLOY_TOKEN，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_status | positive | equals=success_or_blocked | ✅ GENUINE | 状态断言 success_or_blocked 可被步骤行为验证 |

---