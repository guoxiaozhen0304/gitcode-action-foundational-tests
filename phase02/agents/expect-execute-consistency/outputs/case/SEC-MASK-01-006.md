# SEC-MASK-01-006

- **标题**: Secret 日志脱敏不可通过分片输出绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Secret 日志脱敏不可通过分片输出绕过**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-008

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="DEPLOY_TOKEN"
2. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo secret character by  | `secret="${{ secrets.DEPLOY_TOKEN }}" for (( i=0; i<${#secret}; i++ )); do   echo` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  fragment-bypass:
    name: Test fragment bypass
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo secret character by character
        run: |
          secret="${{ secrets.DEPLOY_TOKEN }}"
          for (( i=0; i<${#secret}; i++ )); do
            echo "char $i: ${secret:$i:1}"
          done
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 DEPLOY_TOKEN，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---