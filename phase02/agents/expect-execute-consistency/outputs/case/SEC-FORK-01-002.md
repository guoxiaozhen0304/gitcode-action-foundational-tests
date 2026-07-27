# SEC-FORK-01-002

- **标题**: fork PR 中 secrets 引用返回空值且 job 不崩溃
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**fork PR 中 secrets 引用返回空值且 job 不崩溃**

- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-001

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="API_KEY"
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Check env empty | `if [ -z "$API_KEY" ]; then   echo "API_KEY is empty as expected" else   echo "AP` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  test-empty:
    name: Test empty secret
    runs-on: [ubuntu-latest, x64, small]
    env:
      API_KEY: ${{ secrets.API_KEY }}
    steps:
      - name: Check env empty
        run: |
          if [ -z "$API_KEY" ]; then
            echo "API_KEY is empty as expected"
          else
            echo "API_KEY is not empty"
            exit 1
          fi
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-secrets` |
| Secrets | `['API_KEY']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=API_KEY | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 API_KEY |
| 2 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

### 问题

**断言 1 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 API_KEY

---