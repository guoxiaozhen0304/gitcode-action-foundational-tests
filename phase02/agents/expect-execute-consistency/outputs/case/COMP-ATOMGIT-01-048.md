# COMP-ATOMGIT-01-048

- **标题**: atomgit 事件相关属性可访问性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**atomgit 事件相关属性可访问性**

- 触发事件: `push`
- 规格引用: INTENT-COMP-048

通过标准：
1. type=positive, target=run_logs, must_contain="EVENT_REF=refs/"
2. type=positive, target=run_logs, must_contain="BEFORE="
3. type=positive, target=run_logs, must_contain="AFTER="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print event properties | `echo "EVENT_REF=${{ atomgit.event.ref }}" echo "BEFORE=${{ atomgit.event.before ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  verify:
    name: Verify event properties on push
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print event properties
        run: |
          echo "EVENT_REF=${{ atomgit.event.ref }}"
          echo "BEFORE=${{ atomgit.event.before }}"
          echo "AFTER=${{ atomgit.event.after }}"
          echo "COMMITS_LEN=${{ atomgit.event.commits }}"
          echo "BASE_REF=${{ atomgit.event.base_ref }}"
          echo "CREATED=${{ atomgit.event.created }}"
          echo "DELETED=${{ atomgit.event.deleted }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=EVENT_REF=refs/ | ❌ MISSING_SOURCE | EVENT_REF=refs/: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=BEFORE= | ✅ GENUINE | BEFORE=: GENUINE |
| 3 | run_logs | positive | must_contain=AFTER= | ✅ GENUINE | AFTER=: GENUINE |

### 问题

**断言 1 — MISSING_SOURCE**❌: EVENT_REF=refs/: MISSING_SOURCE (无步骤产出此字符串)

---