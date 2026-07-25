# SEC-PERM-01-003

- 标题: 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库未配置 permissions 声明
操作步骤:
  1. 1. 提交一个未声明 permissions 的 workflow
  2. 2. 触发 workflow 并尝试执行写操作
预期结果:
  - 默认状态下 ATOMGIT_TOKEN 仅拥有仓库 read 权限
  - 写操作被平台拒绝

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt write without permissions | curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/${{ atomgit.repository }}/issues" \n            ... | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: write_permission_granted | UNCOVERED | 期望值 [write_permission_granted] 未在任何步骤输出中找到 |
| [positive] run_status equals: completed | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [write_permission_granted] 未在任何步骤输出中找到

---
