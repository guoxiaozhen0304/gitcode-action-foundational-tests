# USE-TYPE-01-002

- 标题: 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示
- 维度: 易用性 | 优先级: P1
- 评级: BLOCKED

---

## 1. 想测什么（规格）

```
用例 ID:   USE-TYPE-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-009
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      使用 GitHub types 命名 opened/synchronize 时应给出可理解提示

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 配置 on: pull_request: types: [opened, synchronize]

预期结果:
  YAML 校验报错，列出 GitCode 支持的 types 取值，并给出 GitHub 对应关系

验证点:
  - [负向] 不应静默通过校验并在运行时永远不被触发
  - [非功能] 报错中应列出 merge/open/reopen/update 并指出对应关系

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo event (bad-types) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

### 问题

- 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证

---
