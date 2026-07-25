# USE-PERM-01-001

- 标题: 使用 GitCode 权限域命名时正常生效
- 维度: usability/compatibility | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库已配置权限
操作步骤:
  1. 1. 在 workflow 中使用 permissions: repository: read
预期结果:
  权限声明被正确解析，运行成功

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout | uses: checkout | 是 |

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
