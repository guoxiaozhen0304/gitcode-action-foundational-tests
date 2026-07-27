# COMP-STAGES-01-001

- **标题**: stages 阶段间串行、阶段内 job 并行执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**stages 阶段间串行、阶段内 job 并行执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-007

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=stage_order, equals=serial_across_stages
3. type=positive, target=job_parallelism, equals=parallel_within_stage

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
  - name: build-stage
    jobs:
      build-a:
        name: Build A
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Build A step
            run: |
              echo "build-a"
      build-b:
        name: Build B
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Build B step
            run: |
              echo "build-b"
  - name: test-stage
    jobs:
      test:
        name: Test
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Test step
            run: |
              echo "test"
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
| 1 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | stage_order | positive | equals=serial_across_stages | ✅ GENUINE | 平台级断言 stage_order — 由 harness 在运行时观测 |
| 3 | job_parallelism | positive | equals=parallel_within_stage | ✅ GENUINE | 平台级断言 job_parallelism — 由 harness 在运行时观测 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

---