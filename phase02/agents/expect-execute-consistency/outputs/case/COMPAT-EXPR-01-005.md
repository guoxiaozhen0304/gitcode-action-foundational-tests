# COMPAT-EXPR-01-005

- **标题**: contains 表达式空值与空字符串边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**contains 表达式空值与空字符串边界**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-006

通过标准：
1. type=positive, target=run_logs, contains="empty needle:"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | test empty haystack | `echo "empty haystack: ${{ contains('', 'a') }}"` |  | ✅ GENUINE |
| 3 | test empty needle | `echo "empty needle: ${{ contains('abc', '') }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-contains-empty:
    name: Test contains empty boundaries
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: test empty haystack
        run: "echo \"empty haystack: ${{ contains('', 'a') }}\""
      - name: test empty needle
        run: "echo \"empty needle: ${{ contains('abc', '') }}\""
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
| 1 | run_logs | positive | contains=empty needle: | ✅ GENUINE | empty needle:: GENUINE |

---