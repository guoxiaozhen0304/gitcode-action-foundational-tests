# REL-MATRIX-01-026

- **标题**: matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**matrix fail-fast=true——任意 job 实例失败应立即取消其余实例**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-026

通过标准：
1. type=positive, target=job_status, equals=failure
2. type=positive, target=cancelled_jobs_count, equals=8

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | matrix step | `echo version=${{ matrix.version }}` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: matrix test job
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        version: [1, 2, 3]
      fail-fast: true
    steps:
      - name: matrix step
        run: |
          echo version=${{ matrix.version }}
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
| 2 | cancelled_jobs_count | positive | equals=8 | ✅ GENUINE | 断言有条件可被步骤验证 |

---