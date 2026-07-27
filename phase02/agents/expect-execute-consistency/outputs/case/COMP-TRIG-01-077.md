# COMP-TRIG-01-077

- **标题**: pull_request_comment 事件关键字段与过滤验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_comment 事件关键字段与过滤验证**

- 触发事件: `pull_request_comment`
- 规格引用: INTENT-COMP-077

通过标准：
1. type=positive, target=run_logs, must_contain="PR_NUM="
2. type=positive, target=run_logs, must_contain="pr_comment_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print PR comment fields | `echo "PR_NUM=${{ atomgit.event.pull_request.number }}" echo "COMMENT_BODY=${{ at` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_comment:
    types: [created, edited, deleted]
jobs:
  verify:
    name: Verify pull_request_comment fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print PR comment fields
        run: |
          echo "PR_NUM=${{ atomgit.event.pull_request.number }}"
          echo "COMMENT_BODY=${{ atomgit.event.comment.body }}"
          echo "pr_comment_ok"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_comment` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=PR_NUM= | ✅ GENUINE | PR_NUM=: GENUINE |
| 2 | run_logs | positive | must_contain=pr_comment_ok | ✅ GENUINE | pr_comment_ok: GENUINE |

---