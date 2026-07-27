# COMPAT-SHELL-01-001

- **标题**: 默认 shell 隐式行为差异 - 未显式声明时是否为 bash
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**默认 shell 隐式行为差异 - 未显式声明时是否为 bash**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-001

通过标准：
1. type=positive, target=run_logs, contains="bash"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | print shell info | `echo "Current shell: $SHELL" echo "Shell via ps: $(ps -p $$ -o comm=)"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  check-shell:
    name: Check default shell
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: print shell info
        run: |
          echo "Current shell: $SHELL"
          echo "Shell via ps: $(ps -p $$ -o comm=)"
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
| 1 | run_logs | positive | contains=bash | ✅ GENUINE | bash: GENUINE (uses action 内部输出) |

---