# REL-MATRIX-01-038

- **标题**: 大规模 matrix——20 个组合应全部生成并正确调度
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**大规模 matrix——20 个组合应全部生成并正确调度**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-038

通过标准：
1. type=positive, target=generated_jobs_count, equals=20
2. type=positive, target=run_status, equals=completed(success)

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | verify matrix vars | `echo os=${{{{ matrix.os }}}} arch=${{{{ matrix.arch }}}} compiler=${{{{ matrix.c` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: matrix 20 combos test
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        os: [ubuntu, euler]
        arch: [x64, arm64]
        compiler: [gcc, clang]
        mode: [debug, release, profile]
    steps:
      - name: verify matrix vars
        run: |
          echo os=${{{{ matrix.os }}}} arch=${{{{ matrix.arch }}}} compiler=${{{{ matrix.compiler }}}} mode=${{{{ matrix.mode }}}}
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
| 1 | generated_jobs_count | positive | equals=20 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_status | positive | equals=completed(success) | ✅ GENUINE | 状态断言 completed(success) 可被步骤行为验证 |

---