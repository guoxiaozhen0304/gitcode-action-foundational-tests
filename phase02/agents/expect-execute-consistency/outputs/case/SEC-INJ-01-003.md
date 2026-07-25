# SEC-INJ-01-003

- 标题: 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 存在一条包含 shell 元字符的评论
操作步骤:
  1. 1. 提交一个由 issue_comment 触发的 workflow，在 run 中引用评论 body
  2. 2. 提交一条含 shell 元字符的评论触发 workflow
预期结果:
  - 评论 body 中的 shell 元字符不应被解释为命令执行
  - 即使评论被编辑，重新触发时仍应维持安全过滤

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Inline comment body | echo "Comment is ${{ atomgit.event.comment.body }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | issue_comment |
| 触发身份 | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: injected_command_executed | TRIGGER_BLOCKED | 触发事件 issue_comment 无法通过 dispatch API 调度 |
| [positive] run_status equals: success | TRIGGER_BLOCKED | 触发事件 issue_comment 无法通过 dispatch API 调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发事件 issue_comment 无法通过 dispatch API 调度
- **断言 2 - TRIGGER_BLOCKED**: 触发事件 issue_comment 无法通过 dispatch API 调度

---
