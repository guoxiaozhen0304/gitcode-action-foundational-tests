# SEC-PRTGT-01-001

- 标题: pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自外部 fork 的 PR
操作步骤:
  1. 1. 在 base 分支 workflow 中使用 pull_request_target 触发
  2. 2. 显式 checkout fork PR 的 head sha 并执行脚本
  3. 3. 观察 secrets 是否可被该脚本访问
预期结果:
  - 系统应阻止或限制在 pull_request_target 中直接执行未经审核的 fork PR 代码
  - secrets 不应被不可信代码直接读取

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Checkout PR head | uses: checkout | 是 |
| 2 | Attempt secret access | echo "secret is ${{ secrets.DEPLOY_TOKEN }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN | TRIGGER_BLOCKED | 触发事件 pull_request_target 无法通过 dispatch API 调度 |
| [positive] run_status equals: blocked_or_pending | TRIGGER_BLOCKED | 触发事件 pull_request_target 无法通过 dispatch API 调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request_target 无法通过 dispatch API 调度
- **断言 2 - TRIGGER_BLOCKED**: 触发事件 pull_request_target 无法通过 dispatch API 调度

---
