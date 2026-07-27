# REL-RACE-01-048

- **标题**: 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-048

通过标准：
1. type=positive, target=job_a_status, equals=canceled
2. type=positive, target=job_b_status, equals=skipped

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step | `sleep 60` |  | ✅ GENUINE |
| 2 | should not run | `echo this should not run` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job_a:
    name: job A cancel target
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step
        run: |
          sleep 60
  job_b:
    name: job B failure condition
    runs-on: [ubuntu-latest, x64, small]
    needs: job_a
    if: failure()
    steps:
      - name: should not run
        run: |
          echo this should not run
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
| 1 | job_a_status | positive | equals=canceled | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | job_b_status | positive | equals=skipped | ✅ GENUINE | 断言有条件可被步骤验证 |

---