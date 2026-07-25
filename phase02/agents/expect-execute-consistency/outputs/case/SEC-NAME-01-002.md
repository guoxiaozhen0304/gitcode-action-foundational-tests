# SEC-NAME-01-002

- 标题: 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret API_KEY
操作步骤:
  1. 1. 提交一个 workflow，执行 printenv 或读取 /proc/self/environ
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - printenv 输出到日志时，secret 值必须被脱敏
  - 即使通过 env | grep 过滤，过滤后的值也应被脱敏

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Run printenv | printenv \| grep API_KEY \|\| echo not found  | 是 |
| 2 | Read proc environ | cat /proc/self/environ \| tr '\0' '\n' \| grep API_KEY \|\| echo not found  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: API_KEY | COVERED | 步骤使用了 API_KEY，平台需在日志中脱敏 |
| [positive] run_logs equals: masked_or_not_found | UNCOVERED | 期望值 [masked_or_not_found] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [masked_or_not_found] 未在任何步骤输出中找到

---
