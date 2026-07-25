# COMPAT-PERM-01-001

- 标题: 未声明 permissions 时默认 TOKEN 读操作权限范围
- 维度: 兼容性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 未声明 permissions 时默认 TOKEN 读操作权限范围

- [正向] checkout step 成功完成
- [正向] 读操作（如 cat README）成功返回内容
- [负向] 读操作不应因权限不足而失败

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | read repo file | cat README.md | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
| positive | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] checkout step 成功完成 | COVERED | 1 real steps, assertions present |
| [正向] 读操作（如 cat README）成功返回内容 | COVERED | 1 real steps, assertions present |
| [负向] 读操作不应因权限不足而失败 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 读操作不应因权限不足而失败: single dispatch cannot prove negative

---
