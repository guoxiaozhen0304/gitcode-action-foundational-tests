# COMP-CTX-01-052

- **标题**: 上下文在条件表达式 if 中注入验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**上下文在条件表达式 if 中注入验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-051

通过标准：
1. type=positive, target=run_logs, must_contain="always"
2. type=positive, target=run_logs, must_contain="conditional_env_passed"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Always run | `echo "always"` |  | ❌ VACUOUS |
| 2 | Conditional env | `echo "conditional_env_passed"` | ${{ env.ALWAYS_TRUE == 'y | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify context in if expressions
    runs-on: [ubuntu-latest, x64, small]
    if: ${{ atomgit.ref == 'refs/heads/main' || true }}
    steps:
      - name: Always run
        run: |
          echo "always"
      - name: Conditional env
        if: ${{ env.ALWAYS_TRUE == 'yes' }}
        env:
          ALWAYS_TRUE: yes
        run: |
          echo "conditional_env_passed"
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
| 1 | run_logs | positive | must_contain=always | ❌ VACUOUS | always: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | must_contain=conditional_env_passed | ✅ GENUINE | conditional_env_passed: GENUINE |

### 问题

**断言 1 — VACUOUS**❌: always: VACUOUS (步骤仅 echo，未执行功能)

---