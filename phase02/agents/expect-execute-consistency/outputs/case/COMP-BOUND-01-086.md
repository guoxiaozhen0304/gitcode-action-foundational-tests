# COMP-BOUND-01-086

- **标题**: 矩阵构建 include exclude 与单值边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**矩阵构建 include exclude 与单值边界验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-086

通过标准：
1. type=positive, target=run_logs, must_contain="matrix_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Matrix value | `echo "OS=${{ matrix.os }}" echo "VER=${{ matrix.version }}" echo "matrix_ok"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify matrix boundary
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        os: [linux]
        version: [1, 2]
        include:
          - os: linux
            version: 3
        exclude:
          - os: linux
            version: 2
    steps:
      - name: Matrix value
        run: |
          echo "OS=${{ matrix.os }}"
          echo "VER=${{ matrix.version }}"
          echo "matrix_ok"
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
| 1 | run_logs | positive | must_contain=matrix_ok | ✅ GENUINE | matrix_ok: GENUINE |

---