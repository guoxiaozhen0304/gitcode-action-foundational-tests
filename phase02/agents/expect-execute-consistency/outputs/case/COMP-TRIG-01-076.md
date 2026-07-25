# COMP-TRIG-01-076

- 标题: issue_comment 事件关键字段与 types 验证
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-076
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-075~083
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      issue_comment 事件关键字段与 types 验证

前置条件:
  - 仓库已启用 AtomGit Action
  - 存在 Issue

操作步骤:
  1. 配置 issue_comment 触发并定义 types
  2. 创建评论验证触发和字段

预期结果:
  - issue_comment 事件触发 workflow，types 允许 created / edited / deleted，atomgit.event.comment 和 issue 字段可访问

验证点:
  - [正向] issue 评论创建时触发
  - [正向] event.comment.id 非空
  - [正向] event.issue.number 非空

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print comment fields | run: echo "COMMENT_ID=${{ atomgit.event.comment.id }}"
echo "ISSUE_NUM=${{ atomgit.event.issue.number }}"
echo "issue_comment_ok"
 | 是 |

<details><summary>完整 workflow YAML</summary>

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

| 字段 | 值 |
|------|----|
| 触发事件 | issue_comment |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] issue 评论创建时触发 | 🚫 BLOCKED | trigger=issue_comment |
| [正向] event.comment.id 非空 | 🚫 BLOCKED | trigger=issue_comment |
| [正向] event.issue.number 非空 | 🚫 BLOCKED | trigger=issue_comment |

### 问题

- [正向] issue 评论创建时触发: BLOCKED - trigger=issue_comment
- [正向] event.comment.id 非空: BLOCKED - trigger=issue_comment
- [正向] event.issue.number 非空: BLOCKED - trigger=issue_comment

---
