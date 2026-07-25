# SEC-TOCTOU-01-001

- 标题: 审批后推送新 commit 不应被已授权特权运行执行
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了审批触发 workflow
操作步骤:
  1. 1. 管理员审批一个 workflow 运行
  2. 2. 在审批后、执行前，攻击者推送恶意 commit
  3. 3. 观察特权运行是否执行了新 commit
预期结果:
  - 特权运行应绑定审批时刻的具体 commit SHA
  - 审批后推送的新 commit 不应被已授权的特权运行自动采用

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check commit SHA | echo "Running commit: ${{ atomgit.sha }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: unapproved_commit_executed | UNCOVERED | 期望值 [unapproved_commit_executed] 未在任何步骤输出中找到 |
| [positive] run_logs equals: approved_sha_matched | UNCOVERED | 期望值 [approved_sha_matched] 未在任何步骤输出中找到 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [unapproved_commit_executed] 未在任何步骤输出中找到
- **断言 2 - MISSING_SOURCE**: 期望值 [approved_sha_matched] 未在任何步骤输出中找到

---
