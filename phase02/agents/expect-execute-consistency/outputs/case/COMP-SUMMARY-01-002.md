# COMP-SUMMARY-01-002

- **标题**: summary 中不应暴露系统内部路径
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**summary 中不应暴露系统内部路径**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-018

通过标准：
1. type=negative, target=step_summary
2. type=negative, target=step_summary

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write safe summary | `echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify summary security
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write safe summary
        run: |
          echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"
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
| 1 | step_summary | negative |  | ✅ GENUINE | 步骤有 step_summary 输出，断言可观测 |
| 2 | step_summary | negative |  | ✅ GENUINE | 步骤有 step_summary 输出，断言可观测 |

---