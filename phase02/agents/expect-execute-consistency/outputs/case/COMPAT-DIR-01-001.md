# COMPAT-DIR-01-001

- **标题**: 工作流目录差异——.gitcode/workflows/ 正常识别
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**工作流目录差异——.gitcode/workflows/ 正常识别**

- 触发事件: `push`
- 规格引用: INTENT-COMPAT-029

通过标准：
1. type=positive, target=run_status, equals=completed_success
2. type=positive, target=run_logs, eval=llm_assisted
3. type=positive, target=workflow_discovery, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) echo from gitcode di | `echo "GITCODE_DIR_RECOGNIZED_OK"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  verify-gitcode-dir:
    name: Verify .gitcode workflows dir
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) echo from gitcode dir
        run: |
          echo "GITCODE_DIR_RECOGNIZED_OK"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed_success | ✅ GENUINE | 状态断言 completed_success 可被步骤行为验证 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | workflow_discovery | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---