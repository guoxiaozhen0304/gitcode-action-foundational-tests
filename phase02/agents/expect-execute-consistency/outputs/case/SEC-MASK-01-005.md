# SEC-MASK-01-005

- 标题: Secret 日志脱敏不可通过多行值输出绕过
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了多行 secret MULTI_LINE_SECRET
操作步骤:
  1. 1. 提交一个 workflow，直接 echo 多行 secret 到日志
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - 多行 secret 的每一行在日志中均被脱敏
  - 换行符不应成为脱敏边界

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo multiline secret | echo "${{ secrets.MULTI_LINE_SECRET }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: MULTI_LINE_SECRET | COVERED | 步骤使用了 MULTI_LINE_SECRET，平台需在日志中脱敏 |
| [positive] run_logs equals: multiline_masked_with_asterisks | UNCOVERED | 期望值 [multiline_masked_with_asterisks] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [multiline_masked_with_asterisks] 未在任何步骤输出中找到

---
