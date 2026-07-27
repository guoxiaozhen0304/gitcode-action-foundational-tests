# SEC-ORG-01-001

- **标题**: 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**可见范围外仓库的 workflow 绝不应读到组织级 secret 原值**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-039

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="ORG_SHARED_KEY"
2. type=positive, target=run_logs, equals=empty_or_error_outside_scope
3. type=nonfunctional, target=visibility_change, equals=effective_immediately_no_cache_window

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo org secret value | `echo "ORG_SECRET_VALUE: ${{ secrets.ORG_SHARED_KEY }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  org-secret-scope:
    name: Reference org secret outside scope
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo org secret value
        run: |
          echo "ORG_SECRET_VALUE: ${{ secrets.ORG_SHARED_KEY }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `org-scoped-secret` |
| Secrets | `['ORG_SHARED_KEY']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=ORG_SHARED_KEY | ✅ GENUINE | 步骤使用 ORG_SHARED_KEY，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_logs | positive | equals=empty_or_error_outside_scope | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 3 | visibility_change | nonfunctional | equals=effective_immediately_no_cache_window | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---