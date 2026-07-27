# USE-DOC-01-005

- **标题**: configure-steps 的 shell 类型与命令语言不匹配示例照抄失败
- **维度**: 易用性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**configure-steps 的 shell 类型与命令语言不匹配示例照抄失败**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-033

通过标准：
1. type=positive, target=run_status, equals=failure
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | doc example bash step | `Write-Host "hello"` |  | ✅ GENUINE |
| 2 | doc example python step | `echo "hello"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  bash-example:
    name: shell bash with PowerShell command
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: doc example bash step
        shell: bash
        run: |
          Write-Host "hello"
  python-example:
    name: shell python with shell command
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: doc example python step
        shell: python
        run: |
          echo "hello"
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
| 1 | run_status | positive | equals=failure | ❌ IMPOSSIBLE | 期望 !=success 但无步骤可能失败 |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

### 问题

**断言 1 — IMPOSSIBLE**❌: 期望 !=success 但无步骤可能失败

---