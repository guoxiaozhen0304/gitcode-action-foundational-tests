# REL-API-01-065

- **标题**: API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-065

通过标准：
1. type=positive, target=http_200_ratio, equals=100%
2. type=negative, target=http_error_codes, contains="429"
3. type=nonfunctional, target=response_time_p95_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step | `sleep 30` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: reliability test job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step
        run: |
          sleep 30
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
| 1 | http_200_ratio | positive | equals=100% | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | http_error_codes | negative | contains=429 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | response_time_p95_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---