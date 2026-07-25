# USE-ACT-01-001

- 标题: 使用裸插件名 checkout 时正常拉取官方 Action
- 维度: usability/compatibility | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - GitCode 官方插件市场可用
操作步骤:
  1. 1. 在 step 中写 uses: checkout
预期结果:
  官方 Action 被正确拉取并执行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | verify checkout | ls -la  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_status equals: COMPLETED | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |

### 问题

- 无

---
