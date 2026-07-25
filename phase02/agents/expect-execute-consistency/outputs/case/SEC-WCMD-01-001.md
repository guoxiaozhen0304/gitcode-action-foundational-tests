# SEC-WCMD-01-001

- 标题: Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret API_KEY
操作步骤:
  1. 1. 提交一个 workflow，执行 add-mask 命令遮蔽 secret
  2. 2. 触发 workflow 并查看日志中命令的响应
预期结果:
  - workflow 命令的响应中绝不应包含被遮蔽前的 secret 原值
  - 命令执行日志应仅显示命令骨架，不含 payload

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Mask secret | echo "::add-mask::${{ secrets.API_KEY }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: API_KEY | COVERED | 步骤使用了 API_KEY，平台需在日志中脱敏 |
| [positive] run_logs equals: mask_command_without_payload | UNCOVERED | 期望值 [mask_command_without_payload] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [mask_command_without_payload] 未在任何步骤输出中找到

---
