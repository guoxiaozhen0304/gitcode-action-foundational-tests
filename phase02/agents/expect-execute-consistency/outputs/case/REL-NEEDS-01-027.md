# REL-NEEDS-01-027

- **标题**: needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行
- **维度**: 可靠性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-069

通过标准：
1. type=positive, target=job_b_status, equals=failure
2. type=positive, target=job_a_status, equals=skipped
3. type=positive, target=succeeded_instances_count, equals=2
4. type=negative, target=job_a_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | maybe fail step | `if [ "${{ matrix.version }}" = "2" ]; then exit 1; fi echo "matrix_instance_ok=$` |  | ✅ GENUINE |
| 2 | should be skipped step | `echo "this should not run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job_b:
    name: matrix upstream job partial fail
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        version: [1, 2, 3]
      fail-fast: false
    steps:
      - name: maybe fail step
        run: |
          if [ "${{ matrix.version }}" = "2" ]; then exit 1; fi
          echo "matrix_instance_ok=${{ matrix.version }}"
  job_a:
    name: downstream aggregator job
    runs-on: [ubuntu-latest, x64, small]
    needs: job_b
    steps:
      - name: should be skipped step
        run: |
          echo "this should not run"
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
| 1 | job_b_status | positive | equals=failure | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | job_a_status | positive | equals=skipped | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | succeeded_instances_count | positive | equals=2 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | job_a_status | negative | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |

---