# SEC-TOKEN-01-001

- 标题: fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- 维度: 安全性 | 优先级: P0
- 评级: BLOCKED

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-TOKEN-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-003
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限

前置条件:
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以 fork 贡献者身份提交一个使用 ATOMGIT_TOKEN 克隆代码的 workflow
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - ATOMGIT_TOKEN 可成功执行 clone 等读操作
  - 尝试写操作时被平台强制拒绝

验证点:
  - [正向] ATOMGIT_TOKEN 可成功执行 clone 等读操作
  - [负向] 尝试写操作应返回 403 或失败

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Clone with token (token-read) | git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git test | GENUINE |
| 2 | Attempt write via API (token-read) | curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/$ | GENUINE |

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
