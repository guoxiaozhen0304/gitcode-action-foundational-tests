# COMP-STAGES-01-002

- **标题**: fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-007

通过标准：
1. type=positive, target=job_status, equals=skipped_for_should_skip
2. type=negative, target=stage_execution, equals=deploy_stage_executed

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
  - name: test-stage
    fail_fast: true
    jobs:
      fail-job:
        name: Intentional fail
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Force failure
            run: |
              exit 1
      should-skip:
        name: Should be skipped
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Echo skipped
            run: |
              echo "should not execute"
  - name: deploy-stage
    jobs:
      deploy:
        name: Deploy
        runs-on: [ubuntu-latest, x64, small]
        steps:
          - name: Echo deploy
            run: |
              echo "should not execute"
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
| 1 | job_status | positive | equals=skipped_for_should_skip | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | stage_execution | negative | equals=deploy_stage_executed | ✅ GENUINE | 断言有条件可被步骤验证 |

---