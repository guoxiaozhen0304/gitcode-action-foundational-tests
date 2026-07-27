# USE-ENV-01-004

- **标题**: job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证）
- **维度**: 易用性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-046

通过标准：
1. type=positive, target=run_logs, contains="expr=[prod]"
2. type=positive, target=run_logs, contains="shell=[prod]"
3. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | read env both layers | `echo "shell=[$APP_ENV]" echo "expr=[${{ env.APP_ENV }}]"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  env-probe:
    name: job env injection probe
    runs-on: [ubuntu-latest, x64, small]
    env:
      APP_ENV: prod
    steps:
      - name: read env both layers
        run: |
          echo "shell=[$APP_ENV]"
          echo "expr=[${{ env.APP_ENV }}]"
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
| 1 | run_logs | positive | contains=expr=[prod] | ❌ MISSING_SOURCE | expr=[prod]: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | contains=shell=[prod] | ❌ MISSING_SOURCE | shell=[prod]: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

### 问题

**断言 1 — MISSING_SOURCE**❌: expr=[prod]: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: shell=[prod]: MISSING_SOURCE (无步骤产出此字符串)

---