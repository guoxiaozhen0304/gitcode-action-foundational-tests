# REL-CONTINUE-01-030

- **标题**: continue-on-error=true——job 失败后 workflow 不应终止
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**continue-on-error=true——job 失败后 workflow 不应终止**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-030

通过标准：
1. type=positive, target=job_a_status, equals=failure
2. type=positive, target=job_b_status, equals=success
3. type=positive, target=workflow_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | fail step | `exit 1` |  | ✅ GENUINE |
| 2 | success step | `echo job_b executed` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job_a:
    name: job with continue on error
    runs-on: [ubuntu-latest, x64, small]
    continue-on-error: true
    steps:
      - name: fail step
        run: |
          exit 1
  job_b:
    name: downstream after continue
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: success step
        run: |
          echo job_b executed
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
| 1 | job_a_status | positive | equals=failure | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | job_b_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | workflow_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |

---