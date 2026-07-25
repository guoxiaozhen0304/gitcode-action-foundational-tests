# COMP-TRIG-01-073

- 标题: pull_request 事件关键字段与 types 验证
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-073
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-061~083
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      pull_request 事件关键字段与 types 验证

前置条件:
  - 仓库已启用 AtomGit Action
  - 存在可触发 PR 的条件

操作步骤:
  1. 配置 pull_request 触发并定义 types 和 branches
  2. 创建或更新 PR 验证触发

预期结果:
  - pull_request 事件触发 workflow，types 过滤生效，branches 过滤目标分支，atomgit.event.pull_request 各字段可访问

验证点:
  - [正向] PR 创建时触发 workflow
  - [正向] event.pull_request.number 非空
  - [正向] types 仅匹配指定类型

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print PR fields | run: echo "PR_NUM=${{ atomgit.event.pull_request.number }}"
echo "PR_TITLE=${{ atomgit.event.pull_request.title }}"
echo "PR_STATE=${{ atomgit.event.pull_r | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    types: [open, update, reopen]
    branches: [main]
jobs:
  verify:
    name: Verify pull_request event fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print PR fields
        run: |
          echo "PR_NUM=${{ atomgit.event.pull_request.number }}"
          echo "PR_TITLE=${{ atomgit.event.pull_request.title }}"
          echo "PR_STATE=${{ atomgit.event.pull_request.state }}"
          echo "pr_ok"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] PR 创建时触发 workflow | 🚫 BLOCKED | trigger=pull_request |
| [正向] event.pull_request.number 非空 | 🚫 BLOCKED | trigger=pull_request |
| [正向] types 仅匹配指定类型 | 🚫 BLOCKED | trigger=pull_request |

### 问题

- [正向] PR 创建时触发 workflow: BLOCKED - trigger=pull_request
- [正向] event.pull_request.number 非空: BLOCKED - trigger=pull_request
- [正向] types 仅匹配指定类型: BLOCKED - trigger=pull_request

---
