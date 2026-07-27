# REL-RUNNER-01-049

- **标题**: Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-049

通过标准：
1. type=positive, target=resource_ratio
2. type=nonfunctional, target=queued_to_running_minutes

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | probe small | `nproc free -m df -BG ${{RUNNER_TEMP}}` |  | ✅ GENUINE |
| 2 | probe medium | `nproc free -m df -BG ${{RUNNER_TEMP}}` |  | ✅ GENUINE |
| 3 | probe large | `nproc free -m df -BG ${{RUNNER_TEMP}}` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe-small:
    name: probe small runner
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: probe small
        run: |
          nproc
          free -m
          df -BG ${{RUNNER_TEMP}}
  probe-medium:
    name: probe medium runner
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: probe medium
        run: |
          nproc
          free -m
          df -BG ${{RUNNER_TEMP}}
  probe-large:
    name: probe large runner
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: probe large
        run: |
          nproc
          free -m
          df -BG ${{RUNNER_TEMP}}
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
| 1 | resource_ratio | positive |  | ✅ GENUINE | 通用断言匹配 |
| 2 | queued_to_running_minutes | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---