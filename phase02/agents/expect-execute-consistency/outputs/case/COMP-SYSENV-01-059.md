# COMP-SYSENV-01-059

- **标题**: ATOMGIT 系统环境变量关键变量存在性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**ATOMGIT 系统环境变量关键变量存在性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-059

通过标准：
1. type=positive, target=run_logs, must_contain="SHA_SET=yes"
2. type=positive, target=run_logs, must_contain="REF_SET=yes"
3. type=positive, target=run_logs, must_contain="EVENT_NAME_SET=yes"
4. type=positive, target=run_logs, must_contain="WORKSPACE_SET=yes"
5. type=positive, target=run_logs, must_contain="REPO_SET=yes"
6. type=positive, target=run_logs, must_contain="RUN_ID_SET=yes"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Check critical vars | `echo "SHA_SET=$([ -n "$ATOMGIT_SHA" ] && echo yes || echo no)" echo "REF_SET=$([` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify ATOMGIT env presence
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check critical vars
        run: |
          echo "SHA_SET=$([ -n "$ATOMGIT_SHA" ] && echo yes || echo no)"
          echo "REF_SET=$([ -n "$ATOMGIT_REF" ] && echo yes || echo no)"
          echo "REF_NAME_SET=$([ -n "$ATOMGIT_REF_NAME" ] && echo yes || echo no)"
          echo "EVENT_NAME_SET=$([ -n "$ATOMGIT_EVENT_NAME" ] && echo yes || echo no)"
          echo "WORKSPACE_SET=$([ -n "$ATOMGIT_WORKSPACE" ] && echo yes || echo no)"
          echo "REPO_SET=$([ -n "$ATOMGIT_REPOSITORY" ] && echo yes || echo no)"
          echo "RUN_ID_SET=$([ -n "$ATOMGIT_RUN_ID" ] && echo yes || echo no)"
          echo "RUN_NUM_SET=$([ -n "$ATOMGIT_RUN_NUMBER" ] && echo yes || echo no)"
          echo "SERVER_SET=$([ -n "$ATOMGIT_SERVER_URL" ] && echo yes || echo no)"
          echo "API_SET=$([ -n "$ATOMGIT_API_URL" ] && echo yes || echo no)"
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
| 1 | run_logs | positive | must_contain=SHA_SET=yes | ❌ MISSING_SOURCE | SHA_SET=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=REF_SET=yes | ❌ MISSING_SOURCE | REF_SET=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=EVENT_NAME_SET=yes | ❌ MISSING_SOURCE | EVENT_NAME_SET=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 4 | run_logs | positive | must_contain=WORKSPACE_SET=yes | ❌ MISSING_SOURCE | WORKSPACE_SET=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 5 | run_logs | positive | must_contain=REPO_SET=yes | ❌ MISSING_SOURCE | REPO_SET=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 6 | run_logs | positive | must_contain=RUN_ID_SET=yes | ❌ MISSING_SOURCE | RUN_ID_SET=yes: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: SHA_SET=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: REF_SET=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 3 — MISSING_SOURCE**❌: EVENT_NAME_SET=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 4 — MISSING_SOURCE**❌: WORKSPACE_SET=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 5 — MISSING_SOURCE**❌: REPO_SET=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 6 — MISSING_SOURCE**❌: RUN_ID_SET=yes: MISSING_SOURCE (无步骤产出此字符串)

---