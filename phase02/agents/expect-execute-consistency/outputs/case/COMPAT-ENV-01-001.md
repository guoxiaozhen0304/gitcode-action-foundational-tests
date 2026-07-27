# COMPAT-ENV-01-001

- **标题**: ATOMGIT_SHA 环境变量应正确返回触发提交 SHA
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**ATOMGIT_SHA 环境变量应正确返回触发提交 SHA**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-017

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo ATOMGIT_SHA | `echo "atomgit_sha=$ATOMGIT_SHA" echo "done"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test ATOMGIT_SHA env var
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo ATOMGIT_SHA
        run: |
          echo "atomgit_sha=$ATOMGIT_SHA"
          echo "done"
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
| 1 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---