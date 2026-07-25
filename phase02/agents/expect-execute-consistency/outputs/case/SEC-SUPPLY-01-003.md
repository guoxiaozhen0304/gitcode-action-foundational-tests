# SEC-SUPPLY-01-003

- 标题: 第三方 Action 来源应具备信任边界（typosquatting 限制）
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库可引用外部 Action
操作步骤:
  1. 1. 提交一个 workflow，引用一个与官方 Action 名称高度相似的 Action
  2. 2. 触发 workflow
预期结果:
  - 系统不应静默解析 typosquatting 名称为合法来源
  - 首次使用未审核 Action 时应触发警告或需审批

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use typo action | uses: checkout-action@v1 | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status must_not_equal: success | COVERED | 步骤含实际命令/action，失败状态取决于真实执行 |
| [positive] run_logs equals: action_not_found_or_unapproved | COVERED | 期望值可能来自 action 内部日志输出: checkout-action@v1 |

### 问题

- 无

---
