# COMPAT-ISOLATE-01-001

- **标题**: Runner 环境隔离——跨 job 文件隔离
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**Runner 环境隔离——跨 job 文件隔离**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-028

通过标准：
1. type=positive, target=run_logs, eval=llm_assisted
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted
4. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) write workspace mark | `echo "ISOLATION_MARKER_$(date +%s)" > workspace_marker.txt` |  | ✅ GENUINE |
| 2 | (TC) write tmp marker | `echo "ISOLATION_MARKER_TMP_$(date +%s)" > /tmp/isolation_marker.txt` |  | ✅ GENUINE |
| 3 | (TC) output marker names | `echo "workspace_marker=workspace_marker.txt" >> "$ATOMGIT_OUTPUT" echo "tmp_mark` |  | ❌ VACUOUS |
| 4 | (TC) verify workspace iso | `if ls workspace_marker.txt 2>/dev/null; then   echo "ISOLATION_BROKEN_WORKSPACE"` |  | ✅ GENUINE |
| 5 | (TC) verify tmp isolation | `if ls /tmp/isolation_marker.txt 2>/dev/null; then   echo "ISOLATION_BROKEN_TMP" ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-write:
    name: Write isolation markers
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) write workspace marker
        run: |
          echo "ISOLATION_MARKER_$(date +%s)" > workspace_marker.txt
      - name: (TC) write tmp marker
        run: |
          echo "ISOLATION_MARKER_TMP_$(date +%s)" > /tmp/isolation_marker.txt
      - name: (TC) output marker names
        run: |
          echo "workspace_marker=workspace_marker.txt" >> "$ATOMGIT_OUTPUT"
          echo "tmp_marker=/tmp/isolation_marker.txt" >> "$ATOMGIT_OUTPUT"
  job-verify:
    name: Verify file isolation
    runs-on: [ubuntu-latest, x64, small]
    needs: job-write
    steps:
      - name: (TC) verify workspace isolation
        run: |
          if ls workspace_marker.txt 2>/dev/null; then
            echo "ISOLATION_BROKEN_WORKSPACE"
            exit 1
          else
            echo "WORKSPACE_ISOLATED_OK"
          fi
      - name: (TC) verify tmp isolation
        run: |
          if ls /tmp/isolation_marker.txt 2>/dev/null; then
            echo "ISOLATION_BROKEN_TMP"
            exit 1
          else
            echo "TMP_ISOLATED_OK"
          fi
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
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 4 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---