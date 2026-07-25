# SEC-PERM-01-001

- 标题: 显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 permissions 声明
操作步骤:
  1. 1. 提交一个 workflow，在 job 级显式声明 repository: read
  2. 2. 触发 workflow 并尝试执行写操作
预期结果:
  - 声明 read 时读操作成功
  - 声明 read 时写操作返回 403 或失败

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt write | curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/${{ atomgit.repository }}/issues" \n            ... | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_logs equals: read_operations_successful | UNCOVERED | 期望值 [read_operations_successful] 未在任何步骤输出中找到 |
| [negative] run_logs must_not_contain: write_permission_granted | UNCOVERED | 期望值 [write_permission_granted] 未在任何步骤输出中找到 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [read_operations_successful] 未在任何步骤输出中找到
- **断言 2 - MISSING_SOURCE**: 期望值 [write_permission_granted] 未在任何步骤输出中找到

---
