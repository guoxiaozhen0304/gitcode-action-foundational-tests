# REL-IMAGE-01-052-V2

- **标题**: 镜像拉取性能——5GB 自定义 container 环境准备耗时基准
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**镜像拉取性能——5GB 自定义 container 环境准备耗时基准**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-052

通过标准：
1. type=nonfunctional, target=image_pull_time_seconds
2. type=positive, target=job_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | check environment | `python --version` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: image pull 5GB test
    runs-on: [ubuntu-latest, x64, small]
    container:
      image: pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
    steps:
      - name: check environment
        run: |
          python --version
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
| 1 | image_pull_time_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | job_status | positive | equals=success | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---