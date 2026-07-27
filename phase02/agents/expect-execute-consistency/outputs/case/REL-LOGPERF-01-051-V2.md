# REL-LOGPERF-01-051-V2

- **标题**: 日志加载性能——200MB 日志下载与查看耗时
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**日志加载性能——200MB 日志下载与查看耗时**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-051

通过标准：
1. type=nonfunctional, target=download_time_seconds
2. type=positive, target=log_integrity, equals=100%

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate 200MB log | `for i in $(seq 1 200000); do echo LOG_LINE_${{i}} $(date +%s%N); done` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: log perf 200MB test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: generate 200MB log
        run: |
          for i in $(seq 1 200000); do echo LOG_LINE_${{i}} $(date +%s%N); done
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
| 1 | download_time_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | log_integrity | positive | equals=100% | ✅ GENUINE | 断言有条件可被步骤验证 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---