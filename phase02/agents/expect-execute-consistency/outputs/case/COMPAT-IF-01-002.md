# COMPAT-IF-01-002

- **标题**: continue-on-error 标记后失败 step 不阻断后续执行
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**continue-on-error 标记后失败 step 不阻断后续执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-003

通过标准：
1. type=positive, target=run_logs, contains="This should appear"
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | force failure with contin | `exit 1` |  | ✅ GENUINE |
| 2 | should still run | `echo "This should appear"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-continue:
    name: Test continue on error
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: force failure with continue
        continue-on-error: true
        run: |
          exit 1
      - name: should still run
        run: |
          echo "This should appear"
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
| 1 | run_logs | positive | contains=This should appear | ❌ VACUOUS | This should appear: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

### 问题

**断言 1 — VACUOUS**❌: This should appear: VACUOUS (步骤仅 echo，未执行功能)

---