# COMPAT-ARTIFACT-01-002

- **标题**: upload-artifact 保留期行为等价性
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**upload-artifact 保留期行为等价性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-026

通过标准：
1. type=positive, target=run_status, equals=completed_success
2. type=positive, target=run_logs, eval=llm_assisted
3. type=nonfunctional, target=artifact_state, eval=llm_assisted
4. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) create artifact file | `echo "RETENTION_TEST_MARKER" > retention_marker.txt` |  | ❌ VACUOUS |
| 2 | (TC) upload with retentio | `upload-artifact` |  | ✅ GENUINE |
| 3 | (TC) verify upload succes | `echo "ARTIFACT_UPLOADED_OK"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify-retention:
    name: Verify artifact retention
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) create artifact file
        run: |
          echo "RETENTION_TEST_MARKER" > retention_marker.txt
      - name: (TC) upload with retention
        uses: upload-artifact
        with:
          name: retention-test-artifact
          path: retention_marker.txt
          retention-days: 1
      - name: (TC) verify upload success
        run: |
          echo "ARTIFACT_UPLOADED_OK"
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
| 1 | run_status | positive | equals=completed_success | ✅ GENUINE | 状态断言 completed_success 可被步骤行为验证 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | artifact_state | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 4 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---