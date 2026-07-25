# COMPAT-TOKEN-01-002

- 标题: GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射
- 维度: 兼容性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射

- [负向] GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN
- [非功能] 报错信息应提示使用 ATOMGIT_TOKEN 替代

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use GITHUB_TOKEN for API call | STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${{ atomgit.repository | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_logs |  |
| nonfunctional | error_message |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN | COVERED | negative assertion present |
| [非功能] 报错信息应提示使用 ATOMGIT_TOKEN 替代 | WEAK | 1 real steps but no assertions |

### 问题

- [非功能] 报错信息应提示使用 ATOMGIT_TOKEN 替代: 1 real steps but no assertions

---
