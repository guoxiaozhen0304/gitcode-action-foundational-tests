# COMPAT-RUNNER-01-008

- **标题**: 与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-047

通过标准：
1. type=positive, target=run_logs, must_contain="CAPABILITY_PROBE_DONE"
2. type=positive, target=run_logs, eval=llm_assisted
3. type=nonfunctional, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Probe docker daemon | `docker info 2>&1 | head -5 || echo "DOCKER_MISSING"` |  | ✅ GENUINE |
| 2 | Probe browsers | `which google-chrome 2>&1 || echo "CHROME_MISSING" which firefox 2>&1 || echo "FI` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Probe docker and browser capability
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Probe docker daemon
        run: |
          docker info 2>&1 | head -5 || echo "DOCKER_MISSING"
      - name: Probe browsers
        run: |
          which google-chrome 2>&1 || echo "CHROME_MISSING"
          which firefox 2>&1 || echo "FIREFOX_MISSING"
          echo "CAPABILITY_PROBE_DONE"
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
| 1 | run_logs | positive | must_contain=CAPABILITY_PROBE_DONE | ✅ GENUINE | CAPABILITY_PROBE_DONE: GENUINE |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---