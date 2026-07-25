# SEC-INJ-01-002

- 标题: 不可信分支名不可直接插进 run 脚本导致命令注入
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 存在一个分支名含 shell 元字符的 PR
操作步骤:
  1. 1. 提交一个 workflow，在 run 脚本中直接内联引用分支名
  2. 2. 触发该 workflow
预期结果:
  - 分支名中的特殊字符不应被解释为 shell 元字符
  - 表达式值应被安全求值

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Inline branch name | echo "Branch is ${{ atomgit.head_ref }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: injected_command_executed | TRIGGER_BLOCKED | 触发事件 pull_request 无法通过 dispatch API 调度 |
| [positive] run_status equals: success | TRIGGER_BLOCKED | 触发事件 pull_request 无法通过 dispatch API 调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度
- **断言 2 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度

---
