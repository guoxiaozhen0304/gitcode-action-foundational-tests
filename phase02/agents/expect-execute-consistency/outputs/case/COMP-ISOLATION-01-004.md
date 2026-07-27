# COMP-ISOLATION-01-004

- **标题**: 托管 Runner 上特权 options 与敏感路径挂载的边界核查
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**托管 Runner 上特权 options 与敏感路径挂载的边界核查**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-025

通过标准：
1. type=negative, target=run_logs, must_contain="HOST_ROOT_READABLE"
2. type=negative, target=privilege_boundary, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Probe host access | `if [ -d /host-root/etc ]; then echo "HOST_ROOT_READABLE"; else echo "HOST_ROOT_B` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  escalate:
    name: Probe privileged container boundary
    runs-on: [ubuntu-latest, x64, small]
    container:
      image: ubuntu:22.04
      options: --privileged --network=host
      volumes:
        - /:/host-root
    steps:
      - name: Probe host access
        run: |
          if [ -d /host-root/etc ]; then echo "HOST_ROOT_READABLE"; else echo "HOST_ROOT_BLOCKED"; fi
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
| 1 | run_logs | negative | must_contain=HOST_ROOT_READABLE | ✅ GENUINE | HOST_ROOT_READABLE: GENUINE |
| 2 | privilege_boundary | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---