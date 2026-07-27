# COMPAT-PERM-01-005

- **标题**: permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-030

通过标准：
1. type=positive, target=run_logs, eval=llm_assisted
2. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Try read with token | `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $ATOMGIT_TOKEN"` |  | ✅ GENUINE |
| 2 | Try write with token | `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $ATOMGIT_TOKEN"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions: {}
jobs:
  test-empty-perm:
    name: Test empty permissions
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Try read with token
        run: |
          curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $ATOMGIT_TOKEN" "$ATOMGIT_API_URL/user" || true
      - name: Try write with token
        run: |
          curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $ATOMGIT_TOKEN" -X POST "$ATOMGIT_API_URL/user/repos" -d '{"name":"test"}' || true
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
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---