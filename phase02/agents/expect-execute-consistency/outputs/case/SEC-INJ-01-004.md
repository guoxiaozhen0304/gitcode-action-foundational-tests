# SEC-INJ-01-004

- 标题: 不可信 commit message 不可直接插进 run 脚本导致命令注入
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 存在一条 commit message 含反引号或分号的 push
操作步骤:
  1. 1. 提交一个由 push 触发的 workflow，在 run 中引用 commit message
  2. 2. 推送一条含 shell 元字符的 commit
预期结果:
  - commit message 中的 shell 元字符不应被解释为命令执行
  - 安全写法（中间环境变量）应正常生效

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Inline commit message | echo "Message is ${{ atomgit.event.commits[0].message }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: injected_command_executed | TRIGGER_BLOCKED | 触发身份为 untrusted_contributor，无法调度 |
| [positive] run_status equals: success | TRIGGER_BLOCKED | 触发身份为 untrusted_contributor，无法调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发身份为 untrusted_contributor，无法调度
- **断言 2 - TRIGGER_BLOCKED**: 触发身份为 untrusted_contributor，无法调度

---
