# SEC-PRTGT-01-002

- 标题: pull_request_target 无审批不执行 fork PR 代码
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自外部 fork 的 PR
操作步骤:
  1. 1. 在 base 分支 workflow 中使用 pull_request_target 触发
  2. 2. 显式 checkout fork PR 的 head sha
  3. 3. 在无审批状态下触发 workflow
预期结果:
  - 未审批状态下 job 应处于挂起或拒绝态
  - 不应直接执行 fork PR 的代码

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Checkout PR head | uses: checkout | 是 |
| 2 | Run build | echo "Building PR code"  | 否 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status must_not_equal: success_without_approval | TRIGGER_BLOCKED | 触发事件 pull_request_target 无法通过 dispatch API 调度 |
| [positive] run_status equals: pending_or_blocked | TRIGGER_BLOCKED | 触发事件 pull_request_target 无法通过 dispatch API 调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request_target 无法通过 dispatch API 调度
- **断言 2 - TRIGGER_BLOCKED**: 触发事件 pull_request_target 无法通过 dispatch API 调度

---
