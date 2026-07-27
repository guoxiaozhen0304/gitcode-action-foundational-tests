# USE-ENV-01-001

- **标题**: 使用 ATOMGIT_SHA 环境变量时正常取值
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**使用 ATOMGIT_SHA 环境变量时正常取值**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-003

通过标准：
1. type=positive, target=run_logs, contains="sha="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo ATOMGIT_SHA | `echo "sha=$ATOMGIT_SHA"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-env:
    name: test ATOMGIT env var
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo ATOMGIT_SHA
        run: |
          echo "sha=$ATOMGIT_SHA"
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
| 1 | run_logs | positive | contains=sha= | ❌ VACUOUS | sha=: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — VACUOUS**❌: sha=: VACUOUS (步骤仅 echo，未执行功能)

---