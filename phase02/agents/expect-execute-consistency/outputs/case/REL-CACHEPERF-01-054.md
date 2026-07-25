# REL-CACHEPERF-01-054

- 标题: 缓存加速比——cache 命中 vs 未命中构建耗时对比
- 维度: 稳定性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 缓存加速比——cache 命中 vs 未命中构建耗时对比

- [正向] 加速比≥2x
- [负向] cache 命中后不应仍执行完整安装

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | restore cache | uses: cache | Y |
| 2 | install deps | npm ci || true | - |
| 3 | save cache | uses: cache | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| nonfunctional | speedup_ratio |  |
| nonfunctional | restore_time_seconds |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 加速比≥2x | WEAK | 2 real steps but no assertions |
| [负向] cache 命中后不应仍执行完整安装 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 加速比≥2x: 2 real steps but no assertions
- [负向] cache 命中后不应仍执行完整安装: single dispatch cannot prove negative

---
