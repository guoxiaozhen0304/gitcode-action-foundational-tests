# COMPAT-IF-01-001

- **标题**: step 失败后后续 step 默认跳过行为
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**step 失败后后续 step 默认跳过行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-003

通过标准：
1. type=positive, target=run_status, equals=failure
2. type=negative, target=run_logs, contains="This should not appear"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | force failure | `exit 1` |  | ✅ GENUINE |
| 2 | should be skipped | `echo "This should not appear"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-skip:
    name: Test step failure skip
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: force failure
        run: |
          exit 1
      - name: should be skipped
        run: |
          echo "This should not appear"
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
| 1 | run_status | positive | equals=failure | ✅ GENUINE | 存在故意失败步骤或 continue-on-error |
| 2 | run_logs | negative | contains=This should not appear | ❌ VACUOUS | This should not appear: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 2 — VACUOUS**❌: This should not appear: VACUOUS (步骤仅 echo，未执行功能)

---