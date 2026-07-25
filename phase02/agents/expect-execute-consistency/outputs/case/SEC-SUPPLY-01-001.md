# SEC-SUPPLY-01-001

- 标题: 第三方 Action 引用应支持完整 commit hash 固定
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库可引用外部 Action
操作步骤:
  1. 1. 提交一个 workflow，使用完整 commit SHA 引用第三方 Action
  2. 2. 触发 workflow
预期结果:
  - 完整 commit SHA 引用可成功执行 action
  - commit SHA 不匹配时 job 应失败或拒绝执行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use pinned action | uses: docker/build-push-action@1234567890abcdef1234567890abcdef12345678 | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_status equals: success_or_action_executed | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |
| [negative] run_logs must_not_contain: unauthorized_action_execution | COVERED | 期望值可能来自 action 内部日志输出: docker/build-push-action@1234567890abcdef1234567890abcdef12345678 |

### 问题

- 无

---
