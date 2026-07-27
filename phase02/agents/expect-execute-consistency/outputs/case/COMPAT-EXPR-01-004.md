# COMPAT-EXPR-01-004

- **标题**: contains 表达式大小写敏感边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**contains 表达式大小写敏感边界**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-006

通过标准：
1. type=positive, target=run_logs, contains="exact case match: true"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | test lowercase match | `echo "lowercase match: ${{ contains('Hello World', 'world') }}"` |  | ✅ GENUINE |
| 3 | test exact case match | `echo "exact case match: ${{ contains('Hello World', 'World') }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-contains-case:
    name: Test contains case sensitivity
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: test lowercase match
        run: "echo \"lowercase match: ${{ contains('Hello World', 'world') }}\""
      - name: test exact case match
        run: "echo \"exact case match: ${{ contains('Hello World', 'World') }}\""
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
| 1 | run_logs | positive | contains=exact case match: true | ✅ GENUINE | exact case match: true: GENUINE (uses action 内部输出) |

---