# USE-CTX-01-001

- **标题**: 使用 atomgit 上下文时表达式正常求值
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**使用 atomgit 上下文时表达式正常求值**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-002

通过标准：
1. type=positive, target=run_logs, contains="ref=refs/heads/"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo atomgit ref | `echo "ref=${{ atomgit.ref }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-ctx:
    name: test atomgit context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo atomgit ref
        run: |
          echo "ref=${{ atomgit.ref }}"
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
| 1 | run_logs | positive | contains=ref=refs/heads/ | ❌ MISSING_SOURCE | ref=refs/heads/: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: ref=refs/heads/: MISSING_SOURCE (无步骤产出此字符串)

---