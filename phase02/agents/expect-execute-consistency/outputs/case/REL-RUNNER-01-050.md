# REL-RUNNER-01-050

- **标题**: 架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-074

通过标准：
1. type=positive, target=x64_job_arch, equals=x86_64
2. type=positive, target=arm64_job_arch, equals=aarch64
3. type=positive, target=arch_mismatch_count, equals=0
4. type=negative, target=x64_job_arch, equals=aarch64
5. type=nonfunctional, target=no_matching_runner_behavior, equals=queued_or_explicit_error

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | print arch step | `echo "declared=x64 actual=$(uname -m)"` |  | ❌ VACUOUS |
| 2 | print arch step | `echo "declared=arm64 actual=$(uname -m)"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  x64_probe:
    name: x64 arch probe job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: print arch step
        run: |
          echo "declared=x64 actual=$(uname -m)"
  arm64_probe:
    name: arm64 arch probe job
    runs-on: [ubuntu-latest, arm64, small]
    steps:
      - name: print arch step
        run: |
          echo "declared=arm64 actual=$(uname -m)"
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
| 1 | x64_job_arch | positive | equals=x86_64 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | arm64_job_arch | positive | equals=aarch64 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | arch_mismatch_count | positive | equals=0 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | x64_job_arch | negative | equals=aarch64 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 5 | no_matching_runner_behavior | nonfunctional | equals=queued_or_explicit_error | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 5 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---