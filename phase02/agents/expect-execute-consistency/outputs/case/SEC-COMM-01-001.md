# SEC-COMM-01-001

- 标题: issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过
- 维度: 安全性 | 优先级: P0
- 评级: BLOCKED

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-COMM-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-026
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过

前置条件:
  - 仓库配置了评论触发 workflow

操作步骤:
  1. 提交一个由 issue_comment 触发的 workflow，配置关键字过滤
  2. 提交一条将关键字伪装在 markdown 代码块中的评论

预期结果:
  - 伪装在代码块或注释中的关键字绝不应触发 workflow
  - 触发记录应包含评论原始内容哈希，用于审计

验证点:
  - [负向] 伪装在代码块或注释中的关键字绝不应触发 workflow
  - [非功能] 触发记录应包含评论原始内容哈希，用于审计

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Check trigger (comment-filter) | echo "Triggered by comment"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | issue_comment |
| as | untrusted_contributor |
| fault_injection | None |

## 4. 规格 vs 实现对照

### 问题

- 触发事件 `issue_comment` 无 dispatch API，无法在自动化框架中验证

---
