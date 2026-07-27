# COMP-ATOMGIT-01-049

- **标题**: atomgit 边界格式校验
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**atomgit 边界格式校验**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-049

通过标准：
1. type=positive, target=run_logs, must_contain="SHA_LEN=40"
2. type=positive, target=run_logs, must_contain="REF_PREFIX=refs"
3. type=positive, target=run_logs, must_contain="ACTOR_LEN="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Check formats | `echo "SHA_LEN=${#ATOMGIT_SHA}" echo "REF_PREFIX=${ATOMGIT_REF%%/*}" echo "REF_NA` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify atomgit boundary formats
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check formats
        run: |
          echo "SHA_LEN=${#ATOMGIT_SHA}"
          echo "REF_PREFIX=${ATOMGIT_REF%%/*}"
          echo "REF_NAME_NO_PREFIX=${ATOMGIT_REF_NAME#refs/}"
          echo "ACTOR_LEN=${#ATOMGIT_ACTOR}"
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
| 1 | run_logs | positive | must_contain=SHA_LEN=40 | ❌ MISSING_SOURCE | SHA_LEN=40: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=REF_PREFIX=refs | ❌ MISSING_SOURCE | REF_PREFIX=refs: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=ACTOR_LEN= | ❌ VACUOUS | ACTOR_LEN=: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — MISSING_SOURCE**❌: SHA_LEN=40: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: REF_PREFIX=refs: MISSING_SOURCE (无步骤产出此字符串)

**断言 3 — VACUOUS**❌: ACTOR_LEN=: VACUOUS (步骤仅 echo，未执行功能)

---