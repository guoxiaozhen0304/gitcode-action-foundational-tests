# SEC-MASK-01-001

- 标题: Secret 值在运行日志中必须被自动脱敏为 ***
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
操作步骤:
  1. 1. 提交一个 workflow，在 run 步骤中直接 echo secrets.DEPLOY_TOKEN
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - 日志中 DEPLOY_TOKEN 的原值被替换为 ***
  - 日志全文搜索 DEPLOY_TOKEN 原值命中数为 0

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo secret directly | echo "The secret is ${{ secrets.DEPLOY_TOKEN }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN | COVERED | 步骤使用了 DEPLOY_TOKEN，平台需在日志中脱敏 |
| [positive] run_logs equals: masked_with_asterisks | UNCOVERED | 期望值 [masked_with_asterisks] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [masked_with_asterisks] 未在任何步骤输出中找到

---
