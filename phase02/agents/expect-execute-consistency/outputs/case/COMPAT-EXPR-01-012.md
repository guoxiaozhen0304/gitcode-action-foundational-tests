# COMPAT-EXPR-01-012

- **标题**: fromJSON() 函数缺失时的降级行为
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fromJSON() 函数缺失时的降级行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-010

通过标准：
1. type=negative, target=run_logs
2. type=nonfunctional, target=error_message, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Test fromJSON function in | `RESULT="${{ fromJSON('{\"a\": 1}').a }}" echo "fromjson-result=$RESULT"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-fromjson:
    name: Test fromJSON function availability
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Test fromJSON function in run block
        run: |
          RESULT="${{ fromJSON('{\"a\": 1}').a }}"
          echo "fromjson-result=$RESULT"
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---