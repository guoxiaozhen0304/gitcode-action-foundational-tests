# USE-DISP-01-003

- **标题**: workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-051

通过标准：
1. type=positive, target=ui, eval=deterministic
2. type=negative, target=ui, eval=deterministic
3. type=nonfunctional, target=ui, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | marker step | `echo "dispatched"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: "target env"
        required: true
        default: "staging"
      version:
        description: "release version"
        required: false
      dry_run:
        description: "dry run flag"
        required: false
        default: "true"
      approver:
        description: "approver name"
        required: true
      notes:
        description: "extra notes"
        required: false
jobs:
  deploy:
    name: dispatch inputs probe
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: marker step
        run: |
          echo "dispatched"
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
| 1 | ui | positive | eval=deterministic | ✅ GENUINE | 通用断言匹配 |
| 2 | ui | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |
| 3 | ui | nonfunctional | eval=deterministic | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---