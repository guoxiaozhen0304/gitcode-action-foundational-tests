# COMP-SYSENV-01-060

- **标题**: ATOMGIT 系统环境变量值正确性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**ATOMGIT 系统环境变量值正确性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-059

通过标准：
1. type=positive, target=run_logs, must_contain="SHA_MATCH=yes"
2. type=positive, target=run_logs, must_contain="REF_MATCH=yes"
3. type=positive, target=run_logs, must_contain="EVENT_MATCH=yes"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Compare values | `echo "SHA_MATCH=$([ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ] && echo yes || echo ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify ATOMGIT env values
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare values
        run: |
          echo "SHA_MATCH=$([ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ] && echo yes || echo no)"
          echo "REF_MATCH=$([ "$ATOMGIT_REF" = "${{ atomgit.ref }}" ] && echo yes || echo no)"
          echo "EVENT_MATCH=$([ "$ATOMGIT_EVENT_NAME" = "${{ atomgit.event_name }}" ] && echo yes || echo no)"
          echo "REPO_MATCH=$([ "$ATOMGIT_REPOSITORY" = "${{ atomgit.repository }}" ] && echo yes || echo no)"
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
| 1 | run_logs | positive | must_contain=SHA_MATCH=yes | ❌ MISSING_SOURCE | SHA_MATCH=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=REF_MATCH=yes | ❌ MISSING_SOURCE | REF_MATCH=yes: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=EVENT_MATCH=yes | ❌ MISSING_SOURCE | EVENT_MATCH=yes: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: SHA_MATCH=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: REF_MATCH=yes: MISSING_SOURCE (无步骤产出此字符串)

**断言 3 — MISSING_SOURCE**❌: EVENT_MATCH=yes: MISSING_SOURCE (无步骤产出此字符串)

---