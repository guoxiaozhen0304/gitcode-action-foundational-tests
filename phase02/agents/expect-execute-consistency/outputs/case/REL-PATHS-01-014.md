# REL-PATHS-01-014

- 标题: paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效

- [正向] workflow 运行被创建
- [负向] 不应因文件数=300 而判定异常

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo triggered | echo triggered by paths | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed(success) |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | push |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] workflow 运行被创建 | WEAK | assertions present but all steps trivial |
| [负向] 不应因文件数=300 而判定异常 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] workflow 运行被创建: assertions present but all steps trivial
- [负向] 不应因文件数=300 而判定异常: single dispatch cannot prove negative

---
