# COMP-TRIG-01-076

- **标题**: issue_comment 事件关键字段与 types 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**issue_comment 事件关键字段与 types 验证**

- 触发事件: `issue_comment`
- 规格引用: INTENT-COMP-076

通过标准：
1. type=positive, target=run_logs, must_contain="COMMENT_ID="
2. type=positive, target=run_logs, must_contain="issue_comment_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print comment fields | `echo "COMMENT_ID=${{ atomgit.event.comment.id }}" echo "ISSUE_NUM=${{ atomgit.ev` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created, edited, deleted]
jobs:
  verify:
    name: Verify issue_comment fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print comment fields
        run: |
          echo "COMMENT_ID=${{ atomgit.event.comment.id }}"
          echo "ISSUE_NUM=${{ atomgit.event.issue.number }}"
          echo "issue_comment_ok"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `issue_comment` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=COMMENT_ID= | ✅ GENUINE | COMMENT_ID=: GENUINE |
| 2 | run_logs | positive | must_contain=issue_comment_ok | ✅ GENUINE | issue_comment_ok: GENUINE |

---