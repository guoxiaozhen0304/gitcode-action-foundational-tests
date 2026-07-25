# SEC-SUPPLY-01-002

- 标题: commit hash 不匹配时第三方 Action 应被拒绝执行
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库可引用外部 Action
操作步骤:
  1. 1. 提交一个 workflow，使用一个不存在的 commit SHA 引用 Action
  2. 2. 触发 workflow
预期结果:
  - job 进入失败状态或明确拒绝执行
  - 系统不应静默回退到分支 HEAD

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use invalid hash action | uses: docker/build-push-action@0000000000000000000000000000000000000000 | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status must_not_equal: success | COVERED | 步骤含实际命令/action，失败状态取决于真实执行 |
| [positive] run_logs equals: action_not_found_or_sha_mismatch | COVERED | 期望值可能来自 action 内部日志输出: docker/build-push-action@0000000000000000000000000000000000000000 |

### 问题

- 无

---
