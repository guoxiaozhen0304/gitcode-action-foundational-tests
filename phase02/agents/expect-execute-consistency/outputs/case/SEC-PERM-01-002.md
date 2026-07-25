# SEC-PERM-01-002

- 标题: permissions 声明 read 时写操作被平台拒绝
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 permissions: repository: read
操作步骤:
  1. 1. 提交一个 workflow，job 级声明 repository: read
  2. 2. 触发 workflow 并执行 push 操作
预期结果:
  - push 操作返回 403 权限拒绝
  - token 的 effective scope 与声明一致

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Clone repo | git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git repo  | 是 |
| 2 | Attempt push | cd repo echo test > test.txt git add test.txt git commit -m test git push origin main \|\| echo push denied as expected  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: push_successful | UNCOVERED | 期望值 [push_successful] 未在任何步骤输出中找到 |
| [positive] run_logs equals: push_denied_or_403 | UNCOVERED | 期望值 [push_denied_or_403] 未在任何步骤输出中找到 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [push_successful] 未在任何步骤输出中找到
- **断言 2 - MISSING_SOURCE**: 期望值 [push_denied_or_403] 未在任何步骤输出中找到

---
