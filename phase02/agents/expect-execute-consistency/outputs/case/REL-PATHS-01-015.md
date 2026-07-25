# REL-PATHS-01-015

- 标题: paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断

- [正向] workflow 不触发
- [负向] 第 301 个文件不应触发 workflow

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo triggered | echo triggered by paths | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | not_triggered |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | push |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] workflow 不触发 | WEAK | assertions present but all steps trivial |
| [负向] 第 301 个文件不应触发 workflow | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] workflow 不触发: assertions present but all steps trivial
- [负向] 第 301 个文件不应触发 workflow: single dispatch cannot prove negative

---
