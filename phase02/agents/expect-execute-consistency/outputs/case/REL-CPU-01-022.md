# REL-CPU-01-022

- **标题**: Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-022

通过标准：
1. type=positive, target=job_status, equals=success
2. type=nonfunctional, target=job_duration_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | burn 4 CPU processes | `for i in 1 2 3 4; do python3 -c "import time; end=time.time()+60; [x*x for x in ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: CPU saturate test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: burn 4 CPU processes
        run: |
          for i in 1 2 3 4; do python3 -c "import time; end=time.time()+60; [x*x for x in range(10000)] while time.time()<end" & done
          wait
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
| 1 | job_status | positive | equals=success | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |
| 2 | job_duration_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---