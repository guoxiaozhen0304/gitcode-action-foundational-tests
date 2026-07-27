# COMP-RERUN-01-001

- **标题**: rerun 后 atomgit.sha 保持原始值 run_number 递增
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**rerun 后 atomgit.sha 保持原始值 run_number 递增**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-009

通过标准：
1. type=positive, target=rerun_context
2. type=positive, target=rerun_context

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Dump context | `echo "sha=$ATOMGIT_SHA" echo "ref=$ATOMGIT_REF" echo "run_number=$ATOMGIT_RUN_NU` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify rerun context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Dump context
        run: |
          echo "sha=$ATOMGIT_SHA"
          echo "ref=$ATOMGIT_REF"
          echo "run_number=$ATOMGIT_RUN_NUMBER"
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
| 1 | rerun_context | positive |  | ✅ GENUINE | 通用断言匹配 |
| 2 | rerun_context | positive |  | ✅ GENUINE | 通用断言匹配 |

---