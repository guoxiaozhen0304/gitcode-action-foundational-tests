# COMP-SECRET-01-002

- **标题**: secret 原始值不应以明文出现在标准日志中
- **维度**: 完备性
- **优先级**: P0
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**secret 原始值不应以明文出现在标准日志中**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-012

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="TEST_SECRET"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo secret via env | `echo "env secret is $MY_SECRET"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify no secret plaintext
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo secret via env
        env:
          MY_SECRET: ${{ secrets.TEST_SECRET }}
        run: |
          echo "env secret is $MY_SECRET"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['TEST_SECRET']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=TEST_SECRET | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 TEST_SECRET |

### 问题

**断言 1 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 TEST_SECRET

---