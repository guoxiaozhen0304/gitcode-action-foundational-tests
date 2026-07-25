# SEC-ENV-01-002

- 标题: 环境级 secret 审批前 workflow 不可读取
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了环境级 secret PROD_TOKEN
  - 环境审批规则已启用，尚未审批
操作步骤:
  1. 1. 提交一个引用环境级 secret 的 workflow
  2. 2. 在审批前触发 workflow
预期结果:
  - workflow job 无法读取到环境 secret 的值
  - job 应处于挂起或失败状态

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Try use env secret | if [ -z "$PROD_TOKEN" ]; then   echo "secret not accessible before approval" else   echo "secret accessible unexpectedly"   exit 1 fi  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: secret accessible unexpectedly | COVERED | 步骤 [Try use env secret] 执行真实功能时输出该值 |
| [positive] run_status equals: pending_or_failed | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |

### 问题

- 无

---
