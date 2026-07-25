# USE-TYPE-01-001

- 标题: 使用 GitCode types 命名时正常触发
- 维度: 易用性 | 优先级: P1
- 评级: BLOCKED

---

## 1. 想测什么（规格）

```
用例 ID:   USE-TYPE-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-009
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      使用 GitCode types 命名时正常触发

前置条件:
  - 仓库存在 PR

操作步骤:
  1. 配置 on: pull_request: types: [open, update, reopen]

预期结果:
  PR 事件正常触发 workflow

验证点:
  - [正向] PR 创建或更新时触发运行
  - [正向] 运行成功或至少进入执行态

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo event (test-types) | echo "event=${{ atomgit.event_name }}"  | GENUINE |

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
