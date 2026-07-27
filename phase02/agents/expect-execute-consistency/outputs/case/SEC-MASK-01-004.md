# SEC-MASK-01-004

- **标题**: Secret 日志脱敏不可通过字符串拼接或插值绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Secret 日志脱敏不可通过字符串拼接或插值绕过**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-006

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="API_KEY"
2. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo secret in parts | `part1=$(echo "${{ secrets.API_KEY }}" | cut -c1-4) part2=$(echo "${{ secrets.API` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  concat-bypass:
    name: Test concat bypass
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo secret in parts
        run: |
          part1=$(echo "${{ secrets.API_KEY }}" | cut -c1-4)
          part2=$(echo "${{ secrets.API_KEY }}" | cut -c5-8)
          echo "part1=$part1 part2=$part2"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['API_KEY']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=API_KEY | ✅ GENUINE | 步骤使用 API_KEY，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---