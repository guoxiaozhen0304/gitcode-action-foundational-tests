# COMP-STATUS-01-002

- **标题**: 失败 step 的日志完整保留且可查看
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**失败 step 的日志完整保留且可查看**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-017

通过标准：
1. type=positive, target=run_logs, contains="BEFORE_FAILURE_MARKER"
2. type=positive, target=run_logs, contains="ERROR_MARKER"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Before failure | `echo "BEFORE_FAILURE_MARKER"` |  | ❌ VACUOUS |
| 2 | Force failure | `echo "ERROR_MARKER" exit 1` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify failed step logs
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Before failure
        run: |
          echo "BEFORE_FAILURE_MARKER"
      - name: Force failure
        run: |
          echo "ERROR_MARKER"
          exit 1
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
| 1 | run_logs | positive | contains=BEFORE_FAILURE_MARKER | ❌ VACUOUS | BEFORE_FAILURE_MARKER: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | contains=ERROR_MARKER | ✅ GENUINE | ERROR_MARKER: GENUINE |

### 问题

**断言 1 — VACUOUS**❌: BEFORE_FAILURE_MARKER: VACUOUS (步骤仅 echo，未执行功能)

---