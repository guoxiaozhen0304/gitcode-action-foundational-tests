# COMP-ISOLATION-01-003

- **标题**: container.volumes 常规挂载在托管 Runner 的行为记录
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**container.volumes 常规挂载在托管 Runner 的行为记录**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-025

通过标准：
1. type=nonfunctional, target=container_handling, eval=llm_assisted
2. type=negative, target=silent_ignore, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Probe container env | `echo "CONTAINER_PROBE_OK" touch /cache/probe_marker && echo "VOLUME_WRITE_OK"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  contained:
    name: Run in container with volume
    runs-on: [ubuntu-latest, x64, small]
    container:
      image: ubuntu:22.04
      volumes:
        - /tmp/build-cache:/cache
    steps:
      - name: Probe container env
        run: |
          echo "CONTAINER_PROBE_OK"
          touch /cache/probe_marker && echo "VOLUME_WRITE_OK"
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
| 1 | container_handling | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | silent_ignore | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---