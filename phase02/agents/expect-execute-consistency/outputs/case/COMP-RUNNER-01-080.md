# COMP-RUNNER-01-080

- **标题**: runner 上下文属性可访问性验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**runner 上下文属性可访问性验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-080

通过标准：
1. type=positive, target=run_logs, must_contain="NAME="
2. type=positive, target=run_logs, must_contain="TEMP="
3. type=positive, target=run_logs, must_contain="TOOL_CACHE="
4. type=positive, target=run_logs, must_contain="runner_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print runner props | `echo "NAME=${{ runner.name }}" echo "TEMP=${{ runner.temp }}" echo "TOOL_CACHE=$` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify runner context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print runner props
        run: |
          echo "NAME=${{ runner.name }}"
          echo "TEMP=${{ runner.temp }}"
          echo "TOOL_CACHE=${{ runner.tool_cache }}"
          echo "OS=${{ runner.os }}"
          echo "ARCH=${{ runner.arch }}"
          echo "runner_ok"
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
| 1 | run_logs | positive | must_contain=NAME= | ✅ GENUINE | NAME=: GENUINE |
| 2 | run_logs | positive | must_contain=TEMP= | ✅ GENUINE | TEMP=: GENUINE |
| 3 | run_logs | positive | must_contain=TOOL_CACHE= | ✅ GENUINE | TOOL_CACHE=: GENUINE |
| 4 | run_logs | positive | must_contain=runner_ok | ✅ GENUINE | runner_ok: GENUINE |

---