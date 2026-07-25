# SEC-TOKEN-01-002

- 标题: fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- 维度: 安全性 | 优先级: P0
- 评级: BLOCKED

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-TOKEN-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-003
参照来源:  inputs/gitcode-spec/
母意图:    SEC-TOKEN-01-001
标题:      fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝

前置条件:
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以 fork 贡献者身份提交一个尝试用 ATOMGIT_TOKEN 推送代码的 workflow
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - 推送操作返回权限拒绝（403）
  - 运行日志中显示权限不足

验证点:
  - [负向] 写操作绝不应成功
  - [正向] 权限拒绝信息明确

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Attempt push (token-write-denied) | git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git repo | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | untrusted_contributor |
| fault_injection | None |

## 4. 规格 vs 实现对照

### 问题

- 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证

---
