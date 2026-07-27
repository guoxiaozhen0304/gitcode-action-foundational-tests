# COMP-CTX-01-051

- **标题**: 上下文在 workflow job step 各级注入验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**上下文在 workflow job step 各级注入验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-051

通过标准：
1. type=positive, target=run_logs, must_contain="WF_REF=refs/"
2. type=positive, target=run_logs, must_contain="JOB_REF=refs/"
3. type=positive, target=run_logs, must_contain="JOB_STATUS="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Step context | `echo "WF_REF=$WF_REF" echo "JOB_REF=$JOB_REF" echo "JOB_STATUS=${{ job.status }}` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
env:
  WF_REF: ${{ atomgit.ref }}
jobs:
  verify:
    name: Verify context injection at all levels
    runs-on: [ubuntu-latest, x64, small]
    env:
      JOB_REF: ${{ env.WF_REF }}
    steps:
      - name: Step context
        run: |
          echo "WF_REF=$WF_REF"
          echo "JOB_REF=$JOB_REF"
          echo "JOB_STATUS=${{ job.status }}"
          echo "ATOMGIT_REF=${{ atomgit.ref }}"
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
| 1 | run_logs | positive | must_contain=WF_REF=refs/ | ❌ MISSING_SOURCE | WF_REF=refs/: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=JOB_REF=refs/ | ❌ MISSING_SOURCE | JOB_REF=refs/: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=JOB_STATUS= | ✅ GENUINE | JOB_STATUS=: GENUINE |

### 问题

**断言 1 — MISSING_SOURCE**❌: WF_REF=refs/: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: JOB_REF=refs/: MISSING_SOURCE (无步骤产出此字符串)

---