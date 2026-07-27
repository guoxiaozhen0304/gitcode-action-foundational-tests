# COMP-WFLOW-01-065

- **标题**: workflow post 后处理阶段字段验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**workflow post 后处理阶段字段验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-061

通过标准：
1. type=positive, target=run_logs, must_contain="main_done"
2. type=positive, target=run_logs, must_contain="post_done"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Main step | `echo "main_done"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Main job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Main step
        run: |
          echo "main_done"
post:
  run_always: true
  steps:
    - name: Post notification
      run: |
        echo "post_done"
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
| 1 | run_logs | positive | must_contain=main_done | ❌ VACUOUS | main_done: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | must_contain=post_done | ❌ MISSING_SOURCE | post_done: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — VACUOUS**❌: main_done: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — MISSING_SOURCE**❌: post_done: MISSING_SOURCE (无步骤产出此字符串)

---