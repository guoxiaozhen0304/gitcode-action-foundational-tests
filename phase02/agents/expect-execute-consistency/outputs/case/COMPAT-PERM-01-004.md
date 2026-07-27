# COMPAT-PERM-01-004

- **标题**: permissions 命名差异——GitCode repository 权限项正常生效
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**permissions 命名差异——GitCode repository 权限项正常生效**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-030

通过标准：
1. type=positive, target=run_status, equals=completed_success
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted
4. type=negative, target=workflow_parse, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) checkout with reposi | `checkout` |  | ✅ GENUINE |
| 2 | (TC) verify repo access | `if [ -f "README.md" ]; then   echo "REPOSITORY_PERM_OK" else   echo "REPOSITORY_` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions:
  repository: read
jobs:
  verify-repository-perm:
    name: Verify repository permission works
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) checkout with repository read
        uses: checkout
      - name: (TC) verify repo access
        run: |
          if [ -f "README.md" ]; then
            echo "REPOSITORY_PERM_OK"
          else
            echo "REPOSITORY_PERM_FAILED"
            exit 1
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
| 1 | run_status | positive | equals=completed_success | ✅ GENUINE | 状态断言 completed_success 可被步骤行为验证 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 4 | workflow_parse | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---