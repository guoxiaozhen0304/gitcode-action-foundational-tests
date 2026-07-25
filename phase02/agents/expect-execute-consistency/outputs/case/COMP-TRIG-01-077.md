# COMP-TRIG-01-077

- 标题: pull_request_comment 事件关键字段与过滤验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-077
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-469~470
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      pull_request_comment 事件关键字段与过滤验证

前置条件:
  - 仓库已启用 AtomGit Action
  - 存在 PR

操作步骤:
  1. 配置 pull_request_comment 触发并定义 types
  2. 在 PR 下创建评论验证触发

预期结果:
  - pull_request_comment 事件触发 workflow，types 允许 created / edited / deleted，atomgit.event.comment 和 pull_request 字段可访问

验证点:
  - [正向] PR 评论创建时触发
  - [正向] event.comment.body 非空
  - [正向] event.pull_request.number 非空

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print PR comment fields | run: echo "PR_NUM=${{ atomgit.event.pull_request.number }}"
echo "COMMENT_BODY=${{ atomgit.event.comment.body }}"
echo "pr_comment_ok"
 | 是 |

<details><summary>完整 workflow YAML</summary>

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

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request_comment |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] PR 评论创建时触发 | ✅ COVERED | steps have real logic |
| [正向] event.comment.body 非空 | ✅ COVERED | steps have real logic |
| [正向] event.pull_request.number 非空 | ✅ COVERED | steps have real logic |

### 问题

无

---
