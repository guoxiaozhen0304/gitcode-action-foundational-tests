# COMP-STEP-01-069

- **标题**: step 必填与核心字段 name run uses 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**step 必填与核心字段 name run uses 验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-069

通过标准：
1. type=positive, target=run_logs, must_contain="run_ok"
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Run step | `echo "run_ok"` |  | ❌ VACUOUS |
| 2 | Uses step | `checkout` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify step core fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Run step
        run: |
          echo "run_ok"
      - name: Uses step
        uses: checkout
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
| 1 | run_logs | positive | must_contain=run_ok | ❌ VACUOUS | run_ok: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

### 问题

**断言 1 — VACUOUS**❌: run_ok: VACUOUS (步骤仅 echo，未执行功能)

---