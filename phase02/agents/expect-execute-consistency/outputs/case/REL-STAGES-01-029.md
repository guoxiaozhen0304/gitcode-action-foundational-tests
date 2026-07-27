# REL-STAGES-01-029

- **标题**: stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-029

通过标准：
1. type=positive, target=job_status, equals=failure
2. type=positive, target=cancelled_jobs_count

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
stages:
  - name: test_stage
    fail_fast: true
    jobs:
      job_a:
        name: stage job A
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: fail step
            run: |
              exit 1
      job_b:
        name: stage job B
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: sleep step
            run: |
              sleep 30
      job_c:
        name: stage job C
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: sleep step
            run: |
              sleep 30
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
| 1 | job_status | positive | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | cancelled_jobs_count | positive |  | ✅ GENUINE | 通用断言匹配 |

---