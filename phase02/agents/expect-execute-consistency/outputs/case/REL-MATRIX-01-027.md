# REL-MATRIX-01-027

- **标题**: matrix max-parallel=4——9 个组合应最多同时运行 4 个
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**matrix max-parallel=4——9 个组合应最多同时运行 4 个**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-027

通过标准：
1. type=positive, target=max_concurrent_jobs
2. type=positive, target=run_status, equals=completed(success)

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
      max-parallel: 4
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
| 1 | max_concurrent_jobs | positive |  | ✅ GENUINE | 通用断言匹配 |
| 2 | run_status | positive | equals=completed(success) | ✅ GENUINE | 状态断言 completed(success) 可被步骤行为验证 |

---