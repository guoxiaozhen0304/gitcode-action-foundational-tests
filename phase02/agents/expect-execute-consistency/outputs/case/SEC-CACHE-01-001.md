# SEC-CACHE-01-001

- 标题: fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- 维度: 安全性 | 优先级: P0
- 评级: BLOCKED

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-CACHE-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-018
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      fork PR 写入的 cache 必须不可被主仓后续 workflow 读取

前置条件:
  - 仓库配置了 cache

操作步骤:
  1. 以 fork 贡献者身份提交一个写入 cache 的 workflow
  2. 在主仓提交一个读取相同 cache key 的 workflow

预期结果:
  - 主仓 workflow 的 cache restore 不应命中 fork PR 写入的缓存
  - 缓存键应带仓库级隔离前缀

验证点:
  - [负向] 主仓 workflow 在 fork PR 写入 cache 后，绝不应命中到该缓存
  - [非功能] 缓存命中率监控应显示跨仓库命中为 0

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Write cache (cache-write) | cache | GENUINE |

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
