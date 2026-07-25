# SEC-CACHE-01-002

- 标题: 主仓 cache restore 对 fork cache miss
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-CACHE-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-018
参照来源:  inputs/gitcode-spec/core-concepts/artifacts-and-cache.md
母意图:    SEC-CACHE-01-001
标题:      主仓 cache restore 对 fork cache miss

前置条件:
  - fork PR 已写入 cache

操作步骤:
  1. 在主仓触发 workflow，使用与 fork PR 相同的 cache key 尝试 restore
  2. 查看 restore 结果

预期结果:
  - cache restore 结果为 miss
  - 日志中显示未找到对应缓存

验证点:
  - [负向] 主仓绝不应命中 fork PR 的缓存
  - [正向] cache restore 返回 miss

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Restore cache (cache-restore) | cache | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 主仓绝不应命中 fork PR 的缓存 | 覆盖 | real logic exists for negative verification |
| cache restore 返回 miss | 覆盖 | log assertion without specific string check |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore | negative |  | CONSISTENT | real logic exists for negative verification |
| 2 | run_logs | positive | cache_miss | CONSISTENT | log assertion without specific string check |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
