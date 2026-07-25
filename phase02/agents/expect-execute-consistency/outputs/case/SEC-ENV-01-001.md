# SEC-ENV-01-001

- 标题: 环境级 secret 必须经审批后才能被 workflow 访问
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了环境级 secret PROD_TOKEN
  - 环境审批规则已启用
操作步骤:
  1. 1. 提交一个引用环境级 secret 的 workflow
  2. 2. 在审批前触发 workflow
  3. 3. 审批后再次触发 workflow
预期结果:
  - 审批前 workflow 无法读取到环境 secret 的值
  - 审批后 secret 可被正常引用，job 成功执行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use env secret | echo "secret length is ${#PROD_TOKEN}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_status equals: success_after_approval | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |
| [negative] run_logs must_not_contain_secret: PROD_TOKEN | COVERED | 步骤使用了 PROD_TOKEN，平台需在日志中脱敏 |

### 问题

- 无

---
